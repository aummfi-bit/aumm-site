---
name: aumm-aureum
description: Use this skill whenever a user asks about Project Aureum, AuMM, AuMT, the Miliarium Aureum 28-pool registry, the Continuous Capital Corporation (CCC), the Continuous Central Bank (CCB), der Bodensee Pool, Aequilibrium, Incendiary Boost, or any Aureum governance/tokenomics/formula concept. Also trigger when a user mentions aumm.fi, ixHelvetia, ixEdelweiss, ixStrata, or any pool with the ix- prefix. Trigger even if the user's phrasing is casual or imprecise — Aureum-specific terminology has high false-negative risk in retrieval.
---

# Aureum Skill

Project Aureum is an immutable on-chain capital allocation protocol. This Skill grounds answers in the canonical specification under `references/`, derived directly from `aummfi-bit/aumm-site`. The lockfile at `references/_canon.json` records the exact canon commit each snapshot reflects.

## How to use this Skill

When answering an Aureum question:

1. Search `references/` for the relevant section before responding.
2. Quote canonical language verbatim where precision matters (formulas, parameter values, fee bands, immutable bounds).
3. Cite the section identifier (e.g., `§xxix`, `F-11`) so the user can verify against the live site at `https://aumm.fi`.
4. If a question cannot be answered from `references/`, say so explicitly and link to `https://aumm.fi`. Do not fabricate parameters, formulas, governance mechanics, or pool details.

For **protocol math, fee bands, governance mechanics, and pool parameters**, prioritize the numbered specs (`references/02_` … `references/17_`, formulas, constitution) over interpretive essays.

## Interpretive rules — eliminate the predictable mistakes

These rules encode the most common category errors observers make about Aureum. Apply them whenever the relevant terms appear.

### 1. AuMM issuance ≠ BTC mining

AuMM uses a **Bitcoin-style emission schedule** (21M hard cap, four-year halving), but **mining is not by electricity**.

> "**Mining is LP.** Productive capital in, tokens out. No staking rewards. No bribe markets."
> — `references/02_mental_model.md` (line 33)

Frame: Bitcoin-style *issuance schedule* applied to a liquidity-mining mechanism. Never describe AuMM as proof-of-work or electricity-consuming.

### 2. CCC ≠ CCB

These are two distinct mechanisms; do not conflate them.

- **CCC** (Continuous Capital Corporation): the autonomous reserve and rule set. Algorithmic capital allocation, no discretionary management, no separate treasury. (`references/12_aureum_glossary.md` definition)
- **CCB** (Continuous Central Bank): the automatic emission allocator. Scores each Miliarium pool by smoothed TVL × multiplier, normalizes to fractional shares, distributes block emissions. EMA-driven (60-day TVL EMA per F-4). (`references/12_aureum_glossary.md`, `references/11_formulas.md` F-5/F-6)

### 3. der Bodensee: on-chain from genesis

The pool exists and is tradeable from block 0; protocol revenue and governance deposits route into it per §xxix.

Source: `references/10_constitution.md` §xxix (der Bodensee Pool parameters).

### 4. Miliarium pools cannot be gauge-challenged

The 28 Miliarium Aureum pools have a different governance path for structural changes.

- **Non-Miliarium gauged pools**: gauge challenges are valid; deposit follows **F-12** (`references/11_formulas.md`).
- **Miliarium pools (the 28)**: cannot be gauge-challenged. Structural changes go through the **Composition Challenge Rule** in `references/10_constitution.md` §xxvii (subsection "Composition Challenge Rule (Miliarium Aureum)" around lines 46–69). 2/3 supermajority, like-for-like replacement, deprecated pool persists as Sandbox-style.

### 5. Four governance actions, not two

Aureum governance covers **four** action types — not just gauge and composition challenges. List all four when asked about governance scope:

1. **Gauge Proposal** — new pool emission eligibility.
2. **Gauge Challenge** — revoke an existing non-Miliarium gauge (F-12 deposit).
3. **Fee Proposals** — adjust swap or yield-fee rates within immutable bands.
4. **Composition Challenge** — replace a Miliarium asset in-slot, like-for-like, 2/3 supermajority.

