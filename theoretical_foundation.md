# Theoretical Foundations
## v. Research foundations

The CCB draws from established research across multiple disciplines:

**Autonomous Corporate Logic:** Meisser’s “Continuous Capital Corporation” (2022) argues that a corporation can operate via continuous algorithms rather than board meetings — the foundational logic for the CCB as an autonomous institution.

**Pro-Cyclicality:** BIS research (Aramonte et al., 2022) identifies that most DeFi protocols amplify market moves, creating systemic fragility. The EMA is the direct antidote — algorithmic inertia forces anticyclical behaviour.

**Monetary Rules:** Friedman’s k-percent rule (fixed money supply growth) is the intellectual ancestor of the fixed-emission, halving-based schedule.

**Governance Minimization:** Buterin and Meisser argue governance is a security surface. The ±10% Pioneer multiplier collapses the governance attack surface to near-zero.

**Signal Processing:** The EMA is a low-pass filter — “market hype” is noise, “sustained liquidity commitment” is the signal.

**Automatic Stabilizers:** The EMA acts like fiscal automatic stabilizers (unemployment insurance) — elevating yield during crashes without requiring a governance vote.

**Mechanism Design (Roth/Maskin):** Routing unqualified votes to buyback-and-burn makes every outcome — productive allocation or misdirected votes — beneficial to protocol health.

**Hysteresis:** The EMA gives Aureum institutional memory. Most DeFi is memoryless and reflexive.

### Prior work by the founding team

