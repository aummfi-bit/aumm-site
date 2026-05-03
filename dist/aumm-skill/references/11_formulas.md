<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a 11_formulas.md — DO NOT EDIT -->
# Protocol Formulas

*Every formula governing emission allocation, multiplier adjustment, governance power, and (for non-Miliarium targets) gauge-challenge deposits — organized by protocol phase. **All governance deposits** are **one-sided into der Bodensee Pool**; only amounts differ ([Constitution §xxvii](10_constitution.md)).*

All parameters listed here are **immutable from block 0**. See [Immutable Parameters (§xxix)](10_constitution.md).

---

## xlii. Bootstrap Phase (Months 1–10)

### F-0. der Bodensee Bootstrap Emission Decay

**Purpose:** Deepen der Bodensee reserves with one-sided AuMM inflows during cold-start, so weighted-pool price discovery begins from block 0 without allocating emissions to any treasury.

**Effect:** A **piecewise-linear, per-block decaying** fraction of each block's emission is minted as a **one-sided AuMM deposit** into der Bodensee Pool (no LP tokens — same mechanic as one-sided stablecoin fee inflows). The remainder is the **LP tranche** for the 28 Miliarium pools (equal split per F-1). Two segments: genesis → end of Month 6 decays **linearly from 80% to 50%**; end of Month 6 → end of Month 10 decays **linearly from 50% to 0%**. After the final block of Month 10, **bodensee_share = 0 permanently**; 100% to LPs until Month 11.

```
// Using canonical block constants from Constitution §xxix:
//   MONTH_6_END_BLOCK  = genesis_block + 6  × BLOCKS_PER_MONTH
//   MONTH_10_END_BLOCK = genesis_block + 10 × BLOCKS_PER_MONTH
//   BLOCKS_PER_MONTH   = 219,000

if block ≤ MONTH_6_END_BLOCK:
    t1 = (block − genesis_block) / (MONTH_6_END_BLOCK − genesis_block)
    bodensee_share(block) = 0.80 − 0.30 × t1          // 80% → 50%
elif block ≤ MONTH_10_END_BLOCK:
    t2 = (block − MONTH_6_END_BLOCK) / (MONTH_10_END_BLOCK − MONTH_6_END_BLOCK)
    bodensee_share(block) = 0.50 − 0.50 × t2          // 50% → 0%
else:
    bodensee_share(block) = 0                          // permanent cutoff

lp_share(block) = 1 − bodensee_share(block)
```

AuMM routed to der Bodensee Pool in block **b** equals **bodensee_share(b) × block_emission(b)**. After the final block of Month 10 the treasury/bootstrap channel is **immutable at zero** — der Bodensee never again receives AuMM via emission.

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

**Purpose:** Anyone deposits any amount of svZCHF/sUSDS one-sided into der Bodensee Pool in exchange for a **1-epoch (14-day)** supplementary emission stream for a gauged pool, starting at the next epoch boundary — from the same fixed block emission, not new inflation.

**Effect:** Incendiary claims are subtracted from the **LP emission tranche** (after F-0’s bootstrap skim) **before** the tranche splits across pools (equal or CCB). Whatever remains is what equal split or CCB allocates. One boost per pool per epoch.

```
lp_tranche(block) = lp_share(block) × block_emission(block)

Remaining(block) = lp_tranche(block) − Incendiary_claims(block)
```

Deposit amount at user discretion; full amount one-sided into der Bodensee Pool, non-refundable.

---

## xliii. Transition Phase (Months 11–12)

### F-3. Linear Blend from Equal to CCB

**Purpose:** Shift from equal to full CCB over two months, avoiding overnight emission shocks.

**Effect:** Each pool's share of the **post-Incendiary LP tranche** (F-2) blends its equal share (1/28) with its CCB-derived share. **α** rises linearly from zero (pure equal) to one (pure CCB). At midpoint, half and half. During Months 11–12, **bodensee_share = 0** — LP tranche equals full block emission before Incendiary.

```
share_i(block) = (1 − α(block)) × (1/28) + α(block) × CCB_share_i(block)
```

Where **α** runs linearly from **0** at the first block of Month 11 to **1** at the last block of Year 1. **CCB_share_i** uses the same score logic as the post–Year-1 regime (CCB multiplier and Incendiary inside the CCB leg where applicable). Multiply **share_i** by **Remaining(block)** from F-2 to get AuMM to pool **i** for this leg.

---

## xliv. Continuous Operation (Post–Year 1)

### F-4. TVL Exponential Moving Average — EMA(60)

**Purpose:** Smooth each pool's raw TVL into a 60-day moving average that filters short-term noise and preserves sustained liquidity commitment.

