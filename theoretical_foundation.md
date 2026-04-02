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

The Continuous Central Bank allocates emissions with no voting input.

### Activation Sequence

- **Through end of Month 10:** equal **1/28** emissions to each of the 28 immutable Miliarium Aureum pools.
- **Months 11–12:** linear blend: **(1 − α) × (1/28) + α × CCB_share**, **α** from 0 to 1 over the two months; midpoint **α = 0.5**.
- **After Year 1:** full CCB allocation using **TVL EMA(60) × PMAR_mult × Incendiary_mult** (see formula below and `constitution.md`).

### Core Formula

```
TVL_EMA_pool(today) = alpha * TVL_spot(today) + (1 - alpha) * TVL_EMA_pool(yesterday)
alpha = 2 / (60 + 1)

Score(pool_i) = TVL_EMA60(pool_i) * PMAR_mult(pool_i) * Incendiary_mult(pool_i)
share(pool_i) = Score(pool_i) / sum(all pool scores)
```

### Design Consequence

- Capital is the only allocation signal.
- Emission rules are deterministic and immutable.
- Human governance is removed from allocation logic.
- Governance remains available for non-emission actions under on-chain-data-only proposal constraints.

## vii. PMAR Role

PMAR is deterministic and oracle-free, with fixed immutable parameters in `constitution.md`.

## viii. Immutable Reference

See Immutable Parameters in `constitution.md`.
