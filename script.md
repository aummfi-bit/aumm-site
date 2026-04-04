# Script — Required & Suggested Changes

*Review of the Aureum documentation for inconsistencies, incomplete content, and flow improvements.*

---

## Required Changes

### R-1. Era labeling error in appendices.md

**File:** `appendices.md:84`
**Issue:** The Governance Capture row says "fourth root in Era 1" — should be **Era 0**.
**Evidence:** Every other file uses "Era 0" for fourth root:
- `tokenomics.md:76` — "Era 0 (fourth root)"
- `formulas.md:159` — "Era 0 uses fourth-root dampening"
- `aureum_glossary.md:57` — "Era 0 (years 0-4, pre-halving): ... fourth root"

**Fix:** Change "fourth root in Era 1" to "fourth root in Era 0" in the Governance Capture row.

---

### R-2. Six incomplete pool profiles

**Files:**
- `miliarium_profiles/08_ixBrevis.md` (22 lines)
- `miliarium_profiles/09_ixAltrix.md` (22 lines)
- `miliarium_profiles/10_ixMediox.md` (22 lines)
- `miliarium_profiles/21_ixNubix.md` (25 lines)
- `miliarium_profiles/23_ixColossix.md` (25 lines)
- `miliarium_profiles/25_ixMedicix.md` (25 lines)

**Issue:** These profiles have only the Composition table and a one-line Role description. They are missing all of the following sections that every other profile includes (see e.g. `02_ixAetheron.md`, `12_ixStrata.md`, `14_ixAurebit.md` for complete examples at ~50 lines):

| Missing Section | What it should contain |
|:----------------|:----------------------|
| **Real-world analogue** | One-line TradFi comparison |
| **Theme rationale** | Why these specific tokens in this pool |
| **Volume drivers** | Bullet list of expected trading flows |
| **Risk profile** | Bullet list of risk factors |
| **Performance Discipline** | Table with 4626 Quality Gate, Vault TVL floor, Volume percentile floor, Efficiency tournament, CCB multiplier, Composition challenge |
| **Cross-References** | Links to manifest, sectors, theoretical foundation, Miliarium Aureum registry |

**Fix:** Complete each profile following the template used by the other 22 profiles.

---

### R-3. Governance dampening exponents missing from constitution.md canonical list

**File:** `constitution.md` — Section xxix (Immutable Parameters)

**Issue:** The explanatory paragraph at line 84 mentions "governance dampening exponents" as one of three classes of immutable parameters, and the glossary (`aureum_glossary.md:72`) explicitly says "both exponents are immutable." However, the bullet list of canonical immutable parameters (lines 88-96) does not include them.

The bullet list currently ends with:
```
- Core AMM mathematics, CCB formula, and eligibility criteria
- Any withdrawal resets AuMT power
- No admin keys, no multisig, no upgradability, no pause functions
```

**Fix:** Add a bullet to the canonical list:

```
- Governance dampening exponents: fourth root (Era 0, years 0-4), cube root (Era 1+, from first halving block onward) — transition is permanent and occurs once
```

This ensures the canonical source explicitly states the values that every other document references.

---

### R-4. Missing sitemap.xml referenced by robots.txt

**File:** `robots.txt:19`

**Issue:** robots.txt declares `Sitemap: https://aumm.fi/sitemap.xml` but no `sitemap.xml` exists in the repository. Search engines will get a 404.

**Fix:** Either generate a `sitemap.xml` listing all public markdown URLs, or remove the Sitemap directive from `robots.txt`.

---

### R-5. TBD founding team roles in overview.md

**File:** `overview.md:86-88`

**Issue:** Three of four founding team roles are marked **TBD**:
- Smart Contracts — TBD
- Frontend & UX — TBD
- Founding Liquidity — TBD (aligned capital partner)

Only Architecture & Thesis is assigned (Sagix).

**Fix:** Resolve before public launch. Either assign individuals, change to "Seeking [role]", or reframe as open positions.

---

## Suggested Improvements

