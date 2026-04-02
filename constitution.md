# Constitution

*The protocol's power structure, operating rules, and immutable boundaries.*

---

## I. Governance: The "LP = Power" Model

### Protocol Governance (Non-Emission Decisions)

For decisions beyond emission direction (fee parameters, treasury, upgrades), governance power is proportional to **active LP position in emission-qualified pools only** (AuMT held in qualifying pools):

```
Era 1 (Year 0–4, pre-halving):   voting_power = (qualified_AuMT_value × time_in_pool)^(1/4)
Era 2 (post-first-halving):      voting_power = (qualified_AuMT_value × time_in_pool)^(1/3)
```

**`qualified_AuMT_value` is the USD-denominated value of the liquidity the tessera represents** — not the number of AuMT tokens held. Each tessera is a proportional claim on its pool's TVL. An AuMT representing a $50K position in ixAppia carries more governance weight than an AuMT representing a $5K position in a smaller pool, because the underlying locked value is different. Different pools have different TVLs and different token compositions; the governance formula normalises across all of them by pricing each tessera at the current market value of the liquidity it represents.

This ensures governance power reflects real economic commitment — not which pool you happen to be in, but how much capital you have at risk in productive pools.

The dampening exponent transitions from fourth root to cube root at the first halving block. This is a protocol-wide parameter shift — all positions recalculate under the new exponent, regardless of when they were opened. There is no two-tier governance class.

**Why the transition matters:**

- **Era 1 (fourth root):** A $100M position has 18× the governance weight of a $1K position. At low TVL, a single whale can represent 20%+ of the entire protocol. Maximum compression prevents single-actor capture when the protocol is most vulnerable. The whale still has more governance weight than a small LP — they just can't steamroll every vote.
- **Era 2 (cube root):** A $100M position has 46× the governance weight of a $1K position. By year 4, TVL growth has naturally diluted individual power — a $10M whale in a $200M protocol is 5%, not 20%. The ecosystem no longer needs training wheels. The exponent relaxes because the primary decentralization force is now TVL distribution, not governance math.

The transition trigger is the halving block itself — immutable in the contract, no governance vote required, no discretionary timing.

AuMT in pools that fail any eligibility criterion carries zero governance weight. This ensures governance power flows exclusively from productive capital — the same capital that earns emissions and generates protocol fees.

**Governance power for non-emission decisions derives exclusively from active, qualified AuMT positions. AuMT in non-qualified pools carries zero weight. Voting power cannot be purchased on the open market.**

### Minimum Qualification Period and Governance On-Ramp

**Days 0–14: Zero governance weight.** Voting power requires at least **14 days (one full governance cycle)** of continuous qualified AuMT holding before any contribution to the governance power calculation. During this period, `time_in_pool = 0` in the formula — the position is invisible to governance.

**Days 14–180: Governance on-ramp.** After the 14-day qualification, `time_in_pool` begins accruing from zero. Because the governance formula uses `(qualified_AuMT_value × time_in_pool)^(1/4)`, voting power grows sublinearly with time. An LP at day 14 has minimal power. By month 6 (day 180), they reach **full voting weight**. This 6-month on-ramp ensures that governance power reflects sustained commitment, not recent capital deployment.

**Any withdrawal resets everything to zero.** If an LP removes liquidity from a qualified pool — any amount, even 1% — their governance power for that position drops to zero immediately, `time_in_pool` resets to zero, and the 14-day qualification clock restarts from scratch. The 6-month on-ramp begins again.

This eliminates:
- **Flash-LP attacks:** Borrow capital, deposit, vote, withdraw in the same block or day
- **Snapshot-based manipulation:** Accumulate AuMT moments before a governance snapshot, then exit
- **Cycle-boundary gaming:** Deposit at the end of a cycle to vote, remove at the start of the next
- **Ghost governance:** Withdraw most liquidity while retaining outsized governance weight from original position's time-weighting
- **Capital-rotation attacks:** Deposit large capital, vote immediately, then move capital elsewhere — the 6-month on-ramp means new capital has negligible governance power