- **The DRUID Deep Dive** — Routing architecture and aggregator thesis. [www.sagix.io/the-druid-deep-dive/](https://www.sagix.io/the-druid-deep-dive/)
- **The Layer Framework** — Layered DeFi infrastructure model. [www.sagix.io/our-layer-framework/](https://www.sagix.io/our-layer-framework/)
- **Sagix Miliarium Aureum** — Original constellation design, live on Balancer V3 Ethereum mainnet. [www.sagix.io/sagix-miliarium-aureum/](https://www.sagix.io/sagix-miliarium-aureum/)
- **The Risk Premium Problem** — Governance centralisation analysis, published on Leviathan News. Direct catalyst for the fork. [www.sagix.io/the-risk-premium-problem/](https://www.sagix.io/the-risk-premium-problem/)

---

## vi. CCB: Fully Automatic Allocation

The **Continuous Central Bank (CCB)** is the protocol’s automatic rule that decides how each block’s AuMM emission is split across pools. No committee, no vote, no discretion: the same rules apply at every block, using only on-chain state the contracts can read (chiefly liquidity and eligibility flags).

### How the regime unfolds in time

**Through the end of Month 10 (Year 1):** the emission tranche that goes to the Miliarium constellation is split **evenly** across the **28** immutable Miliarium Aureum pools — each gets **one twenty-eighth** of that tranche. Other pools may exist on the AMM, but they do not receive this equal slice.

**Months 11 and 12:** the protocol **ramps** from that equal method toward the full CCB method. Early in the window, the mix still looks mostly like equal one-twenty-eighths; by the last block of Year 1, the mix is **fully** CCB. Halfway through the two-month window, the blend is literally half equal and half CCB. (Exact block math is fixed on-chain; see `constitution.md`.)

**From the first block after Year 1 onward:** allocation is **pure CCB**. Every eligible pool competes on the same score logic, and shares are normalized so the whole emission pie (after Incendiary, below) is distributed.

### What “TVL EMA(60)” means, pool by pool

For **each** pool separately, the protocol maintains a **60-day exponential moving average** of that pool’s on-chain TVL. Think of it as a **smoothed** picture of how much capital is committed there: today’s raw TVL moves the average only a little; big moves take **weeks** to fully show up. That is intentional. Spot TVL can spike or crash in a day from hype, panic, or a single whale; the EMA **filters out one-day noise** and keeps something closer to **sustained** liquidity. So the allocation signal is **per pool**, not one global number and not a single snapshot.

If a pool’s **smoothed** TVL is **falling**, its weight in the CCB score **tends to fall** over time relative to pools whose smoothed TVL is flat or rising — because the score is built from that per-pool average. The drop is **not** instantaneous: yesterday’s EMA still counts, so a sudden exit does not erase the pool’s share in one block. Conversely, if TVL collapses and stays low, the average **eventually** reflects that, and the pool’s **share of total emissions** shrinks. There is no special carve-out that says “Miliarium pools ignore TVL” — the **28** are still individual pools with their own EMA series. What **is** special about the 28 is **PMAR** (Section vii): only they get automatic multiplier adjustments inside a band, which can **soften** how harshly a relative decline hits compared to a raw TVL-only rule.

### Score, eligible pools, and the emission pie

After **Incendiary Boost** claims are paid from the block (below), each **eligible** pool gets a **CCB score** built from: the pool’s **smoothed** TVL (EMA), a **PMAR** multiplier that **only** applies to the **28 Miliarium** pools (and is **neutral** for all other eligible pools), and the **Incendiary multiplier** term defined in `constitution.md` (distinct from Boost claims). **Gauge-eligible pools that are not among the 28** still compete with smoothed TVL and the neutral PMAR slot; they do not receive the Miliarium-only PMAR engine (Section vii). The CCB turns those scores into **shares**: each pool’s share is its score **divided by the sum of scores of all eligible pools**. So allocation is **relative**: a pool’s emissions depend on how it compares to **everyone else** who qualifies, not on a fixed headline percentage forever.

### Incendiary first, then CCB

**Incendiary Boost** claims are paid out of the block reward **before** the remainder is split by the CCB. Incendiary is not a multiplier inside the CCB score; it is a **first claim** on the fixed per-block mint. What is left after those claims is what the CCB allocates by scores. Details are in `bootstrap.md` and `constitution.md`.

### Why this design

Capital in productive, eligible pools is the **only** input to emission weight. Rules are **deterministic and immutable**. Governance does not set weights; it remains available only for **non-emission** actions (gauges, treasury, fees, composition challenges) under the on-chain-data-only proposal rules in `constitution.md`.

### How the math works (summary)

Block reward is split after **Incendiary Boost** claims (first claim on the mint); the **remainder** is allocated by CCB shares. Each pool has its own TVL EMA series; scores combine smoothed TVL, PMAR (Miliarium only), and Incendiary multiplier; shares normalize over all eligible pools. During the transition window (Months 11–12), each immutable pool's share is a linear blend of its equal one-twenty-eighth and what the CCB would assign, ramping smoothly from pure equal to pure CCB over the two months. For full formal definitions of every formula, see `formulas.md`.

---

## vii. PMAR Role

**PMAR** (Miliarium Aureum Multiplier Adjustment Rule) is a **separate** automatic layer that applies **only** to the **28 immutable Miliarium Aureum pools**. It does not replace the CCB; it supplies a **multiplier** that sits in the CCB score **on top of** each Miliarium pool’s TVL EMA (and alongside Incendiary terms). **Other** emission-eligible pools do not run PMAR: for them, the multiplier in the score is effectively **one** — they are still ranked by smoothed TVL and the rest of the rules, but they do not get the bi-weekly PMAR nudges.

### What PMAR is trying to do

Liquidity mining often **rewards whatever grew last week**, which can overpay hot flows and starve sticky capital. PMAR pushes back **inside the Miliarium set only**: it nudges emission **away** from pools that are **running hot relative to the rest of the constellation** and **toward** pools that are **lagging the Miliarium average**, within hard floors and ceilings. So it is **anticyclical among the 28**, not a second governance vote and not an oracle.

### Two channels: protocol-wide and within the 28

**Protocol-wide channel:** the rule watches the **direction of total protocol TVL** (again using a smoothed, memory-bearing picture, not a single raw day). When **aggregate** liquidity is **rising**, multipliers across the Miliarium set face **downward** pressure; when aggregate liquidity is **falling**, they face **upward** pressure. The idea is coarse macro stabilization: don’t let the whole system behave as if every pool should be maxed out in a boom or abandoned in a bust.

**Within-the-28 channel:** each Miliarium pool is compared to the **average** of the Miliarium set. Pools whose smoothed TVL is **growing faster than that average** get **downward** nudges on the multiplier; pools that are **shrinking relative to that average** get **upward** nudges. So a pool whose TVL EMA is **dropping** still **loses ground** in the raw TVL part of the score, but PMAR can **partially offset** that **if** it is weak **relative to the other Miliarium pools**, not merely because the whole market is down together.

### Guards so the rule does not thrash

Multipliers are **clamped** to a fixed band so no pool can be rewarded or punished without limit. A **dead zone** ignores tiny wiggles in the ratios so the system does not constantly flip on noise. Steps are **small and discrete** on a fixed cadence (bi-weekly cycle), not continuous social-media sentiment. All numeric bounds and the EMA horizon are **immutable**; they are listed under Immutable Parameters in `constitution.md`.

### How PMAR lines up with Section vi

The CCB always uses **per-pool** smoothed TVL as the backbone of the score. PMAR **only** adjusts an extra factor for the **28** so that **relative** performance inside the founding constellation can be **taxed or subsidised** without human intervention. Read **Section vi** for how shares work globally; read **`PMAR.md`** for the specification labels; read **`aureum_glossary.md`** for the same mechanics in glossary form.

### How the multiplier updates

Only the 28 Miliarium pools receive PMAR updates; for any other eligible pool the multiplier is neutral (effectively one). Each bi-weekly cycle, a pool’s multiplier is adjusted by two small steps — one driven by the direction of total protocol TVL (macro pressure) and one by the pool’s TVL relative to the Miliarium average (intra-constellation pressure) — then clamped to a hard floor and ceiling so no pool can be rewarded or punished without limit. Initial multiplier is 1.00; dead zone and step size are fixed in `constitution.md`. For the formal update rule, see `formulas.md`.

### FAQ: CCB and PMAR (plain English)

**If one Miliarium pool is gaining share of TVL among the 28, what happens?** Two forces: its **TVL EMA** in the CCB score tends to rise as it takes share from siblings, which pushes its **weight up**. PMAR’s **within-the-28** channel compares each pool to the **Miliarium average** — pools **growing faster than that average** get a **downward** nudge on the multiplier (hot flows taxed), **within [0.75, 1.25]**. Net effect on that pool’s emissions depends on both; it is not “always more” or “always less.”

**If a pool shrinks relative to total protocol TVL (capital moves elsewhere), what happens?** The **CCB score** uses **per-pool** TVL EMA against **all eligible pools** in the denominator. If this pool’s smoothed TVL is lower relative to **other** eligible pools (including non-Miliarium gauges), its **share of total emissions** tends to fall. **PMAR does not** define “relative to total protocol TVL” for **delta_intra** — that is **vs the Miliarium average** only. **delta_global** keys off **aggregate protocol TVL direction** (roughly: boom vs bust pressure on multipliers), not “Miliarium vs the rest” as a separate basket.

**What is the step size on the PMAR multiplier?** Each bi-weekly cycle, each applicable step is **±0.05** before clamp, with multipliers **capped between 0.75 and 1.25**, and a **0.1% dead zone** on the ratio so noise does not flip the rule every time. See `PMAR.md` and Immutable Parameters in `constitution.md`.

**If Miliarium pools as a group lose share of protocol TVL (liquidity shifts to other eligible pools), what happens to emissions to the MA pools?** There is **no** fixed “28-pool basket” guarantee in the written rules. After the equal regime, each pool competes **individually**; **CCB_share** is **Score / sum(scores over all eligible pools)**. If the **non-Miliarium** eligible pools grow their scores faster, **MA pools as a group** can receive a **smaller** fraction of the same CCB pie. **delta_global** is **not** a dedicated “protect the constellation’s share” lever — it is **aggregate** protocol TVL **direction** for multiplier pressure across the 28.

## viii. Immutable Reference

See Immutable Parameters in `constitution.md`.
