## I — Token Design: AuMM (Aureum Market Maker)

### Supply Schedule

| Parameter | Value |
|-----------|-------|
| Token name | **AuMM** (Aureum Market Maker) |
| Pool token | **AuMT** (Aureum Market Tessera) |
| Maximum supply | 21,000,000 |
| Emission rate (Era 1) | ~0.000496 AuMM per block (~50 AuMM per 2-week governance cycle) |
| Governance cycle | **2 weeks** (bi-weekly gauge votes) |
| Halving interval | Every 105 governance cycles (~4 years) |
| First halving | ~4 years after launch |
| Full emission timeline | ~20 years (99%+ mined by year 16) |

### Emission Schedule

| Era | Years | Per-Block Rate | Per Governance Cycle | Annual Emission | Cumulative % |
|-----|-------|---------------|---------------------|-----------------|-------------|
| 1 | 0–4 | ~0.000496 AuMM | ~50 AuMM | 1,300 | 49.5% |
| 2 | 4–8 | ~0.000248 AuMM | ~25 AuMM | 650 | 74.8% |
| 3 | 8–12 | ~0.000124 AuMM | ~12.5 AuMM | 325 | 87.3% |
| 4 | 12–16 | ~0.000062 AuMM | ~6.25 AuMM | 162.5 | 93.6% |
| 5 | 16–20 | ~0.000031 AuMM | ~3.125 AuMM | 81.25 | 96.7% |
| 6+ | 20+ | <0.000031 AuMM | <3.125 AuMM | <81.25 | →100% |

*The model mirrors BTC's emission curve — front-loaded but declining, creating scarcity over time while incentivising early LP participation.*

### Distribution Mechanism

**Emissions stream continuously per block.** Every Ethereum block (~12 seconds), the protocol accrues AuMM to LPs in eligible pools proportional to:

```
lp_reward_per_block = emission_per_block × (LP_value_in_pool × pool_weight) / total_weighted_LP_value
```

Where:
- `emission_per_block` = current era's total emission divided by blocks per governance cycle (~100,800 blocks per 2 weeks at 12s/block)
- `LP_value_in_pool` = USD value of LP's AuMT position in that pool
- `pool_weight` = CCB-derived weight for that pool (60-day EMA TVL share × Pioneer multiplier if applicable, updated bi-weekly)
- `total_weighted_LP_value` = sum across all eligible pools

Deposit → start accruing. Withdraw → stop accruing. No snapshots, no pro-rata, no epoch-boundary gaming. An LP earns exactly what they earned up to the block they withdrew. At the halving block, the per-block rate drops 50%. Clean.

**Why per-block.** Prevents epoch-boundary gaming (deposit before snapshot, earn full period, withdraw). Per-block streaming is the standard pattern used by Balancer gauges, Curve gauges, and MasterChef contracts.

**Gauge weights update bi-weekly.** Emissions stream continuously, but the pool weights that determine how emissions are distributed across pools change only at bi-weekly governance cycle boundaries. This separates the two concerns: continuous, manipulation-resistant accrual paired with deliberate, governance-driven allocation.

**No lock required.** LPs earn tokens while they provide liquidity. Remove liquidity, stop earning. No vesting. No cliff. Tokens are liquid immediately.

### Token Properties

AuMM is a **100% liquid token**. There is no locking, no staking, no ve-mechanism, no wrapper. You hold AuMM, you can sell it at any time.

**AuMM carries zero governance power.** It does not vote on emissions, fee parameters, or any protocol decision. All governance — including emission direction — is AuMT-weighted (active LP positions in qualified pools). AuMM is a pure reward and value-capture token: earned by LPs, burned by the protocol.

AuMM accrues value exclusively through **buyback and burn** — the same mechanism as a corporate stock buyback programme. Protocol revenue is used to buy AuMM on the open market and permanently burn it. Circulating supply declines over time. Each remaining token represents a larger share of future protocol revenue. No yield farming. No APR on holding. Just scarcity.

---

### Token Supply Transparency

The aumm.fi dashboard publishes in real time:
- **Total AuMM emitted** — cumulative tokens distributed to LPs and treasury since block 0
- **Total AuMM burned** — cumulative tokens destroyed through governance deposits, excess burns, and buyback-and-burn
- **Net circulating supply** — emitted minus burned
- **Burn rate** — trailing 30-day annualised burn rate as % of circulating supply

---

## II — Value Capture: Two Revenue Streams

### Stream 1: Swap Fees

