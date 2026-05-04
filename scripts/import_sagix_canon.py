#!/usr/bin/env python3
"""
One-off / maintenance: fetch Sagix (Ghost) articles and write markdown under sagix/.

Extracts <section class="gh-content gh-canvas"> and converts HTML → markdown via html2text.
Requires: pip install html2text

Usage (from repo root):
  python3 scripts/import_sagix_canon.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

try:
    import html2text  # type: ignore
except ImportError:
    print("error: install html2text: pip install html2text", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
SAGIX_DIR = ROOT / "sagix"

# (relative output path under repo root, canonical URL)
ARTICLES: list[tuple[str, str]] = [
    ("sagix/decentralized_money.md", "https://www.sagix.io/decentralized-money/"),
    (
        "sagix/eurodollar_shadow.md",
        "https://www.sagix.io/the-druid-deep-dive-episode-9-part-2-the-eurodollar-shadow-when-dollars-escape-their-makers/",
    ),
    ("sagix/ddd9_part4.md", "https://www.sagix.io/ddd9p4/"),
    ("sagix/ddd9_part3.md", "https://www.sagix.io/ddd-9-part-3/"),
    ("sagix/our_layer_framework.md", "https://www.sagix.io/our-layer-framework/"),
    ("sagix/sagix_miliarium_aureum.md", "https://www.sagix.io/sagix-miliarium-aureum/"),
    ("sagix/risk_premium_problem.md", "https://www.sagix.io/the-risk-premium-problem/"),
]

UA = "aumm-site-canon-import/1.0 (+https://aumm.fi)"

GH_CONTENT_RE = re.compile(
    r'<section\s+class="gh-content\s+gh-canvas"[^>]*>([\s\S]*?)</section>\s*</article>',
    re.IGNORECASE,
)
TITLE_RE = re.compile(
    r'<h1\s+class="gh-article-title"[^>]*>([^<]+)</h1>',
    re.IGNORECASE,
)
TIME_RE = re.compile(
    r'<time[^>]+datetime="([^"]+)"[^>]*>',
    re.IGNORECASE,
)


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_block(html: str) -> str:
    m = GH_CONTENT_RE.search(html)
    if not m:
        raise ValueError("Could not find gh-content section")
    return m.group(1)


def extract_title(html: str) -> str | None:
    m = TITLE_RE.search(html)
    return m.group(1).strip() if m else None


def extract_datetime(html: str) -> str | None:
    m = TIME_RE.search(html)
    return m.group(1).strip() if m else None


def html_to_md(fragment: str) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    h.unicode_snob = True
    return h.handle(fragment).strip()


def main() -> int:
    SAGIX_DIR.mkdir(parents=True, exist_ok=True)
    for rel, url in ARTICLES:
        out = ROOT / rel
        print("fetching", url, "->", rel)
        html = fetch(url)
        title = extract_title(html) or "Untitled"
        published = extract_datetime(html)
        inner = extract_block(html)
        body = html_to_md(inner)
        header_lines = [
            f"# {title}",
            "",
            f"**Canonical source (Sagix Apothecary):** {url}",
        ]
        if published:
            header_lines.append(f"**Original publication date (from page):** {published}")
        header_lines.extend(
            [
                "",
                "**Note:** This file is part of the Aureum / Project documentation canon mirrored from Sagix for offline reference and AI tooling. Protocol mechanics and numeric parameters at `aumm.fi` take precedence where they conflict with interpretive essays.",
                "",
                "---",
                "",
            ]
        )
        out.write_text("\n".join(header_lines) + body + "\n", encoding="utf-8")
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
