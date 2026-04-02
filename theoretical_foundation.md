## I — Theoretical Foundations

The CCB draws from established research across multiple disciplines:

**Autonomous Corporate Logic:** Meisser's "Continuous Capital Corporation" (2022) argues that a corporation can operate via continuous algorithms rather than board meetings — the foundational logic for the CCB as an autonomous institution.

**Pro-Cyclicality:** BIS research (Aramonte et al., 2022) identifies that most DeFi protocols amplify market moves, creating systemic fragility. The EMA is the direct antidote — algorithmic inertia forces anticyclical behaviour.

**Monetary Rules:** Friedman's k-percent rule (fixed money supply growth) is the intellectual ancestor of the fixed-emission, halving-based schedule.

**Governance Minimization:** Buterin and Meisser argue governance is a security surface. The ±10% Pioneer multiplier collapses the governance attack surface to near-zero.

**Signal Processing:** The EMA is a low-pass filter — "market hype" is noise, "sustained liquidity commitment" is the signal.

**Automatic Stabilizers:** The EMA acts like fiscal automatic stabilizers (unemployment insurance) — elevating yield during crashes without requiring a governance vote.

**Mechanism Design (Roth/Maskin):** Routing unqualified votes to buyback-and-burn makes every outcome — productive allocation or misdirected votes — beneficial to protocol health.

**Hysteresis:** The EMA gives Aureum institutional memory. Most DeFi is memoryless and reflexive.

### Prior Work by the Founding Team

