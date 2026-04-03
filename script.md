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

## Suggested Improvements

### S-1. "Two destinations" phrasing in tokenomics.md

**File:** `tokenomics.md:147`

**Issue:** Immediately after the fee split table (which shows three rows: LP bonus 50%, buyback-and-burn 25%, der Bodensee 25%), the text says:

> "There is no treasury. All protocol revenue flows to two destinations only: buyback-and-burn (deflationary pressure) and der Bodensee Pool (autonomous reserve depth)."

The intent is correct — LP bonus is the LP's own share of swap fees, not "protocol revenue" in the captured sense. But a reader scanning the table and then the sentence will see 3 rows → "two only" and be confused.

**Suggested fix:** Add a parenthetical or adjust to:

> "There is no treasury. Protocol-captured revenue flows to two destinations only: buyback-and-burn (deflationary pressure) and der Bodensee Pool (autonomous reserve depth). The remaining 50% of swap fees returns directly to LPs as LP bonus."

---

### S-2. Same "two destinations" phrasing in overview.md

**File:** `overview.md:61`

**Issue:** Same pattern as S-1:

> "All protocol revenue flows automatically to two immutable destinations:"

Then lists buyback-and-burn and der Bodensee Pool. LP bonus (50% of swap fees) is not mentioned at all on this page.

**Suggested fix:** After the two bullet points, add:

> "50% of swap fees returns directly to LPs as LP bonus (see `tokenomics.md` §x)."

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
| S-1 | Suggested | `tokenomics.md:147` | LOW — clarity |
| S-2 | Suggested | `overview.md:61` | LOW — clarity |
| S-3 | Suggested | `aureum_mental_model.md:74` | LOW — completeness |
| S-4 | Suggested | `llms.txt` | LOW — alignment |
| S-5 | Suggested | `Miliarium_Aureum.md` | LOW — explicitness |
| S-6 | Suggested | `constitution.md §xxviii` | LOW — clarity |
