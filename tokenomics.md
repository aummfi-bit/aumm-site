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
| **LP bonus** | **50%** | Additional yield to LPs, proportional to their multiplier voting participation. Vote on Pioneer multipliers → earn bonus. |
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
