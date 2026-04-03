# Tokenomics

## ix. Token Design: AuMM (Aureum Market Maker)

### Supply Rules (Immutable from Block 0)

| Parameter | Value |
|-----------|-------|
| Token name | **AuMM** |
| Pool token | **AuMT** |
| Maximum supply | **21,000,000 AuMM** |
| Emission unit | Block emission rate |
| Halving interval | Every 10,512,000 blocks (~4 years) |
| Emission model | Bitcoin-style geometric halving |

### Emission Schedule

| Era | Years | Block Emission Rate (AuMM) | Era Emission | Annual Emission (approx.) | Cumulative Supply | % of Total |
|-----|-------|---------------------|-------------|--------------------------|-------------------|------------|
| 0 | 0–4 | 1.00 | 10,512,000 | 2,628,000 | 10,512,000 | 50.06% |
| 1 | 4–8 | 0.50 | 5,256,000 | 1,314,000 | 15,768,000 | 75.09% |
| 2 | 8–12 | 0.25 | 2,628,000 | 657,000 | 18,396,000 | 87.60% |
| 3 | 12–16 | 0.125 | 1,314,000 | 328,500 | 19,710,000 | 93.86% |
| 4 | 16–20 | 0.0625 | 657,000 | 164,250 | 20,367,000 | 96.98% |
| 5 | 20–24 | 0.03125 | 328,500 | 82,125 | 20,695,500 | 98.55% |
| 6+ | 24+ | halving continues | diminishing | diminishing | approaches 21,000,000 | approaches 100% |

Each era spans 10,512,000 blocks (~4 years at 12 s/block). Emissions are specified in per-block terms only — no cycle-based accounting.

### Emission Distribution

- **Through end of Month 10 (Year 1):** emissions to the Miliarium tranche are split **equally** across the 28 Miliarium pools (**1/28** each).
- **Months 11–12 (Year 1):** a **two-month linear transition** that blends each pool’s equal one-twenty-eighth share with its CCB-derived share, ramping linearly from pure equal at the start of Month 11 to pure CCB at the end of Year 1. At the midpoint, the mix is half equal and half CCB. See `constitution.md` and `formulas.md`.
- **After Year 1:** pure CCB weighting — each pool is scored by its smoothed TVL and CCB multiplier, then normalized across all eligible pools. See `constitution.md` and `formulas.md`.
- No voting and no discretionary overrides.

### Per-Block Streaming

Emissions stream continuously per Ethereum block (~12 seconds). Each block, the protocol accrues AuMM to LPs in eligible pools proportional to:

```
lp_reward_per_block = emission_per_block × (LP_value_in_pool × pool_weight) / total_weighted_LP_value
```

Where `emission_per_block` is the current era's block emission rate (see table above), `LP_value_in_pool` is the USD value of the LP's AuMT position, `pool_weight` is the CCB-derived weight for that pool (updated at bi-weekly cycle boundaries), and `total_weighted_LP_value` is the sum across all eligible pools.

Deposit — start accruing. Withdraw — stop accruing. No snapshots, no pro-rata, no epoch-boundary gaming. An LP earns exactly what they earned up to the block they withdrew. At the halving block, the block emission rate drops 50%.

**No lock required.** LPs earn tokens while they provide liquidity. Remove liquidity, stop earning. No vesting. No cliff. Tokens are liquid immediately.

**Gauge weights update bi-weekly.** Emissions stream continuously, but the pool weights that determine how emissions are distributed across pools change only at bi-weekly governance cycle boundaries. Continuous, manipulation-resistant accrual paired with deliberate, algorithmic allocation.

### Governance: The "LP = Power" Model

#### Emission Direction: The CCB Engine

Emission allocation is driven by the **Continuous Central Bank (CCB)** — not by direct gauge voting. Each pool's base emission weight is its 60-day EMA of on-chain TVL as a share of total protocol TVL. Capital allocates itself. See `theoretical_foundation.md` (sections vi–vii) and `constitution.md` for the full mechanics.

#### Protocol Governance (Non-Emission Decisions)

For decisions beyond emission direction (fee parameters, treasury, gauge approvals/challenges, composition challenges), governance power is proportional to **active LP position in emission-qualified pools only** (AuMT held in qualifying pools):

```
Era 0 (years 0–4, pre-halving):        voting_power = (qualified_AuMT_value × time_in_pool)^(1/4)
Era 1+ (year 4 onward, post-halving):  voting_power = (qualified_AuMT_value × time_in_pool)^(1/3)
```

