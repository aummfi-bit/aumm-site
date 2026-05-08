#!/usr/bin/env python3
"""
Generate llms-full.txt: one absolute HTTPS URL per line (no comments) for LLM/RAG ingestion.

Also writes ../sitemap.xml for crawlers: same URL set plus site root,
/llms.txt, and /llms-full.txt. lastmod uses each backing file's mtime at
generation time (UTC, W3C dateTime); homepage uses index.html mtime.

Default base: https://aumm.fi  (override with BASE_URL=https://example.com)

Single source of truth: the canonical file list is parsed from index.html's
loadMd('FILENAME.md', ...) calls. Adding/removing a tab from the SPA flows
automatically into llms-full.txt, sitemap.xml, and the Skill build — no
hand-maintained allowlist drifts. Pool profiles use a directory glob (they're loaded via
dynamic router, not enumerated in index.html).

Excluded: 01_intro.json (animation data, not Markdown prose); script.md
(internal review notes); aureum_schedule.md and project_aureum_design_final.md
(no longer canon — the SPA doesn't load them).

See ../llms.txt for human/AI-readable manifest and tab→file mapping.

Optional Skill build: pass --skill-out <dir> to also generate the aumm-skill
references/ tree (canonical .md set + 28 pool profiles + _canon.json lockfile).
Source files stay the canon; references/ files are derived and carry a
DO-NOT-EDIT header.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from xml.sax.saxutils import escape as xml_escape
from datetime import datetime, timezone
from pathlib import Path

# Repo root = parent of scripts/
ROOT = Path(__file__).resolve().parent.parent

DEFAULT_BASE = "https://aumm.fi"

INDEX_HTML = ROOT / "index.html"
LOAD_MD_RE = re.compile(r"""loadMd\(\s*['"]([^'"]+\.md)['"]""")

# Contributor-facing; appended after canon, before pool profiles.
README_PATH = "README.md"

PROFILE_RE = re.compile(r"^(\d{2})_ix.*\.md$", re.IGNORECASE)


def canon_paths() -> list[str]:
    """Parse index.html for loadMd('<file>.md', ...) calls — the canonical file set."""
    if not INDEX_HTML.is_file():
        print(f"error: {INDEX_HTML.relative_to(ROOT)} missing", file=sys.stderr)
        return []
    text = INDEX_HTML.read_text(encoding="utf-8")
    seen: set[str] = set()
    out: list[str] = []
    for m in LOAD_MD_RE.finditer(text):
        rel = m.group(1)
        if rel in seen:
            continue
        seen.add(rel)
        if not (ROOT / rel).is_file():
            print(f"warning: index.html references missing file: {rel}", file=sys.stderr)
            continue
        out.append(rel)
    return out


def collect_paths() -> list[str]:
    paths = canon_paths()

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


def utc_lastmod_from_path(path: Path) -> str:
    """W3C lastmod from filesystem mtime, or UTC 'now' if file is missing."""
    if not path.is_file():
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ts = path.stat().st_mtime
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_sitemap(base: str, rel_paths: list[str]) -> None:
    """Emit sitemap.xml at repo root; URLs = base, llms.txt, llms-full.txt, then each rel."""
    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<urlset xmlns="{ns}">',
    ]
    entries: list[tuple[str, Path]] = [
        (f"{base}/", INDEX_HTML),
        (f"{base}/llms.txt", ROOT / "llms.txt"),
        (f"{base}/llms-full.txt", ROOT / "llms-full.txt"),
    ]
    seen_loc: set[str] = set()
    for loc, lm_path in entries:
        if loc in seen_loc:
            continue
        seen_loc.add(loc)
        lm = utc_lastmod_from_path(lm_path)
        esc = xml_escape(loc)
        lines.append(f"  <url><loc>{esc}</loc><lastmod>{lm}</lastmod></url>")
    for rel in rel_paths:
        loc = f"{base}/{rel}"
        if loc in seen_loc:
            continue
        seen_loc.add(loc)
        lm = utc_lastmod_from_path(ROOT / rel)
        esc = xml_escape(loc)
        lines.append(f"  <url><loc>{esc}</loc><lastmod>{lm}</lastmod></url>")
    lines.append("</urlset>")
    out = ROOT / "sitemap.xml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(seen_loc)} URLs, base={base})")


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

    if refs_dir.exists():
        shutil.rmtree(refs_dir)
    refs_dir.mkdir(parents=True)
    profiles_dir.mkdir(parents=True)

    canon_sha = get_canon_sha()
    written: list[str] = []

    for rel in canon_paths():
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

    rc = check_local_links(refs_dir, set(written))
    if rc != 0:
        return rc

    print(
        f"wrote {len(written)} references + _canon.json to {refs_dir} "
        f"(canon_sha={canon_sha})"
    )
    return 0


# Match markdown links to local .md files: [text](path/to/file.md) or [text](file.md#anchor).
# Skips http(s):// and mailto: targets.
LINK_RE = re.compile(r"\[[^\]]*\]\((?!https?://|mailto:)([^)#]+\.md)(?:#[^)]*)?\)")


def check_local_links(refs_dir: Path, shipped: set[str]) -> int:
    """Fail if any shipped reference contains a markdown link to an unbundled .md file."""
    shipped_basenames = {Path(p).name for p in shipped}
    shipped_relpaths = set(shipped)
    bad: list[tuple[str, str]] = []

    for ref_file in sorted(refs_dir.rglob("*.md")):
        rel_from_refs = ref_file.relative_to(refs_dir).as_posix()
        text = ref_file.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            # Resolve target relative to the file's directory, against the refs/ tree.
            base = (ref_file.parent / target).resolve()
            try:
                rel_target = base.relative_to(refs_dir.resolve()).as_posix()
            except ValueError:
                rel_target = None

            if rel_target and rel_target in shipped_relpaths:
                continue
            if Path(target).name in shipped_basenames:
                continue
            bad.append((rel_from_refs, target))

    if bad:
        print("error: dangling cross-references in skill snapshot:", file=sys.stderr)
        for src, tgt in bad:
            print(f"  {src} -> {tgt}", file=sys.stderr)
        print(
            "Hint: add the missing file to index.html's loadMd() list, or fix "
            "the link in the source .md.",
            file=sys.stderr,
        )
        return 1
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

    write_sitemap(base, rels)

    if args.skill_out is not None:
        rc = build_skill(args.skill_out)
        if rc != 0:
            return rc

    return 0


if __name__ == "__main__":
    sys.exit(main())
