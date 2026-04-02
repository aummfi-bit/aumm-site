# Continuous Rules

*Steady-state emission mechanics: how the protocol allocates and disciplines emissions after full activation.*

---

## The Continuous Central Bank (CCB)

Emission allocation is driven by the **Continuous Central Bank (CCB)** — not by direct gauge voting. Each pool's base emission weight is its 60-day EMA of on-chain TVL as a share of total protocol TVL. Capital allocates itself.

Each pool's emission share is determined by:

```
share(pool_i) = Score(pool_i) / sum(all pool scores)

Score(pool_i) = TVL_EMA60(pool_i) × PMAR_mult(pool_i) × Bubble_mult(pool_i) × Incendiary_mult(pool_i)
```

Where:
- `TVL_EMA60` = 60-day exponential moving average of on-chain TVL (~21-day half-life)
- `PMAR_mult` = Pioneer Multiplier Adjustment Rule output [0.75–1.25] for Pioneer pools, 1.0 for non-Pioneer (see below)
- `Bubble_mult` = tessera-weighted vote result [0.90–2.00] for pools in their first 90 days, 1.0 otherwise
- `Incendiary_mult` = burn-funded boost multiplier, 1.0 for most pools, > 1.0 for pools with active Incendiary Boost

Every bi-weekly governance cycle:
1. CCB recalculates each pool's 60-day EMA TVL weight
2. PMAR recalculates Pioneer multipliers based on TVL ratio slopes
3. Active Incendiary Boosts are calculated as priority claims on block emissions
4. Per-block emission streaming adjusts at cycle boundary
5. LP bonus distributes to governance participants

### Emissions Directed to Unqualified Pools

If emissions are directed toward pools that do not meet eligibility criteria, those emissions are **not distributed to the pool**. Instead, the equivalent AuMM value is routed to the **buyback-and-burn mechanism**. This means:

- Emissions allocated to ineligible pools accelerate deflation
- There is no economic benefit to gaming toward unqualified pools
- The protocol benefits even from misallocated emissions
- All remaining holders benefit from the supply reduction

---

## Pioneer Multiplier Adjustment Rule (PMAR)

The PMAR is a deterministic, oracle-free mechanism that automatically steers emission multipliers across the 25 immutable Pioneer pools. It replaces governance-driven multiplier voting entirely.

### Inputs (All On-Chain, Oracle-Free)

Recalculated at every bi-weekly governance cycle boundary using the 60-day EMA already maintained by the CCB engine.

**Global Pioneer ratio** — Pioneer share of protocol TVL:

```
r_P(t) = TVL_Pioneer_EMA60(t) / TVL_Protocol(t)
```

**Per-pool ratio** — each Pioneer pool's share within the Pioneer constellation:

```
r_i(t) = TVL_i_EMA60(t) / TVL_Pioneer_EMA60(t)     for each Pioneer pool i = 1..25
```

### Slope Calculation

```
slope_P(t) = r_P(t) - r_P(t-1)
slope_i(t) = r_i(t) - r_i(t-1)
```

### Dead Zone

A dead zone prevents noise-driven oscillation when slopes hover near zero:

```
epsilon_P = 0.001 × r_P(t)
epsilon_i = 0.001 × r_i(t)
```

If `|slope| < epsilon`, the adjustment is 0.

### Adjustment Rules

**Global adjustment** (uniform to all 25 pools):

| Condition | Delta |
|-----------|-------|
| `slope_P < -epsilon_P` (Pioneers losing share) | +0.05 |
| `slope_P > +epsilon_P` (Pioneers gaining share) | -0.05 |
| Within dead zone | 0 |

**Per-pool adjustment**:

| Condition | Delta |
|-----------|-------|
| `slope_i < -epsilon_i` (pool losing intra-share) | +0.05 |
| `slope_i > +epsilon_i` (pool gaining intra-share) | -0.05 |
| Within dead zone | 0 |

**Multiplier update**:

```
M_i(t) = clamp( M_i(t-1) + delta_global + delta_intra_i,  0.75,  1.25 )
```

### Guarantees

- **Bounded**: All multipliers stay inside [0.75, 1.25] at every step.
- **Anticyclical**: Group-level loss of share triggers a collective boost; internal crowding triggers relative penalties.
- **Stable**: The 0.1%-of-ratio dead zone prevents flip-flopping on noise.
- **Immutable**: Step size (+/-0.05), clamp bounds, dead zone threshold, and EMA horizon are all hard-coded from block 0.

