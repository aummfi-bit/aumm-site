# Protocol Formulas

*Every formula governing emission allocation, multiplier adjustment, governance power, and (for non-Miliarium targets) gauge-challenge deposits — organized by protocol phase. **All governance deposits** are **one-sided into der Bodensee Pool**; only amounts differ ([Constitution §xxvii](10_constitution.md)).*

All parameters listed here are **immutable from block 0**. See [Immutable Parameters (§xxix)](10_constitution.md).

---

## Bootstrap Phase (Months 1–10)

### F-0. der Bodensee Bootstrap Emission Decay

**Purpose:** Deepen der Bodensee reserves with one-sided AuMM inflows during cold-start, so weighted-pool price discovery begins from block 0 without allocating emissions to any treasury.

**Effect:** A linearly decaying fraction of each block’s emission is minted as a **one-sided AuMM deposit** into der Bodensee Pool (no LP tokens — same mechanic as one-sided svZCHF fee inflows). The remainder is the **LP tranche** for the 28 Miliarium pools (equal split per F-1). After the final block of Month 10, **bodensee_share = 0**; 100% to LPs until Month 11.

```
month_10_end_block = last_block_of_Month_10
t = min( (block − genesis_block) / (month_10_end_block − genesis_block),  1 )

bodensee_share(block) = 0.80 × max(0, 1 − t)
lp_share(block)       = 1 − bodensee_share(block)
```

AuMM routed to der Bodensee Pool in block **b** equals **bodensee_share(b) × block_emission(b)**.

---

### F-1. Equal Emission Split

**Purpose:** Guarantee every founding pool an identical share of the **LP emission tranche** during cold-start, removing any advantage from early TVL differences.

**Effect:** Each of the 28 pools receives **one twenty-eighth** of the LP tranche every block — not of the full block emission when **bodensee_share > 0** (see F-0).

```
share_of_LP_tranche_i = 1 / 28

emission_to_pool_i(block) = lp_share(block) × block_emission(block) × (1 / 28)
```

Where **i** ranges over the 28 Miliarium Aureum pools.

---

### F-2. Incendiary Boost Priority Claim

**Purpose:** Operators commit conviction capital (escrowed svZCHF/sUSDS, one-sided into der Bodensee) in exchange for a time-limited supplementary emission stream from the same fixed block emission — not new inflation.

**Effect:** Incendiary claims are subtracted from the **LP emission tranche** (after F-0’s bootstrap skim) **before** the tranche splits across pools (equal or CCB). Whatever remains is what equal split or CCB allocates.

```
lp_tranche(block) = lp_share(block) × block_emission(block)

Remaining(block) = lp_tranche(block) − Incendiary_claims(block)
```

30-day stream pegged to the 85th efficiency percentile. Escrowed svZCHF/sUSDS deposited one-sided into der Bodensee.

---

## Transition Phase (Months 11–12)

### F-3. Linear Blend from Equal to CCB

**Purpose:** Shift from equal to full CCB over two months, avoiding overnight emission shocks.

**Effect:** Each pool's share of the **post-Incendiary LP tranche** (F-2) blends its equal share (1/28) with its CCB-derived share. **α** rises linearly from zero (pure equal) to one (pure CCB). At midpoint, half and half. During Months 11–12, **bodensee_share = 0** — LP tranche equals full block emission before Incendiary.

```
share_i(block) = (1 − α(block)) × (1/28) + α(block) × CCB_share_i(block)
```

Where **α** runs linearly from **0** at the first block of Month 11 to **1** at the last block of Year 1. **CCB_share_i** uses the same score logic as the post–Year-1 regime (CCB multiplier and Incendiary inside the CCB leg where applicable). Multiply **share_i** by **Remaining(block)** from F-2 to get AuMM to pool **i** for this leg.

---

## Continuous Operation (Post–Year 1)

### F-4. TVL Exponential Moving Average — EMA(60)

**Purpose:** Smooth each pool's raw TVL into a 60-day moving average that filters short-term noise and preserves sustained liquidity commitment.

**Effect:** A pool that loses all TVL today retains ~50% of its signal after three weeks, ~25% after six. Low-pass filter: suppresses daily volatility, passes only the long-term capital signal. The protocol cannot be jolted into instant reallocation by a single day's movement.

