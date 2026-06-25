# Spec: `ask` Query Endpoint for aumm-site

*A retrieval-augmented query layer over the canonical docs, for agents that reach the docs over HTTP rather than via the installed skill.*

**Status:** implemented (aumm-site); optional skill fallback pending sync to `aummfi-bit/aumm-skill`  
**Owner repo:** `aummfi-bit/aumm-site` (service deploys with the live site)  
**Depends on:** the existing canonical corpus + `_canon.json` lockfile  
**Does NOT touch:** `aummfi-bit/aumm-skill` runtime (see §6); one optional `SKILL.md` line  

**Implementation map:** `api/ask.ts`, `ask/`, `scripts/build_ask_index.py`, `scripts/chunk_corpus.py`, `scripts/append_agent_footer.py`, `vercel.json`, [`llms.txt`](llms.txt), [`ask/agent-instructions.md`](ask/agent-instructions.md)

---

## 1. What `ask` is

A query parameter on documentation page URLs that turns a static page into a question-answering endpoint. Instead of returning the rendered page, the server runs retrieval-augmented generation (RAG) over the whole documentation corpus and returns a direct, cited natural-language answer.

```
GET https://aumm.fi/04_tokenomics.md?ask=<question>&goal=<end_goal>
```

- `ask` — the immediate, self-contained question, in natural language.
- `goal` — optional; the broader objective the agent is pursuing, used to tailor the answer toward what is actually useful.

The response contains a direct answer plus the supporting excerpts and their canonical section identifiers (`§xxix`, `F-0`, etc.), so the answer is verifiable against the spec.

This is the same convention GitBook exposes on docs published through its platform. Matching the convention exactly means any agent that already knows the GitBook pattern can use the Aureum endpoint with zero new learning.

---

## 2. Why it is the pull-side complement to the skill

| | `aumm-skill` | `aumm-site` + `ask` |
|---|---|---|
| Access mode | Push — cloned into the agent's filesystem | Pull — queried over HTTP |
| Audience | Agents that can install skills (Claude Desktop/CLI) | Any web-enabled agent / browsing model |
| Retrieval | Agent reads `references/` directly | Server retrieves + synthesizes |
| Runtime | None (static artifact) | Serverless function |
| Canon pin | `_canon.json` snapshot | Index built from same `canon_sha` |

The skill cannot reach a browsing agent; `ask` cannot match the skill's zero-latency local residency. Together they cover both populations. **`ask` is not a duplicate of the skill — it is the access path for agents the skill cannot install into.**

---

## 3. Determine hosting first (branch point)

**If aumm-site is published through GitBook:** the `ask` endpoint may already be available natively. Verify, enable it, and skip to §7 (advertising). No build required.

**If aumm-site is a self-hosted static site** (current evidence — generated markdown with `GENERATED FROM aumm-site@<sha>` headers, a custom `_canon.json` lockfile, and a sync pipeline to the skill — points here): build the service per §4–§5.

**Current deployment:** self-hosted path. Static corpus on GitHub Pages; `ask` runtime on Vercel (`vercel.json` rewrite + `api/ask.ts`).

---

## 4. Required components (self-hosted path)

The corpus is small (~50 files), so this needs no heavy infrastructure.

1. **Corpus** — exists already: the canonical markdown + `_canon.json` manifest. Input, unchanged.
2. **Chunker** — split each doc at its existing section boundaries (headings, `§` anchors, `F-N` formula IDs). Carry the section identifier as chunk metadata so citations resolve to a verifiable anchor. Do not chunk blindly by token count; the docs are already structured — preserve that structure. (`scripts/chunk_corpus.py`)
3. **Embedding index** — chunk metadata bundle (`ask/index.json`); retrieval is **BM25 lexical search** at runtime (no embedding provider). Rebuilt on every deploy.
4. **Retriever** — BM25 with length normalization (k1=1.5, b=0.75), top-k over corpus; optional boost for the routed `.md` page in the URL. (`ask/lib/retriever.ts`)
5. **Synthesizer (LLM)** — pass retrieved chunks + `ask` + optional `goal` to the Anthropic API. The system prompt MUST enforce the same grounding rules already written in the skill's `SKILL.md` (§5 below). The model never sees the corpus directly — only the retrieved chunks — which keeps answers bounded by what was actually retrieved. (`ask/lib/synthesizer.ts`, `ask/lib/prompts.ts`)
6. **HTTP handler** — parse `ask`/`goal`, run retrieve → synthesize, return the response (§5 shape). Strip and ignore any other query params. (`api/ask.ts`)
7. **Hosting** — a serverless function co-deployed with the static site (Vercel function). The LLM API key stays server-side and is never exposed to the client.

---

## 5. Grounding contract (the part that matters)

The endpoint must give the **same answer the skill would give** for the same question. Consistency across access modes is the whole point — an agent must not get one answer from the installed skill and a different one from the live endpoint.

The synthesizer's system prompt reuses the skill's existing rules verbatim:

- Quote canonical language where precision matters (formulas, parameter values, fee bands, immutable bounds).
- Cite the section identifier (`§xxix`, `F-5`) for every claim.
- If the retrieved context does not contain the answer, **say so explicitly** and point to `https://aumm.fi`. Do not fabricate parameters, formulas, governance mechanics, or pool details.
- Apply the interpretive rules already in `SKILL.md` (AuMM issuance ≠ BTC mining; CCC ≠ CCB; etc.).

This is the property that distinguishes a useful `ask` from marketing: it must return *absence* honestly. If a question has no committed answer in the corpus, the endpoint says "not specified" — exactly as the corpus itself does — rather than inventing one.

### Response shape

Return both a machine field and a human field:

```json
{
  "answer": "<natural-language answer>",
  "citations": [
    { "section_id": "§xxix", "file": "10_constitution.md", "excerpt": "<verbatim>" }
  ],
  "canon_sha": "<sha the index was built from>",
  "answered_from_corpus": true
}
```

`answered_from_corpus: false` when the retriever found nothing relevant — the signal an agent uses to fall back to a human or to the live site.

---

## 6. Canon coupling — one source of truth, three surfaces

The index MUST be rebuilt whenever the canon advances, on the same trigger that regenerates the skill snapshot. Concretely:

- Build the embedding index from the same `aumm-site@<sha>` that `_canon.json` records.
- Stamp the resulting index with that `canon_sha`.
- Return `canon_sha` in every response (§5), so an agent can confirm the answer reflects current canon — the pull-side parallel to the skill's `_canon.json` lockfile.

Result: site, skill, and `ask` index all pin to one commit. A canon bump fans out to all three from a single sync. They cannot drift.

**Vercel buildCommand:** `generate_llms_manifest.py` → `build_ask_index.py` → `append_agent_footer.py`.

---

## 7. The skill stays untouched — with one optional line

`aumm-skill` needs no changes; it has no runtime and reads `references/` directly. The only optional touch is upgrading its existing fallback rule. `SKILL.md` today says: if a question cannot be answered from `references/`, say so and link to `https://aumm.fi`. That can become:

> …say so explicitly, and for questions that may post-date this snapshot, query the live endpoint: `GET https://aumm.fi/<page>.md?ask=<question>` (optional `&goal=<end_goal>`).

This gives an offline skill a live escape hatch for content newer than its pinned `canon_sha` — without putting any service logic in the skill repo.

*(Draft applied in `dist/aumm-skill/SKILL.md`; sync to remote on next skill publish.)*

---

## 8. Advertising the endpoint — discovery ladder

Discovery is two separate problems:

1. **"How do I get here?"** — an agent that has never touched the docs.
2. **"Now that I'm here, how do I ask?"** — an agent that already fetched a page.

Both must be solved. §8 in the original proposal covered only the second. The full ladder:

### 8.1 Installed-skill agents — no discovery needed

For the agent population that matters most, discovery is a non-problem: the installed skill *is* the corpus, resident locally. The optional `SKILL.md` line from §7 is what bridges the two — it tells the skilled agent "for anything past your snapshot, the live endpoint is here." A Claude agent never has to *discover* `ask`; it's handed the URL by its own skill when it needs the fallback.

### 8.2 Root-level `llms.txt` — closes "how do I get here?"

The emerging convention is a `/llms.txt` (and fuller `/llms-full.txt`) at the domain root — a machine-readable index that agents and crawlers look for the way they look for `robots.txt` or `sitemap.xml`.

**This file must name the `ask` endpoint explicitly** — so an agent that fetches `aumm.fi/llms.txt` learns both the corpus structure and that a query endpoint exists, *before* reading a single doc page.

Requirements:

- **`Agent discovery — start here`** section near the top (after welcome block), before bulk URL lists.
- Routing table: question → `ask`; context-building → this file + `llms-full.txt`; already on page → footer; Claude with skill → local corpus.
- Explicit **discovery ladder** listing all four layers (see §8.5).
- **`Query endpoint (ask)`** section with parameters, example, response schema, grounding contract.
- `<link rel="llms-txt" href="/llms.txt">` in `index.html` (already present).
- `robots.txt` comment block pointing to `llms.txt` as START HERE and naming the `ask` URL pattern.

### 8.3 In-page Agent Instructions — closes "now that I'm here, how do I ask?"

Every served `.md` page carries a short **Agent Instructions** block at the foot describing the `ask`/`goal` params in plain language — the GitBook mechanism that worked on Cap. One page fetched teaches the agent how to query all of them.

Implementation:

- Source fragment: `ask/agent-instructions.md`
- Injected at deploy time by `scripts/append_agent_footer.py` (source `.md` in git stays footer-free)
- Footer points **up** to `llms.txt` for root discovery
- Clarifies retrieval spans the **full corpus**, not just the current page

### 8.4 Standard web-crawl surface — upstream of everything

`sitemap.xml`, clean semantic HTML, raw `.md` variants reachable at stable URLs, `robots.txt` with `Sitemap:` directive. No `ask`-specific work; table stakes so docs get indexed and found at all.

