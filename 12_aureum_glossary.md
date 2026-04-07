# Aureum Protocol - Glossary

## xxxi. Core Tokens

- **AuMM** (Aureum Market Maker): reward token. 21,000,000 max supply, immutable halving schedule. Earned by LPs, backed by protocol revenue flowing into der Bodensee Pool. Zero governance power. Not a Miliarium Aureum pool slot — the 28 Miliarium pools are the ix-named registry in the [Miliarium Aureum registry](05_miliarium_aureum.md). Price discovery happens in **der Bodensee Pool** (AuMM/sUSDS/svZCHF three-token weighted pool, fixed 40/30/30); **Months 1–10** it also receives **piecewise-decaying bootstrap** AuMM (one-sided deposits, 80%→50% by Month 6, 50%→0% by Month 10); **after Month 10**, the bootstrap channel is permanently zero and emissions route only to LP pools + gauges. See [Tokenomics](04_tokenomics.md).
- **AuMT** (Aureum Market Tessera): LP participation token — your tessera. Proves an active liquidity position in a qualifying pool. Governance weight scales with USD value of the underlying position and time held. AuMT in non-qualifying pools carries zero weight.
- **Tessera**: Roman term for a small tablet used as a ticket, voucher, or proof of identity — the conceptual name for AuMT. In Rome, a tessera proved you belonged: entry, grain distribution, voting in assemblies. Here it proves your stake in protocol liquidity and carries the same rights — emissions and governance power.

- **ixEDEL**: routing anchor token held by 26 of the 28 Miliarium pools (typically at 16% weight). A **Reserve Protocol DTF** (Diversified Token Fund) — a basket token whose constituents are governed by the Reserve Protocol. **Mint and redeem at NAV** via the Reserve app: [Reserve — ixEDEL DTF overview](https://app.reserve.org/ethereum/index-dtf/0xe4a10951f962e6cb93cb843a4ef05d2f99db1f94/overview). Strategy and portfolio context (Club Edelweiss / risk-parity thesis): [Sagix — ixEDEL](https://www.sagix.io/ixedel/). Cross-pool trades route through ixEDEL on both legs, generating fees in both pools. Primary price discovery happens in **ixEdelweiss** (slot 05), which holds 46% ixEDEL. With **svZCHF**, it forms the **dual-anchor / universal-connector** design (horizontal routing vs reserve rail — see **Dual anchors** in [Mental model (§iii — Constellation routing)](02_mental_model.md)). See also [ixEdelweiss pool profile](miliarium_profiles/05_ixEdelweiss.md).

- **svZCHF** (Frankencoin savings): ERC-4626 CHF-anchored stable used in **der Bodensee Pool** (fixed-weight AuMM / sUSDS / svZCHF), **governance deposits**, **Incendiary Boost** one-sided deposits, and protocol fee consolidation — the second **universal connector** alongside **ixEDEL**: not primarily for cross-sector swaps, but for **anchoring value and boosts into the autonomous reserve** and Frankencoin stack. See [Tokenomics](04_tokenomics.md), the **der Bodensee Pool** entry below in this glossary, and [Mental model (§iii — Constellation routing)](02_mental_model.md).

## xxxii. Core Systems

- **Aequilibrium**: the AMM engine. Balancer V3's Certora-verified smart contracts — pool math, vault, SOR, and hooks byte-identical to the audited code. Only the tokenomics layer is new.

- **CCB** (Continuous Central Bank): fully automatic emission allocator — named after a central bank because it acts like one, without humans. A central bank tightens during booms and loosens during busts. The CCB does the same for LP yield: when TVL spikes, the EMA lags spot TVL, so relative yield compresses — the protocol does not overpay for speculative capital. When TVL crashes, the EMA preserves the memory of higher TVL, keeping absolute emission levels elevated — yield spikes for remaining LPs, a programmatic lender of last resort. No committee vote. No discretion. Algorithmic inertia enforced on-chain.

  **CCB multiplier (Miliarium pools only):** deterministic, oracle-free multiplier applied exclusively to the 28 Miliarium pools inside the CCB score. Every bi-weekly cycle, each pool's multiplier adjusts by a protocol-wide step (direction of total protocol TVL) and a pool-specific step (pool TVL relative to Miliarium average), then clamps to the immutable band. Pools growing too fast are taxed; pools shrinking are subsidized. Numeric bounds (step size, clamp range, dead zone): [Immutable Parameters (§xxix)](10_constitution.md). Narrative explanation: [Theoretical foundations (§vii)](03_theoretical_foundation.md); formal update rule: [Protocol formulas (F-8)](11_formulas.md).

  **Full emission sequence (every block):** EMA updates run continuously; **der Bodensee bootstrap** (Months 1–10 only; see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)) is applied first when active; Incendiary Boost claims are skimmed from the **LP emission tranche**; the remainder follows the active regime (equal 1/28, blend, or pure CCB). Each pool's total emission is its regime share plus any Incendiary claim. Oracle-free — reads only internal contract balances. 21M hard cap never breached: Incendiary is reallocation, not new inflation. Step-by-step formal sequence: [Protocol formulas](11_formulas.md).