### ~~S-1. RESOLVED~~ — buyback-and-burn removed; fee model redesigned (single destination: der Bodensee Pool)

### ~~S-2. RESOLVED~~ — same as S-1

---

### S-3. Only ixLibertas named as no-ixEDEL exception

**File:** `aureum_mental_model.md:74`

**Issue:** The text says:

> "ixLibertas (slot 06) is the exception — the USD stable hub holds no ixEDEL."

But ixHelvetia (slot 01) also has no ixEDEL. The earlier sentence ("Twenty-six of the 28") is numerically correct, but this paragraph only names one of the two exceptions. The ixEdelweiss profile (`05_ixEdelweiss.md:27`) correctly names both.

**Suggested fix:** Add ixHelvetia:

> "**ixHelvetia (slot 01)** and **ixLibertas (slot 06)** are the two pools without ixEDEL — ixHelvetia is the pure Frankencoin money market (svZCHF/sUSDS only), and ixLibertas is the seven-token USD stable hub."

---

### S-4. llms.txt reading order vs overview.md Builder track

**File:** `llms.txt` (lines 12-21) vs `overview.md` (lines 22-29)

**Issue:** The two recommended reading orders differ for the Builder/Auditor audience:

| Step | llms.txt | overview.md Builder track |
|:-----|:---------|:--------------------------|
| 1 | overview.md | theoretical_foundation.md |
| 2 | aureum_mental_model.md | constitution.md |
| 3 | **constitution.md** | formulas.md |
| 4 | **theoretical_foundation.md** | bootstrap.md |

`llms.txt` puts constitution before theoretical_foundation; the Builder track in `overview.md` puts theoretical_foundation first "for context on the systems the other files formalize."

**Suggested fix:** Align `llms.txt` with the `overview.md` Builder track order, or add a note in `llms.txt` that the order there is optimised for LLM/RAG ingestion (broad → narrow) rather than human reading.

---

### S-5. Explicit weight basis note in Miliarium_Aureum.md

**File:** `Miliarium_Aureum.md` — Section xi (near the standardised template table, line ~26)

**Issue:** Pool weight percentages (52/16/32, 80/20, etc.) are USD-value-based per the Balancer V3 architecture, but this is never explicitly stated in the registry.

**Suggested fix:** Add a one-liner after the standardised template table:

> "All percentages represent target allocations by **USD value** of the underlying assets, following Balancer V3's value-weighted pool architecture."

---

### S-6. Consolidated "eligible pools" definition

**File:** `constitution.md` — Section xxviii

**Issue:** What constitutes an "eligible pool" for CCB emissions is spread across `constitution.md`, `bootstrap.md`, and `formulas.md`. A reader of the constitution alone may not have full clarity.

**Suggested fix:** Add a one-line definition early in Section xxviii:

> "**Eligible pools** for CCB emissions: the 28 permanent Miliarium Aureum slots plus any external pool with an active, approved gauge that passes all anti-gaming criteria (4626 Quality Gate, TVL floor, volume percentile floor, efficiency tournament)."

---

## Summary

| # | Type | File | Severity |
|:--|:-----|:-----|:---------|
| R-1 | Required | `appendices.md:84` | HIGH — factual error |
| R-2 | Required | 6 pool profiles | HIGH — incomplete content |
| R-3 | Required | `constitution.md §xxix` | MEDIUM — missing canonical parameter |
| R-4 | Required | `robots.txt:19` | MEDIUM — references missing sitemap.xml |
| R-5 | Required | `overview.md:86-88` | LOW — TBD team roles (pre-launch) |
| S-1 | ~~RESOLVED~~ | `tokenomics.md` | Buyback-and-burn removed; fee model redesigned |
| S-2 | ~~RESOLVED~~ | `overview.md` | Same as S-1 |
| S-3 | Suggested | `aureum_mental_model.md:74` | LOW — completeness |
| S-4 | Suggested | `llms.txt` | LOW — alignment |
| S-5 | Suggested | `Miliarium_Aureum.md` | LOW — explicitness |
| S-6 | Suggested | `constitution.md §xxviii` | LOW — clarity |
