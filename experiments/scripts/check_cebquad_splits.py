"""Split-leakage check for CebQuAD (jhoannarica/cebquad_split).

Usage: python -I experiments/scripts/check_cebquad_splits.py data/cebquad
Reports, for every pair of splits, how many articles / contexts / questions appear in both.
"""
import csv
import re
import sys
from itertools import combinations
from pathlib import Path

csv.field_size_limit(10**9)
SPLITS = ("train", "validation", "test")


def norm(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def load(folder):
    data = {}
    for split in SPLITS:
        with open(Path(folder) / f"{split}.csv", encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        data[split] = {
            "rows": len(rows),
            "article_id": {r["article_id"] for r in rows},
            "article_body": {norm(r["article_body"]) for r in rows},
            "body_head": {norm(r["article_body"])[:300] for r in rows},  # catches near-copies with edited endings
            "title": {norm(r["article_title"]) for r in rows},
            "context": {norm(r["context"]) for r in rows},
            "question": {norm(r["question"]) for r in rows},
            "q_and_context": {(norm(r["question"]), norm(r["context"])) for r in rows},  # true leakage unit
        }
    return data


def main(folder):
    data = load(folder)
    keys = ("article_id", "article_body", "body_head", "title", "context", "question", "q_and_context")
    assert all(data[s]["rows"] > 0 for s in SPLITS), "empty split: check the CSV paths"
    print("split       rows  " + "  ".join(f"{k:>12}" for k in keys))
    for s in SPLITS:
        print(f"{s:<10} {data[s]['rows']:>5}  " + "  ".join(f"{len(data[s][k]):>12}" for k in keys))
    print("\nOverlap (count in both splits):")
    for a, b in combinations(SPLITS, 2):
        print(f"{a} & {b}: " + ", ".join(f"{k}={len(data[a][k] & data[b][k])}" for k in keys))
    # Questions written with the passage in view are often too generic to find it in a whole corpus.
    contexts_per_q = {}
    for s in SPLITS:
        for q, c in data[s]["q_and_context"]:
            contexts_per_q.setdefault(q, set()).add(c)
    test_qs = data["test"]["question"]
    ambiguous = sum(1 for q in test_qs if len(contexts_per_q[q]) > 1)
    print(f"\nTest questions that also appear with a different passage anywhere: {ambiguous} of {len(test_qs)} "
          f"({100 * ambiguous / len(test_qs):.1f}%)")
    print("\nSample shared questions (train & test):")
    for q in sorted(data["train"]["question"] & data["test"]["question"])[:10]:
        print("  ", q[:100])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/cebquad")