| Destination | Share | Mechanism |
|-------------|-------|-----------|
| **LP bonus** | **50%** | Additional yield to LPs, proportional to their governance participation (Bubble votes, gauge votes, protocol governance). |
| AuMM buyback and burn | 25% | Market buy AuMM + permanent burn. Deflationary pressure. |
| Protocol treasury | 25% | Funds development, audits, and integrations |

### Stream 2: ERC-4626 Yield Fees

The Aequilibrium vault takes 10% of all yield accrued on ERC-4626 tokens (svZCHF, waEthUSDT, GHO Prime, sUSDS, etc.). This is protocol revenue from day one — it doesn't depend on swap volume.

| Destination | Share | Mechanism |
|-------------|-------|-----------|
| AuMM buyback and burn | 25% | Permanent deflationary pressure from block one |
| Protocol treasury | 75% | Funds ongoing operations |

### The Day-One Revenue Guarantee

Because ERC-4626 pools generate yield fee revenue regardless of trading volume, the protocol has treasury income from the first block. This is not dependent on routing, aggregator integration, or TVL growth. It's architectural. Every dollar of yield-bearing tokens in any pool generates protocol revenue automatically. During the treasury emission phase (months 0–10), this revenue accumulates alongside AuMM emissions, building the capital needed to seed the AuMM trading pool at month 6, fund the price ceiling stabilization mechanism, and activate buyback-and-burn from month 6 onward.

### The Deflationary Crossover

At scale, the combined buyback-and-burn from swap fees (25%) and yield fees (25% of 10%) can exceed the emission rate — making AuMM net deflationary despite ongoing LP mining rewards. BTC scarcity with productive backing.

### AuMM Liquidity: The Non-Emission Pool

The AuMM trading pool operates as a non-emission pool — AuMM cannot be a component in emission-eligible pools (no self-referential tokens). LPs earn only swap fees plus native ERC-4626 yield on the non-AuMM side (svZCHF, waEthUSDC, sUSDS — 75% of pool TVL is yield-bearing). No circular incentives. The treasury seeds the pool at month 6, operates the price ceiling between months 6–10, then at month 10 deposits max 80% of remaining stablecoin balance plus corresponding AuMM at market price and burns all leftover AuMM.

**The LP proposition.** svZCHF, waEthUSDC, and sUSDS are ERC-4626 tokens that accrue native yield inside the pool. LPs earn swap fees from AuMM trading PLUS 2–4% native yield on 75% of their position. That's a competitive return without any emission subsidies.

**Volume comes from two natural flows.** Sell-side: LPs in emission-eligible pools selling AuMM they earned from mining. Buy-side: participants who want exposure to the protocol's growth via the deflationary supply mechanics (buyback-and-burn reducing circulating supply over time). No governance motivation needed — AuMM carries zero voting power.

**The self-reinforcing loop.** The protocol captures the 10% yield fee on the ERC-4626 tokens in the pool (svZCHF, sUSDS, waEthUSDC). 25% of that goes to buyback-and-burn of AuMM. So the AuMM trading pool feeds the deflationary mechanism that makes AuMM scarcer — even though the pool itself receives no emissions.

---

## III — Proof of Real Yield Dashboard

The aumm.fi dashboard publishes all protocol economics in real time — on-chain, oracle-free, independently verifiable. No proprietary data feeds. Every number is derived from public smart contract state.

### Supply Metrics

| Metric | Source | Update Frequency |
|:-------|:-------|:-----------------|
| **Total AuMM emitted** | Cumulative emissions from block 0 (LP rewards + treasury phase) | Per block |
| **Total AuMM burned** | Governance deposits + excess burns + buyback-and-burn | Per block |
| **Net circulating supply** | Emitted − burned | Per block |
| **30-day trailing burn rate** | Annualised burn as % of circulating supply | Daily |
| **Emission era** | Current halving era and per-block rate | Per halving block |

### Revenue Metrics

| Metric | Source | Update Frequency |
|:-------|:-------|:-----------------|
| **Swap fee revenue** | Cumulative fees across all pools, split by destination (LP bonus / buyback / treasury) | Per swap |
| **ERC-4626 yield revenue** | 10% skim on vault yield across all pools, split by destination (buyback / treasury) | Per yield accrual |
| **Total protocol revenue** | Swap fees + yield fees combined | Daily |
| **Revenue per pool** | Per-pool breakdown of swap fees and yield revenue | Per governance cycle |
| **Efficiency ratio per pool** | `(swap_fees + yield_revenue) / emissions_received` — the Efficiency Tournament input | Per governance cycle |

### Pool Health Metrics

