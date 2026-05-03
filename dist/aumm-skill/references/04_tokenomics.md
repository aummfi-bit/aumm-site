<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 04_tokenomics.md — DO NOT EDIT -->
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

Each era spans 10,512,000 blocks (~4 years at 12 s/block). Per-block terms only — no cycle-based accounting.

### Emission Distribution

- **Through end of Month 10 (Year 1):** each block’s emission splits into a **der Bodensee bootstrap** share and an **LP tranche**. The bootstrap share follows a **piecewise linear decay**: **80% at genesis → 50% at end of Month 6**, then **50% → 0% by end of Month 10**; minted as **one-sided AuMM** into der Bodensee Pool (no LP tokens — same mechanic as one-sided stablecoin fee inflows; see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)). The **LP tranche** is the remainder. The **28 Miliarium pools** each receive **1/28 of the LP tranche** (not of the full block emission while the bootstrap share is positive).
- **Months 11–12 (Year 1):** a **two-month linear transition** blending each pool’s equal one-twenty-eighth share with its CCB-derived share, ramping from pure equal at the start of Month 11 to pure CCB at the end of Year 1. At midpoint, half and half. See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).
- **After Year 1:** pure CCB weighting — each pool scored by smoothed TVL and CCB multiplier, normalized across all eligible pools. See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).
- No voting and no discretionary overrides.

### Per-Block Streaming

Emissions stream continuously per Ethereum block (~12 seconds). Each block, AuMM accrues to LPs in eligible pools proportional to:

```
lp_reward_per_block = emission_per_block × (LP_value_in_pool × pool_weight) / total_weighted_LP_value
```

Where `emission_per_block` is the current era's block emission rate (see table above), `LP_value_in_pool` is the USD value of the LP's AuMT position, `pool_weight` is the CCB-derived weight for that pool (updated at bi-weekly cycle boundaries), and `total_weighted_LP_value` is the sum across all eligible pools.

Deposit — start accruing. Withdraw — stop accruing. No snapshots, no pro-rata, no epoch-boundary gaming. An LP earns exactly what they earned up to the block they exit. At the halving block, the emission rate drops 50%.

**No lock required.** LPs earn tokens while they provide liquidity. Remove liquidity, stop earning. No vesting. No cliff. Tokens are liquid immediately.

**Gauge weights update bi-weekly.** Emissions stream continuously, but pool weights change only at bi-weekly governance cycle boundaries. Continuous, manipulation-resistant accrual paired with deliberate, algorithmic allocation.

### Governance: The "LP = Power" Model

#### Emission Direction: The CCB Engine

Emission allocation is driven by the **Continuous Central Bank (CCB)** — not by direct gauge voting. Each pool's base emission weight is its 60-day EMA of on-chain TVL as a share of total protocol TVL. Capital allocates itself. See [Theoretical foundations](03_theoretical_foundation.md) (CCB §§vi–vii; **EMA** §vi-b) and [Constitution](10_constitution.md).

#### Protocol Governance (Non-Emission Decisions)

For decisions beyond emission direction (fee parameters, gauge approvals/challenges, composition challenges), governance power is proportional to **active LP position in emission-qualified pools only** (AuMT held in qualifying pools):

```
Era 0 (years 0–4, pre-halving):        voting_power = (qualified_AuMT_value × time_in_pool)^(1/4)
Era 1+ (year 4 onward, post-halving):  voting_power = (qualified_AuMT_value × time_in_pool)^(1/3)
```

**`qualified_AuMT_value` is the USD-denominated value of the liquidity the tessera represents** — not the number of AuMT tokens held. Each tessera is a proportional claim on its pool's TVL. An AuMT representing a $50K position in ixEquitix carries more governance weight than one representing a $5K position in a smaller pool because the underlying locked value differs. The governance formula normalises across all pools by pricing each tessera at the current market value of the liquidity it represents.

