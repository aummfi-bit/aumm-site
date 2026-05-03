<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a 03_theoretical_foundation.md — DO NOT EDIT -->
# Theoretical Foundations

## v. Research foundations

The CCB draws on research across multiple disciplines:

**Continuous Capital Corporation (CCC):** Dr. Luzius Meisser’s CCC thesis (*Essays in Decentralized Finance*, 2024) and Frankencoin (ZCHF) demonstrate that a protocol can operate as a fully autonomous corporation — pricing, issuing, and redeeming equity via fixed on-chain rules without discretionary management or a separate treasury. Aureum adopts this as its core design philosophy: emission allocation (CCB), reserve management (der Bodensee Pool), and fee routing are algorithmic and immutable from block 0. No treasury wallet: **Months 1–10** bootstrap AuMM is one-sided into der Bodensee Pool only (see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)); thereafter emissions accrue to LPs per the fixed rules.

**Layered liquidity-risk decomposition:** Sagix’s [four-layer framework](https://www.sagix.io/our-layer-framework/) treats DeFi liquidity risk as a stack of separable layers — venue, routing, anchor, reserve — rather than a single undifferentiated number. The [Sagix Miliarium Aureum](https://www.sagix.io/sagix-miliarium-aureum/), live on Balancer V3 Ethereum mainnet, operationalises that framework with **two** universal cross-pool connectors present in **26 of 28** pools: **svZCHF** as the **deeper, primary routing rail** (deterministic Rate-Provider pricing, yield-bearing ERC-4626, lowest slippage variance) and **ixEDEL** as the **secondary routing / arbitrage-extraction rail** whose NAV mint/redeem cycles bridge otherwise isolated asset clusters. svZCHF additionally serves as the autonomous-reserve anchor (der Bodensee, governance deposits, Incendiary boosts, fee consolidation) — that reserve role sits on top of, not instead of, its cross-pool routing duty. Aureum inherits both anchors — see [Mental model (§iii — Dual anchors)](02_mental_model.md) — and stacks the CCB / EMA discipline layer on top of them.

**Pro-Cyclicality:** BIS research (Aramonte et al., 2022) identifies that most DeFi protocols amplify market moves, creating systemic fragility. The EMA is the direct antidote — algorithmic inertia forces anticyclical behaviour.

**Monetary Rules:** Friedman’s k-percent rule (fixed money supply growth) is the intellectual ancestor of the fixed-emission, halving-based schedule.

**Governance Minimization:** Buterin and Dr. Luzius Meisser argue governance is a security surface. The [0.75–1.25] CCB multiplier collapses the governance attack surface to near-zero.

**Signal Processing:** The EMA is a low-pass filter — “market hype” is noise, “sustained liquidity commitment” is the signal.

**Automatic Stabilizers:** The EMA acts like fiscal automatic stabilizers (unemployment insurance) — elevating yield during crashes without a governance vote.

**Hysteresis:** The EMA gives Aureum institutional memory. Most DeFi is memoryless and reflexive.

---

## vi. CCB: Fully Automatic Allocation

The **Continuous Central Bank (CCB)** is the protocol’s automatic rule that decides how each block’s AuMM emission is split across pools. Two layers: a **scoring layer** built from each pool’s smoothed TVL (the EMA; see §vi-b), and a **multiplier layer** that fine-tunes allocation among the 28 Miliarium pools only (§vii). No committee, no vote, no discretion — the same rules apply at every block, using only on-chain state the contracts can read. It tightens yield during booms and loosens during busts, automatically.

### 1. How pools score and compete

Each **eligible** pool gets a **CCB score** combining its smoothed TVL (EMA) and a **CCB multiplier**. The multiplier applies **only** to the 28 Miliarium pools; for all others it is effectively one. Non-Miliarium gauge-eligible pools still compete on smoothed TVL — they just skip the bi-weekly multiplier adjustments described in §vii.

The CCB turns scores into **shares**: each pool’s share is its score divided by the total score of all eligible pools. Allocation is **relative** — a pool’s emissions depend on how it ranks against every other eligible pool, not on a fixed percentage.

der Bodensee Pool (AuMM/sUSDS/svZCHF three-token weighted pool, fixed 40/30/30) receives **bootstrap** AuMM **Months 1–10** only (one-sided deposits, piecewise decay 80%→50%→0%; see [Miliarium Aureum registry (§xii — der Bodensee)](05_miliarium_aureum.md)). Its TVL is **excluded** from the CCB denominator so it does not dilute emission-eligible pool scores.

### 2. How the block emission flows

**Through the end of Month 10:** each block, a **der Bodensee bootstrap** share (piecewise linear: 80% at genesis → 50% at end of Month 6 → 0% at end of Month 10) is minted as one-sided AuMM into der Bodensee Pool. The **LP emission tranche** is split **evenly** across the 28 Miliarium pools — **one twenty-eighth** each. No treasury wallet. Other pools may exist on the AMM but receive none of this tranche.

**Months 11–12:** the protocol ramps from equal toward full CCB. Early in the window, mostly equal; by the last block of Year 1, fully CCB. At midpoint, half and half. Exact block math is fixed on-chain — see [Constitution (§xxviii)](10_constitution.md).

**After Year 1:** pure CCB. Every eligible pool competes on the same score logic; shares are normalized so the full LP emission pie (after Incendiary) is distributed.

**Incendiary priority skim.** Incendiary Boost claims are paid from the **LP emission tranche** **after** the der Bodensee bootstrap skim (zero after Month 10), **before** the remainder is split by equal blend or CCB. Incendiary is not a multiplier inside the CCB score — it is a first claim on the LP tranche. What remains is what the regime allocates. Anyone can boost any gauged pool by depositing any amount of svZCHF/sUSDS one-sided into der Bodensee; the boost lasts 1 epoch (14 days), starting at the next epoch boundary. Once per epoch per pool. Details in [Bootstrap (§xxii)](08_bootstrap.md) and [Constitution (§xxviii)](10_constitution.md).

### Design rationale

Capital in productive, eligible pools is the **only** input to emission weight. Rules are deterministic and immutable. Governance does not set weights — it exists only for non-emission actions (gauges, fees, composition challenges) under the on-chain-data-only proposal rules in [Constitution](10_constitution.md). Full formal definitions in [Protocol formulas](11_formulas.md).

---

## vi-b. EMA — sustained liquidity signal

For **each** pool separately, the protocol maintains a **60-day exponential moving average** of that pool’s on-chain TVL. A **smoothed** picture of committed capital: today’s raw TVL moves the average only a little; big moves take **weeks** to fully register. The EMA is a low-pass filter — it suppresses one-day noise (hype, panic, a single whale) and passes only **sustained** liquidity commitment.

If a pool’s smoothed TVL is **falling**, its CCB weight falls over time relative to pools whose smoothed TVL is flat or rising. The drop is **not** instantaneous: yesterday’s EMA still counts, so a sudden exit does not erase the pool’s share in one block. But if TVL collapses and stays low, the average eventually reflects that, and emissions shrink. The 28 Miliarium pools are still individual pools with their own EMA series — no special carve-out ignores TVL. What differs for the 28 is the **CCB multiplier** (§vii): only they get automatic adjustments that soften how harshly a relative decline hits compared to a raw TVL-only rule.

---

## vii. CCB Multiplier Engine

The CCB includes an **automatic multiplier adjustment** — a **separate** layer applying **only** to the **28 Miliarium pools**. It does not replace the CCB; it supplies a **multiplier** sitting in the CCB score **on top of** each Miliarium pool’s TVL EMA (and alongside Incendiary terms). **Other** emission-eligible pools do not receive this multiplier: for them it is effectively **one** — still ranked by smoothed TVL, just without the bi-weekly multiplier nudges.

### What the multiplier is trying to do

Liquidity mining often **rewards whatever grew last week** — overpaying hot flows, starving sticky capital. The CCB multiplier pushes back **inside the Miliarium set only**: nudging emission **away** from pools **running hot relative to the constellation** and **toward** pools **lagging the Miliarium average**, within hard floors and ceilings. Anticyclical among the 28 — not a second governance vote, not an oracle.

### Two channels: protocol-wide and within the 28

**Protocol-wide channel:** the rule watches the **direction of total protocol TVL** (smoothed, not a single raw day). When **aggregate** liquidity is **rising**, multipliers across the Miliarium set face **downward** pressure; when falling, **upward** pressure. Coarse macro stabilization: don’t let the whole system behave as if every pool should be maxed out in a boom or abandoned in a bust.

**Within-the-28 channel:** each Miliarium pool is compared to the **average** of the Miliarium set. Pools whose smoothed TVL is **growing faster than that average** get **downward** multiplier nudges; pools **shrinking relative to that average** get **upward** nudges. A pool whose TVL EMA is **dropping** still **loses ground** in the raw TVL part of the score, but the CCB multiplier can **partially offset** that **if** it is weak **relative to the other Miliarium pools** — not merely because the whole market is down together.

### Guards so the rule does not thrash

Multipliers are **clamped** to an immutable band — no pool rewarded or punished without limit. A **dead zone** ignores tiny wiggles so the system does not flip on noise. Steps are **small and discrete** on a fixed cadence (bi-weekly cycle), not continuous social-media sentiment. All numeric bounds (step size, clamp range, dead zone, EMA horizon) are **immutable from block 0** — see [Immutable Parameters (§xxix)](10_constitution.md).

### How the multiplier lines up with Sections vi and vi-b

The CCB always uses **per-pool** smoothed TVL as the backbone of the score. The multiplier **only** adjusts an extra factor for the **28** so that **relative** performance inside the founding constellation can be **taxed or subsidised** without human intervention. Formal update rule: [Protocol formulas (F-8)](11_formulas.md). Glossary form: [Glossary](12_aureum_glossary.md).

### How the multiplier updates

Only the 28 Miliarium pools receive CCB multiplier updates; for any other eligible pool the multiplier is neutral (effectively one). Each bi-weekly cycle, a pool’s multiplier is adjusted by two small steps — one driven by aggregate protocol TVL direction (macro pressure), one by the pool’s TVL relative to the Miliarium average (intra-constellation pressure) — then clamped to a hard floor and ceiling. Initial multiplier: 1.00. Numeric bounds (step size, clamp range, dead zone): [Immutable Parameters (§xxix)](10_constitution.md). Formal update rule: [Protocol formulas](11_formulas.md).

---

## vii-a. CCB and the Multiplier — Plain-English FAQ

**If one Miliarium pool is gaining share of TVL among the 28, what happens?** Two forces: its **TVL EMA** in the CCB score rises as it takes share from siblings, pushing its **weight up**. The CCB multiplier’s **within-the-28** channel compares each pool to the **Miliarium average** — pools **growing faster than that average** get a **downward** nudge (hot flows taxed), **within the immutable band** (see [Constitution (§xxix)](10_constitution.md)). Net effect depends on both forces; it is not “always more” or “always less.”

**If a pool shrinks relative to total protocol TVL (capital moves elsewhere), what happens?** The **CCB score** uses **per-pool** TVL EMA against **all eligible pools** in the denominator. If this pool’s smoothed TVL is lower relative to **other** eligible pools (including non-Miliarium gauges), its **share of total emissions** falls. The CCB multiplier does not define “relative to total protocol TVL” for **delta_intra** — that is **vs the Miliarium average** only. **delta_global** keys off **aggregate protocol TVL direction** (boom vs bust pressure on multipliers), not “Miliarium vs the rest” as a separate basket.

**What is the step size on the CCB multiplier?** See [Immutable Parameters (§xxix)](10_constitution.md) for the exact step size, clamp band, and dead zone — all immutable from block 0.

**If Miliarium pools as a group lose share of protocol TVL (liquidity shifts to other eligible pools), what happens to emissions to the MA pools?** There is **no** fixed “28-pool basket” guarantee. After the equal regime, each pool competes **individually**; **CCB_share** is **Score / sum(scores over all eligible pools)**. If **non-Miliarium** eligible pools grow their scores faster, **MA pools as a group** receive a **smaller** fraction of the same CCB pie. **delta_global** is **not** a “protect the constellation’s share” lever — it is **aggregate** protocol TVL **direction** for multiplier pressure across the 28.

---

## viii. Immutable Reference

See [Immutable Parameters (§xxix)](10_constitution.md).

---

## ix. References

### Prior work by the founding team

See [Team — Prior Work](16_team.md).
