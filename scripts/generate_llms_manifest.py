#!/usr/bin/env python3
"""
Generate llms-full.txt: one absolute HTTPS URL per line (no comments) for LLM/RAG ingestion.

Default base: https://aumm.fi  (override with BASE_URL=https://example.com)

CORE_PATHS order aligns with index.html loadMd() batch and site structure:
  Intro uses 01_intro.json (not listed here).
  Nav: Mental Model, Foundations, Tokenomics, Miliarium (05–07), Governance (10,08,09,11), Glossary, Appendices, UX/UI, Team (16); Overview (15) loads programmatically.

Excluded from output: script.md (internal review notes); 01_intro.json (not Markdown prose).

See ../llms.txt for human/AI-readable manifest and tab→file mapping.

Optional Skill build: pass --skill-out <dir> to also generate the aumm-skill references/
tree (canonical .md subset + 28 pool profiles + _canon.json lockfile). Source files stay
the canon; references/ files are derived and carry a DO-NOT-EDIT header.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
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
    "16_team.md",
]

SECONDARY_PATHS: list[str] = [
    "aureum_schedule.md",
    "project_aureum_design_final.md",
]

# Contributor-facing; listed after secondary, before pool profiles.
README_PATH = "README.md"

PROFILE_RE = re.compile(r"^(\d{2})_ix.*\.md$", re.IGNORECASE)

# Subset of canon shipped to the Claude Skill. Pool profiles are added separately.
SKILL_REFERENCES: list[str] = [
    "15_overview.md",
    "02_mental_model.md",
    "03_theoretical_foundation.md",
    "04_tokenomics.md",
    "05_miliarium_aureum.md",
    "08_bootstrap.md",
    "10_constitution.md",
    "11_formulas.md",
    "12_aureum_glossary.md",
]


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


def get_canon_sha() -> str:
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL
        )
        return sha.decode("ascii").strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def write_skill_reference(src: Path, dst: Path, canon_sha: str, rel: str) -> None:
    header = f"<!-- GENERATED FROM aumm-site@{canon_sha} {rel} — DO NOT EDIT -->\n"
    body = src.read_text(encoding="utf-8")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(header + body, encoding="utf-8")


def build_skill(out_dir: Path) -> int:
    refs_dir = out_dir / "references"
    profiles_dir = refs_dir / "miliarium_profiles"

    # Wipe and rebuild references/ deterministically.
    if refs_dir.exists():
        shutil.rmtree(refs_dir)
    refs_dir.mkdir(parents=True)
    profiles_dir.mkdir(parents=True)

    canon_sha = get_canon_sha()
    written: list[str] = []

    for rel in SKILL_REFERENCES:
        src = ROOT / rel
        if not src.is_file():
            print(f"error: skill reference missing: {rel}", file=sys.stderr)
            return 1
        write_skill_reference(src, refs_dir / rel, canon_sha, rel)
        written.append(rel)

    prof_dir = ROOT / "miliarium_profiles"
    if not prof_dir.is_dir():
        print("error: miliarium_profiles/ missing — cannot build skill", file=sys.stderr)
        return 1

    prof_files: list[tuple[int, str, str]] = []
    for name in os.listdir(prof_dir):
        m = PROFILE_RE.match(name)
        if m:
            prof_files.append((int(m.group(1)), name, f"miliarium_profiles/{name}"))
    prof_files.sort(key=lambda x: x[0])
    for _slot, name, rel in prof_files:
        write_skill_reference(prof_dir / name, profiles_dir / name, canon_sha, rel)
        written.append(rel)

    lockfile = {
        "canon_sha": canon_sha,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_repo": "aummfi-bit/aumm-site",
        "files": written,
    }
    (refs_dir / "_canon.json").write_text(
        json.dumps(lockfile, indent=2) + "\n", encoding="utf-8"
    )

    print(
        f"wrote {len(written)} references + _canon.json to "
        f"{refs_dir.relative_to(out_dir.parent) if out_dir.parent in refs_dir.parents else refs_dir} "
        f"(canon_sha={canon_sha})"
    )
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0] if __doc__ else None)
    p.add_argument(
        "--skill-out",
        type=Path,
        default=None,
        help="If set, also build the aumm-skill references/ tree under this directory.",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])

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

    if args.skill_out is not None:
        rc = build_skill(args.skill_out)
        if rc != 0:
            return rc

    return 0


if __name__ == "__main__":
    sys.exit(main())