Governance power reflects real economic commitment — how much capital you have at risk in productive pools, not which pool you happen to be in.

The dampening exponent transitions from fourth root to cube root at the first halving block. All positions recalculate under the new exponent, regardless of when they were opened. No two-tier governance class.

**Why these specific exponents:** The ratio of the largest LP to total protocol TVL changes dramatically over time — the exponent must match the capture risk of each era.

- **Era 0 (fourth root):** At genesis, a $100M LP in a $1M protocol is 100% of TVL. Without dampening, that single actor controls the entire governance surface. Fourth-root compression reduces the gap: a $100M position has 18× the governance weight of a $1K position (vs. 100,000× under linear weighting). Maximum compression when the protocol is most vulnerable. The whale still has more weight than a small LP — they just cannot steamroll every vote.
- **Era 1+ (cube root, permanent from year 4):** By year 4, TVL growth has naturally diluted individual power. The same $100M LP in a $1B protocol is 10%, not 100%. Cube root: a $100M position has 46× the governance weight of a $1K position — more responsive to capital differences than fourth root, reflecting lower capture risk in a larger ecosystem. The exponent relaxes at the first halving block and stays at cube root permanently — subsequent halvings affect emission rate only, not governance mechanics.

**Worked example:** At genesis, $1M total TVL. One LP deposits $100M (100× the rest). Under linear weighting, that LP holds 99% of governance power — functionally a dictatorship. Under fourth root: the $100M LP has power proportional to $(100M)^{1/4} \approx 100$, while the remaining $1M of LPs collectively has $(1M)^{1/4} \approx 31.6$. The whale holds ~76% — still dominant, but a coalition of smaller LPs can contest any proposal. By year 4, suppose $1B TVL and the same LP still has $100M (now 10%). Under cube root: $(100M)^{1/3} \approx 464$, while the remaining $900M has $(900M)^{1/3} \approx 965$. The whale holds ~32% — influential but far from controlling. Natural TVL growth did most of the work; the exponent relaxation reflects that.

The transition trigger is the halving block itself — immutable in the contract, no governance vote, no discretionary timing.

AuMT in pools that fail any eligibility criterion carries zero governance weight. Governance power flows exclusively from productive capital — the same capital that earns emissions and generates protocol fees.

**Governance power for non-emission decisions derives exclusively from active, qualified AuMT positions. AuMT in non-qualified pools carries zero weight. Voting power cannot be purchased on the open market.**

- **Voting power = dampened AuMT.** `(AuMT_value × time_in_pool)^(1/4)` — same formula as protocol governance. 14-day qualification, 6-month on-ramp, any withdrawal resets to zero. See [Glossary (section xxxv)](12_aureum_glossary.md) for the full rule set.

#### Minimum Qualification Period and Governance On-Ramp

**Days 0–14: Zero governance weight.** Voting power requires at least **14 days (one full governance cycle)** of continuous qualified AuMT holding. During this period, `time_in_pool = 0` — the position is invisible to governance.

**Days 14–180: Governance on-ramp.** After the 14-day qualification, `time_in_pool` accrues from zero. Because the formula uses `(qualified_AuMT_value × time_in_pool)^(1/4)`, voting power grows sublinearly with time. An LP at day 14 has minimal power. By month 6 (day 180), they reach **full voting weight**. The 6-month on-ramp ensures governance power reflects sustained commitment, not recent capital deployment.

**Any withdrawal resets everything to zero.** Remove any amount of liquidity from a qualified pool — even 1% — and governance power for that position drops to zero immediately. `time_in_pool` resets. The 14-day qualification clock restarts from scratch. The 6-month on-ramp begins again.

This eliminates:

- **Flash-LP attacks:** Borrow capital, deposit, vote, withdraw in the same block or day
- **Snapshot-based manipulation:** Accumulate AuMT moments before a governance snapshot, then exit
- **Cycle-boundary gaming:** Deposit at the end of a cycle to vote, remove at the start of the next
- **Ghost governance:** Withdraw most liquidity while retaining outsized governance weight from original position's time-weighting
- **Capital-rotation attacks:** Deposit large capital, vote immediately, then move capital elsewhere — the 6-month on-ramp means new capital has negligible governance power

#### Low-Turnout Safeguard

Every proposal type requires a minimum turnout of **20% of total qualified voting power**. Below 20%, the proposal is **automatically rejected** regardless of vote outcome. No timelock fallback — it fails and must be resubmitted.

Applies uniformly: gauge approvals, gauge challenges, fee changes, and composition challenges all share the same 20% floor. **All governance proposal deposits** are **one-sided into der Bodensee Pool** (same mechanic; see [Constitution §xxvii](10_constitution.md)). **Deposit amounts** are proposal-specific; gauge challenges apply only to **non-Miliarium** pools per [F-12](11_formulas.md) — **Miliarium Aureum pools cannot be gauge-challenged** (structural changes go through the Composition Challenge path). The deposit filters spam; the turnout floor prevents a small coordinated group from pushing through structural changes while the broader LP community is inactive.

#### Anti-Market Buying

Only active liquidity providers in **emission-qualified pools** have governance voting power. AuMT in pools that fail eligibility carries zero weight. You cannot buy governance power on the open market or earn it by parking capital in unproductive pools.

Fourth root (Era 0) then cube root (Era 1) dampens whale dominance — maximum compression when the protocol is smallest, relaxing as TVL growth naturally decentralizes power. Time-weighting rewards commitment without lock mechanisms.

#### Governance Scope

**What governance controls:**

- Fee parameters (swap fee %, yield fee %)
- Gauge approvals and challenges (with timelock)
- Miliarium Aureum composition challenges (2/3 supermajority)

**What governance cannot control:** Emission schedule, maximum supply, CCB engine parameters, governance dampening transition, eligibility criteria, fee distribution split, der Bodensee Pool parameters, and all launch mechanics. Immutable in contract. Full list: [Immutable Parameters (§xxix)](10_constitution.md).

### Token Properties

AuMM is **100% liquid**. No locking, no staking, no ve-mechanism, no wrapper. You hold it, you can sell it.

**AuMM carries zero governance power.** It does not vote on emissions, fee parameters, or any protocol decision. All governance — including emission direction — is AuMT-weighted (active LP positions in qualified pools). AuMM is a pure reward and value-capture token: earned by LPs, backed by protocol revenue.

AuMM accrues value through **der Bodensee Pool** — the protocol's autonomous reserve. **Protocol-captured** revenue (the **protocol share** of swap fees from **other** gauged pools — see §x — plus ERC-4626 yield fees) enters as **one-sided stablecoin (sUSDS/svZCHF) inflows**, continuously deepening the reserve side. **Swap fees on trades inside der Bodensee Pool** accrue to der Bodensee LPs in full (see §x). The pool holds **fixed weights — 40% AuMM / 30% sUSDS / 30% svZCHF, immutable from block 0**. AuMM supply in the pool is capped (only the decaying F-0 bootstrap adds AuMM, and that channel goes permanently to zero at the end of Month 10), while stablecoin reserves grow continuously from protocol fees. Weighted-pool math reprices AuMM higher as the stablecoin side grows relative to the AuMM side. No buyback. No burn. No market purchases. Value backed by real revenue.

## x. Value Capture

### Fee Routing

All **protocol-captured** fee revenue flows to a single destination: **der Bodensee Pool**. **LP residuals** on swap fees (the Vault LP leg on non–der Bodensee pools) are not protocol revenue — they stay with originating-pool LPs ([Constitution §xxix — Fee routing](10_constitution.md)).