```
alpha = 2 / (60 + 1)                          // ≈ 0.0328

TVL_EMA_pool(today) = alpha × TVL_spot(today)
                    + (1 − alpha) × TVL_EMA_pool(yesterday)
```

The EMA runs continuously for **each pool** individually. Half-life is approximately 21 days.

---

### F-5. CCB Score

**Purpose:** Combine smoothed TVL with CCB multiplier into a single score determining each pool's share of remaining block emission.

**Effect:** Higher sustained TVL and favorable multiplier positioning → larger scores. **Relative** — emissions depend on how a pool ranks against all others, not on a fixed percentage. Incendiary effects are handled via priority skim (F-2), not inside the CCB score.

```
Score(pool_i) = TVL_EMA60(pool_i) × CCB_mult(pool_i)
```

**CCB_mult** applies only to the 28 Miliarium pools (all others use 1).

---

### F-6. CCB Share and Emission Distribution

**Purpose:** Normalize scores into fractional shares summing to 100%, then distribute remaining emission accordingly.

**Effect:** The entire post-Incendiary emission is distributed in proportion to scores. No emissions left unallocated. Score rises → share grows; score falls → share shrinks. Automatic, every block.

```
CCB_share_i = Score(pool_i) / Σ(Score(all eligible pools))

emission_from_CCB_i = Remaining(block) × CCB_share_i
```

---

### F-7. Full Emission Sequence (Every Block, Post–Year 1)

**Purpose:** Complete per-block algorithm in one reference sequence.

**Effect:** EMA updates run continuously; Incendiary claims skimmed first; remainder split by CCB scores. Oracle-free — reads only internal contract balances. 21M cap never breached: Incendiary is reallocation, not new inflation.

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

**Purpose:** Adjust each Miliarium pool's emission multiplier every bi-weekly cycle — deterministic, oracle-free, replacing human governance over emission weights.

**Effect:** Pools growing too fast relative to the protocol or constellation average are taxed (multiplier nudged down); pools shrinking are subsidized (nudged up). Anticyclical behavior within the 28, no human intervention.

```
M_i(t) = clamp( M_i(t-1) + delta_global + delta_intra_i,  0.75,  1.25 )
```

Where:
- **M_i(t-1)** = pool i's multiplier from the prior cycle, initialized at 1.00
- **delta_global** = protocol-wide step from the direction of total protocol TVL EMA — rising TVL applies downward pressure; falling TVL applies upward pressure
- **delta_intra_i** = pool-specific step from pool i's TVL EMA relative to the Miliarium average — pools growing faster than average are nudged down; pools shrinking relative to average are nudged up
- **clamp** = hard floor and ceiling; the multiplier can never leave this band
- **dead zone** = if the TVL ratio is within the dead zone of neutral, no step is applied — prevents noise from triggering constant micro-adjustments

Step size, clamp bounds, and dead zone threshold are all immutable from block 0 — see [Immutable Parameters (§xxix)](10_constitution.md) for exact values.

Only **i ∈ {28 Miliarium pools}** receive CCB multiplier updates; for any other eligible pool, **CCB_mult = 1**.

---

### F-9. Governance Power

**Purpose:** Convert LP stake and time commitment into governance weight with sub-linear dampening to prevent whale capture.

**Effect:** Root function compresses large positions — 100× capital ≠ 100× voting power. Era 0: fourth root (maximum compression when TVL is lowest). Era 1+: cube root (TVL growth has diluted individual power).

```
Era 0 (years 0–4):    Power = (qualified_AuMT_value × time_in_pool) ^ (1/4)
Era 1+ (years 4+):    Power = (qualified_AuMT_value × time_in_pool) ^ (1/3)
```

**qualified_AuMT_value** is the USD value of the LP position — not token count. Transition occurs at the halving block. Both exponents are immutable.

---

### F-10. Efficiency Tournament

**Purpose:** Rank gauged pools by capital efficiency and cap emissions for the least productive.

**Effect:** Bottom 15% capped at tiered levels. Excess redistributed to uncapped pools pro-rata by CCB share. Activates at month 13.

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

Price-agnostic — numerator (revenue) and denominator (emissions) measured in the same unit. See [Bootstrap (§xxiii)](08_bootstrap.md).

---

### F-11. der Bodensee Pool Weight Decay

