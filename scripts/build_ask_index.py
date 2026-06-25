#!/usr/bin/env python3
"""
Build ask/index.json for the aumm.fi `ask` endpoint.

Chunks the canonical corpus at heading boundaries (via chunk_corpus.py),
tags each chunk with section_id, and stamps canon_sha from _canon.json
(when present) or git HEAD.

No embedding provider required — retrieval is BM25 at runtime.

  python3 scripts/build_ask_index.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from chunk_corpus import chunk_file, collect_corpus_files
from generate_llms_manifest import get_canon_sha

OUT_PATH = ROOT / "ask" / "index.json"
CANON_LOCK = ROOT / "dist" / "aumm-skill" / "references" / "_canon.json"


def resolve_canon_sha() -> str:
    if CANON_LOCK.is_file():
        try:
            data = json.loads(CANON_LOCK.read_text(encoding="utf-8"))
            sha = data.get("canon_sha")
            if sha:
                return sha
        except (json.JSONDecodeError, OSError):
            pass
    return get_canon_sha()


def build_index() -> dict:
    rel_paths = collect_corpus_files()
    if not rel_paths:
        print("error: no corpus files", file=sys.stderr)
        raise SystemExit(1)

    chunks = []
    for rel in rel_paths:
        src = ROOT / rel
        if not src.is_file():
            print(f"warning: missing {rel}, skipping", file=sys.stderr)
            continue
        for c in chunk_file(rel, src.read_text(encoding="utf-8")):
            chunks.append(c.to_dict())

    if not chunks:
        print("error: no chunks produced", file=sys.stderr)
        raise SystemExit(1)

    return {
        "canon_sha": resolve_canon_sha(),
        "chunk_count": len(chunks),
        "chunks": chunks,
    }


def main() -> int:
    index = build_index()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(index, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"wrote {OUT_PATH.relative_to(ROOT)} "
        f"({index['chunk_count']} chunks, canon_sha={index['canon_sha'][:12]})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