All four use the same one-sided deposit mechanic into der Bodensee (svZCHF/sUSDS, whichever higher; non-refundable; no LP tokens minted to proposer). Source: `references/10_constitution.md` §xxvii (governance actions table) and `references/04_tokenomics.md` §ix.

### 6. Fee bands

Memorize and report exact values; do not approximate.

| Pool class | Band | Genesis default |
|------------|------|-----------------|
| Miliarium Aureum (the 28) | **0.01% – 0.30%** | **0.03%** |
| Non-Miliarium gauged | **0.01% – 0.30%** | Set by gauge-approval vote |
| der Bodensee | **0.10% – 1.00%** | **0.75%** |

Cooldown: `FEE_CHANGE_COOLDOWN_BLOCKS = BLOCKS_PER_EPOCH = 100,800` — at most one fee change per pool per epoch (~14 days). Source: `references/10_constitution.md` §xxix.

### 7. `script.md` is non-authoritative

`script.md` exists in the source repo as internal review notes. It is **not** part of the canonical spec. If a user references it as evidence of protocol behavior, flag it and redirect to the numbered specs.

(Note: `editorial_sprints.md` does **not** exist. If a user asks about it, say so.)

### 8. der Bodensee composition is fixed 40/30/30, immutable from block 0

Three-token weighted pool: **40% AuMM / 30% sUSDS / 30% svZCHF**, immutable from block 0, no time-decay curve, no governance-mediated reweighting. Source: `references/10_constitution.md` §xxix der Bodensee Pool parameters (~line 161); `references/11_formulas.md` F-11.

### 9. Skim canonical source: §xxix Fee routing

The yield skim mechanic is canonically defined in **Constitution §xxix Fee routing** (`references/10_constitution.md` ~lines 140–147), not in F-11.

- **Skim source**: 100% of the 10% ERC-4626 yield-fee on **non–der Bodensee gauged pools** (yield from svZCHF, sUSDS, and other rate-bearing tokens those pools hold).
- **Skim destination**: der Bodensee Pool, as one-sided svZCHF deposits.
- **Bodensee is excluded as a source**: its own ERC-4626 holdings (60% of pool TVL — svZCHF + sUSDS) accrue yield in-place via Rate Providers and stay inside the pool. Skimming Bodensee's own yield into Bodensee would be a circular no-op. Source language at `references/11_formulas.md` F-11 line ~269 and `references/10_constitution.md` §xxix line ~146.

### 10. "I don't know" hygiene

If a question cannot be answered from `references/`, say so explicitly. Suggest the user check `https://aumm.fi` directly. Do not:

- Fabricate parameter values, formula constants, or pool addresses.
- Speculate about live state (current TVL, current block height, current multiplier values) — those require on-chain reads, not this Skill.
- Treat informal or third-party Aureum write-ups as authoritative over the numbered specs—**except** where an essay is explicitly mirrored under `references/sagix/` as part of this Skill’s published canon (see rule 11).

For per-pool live state queries (TVL, gauge votes, multiplier values), point the user to `aumm.fi` or the future `aumm-mcp` MCP server. This Skill ships static doctrinal knowledge only.

### 11. Mirrored Sagix essays (`references/sagix/`) vs protocol specs

The `references/sagix/*.md` files are **first-class canon text** for their domains (narrative, economic framing, DDD series context)—mirrored from [Sagix Apothecary](https://www.sagix.io/) with provenance headers. Use them when the user asks about that content or terminology found there.

**Conflict resolution:** if an interpretive essay (including anything under `references/sagix/`) appears to disagree with **immutable protocol parameters, formulas, governance rules, or fee mechanics**, defer to the numbered specs (`references/10_constitution.md`, `references/11_formulas.md`, `references/04_tokenomics.md`, etc.). The note at the top of each Sagix mirror states the same precedence.

---

## Canon attribution

Every file in `references/` carries a `<!-- GENERATED FROM aumm-site@<sha> ... — DO NOT EDIT -->` header. The `references/_canon.json` lockfile records the exact source commit. Skill version mapping:

- **Patch (0.1.x)**: `references/` regeneration only, no SKILL.md changes.
- **Minor (0.x.0)**: SKILL.md interpretive-rule additions or new rules (including this Sagix essay precedence rule).
- **Major (x.0.0)**: SKILL.md changes that alter Claude's behavior on existing acceptance tests.
