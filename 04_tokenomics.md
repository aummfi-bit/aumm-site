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

- **Through end of Month 10 (Year 1):** each block’s emission is split in two: a **der Bodensee bootstrap** share and an **LP tranche**. The bootstrap share is **80% of block emission at genesis**, decaying **linearly to zero** by the **final block of Month 10**; it is minted as **one-sided AuMM** into der Bodensee Pool (no LP tokens — same mechanic as one-sided svZCHF fee inflows; see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)). The **LP tranche** is the remainder of the block emission. The **28 Miliarium pools** each receive **1/28 of the LP tranche** (not of the full block emission while the bootstrap share is positive).
- **Months 11–12 (Year 1):** a **two-month linear transition** that blends each pool’s equal one-twenty-eighth share with its CCB-derived share, ramping linearly from pure equal at the start of Month 11 to pure CCB at the end of Year 1. At the midpoint, the mix is half equal and half CCB. See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).
- **After Year 1:** pure CCB weighting — each pool is scored by its smoothed TVL and CCB multiplier, then normalized across all eligible pools. See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).
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

Emission allocation is driven by the **Continuous Central Bank (CCB)** — not by direct gauge voting. Each pool's base emission weight is its 60-day EMA of on-chain TVL as a share of total protocol TVL. Capital allocates itself. See [Theoretical foundations (§§vi–vii)](03_theoretical_foundation.md) and the [Constitution](10_constitution.md) for the full mechanics.

#### Protocol Governance (Non-Emission Decisions)

For decisions beyond emission direction (fee parameters, gauge approvals/challenges, composition challenges), governance power is proportional to **active LP position in emission-qualified pools only** (AuMT held in qualifying pools):

```
Era 0 (years 0–4, pre-halving):        voting_power = (qualified_AuMT_value × time_in_pool)^(1/4)
Era 1+ (year 4 onward, post-halving):  voting_power = (qualified_AuMT_value × time_in_pool)^(1/3)
```

**`qualified_AuMT_value` is the USD-denominated value of the liquidity the tessera represents** — not the number of AuMT tokens held. Each tessera is a proportional claim on its pool's TVL. An AuMT representing a $50K position in ixEquitix carries more governance weight than an AuMT representing a $5K position in a smaller pool, because the underlying locked value is different. Different pools have different TVLs and different token compositions; the governance formula normalises across all of them by pricing each tessera at the current market value of the liquidity it represents.

This ensures governance power reflects real economic commitment — not which pool you happen to be in, but how much capital you have at risk in productive pools.

The dampening exponent transitions from fourth root to cube root at the first halving block. This is a protocol-wide parameter shift — all positions recalculate under the new exponent, regardless of when they were opened. There is no two-tier governance class.

**Why these specific exponents:** Governance dampening exponents are chosen to prevent large-capital capture while preserving meaningful voting power for productive LPs. The key insight is that the ratio of the largest LP to total protocol TVL changes dramatically over time — the exponent must match the capture risk of each era.

- **Era 0 (fourth root):** At genesis, a $100M LP in a $1M protocol is 100% of TVL. Without dampening, that single actor controls the entire governance surface. Fourth-root compression reduces the gap: a $100M position has 18x the governance weight of a $1K position (vs. 100,000x under linear weighting). Maximum compression prevents single-actor capture when the protocol is most vulnerable. The whale still has more governance weight than a small LP — they just cannot steamroll every vote.
- **Era 1+ (cube root, permanent from year 4):** By year 4, TVL growth has naturally diluted individual power. The same $100M LP in a $1B protocol is now 10%, not 100%. Cube root is the appropriate compression for this regime: a $100M position has 46x the governance weight of a $1K position — more responsive to capital differences than fourth root, reflecting the lower capture risk in a larger ecosystem. The exponent relaxes at the first halving block and stays at cube root permanently — subsequent halvings affect the block emission rate only, not governance mechanics.

