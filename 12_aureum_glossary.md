# Aureum Protocol - Glossary

## xxxi. Core Tokens

- **AuMM** (Aureum Market Maker): reward token with 21,000,000 max supply and immutable halving schedule. Earned by LPs, backed by protocol revenue flowing into der Bodensee Pool. Carries zero governance power. Not a Miliarium Aureum pool slot — the 28 Miliarium pools are the ix-named registry in the [Miliarium Aureum registry](05_miliarium_aureum.md). AuMM price discovery happens in **der Bodensee Pool** (AuMM + svZCHF LBP); **Months 1–10** it also receives **decaying bootstrap** AuMM (one-sided deposits); **after Month 10**, emissions route only to LP pools + gauges. See [Tokenomics](04_tokenomics.md).
- **AuMT** (Aureum Market Tessera): LP participation token — your tessera. Proves active liquidity position in a qualifying pool. Carries governance weight proportional to the USD value of the underlying LP position and time held. AuMT in non-qualifying pools carries zero weight.
- **Tessera**: Roman term for a small tablet used as a ticket, voucher, or token of identity — the conceptual name for AuMT. In Rome, a tessera proved you belonged and carried rights: entry, grain distribution, voting in assemblies. Your tessera proves your stake in the protocol's liquidity and carries the same rights — emissions, governance power, LP bonus eligibility.

- **ixEDEL**: the routing anchor token held by 26 of the 28 Miliarium pools (typically at 16% weight). ixEDEL is a **Reserve Protocol DTF** (Diversified Token Fund) — a basket token whose constituents are governed by the Reserve Protocol. **Mint and redeem at NAV** via the Reserve app: [Reserve — ixEDEL DTF overview](https://app.reserve.org/ethereum/index-dtf/0xe4a10951f962e6cb93cb843a4ef05d2f99db1f94/overview). Strategy and portfolio context (Club Edelweiss / risk-parity thesis): [Sagix — ixEDEL](https://www.sagix.io/ixedel/). It serves as the shared medium through which cross-pool trades route: when a trader swaps between any two ixEDEL-holding pools, the trade passes through ixEDEL on both legs, generating fees in both pools. Primary price discovery happens in **ixEdelweiss** (slot 05), which holds 46% ixEDEL. See [Mental model (§iii — Constellation routing)](02_mental_model.md) and [ixEdelweiss pool profile](miliarium_profiles/05_ixEdelweiss.md).

## xxxii. Core Systems

- **Aequilibrium**: the AMM engine. Derived from Balancer V3's Certora-verified smart contracts. Pool math, vault, SOR, and hooks are byte-identical to the audited code. Only the tokenomics layer is new.

- **CCB** (Continuous Central Bank): the protocol's fully automatic emission allocator — named after a central bank because it does what a central bank does, without humans. A central bank tightens during booms (raises rates, reduces money supply growth) and loosens during busts (cuts rates, expands liquidity). The CCB does the same for LP yield: when TVL spikes in a bull market, the EMA lags spot TVL, so relative yield (%) compresses — the protocol does not overpay for speculative capital. When TVL crashes, the EMA preserves the memory of higher TVL, keeping absolute emission levels elevated — yield (%) spikes for remaining LPs, creating a programmatic lender of last resort. No committee vote. No discretion. Algorithmic inertia enforced on-chain.

  **CCB multiplier (Miliarium pools only):** a deterministic, oracle-free multiplier applied exclusively to the 28 Miliarium pools inside the CCB score. Every bi-weekly cycle, each Miliarium pool's multiplier is adjusted by a protocol-wide step (direction of total protocol TVL) and a pool-specific step (pool TVL relative to the Miliarium average), then clamped to the immutable band. Pools growing too fast are automatically taxed; pools shrinking are automatically subsidized. For all numeric bounds (step size, clamp range, dead zone), see [Immutable Parameters (§xxix)](10_constitution.md). For the narrative explanation, see [Theoretical foundations (§vii)](03_theoretical_foundation.md); for the formal update rule, see [Protocol formulas (F-8)](11_formulas.md).

  **Full emission sequence (every block):** the EMA for each pool updates continuously; **der Bodensee bootstrap** (Months 1–10 only; see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)) is applied first when active; Incendiary Boost claims are skimmed from the **LP emission tranche**; the remainder follows the active regime (equal 1/28, blend, or pure CCB). Each pool's total emission is its regime share plus any Incendiary claim. Oracle-free — reads only internal contract balances. 21M hard cap never breached because Incendiary is a reallocation from the same fixed pie, not new inflation. See [Protocol formulas](11_formulas.md) for the step-by-step formal sequence.

- **EMA(60)**: 60-day exponential moving average of on-chain TVL — the CCB's anticyclical memory. A pool that loses all its TVL today still retains a fading signal over weeks, preventing instant reallocation from a single day's capital movement. For the full explanation of how the EMA works and why, see [Theoretical foundations (§vi-b)](03_theoretical_foundation.md). For the formal definition, see [Protocol formulas (F-4)](11_formulas.md). The EMA horizon is immutable — see [Constitution (§xxix)](10_constitution.md).