| Metric | Source | Update Frequency |
|:-------|:-------|:-----------------|
| **TVL per pool** | Spot and 60-day EMA | Per block / per cycle |
| **PMAR multiplier per Pioneer** | Current multiplier [0.75–1.25] for each Mercatūs Praecursorii | Per governance cycle |
| **Volume percentile ranking** | Each pool's position in the protocol-wide volume distribution | Per 4-week rolling window |
| **Efficiency Tournament ranking** | All pools ranked by efficiency ratio (2-epoch moving average) | Per governance cycle |
| **Eligibility status** | Active / Warning / Disqualified per pool | Per governance cycle |

### Deflationary Crossover Tracker

The dashboard tracks whether the protocol has reached the **deflationary crossover** — the point where combined buyback-and-burn exceeds the emission rate:

```
Net supply change = Emissions per block − Burn per block
```

| State | Condition | Implication |
|:------|:----------|:------------|
| **Inflationary** | Emissions > Burns | Supply growing, normal for early eras |
| **Crossover** | Emissions ≈ Burns | Supply stabilising, protocol approaching maturity |
| **Deflationary** | Burns > Emissions | Supply shrinking — BTC scarcity with productive backing |

All metrics are derived from on-chain state. No off-chain APIs, no proprietary feeds, no oracle dependencies. Any participant can independently verify every number by reading the smart contracts directly.

---

## IV — Treasury

### Revenue Sources

The protocol treasury is funded exclusively by stablecoin fee revenue — never by selling AuMM.

| Source | Treasury Share | Mechanism |
|:-------|:--------------|:----------|
| Swap fees | 25% | Stablecoin revenue from trading activity across all pools |
| ERC-4626 yield fees | 75% of the 10% skim | Stablecoin revenue from vault yield accrued in all pools |

**The Day-One Guarantee.** Because ERC-4626 pools generate yield fees regardless of swap volume, the treasury has income from block 0. This is architectural — every dollar of yield-bearing tokens in any pool generates treasury revenue automatically.

### Treasury Emission Phase (Months 0–10)

During the launch phase, the treasury also receives a declining share of AuMM emissions:

| Period | Treasury AuMM Share | Purpose |
|:-------|:-------------------|:--------|
| Months 0–6 | 75% → 50% (declining) | Accumulate AuMM for trading pool seed |
| Month 6 | — | Deploy 80% of treasury assets to seed AuMM trading pool |
| Months 6–10 | 50% → 0% (declining) | Price ceiling stabilization inventory |
| Month 10 | **Hard stop** | Remaining stablecoins + AuMM deposited as locked liquidity; leftover AuMM burned |
| Month 10+ | **0% — permanent** | Treasury never receives AuMM again |

**The "no team allocation" guarantee.** AuMM received during the treasury phase is used exclusively for protocol-owned liquidity — never converted to stablecoins for team spending. Stabilization sale proceeds are deposited as permanently locked liquidity in qualifying Mercatūs Praecursorii. The team cannot extract value through AuMM sales.

### Operating Budget

After month 10, the treasury operates entirely on stablecoin fee revenue:

| Category | Allocation | Notes |
|:---------|:----------|:------|
| Audits & Security | 40% | Ongoing audit coverage, bug bounties, formal verification |
| Development | 30% | Smart contract maintenance, frontend, integrations |
| Operations | 20% | Infrastructure, RPC, subgraph, monitoring |
| Reserve | 10% | Emergency fund |

### Governance Controls

Treasury spending requires governance vote (AuMT-weighted, qualified pool LPs only). No single party controls the treasury.

| Decision | Quorum | Deposit | Process |
|:---------|:-------|:--------|:--------|
| Treasury spend ≤10% of balance | No quorum | 1,000 svZCHF/sUSDS equiv in AuMM (burned) | Simple majority |
| Treasury spend >10% of balance | 20% of qualified voting power | 1,000 svZCHF/sUSDS equiv in AuMM (burned) | Auto-fail if quorum not met → 14-day timelock + public review |

**Multi-sig.** Founding team members initially hold multi-sig keys, transitioning to LP-elected council after Year 1. The multi-sig executes governance-approved spending only — it cannot initiate spends unilaterally.

### Treasury Transparency

All treasury flows are published on the Proof of Real Yield Dashboard:

- **Treasury balance** — current stablecoin holdings by denomination
- **Revenue inflow** — trailing 30-day treasury revenue (swap fees + yield fees)
- **Spending outflow** — all governance-approved disbursements with transaction links
- **Locked liquidity** — permanently locked LP positions in Mercatūs Praecursorii from stabilization proceeds (treasury can never withdraw)