**Worked example:** At genesis, a protocol has $1M total TVL. One LP deposits $100M (100x the rest). Under linear weighting, that LP holds 99% of governance power — functionally a dictatorship. Under fourth root: the $100M LP has power proportional to $(100M)^{1/4} \approx 100$, while the remaining $1M of LPs collectively has power proportional to $(1M)^{1/4} \approx 31.6$. The whale holds roughly 76% — still dominant, but a coalition of smaller LPs can contest any proposal. By year 4, suppose the protocol has grown to $1B TVL and the same LP still has $100M (now 10% of TVL). Under cube root: $(100M)^{1/3} \approx 464$, while the remaining $900M has $(900M)^{1/3} \approx 965$. The whale holds roughly 32% — influential but far from controlling. Natural TVL growth did most of the work; the exponent relaxation reflects that reality.

The transition trigger is the halving block itself — immutable in the contract, no governance vote required, no discretionary timing.

AuMT in pools that fail any eligibility criterion carries zero governance weight. This ensures governance power flows exclusively from productive capital — the same capital that earns emissions and generates protocol fees.

**Governance power for non-emission decisions derives exclusively from active, qualified AuMT positions. AuMT in non-qualified pools carries zero weight. Voting power cannot be purchased on the open market.**

- **Voting power = dampened AuMT.** `(AuMT_value × time_in_pool)^(1/4)` — same formula as protocol governance. 14-day qualification, 6-month on-ramp, any withdrawal resets to zero. See [Glossary (section xxxv)](12_aureum_glossary.md) for the full rule set.

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

This applies uniformly: gauge approvals, gauge challenges, fee changes, and composition challenges all share the same 20% floor. The deposit filters low-effort spam; the turnout floor prevents a small coordinated group from pushing through structural changes while the broader LP community is inactive.

#### Anti-Market Buying

Only active liquidity providers in **emission-qualified pools** possess governance voting power. AuMT held in pools that do not meet eligibility criteria carries zero voting weight. You cannot buy governance power on the open market, and you cannot earn it by parking capital in unproductive pools. You must be providing liquidity to pools that meet every anti-gaming criterion.

Fourth root (Era 0) then cube root (Era 1) dampens whale dominance — maximum compression when the protocol is smallest and most vulnerable, relaxing as TVL growth naturally decentralizes power. Time-weighting rewards commitment without requiring lock mechanisms.

#### Governance Scope

**What governance controls:**

- Fee parameters (swap fee %, yield fee %)
- Gauge approvals and challenges (with timelock)
- Miliarium Aureum composition challenges (2/3 supermajority)

**What governance cannot control:** See [Immutable Parameters (§xxix)](10_constitution.md) for the full list. In short: emission schedule, maximum supply, CCB engine parameters, governance dampening transition, eligibility criteria, fee distribution split, der Bodensee Pool parameters, and all launch mechanics are immutable in contract.

### Token Properties

AuMM is a **100% liquid token**. There is no locking, no staking, no ve-mechanism, no wrapper. You hold AuMM, you can sell it at any time.

**AuMM carries zero governance power.** It does not vote on emissions, fee parameters, or any protocol decision. All governance — including emission direction — is AuMT-weighted (active LP positions in qualified pools). AuMM is a pure reward and value-capture token: earned by LPs, supported by protocol revenue.

AuMM accrues value through **der Bodensee Pool** — the protocol's autonomous reserve. **Protocol-captured** revenue (swap fees from **other** pools and ERC-4626 yield fees) enters der Bodensee Pool as one-sided svZCHF inflows, continuously deepening the AuMM/svZCHF liquidity and strengthening the price floor. **Swap fees on trades inside der Bodensee Pool** accrue to der Bodensee LPs in the pool (see §x). The combination of linear weight decay (90% → 48% AuMM over 18 months) and growing svZCHF reserves creates a self-reinforcing price support mechanism. No yield farming. No APR on holding. Value backed by real revenue.