| Stream | Destination | Share |
|--------|-------------|-------|
| **Protocol share** of swap fees on **non–der Bodensee gauged pools** ( **`protocolSwapFeePercentage = 50e16`** — **~50%** of the pool's charged swap fee) | der Bodensee Pool (one-sided svZCHF) via Balancer V3 hook on `onAfterSwap` | **100%** of that protocol share |
| **LP residual** of swap fees on **non–der Bodensee gauged pools** | LPs of the originating pool (Vault accounting) | **~50%** of the charged swap fee |
| ERC-4626 yield fee (10% skim) on **non–der Bodensee gauged pools** | der Bodensee Pool (one-sided svZCHF) | **100%** of the skim (separate from swap-fee split) |
| ERC-4626 yield on **der Bodensee's own holdings** (svZCHF + sUSDS) | Accrues in-pool via Rate Providers — no skim, no external routing | 100% in-pool |
| Swap fees on **trades inside der Bodensee Pool** | der Bodensee LPs (retained in pool) | **100%** of the in-pool tier (e.g. **0.75%** at genesis) |

**Non–der Bodensee pools:** the **OQ-11** bands (e.g. **0.01–0.30%** on Miliarium) set the **rate the pool charges**; the **50/50 protocol vs LP** split on that fee is a **Vault registration invariant**, not governable.

**der Bodensee Pool** uses a **0.75%** swap-fee tier at genesis. Every wei of that fee **stays in the pool** for der Bodensee LPs — it does **not** route through the protocol fee pipeline.

No treasury. All **protocol-captured** revenue flows to **der Bodensee Pool** as one-sided stablecoin inflows. Fee routing is contract-enforced and immutable.

### The Day-One Revenue Guarantee

ERC-4626 pools generate yield fee revenue regardless of trading volume — the protocol has revenue from the first block. Not dependent on routing, aggregator integration, or TVL growth. Architectural. Every dollar of yield-bearing tokens in any pool generates protocol revenue automatically. From block 0, **protocol-captured** fees (yield skim + **protocol share** of swap fees on other gauged pools) flow into der Bodensee Pool as one-sided stablecoin inflows; **swap fees on trades inside der Bodensee** stay **in pool** for der Bodensee LPs in full.

## x-a. der Bodensee Pool

**Miliarium** LP returns include **AuMM emissions**, **ERC-4626 native yield**, and **~50%** of swap fees charged on the pool (the Vault LP residual); the **other ~50%** is the protocol share the hook routes to der Bodensee. **Der Bodensee** LPs **additionally** earn the **full in-pool swap-fee tier** on the three-token pool (e.g. **0.75%** at genesis).

der Bodensee Pool is the protocol's self-regulating reserve and the AuMM trading venue — a **three-token weighted pool** with **fixed** composition. It replaces discretionary treasuries and manual price stabilization. *Der Bodensee — a lake that only gets deeper.*

### Composition (immutable from block 0)

| Parameter | Value |
|:----------|:------|
| Tokens | **AuMM / sUSDS / svZCHF** |
| Weights | **40% AuMM / 30% sUSDS / 30% svZCHF** (fixed, no time-decay) |
| Swap fee | **0.75%**, fully retained **in pool** for der Bodensee LPs |
| ERC-4626 yield share | **60% of pool TVL** (sUSDS + svZCHF) earns native vault yield |
| Emission eligibility | **None** — AuMM cannot sit in an emission-eligible pool (no self-referential tokens) |

There is no founder-set price, no governance-voted multiple, no TVL measurement window, no stabilization inventory, no buyback, and no burn. The ratio of AuMM to stablecoins in the pool **is** the price; weighted-pool math handles it organically from genesis.

### How AuMM enters the pool (decaying treasury emission)

| Period | Bootstrap share | Behavior |
|:-------|:----------------|:---------|
| Block 0 → end of Month 6 | 80% → 50% | Linear per block |
| End of Month 6 → end of Month 10 | 50% → 0% | Linear per block |
| After Month 10 | **0% (permanent)** | Immutable — der Bodensee never receives AuMM via emission again |

Bootstrap AuMM is minted **one-sided** into der Bodensee with no LP tokens issued. Formal definition: [F-0](11_formulas.md). After Month 10 the AuMM side of the pool is fixed forever — the only way more AuMM can enter is via swap-in by traders.

### How stablecoins enter the pool (continuous protocol revenue)

**100%** of the **protocol share** of swap fees on all non–der Bodensee gauged pools (**100%** of what **`protocolSwapFeePercentage`** assigns — **~50%** of charged swap fee volume) plus **100%** of the ERC-4626 yield fee (10% skim on yield-bearing tokens in **non–der Bodensee gauged pools**) enter der Bodensee as **one-sided stablecoin deposits** (routed as svZCHF per Constitution §xxix), deepening the reserve side every block. **LP residuals** on those swap fees remain with originating-pool LPs. Governance proposal deposits and Incendiary Boost deposits use the same one-sided path.

### Value capture (no buyback, no burn, no market purchases)

The pool **is** the value capture mechanism. AuMM inflows are decaying and stop permanently at Month 10. Stablecoin inflows are continuous and grow with protocol usage. AuMM becomes progressively scarcer relative to a deepening reserve, and weighted-pool math reprices it mechanically. No burn is required — the pool math does the work.

### How yield accrues to AuMM without leaving the pool

Der Bodensee holds svZCHF and sUSDS — both ERC-4626 yield-bearing tokens — directly. Each is configured at pool registration with a Balancer V3 **Rate Provider** that reports `convertToAssets(1e18)`: the underlying-asset-per-share ratio. As Frankencoin and Sky earn yield on their respective reserves, those Rate Providers report progressively higher rates over time. Balancer V3's weighted-pool math uses **rate-adjusted balances** to compute swap outcomes and spot prices — so the pool natively understands that one svZCHF token today is worth more than one svZCHF token was yesterday.

The consequence runs through four steps:

1. **Yield accrues silently.** As time passes with no swap activity, the svZCHF and sUSDS Rate Providers report higher rates. The pool's accounted balances (in rate-scaled terms) rise on the stablecoin sides without any token movement.
2. **Weighted-pool invariant adjusts.** The pool's 40% AuMM / 30% sUSDS / 30% svZCHF target is enforced on rate-scaled balances. As the stablecoin sides grow in value while the AuMM side stays fixed (no AuMM enters via emission after Month 10), the implied AuMM price rises mechanically — there are now more rate-scaled stablecoins backing the same AuMM supply.
3. **No yield leaves the pool.** No wei of AuMM, svZCHF, or sUSDS is transferred out. The yield is fully embedded in the rising rate of the 4626 tokens, captured 100% by Bodensee LPs through their pro-rata BPT share of the growing pool value, and reflected in AuMM's price through the weighted-pool math acting on rate-adjusted balances.
4. **No skim, no buyback, no burn.** AuMM scarcity is enforced by the F-0 bootstrap channel (decaying then permanently zero at Month 10). Stablecoin depth grows from two independent sources: the continuous one-sided fee inflows from other pools (**protocol share** of swap fees + 10% yield skim from non-Bodensee gauged pools), *and* the ongoing in-place yield on every stablecoin already sitting in der Bodensee. The pool feeds its own growth.

This mechanism is why the spec frames der Bodensee as *"a lake that only gets deeper"* and why no buyback / burn / market-purchase logic exists anywhere in the protocol. The pool math is the value-capture mechanism.

**One clarification on the protocol fee structure:** the "10% ERC-4626 yield fee" referenced in [Constitution §xxix](10_constitution.md) applies to ERC-4626 tokens held inside **other gauged pools** (the 28 Miliarium pools and any non-Miliarium gauged pool), **not** to der Bodensee's own ERC-4626 holdings. Skimming yield from Bodensee and depositing it back into Bodensee would be a no-op that burns gas. The skim mechanism extracts 10% of yield from every other gauged pool's ERC-4626 component, swaps it to svZCHF via the Aequilibrium routing layer, and one-sided-deposits into Bodensee — adding to the stablecoin depth that already compounds in-place.

### CCC alignment

der Bodensee Pool is a CCC reserve in the spirit of Dr. Luzius Meisser's thesis and Frankencoin: capital allocation is algorithmic, revenue flows are rule-based, and no separate treasury can receive, hold, or sell newly emitted tokens. Composition and revenue routing are immutable from block 0. Formal composition definition: [Protocol formulas — der Bodensee Pool composition (F-11)](11_formulas.md).

### The Self-Reinforcing Loop

**60%** of der Bodensee Pool TVL sits in ERC-4626 yield-bearing vaults (sUSDS + svZCHF). That yield compounds **in-place** via Rate Providers (not via the protocol's 10% skim, which applies to **other** gauged pools only — see "How yield accrues to AuMM without leaving the pool" above). Separately, **10%** of ERC-4626 yield from **non-Bodensee** gauged pools is skimmed and deposited one-sided into Bodensee as svZCHF. During **Months 1–10** der Bodensee also receives the decaying one-sided AuMM bootstrap; **after** Month 10 the AuMM channel is permanently zero, but stablecoin depth continues to grow from fee routing, skim inflows, and in-place vault compounding. Higher protocol TVL means more yield-fee revenue from Miliarium and other gauged pools, more stablecoin depth, more upward repricing of AuMM against the reserve.

### Reserve Depth Growth

At scale, combined **protocol-captured** revenue from the **protocol share** of **swap fees on other pools** (**100%** of that share to Bodensee) and **yield fees** (**100%** of the skim to Bodensee) flows into der Bodensee Pool as one-sided stablecoin inflows, continuously deepening the reserve side — **in addition to** **0.75%** swap fees retained **in pool** for der Bodensee LPs on **trades inside der Bodensee**.

**Worked example.** Assume **$100M protocol-wide TVL across the 28 Miliarium pools (excluding der Bodensee)** and $20M average daily volume at maturity. The pool charges **0.03%** (Miliarium genesis default); **~50%** of that fee is the **protocol share** routed to Bodensee (**100%** of the protocol leg), **~50%** the **LP residual** (not reserve inflow).

| Revenue source | Calculation | Annual stablecoin inflow |
|:---------------|:------------|:-------------------------|
| Swap fee revenue (protocol leg) | $20M/day × 0.03% × **50%** protocol share × **100%** to Bodensee × 365 days | ~$1,095,000/year |
| Yield fee revenue | $100M Miliarium TVL × ~60% ERC-4626 weight × 2.5% avg yield × 10% skim × 100% to Bodensee | ~$150,000/year |
| **Total annual reserve inflow** | | **~$1,245,000/year** in stablecoin depth |

*Note: revenue figures above use calendar-year conventions for illustration; contract computations use block-based time per [Constitution §xxix](10_constitution.md). The **yield fee** targets ERC-4626 holdings in **non-Bodensee** gauged pools only — der Bodensee's own 60% 4626 holdings compound in-place via Rate Providers (see "How yield accrues to AuMM without leaving the pool" above). The **50/50** split on swap fees is the Vault **`protocolSwapFeePercentage`** invariant — see [Constitution §xxix](10_constitution.md).*

As protocol TVL grows beyond $100M, both swap volume and yield fee revenue scale with it, accelerating reserve growth. The halving schedule reduces emission dilution every four years while revenue scales with TVL — the reserve grows faster than new supply enters the market.

*All governance proposal deposits — gauge approval, gauge challenge, fee proposals, composition challenge — are one-sided sUSDS/svZCHF inflows into der Bodensee Pool; Incendiary Boost deposits use the same reserve destination. Together they deepen the autonomous reserve.*

### Immutable Reference

See [Immutable Parameters (§xxix)](10_constitution.md).
