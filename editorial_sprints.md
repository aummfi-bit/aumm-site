# Editorial Sprints — Aureum Protocol Documentation

Fixes organised by priority. Each sprint is self-contained and can be merged independently.

---

## Sprint 1 — CCB Explanation Rewrite
**Files:** `theoretical_foundation.md`
**Impact:** Critical — the protocol's core mechanic is currently fragmented across 350 lines and leaves readers unable to state plainly how emissions are decided.

### Tasks
- [ ] Rewrite §vi opening: separate the EMA-as-scoring-input from the multiplier-as-adjustment into clearly distinct paragraphs before any detail
- [ ] Restructure §vi into three clean subsections: (1) What the EMA does and why, (2) How pools score and compete — normalisation across all eligible pools, (3) How the block reward flows after Incendiary skim
- [ ] Restructure §vii opening to clearly state upfront: "The CCB multiplier is a *separate layer on top of* the base score. It applies only to the 28 Miliarium pools. Non-Miliarium pools use a neutral multiplier of 1."
- [ ] Move the FAQ block (§vii bottom) to a collapsible or appendix section — the Q&A format introduces new concepts mid-explanation and stalls comprehension
- [ ] Remove all within-section back-references ("as explained above", "read Section vi first") and make each subsection self-standing

---

## Sprint 2 — Constellation Routing Explanation
**Files:** `aureum_mental_model.md`
**Impact:** Critical — 26 of 28 pools hold ixEDEL but the routing mechanic is never plainly stated anywhere.

### Tasks
- [ ] Add a "Constellation Routing" subsection to §iii (How Aureum Works) explaining: pool A → ixEdelweiss → pool B, fees on both legs, why ixEDEL appears in 26 pools
- [ ] Explain what ixEdelweiss (slot 05) does differently from the other ixEDEL-holding pools — it is the routing hub, the others are spokes
- [ ] Add one sentence clarifying ixLibertas (slot 06) as the USD stable hub with no ixEDEL — explain why the exception exists
- [ ] Connect the Roman metaphor explicitly: ixEDEL = the via (road), ixEdelweiss = the Miliarium Aureum monument itself

---

## Sprint 3 — Reading Guide and Audience Tracks
**Files:** `overview.md`
**Impact:** High — no reading order is defined; new readers start randomly and get lost.

### Tasks
- [ ] Add a "How to Read This Documentation" section at the top of `overview.md`
- [ ] Define two tracks explicitly:
  - **LP / Investor track:** overview → aureum_mental_model → tokenomics (§ix–x) → one pool profile → appendices (xxxvii, xxxix)
  - **Builder / Auditor track:** constitution → formulas → bootstrap (§xxiii–xxv) → theoretical_foundation → appendices (xxxvi)
- [ ] Add a one-line description of each file's purpose and audience to the reading guide
- [ ] Cross-link the reading guide from `README.md`

---

## Sprint 4 — "Miniature Economy" and 28-Pool Rationale
**Files:** `aureum_mental_model.md`, `miliarium_profiles/sectors.md`
**Impact:** High — the "miniature economy" framing is the strongest conceptual hook but is buried in a taxonomy file; the number 28 is never justified.

### Tasks
- [ ] Move the "miniature economy" concept from `sectors.md` §xvii into `aureum_mental_model.md` §ii (Core Principles) or the Roman Infrastructure section
- [ ] Add an explanation for why 28 pools: enough sectors to weather macro rotation, small enough for on-chain CCB multiplier tracking — state this directly rather than leaving readers to infer it
- [ ] In `sectors.md` §xvii, keep the design principle but reference back to `aureum_mental_model.md` as the canonical intro
- [ ] Add one sentence to the CCB description in `theoretical_foundation.md` connecting the miniature economy framing: "The CCB acts as the central bank of this miniature economy — tightening yield during booms, loosening during busts, automatically"

---

## Sprint 5 — Equal → CCB Transition Motivation
**Files:** `aureum_mental_model.md`, `transitions.md`
**Impact:** High — the mechanics are clear but the *why* is absent: why two months, what pool operators should expect, what this means for LP ROI calculations.

### Tasks
- [ ] Add a motivation paragraph to `aureum_mental_model.md` §iv (Emission Regimes) explaining: why 2 months (gradual vs. abrupt), what pools should expect (emission share will shift; some gain, some lose), and that the TVL EMA needs time to stabilise with real data
- [ ] In `transitions.md` §xxvi (Month 11 entry), add a plain-English note: "Pools that performed well under equal allocation may see their share decline if their TVL lags the protocol average. This is by design — the transition rewards sustained capital, not historical incumbency."
- [ ] Add a note clarifying that the equal regime gives all 28 pools identical treatment regardless of TVL — intentional to bootstrap the constellation before the EMA has meaningful data

---

## Sprint 6 — Governance Exponent Justification
**Files:** `tokenomics.md`, `constitution.md`
**Impact:** High — 4th root (Era 0) and cube root (Era 1+) are stated and the transition is now correctly described as permanent, but *why those specific exponents* is not argued anywhere.

