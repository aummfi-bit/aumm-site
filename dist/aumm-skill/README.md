# aumm-skill — Claude Skill for Project Aureum

A Claude Skill that grounds answers about [Project Aureum](https://aumm.fi) in the canonical specification, derived directly from `aummfi-bit/aumm-site`.

## What's here

- `SKILL.md` — interpretive layer: triggers, rules, and "I don't know" hygiene.
- `references/` — generated subset of the canon (9 numbered specs + 28 pool profiles). Each file carries a `<!-- GENERATED FROM aumm-site@<sha> ... — DO NOT EDIT -->` header.
- `references/_canon.json` — lockfile recording the exact `aumm-site` commit each snapshot reflects.

## Install (manual, until plugin marketplace publishing is available)

```bash
git clone https://github.com/aummfi-bit/aumm-skill.git ~/.claude/skills/aumm-aureum
```

Claude Code picks up Skills under `~/.claude/skills/<name>/` automatically.

## Stay in sync

`references/` is regenerated on every canon change in `aumm-site` via the cross-repo CI workflow (`.github/workflows/skill-publish.yml` in `aumm-site`). Do **not** edit any file under `references/` by hand — the protect-references CI check will reject the PR.

To update locally before the auto-sync runs:

```bash
cd ~/work/aumm-site
python3 scripts/generate_llms_manifest.py --skill-out ~/work/aumm-skill
```

## Versioning

Semver. See `SKILL.md` "Canon attribution" section for the bump rules.

## Out of scope

- Live on-chain state (TVL, gauge votes, multiplier values) — that's the future `aumm-mcp` MCP server.
- Editorial drift surveillance — handled by a separate quarterly review checklist; not enforced by CI.

## Source repo

Canonical specification: <https://github.com/aummfi-bit/aumm-site>