- **The DRUID Deep Dive** — Routing architecture and aggregator thesis. [www.sagix.io/the-druid-deep-dive/](https://www.sagix.io/the-druid-deep-dive/)
- **The Layer Framework** — Layered DeFi infrastructure model. [www.sagix.io/our-layer-framework/](https://www.sagix.io/our-layer-framework/)
- **Sagix Miliarium Aureum** — Original constellation design, live on Balancer V3 Ethereum mainnet. [www.sagix.io/sagix-miliarium-aureum/](https://www.sagix.io/sagix-miliarium-aureum/)
- **The Risk Premium Problem** — Governance centralisation analysis, published on Leviathan News. Direct catalyst for the fork. [www.sagix.io/the-risk-premium-problem/](https://www.sagix.io/the-risk-premium-problem/)

---

## II — The Continuous Central Bank (CCB)

> **Activation:** The CCB engine activates during the month 11–12 transition. During months 0–10, emissions are distributed equally across the 25 Mercatūs Praecursorii (1/25th each). See **Launch Procedures** for the full timeline.

### The Problem: Pro-Cyclicality

Most DeFi protocols amplify market moves — pouring incentives into pumps and withdrawing them during crashes. Research from the Bank for International Settlements (Aramonte et al., 2022) identifies this as systemic pro-cyclicality: the protocol accelerates the very volatility it should be dampening. Governance-driven emission allocation compounds the problem: in bull markets, voters chase hot pools; in bear markets, they flee to safety. The protocol's own incentive layer becomes a reflexive amplifier.

### The Solution: Algorithmic Inertia

The Continuous Central Bank (CCB) replaces human-driven emission allocation with an algorithmic engine that uses each pool's **60-day Exponential Moving Average (EMA) of on-chain TVL** as the base emission weight. Governance does not set pool weights. Capital sets pool weights. Governance only nudges Mercatūs Praecursorii multipliers within a constrained band.

```
TVL_EMA_pool(today) = α × TVL_spot(today) + (1 - α) × TVL_EMA_pool(yesterday)
α = 2 / (N + 1)    where N = 60 days
```

The 60-day EMA has a **half-life of approximately 21 days** — closely aligned with the bi-weekly governance cycle. After a capital withdrawal, the ghost signal halves every three weeks, eliminating the flat-persistence problem of a simple moving average while preserving meaningful anticyclical smoothing.

### Anticyclical Dynamics

**The bull market brake.** During rapid price appreciation, TVL spikes. The EMA lags behind the spot growth, so relative yield (%) drops. The protocol does not overpay for capital during periods of greed, reducing the risk of speculative bubbles.

**The bear market floor.** During market crashes, liquidity exits rapidly. But the EMA preserves the "memory" of higher TVL, keeping absolute emission levels elevated. Yield (%) spikes for remaining LPs, creating a programmatic lender of last resort that attracts capital when the market is most illiquid.

This is the protocol behaving as an anticyclical central bank — tightening during booms, loosening during busts — without human discretion.

### The Emission Formula

Every pool's base emission weight is its EMA-smoothed TVL share of total protocol TVL. Multiple multipliers layer on top for qualifying pools:

```
Score(pool) = TVL_EMA60(pool) × Pioneer_mult(pool) × Bubble_mult(pool) × Incendiary_mult(pool)
```

Where:
- `Pioneer_mult` = PMAR-computed multiplier [0.75–1.25] for Mercatūs Praecursorii, 1.00 for non-Pioneer (see PMAR Specification)
- `Bubble_mult` = tessera-weighted vote result [0.90–2.00] for pools in their first 90 days post-gauge-approval, 1.00 otherwise
- `Incendiary_mult` = burn-funded boost multiplier, 1.00 for most pools, > 1.00 for pools with active Incendiary Boost

**Two-step emission distribution:**

```
Step 1:  Incendiary_total = Σ (all active Incendiary Boost claims this block)
Step 2:  Remaining_emission = block_emission - Incendiary_total
Step 3:  CCB_share(pool_i) = Remaining_emission × Score(pool_i) / Σ Score(all_pools)
Step 4:  Total_emission(pool_i) = CCB_share(pool_i) + Incendiary_claim(pool_i)
```

The 21M hard cap is never breached. Incendiary Boosts eat from the same fixed pie — they are subtracted before CCB distribution, not added on top. Every AuMM emitted via Incendiary Boost is one less AuMM distributed via the CCB to all other pools.

**Zero-sum normalization.** The total emission rate is fixed. Any boost — Pioneer, Bubble, or Incendiary — is a reallocation of existing emissions, not new inflation.

### The Steering Mechanism: Pioneer Multiplier Voting

Tessera-weighted governance votes set the multiplier for each Mercatūs Praecursorii within a constrained range:

| Discrete Steps | 0.90 | 0.95 | 1.00 | 1.05 | 1.10 |
|---------------|------|------|------|------|------|

**The final multiplier for each Mercatūs Praecursorii is the tessera-weighted average of all votes cast for that pool.** Individual voters choose from discrete steps (0.90, 0.95, 1.00, 1.05, 1.10), but the weighted average produces a continuous result (e.g., 1.034). This forces consensus — no single voter or coalition can slam a multiplier to the extreme. The system gravitates toward the middle ground.

**Voting mechanics:**
- Multiplier votes are cast per Mercatūs Praecursorii every **6 weeks** (three governance cycles)
- Only qualified AuMT holders can vote (same qualification as all governance)
- Withdrawal from any pool resets voting power to zero (see Governance section)
- If no votes are cast in a cycle, the multiplier persists from the prior cycle

**Non-Mercatūs Praecursorii have no multiplier.** Their emission share is pure TVL-EMA weight. No governance input. Capital is the only signal.

### Strategic Examples

The multiplier applies only to Mercatūs Praecursorii that currently hold a valid tag. If tags are revoked (gauge loss, disqualification), the multiplier pool shrinks — 15 active Pioneers means governance steers 15 pools, not 20. The math adjusts automatically.

| Strategy | Pioneer Votes | Effect |
|----------|--------------|--------|
| Boost all Pioneers | 1.10 on all active Pioneers | Mercatūs Praecursorii collectively get ~10% more than TVL-weighted share |
| Boost ecosystem pools | 0.90 on all active Pioneers | Non-Mercatūs Praecursorii collectively get more emissions |
| Concentrate on ixAppia | 1.10 on ixAppia, 0.90 on others | Gold pool favored within Pioneer set |
| Neutral | 1.00 on all | Pure TVL-weighted allocation everywhere |

### Self-Referential Integrity

The CCB is **oracle-free**. It relies entirely on internal contract balances and time-weighted EMA data. No external price feeds, no Chainlink dependency, no oracle manipulation surface. The protocol prices its own liquidity commitments using its own on-chain state.

**Note on the Treasury Stabilization module.** The Price Ceiling mechanism (months 6–10) requires a price reference — the 7-day SMA of AuMM's price derived from the internal AuMM/stablecoin trading pool. This is not an external oracle: it reads the protocol's own on-chain pool price, which is manipulation-resistant due to the pool's 0.75% swap fee and the 7-day averaging window. The emission allocation engine (CCB) and the treasury stabilization module are both oracle-free in the sense that neither depends on external price feeds.

### Interaction with Existing Mechanisms

The CCB replaces how the emission pie is sliced. It does not replace any existing discipline mechanism:

- **Efficiency tournament** still caps the bottom 15% of pools by efficiency ratio. A pool with high EMA-TVL but terrible efficiency still gets capped.
- **Volume percentile floor** still disqualifies dead pools. The EMA gives them a decaying weight, but the percentile floor kills them outright.
- **Gauge revocation** still removes dead gauges after 4 cycles. The CCB doesn't protect non-performing pools.
- **Buyback-and-burn on unqualified votes** still applies. If the EMA directs weight to a pool that fails eligibility, those emissions are burned.

The CCB handles allocation. The anti-gaming stack handles discipline. Orthogonal systems, complementary effects.