### Tasks
- [ ] In `tokenomics.md` §ix, expand the Era 0 / Era 1+ explanation to argue the design goal: "Governance dampening exponents are chosen to prevent large-capital capture while preserving meaningful voting power for productive LPs."
- [ ] Add the worked example: at genesis a $100M LP in a $1M protocol is 100% of TVL — 4th root compression is necessary; by year 4 in a $1B protocol the same LP is 10% — cube root reflects natural dilution
- [ ] In `constitution.md` §xxix (Immutable Parameters), add a brief context paragraph before the list explaining *why* each class of parameter is immutable: economic constants, anti-gaming safeguards, and anti-capture mechanics

---

## Sprint 7 — Deflationary Crossover Worked Example
**Files:** `tokenomics.md`
**Impact:** Medium — the concept is mentioned but feels aspirational without numbers; a worked example makes it real.

### Tasks
- [ ] Add a worked example to `tokenomics.md` §x ("The Deflationary Crossover") using a realistic TVL and volume assumption (e.g. $100M TVL, $20M average daily volume)
- [ ] Show the calculation: swap fee burn + yield fee burn vs. Era 0 emission rate vs. Era 1+ emission rate
- [ ] State clearly at which era the crossover is structurally expected and what drives it (TVL growth, not token price)
- [ ] Add a note: "This calculation is illustrative; actual crossover depends on protocol TVL and fee revenue at the time"

---

## Sprint 8 — Composition Challenge Mechanics
**Files:** `bootstrap.md`, `constitution.md`
**Impact:** Medium — the mechanic is described but ambiguous for edge cases that real operators will face.

### Tasks
- [ ] Add a concrete worked example to `bootstrap.md` §xxiv: the cbBTC delisting scenario — what clearly qualifies (tBTC — same asset type), what clearly doesn't (physical gold — different asset class), and what is borderline (Bitcoin L2 token — requires 2/3 to judge "similar economic properties")
- [ ] Clarify whether a composition challenge can replace both theme assets simultaneously or must be done in two separate votes
- [ ] Clarify "like-for-like renewal only" more precisely: same sector, same risk profile, same template role (yield core vs. routing vs. theme)

---

## Sprint 9 — Price Ceiling and Low-Turnout Precision
**Files:** `tokenomics.md`, `constitution.md`
**Impact:** Medium — both mechanisms are currently described in terms too vague to be actionable.

### Tasks
- [ ] **Price ceiling** (`tokenomics.md` §x): specify what "fixed multiple of trailing fundamentals" means — define the fundamental metric (protocol revenue per circulating AuMM), the multiple, and how the ceiling is calculated on-chain
- [ ] **Low-turnout safeguard** (`tokenomics.md` §ix, `constitution.md` §xxvii): replace "very low turnout" with a specific threshold; specify which proposal types auto-fail vs. enter timelock; specify the timelock duration

---

## Sprint 10 — Repetition and Parameter Canonicalisation
**Files:** `constitution.md`, all files referencing CCB parameters
**Impact:** Medium — CCB multiplier parameters are restated in 7 files; "28 Miliarium Aureum pools" appears 34 times with inconsistent variants.

### Tasks
- [ ] Designate `constitution.md` §xxix as the canonical source for all immutable parameters
- [ ] In every other file that restates CCB multiplier bounds, step size, dead zone, or EMA horizon: replace the inline restatement with a citation — "See Immutable Parameters (`constitution.md` §xxix)"
- [ ] Standardise the primary term for the founding pools: choose one form (e.g. "the 28 Miliarium pools") and apply it consistently; reserve "immutable" qualifier only for sentences where immutability is the point
- [ ] Standardise "block emission rate" as the primary term (replacing "block reward," "per-block emission," "emission_per_block" — keep the formula variable name in `formulas.md` only)
- [ ] Audit the EMA explanation: it appears in 5 files; designate `theoretical_foundation.md` §vi as canonical; replace full re-explanations in other files with one-sentence summaries + cross-reference

---

## Sprint 11 — bootstrap.md Restructure
**Files:** `bootstrap.md`
**Impact:** Medium — the gauge-as-prerequisite is buried at the end of §xxi instead of stated upfront; the sequence is unclear on first read.

### Tasks
- [ ] Move "All layers require gauge approval first" to the opening sentence of §xxi, not the closing
- [ ] Restructure §xxi to state the prerequisite model clearly: "Gauge approval is the single gate. Without it: no emissions, no Incendiary Boost, no 90-day multiplier. With it: the following mechanisms become available…"
- [ ] Introduce Incendiary Boost and 90-day gauge boost explicitly as *optional, post-approval* mechanisms
- [ ] Clarify that a pool can have the 90-day boost *without* Incendiary (automatic on gauge approval) and *with* Incendiary (operator-funded, stacked on top)

---

*Each sprint should be committed and merged independently. Sprints 1–3 have the highest reader impact and should be prioritised first.*
