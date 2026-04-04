#!/usr/bin/env python3
"""
Generate llms-full.txt: one absolute HTTPS URL per line (no comments) for LLM/RAG ingestion.

Default base: https://aumm.fi  (override with BASE_URL=https://example.com)

CORE_PATHS order aligns with index.html loadMd() batch and site structure:
  Intro uses 01_intro.json (not listed here).
  Nav: Mental Model, Foundations, Tokenomics, Miliarium (05–07), Governance (10,08,09,11), Glossary, Appendices, UX/UI; Overview (15) loads programmatically.

Excluded from output: editorial_sprints.md, script.md (internal); 01_intro.json (not Markdown prose).

See ../llms.txt for human/AI-readable manifest and tab→file mapping.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# Repo root = parent of scripts/
ROOT = Path(__file__).resolve().parent.parent

DEFAULT_BASE = "https://aumm.fi"

# Order matches site nav / plan (index.html loadMd batch + secondary specs).
CORE_PATHS: list[str] = [
    "15_overview.md",
    "02_mental_model.md",
    "03_theoretical_foundation.md",
    "04_tokenomics.md",
    "05_miliarium_aureum.md",
    "06_miliarium_manifest.md",
    "07_miliarium_sectors.md",
    "07a_tokens.md",
    "08_bootstrap.md",
    "09_transitions.md",
    "10_constitution.md",
    "11_formulas.md",
    "12_aureum_glossary.md",
    "13_appendices.md",
    "14_ux_ui.md",
]

SECONDARY_PATHS: list[str] = [
    "aureum_schedule.md",
    "project_aureum_design_final.md",
]

# Contributor-facing; listed after secondary, before pool profiles.
README_PATH = "README.md"

PROFILE_RE = re.compile(r"^(\d{2})_ix.*\.md$", re.IGNORECASE)


def collect_paths() -> list[str]:
    paths: list[str] = []
    for rel in CORE_PATHS + SECONDARY_PATHS:
        p = ROOT / rel
        if not p.is_file():
            print(f"warning: missing file (skipped): {rel}", file=sys.stderr)
            continue
        paths.append(rel.replace("\\", "/"))

    readme = ROOT / README_PATH
    if readme.is_file():
        paths.append(README_PATH)

    prof_dir = ROOT / "miliarium_profiles"
    if not prof_dir.is_dir():
        print("warning: miliarium_profiles/ missing", file=sys.stderr)
        return paths

    prof_files: list[tuple[int, str]] = []
    for name in os.listdir(prof_dir):
        m = PROFILE_RE.match(name)
        if m:
            prof_files.append((int(m.group(1)), f"miliarium_profiles/{name}"))
    prof_files.sort(key=lambda x: x[0])
    for _slot, rel in prof_files:
        if (ROOT / rel).is_file():
            paths.append(rel.replace("\\", "/"))
        else:
            print(f"warning: missing profile (skipped): {rel}", file=sys.stderr)

    return paths


def main() -> int:
    base = os.environ.get("BASE_URL", DEFAULT_BASE).rstrip("/")
    rels = collect_paths()
    if not rels:
        print("error: no paths collected", file=sys.stderr)
        return 1

    lines = [f"{base}/{rel}" for rel in rels]
    if len(lines) != len(set(lines)):
        print("error: duplicate URLs", file=sys.stderr)
        return 1

    out = ROOT / "llms-full.txt"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(lines)} URLs to {out.relative_to(ROOT)} (base={base})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
