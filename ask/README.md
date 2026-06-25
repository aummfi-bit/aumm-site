# ask — RAG query layer

Retrieval-augmented query endpoint for agents that reach the docs over HTTP.

Full design spec: [ASK_SPEC.md](../ASK_SPEC.md).

## Discovery ladder

| Layer | Surface | Closes |
|-------|---------|--------|
| 1 | [`llms.txt`](https://aumm.fi/llms.txt) at root | "How do I get here?" + names `ask` before any page fetch |
| 2 | Agent Instructions footer on every `.md` | "Now that I'm here, how do I ask?" |
| 3 | [`SKILL.md`](../dist/aumm-skill/SKILL.md) fallback | Installed-skill agents handed the live URL when snapshot is stale |
| 4 | `sitemap.xml`, `robots.txt`, raw `.md` URLs | Upstream crawlability so docs get indexed at all |

## Endpoint

```
GET https://aumm.fi/<page>.md?ask=<question>&goal=<end_goal>
```

Returns JSON (`answer`, `citations`, `canon_sha`, `answered_from_corpus`).

Requires Vercel deployment (serverless function at `api/ask.ts`). GitHub Pages serves static Markdown only; the `ask` runtime lives on Vercel.

## Build the embedding index

```bash
export OPENAI_API_KEY=...
python3 scripts/build_ask_index.py
```

Writes `ask/index.json` (not committed — built at deploy time via `vercel.json` `buildCommand`).

## Environment variables (Vercel)

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | Query + index embeddings (`text-embedding-3-small`) |
| `ANTHROPIC_API_KEY` | Answer synthesis (Claude) |

## Canon coupling

Index is stamped with `canon_sha` from `git rev-parse HEAD`, same as `_canon.json` in the skill snapshot. Rebuild on every canon advance (Vercel build + optional local run after edits).

## Agent Instructions footer

`ask/agent-instructions.md` is appended to every canonical `.md` file at deploy time (`scripts/append_agent_footer.py`). Source files in git stay footer-free.