### 8.5 Discovery hierarchy (reference)

| Priority | Population | Surface | Problem solved |
|----------|------------|---------|----------------|
| — | Installed-skill Claude | `SKILL.md` fallback URL | Beyond-snapshot queries; no discovery |
| 1 | Browsing agent (pre-landing) | `llms.txt` at root | Corpus map + `ask` named before any page fetch |
| 2 | Browsing agent (post-landing) | Agent Instructions footer on every `.md` | Self-bootstrapping `ask` convention |
| 3 | Everything upstream | `sitemap.xml`, `robots.txt`, crawlable `.md` | Docs indexed and found at all |

**Honest dependency:** in-page blocks (§8.3) only fire *after* the agent has loaded a page. Root `llms.txt` (§8.2) is the missing prerequisite that §8 alone cannot provide.

---

## 9. Environment and deployment

| Variable | Where | Purpose |
|----------|-------|---------|
| `ANTHROPIC_API_KEY` | Vercel (runtime) | Answer synthesis (Claude) |
| `ASK_MODEL` | Vercel (optional) | Override default model (`claude-sonnet-4-20250514`) |

GitHub Pages serves static markdown with agent footers only; the RAG JSON endpoint requires Vercel.

---

## Appendix A — Sample `llms.txt` discovery sections

*Excerpt from the live [`llms.txt`](llms.txt). The full file also includes tab→file mapping, reading order, retrieval hints, and exclusions.*

```markdown
# Project Aureum — LLM / AI agent manifest

**Canonical site:** `https://aumm.fi`
**Standards:** Compatible with the llms.txt specification. index.html declares
<link rel="llms-txt" href="/llms.txt">.

---

## Agent discovery — start here

This file is the **root-level entry point** for agents that have not yet read any
doc page. Fetch it first — the way crawlers fetch robots.txt or sitemap.xml — to
learn both the corpus layout and how to query it.

| If you are… | Start with… |
|-------------|-------------|
| A **browsing agent** with a question | **Query endpoint** below — append ?ask= to any .md URL |
| A **browsing agent** building context | This file, then llms-full.txt for the complete URL list |
| An agent that **already fetched a page** | Agent Instructions footer at the foot of every .md page |
| A **Claude agent with the installed skill** | Local references/ in aumm-skill; SKILL.md for live fallback |

**Discovery ladder (weakest → strongest signal):**

1. **Crawl surface** — sitemap.xml, robots.txt, raw .md URLs
2. **This file** — corpus map + ask endpoint named explicitly
3. **In-page Agent Instructions** — self-bootstrapping once any page is loaded
4. **Installed skill** — corpus local; SKILL.md hands live URL when snapshot is stale

---

## Query endpoint (ask) — preferred for questions

Do not bulk-fetch the corpus to answer a single question. Use the GitBook-compatible
query convention:

    GET https://aumm.fi/<page>.md?ask=<question>&goal=<end_goal>

| Parameter | Required | Purpose |
|-----------|----------|---------|
| ask       | yes      | Immediate, self-contained question |
| goal      | no       | Broader objective; tailors the answer |

Example:

    GET https://aumm.fi/04_tokenomics.md?ask=What+is+the+AuMM+maximum+supply

Response (JSON): answer, citations ({ section_id, file, excerpt }), canon_sha,
answered_from_corpus.

Grounding rules match aumm-skill. Retrieval spans the **full corpus**, not just
the page in the URL.
```

---

## Appendix B — Sample Agent Instructions footer

*Injected at deploy time from [`ask/agent-instructions.md`](ask/agent-instructions.md).*

```markdown
---

## Agent Instructions

**Root discovery:** fetch https://aumm.fi/llms.txt first for corpus structure
and the full agent discovery ladder.

**Query this corpus:**

    GET https://aumm.fi/<page>.md?ask=<question>&goal=<end_goal>

- ask (required) — immediate question
- goal (optional) — broader objective

Response: JSON with answer, citations, canon_sha, answered_from_corpus.
Retrieval spans the full corpus, not just this page.
```

---

## Summary

- Build `ask` in **aumm-site**; it is a runtime service and belongs with the live docs.
- Do **not** build it in **aumm-skill**; that repo has no runtime and its agents already hold the corpus locally.
- Reuse the skill's grounding rules so both access modes answer identically — including answering *absence* honestly.
- Pin the index to the same `canon_sha` as the skill and site, rebuilt on the same sync, so all three surfaces stay consistent.
- **Discovery is a ladder, not a single surface:**
  - **Root `llms.txt`** names `ask` before any page fetch (§8.2).
  - **In-page footers** self-bootstrap once any page is loaded (§8.3).
  - **`SKILL.md`** hands installed agents the live URL (§7).
  - **Crawl surface** (`sitemap`, `.md` URLs) is upstream table stakes (§8.4).
- One optional skill edit: point its "beyond snapshot" fallback at the live endpoint.
