#!/usr/bin/env python3
"""
Build the ask/ embedding index from the canonical markdown corpus.

Output: ask/index.json — flat in-memory index stamped with canon_sha.
Requires OPENAI_API_KEY (text-embedding-3-small) at build time.

Run on the same trigger as skill snapshot regeneration:
  python3 scripts/build_ask_index.py
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from chunk_corpus import Chunk, chunk_file, collect_corpus_files
from generate_llms_manifest import get_canon_sha

EMBED_MODEL = "text-embedding-3-small"
EMBED_BATCH = 64
OUT_PATH = ROOT / "ask" / "index.json"


def embed_texts(texts: list[str], api_key: str) -> list[list[float]]:
    url = "https://api.openai.com/v1/embeddings"
    payload = json.dumps({"model": EMBED_MODEL, "input": texts}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"error: OpenAI embeddings API failed ({e.code}): {body}", file=sys.stderr)
        raise SystemExit(1) from e

    items = sorted(data["data"], key=lambda x: x["index"])
    return [item["embedding"] for item in items]


def build_index(api_key: str) -> dict:
    rel_paths = collect_corpus_files()
    if not rel_paths:
        print("error: no corpus files", file=sys.stderr)
        raise SystemExit(1)

    all_chunks: list[Chunk] = []
    for rel in rel_paths:
        src = ROOT / rel
        if not src.is_file():
            print(f"warning: missing {rel}, skipping", file=sys.stderr)
            continue
        all_chunks.extend(chunk_file(rel, src.read_text(encoding="utf-8")))

    if not all_chunks:
        print("error: no chunks produced", file=sys.stderr)
        raise SystemExit(1)

    embeddings: list[list[float]] = []
    texts = [c.text for c in all_chunks]
    for i in range(0, len(texts), EMBED_BATCH):
        batch = texts[i : i + EMBED_BATCH]
        embeddings.extend(embed_texts(batch, api_key))

    entries = []
    for chunk, embedding in zip(all_chunks, embeddings):
        row = chunk.to_dict()
        row["embedding"] = embedding
        entries.append(row)

    return {
        "canon_sha": get_canon_sha(),
        "embed_model": EMBED_MODEL,
        "chunk_count": len(entries),
        "chunks": entries,
    }


def main() -> int:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print(
            "error: OPENAI_API_KEY is required to build ask/index.json",
            file=sys.stderr,
        )
        return 1

    index = build_index(api_key)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(index) + "\n", encoding="utf-8")
    print(
        f"wrote {OUT_PATH.relative_to(ROOT)} "
        f"({index['chunk_count']} chunks, canon_sha={index['canon_sha'][:7]})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