## x. Value Capture

### Fee Splits

**Canonical rule:** the **50/50 swap-fee split** applies to **swap fees generated on Miliarium pools and other non–der Bodensee pools** — not to swaps executed **inside** der Bodensee Pool.

| Stream | Destination | Share |
|--------|-------------|-------|
| Swap fees (non–der Bodensee pools) | LP bonus | 50% |
| Swap fees (non–der Bodensee pools) | der Bodensee Pool (one-sided svZCHF) | 50% |
| ERC-4626 yield fee (10% skim) | der Bodensee Pool (one-sided svZCHF) | 100% |
| Swap fees (**trades inside der Bodensee Pool**) | der Bodensee LPs (retained in pool) | 100% of the 0.75% fee |

**der Bodensee Pool** uses a **0.75%** swap-fee tier. Every wei of that fee **stays in the pool** for der Bodensee LPs — it does **not** enter the protocol-wide 50/50 splitter.

There is no treasury. **Protocol-captured** revenue flows to **der Bodensee Pool** as one-sided svZCHF inflows (autonomous reserve depth). The **other 50%** of swap fees on **other** pools returns directly to those pools’ LPs as LP bonus. All splits are contract-enforced and immutable.

### The Day-One Revenue Guarantee

Because ERC-4626 pools generate yield fee revenue regardless of trading volume, the protocol has revenue from the first block. This is not dependent on routing, aggregator integration, or TVL growth. It’s architectural. Every dollar of yield-bearing tokens in any pool generates protocol revenue automatically. From block 0, **protocol-captured** fees (yield skim + 50% of swap fees on other pools) flow into der Bodensee Pool as one-sided svZCHF inflows; **swap fees on trades inside der Bodensee** stay **in pool** for der Bodensee LPs.

### der Bodensee Pool (Autonomous Reserve)

der Bodensee Pool is the protocol’s self-regulating reserve — a two-token Liquidity Bootstrapping Pool (AuMM + svZCHF) with linear time-decay weights. It replaces any discretionary treasury or manual price stabilization mechanism.

#### Genesis seeding

At **pool creation**, the protocol deposits **1 AuMM** and **1 svZCHF** into der Bodensee Pool — minimal seed liquidity so the LBP exists and pricing can begin; **no** discretionary follow-on seeding. Everything after that is **bootstrap emissions**, **protocol-captured fees from other pools**, **escrow/governance** inflows, and **LP adds** per normal AMM mechanics.

#### Swap fee on der Bodensee

| Parameter | Value |
|-----------|-------|
| Swap fee (trades inside this pool) | **0.75%** |
| Fee routing | **100%** to der Bodensee LPs — accrues **in pool** (not via the 50/50 protocol split) |

#### Weight decay

| Parameter | Value |
|-----------|-------|
| Tokens | AuMM + svZCHF |
| Genesis weights | 90% AuMM / 10% svZCHF |
| End weights (18 months) | 48% AuMM / 52% svZCHF |
| Decay | Linear, automatic via block timestamp |
| Post-18-month | Weights fixed permanently at 48/52 |
| Emissions (AuMM) | **Months 1–10:** linear decay — **80%** of block emission at genesis as one-sided AuMM → **0%** at end of Month 10. **After Month 10:** no further AuMM via emission; only fee and escrow inflows |

At genesis, the high AuMM weight means the pool prices AuMM low relative to svZCHF — a natural starting point for a new token. As the AuMM weight declines linearly over 18 months, the pool progressively requires more svZCHF per unit of AuMM, creating organic price discovery driven by time-decay and real revenue inflows rather than speculative demand or manual intervention.

#### One-sided revenue inflows