See the full [PMAR Specification](PMAR.md) for detailed scenario walkthroughs and integration notes.

---

## Anti-Gaming Criteria

Pools must meet ALL criteria to remain eligible for AuMM emissions:

| Criterion | Requirement | Rationale |
|-----------|-------------|-----------|
| Protocol version | Aequilibrium only | No legacy pool farming |
| ERC-4626 composition ("4626 Quality Gate") | **≥52%** yield-bearing tokens by weight. Each ERC-4626 token must have **≥$5M, 30 BTC, or 4,000,000 svZCHF (whichever is largest) in its underlying vault** (`totalAssets()`) to count toward the 52% threshold. | Ensures pools generate real protocol yield fees. Three independent currency-denominated floors (USD, BTC, CHF) prevent any single inflation or devaluation event from eroding the quality gate. |
| Minimum TVL | $10K **7-day SMA** (exempt during months 0–3 grace period) | Filters ghost pools. The 7-day SMA prevents flickering eligibility from intra-day price fluctuations. |
| Volume percentile floor | Graduated by pool age (see below) | Benchmarks pool activity against protocol-wide distribution |
| Efficiency-based emission caps | Bottom 15% capped (see Efficiency Tournament below). **Activates at month 13.** | Throttles inefficient pools without reflexive disqualification. Price-agnostic. |
| No self-referential tokens | AuMM cannot be a pool component | Prevents circular farming |

### Graduated Grace Period

| Pool Age | Volume Percentile Floor | Efficiency Caps | Notes |
|----------|------------------------|-----------------|-------|
| Months 0–3 | None | Exempt | Full experimentation window. Structural criteria still apply. |
| Months 3–6 | 5th percentile | Exempt | First signal required. |
| Months 6–12 | 10th percentile | Exempt | Higher bar, still in discovery phase. |
| Month 13+ | 15th percentile | **Active** | Full discipline. |

Percentile rankings are calculated against the trailing 4-week rolling window of fee + yield revenue across all emission-eligible pools.

### Hysteresis Buffer (Anti-Oscillation)

| Zone | Volume Percentile | Status | Action |
|------|------------------|--------|--------|
| **Safe** | Above 15th | Fully eligible | Normal emissions, no flags |
| **Warning** | 10th–15th | Flagged | Emissions continue. Must recover within 2 cycles (4 weeks). |
| **Cut** | Below 10th | Disqualified | Emissions cease immediately. Routed to buyback-and-burn. |

**Critical design choice:** Emissions continue during the warning period. Cutting emissions from a pool in the warning zone reduces its attractiveness exactly when it needs to attract more volume — that's a death sentence disguised as a second chance.

Re-qualification after disqualification requires sustaining activity above the 15th percentile for one full rolling window (4 weeks) with no emissions.

### Emission Efficiency Tournament

All gauged pools **above $10K TVL** are ranked by efficiency ratio — `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received` — using a **2-epoch (4-week) moving average**.

| Efficiency Rank | Emission Cap | Effect |
|----------------|-------------|--------|
| Above 15th percentile | No cap | Full emissions |
| 10th–15th percentile | 1% of total protocol emissions | Capped |
| 5th–10th percentile | 0.5% of total protocol emissions | Harder cap |
| Below 5th percentile | 0.1% of total protocol emissions | Nearly starved |

**Excess emissions are redistributed** to uncapped pools pro-rata by their existing emission weight. This rewards productive pools rather than burning the excess.

**Self-correcting.** A pool gets capped → receives fewer emissions → its efficiency ratio improves next cycle → it climbs out. No death spiral.

**Governance-capture resistant.** A group colludes to send 50% of emissions to a zero-fee pool. The protocol sees the worst efficiency ratio in the set, ranks it in the bottom 5%. Despite 50% of the votes, it receives 0.1% of emissions. The other 49.9% is redistributed to productive pools.

### Disqualification and Gauge Revocation

**Stage 1: Disqualification.** A pool below the 10th volume percentile is disqualified — emissions cease immediately. The gauge remains. Recovery above the 15th percentile for 4 weeks with no emissions re-qualifies automatically.

**Stage 2: Gauge revocation.** A pool disqualified for **4 consecutive governance cycles (8 weeks)** has its gauge permanently revoked. New gauge proposal required to restart.

### How the Criteria Interact

After month 13, a gauged pool must clear the volume floor (or be disqualified) AND survive the efficiency ranking (or be capped). Volume floor catches dead pools. Efficiency caps catch extractive pools. Neither alone is sufficient. Both are self-correcting — no governance vote required.
