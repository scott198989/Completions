"""Label prompt/completion JSONL files with difficulty, domain, task_type, response_style.

Produces two outputs per input:
  <name>_labeled.jsonl     — original fields + tag fields
  <name>_conditioned.jsonl — tags injected into prompt as [TAG: value] prefix
"""

import json
import re
from pathlib import Path

ROOT = Path(r"c:/Users/stusc/OneDrive/Desktop/Completions")

FILES = {
    "AC_Circuits.jsonl": "ac_circuits",
    "Advanced_Eng_Math.jsonl": "advanced_eng_math",
}

# --- task_type classification --------------------------------------------------

CONTRAST_PATTERNS = [
    r"\bdifference between\b", r"\bvs\.?\b", r"\bversus\b",
    r"\bcompare\b", r"\bcontrast\b", r"\bdiffer(ent|ence)?\b",
    r"\bsame as\b", r"\bdistinguish\b",
]
DEFINITION_PATTERNS = [
    r"^\s*what\s+is\b", r"^\s*what\s+does .* mean\b", r"^\s*what'?s\b",
    r"^\s*define\b", r"^\s*definition of\b", r"\bmeaning\??\s*$",
    r"\bin plain (words|english)\b", r"\bin simple terms\b",
    r"^\s*\w[\w\s\-']{1,40}\??$",  # bare noun-phrase prompts like "rms?" or "homogeneous ode meaning?"
]
CAUSE_EFFECT_PATTERNS = [
    r"^\s*why\b", r"\bwhat causes\b", r"\beffect of\b", r"\bbecause\b",
    r"\bleads? to\b", r"\bresults? in\b", r"\bdue to\b",
]
RELATION_PATTERNS = [
    r"\brelationship\b", r"\brelated?\b", r"\bhow .* relate\b",
    r"\bconnection between\b", r"\blink between\b", r"\bdepend on\b",
    r"\bhow .* affect(s|ed)?\b", r"\bhow .* (change|influence)",
]
DECOMPOSITION_PATTERNS = [
    r"\bsteps\b", r"\bbreak (it |this )?down\b", r"\bcomponents of\b",
    r"\bparts of\b", r"\bmake[- ]?up\b", r"\bstages\b", r"\bprocedure\b",
    r"\bwalk (me |us )?through\b", r"\blist the\b",
]
APPLICATION_PATTERNS = [
    r"^\s*(calculate|find|compute|solve|evaluate|determine|derive)\b",
    r"\bgiven\s+[a-z]", r"\bif\s+[a-z].*,.*what\b",
    r"\bexample of\b", r"\bgive (me )?an example\b", r"\bfor example\b",
    r"\bfor a\b.*\bwhat\b", r"\bcould this\b", r"\bwhen .* what\b",
    r"\bhow (do|would) (you|one|i)\b.*(solve|calculate|find|compute|apply)",
]
CLARIFICATION_PATTERNS = [
    r"^\s*what do you mean\b", r"^\s*can you clarify\b",
    r"^\s*wait\b", r"^\s*so\b.*\?", r"^\s*i don'?t (get|understand)",
    r"^\s*clarify\b", r"\bhuh\b", r"\bconfused\b",
]
PARAPHRASE_PATTERNS = [
    r"\brephrase\b", r"\bin other words\b", r"\bput (it|that) another way\b",
    r"\brestate\b", r"\bsay .* differently\b", r"\bsimpler (way|words)\b",
]


def match_any(patterns, text):
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            return True
    return False


def classify_task_type(prompt: str) -> str:
    p = prompt.strip()
    # Order matters: more specific first.
    if match_any(CLARIFICATION_PATTERNS, p):
        return "clarification"
    if match_any(PARAPHRASE_PATTERNS, p):
        return "paraphrase"
    if match_any(CONTRAST_PATTERNS, p):
        return "contrast"
    if match_any(CAUSE_EFFECT_PATTERNS, p):
        return "cause_effect"
    if match_any(RELATION_PATTERNS, p):
        return "relation"
    if match_any(DECOMPOSITION_PATTERNS, p):
        return "decomposition"
    if match_any(APPLICATION_PATTERNS, p):
        return "application"
    if match_any(DEFINITION_PATTERNS, p):
        return "definition"
    # Fallback: short factual queries default to definition; anything else = reasoning.
    if len(p) < 60 and p.endswith("?"):
        return "definition"
    return "reasoning"


# --- response_style -----------------------------------------------------------

def classify_style(completion: str) -> str:
    n = len(completion)
    # Also count sentences as a secondary signal.
    sentences = re.split(r"(?<=[.!?])\s+", completion.strip())
    s = len([x for x in sentences if x])
    if n < 180 and s <= 2:
        return "short"
    if n < 450 and s <= 5:
        return "medium"
    return "long"


# --- difficulty ---------------------------------------------------------------

MATH_TOKENS = re.compile(
    r"(∫|∂|∇|∑|∏|√|≈|≠|≤|≥|⇒|⇔|=|\+|\-|\*|/|\^|d/d|dx|dy|dt|"
    r"\bsin\b|\bcos\b|\btan\b|\blog\b|\bexp\b|\bln\b|"
    r"\bmatrix|\beigen|\bfourier|\blaplace|\bpde|\bode|\bintegral|\bderivative)",
    re.IGNORECASE,
)

BRUTAL_HINTS = re.compile(
    r"\b(prove|proof|derive from first principles|rigorously|general solution to|"
    r"arbitrary (boundary|initial) conditions|green'?s function|"
    r"sturm[- ]liouville|distributional|weak solution|well-posed(ness)?)\b",
    re.IGNORECASE,
)

