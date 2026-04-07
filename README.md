# AUREUM — Protocol design site

Static documentation and registry for **Project Aureum**: tokenomics, governance bounds, and the **Miliarium Aureum** constellation of **28** immutable liquidity pools.

**Aumm.fi is a publication of The Genesis Address LLC.**

## Contents

| Path | Role |
|:-----|:-----|
| `index.html` | Single-page app: loads Markdown via `fetch`, renders with [marked](https://github.com/markedjs/marked), theme toggle (Au / Day / Night) |
| [Miliarium Aureum registry](05_miliarium_aureum.md) | **Canonical** registry: slot order **01–28**, compositions, sector tables |
| [miliarium_profiles/](miliarium_profiles/) | One profile per pool (`NN_ixCanonicalName.md`); manifest and sector taxonomy: [Manifest](06_miliarium_manifest.md), [Sectors](07_miliarium_sectors.md), [Token inventory](07a_tokens.md) (deduplicated tickers) |
| Numbered specs `02_*.md` … `15_*.md` | Core protocol docs (mental model, foundations, tokenomics, bootstrap, transitions, constitution, formulas, glossary, appendices, UX/UI, overview) — see [llms.txt](llms.txt) for full **tab → file** map |
| [Constitution](10_constitution.md), [Tokenomics](04_tokenomics.md), [Protocol formulas](11_formulas.md), … | Immutable law, economics, F-0–F-12 (incl. gauge-challenge deposit rule for non-Miliarium pools) |
| `llms.txt`, `llms-full.txt` | **AI / LLM manifest** (human-readable guide + one URL per line); `llms-full.txt` is **generated** by `scripts/generate_llms_manifest.py` |
| `robots.txt` | Crawl policy: **all AI crawlers and future agents welcome**; points to `llms.txt` / `llms-full.txt` |

## AI agents, crawlers, and tools

This project **welcomes** search indexes, assistants, and research bots to use the public Markdown as grounding context.

- **[llms.txt](llms.txt)** — Structured manifest: reading order, retrieval hints, Governance/Miliarium nav mapping, exclusions (`editorial_sprints.md`, `script.md`), confidentiality note. Compatible with [llmstxt.org](https://llmstxt.org/).
- **[llms-full.txt](llms-full.txt)** — Canonical list of spec URLs (default origin `https://aumm.fi`). Regenerate after adding or renaming `.md` files.
- **[robots.txt](robots.txt)** — `Allow: /` for all user agents; named AI bots listed for clarity.

`index.html` includes `<link rel="llms-txt" href="/llms.txt">`.

## Section numbering (site-wide)

`##` headings use **lowercase Roman numerals with a dot** (e.g. `## i.`, `## ii.`, … `## xxxix.`) in one continuous sequence in nav order: **i.–iv.** Mental Model → **v.–viii.** Theoretical Foundations → **ix.–x.** Tokenomics → **xi.–xii.** Miliarium registry ([05_miliarium_aureum.md](05_miliarium_aureum.md)) → **xiii.–xv.** Manifest → **xvi.–xx.** Sectors → **xxi.–xxv.** Bootstrap → **xxvi.** Transitions → **xxvii.–xxx.** Constitution → **xxxi.–xxxv.** Glossary → **xxxvi.–xl.** Appendices. In [Miliarium Aureum registry](05_miliarium_aureum.md), the registry block is **Section xi** and the AuMM pool block is **Section xii**. **[Overview](15_overview.md)** uses unnumbered `##` headings (not in the sequence).

## Local preview

No build step. Serve the repository root over HTTP (required for `fetch` of `.md` files):

```bash
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

Or: `npx --yes serve -p 8080`

## UI notes

- **Intro** is driven by `01_intro.json` (JSON array of typed lines).
- After the intro, **ENTER** goes straight to the documentation (see `index.html`).
- **Miliarium ▾** — **Registry** ([05_miliarium_aureum.md](05_miliarium_aureum.md)), **Manifest** ([06_miliarium_manifest.md](06_miliarium_manifest.md)), **Sectors** ([07_miliarium_sectors.md](07_miliarium_sectors.md)), **Tokens** ([07a_tokens.md](07a_tokens.md)); in-app rendering of pool profiles so `.md` links do not open as raw files.
- **Governance ▾** — **Constitution** ([10_constitution.md](10_constitution.md)), **Bootstrap** ([08_bootstrap.md](08_bootstrap.md)), **Transitions** ([09_transitions.md](09_transitions.md)), **Formulas** ([11_formulas.md](11_formulas.md)).

## Reading guide

Start with the **[Overview](15_overview.md)** — it contains a [How to Read This Documentation](15_overview.md#how-to-read-this-documentation) section with two audience tracks (LP/Investor and Builder/Auditor) and a one-line index of every file.

## Editing

- Change pool data in the **[Miliarium Aureum registry](05_miliarium_aureum.md)** first, then align [Manifest](06_miliarium_manifest.md) and profiles as needed.
- **[Overview](15_overview.md)** summarizes protocol character at a glance.

### LLM manifest (`llms.txt` / `llms-full.txt`)

- **`llms.txt`** — Editable manifest for humans and AI: welcome policy, tab→file table, reading order, exclusions. Site root.
- **`llms-full.txt`** — One absolute URL per canonical Markdown file (and `README.md`); **generated** — do not edit by hand.
- After adding or renaming `.md` files (especially under `miliarium_profiles/`), regenerate:

```bash
python3 scripts/generate_llms_manifest.py
```

Use `BASE_URL=https://example.com` if you need a different origin in the output.

Excluded from **`llms-full.txt`** (not canonical protocol spec): **`editorial_sprints.md`**, **`script.md`**. Supporting docs **are** in the manifest: `aureum_schedule.md`, `project_aureum_design_final.md`, `README.md`.

## License

This protocol forks the Balancer V3 vault and pool contracts under GPL-3.0. Aureum is not affiliated with, endorsed by, or sponsored by Balancer Labs or Balancer DAO.

Protocol design documentation for Project Aureum. **`editorial_sprints.md`** and **`script.md`** are internal / non-normative. **`aureum_schedule.md`** and other auxiliary files may be marked in-file. Treat content as confidential where noted in repository or page footers.

## Disclaimer

**Nothing on Aumm.fi constitutes financial advice.**

Aumm.fi is a publication of **The Genesis Address LLC**. All content in this repository — protocol specifications, tokenomics, the Miliarium Aureum registry, governance documents, formulas, pool profiles, and commentary — is provided **exclusively for educational, informational, and historical research purposes**. It should **not** be construed as investment advice, financial planning guidance, tax or legal advice, policy recommendation, or a solicitation to buy or sell any securities, tokens, or other financial instruments.

DeFi liquidity provision involves substantial risk, including impermanent loss, smart‑contract risk, oracle risk, governance risk, regulatory risk, and the total loss of deposited assets. Forward‑looking statements about emissions, transitions, or governance are subject to change and are not guarantees. References to third‑party protocols are factual and do not imply affiliation or endorsement.

Portions of this documentation were prepared with the assistance of artificial intelligence tools. Readers must **independently verify** any factual claim, contract address, parameter, or formula before acting on it, and should consult qualified professionals about their personal financial, tax, and legal situation. Use of this material is at the reader's sole risk. The Genesis Address LLC, its members, contributors, and affiliates accept no liability for any loss or damage arising from reliance on the contents of Aumm.fi.

See [Team → Disclaimer](16_team.md#xliii-disclaimer) for the on‑site version.
