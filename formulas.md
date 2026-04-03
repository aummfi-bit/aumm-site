# Protocol Formulas

*Every formula that governs Aureum emission allocation, multiplier adjustment, and governance power — organized by protocol phase.*

All parameters listed here are **immutable from block 0**. See Immutable Parameters (`constitution.md` §xxix).

---

## Bootstrap Phase (Months 1–10)

### F-1. Equal Emission Split

**Purpose:** Guarantee every founding pool an identical share of emissions during the cold-start period, removing any advantage from early TVL differences and giving the constellation time to build liquidity organically.

**Effect:** Each of the 28 Miliarium Aureum pools receives exactly the same fraction of the Miliarium emission tranche every block. No pool can outcompete another on emissions during this window.

```
share_i = 1 / 28
```

Where **i** ranges over the 28 Miliarium Aureum pools.

---

### F-2. Incendiary Boost Priority Claim

**Purpose:** Allow operators to commit conviction capital (escrowed and burned AuMM) in exchange for a time-limited supplementary emission stream, funded from the same fixed block emission — not from new inflation.

**Effect:** Incendiary claims are subtracted from the block emission **before** the CCB distributes the remainder. This ensures boosted pools receive their committed stream without inflating total supply. Whatever is left after Incendiary claims is what the CCB allocates.

```
Remaining(block) = block_emission(block) − Incendiary_claims(block)
```

Incendiary Boost provides a 30-day supplementary emission stream pegged to the 85th efficiency percentile. Escrowed AuMM is permanently burned.

---

## Transition Phase (Months 11–12)

### F-3. Linear Blend from Equal to CCB

**Purpose:** Gradually shift from the equal regime to fully automatic CCB allocation over a two-month window, avoiding a sudden jump that could destabilize pool economics overnight.

**Effect:** Each pool's emission share is a weighted mix of its equal share (1/28) and what the CCB formula would give it. The blend parameter **α** starts at zero (pure equal) and rises linearly to one (pure CCB) over the two-month window. At the midpoint, the mix is exactly half equal and half CCB.

```
share_i(block) = (1 − α(block)) × (1/28) + α(block) × CCB_share_i(block)
```

Where **α** runs linearly from **0** at the first block of Month 11 to **1** at the last block of Year 1. **CCB_share_i** uses the same score logic as the post–Year-1 regime (CCB multiplier and Incendiary inside the CCB leg).

---

## Continuous Operation (Post–Year 1)

### F-4. TVL Exponential Moving Average — EMA(60)

**Purpose:** Smooth each pool's raw TVL into a 60-day moving average that filters out short-term noise (hype, panic, whale movements) and preserves a memory of sustained liquidity commitment.

**Effect:** A pool that loses all its TVL today still retains roughly 50% of its signal after three weeks and 25% after six weeks. The EMA is a low-pass filter — it suppresses daily volatility and passes only the long-term capital signal. This is the foundation of the CCB's anticyclical behavior: the protocol cannot be jolted into instant reallocation by a single day's capital movement.

```
alpha = 2 / (60 + 1)                          // ≈ 0.0328

TVL_EMA_pool(today) = alpha × TVL_spot(today)
                    + (1 − alpha) × TVL_EMA_pool(yesterday)
```

The EMA runs continuously for **each pool** individually. Half-life is approximately 21 days.

---

### F-5. CCB Score

**Purpose:** Combine a pool's smoothed TVL with its CCB multiplier into a single composite score that determines how much of the remaining block emission it receives.

**Effect:** Pools with higher sustained TVL and favorable CCB multiplier positioning earn proportionally larger scores. The score is **relative** — a pool's emissions depend on how it compares to every other eligible pool, not on a fixed percentage. Incendiary Boost effects are handled separately via the priority skim (F-2), not inside the CCB score.

```
Score(pool_i) = TVL_EMA60(pool_i) × CCB_mult(pool_i)
```

**CCB_mult** applies only to the 28 Miliarium pools (all others use 1).

