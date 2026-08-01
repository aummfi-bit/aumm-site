#!/usr/bin/env python3
"""
Append the ask/agent-instructions.md footer to every canonical .md file in-place
for deployment. Idempotent: skips files that already contain the marker.

With --replace: rewrite existing footers from the current template (from the
horizontal rule immediately before ## Agent Instructions, or the heading itself,
through EOF).

Run before GitHub Pages upload or as part of Vercel build (after manifest gen).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from chunk_corpus import collect_corpus_files

MARKER = "## Agent Instructions"
FOOTER_PATH = ROOT / "ask" / "agent-instructions.md"


def strip_existing_footer(text: str) -> str:
    """Remove an existing Agent Instructions footer (and optional leading ---)."""
    idx = text.find(MARKER)
    if idx < 0:
        return text
    before = text[:idx]
    # Drop the horizontal rule immediately preceding the marker, if present.
    stripped = before.rstrip()
    if stripped.endswith("---"):
        stripped = stripped[: -len("---")].rstrip()
    return stripped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace existing Agent Instructions footers with the current template",
    )
    args = parser.parse_args()

    if not FOOTER_PATH.is_file():
        print(f"error: {FOOTER_PATH} missing", file=sys.stderr)
        return 1

    footer = FOOTER_PATH.read_text(encoding="utf-8").strip()
    if MARKER not in footer:
        print(
            "error: agent-instructions.md must contain Agent Instructions heading",
            file=sys.stderr,
        )
        return 1

    updated = 0
    skipped = 0
    replaced = 0
    for rel in collect_corpus_files():
        if not rel.endswith(".md"):
            continue
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            if not args.replace:
                skipped += 1
                continue
            body = strip_existing_footer(text)
            path.write_text(body.rstrip() + "\n\n" + footer + "\n", encoding="utf-8")
            replaced += 1
            continue
        path.write_text(text.rstrip() + "\n\n" + footer + "\n", encoding="utf-8")
        updated += 1

    if args.replace:
        print(
            f"agent footer: {updated} appended, {replaced} replaced, {skipped} skipped"
        )
    else:
        print(f"agent footer: {updated} updated, {skipped} already had footer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
