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

Requires Vercel deployment (serverless function at `api/ask.ts`). Requests **without** `?ask=` pass through to static `.md` — the SPA is unaffected.

## Build the index

```bash
python3 scripts/build_ask_index.py
python3 scripts/test_ask_retrieval.py   # optional sanity check
```

Writes `ask/index.json` (BM25 lexical index — no embedding API). Built at deploy via `vercel.json` `buildCommand`.

## Environment variables (Vercel)

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | Answer synthesis (required) |
| `ASK_MODEL` | Optional model override |

## Retrieval

BM25 (k1=1.5, b=0.75) with length normalization so short factual chunks (e.g. supply tables) rank above long chunks that repeat query terms. The routed `<page>.md` in the URL gets a 1.4× score boost.

## Canon coupling

Index is stamped with `canon_sha` from `dist/aumm-skill/references/_canon.json` when present, else `git rev-parse HEAD` — same pin as the skill lockfile.

## Agent Instructions footer

`ask/agent-instructions.md` is appended to every canonical `.md` file at deploy time (`scripts/append_agent_footer.py`). Source files in git stay footer-free.