### Soft Quorum for Major Decisions

Not all governance decisions carry equal weight. Major changes require minimum participation to prevent low-turnout capture:

| Decision Type | Quorum Requirement | Deposit (in AuMM, burned) | Failure Mode |
|--------------|-------------------|--------------------------|-------------|
| Bubble multiplier voting | No quorum (6-week cycle) | None | Tessera-weighted average of votes cast per new pool (first 90 days) |
| Gauge approval | No quorum | 100 svZCHF/sUSDS equivalent | Simple majority of votes cast |
| Gauge challenge | No quorum | 1,000 svZCHF/sUSDS equivalent | Simple majority to revoke; gauge removed if passed |
| Fee parameter changes | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail if quorum not met |
| Treasury spends >10% of balance | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail → 14-day timelock + public review |
| Fee distribution split changes (after Year 4) | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail → 14-day timelock + public review |
| Protocol upgrades | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail → 14-day timelock + public review |

All governance deposits are paid in **AuMM and burned automatically**. The deposit amount is denominated in **svZCHF or sUSDS equivalent, whichever is higher at the time of submission** — preventing gaming via currency fluctuation. Gauge proposals: 100 equivalent. All other proposals and challenges: 1,000 equivalent. Non-refundable. Every governance action creates deflationary pressure on AuMM.

Uncontested proposals with very low turnout do not pass silently. They either auto-fail or route to a timelock with a mandatory public review period. This prevents a small coordinated group from pushing through structural changes while the broader LP community is inactive.

**Anti-Market Buying:** Only active liquidity providers in **emission-qualified pools** possess governance voting power. AuMT held in pools that do not meet eligibility criteria carries zero voting weight. You cannot buy governance power on the open market, and you cannot earn it by parking capital in unproductive pools. You must be providing liquidity to pools that meet every anti-gaming criterion.

**What governance controls:**
- Bubble multipliers via 6-weekly tessera-weighted voting for new pools in their first 90 days (constrained to [0.90–2.00])
- *Note: Pioneer pool multipliers are set automatically by the PMAR — not by governance vote*
- Gauge approval (AuMT vote to grant a pool emission eligibility — requires 100 svZCHF/sUSDS equivalent in AuMM, burned). **Available from month 11 onward only.**
- Gauge revocation (AuMT vote to remove a gauge via challenge — requires 1,000 svZCHF/sUSDS equivalent in AuMM, burned)
- Fee parameters (swap fee %, yield fee %)
- Treasury allocation (within defined bounds)
- Protocol upgrades (with timelock)

**What governance cannot control:** See **Immutable Parameters** at the end of this document.

---

## II. Emission Operating Rules

### The Continuous Central Bank (CCB)

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

### Pioneer Multiplier Adjustment Rule (PMAR)

The PMAR is a deterministic, oracle-free mechanism that automatically steers emission multipliers across the 25 immutable Pioneer pools. It replaces governance-driven multiplier voting entirely.

**Inputs (All On-Chain, Oracle-Free)**

Recalculated at every bi-weekly governance cycle boundary using the 60-day EMA already maintained by the CCB engine.

Global Pioneer ratio — Pioneer share of protocol TVL:

```
r_P(t) = TVL_Pioneer_EMA60(t) / TVL_Protocol(t)
```

Per-pool ratio — each Pioneer pool's share within the Pioneer constellation:

```
r_i(t) = TVL_i_EMA60(t) / TVL_Pioneer_EMA60(t)     for each Pioneer pool i = 1..25
```

**Slope Calculation**

```
slope_P(t) = r_P(t) - r_P(t-1)
slope_i(t) = r_i(t) - r_i(t-1)
```

**Dead Zone**

A dead zone prevents noise-driven oscillation when slopes hover near zero:

```
epsilon_P = 0.001 × r_P(t)
epsilon_i = 0.001 × r_i(t)
```