- **EMA(60)**: 60-day exponential moving average of on-chain TVL — the CCB's anticyclical memory. A pool that loses all TVL today still retains a fading signal over weeks, preventing instant reallocation from a single day's movement. Full explanation: [Theoretical foundations (§vi-b)](03_theoretical_foundation.md). Formal definition: [Protocol formulas (F-4)](11_formulas.md). Horizon is immutable — [Constitution (§xxix)](10_constitution.md).

- **Anti-Gaming Engine**: umbrella term for all immutable eligibility and performance criteria governing emission qualification. Includes: ERC-4626 Quality Gate (≥52%), Minimum TVL ($10K 7-day SMA), Volume Percentile Floor (graduated from 5th to 15th by pool age), Efficiency Tournament (tiered emission caps for bottom 15%), no self-referential tokens, and protocol version requirement. All immutable from block 0 — governance cannot waive them. The CCB determines *how much*; the Anti-Gaming Engine determines *whether*. See [Bootstrap (section xxiii)](08_bootstrap.md).

- **Incendiary Boost**: user-funded priority emission stream. Anyone deposits any amount of svZCHF/sUSDS one-sided into der Bodensee Pool → target pool receives a **1-epoch (14-day)** supplementary AuMM stream starting at the next epoch boundary. Once per epoch per pool. Deposit amount at user discretion. Claims are subtracted from the **LP emission tranche** (after der Bodensee bootstrap skim in Months 1–10) *before* equal/CCB distribution — not a CCB score multiplier. See [Bootstrap](08_bootstrap.md).

- **Priority Skim**: the mechanism by which Incendiary Boost emissions are subtracted from the **LP emission tranche** *before* equal or CCB distribution. Total block emission never changes — Incendiary claims reduce the remainder available to all other pools, directly diluting their share. Boosting pools has a real cost borne by the entire emission economy, not free inflation.

- **der Bodensee Pool**: autonomous reserve, AuMM trading venue, and sole destination for **protocol-captured** revenue — a **three-token weighted pool** (AuMM / sUSDS / svZCHF) with **fixed weights 40% / 30% / 30%**, immutable from block 0 (no time-decay). **60%** of pool TVL (sUSDS + svZCHF) earns native ERC-4626 vault yield. **Protocol-captured** fee revenue (swap fees on **other** pools + ERC-4626 yield fees) flows one-sided into the stablecoin side as sUSDS/svZCHF — **all protocol fee revenue, no split**. **Swap fee inside der Bodensee:** **0.75%**, **100%** retained **in pool** for der Bodensee LPs. **Months 1–10:** also receives **piecewise-decaying one-sided AuMM bootstrap** (80%→50% by Month 6, 50%→0% by Month 10; see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)). **After Month 10:** bootstrap channel permanently zero. **Hidden from UI Months 0–6**, visible and tradeable from Month 6 onward. **Not emission-eligible** — no self-referential tokens. No buyback, no burn, no market purchases — the pool **is** the value-capture mechanism: AuMM is capped (decaying then zero), stablecoins grow continuously, and weighted-pool math reprices AuMM mechanically. *Der Bodensee — a lake that only gets deeper.* See [Tokenomics](04_tokenomics.md) and [Protocol formulas (F-11)](11_formulas.md).

