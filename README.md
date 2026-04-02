# AUREUM — Protocol design site

Static documentation and registry for **Project Aureum**: tokenomics, governance bounds, and the **Miliarium Aureum** constellation of **28** immutable liquidity pools.

## Contents

| Path | Role |
|:-----|:-----|
| `index.html` | Single-page app: loads Markdown via `fetch`, renders with [marked](https://github.com/markedjs/marked), theme toggle (Au / Day / Night) |
| `Miliarium_Aureum.md` | **Canonical** registry: slot order **01–28**, compositions, sector tables |
| `miliarium_profiles/` | One profile per pool (`NN_ixCanonicalName.md`), plus `manifest.md` and `sectors.md` |
| `constitution.md`, `tokenomics.md`, `PMAR.md`, … | Core protocol specs |

## Section numbering (site-wide)

`##` headings in the main tabs follow **one continuous Roman sequence** in nav order: **I–IV** Mental Model → **V–VIII** Theoretical Foundations → **IX–X** Tokenomics → **XI–XII** Miliarium registry (`Miliarium_Aureum.md`) → **XIII–XV** Manifest → **XVI–XX** Sectors → **XXI–XXV** Bootstrap → **XXVI** Transitions → **XXVII–XXX** Constitution → **XXXI–XXXV** Glossary → **XXXVI–XXXIX** Appendices. In `Miliarium_Aureum.md`, the registry block is **Section XI** and the AuMM pool block is **Section XII**. **`overview.md`** uses unnumbered `##` headings (not in the sequence).

## Local preview

No build step. Serve the folder over HTTP (required for `fetch` of `.md` files):

```bash
cd aumm-site
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

Or: `npx --yes serve -p 8080`

## UI notes

- **Intro** is driven by `intro.md` (JSON array of typed lines).
- After the intro, a gate prompts for the Tessera (see `index.html`); this is a presentation layer for the static bundle.
- **Miliarium ▾** in the nav opens **Registry** (`Miliarium_Aureum.md`), **Manifest**, **Sectors**, and in-app rendering of pool profile files so `.md` links do not open as raw files.

## Editing

- Change pool data in **`Miliarium_Aureum.md`** first, then align `miliarium_profiles/manifest.md` and profiles as needed.
- **`overview.md`** summarizes protocol character at a glance.

## License / confidentiality

Content is marked confidential where noted in-page (e.g. footer). Treat distribution accordingly.
