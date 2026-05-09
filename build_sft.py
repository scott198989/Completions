"""SFT formatting layer for the HAVOC completions dataset.

The on-disk source format is canonical and is NOT modified by this script:
    {"prompt": ..., "completion": ...,
     "difficulty": ..., "task_type": ..., "response_style": ...}
(D_AC_Circuits.jsonl and D_Advanced_Eng_Math.jsonl carry only prompt+completion.)

This script reads every D_*.jsonl source, dedups on (prompt, completion), shuffles
deterministically, and writes train.jsonl / val.jsonl as one {"text": ...} record
per line.

Default text format:

    User: {prompt}
    Assistant: {completion}

With INCLUDE_METADATA=True (and the row carries all three metadata fields), the
record is prepended with conditioning lines:

    Difficulty: {difficulty}
    Task type: {task_type}
    Style: {response_style}
    User: {prompt}
    Assistant: {completion}

Rows missing any metadata field fall back to the default format even when
INCLUDE_METADATA=True.
"""

import json
import random
from pathlib import Path

ROOT = Path(__file__).parent
SOURCES = sorted(ROOT.glob("D_*.jsonl"))
TRAIN = ROOT / "train.jsonl"
VAL = ROOT / "val.jsonl"

SEED = 13
VAL_FRACTION = 0.10
INCLUDE_METADATA = False

META_KEYS = ("difficulty", "task_type", "response_style")


def format_row(row: dict, include_metadata: bool = INCLUDE_METADATA) -> str:
    parts = []
    if include_metadata and all(row.get(k) for k in META_KEYS):
        parts.append(f"Difficulty: {row['difficulty']}")
        parts.append(f"Task type: {row['task_type']}")
        parts.append(f"Style: {row['response_style']}")
    parts.append(f"User: {row['prompt']}")
    parts.append(f"Assistant: {row['completion']}")
    return "\n".join(parts)


def load_rows():
    seen = set()
    rows = []
    for src in SOURCES:
        with src.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                o = json.loads(line)
                key = (o["prompt"].strip(), o["completion"].strip())
                if key in seen:
                    continue
                seen.add(key)
                rows.append(o)
    return rows


def main():
    rows = load_rows()
    rng = random.Random(SEED)
    rng.shuffle(rows)

    cut = int(len(rows) * (1 - VAL_FRACTION))
    train_rows = rows[:cut]
    val_rows = rows[cut:]

    def dump(path, data):
        with path.open("w", encoding="utf-8") as out:
            for r in data:
                rec = {"text": format_row(r, INCLUDE_METADATA)}
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")

    dump(TRAIN, train_rows)
    dump(VAL, val_rows)

    print(f"sources:          {len(SOURCES)} files")
    print(f"after dedup:      {len(rows)}")
    print(f"include_metadata: {INCLUDE_METADATA}")
    print(f"train:            {len(train_rows)} -> {TRAIN.name}")
    print(f"val:              {len(val_rows)} -> {VAL.name}")


if __name__ == "__main__":
    main()