If `|slope| < epsilon`, the adjustment is 0.

**Adjustment Rules**

Global adjustment (uniform to all 25 pools):

| Condition | Delta |
|-----------|-------|
| `slope_P < -epsilon_P` (Pioneers losing share) | +0.05 |
| `slope_P > +epsilon_P` (Pioneers gaining share) | -0.05 |
| Within dead zone | 0 |

Per-pool adjustment:

| Condition | Delta |
|-----------|-------|
| `slope_i < -epsilon_i` (pool losing intra-share) | +0.05 |
| `slope_i > +epsilon_i` (pool gaining intra-share) | -0.05 |
| Within dead zone | 0 |

Multiplier update:

```
M_i(t) = clamp( M_i(t-1) + delta_global + delta_intra_i,  0.75,  1.25 )
```

**Guarantees:**
- **Bounded**: All multipliers stay inside [0.75, 1.25] at every step.
- **Anticyclical**: Group-level loss of share triggers a collective boost; internal crowding triggers relative penalties.
- **Stable**: The 0.1%-of-ratio dead zone prevents flip-flopping on noise.
- **Immutable**: Step size (+/-0.05), clamp bounds, dead zone threshold, and EMA horizon are all hard-coded from block 0.

See the full [PMAR Specification](PMAR.md) for detailed scenario walkthroughs and integration notes.

### Anti-Gaming Criteria

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

---

## III. Immutable Parameters

The following parameters are immutable in the smart contracts. No governance vote, no multisig, no admin key can modify them. They are the protocol's constitution.

**Emission schedule.** 21M maximum supply. BTC-style halving every ~4 years. Per-block streaming. Immutable from block 0.

**Governance dampening transition.** Fourth root (Era 1, pre-halving) → cube root (Era 2, post-halving). Triggered at halving block. No governance vote. All positions recalculate.

**Any withdrawal = governance reset.** Full details in Governance section.

**Eligibility criteria.** ERC-4626 composition ≥52% with $5M/30 BTC/4M svZCHF vault TVL floor per token. Volume percentile floors. Efficiency-based emission caps. Grace period schedule. Gauge revocation after 4 consecutive failed cycles. None of this can be changed.

**Pioneer pool tags.** All 25 pre-defined at launch, locked from block 0. No open slots. PMAR-steered multiplier [0.75–1.25]. Non-transferable. Revoked on gauge loss. No replacements ever.

**Continuous Central Bank (CCB).** Emission allocation driven by 60-day EMA of on-chain TVL. Each pool's emission share = `(TVL_EMA60 * M * Incendiary_mult) / sum(all pool scores)`. Pioneer multipliers set automatically by PMAR [0.75–1.25] — no governance vote. Bubble multiplier range [0.90–2.00] for first 90 days post-gauge-approval (governance-voted). All parameters immutable.

**Pioneer Multiplier Adjustment Rule (PMAR).** Deterministic, oracle-free multiplier steering for Pioneer pools. +/-0.05 adjustments based on slope of EMA(60) TVL ratios with 0.1%-of-ratio dead zone. Clamped to [0.75, 1.25]. Recalculated at bi-weekly cycle boundaries. All parameters immutable from block 0.

**Incendiary Boost.** 30-day supplementary emission funded by operator AuMM escrow. Emission rate pegged to 85th percentile efficiency × (2 - pool's efficiency rank). Priority claim on block rewards. Renewal only after pool enters 85th percentile in Efficiency Tournament. All parameters immutable.

**Sandbox fast-track.** Non-gauged pools reaching top 10% efficiency organically earn automatic gauge approval. No governance vote. Immutable threshold.

**Fee distribution split.** Immutable for first 4 years. Governance-adjustable only after first halving.

**Governance proposal deposits.** All paid in AuMM, burned automatically. Denominated in svZCHF or sUSDS equivalent (whichever is higher). 100 equivalent for gauge proposals, 1,000 for all other governance. Non-refundable. This is immutable.