**Protocol-captured** fee revenue — **50% of swap fees on other pools** plus **100% of ERC-4626 yield fees** — enters der Bodensee Pool as **one-sided svZCHF inflows**. This deepens the svZCHF side over time, strengthening the reserve and creating continuous buy pressure on AuMM within the pool. **Swap fees on trades inside der Bodensee** (0.75%) are **not** part of this split; they remain **in the pool** for der Bodensee LPs. The combination of declining AuMM weight and growing svZCHF reserves produces a self-reinforcing price floor that tightens as the protocol matures.

#### Routing yield and fees to svZCHF (non-svZCHF assets)

Miliarium pools hold **multiple** ERC-4626 and wrapped assets (e.g. sUSDS, waEthUSDC, sfrxUSD). The **10% yield skim** and the **protocol’s share of swap fees** accrue in whatever asset the pool settles in — not necessarily svZCHF at the point of accrual. **Before** a one-sided add to der Bodensee, the fee pipeline **converts to svZCHF** along fixed, contract-enforced paths: redeem vault shares where possible, then **swap or batch** through the integrated router (e.g. Balancer V3 routes / atomic multicall) so the **reserve always receives svZCHF**. There is no discretionary wallet: the same modules that skim fees execute the **svZCHF** leg before deposit to der Bodensee, per immutable wiring from block 0.

#### CCC alignment

der Bodensee Pool is a Continuous Capital Corporation (CCC) reserve in the spirit of Meisser’s thesis and Frankencoin’s implementation: capital allocation is algorithmic, revenue flows are rule-based, and there is no separate treasury that can receive, hold, or sell newly emitted tokens. The pool’s weight evolution and revenue routing are immutable from block 0. See [Protocol formulas — LBP weight decay (F-11)](11_formulas.md) for the formal weight decay definition.

### The Self-Reinforcing Loop

der Bodensee Pool holds svZCHF — an ERC-4626 yield-bearing savings vault. The protocol captures 10% of the yield those tokens generate. 100% of that yield fee flows back into der Bodensee Pool as additional svZCHF depth. So der Bodensee Pool feeds its own growth — and during **Months 1–10** it also receives one-sided AuMM bootstrap emissions (decaying to zero by month-end); **after** bootstrap emissions end, growth continues from fees and escrow alone. Higher TVL in der Bodensee Pool means more yield fee revenue, more svZCHF depth, and a stronger AuMM price floor. The pool’s own existence deepens the reserve of the token it trades.

### Reserve Depth Growth

At scale, the combined **protocol-captured** revenue from **swap fees on other pools** (50% to Bodensee) and **yield fees** (100% of the skim to Bodensee) flows into der Bodensee Pool as one-sided svZCHF inflows, continuously deepening the AuMM/svZCHF reserve — **in addition to** 0.75% swap fees retained **in pool** for der Bodensee LPs.

**Worked example.** Assume $100M protocol TVL and $20M average daily volume at maturity:

| Revenue source | Calculation | Annual svZCHF inflow |
|:---------------|:------------|:---------------------|
| Swap fee revenue | $20M/day × 0.05% fee × 50% to Bodensee × 365 days | ~$1,825,000/year |
| Yield fee revenue | $100M TVL × ~52% ERC-4626 weight × 2.5% avg yield × 10% skim × 100% to Bodensee | ~$130,000/year |
| **Total annual reserve inflow** | | **~$1,955,000/year** in svZCHF depth |

As protocol TVL grows beyond $100M, both swap volume and yield fee revenue scale with it, accelerating reserve growth. Higher TVL means more fees, deeper reserves, and a stronger AuMM price floor. The halving schedule reduces emission dilution every four years while revenue scales with TVL — the reserve grows faster than new supply enters the market.

*svZCHF/sUSDS deposits into der Bodensee Pool also occur through governance deposits (gauge proposals, challenges, fee changes) and Incendiary Boost escrow, further deepening the autonomous reserve.*

### Immutable Reference

See [Immutable Parameters (§xxix)](10_constitution.md).