- **Anti-Gaming Engine**: the umbrella term for all immutable eligibility and performance criteria that determine whether a pool qualifies for emissions. Includes: ERC-4626 Quality Gate (≥52%), Minimum TVL ($10K 7-day SMA), Volume Percentile Floor (graduated from 5th to 15th by pool age), Efficiency Tournament (tiered emission caps for bottom 15%), no self-referential tokens, and protocol version requirement. All criteria are immutable from block 0 — governance cannot waive or relax them. The CCB determines *how much* each pool receives; the Anti-Gaming Engine determines *whether* a pool is eligible at all. See [Bootstrap (section xxiii)](08_bootstrap.md).

- **Incendiary Boost**: operator-funded priority emission stream. Operator escrows svZCHF/sUSDS into der Bodensee Pool (one-sided inflow) → pool receives a 30-day supplementary AuMM emission stream pegged to the 85th efficiency percentile × (2 − R). Incendiary claims are subtracted from the **LP emission tranche** (after der Bodensee bootstrap skim in Months 1–10) *before* equal/CCB distribution — not a CCB score multiplier. See [Bootstrap](08_bootstrap.md).

- **Priority Skim**: the mechanism by which Incendiary Boost emissions are subtracted from the **LP emission tranche** *before* equal or CCB distribution. The total block emission never changes — Incendiary claims reduce the remainder available to all other pools, directly diluting their share. This ensures bootstrapping new pools has a real cost borne by the entire emission economy, not free inflation.

- **der Bodensee Pool (LBP)**: the protocol's autonomous reserve and sole destination for **protocol-captured** revenue — a two-token Liquidity Bootstrapping Pool (AuMM + svZCHF) with linear time-decay weights over 18 months. **Genesis seed:** 1 AuMM and 1 svZCHF at pool creation. Genesis weights: 90% AuMM / 10% svZCHF. End weights: 48% AuMM / 52% svZCHF (fixed permanently after 18 months). **Protocol-captured** fee revenue (50% of swap fees on **other** pools + 100% of ERC-4626 yield fees) flows one-sided into the svZCHF side. **Swap fee on trades inside der Bodensee:** **0.75%**, **100%** retained **in pool** for der Bodensee LPs. **Months 1–10:** also receives **decaying one-sided AuMM bootstrap** (see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)). **After Month 10:** no further AuMM via emission. Acts as the self-regulating reserve in the CCC design — price discovery is forced by time-decay and real revenue inflows, not by manual intervention. See [Tokenomics](04_tokenomics.md) and [Protocol formulas (F-11)](11_formulas.md).

- **Continuous Capital Corporation (CCC)**: Aureum's design philosophy, drawn from Meisser's 2024 PhD thesis *Essays in Decentralized Finance* and Frankencoin's implementation. An autonomous, rule-based system that allocates capital and manages reserves according to fixed on-chain rules without discretionary management or a separate treasury. Aureum implements CCC through algorithmic emission allocation (CCB), autonomous reserve management (der Bodensee Pool), and immutable fee routing.

## Pool Concepts

- **Gauge**: an on-chain approval granting a pool emission eligibility. Without a gauge, a pool operates in the Sandbox (zero emissions). Gauge approval is a governance vote — qualified AuMT holders decide whether a pool deserves to compete for emissions. Gauges can be revoked via challenge.
- **Sandbox**: the permissionless default state. Any pool can be deployed without a gauge from block 0. Sandbox pools receive no CCB emissions and no Incendiary Boost, but are ranked in the Efficiency Tournament. Proves the protocol is open without creating an emission exploit vector.
- **Fast-Track Rule**: if a non-gauged Sandbox pool sustains top 10% efficiency in the Efficiency Tournament for **3 epochs (6 weeks)** without leaving the top 10%, it earns automatic gauge approval. No governance vote required.
- **ERC-4626 Quality Gate**: primary eligibility criterion. A pool must hold ≥52% yield-bearing (ERC-4626) tokens by weight. Each ERC-4626 token must have ≥$5M, 30 BTC, or 4,000,000 svZCHF (whichever is largest) in its underlying vault `totalAssets()` to count toward the 52% threshold. Ensures pools generate real protocol yield fees. Immutable.
- **Efficiency Tournament**: relative ranking of all gauged pools above $10K TVL by efficiency ratio: `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received`, using a 3-epoch (6-week) moving average. Tiered caps for the bottom 15%: above 15th = no cap; 10th–15th = 1% of total emissions; 5th–10th = 0.5%; below 5th = 0.1%. Excess emissions from capped pools are redistributed to uncapped pools pro-rata by CCB share. Activates at month 13. Price-agnostic by design. See [Bootstrap (section xxiii)](08_bootstrap.md).
- **Volume Percentile Floor**: pools must stay above the 15th volume percentile (trailing 3-epoch (6-week) fee + yield revenue distribution) to retain emissions. Catches dead pools. Graduated during bootstrap phase: 5th percentile at month 3, 10th at month 6, 15th at month 13.
- **Hysteresis Buffer**: prevents binary oscillation around the volume floor. Three zones: Safe (above 15th, normal emissions), Warning (10th–15th, emissions continue, 3-epoch (6-week) recovery window), Cut (below 10th, emissions cease immediately, redistributed to remaining eligible pools).
- **LP Bonus**: 50% of swap fee revenue on **non–der Bodensee pools** is distributed to LPs on those pools as an additional yield stream, proportional to their share of pool liquidity. **Trades inside der Bodensee Pool** use a separate **0.75%** fee tier; those fees stay **in pool** for der Bodensee LPs. Provides direct incentive to provide and maintain liquidity.