**`qualified_AuMT_value` is the USD-denominated value of the liquidity the tessera represents** — not the number of AuMT tokens held. Each tessera is a proportional claim on its pool's TVL. An AuMT representing a $50K position in ixAppia carries more governance weight than an AuMT representing a $5K position in a smaller pool, because the underlying locked value is different. Different pools have different TVLs and different token compositions; the governance formula normalises across all of them by pricing each tessera at the current market value of the liquidity it represents.

This ensures governance power reflects real economic commitment — not which pool you happen to be in, but how much capital you have at risk in productive pools.

The dampening exponent transitions from fourth root to cube root at the first halving block. This is a protocol-wide parameter shift — all positions recalculate under the new exponent, regardless of when they were opened. There is no two-tier governance class.

**Why these specific exponents:** Governance dampening exponents are chosen to prevent large-capital capture while preserving meaningful voting power for productive LPs. The key insight is that the ratio of the largest LP to total protocol TVL changes dramatically over time — the exponent must match the capture risk of each era.

- **Era 0 (fourth root):** At genesis, a $100M LP in a $1M protocol is 100% of TVL. Without dampening, that single actor controls the entire governance surface. Fourth-root compression reduces the gap: a $100M position has 18x the governance weight of a $1K position (vs. 100,000x under linear weighting). Maximum compression prevents single-actor capture when the protocol is most vulnerable. The whale still has more governance weight than a small LP — they just cannot steamroll every vote.
- **Era 1+ (cube root, permanent from year 4):** By year 4, TVL growth has naturally diluted individual power. The same $100M LP in a $1B protocol is now 10%, not 100%. Cube root is the appropriate compression for this regime: a $100M position has 46x the governance weight of a $1K position — more responsive to capital differences than fourth root, reflecting the lower capture risk in a larger ecosystem. The exponent relaxes at the first halving block and stays at cube root permanently — subsequent halvings affect the block emission rate only, not governance mechanics.

**Worked example:** At genesis, a protocol has $1M total TVL. One LP deposits $100M (100x the rest). Under linear weighting, that LP holds 99% of governance power — functionally a dictatorship. Under fourth root: the $100M LP has power proportional to $(100M)^{1/4} \approx 100$, while the remaining $1M of LPs collectively has power proportional to $(1M)^{1/4} \approx 31.6$. The whale holds roughly 76% — still dominant, but a coalition of smaller LPs can contest any proposal. By year 4, suppose the protocol has grown to $1B TVL and the same LP still has $100M (now 10% of TVL). Under cube root: $(100M)^{1/3} \approx 464$, while the remaining $900M has $(900M)^{1/3} \approx 965$. The whale holds roughly 32% — influential but far from controlling. Natural TVL growth did most of the work; the exponent relaxation reflects that reality.

The transition trigger is the halving block itself — immutable in the contract, no governance vote required, no discretionary timing.

AuMT in pools that fail any eligibility criterion carries zero governance weight. This ensures governance power flows exclusively from productive capital — the same capital that earns emissions and generates protocol fees.

**Governance power for non-emission decisions derives exclusively from active, qualified AuMT positions. AuMT in non-qualified pools carries zero weight. Voting power cannot be purchased on the open market.**

- **Voting power = dampened AuMT.** `(AuMT_value × time_in_pool)^(1/4)` — same formula as protocol governance. 14-day qualification, 6-month on-ramp, any withdrawal resets to zero. See `aureum_glossary.md` (section xxxv) for the full rule set.

#### Minimum Qualification Period and Governance On-Ramp

**Days 0–14: Zero governance weight.** Voting power requires at least **14 days (one full governance cycle)** of continuous qualified AuMT holding before any contribution to the governance power calculation. During this period, `time_in_pool = 0` in the formula — the position is invisible to governance.

**Days 14–180: Governance on-ramp.** After the 14-day qualification, `time_in_pool` begins accruing from zero. Because the governance formula uses `(qualified_AuMT_value × time_in_pool)^(1/4)`, voting power grows sublinearly with time. An LP at day 14 has minimal power. By month 6 (day 180), they reach **full voting weight**. This 6-month on-ramp ensures that governance power reflects sustained commitment, not recent capital deployment.