HARD_HINTS = re.compile(
    r"\b(solve|derive|show that|transform|separate variables|"
    r"expand in|series solution|boundary conditions|eigenvalue problem|"
    r"inverse (laplace|fourier)|convolution|residue theorem|"
    r"thevenin|norton|mesh analysis|nodal analysis|superposition|"
    r"three[- ]phase|unbalanced|power factor correction|resonant circuit design)\b",
    re.IGNORECASE,
)

MEDIUM_HINTS = re.compile(
    r"\b(calculate|compute|find|given|formula|equation|apply|how (do|to)|"
    r"impedance|reactance|phasor|rms|peak|resonance|bandwidth|"
    r"integration|differentiate|partial|gradient|divergence|curl)\b",
    re.IGNORECASE,
)


def classify_difficulty(prompt: str, completion: str, task_type: str) -> str:
    text = prompt + " " + completion
    n = len(completion)
    math_hits = len(MATH_TOKENS.findall(text))

    # Brutal: explicit proof/rigorous derivation with long completion.
    if BRUTAL_HINTS.search(text) and n > 400:
        return "brutal"

    # Extremely hard: hard-technique cues + long derivation-style completion.
    if HARD_HINTS.search(text) and n > 500:
        return "extremely_hard"
    if HARD_HINTS.search(text) and math_hits >= 4 and n > 300:
        return "extremely_hard"

    # Hard: multi-step reasoning indicators, moderate length, multiple math tokens.
    if HARD_HINTS.search(text) and n > 200:
        return "hard"
    if math_hits >= 5 and n > 250:
        return "hard"

    # Medium: application/contrast/relation with some substance, or formula-y short answer.
    if task_type in {"application", "contrast", "relation", "decomposition", "cause_effect"}:
        if n > 120 or math_hits >= 2 or MEDIUM_HINTS.search(text):
            return "medium"
    if math_hits >= 2 and n > 100:
        return "medium"
    if n > 220:
        return "medium"

    # Easy: definitional recall, clarifications, paraphrase, very short answers.
    return "easy"


# --- main --------------------------------------------------------------------

PROMPT_ALIASES = {"prompt", "comprehensive", "question", "query"}
COMPLETION_ALIASES = {"completion", "placement", "comparison", "response", "answer"}

JUNK_SUFFIX = re.compile(r"(Add to Conversation|AddtoConversation)\s*$", re.IGNORECASE)

# Lenient extractor for rows that fail strict JSON parsing (usually due to
# unescaped inner quotes). Assumes the line is a single flat object of the form
# {"<key1>": "<val1>", "<key2>": "<val2>"}.
LENIENT_RE = re.compile(
    r'^\s*\{\s*"([^"]+)"\s*:\s*"(.*)"\s*,\s*"([^"]+)"\s*:\s*"(.*)"\s*\}\s*$',
    re.DOTALL,
)


def parse_row(line: str):
    line = JUNK_SUFFIX.sub("", line).strip()
    try:
        obj = json.loads(line)
    except json.JSONDecodeError:
        m = LENIENT_RE.match(line)
        if not m:
            return None
        obj = {m.group(1): m.group(2), m.group(3): m.group(4)}

    prompt = None
    completion = None
    for k, v in obj.items():
        if k in PROMPT_ALIASES and prompt is None:
            prompt = v
        elif k in COMPLETION_ALIASES and completion is None:
            completion = v
    if prompt is None or completion is None:
        return None
    return prompt, completion


def process(path: Path, domain: str):
    labeled_path = path.with_name(path.stem + "_labeled.jsonl")
    conditioned_path = path.with_name(path.stem + "_conditioned.jsonl")

    labeled_lines = []
    conditioned_lines = []
    skipped = []

    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            raw = line.rstrip("\n")
            if not raw.strip():
                continue
            parsed = parse_row(raw)
            if parsed is None:
                skipped.append(i)
                continue
            prompt, completion = parsed

            task_type = classify_task_type(prompt)
            response_style = classify_style(completion)
            difficulty = classify_difficulty(prompt, completion, task_type)

            labeled = {
                "prompt": prompt,
                "completion": completion,
                "difficulty": difficulty,
                "domain": domain,
                "task_type": task_type,
                "response_style": response_style,
            }
            labeled_lines.append(json.dumps(labeled, ensure_ascii=False))

            tag_prefix = (
                f"[DOMAIN: {domain}] "
                f"[DIFFICULTY: {difficulty}] "
                f"[TASK: {task_type}] "
                f"[STYLE: {response_style}] "
            )
            conditioned = {
                "prompt": tag_prefix + prompt,
                "completion": completion,
            }
            conditioned_lines.append(json.dumps(conditioned, ensure_ascii=False))

    labeled_path.write_text("\n".join(labeled_lines) + "\n", encoding="utf-8")
    conditioned_path.write_text("\n".join(conditioned_lines) + "\n", encoding="utf-8")

    return labeled_path, conditioned_path, len(labeled_lines), skipped


def summarize(path: Path):
    from collections import Counter
    diff = Counter()
    task = Counter()
    style = Counter()
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            o = json.loads(line)
            diff[o["difficulty"]] += 1
            task[o["task_type"]] += 1
            style[o["response_style"]] += 1
    return diff, task, style


if __name__ == "__main__":
    import io, sys
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    for fname, domain in FILES.items():
        p = ROOT / fname
        lp, cp, n, skipped = process(p, domain)
        print(f"{fname}: {n} rows, skipped={skipped}")
        print(f"  -> {lp.name}")
        print(f"  -> {cp.name}")
        d, t, s = summarize(lp)
        print(f"  difficulty: {dict(d)}")
        print(f"  task_type:  {dict(t)}")
        print(f"  style:      {dict(s)}")
