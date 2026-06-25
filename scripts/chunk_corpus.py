#!/usr/bin/env python3
"""
Split canonical Aureum markdown into section-bound chunks for the ask index.

Chunks at ## / ### headings and F-N formula IDs. Each chunk carries a
section_id suitable for citations (§xxix, F-0, ixHelvetia/Composition, …).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

H2_RE = re.compile(r"^##\s+(.+)$")
H3_RE = re.compile(r"^###\s+(.+)$")
ROMAN_SECTION_RE = re.compile(
    r"^(§)?([ivxlcdm]+)\.\s*(.*)$", re.IGNORECASE
)
FORMULA_RE = re.compile(r"^(F-\d+)\.\s*(.*)$", re.IGNORECASE)
PROFILE_RE = re.compile(r"^(\d{2})_(ix\w+)\.md$", re.IGNORECASE)


@dataclass
class Chunk:
    file: str
    section_id: str
    heading: str
    text: str

    def to_dict(self) -> dict:
        return {
            "file": self.file,
            "section_id": self.section_id,
            "heading": self.heading,
            "text": self.text,
        }


def roman_to_section_id(title: str) -> str | None:
    m = ROMAN_SECTION_RE.match(title.strip())
    if not m:
        return None
    numeral = m.group(2).lower()
    return f"§{numeral}"


def formula_section_id(title: str) -> str | None:
    m = FORMULA_RE.match(title.strip())
    if not m:
        return None
    return m.group(1).upper().replace("f-", "F-")


def slug_heading(title: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", title).strip().lower()
    cleaned = re.sub(r"\s+", "-", cleaned)
    return cleaned or "section"


def profile_prefix(rel_path: str) -> str | None:
    name = Path(rel_path).name
    m = PROFILE_RE.match(name)
    if not m:
        return None
    return m.group(2)


def section_id_for_heading(
    rel_path: str,
    heading: str,
    parent_section: str | None,
    level: int,
) -> str:
    roman = roman_to_section_id(heading)
    if roman:
        return roman
    formula = formula_section_id(heading)
    if formula:
        return formula
    pool = profile_prefix(rel_path)
    slug = slug_heading(heading)
    if pool:
        return f"{pool}/{slug}"
    if parent_section:
        return f"{parent_section}/{slug}"
    if level == 2:
        return slug
    return slug_heading(Path(rel_path).stem) + f"/{slug}"


def chunk_file(rel_path: str, content: str) -> list[Chunk]:
    rel = rel_path.replace("\\", "/")
    lines = content.splitlines()
    chunks: list[Chunk] = []
    parent_section: str | None = None
    current_heading = Path(rel).stem
    current_section_id = slug_heading(Path(rel).stem)
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_lines
        body = "\n".join(current_lines).strip()
        if not body:
            return
        chunks.append(
            Chunk(
                file=rel,
                section_id=current_section_id,
                heading=current_heading,
                text=body,
            )
        )

    for line in lines:
        h2 = H2_RE.match(line)
        h3 = H3_RE.match(line)
        if h2:
            flush()
            heading = h2.group(1).strip()
            sid = section_id_for_heading(rel, heading, parent_section, 2)
            parent_section = sid if sid.startswith("§") or sid.startswith("F-") else sid
            current_heading = heading
            current_section_id = sid
            current_lines = [line]
        elif h3:
            flush()
            heading = h3.group(1).strip()
            sid = section_id_for_heading(rel, heading, parent_section, 3)
            current_heading = heading
            current_section_id = sid
            current_lines = [line]
        else:
            current_lines.append(line)

    flush()

    if not chunks and content.strip():
        chunks.append(
            Chunk(
                file=rel,
                section_id=slug_heading(Path(rel).stem),
                heading=Path(rel).stem,
                text=content.strip(),
            )
        )

    return chunks


def collect_corpus_files() -> list[str]:
    """Reuse the same canonical file set as generate_llms_manifest.py."""
    from generate_llms_manifest import collect_paths

    return collect_paths()