**Any withdrawal resets everything to zero.** If an LP removes liquidity from a qualified pool — any amount, even 1% — their governance power for that position drops to zero immediately, `time_in_pool` resets to zero, and the 14-day qualification clock restarts from scratch. The 6-month on-ramp begins again.

This eliminates:

- **Flash-LP attacks:** Borrow capital, deposit, vote, withdraw in the same block or day
- **Snapshot-based manipulation:** Accumulate AuMT moments before a governance snapshot, then exit
- **Cycle-boundary gaming:** Deposit at the end of a cycle to vote, remove at the start of the next
- **Ghost governance:** Withdraw most liquidity while retaining outsized governance weight from original position's time-weighting
- **Capital-rotation attacks:** Deposit large capital, vote immediately, then move capital elsewhere — the 6-month on-ramp means new capital has negligible governance power

#### Low-Turnout Safeguard

Every proposal type requires a minimum turnout of **20% of total qualified voting power**. If turnout falls below 20%, the proposal is **automatically rejected** regardless of vote outcome. There is no timelock fallback — the proposal simply fails and must be resubmitted.

This applies uniformly: gauge approvals, gauge challenges, fee changes, treasury spends, and composition challenges all share the same 20% floor. The burn deposit filters low-effort spam; the turnout floor prevents a small coordinated group from pushing through structural changes while the broader LP community is inactive.

#### Anti-Market Buying

Only active liquidity providers in **emission-qualified pools** possess governance voting power. AuMT held in pools that do not meet eligibility criteria carries zero voting weight. You cannot buy governance power on the open market, and you cannot earn it by parking capital in unproductive pools. You must be providing liquidity to pools that meet every anti-gaming criterion.

Fourth root (Era 0) then cube root (Era 1) dampens whale dominance — maximum compression when the protocol is smallest and most vulnerable, relaxing as TVL growth naturally decentralizes power. Time-weighting rewards commitment without requiring lock mechanisms.

#### Governance Scope

**What governance controls:**

- Fee parameters (swap fee %, yield fee %)
- Treasury allocation (within defined bounds)
- Gauge approvals and challenges (with timelock)
- Miliarium Aureum composition challenges (2/3 supermajority)

**What governance cannot control:** See Immutable Parameters (`constitution.md` §xxix) for the full list. In short: emission schedule, maximum supply, CCB engine parameters, governance dampening transition, eligibility criteria, fee distribution split, and all launch mechanics are immutable in contract.

### Token Properties

AuMM is a **100% liquid token**. There is no locking, no staking, no ve-mechanism, no wrapper. You hold AuMM, you can sell it at any time.

**AuMM carries zero governance power.** It does not vote on emissions, fee parameters, or any protocol decision. All governance — including emission direction — is AuMT-weighted (active LP positions in qualified pools). AuMM is a pure reward and value-capture token: earned by LPs, burned by the protocol.

AuMM accrues value exclusively through **buyback and burn** — the same mechanism as a corporate stock buyback programme. Protocol revenue is used to buy AuMM on the open market and permanently burn it. Circulating supply declines over time. Each remaining token represents a larger share of future protocol revenue. No yield farming. No APR on holding. Just scarcity.

## x. Value Capture

### Fee Splits

| Stream | Destination | Share |
|--------|-------------|-------|
| Swap fees | LP bonus | 50% |
| Swap fees | AuMM buyback and burn | 25% |
| Swap fees | Treasury | 25% |
| ERC-4626 yield fee (10% skim) | AuMM buyback and burn | 25% |
| ERC-4626 yield fee (10% skim) | Treasury | 75% |

### The Day-One Revenue Guarantee

Because ERC-4626 pools generate yield fee revenue regardless of trading volume, the protocol has treasury income from the first block. This is not dependent on routing, aggregator integration, or TVL growth. It's architectural. Every dollar of yield-bearing tokens in any pool generates protocol revenue automatically. During the treasury emission phase (months 0–10), this revenue accumulates alongside AuMM emissions, building the capital needed to seed the AuMM trading pool at month 6, fund the price ceiling stabilization mechanism (months 6–12), and activate buyback-and-burn from month 6 onward.

### Price Ceiling Stabilization (Months 6–12)

At month 6, the treasury seeds the AuMM trading pool (AuMM / svZCHF · sUSDS) using accumulated protocol revenue. From month 6 through month 12, the treasury operates a **price ceiling mechanism** that converts AuMM overvaluation into permanent pool depth.

