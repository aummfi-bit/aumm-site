#!/usr/bin/env python3
"""Sanity-check BM25 retrieval against ask/index.json (no API calls)."""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "ask" / "index.json"

TOP_K = 12
ROUTED_BOOST = 1.4
K1 = 1.5
B = 0.75


def tokenize(s: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9§-]+", s.lower()) if len(t) > 1]


def retrieve(chunks: list[dict], query: str, routed: str | None = None) -> list[tuple[dict, float]]:
    q_terms = tokenize(query)
    docs = [
        tokenize(f"{c['text']} {c['heading']} {c['section_id']}")
        for c in chunks
    ]
    df: dict[str, int] = {}
    for d in docs:
        for t in set(d):
            df[t] = df.get(t, 0) + 1
    n = len(chunks)
    avgdl = sum(len(d) for d in docs) / n

    scored = []
    for c, d in zip(chunks, docs):
        tf: dict[str, int] = {}
        for t in d:
            tf[t] = tf.get(t, 0) + 1
        dl = len(d)
        score = 0.0
        for qt in q_terms:
            f = tf.get(qt, 0)
            if not f:
                continue
            doc_freq = df.get(qt, 0)
            idf = math.log(1 + (n - doc_freq + 0.5) / (doc_freq + 0.5))
            score += idf * (f * (K1 + 1)) / (f + K1 * (1 - B + B * dl / avgdl))
        if routed and c["file"] == routed:
            score *= ROUTED_BOOST
        scored.append((c, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [x for x in scored if x[1] > 0][:TOP_K]


def main() -> int:
    if not INDEX.is_file():
        print(f"error: run scripts/build_ask_index.py first ({INDEX})", file=sys.stderr)
        return 1

    data = json.loads(INDEX.read_text(encoding="utf-8"))
    chunks = data["chunks"]
    tests = [
        ("maximum supply AuMM", "04_tokenomics.md", "21,000,000"),
        ("no buyback no burn", None, "buyback"),
        ("fee routing der Bodensee", "10_constitution.md", "Fee routing"),
    ]

    failed = 0
    for query, routed, expect in tests:
        top = retrieve(chunks, query, routed)
        if not top:
            print(f"FAIL: no results for {query!r}")
            failed += 1
            continue
        best = top[0][0]
        hay = best["text"]
        ok = expect.lower() in hay.lower()
        print(f"{'OK' if ok else 'FAIL'}: {query!r} -> {best['file']} [{best['section_id']}]")
        if not ok:
            print(f"      expected {expect!r} in top chunk")
            failed += 1

    print(f"\n{len(chunks)} chunks, canon_sha={data['canon_sha'][:12]}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
