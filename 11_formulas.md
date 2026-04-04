# Protocol Formulas

*Every formula that governs Aureum emission allocation, multiplier adjustment, and governance power — organized by protocol phase.*

All parameters listed here are **immutable from block 0**. See [Immutable Parameters (§xxix)](10_constitution.md).

---

## Bootstrap Phase (Months 1–10)

### F-0. der Bodensee Bootstrap Emission Decay

**Purpose:** Deepen der Bodensee Pool reserves with one-sided AuMM inflows during the cold-start period, aligned with svZCHF fee inflows, so weighted-pool price discovery begins from block 0 without allocating emissions to any treasury or wallet.

**Effect:** A linearly decaying fraction of each block’s emission is minted as a **one-sided AuMM deposit** into der Bodensee Pool (no LP tokens minted — same mechanic as one-sided svZCHF fee inflows). The remainder of the block emission is the **LP tranche** for the 28 Miliarium pools (equal split per F-1). After the final block of Month 10, **bodensee_share = 0**; 100% of emissions go to LPs under the equal regime until Month 11.

```
month_10_end_block = last_block_of_Month_10
t = min( (block − genesis_block) / (month_10_end_block − genesis_block),  1 )

bodensee_share(block) = 0.80 × max(0, 1 − t)
lp_share(block)       = 1 − bodensee_share(block)
```

AuMM routed to der Bodensee Pool in block **b** equals **bodensee_share(b) × block_emission(b)**.

---

### F-1. Equal Emission Split

**Purpose:** Guarantee every founding pool an identical share of the **LP emission tranche** during the cold-start period, removing any advantage from early TVL differences and giving the constellation time to build liquidity organically.

**Effect:** Each of the 28 Miliarium Aureum pools receives exactly **one twenty-eighth** of the LP tranche every block — not one twenty-eighth of the full block emission when **bodensee_share > 0** (see F-0). No pool can outcompete another on emissions during this window.

```
share_of_LP_tranche_i = 1 / 28

emission_to_pool_i(block) = lp_share(block) × block_emission(block) × (1 / 28)
```

Where **i** ranges over the 28 Miliarium Aureum pools.

---

### F-2. Incendiary Boost Priority Claim

**Purpose:** Allow operators to commit conviction capital (escrowed svZCHF/sUSDS deposited one-sided into der Bodensee Pool) in exchange for a time-limited supplementary emission stream, funded from the same fixed block emission — not from new inflation.

**Effect:** Incendiary claims are subtracted from the **LP emission tranche** (after F-0’s der Bodensee bootstrap skim) **before** that tranche is split across pools (equal or CCB). This ensures boosted pools receive their committed stream without inflating total supply. Whatever is left after Incendiary claims is what the equal split (Months 1–10) or CCB (later) allocates.

```
lp_tranche(block) = lp_share(block) × block_emission(block)

Remaining(block) = lp_tranche(block) − Incendiary_claims(block)
```

Incendiary Boost provides a 30-day supplementary emission stream pegged to the 85th efficiency percentile. Escrowed svZCHF/sUSDS is deposited one-sided into der Bodensee Pool.

---

## Transition Phase (Months 11–12)

### F-3. Linear Blend from Equal to CCB

**Purpose:** Gradually shift from the equal regime to fully automatic CCB allocation over a two-month window, avoiding a sudden jump that could destabilize pool economics overnight.

**Effect:** Each pool's fractional share of the **post-Incendiary LP emission tranche** (F-2) is a weighted mix of its equal share (1/28) and what the CCB formula would give it. The blend parameter **α** starts at zero (pure equal) and rises linearly to one (pure CCB) over the two-month window. At the midpoint, the mix is exactly half equal and half CCB. During Months 11–12, **bodensee_share = 0**, so the LP tranche equals the full block emission before Incendiary.

```
share_i(block) = (1 − α(block)) × (1/28) + α(block) × CCB_share_i(block)
```

Where **α** runs linearly from **0** at the first block of Month 11 to **1** at the last block of Year 1. **CCB_share_i** uses the same score logic as the post–Year-1 regime (CCB multiplier and Incendiary inside the CCB leg where applicable). Multiply **share_i** by **Remaining(block)** from F-2 to get AuMM to pool **i** for this leg.

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

**Effect:** Pools with higher sustained TVL and favorable CCB multiplier positioning earn proportionally larger scores. The score is **relative** — a pool's emissions depend on how it compares to every other eligible pool, not on a fixed percentage. Incendiary Boost effects are handled separately via the priority skim (F-2) on the LP tranche, not inside the CCB score.

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

Step size, clamp bounds, and dead zone threshold are all immutable from block 0 — see [Immutable Parameters (§xxix)](10_constitution.md) for exact values.

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

### F-10. Efficiency Tournament

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

Efficiency ranking is price-agnostic — both the numerator (revenue) and the denominator (emissions) are measured in the same unit. See [Bootstrap (§xxiii)](08_bootstrap.md).

---

### F-11. der Bodensee Pool Weight Decay

**Purpose:** Define the linear time-decay of token weights in der Bodensee Pool (the protocol's autonomous reserve), replacing any discretionary price discovery or stabilization mechanism.

**Effect:** der Bodensee Pool is a two-token Liquidity Bootstrapping Pool (AuMM + svZCHF) whose weights shift linearly from genesis to the 18-month endpoint. **Genesis seed:** **1 AuMM** and **1 svZCHF** at pool creation. **Swap fee on trades in this pool:** **0.75%**, fully retained **in pool** for der Bodensee LPs (not routed through the protocol-wide 50/50 swap-fee split). **Protocol-captured** fee revenue from **other** pools flows one-sided into the svZCHF side. Price discovery is forced by the combination of time-decay and real revenue inflows — no oracle, no manual trigger.

```
genesis_block = block_0
end_block     = genesis_block + 18_months_in_blocks          // ~3,942,000 blocks at 12 s/block

t = min( (current_block − genesis_block) / (end_block − genesis_block),  1 )

weight_AuMM(t)  = 0.90 − (0.42 × t)                         // 90% → 48%
weight_svZCHF(t) = 0.10 + (0.42 × t)                        // 10% → 52%
```

At genesis, der Bodensee Pool holds **90% AuMM / 10% svZCHF** **weights** with **minimal seed balances: 1 AuMM and 1 svZCHF** at deployment. By the 18-month endpoint, weights stabilize at **48% AuMM / 52% svZCHF** and remain fixed permanently. **Protocol-captured** fee revenue — **50% of swap fees on non–der Bodensee pools** plus **100% of ERC-4626 yield fees** — enters as one-sided svZCHF inflows. **Swaps inside der Bodensee** pay **0.75%**, fully to der Bodensee LPs in-pool. During **Months 1–10**, der Bodensee Pool also receives a **linearly decaying one-sided AuMM bootstrap** (80% of block emission at genesis → 0% at end of Month 10; see F-0). **After Month 10**, no further AuMM is routed to der Bodensee via emission — only protocol-captured fee inflows, **in-pool** swap fees, and governance/Incendiary svZCHF/sUSDS deposits. Weight decay parameters are immutable from block 0.

---

*All formulas are immutable from block 0. See [Immutable Parameters (§xxix)](10_constitution.md) for the full list.*