**Effect:** A pool that loses all TVL today retains ~50% of its signal after three weeks, ~25% after six. Low-pass filter: suppresses daily volatility, passes only the long-term capital signal. The protocol cannot be jolted into instant reallocation by a single day's movement.

**Sampling cadence.** The EMA updates **once per `BLOCKS_PER_DAY` (7,200 blocks)**, not every block. Each sample is an **intra-day TWAP over the last `TWAP_WINDOW_BLOCKS` (720 blocks, ~1 hour) before the sample boundary**, not a single-block spot read. The TWAP eliminates block-timing manipulation at trivial gas cost; the accumulator pattern (running `cumulativeTVL` and `cumulativeBlock` updated on each swap/liquidity event) lets the sample be read as `(cumulativeTVL_now − cumulativeTVL_dayAgo) / (cumulativeBlock_now − cumulativeBlock_dayAgo)`.

**Update rule.** Using canonical constants from Constitution §xxix (`EMA_ALPHA_NUMERATOR = 2`, `EMA_ALPHA_DENOMINATOR = 61`):

```
alpha = 2 / 61                                            // ≈ 0.0328

// Triggered once per BLOCKS_PER_DAY (permissionless call; deterministic math):
if block.number ≥ lastEMAUpdateBlock[pool] + BLOCKS_PER_DAY:
    twapTVL = (cumulativeTVL[pool].atBlock(block.number) − cumulativeTVL[pool].atBlock(block.number − TWAP_WINDOW_BLOCKS))
              / TWAP_WINDOW_BLOCKS

    tvlEMA[pool] = (EMA_ALPHA_NUMERATOR × twapTVL
                 + (EMA_ALPHA_DENOMINATOR − EMA_ALPHA_NUMERATOR) × tvlEMA[pool])
                 / EMA_ALPHA_DENOMINATOR
                 // = (2 × twapTVL + 59 × tvlEMA[pool]) / 61

    lastEMAUpdateBlock[pool] = block.number
```

The EMA runs **per pool** independently. Half-life is approximately 21 days. Gas cost: ~50k per pool per day for the EMA update, plus negligible accumulator updates on each swap/liquidity event.

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

### F-11. der Bodensee Pool Composition (Fixed Weights)

**Purpose:** Define the immutable composition of der Bodensee Pool — the protocol's autonomous reserve and AuMM price-discovery venue.

**Effect:** Three-token weighted pool with **fixed** weights from block 0. No time-decay curve. No discretionary reweighting. Weighted-pool math is the only pricing mechanism — as the stablecoin side deepens via continuous one-sided fee inflows while the AuMM side is capped by the decaying F-0 bootstrap (zero after Month 10), the ratio re-prices AuMM mechanically.

```
weight_AuMM   = 0.40        // 40%
weight_sUSDS  = 0.30        // 30%
weight_svZCHF = 0.30        // 30%
// sum = 1.00, immutable from block 0
```

| Parameter | Value |
|:----------|:------|
| Tokens | AuMM, sUSDS, svZCHF |
| Weights | **40% / 30% / 30%** (fixed, immutable) |
| Swap fee | **0.75%**, fully retained **in pool** (not routed through the protocol fee pipeline) |
| ERC-4626 yield-bearing share | **60%** of pool TVL (sUSDS + svZCHF) earns native vault yield |
| Emission eligibility | **None** — der Bodensee cannot receive CCB emissions (no self-referential tokens) |

**AuMM inflows.** Only the F-0 bootstrap deposits AuMM into der Bodensee — decaying per block through Month 10, then **permanently zero**. No other mechanism mints AuMM into this pool.

**Stablecoin inflows.** **100%** of the **protocol share** of swap fees on all non–der Bodensee gauged pools (**100%** of the Vault-assigned protocol fee — **`protocolSwapFeePercentage = 50e16`**, i.e. **~50%** of charged swap fee volume; see [Constitution §xxix — Fee routing](10_constitution.md)) plus **100%** of the ERC-4626 yield fee (10% skim on all yield-bearing tokens held in **non–der Bodensee gauged pools**) enter as **one-sided stablecoin deposits** (always routed as svZCHF per Constitution §xxix), continuously deepening the reserve side. **LP residuals** on swap fees stay with originating-pool LPs. Governance deposits and Incendiary Boost deposits use the same one-sided path.

**Der Bodensee is excluded from the yield skim.** Its own ERC-4626 holdings (svZCHF + sUSDS, 60% of pool TVL) accrue yield continuously via the Rate Provider mechanism, and that yield stays inside the pool — it accrues to Bodensee LPs via their BPT share and reprices AuMM upward via weighted-pool math. Skimming Bodensee's yield and depositing it back into Bodensee would be a circular no-op. The skim mechanism extracts yield from *other* pools only; Bodensee is the **destination** of the skim, not a source. See [Tokenomics §x-a](04_tokenomics.md) for the full self-yield mechanism.

