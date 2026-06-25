# AUREUM — Protocol design site

Static documentation and registry for **Project Aureum**: tokenomics, governance bounds, and the **Miliarium Aureum** constellation of **28** immutable liquidity pools.

**Aumm.fi is a publication of The Genesis Address LLC.**

## Contents

| Path | Role |
|:-----|:-----|
| `index.html` | Single-page app: loads Markdown via `fetch`, renders with [marked](https://github.com/markedjs/marked), theme toggle (Au / Day / Night) |
| [Miliarium Aureum registry](05_miliarium_aureum.md) | **Canonical** registry: slot order **01–28**, compositions, sector tables |
| [miliarium_profiles/](miliarium_profiles/) | One profile per pool (`NN_ixCanonicalName.md`); manifest and sector taxonomy: [Manifest](06_miliarium_manifest.md), [Sectors](07_miliarium_sectors.md), [Token inventory](07a_tokens.md) (deduplicated tickers) |
| Numbered specs `02_*.md` … `16_*.md` | Core protocol docs (mental model, foundations, tokenomics, Miliarium registry, bootstrap, transitions, constitution, formulas, glossary, appendices, UX/UI, overview, team/disclaimer) — see [llms.txt](llms.txt) for full **tab → file** map |
| [Constitution](10_constitution.md), [Tokenomics](04_tokenomics.md), [Protocol formulas](11_formulas.md), … | Immutable law, economics, F-0–F-12 (gauge-challenge deposit **F-12** for non-Miliarium pools; **§xxix** canonical time constants, fee routing, swap-fee bands, Bodensee yield-skim exclusion, `BTC_WRAPPERS`) |
| `llms.txt`, `llms-full.txt`, `sitemap.xml` | **AI / crawler discovery**: human manifest + bulk URL list + XML sitemap of every canonical prose URL (`sitemap.xml` and `llms-full.txt` are **generated** by `scripts/generate_llms_manifest.py`) |
| `robots.txt` | Crawl policy: **all AI crawlers welcome**; `Sitemap: https://aumm.fi/sitemap.xml`; points readers to `llms.txt` / `llms-full.txt` |
| `vercel.json` | Deployment headers (Markdown and manifest files served as UTF-8 `text/markdown` / `text/plain` / `application/xml` where applicable on Vercel); **`ask` query rewrite** to serverless RAG endpoint |
| [ask/](ask/) | RAG query layer: `GET /<page>.md?ask=<question>&goal=<goal>` returns cited JSON answers (Vercel only; see [ask/README.md](ask/README.md), design spec [ASK_SPEC.md](ASK_SPEC.md)) |

## AI agents, crawlers, and tools

This project **welcomes** search indexes, assistants, and research bots to use the public Markdown as grounding context.

- **[llms.txt](llms.txt)** — Structured manifest: reading order, retrieval hints, Governance/Miliarium nav mapping, exclusions (`editorial_sprints.md`, `script.md`), confidentiality note. Compatible with [llmstxt.org](https://llmstxt.org/).
- **[llms-full.txt](llms-full.txt)** — Canonical list of spec URLs (default origin `https://aumm.fi`). Regenerate after adding or renaming `.md` files.
- **[sitemap.xml](sitemap.xml)** — Same corpus as `llms-full.txt` plus `/`, `/llms.txt`, `/llms-full.txt`; submit in Search Console / use for crawler seeding.
- **[robots.txt](robots.txt)** — `Allow: /`; `Sitemap` directive; named AI bots listed for clarity.

`index.html` includes `<link rel="llms-txt" href="/llms.txt">`, a static sidebar block linking to manifests and key `.md` sources, and a `<noscript>` panel with the same links for clients that do not run JavaScript.

### Canonical Claude skill repo (`aumm-skill`)

The skill bundle generated under [`dist/aumm-skill/`](dist/aumm-skill/) is intended for the public repo **[github.com/aummfi-bit/aumm-skill](https://github.com/aummfi-bit/aumm-skill)**. **External tools (ChatGPT browsing, crawlers, other assistants) can only retrieve that corpus if the GitHub repo is public and kept in sync.**

Regenerate references and `_canon.json` after canon edits:

```bash
python3 scripts/generate_llms_manifest.py --skill-out ./dist/aumm-skill
```

Then push those files from `dist/aumm-skill/` to the `aumm-skill` remote (maintainers only). If the repo is private or empty, cite **only** `https://aumm.fi/…` URLs in prompts—not the GitHub path.

## Section numbering (site-wide)

`##` headings use **lowercase Roman numerals with a dot** (e.g. `## i.`, `## ii.`, … `## xxxix.`) in one continuous sequence in nav order: **i.–iv.** Mental Model → **v.–viii.** Theoretical Foundations → **ix.–x.** Tokenomics → **xi.–xii.** Miliarium registry ([05_miliarium_aureum.md](05_miliarium_aureum.md)) → **xiii.–xv.** Manifest → **xvi.–xx.** Sectors → **xxi.–xxv.** Bootstrap → **xxvi.** Transitions → **xxvii.–xxx.** Constitution → **xxxi.–xxxv.** Glossary → **xxxvi.–xl.** Appendices. In [Miliarium Aureum registry](05_miliarium_aureum.md), the registry block is **Section xi** and the AuMM pool block is **Section xii**. **[Overview](15_overview.md)** uses unnumbered `##` headings (not in the sequence). **[Team](16_team.md)** uses **§xl–§xliii** for team, prior work, confidentiality, and disclaimer.

## Spec alignment (current docs)

Normative Markdown reflects a single coherent baseline across the site (gap resolutions and follow-on edits through 2026). For grounding and search, treat these as fixed points:

- **[Mental model](02_mental_model.md):** **AuMM** is the reward token earned by **liquidity** (productive pools). **Bitcoin-style** means **issuance schedule** (cap, halving) for **AuMM**, not mining or minting Bitcoin. **§v. The Flywheel** — reflexive value loop and participant positions ([standalone mirror](02a_flywheel.md)).
- **[Constitution §xxix](10_constitution.md):** Block-number time aliases (`BLOCKS_PER_*`, `MONTH_*_END_BLOCK`, …), EMA sampling (see **F-4**), fee routing to der Bodensee (**protocol share** of swap fees on non–Bodensee **gauged** pools; **LP residual** stays with originating-pool LPs), **ERC-4626 yield skim** from other gauged pools only (Bodensee excluded), swap-fee **bands**, `BTC_WRAPPERS` / F-12, **Composition Challenge** sub-rules (specified-pool model, fee hook on deprecated pools), bounded Stage B multisig window.
- **[Tokenomics §x-a](04_tokenomics.md) / [F-11](11_formulas.md):** Bodensee **Rate Provider** self-yield vs protocol skim; reserve and fee tables match §xxix.
- **[Miliarium / tokens](05_miliarium_aureum.md) / [07a_tokens.md](07a_tokens.md) / profiles:** e.g. **ixCambio** composition (incl. **JPYC**, **tGBP**), **st-EURA** as ERC-4626, **ixViatica** 4626 totals — registry and profiles stay in sync.
- **[UX/UI](14_ux_ui.md):** MVP vs post-MVP scope split; der Bodensee surfaced from genesis.

## Local preview

No build step. Serve the repository root over HTTP (required for `fetch` of `.md` files):

```bash
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

Or: `npx --yes serve -p 8080`

## Deployment (Vercel — production)

**Production host:** [Vercel project `aumm-site`](https://vercel.com/aummfi-bits-projects/aumm-site) (team: `aummfi-bit`). GitHub repo `aummfi-bit/aumm-site` is connected — every push to `main` deploys automatically.

GitHub Pages is **disabled for push** (manual `workflow_dispatch` only) so `aumm.fi` is not served from two hosts.

### One-time DNS cutover

1. Vercel dashboard → **aumm-site** → **Settings** → **Domains** → add `aumm.fi` and `www.aumm.fi`.
2. At your DNS provider, point `aumm.fi` to Vercel (remove the GitHub Pages CNAME target). Vercel shows the exact A/CNAME records after you add the domain.
3. Wait for SSL provisioning (usually minutes).

### Environment variables (Vercel → Settings → Environment Variables)

| Variable | Environments | Purpose |
|----------|--------------|---------|
| `ANTHROPIC_API_KEY` | Production, Preview | **`ask` endpoint** — required for `?ask=` queries |
| `ASK_MODEL` | optional | Override default Claude model |

Without `ANTHROPIC_API_KEY`, the static site works but `GET /<page>.md?ask=…` returns 503.

### Verify after deploy

```bash
curl -s 'https://aumm.fi/llms.txt' | head
curl -s 'https://aumm.fi/04_tokenomics.md?ask=What+is+the+AuMM+maximum+supply' | jq .
```

### Local Vercel CLI

```bash
npx vercel link    # already linked for this repo
npx vercel deploy  # preview
npx vercel --prod  # production
```

Build runs `generate_llms_manifest.py` → `build_ask_index.py` → `append_agent_footer.py` (see `vercel.json`).

## UI notes

- **Intro** is driven by `01_intro.json` (JSON array of typed lines).
- After the intro, **ENTER** goes straight to the documentation (see `index.html`).
- **Navigation** — left **sidebar** (desktop): full doc tree with section anchors under each long page; footer block with canonical manifest / `.md` links for crawlers; **theme** (Au / Day / Night). On narrow viewports the sidebar is a **drawer** (hamburger in the top bar + backdrop).
- **Miliarium** — **Registry** ([05_miliarium_aureum.md](05_miliarium_aureum.md)), **Manifest** ([06_miliarium_manifest.md](06_miliarium_manifest.md)), **Sectors** ([07_miliarium_sectors.md](07_miliarium_sectors.md)), **Tokens** ([07a_tokens.md](07a_tokens.md)); in-app rendering of pool profiles so `.md` links do not open as raw files.
- **Governance** — **Constitution** ([10_constitution.md](10_constitution.md)), **Bootstrap** ([08_bootstrap.md](08_bootstrap.md)), **Transitions** ([09_transitions.md](09_transitions.md)), **Formulas** ([11_formulas.md](11_formulas.md)).
- **Team** — **Team / disclaimer** ([16_team.md](16_team.md)).

## Reading guide

Start with the **[Overview](15_overview.md)** — it contains a [How to Read This Documentation](15_overview.md#how-to-read-this-documentation) section with two audience tracks (LP/Investor and Builder/Auditor) and a one-line index of every file.

## Editing

- Change pool data in the **[Miliarium Aureum registry](05_miliarium_aureum.md)** first, then align [Manifest](06_miliarium_manifest.md) and profiles as needed.
- **[Overview](15_overview.md)** summarizes protocol character at a glance.

### LLM manifest (`llms.txt` / `llms-full.txt`) and sitemap

- **`llms.txt`** — Editable manifest for humans and AI: welcome policy, tab→file table, reading order, exclusions. Site root.
- **`llms-full.txt`** — One absolute URL per canonical Markdown file (and `README.md`); **generated** — do not edit by hand.
- **`sitemap.xml`** — **Generated**; lists the site root, both manifests, and every canonical `.md` URL for search engines.
- After adding or renaming `.md` files (especially under `miliarium_profiles/`), regenerate:

```bash
python3 scripts/generate_llms_manifest.py
```

Use `BASE_URL=https://example.com` if you need a different origin in the output.

Excluded from **`llms-full.txt` / `sitemap.xml`** (not canonical protocol spec): **`editorial_sprints.md`**, **`script.md`**. Supporting **`README.md`** is included.

## License

This protocol forks the Balancer V3 vault and pool contracts under GPL-3.0. Aureum is not affiliated with, endorsed by, or sponsored by Balancer Labs or Balancer DAO.

Protocol design documentation for Project Aureum. **`editorial_sprints.md`** and **`script.md`** are internal / non-normative. **`aureum_schedule.md`** and other auxiliary files may be marked in-file. Treat content as confidential where noted in repository or page footers.

## Disclaimer

**Nothing on Aumm.fi constitutes financial advice.**

Aumm.fi is a publication of **The Genesis Address LLC**. All content in this repository — protocol specifications, tokenomics, the Miliarium Aureum registry, governance documents, formulas, pool profiles, and commentary — is provided **exclusively for educational, informational, and historical research purposes**. It should **not** be construed as investment advice, financial planning guidance, tax or legal advice, policy recommendation, or a solicitation to buy or sell any securities, tokens, or other financial instruments.

DeFi liquidity provision involves substantial risk, including impermanent loss, smart‑contract risk, oracle risk, governance risk, regulatory risk, and the total loss of deposited assets. Forward‑looking statements about emissions, transitions, or governance are subject to change and are not guarantees. References to third‑party protocols are factual and do not imply affiliation or endorsement.

Portions of this documentation were prepared with the assistance of artificial intelligence tools. Readers must **independently verify** any factual claim, contract address, parameter, or formula before acting on it, and should consult qualified professionals about their personal financial, tax, and legal situation. Use of this material is at the reader's sole risk. The Genesis Address LLC, its members, contributors, and affiliates accept no liability for any loss or damage arising from reliance on the contents of Aumm.fi.

See [Team → Disclaimer](16_team.md#xliii-disclaimer) for the on‑site version.
