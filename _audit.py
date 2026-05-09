"""One-shot audit: token counts, dupes, near-dupes, schema errors."""
import io
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import tiktoken

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).parent
ENC = tiktoken.get_encoding("cl100k_base")


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.lower().strip()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def shingles(s: str, n: int = 5):
    toks = s.split()
    if len(toks) < n:
        return frozenset([" ".join(toks)]) if toks else frozenset()
    return frozenset(" ".join(toks[i : i + n]) for i in range(len(toks) - n + 1))


def jaccard(a, b) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def audit_file(path: Path, near_threshold: float = 0.85):
    rows = []
    parse_errs = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                parse_errs.append((i, str(e), line[:120]))
                continue
            rows.append((i, obj, line))

    schema_issues = []
    valid = []
    for i, obj, raw in rows:
        if not isinstance(obj, dict):
            schema_issues.append((i, "not an object", raw[:120]))
            continue
        p = obj.get("prompt")
        c = obj.get("completion")
        if p is None or c is None:
            keys = sorted(obj.keys())
            schema_issues.append((i, f"missing prompt/completion; keys={keys}", raw[:120]))
            continue
        if not isinstance(p, str) or not isinstance(c, str):
            schema_issues.append((i, "prompt/completion not str", raw[:120]))
            continue
        if not p.strip() or not c.strip():
            schema_issues.append((i, "empty prompt or completion", raw[:120]))
            continue
        valid.append((i, obj, p, c))

    # Token count
    total_tokens = 0
    for _, _, p, c in valid:
        total_tokens += len(ENC.encode(p)) + len(ENC.encode(c))

    # Exact dupes (prompt+completion)
    seen = {}
    exact_dupes = []  # list of (kept_lineno, dup_lineno)
    for i, obj, p, c in valid:
        key = (p.strip(), c.strip())
        if key in seen:
            exact_dupes.append((seen[key], i))
        else:
            seen[key] = i

    # Prompt-only dupes (same prompt, different completion)
    prompt_index = defaultdict(list)
    for i, obj, p, c in valid:
        prompt_index[p.strip()].append((i, c))
    prompt_dupes = []
    for p, items in prompt_index.items():
        if len(items) > 1:
            uniq_completions = {c.strip() for _, c in items}
            if len(uniq_completions) > 1:
                prompt_dupes.append((p, items))

    # Near-dupes (jaccard on 5-shingles of normalized prompt)
    sigs = []
    for i, obj, p, c in valid:
        nrm = normalize(p)
        sh = shingles(nrm, n=5)
        sigs.append((i, p, sh))

    near = []
    # bucket by token presence to reduce comparisons; full O(n^2) on smaller files
    n = len(sigs)
    if n < 4000:
        for a in range(n):
            ia, pa, sa = sigs[a]
            if not sa:
                continue
            for b in range(a + 1, n):
                ib, pb, sb = sigs[b]
                if not sb:
                    continue
                # cheap prefilter
                small = min(len(sa), len(sb))
                if small == 0:
                    continue
                # quick token overlap upper bound
                if len(sa & sb) / max(len(sa), len(sb)) < near_threshold:
                    continue
                j = jaccard(sa, sb)
                if j >= near_threshold:
                    # exclude if exact
                    if pa.strip() == pb.strip():
                        continue
                    near.append((ia, ib, round(j, 3), pa[:80], pb[:80]))
    else:
        # bucketed by sorted shingle tokens hash
        buckets = defaultdict(list)
        for i, p, sh in sigs:
            if not sh:
                continue
            for s in sh:
                buckets[s].append((i, p, sh))
        seen_pair = set()
        for tok, items in buckets.items():
            if len(items) < 2 or len(items) > 200:
                continue
            for a in range(len(items)):
                ia, pa, sa = items[a]
                for b in range(a + 1, len(items)):
                    ib, pb, sb = items[b]
                    pair = (min(ia, ib), max(ia, ib))
                    if pair in seen_pair:
                        continue
                    seen_pair.add(pair)
                    j = jaccard(sa, sb)
                    if j >= near_threshold and pa.strip() != pb.strip():
                        near.append((ia, ib, round(j, 3), pa[:80], pb[:80]))

    return {
        "path": path.name,
        "rows_raw": len(rows),
        "rows_valid": len(valid),
        "tokens": total_tokens,
        "parse_errs": parse_errs,
        "schema_issues": schema_issues,
        "exact_dupes": exact_dupes,
        "prompt_dupes": prompt_dupes,
        "near_dupes": near,
    }


def main():
    files = sorted(p for p in ROOT.glob("*.jsonl") if p.stat().st_size > 0)
    grand_tokens = 0
    grand_rows = 0
    print(f"{'file':45s} {'rows':>7s} {'tokens':>10s} {'parse':>6s} {'schema':>7s} {'exact':>6s} {'pdup':>5s} {'near':>5s}")
    print("-" * 100)
    reports = []
    for p in files:
        r = audit_file(p)
        reports.append(r)
        grand_tokens += r["tokens"]
        grand_rows += r["rows_valid"]
        print(
            f"{r['path']:45s} {r['rows_valid']:7d} {r['tokens']:10d} "
            f"{len(r['parse_errs']):6d} {len(r['schema_issues']):7d} "
            f"{len(r['exact_dupes']):6d} {len(r['prompt_dupes']):5d} {len(r['near_dupes']):5d}"
        )
    print("-" * 100)
    print(f"{'TOTAL':45s} {grand_rows:7d} {grand_tokens:10d}")

    # Detail dump
    print("\n\n=== DETAILS ===\n")
    for r in reports:
        if r["parse_errs"] or r["schema_issues"] or r["exact_dupes"] or r["prompt_dupes"] or r["near_dupes"]:
            print(f"\n--- {r['path']} ---")
            for ln, msg, snippet in r["parse_errs"]:
                print(f"  PARSE_ERR L{ln}: {msg} :: {snippet}")
            for ln, msg, snippet in r["schema_issues"]:
                print(f"  SCHEMA   L{ln}: {msg} :: {snippet}")
            for kept, dup in r["exact_dupes"]:
                print(f"  EXACT    keep L{kept}, drop L{dup}")
            for prompt, items in r["prompt_dupes"]:
                lines = [str(i) for i, _ in items]
                print(f"  P-DUPE   L{','.join(lines)}: {prompt[:80]!r}")
            for ia, ib, j, pa, pb in r["near_dupes"]:
                print(f"  NEAR     L{ia} <-> L{ib} (j={j})")
                print(f"           A: {pa!r}")
                print(f"           B: {pb!r}")


if __name__ == "__main__":
    main()