**Price discovery.** No founder-set price, no governance-voted multiple, no TVL measurement window. The ratio of AuMM to stablecoins in the pool **is** the price; weighted-pool math handles it organically from genesis.

All composition parameters immutable from block 0.

---

### F-12. Gauge Challenge Deposit (Non-Miliarium Gauged Pools Only)

**Purpose:** Scale the gauge-challenge deposit so nuisance challenges against **large, efficient** gauges cost real money, while keeping a lower bar for tail or weak pools. **The 28 Miliarium Aureum pools cannot be gauge-challenged** — structural changes to those slots go exclusively through the **Composition Challenge** path ([Constitution §xxvii](10_constitution.md)).

**Effect:** The full deposit (after the `max` below) is paid **one-sided into der Bodensee Pool** — same mechanic as other governance deposits: **svZCHF or sUSDS equivalent (whichever is higher)**, non-refundable, **no LP tokens** minted to the challenger.

For a challenge targeting a **non-Miliarium** pool, the deposit equals the **greater** of:

1. **10 BTC** expressed in **CHF**, then converted to **svZCHF or sUSDS equivalent (whichever is higher)** at submission time — then deposited **one-sided into der Bodensee Pool**; and  
2. **1,000,000 CHF** × **sqrt((1 − p_tvl) × (1 − p_eff))**, likewise converted to svZCHF/sUSDS equivalent and deposited **one-sided into der Bodensee Pool**.

**BTC/CHF reference price source.** BTC is a **unit of account** here, not a payment currency — the yardstick the deposit size is measured against, deliberately chosen because BTC tracks purchasing power across cycles better than any USD-denominated figure. A "10-BTC-equivalent deposit" remains economically meaningful at $40K BTC and at $200K BTC. Nothing about BTC changes hands; the deposit is always paid in svZCHF/sUSDS one-sided into der Bodensee.

The BTC/CHF rate is a **spot-price average** computed at submission time across all currently-gauged pools holding any token in the `BTC_WRAPPERS` set (see Constitution §xxix; initial set: WBTC, cbBTC). The contract enumerates gauged pools, filters for those containing any BTC wrapper, reads spot rates (wrapped-BTC ↔ svZCHF, or against sUSDS then converted via arbitrage-aligned cross-rates), and averages. If a wrapper deprecates (e.g. cbBTC delisted), it falls out of the average; if a new BTC wrapper enters the constellation via composition challenge or new gauge approval, it auto-joins — no contract change required in either case.

**Why spot (not TWAP) is acceptable:**
- Averaging across multiple pools dilutes single-pool manipulation; an attacker would need to push BTC/svZCHF across every BTC-holding gauged pool simultaneously in the same block.
- Arbitrage keeps cross-pool BTC rates aligned naturally.
- The F-12 max-of-two-formulas rule backstops a low BTC reading — if manipulation pushes the (1) calculation toward zero, the (2) CHF-denominated calculation dominates and keeps the deposit meaningful.
- Gauge challenges are a one-time-fee low-frequency operation paid from the challenger's wallet; spending a few hundred thousand gas on pool enumeration + spot reads is acceptable here.

**Elite tail convention:** **p_tvl** and **p_eff** use **rank / N** (not CDF-from-bottom). Among **all gauged pools** (including Miliarium), **N** = count of gauged pools. Sort by **spot TVL**; **rank 1** = highest TVL → **p_tvl = rank / N**. Independently sort by **efficiency ratio** as in F-10 (3-epoch moving average); **rank 1** = highest efficiency → **p_eff = rank / N**. **Ties** break deterministically (e.g. lower pool contract address hex first).

**(1 − p_tvl)** and **(1 − p_eff)** are large when the target is elite on both axes (rank 1 ⇒ **p ≈ 1/N** ⇒ factors near **1 − 1/N**). The weakest pool on either axis has **p ≈ 1** → that factor → **0**, so the **10 BTC** floor typically binds.

```
deposit_CHF_component = 1_000_000 × sqrt((1 − p_tvl) × (1 − p_eff))

gauge_challenge_deposit = max( 10_BTC_in_CHF ,  deposit_CHF_component )
// convert to svZCHF/sUSDS equivalent; one-sided deposit into der Bodensee Pool; non-refundable
```

**Miliarium Aureum exclusion:** The **28 Miliarium Aureum** pools **cannot be gauge-challenged**. Structural changes to those slots go exclusively through the **Composition Challenge** path ([Constitution §xxvii](10_constitution.md)).

---

*All formulas are immutable from block 0. See [Immutable Parameters (§xxix)](10_constitution.md) for the full list.*