#### The FDV/TVL ratio

The ceiling metric is the protocol’s **fully diluted valuation relative to its total value locked**:

```
FDV/TVL = (21,000,000 × AuMM_price) / total_protocol_TVL
```

Both inputs are readable on-chain with no external oracle. The AuMM trading pool is seeded at **FDV/TVL = 1** (fully diluted valuation equals protocol TVL at launch). The ratio is smoothed using a **21-day EMA** to filter short-term spikes — the pool’s **0.75% swap fee** makes single-day price manipulation expensive, and the EMA window ensures that transient volatility does not trigger unnecessary sells.

For context, established AMM protocols (Uniswap, Aerodrome, Cetus) trade at FDV/TVL multiples ranging from roughly 0.5 to 2. The ceiling is set at the upper bound of this range.

#### Ceiling trigger and sell mechanics

When the **EMA(21) of FDV/TVL ≥ 2**, the treasury sells **0.75% of the AuMM pool’s AuMM balance per day** into the pool, pushing the price down. Sells execute **once per day, every day** the EMA remains at or above the threshold, and stop automatically when EMA(21) drops below 2.

Revenue from ceiling sells is deposited as **permanent locked liquidity** into the Miliarium Aureum pools with the **lowest TVL** that meet the 4626 Quality Gate. The treasury can never withdraw this liquidity. Speculation above fair value directly strengthens the weakest pools in the constellation.

#### Limits and expiry

The ceiling is capped at **80% of treasury assets** — the treasury can never fully deplete itself on stabilization. If the stabilization inventory runs out, the mechanism stops naturally. The treasury's emission share drops to zero at **month 10** (no new AuMM after that point); the ceiling continues on existing inventory. At **month 12**, any excess AuMM remaining in the stabilization inventory is permanently burned. All stabilization parameters are immutable in contract.

### The Self-Reinforcing Loop

The AuMM trading pool holds ERC-4626 yield-bearing tokens (svZCHF, sUSDS, waEthUSDC) as 75% of its TVL. The protocol captures 10% of the yield those tokens generate. 25% of that yield fee goes to buyback-and-burn of AuMM. So the AuMM trading pool feeds the deflationary mechanism that makes AuMM scarcer — even though the pool itself receives no emissions. Higher TVL in the trading pool means more yield fee revenue, more buyback-and-burn, and fewer AuMM in circulation. The pool's own existence tightens the supply of the token it trades.

### The Deflationary Crossover

At scale, the combined buyback-and-burn from swap fees (25%) and yield fees (25% of 10%) can exceed the emission rate — making AuMM net deflationary despite ongoing LP mining rewards. BTC scarcity with productive backing.

**Worked example.** Assume $100M protocol TVL and $20M average daily volume at maturity:

| Burn source | Calculation | Annual burn (AuMM) |
|:------------|:------------|:-------------------|
| Swap fee burn | $20M/day × 0.05% fee × 25% to burn × 365 days = $912,500/year in buy pressure | Depends on AuMM price |
| Yield fee burn | $100M TVL × ~52% ERC-4626 weight × 2.5% avg yield × 10% skim × 25% to burn = $32,500/year in buy pressure | Depends on AuMM price |
| **Total annual burn pressure** | | **~$945,000/year** in AuMM purchased and destroyed |

| Era | Annual emission (AuMM) | Crossover at $1 AuMM? | Crossover at $0.50 AuMM? |
|:----|:----------------------|:----------------------|:-------------------------|
| 0 (years 0–4) | 2,628,000 | No ($945K < $2.63M) | No ($945K < $1.31M) |
| 1 (years 4–8) | 1,314,000 | No (but closer) | Yes ($945K > $657K) |
| 2 (years 8–12) | 657,000 | Yes ($945K > $657K) | Yes |

The crossover is structurally expected during **Era 1 or Era 2**, driven primarily by TVL growth and fee revenue — not by AuMM price appreciation. As protocol TVL grows beyond $100M, both swap volume and yield fee revenue scale with it, pulling the crossover earlier. Higher TVL means more fees, more burn, and a lower crossover threshold.

*This calculation is illustrative; actual crossover timing depends on protocol TVL, trading volume, and fee revenue at the time. The key structural point is that emissions halve every four years while revenue scales with TVL — the curves must eventually cross.*

### Immutable Reference

See Immutable Parameters (`constitution.md` §xxix).