- **Continuous Capital Corporation (CCC)**: Aureum's design philosophy, from Dr. Luzius Meisser's 2024 PhD thesis *Essays in Decentralized Finance* and Frankencoin's implementation. An autonomous, rule-based system that allocates capital and manages reserves via fixed on-chain rules — no discretionary management, no separate treasury. Aureum implements CCC through algorithmic emission allocation (CCB), autonomous reserve management (der Bodensee Pool), and immutable fee routing.

## xxxii-a. Pool Concepts

- **Gauge**: on-chain approval granting a pool emission eligibility. Without one, a pool operates in the Sandbox (zero emissions). Gauge approval is a governance vote — qualified AuMT holders decide whether a pool deserves to compete for emissions. Revocable via challenge.
- **Sandbox**: permissionless default state. Any pool can deploy without a gauge from block 0. Sandbox pools receive no CCB emissions and are not eligible for Incendiary Boost, but rank in the Efficiency Tournament. Open access without an emission exploit vector.
- **Fast-Track Rule**: a non-gauged Sandbox pool sustaining top 10% efficiency for **3 epochs (6 weeks)** earns automatic gauge approval. No governance vote required.
- **ERC-4626 Quality Gate**: primary eligibility criterion. ≥52% yield-bearing (ERC-4626) tokens by weight. Each ERC-4626 token must have ≥$5M, 30 BTC, or 4,000,000 svZCHF (whichever is largest) in its underlying vault `totalAssets()` to count toward the threshold. Ensures real protocol yield fees. Immutable.
- **Efficiency Tournament**: relative ranking of all gauged pools above $10K TVL by efficiency ratio: `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received`, 3-epoch (6-week) moving average. Tiered caps for the bottom 15%: above 15th = no cap; 10th–15th = 1% of total emissions; 5th–10th = 0.5%; below 5th = 0.1%. Excess from capped pools redistributed to uncapped pools pro-rata by CCB share. Activates at month 13. Price-agnostic. See [Bootstrap (section xxiii)](08_bootstrap.md).
- **Volume Percentile Floor**: pools must stay above the 15th volume percentile (trailing 3-epoch fee + yield revenue) to retain emissions. Catches dead pools. Graduated: 5th percentile at month 3, 10th at month 6, 15th at month 13.
- **Hysteresis Buffer**: prevents binary oscillation around the volume floor. Three zones: Safe (above 15th — normal emissions), Warning (10th–15th — emissions continue, 3-epoch recovery window), Cut (below 10th — emissions cease, redistributed to remaining eligible pools).
- **LP Bonus**: AuMM emission rewards distributed to LPs proportional to their pool's CCB-weighted share. **Trades inside der Bodensee** use a separate **0.75%** fee; those fees stay **in pool** for der Bodensee LPs. Swap fee revenue on non-Bodensee pools flows entirely to der Bodensee Pool as protocol-captured revenue.

## xxxiii. Launch Structure