## xxxiii. Launch Structure

- **Miliarium Aureum**: the 28 founding pools, locked at launch. No open slots. The routing hub from which all protocol paths radiate — named after the Golden Milestone in the Roman Forum from which all distances in the Empire were measured.
- **Equal regime (through Month 10)**: the LP emission tranche (after der Bodensee bootstrap skim) split equally across the 28 Miliarium pools (1/28 of the tranche each).
- **Transition (Months 11–12)**: linear blend from equal to CCB (α from 0 to 1; halfway at α = 0.5).
- **Post–Year-1 automatic regime**: pure CCB — Incendiary claims skimmed first, remainder by TVL EMA × CCB multiplier; no voting.

## Eras

- **Era 0 (years 0–4, pre-halving)**: block emission rate 1.00 AuMM. Governance dampening exponent: fourth root. Maximum compression protects against whale capture when protocol TVL is lowest.
- **Era 1+ (year 4 onward, post-first-halving)**: block emission rate 0.50 AuMM in Era 1, continuing to halve each era. Governance dampening exponent transitions permanently to cube root at the first halving block — subsequent halvings affect the block emission rate only, not governance mechanics. TVL growth has naturally diluted individual power — the exponent relaxes accordingly.

## xxxiv. Controls (Immutable)

- no admin keys
- no multisig
- no upgradeability
- no pause function
- no voting over emissions
- no external oracle dependency for core operation

## xxxv. Governance

- **Governance actions (overview)**: The four **non-emission** vote types — **Gauge Proposal** (new pool emission eligibility), **Gauge Challenge** (revoke a gauge), **fee proposals** (swap/yield parameters within immutable bounds), **Miliarium Aureum Composition Challenge** (2/3 supermajority, deprecate-and-replace in-slot). Canonical list and quorum/deposit matrix: [Constitution (§xxvii)](10_constitution.md). Gauge and composition mechanics: [Bootstrap](08_bootstrap.md) §xxiv.
- **Tessera-Weighted Voting**: the governance voting mechanism. Voting power is derived exclusively from active LP positions — `(USD value of qualified AuMT × time_in_pool)^(1/4)` in Era 0, relaxing to `^(1/3)` in Era 1. No token purchases grant governance power; only productive liquidity held over time. Sub-linear dampening prevents whale capture.
- **Governance Power**: a sub-linear function of the USD value of the LP position multiplied by time held in pool. Era 0 uses fourth-root dampening (maximum compression); Era 1 onward relaxes to cube-root. Transition occurs at the halving block; both exponents are immutable. See [Protocol formulas](11_formulas.md) for the formal expression.
- **Qualification Period**: 14 days of continuous qualified AuMT holding before any governance weight accrues (`time_in_pool = 0` during this window).
- **Governance On-Ramp**: after the 14-day qualification, `time_in_pool` accrues sublinearly. Full voting weight reached at ~6 months (day 180).
- **Withdrawal Reset**: any withdrawal from a qualifying pool — any amount — resets governance power to zero and restarts the 14-day qualification clock.
- **Gauge Proposal**: submit gauge request with 100 svZCHF/sUSDS (deposited one-sided into der Bodensee Pool).
- **Gauge Challenge**: challenge/revoke an active gauge. **Non-Miliarium** gauged pools: scaled deposit per [F-12](11_formulas.md). **Miliarium Aureum (28):** fixed **1,000** svZCHF/sUSDS — **F-12 does not apply**.
- **General Proposal** (fee parameters): 1,000 svZCHF/sUSDS (deposited one-sided into der Bodensee Pool).
- **Composition Challenge**: deprecate a Miliarium pool and launch a replacement into the same slot via the standard bootstrap path (for delistings/failures). Pool composition is immutable on-chain — no in-place token swap. Requires 2/3 protocol-wide tessera-weighted approval. Like-for-like renewal only (same sector, risk, template role). See [Bootstrap (§xxiv)](08_bootstrap.md).
- **On-Chain-Only Proposal Rule**: every proposal must cite verifiable on-chain state only — contract addresses, block ranges, deterministic metrics. Off-chain claims are invalid.
See [Immutable Parameters (§xxix)](10_constitution.md).