---

### F-6. CCB Share and Emission Distribution

**Purpose:** Normalize pool scores into fractional shares that sum to 100%, then distribute the remaining block emission (after Incendiary claims) according to those shares.

**Effect:** The entire post-Incendiary block emission is distributed across eligible pools in proportion to their scores. No emissions are left unallocated. If a pool's score rises relative to others, its share of the pie grows; if it falls, its share shrinks — automatically, every block.

```
CCB_share_i = Score(pool_i) / Σ(Score(all eligible pools))

emission_from_CCB_i = Remaining(block) × CCB_share_i
```

---

### F-7. Full Emission Sequence (Every Block, Post–Year 1)

**Purpose:** Consolidate the end-to-end emission logic into a single reference sequence showing exactly how each block's reward is computed and distributed.

**Effect:** This is the complete per-block algorithm. EMA updates run continuously; Incendiary claims are skimmed first; the remainder is split by CCB scores across all eligible pools. Oracle-free — reads only internal contract balances. The 21M hard cap is never breached because Incendiary is a reallocation from the same fixed pie, not new inflation.

```
// Step 0 — EMA update (runs continuously for each pool)
alpha = 2 / (60 + 1)                                           // ≈ 0.0328
TVL_EMA(pool, today) = alpha × TVL_spot(pool, today)
                     + (1 - alpha) × TVL_EMA(pool, yesterday)

// Step 1 — Incendiary priority skim
Incendiary_total = Σ active Incendiary Boost claims this block

// Step 2 — Remainder after Incendiary
Remaining = block_emission - Incendiary_total

// Step 3 — CCB scoring
Score(pool_i) = TVL_EMA60(pool_i) × CCB_mult(pool_i)

// Step 4 — Share and distribute
CCB_share(pool_i) = Remaining × Score(pool_i) / Σ Score(all eligible pools)

// Step 5 — Total per pool
Total_emission(pool_i) = CCB_share(pool_i) + Incendiary_claim(pool_i)
```

---

### F-8. CCB Multiplier Update

**Purpose:** Automatically adjust the emission multiplier for each of the 28 Miliarium pools every bi-weekly cycle, replacing human governance voting over emission weights with a deterministic, oracle-free rule.

**Effect:** Pools growing too fast relative to the protocol or the Miliarium average are automatically taxed (multiplier nudged down); pools shrinking relative to average are automatically subsidized (multiplier nudged up). The result is anticyclical behavior within the founding constellation — without any human intervention.

```
M_i(t) = clamp( M_i(t-1) + delta_global + delta_intra_i,  0.75,  1.25 )
```

Where:
- **M_i(t-1)** = pool i's multiplier from the prior cycle, initialized at 1.00
- **delta_global** = protocol-wide step from the direction of total protocol TVL EMA — rising TVL applies downward pressure; falling TVL applies upward pressure
- **delta_intra_i** = pool-specific step from pool i's TVL EMA relative to the Miliarium average — pools growing faster than average are nudged down; pools shrinking relative to average are nudged up
- **clamp** = hard floor and ceiling; the multiplier can never leave this band
- **dead zone** = if the TVL ratio is within the dead zone of neutral, no step is applied — prevents noise from triggering constant micro-adjustments

Step size, clamp bounds, and dead zone threshold are all immutable from block 0 — see Immutable Parameters (`constitution.md` §xxix) for exact values.

Only **i ∈ {28 Miliarium pools}** receive CCB multiplier updates; for any other eligible pool, **CCB_mult = 1**.

---

### F-9. Governance Power

**Purpose:** Convert a liquidity provider's economic stake and time commitment into governance weight, using sub-linear dampening to prevent whale capture.

**Effect:** Governance power grows with both the value of the LP position and the duration held, but the root function compresses large positions so that a whale with 100× the capital does not get 100× the voting power. Era 0 uses fourth-root dampening (maximum compression when protocol TVL is lowest and capture risk is highest); Era 1 onward relaxes to cube-root (TVL growth has naturally diluted individual power).