- **Miliarium Aureum**: the 28 founding pools, locked at launch. No open slots. Named after the Golden Milestone in the Roman Forum from which all distances in the Empire were measured — the routing hub from which all protocol paths radiate.
- **Equal regime (through Month 10)**: the LP emission tranche (after der Bodensee bootstrap skim) split equally across the 28 Miliarium pools (1/28 of the tranche each).
- **Transition (Months 11–12)**: linear blend from equal to CCB (α from 0 to 1; halfway at α = 0.5).
- **Post–Year-1 automatic regime**: pure CCB — Incendiary claims skimmed first, remainder by TVL EMA × CCB multiplier; no voting.

## xxxiii-a. Eras

- **Era 0 (years 0–4, pre-halving)**: block emission 1.00 AuMM. Governance dampening: fourth root. Maximum compression when protocol TVL is lowest.
- **Era 1+ (year 4 onward, post-first-halving)**: block emission 0.50 AuMM in Era 1, halving each subsequent era. Governance dampening transitions permanently to cube root at the first halving block — later halvings affect emission rate only. TVL growth has naturally diluted individual power; the exponent relaxes accordingly.

## xxxiv. Controls (Immutable)

- no admin keys
- no multisig
- no upgradeability
- no pause function
- no voting over emissions
- no external oracle dependency for core operation

## xxxv. Governance

- **Governance actions (overview)**: four **non-emission** vote types — **Gauge Proposal** (new pool emission eligibility), **Gauge Challenge** (revoke a gauge), **fee proposals** (swap/yield parameters within immutable bounds), **Miliarium Aureum Composition Challenge** (2/3 supermajority, deprecate-and-replace in-slot). Every deposit is **one-sided into der Bodensee Pool** (svZCHF/sUSDS equivalent; amounts in [Constitution (§xxvii)](10_constitution.md)). Gauge and composition mechanics: [Bootstrap](08_bootstrap.md) §xxiv.
- **Tessera-Weighted Voting**: voting power derived exclusively from active LP positions — `(USD value of qualified AuMT × time_in_pool)^(1/4)` in Era 0, relaxing to `^(1/3)` in Era 1. No token purchase grants governance power — only productive liquidity held over time. Sub-linear dampening prevents whale capture.
- **Governance Power**: sub-linear function of LP position USD value × time held. Era 0: fourth-root (maximum compression); Era 1+: cube-root. Transition at the halving block; both exponents immutable. Formal expression: [Protocol formulas](11_formulas.md).
- **Qualification Period**: 14 days of continuous qualified AuMT holding before any governance weight accrues (`time_in_pool = 0` during this window).
- **Governance On-Ramp**: after the 14-day qualification, `time_in_pool` accrues sublinearly. Full voting weight reached at ~6 months (day 180).
- **Withdrawal Reset**: any withdrawal from a qualifying pool — any amount — resets governance power to zero and restarts the 14-day qualification clock.
- **Gauge Proposal**: submit gauge request with 100 svZCHF/sUSDS (deposited one-sided into der Bodensee Pool).
- **Gauge Challenge**: challenge/revoke an active **non-Miliarium** gauge; deposit is **one-sided into der Bodensee Pool** per [F-12](11_formulas.md) (see [Constitution §xxvii](10_constitution.md)). **Miliarium Aureum (28) cannot be gauge-challenged** — use Composition Challenge instead.
- **General Proposal** (fee parameters): 1,000 svZCHF/sUSDS (deposited one-sided into der Bodensee Pool).
- **Composition Challenge**: deprecate a Miliarium pool and launch a replacement into the same slot via standard bootstrap (for delistings/failures). Pool composition is immutable on-chain — no in-place token swap. **Deposit:** one-sided into der Bodensee Pool ([Constitution §xxvii](10_constitution.md)). Requires 2/3 protocol-wide tessera-weighted approval. Like-for-like renewal only (same sector, risk, template role). See [Bootstrap (§xxiv)](08_bootstrap.md).
- **On-Chain-Only Proposal Rule**: every proposal must cite verifiable on-chain state only — contract addresses, block ranges, deterministic metrics. Off-chain claims are invalid.
See [Immutable Parameters (§xxix)](10_constitution.md).
