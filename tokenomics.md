# Tokenomics

## ix. Token Design: AuMM (Aureum Market Maker)

### Supply Rules (Immutable from Block 0)

| Parameter | Value |
|-----------|-------|
| Token name | **AuMM** |
| Pool token | **AuMT** |
| Maximum supply | **21,000,000 AuMM** |
| Emission unit | Per-block reward |
| Halving interval | Every 10,512,000 blocks (~4 years) |
| Emission model | Bitcoin-style geometric halving |

### Emission Schedule

| Era | Years | Blocks per Era | Block Reward (AuMM) | Era Emission | Cumulative Supply | % of Total |
|-----|-------|----------------|---------------------|-------------|-------------------|------------|
| 0 | 0-4 | 10,512,000 | 1.00 | 10,512,000 | 10,512,000 | 50.06% |
| 1 | 4-8 | 10,512,000 | 0.50 | 5,256,000 | 15,768,000 | 75.09% |
| 2 | 8-12 | 10,512,000 | 0.25 | 2,628,000 | 18,396,000 | 87.60% |
| 3 | 12-16 | 10,512,000 | 0.125 | 1,314,000 | 19,710,000 | 93.86% |
| 4+ | ... | ... | halving continues | ... | approaches 21,000,000 | approaches 100% |

The old cycle-based emission table is removed. Emissions are specified only in per-block terms.

### Emission Distribution

- **Through end of Month 10 (Year 1):** emissions to the Miliarium tranche are split **equally** across the 28 pools (**1/28** each).
- **Months 11–12 (Year 1):** a **two-month linear transition** that blends each pool’s equal one-twenty-eighth share with its CCB-derived share, ramping linearly from pure equal at the start of Month 11 to pure CCB at the end of Year 1. At the midpoint, the mix is half equal and half CCB. See `constitution.md` and `formulas.md`.
- **After Year 1:** pure CCB weighting — each pool is scored by its smoothed TVL, MAMAR multiplier, and Incendiary multiplier, then normalized across all eligible pools. See `constitution.md` and `formulas.md`.
- No voting, no Bubble multipliers, and no discretionary overrides.

### Governance: The "LP = Power" Model

#### Emission Direction: The CCB Engine

Emission allocation is driven by the **Continuous Central Bank (CCB)** — not by direct gauge voting. Each pool's base emission weight is its 60-day EMA of on-chain TVL as a share of total protocol TVL. Capital allocates itself. See `theoretical_foundation.md` (sections vi–vii) and `constitution.md` for the full mechanics.

#### Protocol Governance (Non-Emission Decisions)

For decisions beyond emission direction (fee parameters, treasury, gauge approvals/challenges, composition challenges), governance power is proportional to **active LP position in emission-qualified pools only** (AuMT held in qualifying pools):

```
Era 0 (years 0–4, pre-halving):   voting_power = (qualified_AuMT_value × time_in_pool)^(1/4)
Era 1 (years 4–8, post-halving):  voting_power = (qualified_AuMT_value × time_in_pool)^(1/3)
```

**`qualified_AuMT_value` is the USD-denominated value of the liquidity the tessera represents** — not the number of AuMT tokens held. Each tessera is a proportional claim on its pool's TVL. An AuMT representing a $50K position in ixAppia carries more governance weight than an AuMT representing a $5K position in a smaller pool, because the underlying locked value is different. Different pools have different TVLs and different token compositions; the governance formula normalises across all of them by pricing each tessera at the current market value of the liquidity it represents.

This ensures governance power reflects real economic commitment — not which pool you happen to be in, but how much capital you have at risk in productive pools.

The dampening exponent transitions from fourth root to cube root at the first halving block. This is a protocol-wide parameter shift — all positions recalculate under the new exponent, regardless of when they were opened. There is no two-tier governance class.

**Why the transition matters:**

- **Era 0 (fourth root):** A $100M position has 18x the governance weight of a $1K position. At low TVL, a single whale can represent 20%+ of the entire protocol. Maximum compression prevents single-actor capture when the protocol is most vulnerable. The whale still has more governance weight than a small LP — they just can't steamroll every vote.
- **Era 1 (cube root):** A $100M position has 46x the governance weight of a $1K position. By year 4, TVL growth has naturally diluted individual power — a $10M whale in a $200M protocol is 5%, not 20%. The ecosystem no longer needs training wheels. The exponent relaxes because the primary decentralization force is now TVL distribution, not governance math.

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

Uncontested proposals with very low turnout do not pass silently. They either auto-fail or route to a timelock with a mandatory public review period. This prevents a small coordinated group from pushing through structural changes while the broader LP community is inactive.

#### Anti-Market Buying

Only active liquidity providers in **emission-qualified pools** possess governance voting power. AuMT held in pools that do not meet eligibility criteria carries zero voting weight. You cannot buy governance power on the open market, and you cannot earn it by parking capital in unproductive pools. You must be providing liquidity to pools that meet every anti-gaming criterion.

Fourth root (Era 0) then cube root (Era 1) dampens whale dominance — maximum compression when the protocol is smallest and most vulnerable, relaxing as TVL growth naturally decentralizes power. Time-weighting rewards commitment without requiring lock mechanisms.

#### Governance Scope

**What governance controls:**

- Fee parameters (swap fee %, yield fee %)
- Treasury allocation (within defined bounds)
- Gauge approvals and challenges (with timelock)
- Miliarium Aureum composition challenges (2/3 supermajority)

**What governance cannot control:** See Immutable Parameters in `constitution.md` for the full list. In short: emission schedule, maximum supply, CCB engine parameters (60-day EMA, Miliarium Aureum emissions, Incendiary Boost mechanics, Sandbox fast-track threshold), governance dampening transition, eligibility criteria, fee distribution split, and all launch mechanics are immutable in contract.

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

Because ERC-4626 pools generate yield fee revenue regardless of trading volume, the protocol has treasury income from the first block. This is not dependent on routing, aggregator integration, or TVL growth. It's architectural. Every dollar of yield-bearing tokens in any pool generates protocol revenue automatically. During the treasury emission phase (months 0–10), this revenue accumulates alongside AuMM emissions, building the capital needed to seed the AuMM trading pool at month 6, fund the price ceiling stabilization mechanism, and activate buyback-and-burn from month 6 onward.

### The Deflationary Crossover

At scale, the combined buyback-and-burn from swap fees (25%) and yield fees (25% of 10%) can exceed the emission rate — making AuMM net deflationary despite ongoing LP mining rewards. BTC scarcity with productive backing.

### Immutable Reference

See Immutable Parameters in `constitution.md`.