**Purpose:** Define linear time-decay of token weights in der Bodensee Pool, replacing discretionary price discovery.

**Effect:** Two-token LBP (AuMM + svZCHF), weights shifting linearly from genesis to 18-month endpoint. **Seed:** **1 AuMM** and **1 svZCHF**. **Swap fee:** **0.75%**, fully retained **in pool** (not routed through the protocol fee pipeline). **Protocol-captured** revenue from **other** pools flows one-sided into the svZCHF side. Price discovery forced by time-decay + real revenue — no oracle, no manual trigger.

```
genesis_block = block_0
end_block     = genesis_block + 18_months_in_blocks          // ~3,942,000 blocks at 12 s/block

t = min( (current_block − genesis_block) / (end_block − genesis_block),  1 )

weight_AuMM(t)  = 0.90 − (0.42 × t)                         // 90% → 48%
weight_svZCHF(t) = 0.10 + (0.42 × t)                        // 10% → 52%
```

Genesis: **90/10** weights, seed **1 AuMM + 1 svZCHF**. By 18 months: **48/52**, fixed permanently. **Protocol-captured** revenue (swap fees on other pools + ERC-4626 yield fees) enters as one-sided svZCHF. **Swaps inside der Bodensee:** 0.75%, fully to der Bodensee LPs. **Months 1–10:** also receives decaying one-sided AuMM bootstrap (80% at genesis → 0% at end of Month 10; see F-0). **After Month 10:** no further AuMM via emission — only fee inflows, in-pool swap fees, and governance/Incendiary deposits. All weight decay parameters immutable from block 0.

---

### F-12. Gauge Challenge Deposit (Non-Miliarium Gauged Pools Only)

**Purpose:** Scale the gauge-challenge deposit so nuisance challenges against **large, efficient** non-Miliarium gauges cost real money, while keeping a lower bar for tail or weak pools. **Does not apply to the 28 Miliarium Aureum pools** — those use the **flat** deposit in [Constitution (§xxvii)](10_constitution.md).

**Effect:** The full deposit (after the `max` below) is paid **one-sided into der Bodensee Pool** — same mechanic as other governance deposits: **svZCHF or sUSDS equivalent (whichever is higher)**, non-refundable, **no LP tokens** minted to the challenger.

For a challenge targeting a **non-Miliarium** pool, the deposit equals the **greater** of:

1. **10 BTC** expressed in **CHF**, then converted to **svZCHF or sUSDS equivalent (whichever is higher)** at submission time — then deposited **one-sided into der Bodensee Pool**; and  
2. **1,000,000 CHF** × **sqrt((1 − p_tvl) × (1 − p_eff))**, likewise converted to svZCHF/sUSDS equivalent and deposited **one-sided into der Bodensee Pool**.

**Elite tail convention:** **p_tvl** and **p_eff** use **rank / N** (not CDF-from-bottom). Among **all gauged pools** (including Miliarium), **N** = count of gauged pools. Sort by **spot TVL**; **rank 1** = highest TVL → **p_tvl = rank / N**. Independently sort by **efficiency ratio** as in F-10 (3-epoch moving average); **rank 1** = highest efficiency → **p_eff = rank / N**. **Ties** break deterministically (e.g. lower pool contract address hex first).

**(1 − p_tvl)** and **(1 − p_eff)** are large when the target is elite on both axes (rank 1 ⇒ **p ≈ 1/N** ⇒ factors near **1 − 1/N**). The weakest pool on either axis has **p ≈ 1** → that factor → **0**, so the **10 BTC** floor typically binds.

```
deposit_CHF_component = 1_000_000 × sqrt((1 − p_tvl) × (1 − p_eff))

gauge_challenge_deposit = max( 10_BTC_in_CHF ,  deposit_CHF_component )
// convert to svZCHF/sUSDS equivalent; one-sided deposit into der Bodensee Pool; non-refundable
```

**Miliarium Aureum exclusion:** If the target **is** one of the **28 Miliarium Aureum** pools, F-12 does not apply — use the **fixed** 1,000 svZCHF/sUSDS equivalent deposit, **one-sided into der Bodensee Pool**. Structural changes to those slots follow **composition challenge**, not this scaling rule.

---

*All formulas are immutable from block 0. See [Immutable Parameters (§xxix)](10_constitution.md) for the full list.*
