# Theoretical Foundations
## v. Research foundations

The CCB draws from established research across multiple disciplines:

**Autonomous Corporate Logic:** Meisser’s “Continuous Capital Corporation” (2022) argues that a corporation can operate via continuous algorithms rather than board meetings — the foundational logic for the CCB as an autonomous institution.

**Pro-Cyclicality:** BIS research (Aramonte et al., 2022) identifies that most DeFi protocols amplify market moves, creating systemic fragility. The EMA is the direct antidote — algorithmic inertia forces anticyclical behaviour.

**Monetary Rules:** Friedman’s k-percent rule (fixed money supply growth) is the intellectual ancestor of the fixed-emission, halving-based schedule.

**Governance Minimization:** Buterin and Meisser argue governance is a security surface. The [0.75–1.25] CCB multiplier collapses the governance attack surface to near-zero.

**Signal Processing:** The EMA is a low-pass filter — “market hype” is noise, “sustained liquidity commitment” is the signal.

**Automatic Stabilizers:** The EMA acts like fiscal automatic stabilizers (unemployment insurance) — elevating yield during crashes without requiring a governance vote.

**Hysteresis:** The EMA gives Aureum institutional memory. Most DeFi is memoryless and reflexive.

### Prior work by the founding team

- **The DRUID Deep Dive** — Routing architecture and aggregator thesis. [www.sagix.io/the-druid-deep-dive/](https://www.sagix.io/the-druid-deep-dive/)
- **The Layer Framework** — Layered DeFi infrastructure model. [www.sagix.io/our-layer-framework/](https://www.sagix.io/our-layer-framework/)
- **Sagix Miliarium Aureum** — Original constellation design, live on Balancer V3 Ethereum mainnet. [www.sagix.io/sagix-miliarium-aureum/](https://www.sagix.io/sagix-miliarium-aureum/)
- **The Risk Premium Problem** — Governance centralisation analysis, published on Leviathan News. Direct catalyst for the fork. [www.sagix.io/the-risk-premium-problem/](https://www.sagix.io/the-risk-premium-problem/)

---

## vi. CCB: Fully Automatic Allocation

The **Continuous Central Bank (CCB)** is the protocol’s automatic rule that decides how each block’s AuMM emission is split across pools. It has two distinct layers: a **scoring layer** built from each pool’s smoothed TVL (the EMA), and a **multiplier layer** that fine-tunes allocation among the 28 Miliarium pools only (§vii). No committee, no vote, no discretion — the same rules apply at every block, using only on-chain state the contracts can read. The CCB acts as the central bank of the Miliarium economy — tightening yield during booms, loosening during busts, automatically.

### 1. What the EMA does and why

For **each** pool separately, the protocol maintains a **60-day exponential moving average** of that pool’s on-chain TVL. Think of it as a **smoothed** picture of how much capital is committed there: today’s raw TVL moves the average only a little; big moves take **weeks** to fully show up. That is intentional — the EMA is a low-pass filter that suppresses one-day noise (hype, panic, a single whale) and passes only **sustained** liquidity commitment.

If a pool’s smoothed TVL is **falling**, its weight in the CCB score tends to fall over time relative to pools whose smoothed TVL is flat or rising. The drop is **not** instantaneous: yesterday’s EMA still counts, so a sudden exit does not erase the pool’s share in one block. Conversely, if TVL collapses and stays low, the average eventually reflects that, and the pool’s share of total emissions shrinks. The 28 Miliarium pools are still individual pools with their own EMA series — there is no special carve-out that ignores TVL. What is special about the 28 is the **CCB multiplier** (§vii): only they get automatic adjustments that can soften how harshly a relative decline hits compared to a raw TVL-only rule.

### 2. How pools score and compete

Each **eligible** pool gets a **CCB score** combining its smoothed TVL (EMA) and a **CCB multiplier**. The multiplier applies **only** to the 28 Miliarium pools; for all other eligible pools it is effectively one. Gauge-eligible pools that are not among the 28 still compete on smoothed TVL — they just do not receive the bi-weekly multiplier adjustments described in §vii.

The CCB turns scores into **shares**: each pool’s share is its score divided by the sum of scores of all eligible pools. Allocation is **relative** — a pool’s emissions depend on how it compares to every other eligible pool, not on a fixed headline percentage.

The AuMM trading pool (AuMM / svZCHF · sUSDS) receives **no emissions** (see `Miliarium_Aureum.md` §xii). Its TVL is **excluded** from the denominator so that it does not dilute the scores of emission-eligible pools.

### 3. How the block emission flows

**Through the end of Month 10:** the Miliarium emission tranche is split **evenly** — each of the 28 Miliarium pools gets one twenty-eighth. Other pools may exist on the AMM but do not receive this equal slice.

**Months 11–12:** the protocol ramps from equal toward full CCB. Early in the window the mix is mostly equal; by the last block of Year 1 it is fully CCB. At the midpoint, the blend is half equal and half CCB. Exact block math is fixed on-chain — see `constitution.md` §xxviii.

**After Year 1:** allocation is pure CCB. Every eligible pool competes on the same score logic, and shares are normalized so the whole emission pie (after Incendiary) is distributed.

**Incendiary priority skim.** Incendiary Boost claims are paid out of the block emission **before** the remainder is split by the CCB. Incendiary is not a multiplier inside the CCB score; it is a first claim on the fixed per-block mint. What is left after those claims is what the CCB allocates. Details are in `bootstrap.md` §xxii and `constitution.md` §xxviii.

### Design rationale

Capital in productive, eligible pools is the **only** input to emission weight. Rules are deterministic and immutable. Governance does not set weights; it remains available only for non-emission actions (gauges, treasury, fees, composition challenges) under the on-chain-data-only proposal rules in `constitution.md`. For full formal definitions of every formula, see `formulas.md`.

---

## vii. CCB Multiplier Engine

The CCB includes an **automatic multiplier adjustment** that is a **separate** layer that applies **only** to the **28 Miliarium pools**. It does not replace the CCB; it supplies a **multiplier** that sits in the CCB score **on top of** each Miliarium pool’s TVL EMA (and alongside Incendiary terms). **Other** emission-eligible pools do not receive this multiplier: for them, the multiplier in the score is effectively **one** — they are still ranked by smoothed TVL and the rest of the rules, but they do not get the bi-weekly multiplier nudges.

### What the multiplier is trying to do

Liquidity mining often **rewards whatever grew last week**, which can overpay hot flows and starve sticky capital. The CCB multiplier pushes back **inside the Miliarium set only**: it nudges emission **away** from pools that are **running hot relative to the rest of the constellation** and **toward** pools that are **lagging the Miliarium average**, within hard floors and ceilings. So it is **anticyclical among the 28**, not a second governance vote and not an oracle.

### Two channels: protocol-wide and within the 28

**Protocol-wide channel:** the rule watches the **direction of total protocol TVL** (again using a smoothed, memory-bearing picture, not a single raw day). When **aggregate** liquidity is **rising**, multipliers across the Miliarium set face **downward** pressure; when aggregate liquidity is **falling**, they face **upward** pressure. The idea is coarse macro stabilization: don’t let the whole system behave as if every pool should be maxed out in a boom or abandoned in a bust.

**Within-the-28 channel:** each Miliarium pool is compared to the **average** of the Miliarium set. Pools whose smoothed TVL is **growing faster than that average** get **downward** nudges on the multiplier; pools that are **shrinking relative to that average** get **upward** nudges. So a pool whose TVL EMA is **dropping** still **loses ground** in the raw TVL part of the score, but the CCB multiplier can **partially offset** that **if** it is weak **relative to the other Miliarium pools**, not merely because the whole market is down together.

### Guards so the rule does not thrash

Multipliers are **clamped** to an immutable band so no pool can be rewarded or punished without limit. A **dead zone** ignores tiny wiggles in the ratios so the system does not constantly flip on noise. Steps are **small and discrete** on a fixed cadence (bi-weekly cycle), not continuous social-media sentiment. All numeric bounds (step size, clamp range, dead zone, EMA horizon) are **immutable from block 0** — see Immutable Parameters (`constitution.md` §xxix) for the exact values.

### How the multiplier lines up with Section vi

The CCB always uses **per-pool** smoothed TVL as the backbone of the score. The multiplier **only** adjusts an extra factor for the **28** so that **relative** performance inside the founding constellation can be **taxed or subsidised** without human intervention. The formal update rule is in `formulas.md` (F-8); `aureum_glossary.md` covers the same mechanics in glossary form.

### How the multiplier updates

Only the 28 Miliarium pools receive CCB multiplier updates; for any other eligible pool the multiplier is neutral (effectively one). Each bi-weekly cycle, a pool’s multiplier is adjusted by two small steps — one driven by the direction of total protocol TVL (macro pressure) and one by the pool’s TVL relative to the Miliarium average (intra-constellation pressure) — then clamped to a hard floor and ceiling so no pool can be rewarded or punished without limit. Initial multiplier is 1.00. For all numeric bounds (step size, clamp range, dead zone), see Immutable Parameters (`constitution.md` §xxix). For the formal update rule, see `formulas.md`.

---

## vii-a. CCB and the Multiplier — Plain-English FAQ

**If one Miliarium pool is gaining share of TVL among the 28, what happens?** Two forces: its **TVL EMA** in the CCB score tends to rise as it takes share from siblings, which pushes its **weight up**. The CCB multiplier’s **within-the-28** channel compares each pool to the **Miliarium average** — pools **growing faster than that average** get a **downward** nudge on the multiplier (hot flows taxed), **within the immutable band** (see `constitution.md` §xxix). Net effect on that pool’s emissions depends on both; it is not “always more” or “always less.”

**If a pool shrinks relative to total protocol TVL (capital moves elsewhere), what happens?** The **CCB score** uses **per-pool** TVL EMA against **all eligible pools** in the denominator. If this pool’s smoothed TVL is lower relative to **other** eligible pools (including non-Miliarium gauges), its **share of total emissions** tends to fall. The CCB multiplier does not define “relative to total protocol TVL” for **delta_intra** — that is **vs the Miliarium average** only. **delta_global** keys off **aggregate protocol TVL direction** (roughly: boom vs bust pressure on multipliers), not “Miliarium vs the rest” as a separate basket.

**What is the step size on the CCB multiplier?** See Immutable Parameters (`constitution.md` §xxix) for the exact step size, clamp band, and dead zone — all immutable from block 0.

**If Miliarium pools as a group lose share of protocol TVL (liquidity shifts to other eligible pools), what happens to emissions to the MA pools?** There is **no** fixed “28-pool basket” guarantee in the written rules. After the equal regime, each pool competes **individually**; **CCB_share** is **Score / sum(scores over all eligible pools)**. If the **non-Miliarium** eligible pools grow their scores faster, **MA pools as a group** can receive a **smaller** fraction of the same CCB pie. **delta_global** is **not** a dedicated “protect the constellation’s share” lever — it is **aggregate** protocol TVL **direction** for multiplier pressure across the 28.

---

## viii. Immutable Reference

See Immutable Parameters (`constitution.md` §xxix).