```
Era 0 (years 0–4):    Power = (qualified_AuMT_value × time_in_pool) ^ (1/4)
Era 1+ (years 4+):    Power = (qualified_AuMT_value × time_in_pool) ^ (1/3)
```

**qualified_AuMT_value** is the USD value of the LP position — not token count. Transition occurs at the halving block. Both exponents are immutable.

---

### F-10. Treasury Emission Decline Schedule

**Purpose:** Define the rate at which the treasury's share of per-block emissions declines from genesis to zero, ensuring the treasury accumulates enough capital to seed the AuMM pool and operate the price ceiling without retaining permanent emission access.

**Effect:** The treasury share declines linearly from 75% at block 0 to 50% at month 6, then linearly from 50% to 0% at month 10. After month 10, the treasury never receives AuMM again.

```
if block < month_6_block:
    treasury_share = 0.75 − (0.25 × block / month_6_block)

else if block < month_10_block:
    treasury_share = 0.50 − (0.50 × (block − month_6_block) / (month_10_block − month_6_block))

else:
    treasury_share = 0
```

LP share = 1 − treasury_share. The LP share increases monotonically from 25% at genesis to 100% at month 10+.

---

### F-11. Price Ceiling Stabilization (FDV/TVL)

**Purpose:** Define the price ceiling trigger, sell mechanics, and revenue routing that convert AuMM overvaluation into permanent pool depth.

**Effect:** When the smoothed FDV/TVL ratio exceeds 2, the treasury sells a fixed fraction of its AuMM pool balance daily, pushing the price down. Revenue is locked as permanent liquidity in the weakest Miliarium pools.

```
FDV = 21_000_000 × AuMM_price
TVL = total_protocol_TVL

alpha_21 = 2 / (21 + 1)                                       // ≈ 0.0909

FDV_TVL_EMA(today) = alpha_21 × (FDV / TVL)
                   + (1 − alpha_21) × FDV_TVL_EMA(yesterday)

if FDV_TVL_EMA ≥ 2 AND month ∈ [6, 12] AND treasury_inventory > 0:
    sell_amount = 0.0075 × AuMM_pool_balance                  // 0.75% per day
    sell_amount = min(sell_amount, 0.80 × treasury_assets)     // cap at 80%
    // execute once per day; revenue → permanent locked liquidity
    // in lowest-TVL Miliarium pools meeting 4626 Quality Gate
```

AuMM pool is seeded at FDV/TVL = 1. Stabilization shuts off permanently at month 12; all remaining inventory is burned.

---

### F-12. Efficiency Tournament

**Purpose:** Rank all gauged pools by capital efficiency and cap emissions for the least productive, preventing extractive pools from consuming disproportionate emission share.

**Effect:** Pools in the bottom 15% of the efficiency ranking have their emissions capped at tiered levels. Excess emissions are redistributed to uncapped pools pro-rata by CCB share. Activates at month 13.

```
efficiency_ratio(pool_i) = (swap_fee_revenue_i + yield_fee_revenue_i)
                         / emissions_received_i
// 3-epoch (6-week) moving average

rank pools by efficiency_ratio (highest = rank 1)

if rank > 85th percentile:                                     // bottom 15%
    if rank ∈ [85th, 90th):   emission_cap = 0.01 × total_emissions
    if rank ∈ [90th, 95th):   emission_cap = 0.005 × total_emissions
    if rank ≥ 95th:           emission_cap = 0.001 × total_emissions
else:
    emission_cap = none                                        // uncapped

excess = Σ (uncapped_emission − capped_emission) for all capped pools
redistribute excess to uncapped pools pro-rata by CCB_share
```

Efficiency ranking is price-agnostic — both the numerator (revenue) and the denominator (emissions) are measured in the same unit. See `bootstrap.md` §xxiii.

---

*All formulas are immutable from block 0. See Immutable Parameters (`constitution.md` §xxix) for the full list.*
