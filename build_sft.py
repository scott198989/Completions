"""Build SFT-ready train/val files in chat-messages format.

Reads combined_labeled.jsonl and produces:
  train.jsonl  (~90% of rows)
  val.jsonl    (~10% of rows)

Each output row:
  {"messages": [
      {"role": "system",    "content": "<tags as structured system prompt>"},
      {"role": "user",      "content": "<original prompt>"},
      {"role": "assistant", "content": "<original completion>"}
  ]}

Conditioning tags live in the system message so they don't leak into the
user-turn distribution at inference time. Dedup is keyed on (prompt, completion).
Split is deterministic via a fixed seed.
"""

import json
import random
from pathlib import Path

ROOT = Path(r"c:/Users/stusc/OneDrive/Desktop/Completions")
SRC = ROOT / "combined_labeled.jsonl"
TRAIN = ROOT / "train.jsonl"
VAL = ROOT / "val.jsonl"

SEED = 13
VAL_FRACTION = 0.10


def system_prompt(row: dict) -> str:
    return (
        f"You are a tutor answering a question in the domain of {row['domain']}. "
        f"Target difficulty: {row['difficulty']}. "
        f"Task type: {row['task_type']}. "
        f"Response style: {row['response_style']}."
    )


def main():
    seen = set()
    rows = []
    with SRC.open("r", encoding="utf-8") as f:
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

    rng = random.Random(SEED)
    rng.shuffle(rows)

    cut = int(len(rows) * (1 - VAL_FRACTION))
    train_rows = rows[:cut]
    val_rows = rows[cut:]

    def dump(path, data):
        with path.open("w", encoding="utf-8") as out:
            for r in data:
                rec = {
                    "messages": [
                        {"role": "system", "content": system_prompt(r)},
                        {"role": "user", "content": r["prompt"]},
                        {"role": "assistant", "content": r["completion"]},
                    ]
                }
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")

    dump(TRAIN, train_rows)
    dump(VAL, val_rows)

    print(f"source rows:     {sum(1 for _ in SRC.open('r', encoding='utf-8'))}")
    print(f"after dedup:     {len(rows)}")
    print(f"train:           {len(train_rows)} -> {TRAIN.name}")
    print(f"val:             {len(val_rows)} -> {VAL.name}")


if __name__ == "__main__":
    main()
