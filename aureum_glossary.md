# Aureum Protocol - Glossary

## xxxi. Core Tokens

- **AuMM** (Aureum Market Maker): reward token with 21,000,000 max supply and immutable halving schedule. Earned by LPs, burned by the protocol. Carries zero governance power. Not a Miliarium Aureum pool slot — the 28 immutable pools are the ix-named registry in `Miliarium_Aureum.md`. Trading liquidity is **AuMM / svZCHF** and **AuMM / sUSDS**; that venue receives **no** emissions (emissions go to the 28 pools + gauges). See `tokenomics.md`.
- **AuMT** (Aureum Market Tessera): LP participation token — your tessera. Proves active liquidity position in a qualifying pool. Carries governance weight proportional to the USD value of the underlying LP position and time held. AuMT in non-qualifying pools carries zero weight.
- **Tessera**: Roman term for a small tablet used as a ticket, voucher, or token of identity — the conceptual name for AuMT. In Rome, a tessera proved you belonged and carried rights: entry, grain distribution, voting in assemblies. Your tessera proves your stake in the protocol's liquidity and carries the same rights — emissions, governance power, LP bonus eligibility.

## xxxii. Core Systems

- **Aequilibrium**: the AMM engine. Derived from Balancer V3's Certora-verified smart contracts. Pool math, vault, SOR, and hooks are byte-identical to the audited code. Only the tokenomics layer is new.

- **CCB** (Continuous Central Bank): the protocol's fully automatic emission allocator — named after a central bank because it does what a central bank does, without humans. A central bank tightens during booms (raises rates, reduces money supply growth) and loosens during busts (cuts rates, expands liquidity). The CCB does the same for LP yield: when TVL spikes in a bull market, the EMA lags spot TVL, so relative yield (%) compresses — the protocol does not overpay for speculative capital. When TVL crashes, the EMA preserves the memory of higher TVL, keeping absolute emission levels elevated — yield (%) spikes for remaining LPs, creating a programmatic lender of last resort. No committee vote. No discretion. Algorithmic inertia enforced on-chain.

  **Full emission sequence (every block, post-Year-1):**
  ```
  // EMA update (runs continuously for each pool)
  alpha = 2 / (60 + 1)                                           // ≈ 0.0328
  TVL_EMA(pool, today) = alpha × TVL_spot(pool, today)
                       + (1 - alpha) × TVL_EMA(pool, yesterday)

  // Emission distribution
  Step 1:  Incendiary_total = Σ active Incendiary Boost claims this block
  Step 2:  Remaining = block_emission - Incendiary_total
  Step 3:  Score(pool_i) = TVL_EMA60(pool_i) × PMAR_mult(pool_i)
  Step 4:  CCB_share(pool_i) = Remaining × Score(pool_i) / Σ Score(all pools)
  Step 5:  Total_emission(pool_i) = CCB_share(pool_i) + Incendiary_claim(pool_i)
  ```
  Oracle-free: reads only internal contract balances. 21M hard cap never breached — Incendiary is a reallocation from the same fixed pie, not new inflation.

- **EMA(60)**: 60-day exponential moving average of on-chain TVL. α = 2/(60+1) ≈ 0.033. Half-life ~21 days — a pool that loses all its TVL today still has 50% of its ghost signal after three weeks, 25% after six. This is the source of the CCB's anticyclical memory: the protocol cannot be jolted into instant reallocation by a single day's capital movement. It is a low-pass filter — suppresses short-term noise (hype, panic), passes long-term signal (sustained committed capital).

- **PMAR** (Miliarium Aureum Multiplier Adjustment Rule): the deterministic, oracle-free multiplier engine applied exclusively to the 28 Miliarium pools inside the CCB score. Replaces human governance voting over emission weights with an algorithmic rule. Every bi-weekly cycle, each Miliarium pool's multiplier updates as:

  ```
  M_i(t) = clamp( M_i(t-1) + delta_global + delta_intra_i,  0.75,  1.25 )
  ```

  Where:
  - `M_i(t-1)` = pool i's multiplier from the prior cycle, initialised at 1.00
  - `delta_global` = a protocol-wide step (±0.05) derived from the direction of total protocol TVL EMA — rising TVL applies downward pressure across all multipliers; falling TVL applies upward pressure
  - `delta_intra_i` = a pool-specific step (±0.05) derived from pool i's TVL EMA relative to the Miliarium average — pools growing faster than average are nudged down; pools shrinking relative to average are nudged up
  - `clamp [0.75, 1.25]` = hard floor and ceiling; multiplier can never leave this band
  - `dead zone 0.1%` = if the TVL ratio that triggers a step is within 0.1% of neutral, no step is applied — prevents oscillation noise from triggering constant micro-adjustments

  The result: pools that are growing too fast relative to the protocol are automatically taxed; pools that are shrinking are automatically subsidised. Anticyclical within the Miliarium set, without any human intervention. All parameters are immutable from block 0. See `PMAR.md`.

- **Incendiary Boost**: operator-funded priority emission stream. Operator escrows AuMM → pool receives a 30-day supplementary emission stream pegged to the 85th efficiency percentile × (2 − R). Incendiary claims are subtracted from block emission *before* CCB distribution — not a CCB score multiplier. Escrowed AuMM is permanently burned. See `bootstrap.md`.

- **Buyback-and-burn**: the protocol's value capture mechanism. Protocol revenue (25% of swap fees + 25% of ERC-4626 yield fees) is used to buy AuMM on the open market and permanently burn it. Circulating supply declines over time. No yield on holding — pure scarcity mechanics.

## Pool Concepts

- **Gauge**: an on-chain approval granting a pool emission eligibility. Without a gauge, a pool operates in the Sandbox (zero emissions). Gauge approval is a governance vote — qualified AuMT holders decide whether a pool deserves to compete for emissions. Gauges can be revoked via challenge.
- **Sandbox**: the permissionless default state. Any pool can be deployed without a gauge from block 0. Sandbox pools receive no CCB emissions and no Incendiary Boost, but are ranked in the Efficiency Tournament. Proves the protocol is open without creating an emission exploit vector.
- **Fast-Track Rule**: if a non-gauged Sandbox pool reaches top 10% efficiency in the Efficiency Tournament organically, it earns automatic gauge approval. No governance vote required.
- **ERC-4626 Quality Gate**: primary eligibility criterion. A pool must hold ≥52% yield-bearing (ERC-4626) tokens by weight. Each ERC-4626 token must have ≥$5M, 30 BTC, or 4,000,000 svZCHF (whichever is largest) in its underlying vault `totalAssets()` to count toward the 52% threshold. Ensures pools generate real protocol yield fees. Immutable.
- **Efficiency Tournament**: relative ranking of all gauged pools above $10K TVL by efficiency ratio: `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received`, using a 4-week moving average. Bottom 15% receive hard emission caps (0.1%–1% of total protocol emissions) regardless of PMAR or EMA weight. Activates at month 13. Price-agnostic by design.
- **Volume Percentile Floor**: pools must stay above the 15th volume percentile (trailing 4-week fee + yield revenue distribution) to retain emissions. Catches dead pools. Graduated during bootstrap phase: 5th percentile at month 3, 10th at month 6, 15th at month 13.
- **Hysteresis Buffer**: prevents binary oscillation around the volume floor. Three zones: Safe (above 15th, normal emissions), Warning (10th–15th, emissions continue, 2-cycle recovery window), Cut (below 10th, emissions cease immediately, routes to buyback-and-burn).
- **LP Bonus**: 50% of all swap fee revenue is distributed to LPs as an additional yield stream, proportional to their governance participation. Provides direct incentive to both provide liquidity and participate in governance.

## xxxiii. Launch Structure

- **Miliarium Aureum**: 28 immutable founding pools, locked at launch. No open slots. The routing hub from which all protocol paths radiate — named after the Golden Milestone in the Roman Forum from which all distances in the Empire were measured.
- **Equal regime (through Month 10)**: emissions split equally across the 28 pools (1/28).
- **Transition (Months 11–12)**: linear blend from equal to CCB (α from 0 to 1; halfway at α = 0.5).
- **Post–Year-1 automatic regime**: pure CCB — Incendiary claims skimmed first, remainder by TVL EMA × PMAR; no voting.

## Eras

- **Era 0 (years 0–4, pre-halving)**: block reward 1.00 AuMM. Governance dampening exponent: fourth root. Maximum compression protects against whale capture when protocol TVL is lowest.
- **Era 1 (years 4–8, post-first-halving)**: block reward 0.50 AuMM. Governance dampening exponent transitions to cube root at the halving block. TVL growth has naturally diluted individual power — the exponent relaxes accordingly.

## xxxiv. Controls (Immutable)

- no admin keys
- no multisig
- no upgradeability
- no pause function
- no voting over emissions
- no external oracle dependency for core operation

## xxxv. Governance

- **Governance Power**: `(qualified_AuMT_value × time_in_pool)^(1/4)` in Era 0, `^(1/3)` in Era 1+. Transition at halving block, immutable. `qualified_AuMT_value` is the USD value of the LP position — not token count.
- **Qualification Period**: 14 days of continuous qualified AuMT holding before any governance weight accrues (`time_in_pool = 0` during this window).
- **Governance On-Ramp**: after the 14-day qualification, `time_in_pool` accrues sublinearly. Full voting weight reached at ~6 months (day 180).
- **Withdrawal Reset**: any withdrawal from a qualifying pool — any amount — resets governance power to zero and restarts the 14-day qualification clock.
- **Gauge Proposal**: submit gauge request with 100 svZCHF/sUSDS equivalent in AuMM (burned).
- **Gauge Challenge**: challenge/revoke active gauge with 1,000 svZCHF/sUSDS equivalent in AuMM (burned).
- **General Proposal** (treasury/fee): 1,000 svZCHF/sUSDS equivalent in AuMM (burned).
- **Composition Challenge**: replace a Miliarium pool token (for delistings/failures). Requires 2/3 protocol-wide tessera-weighted approval. Like-for-like renewal only.
- **On-Chain-Only Proposal Rule**: every proposal must cite verifiable on-chain state only — contract addresses, block ranges, deterministic metrics. Off-chain claims are invalid.
- **Unqualified-Vote-to-Burn**: if CCB directs emissions toward a pool that fails eligibility criteria, those emissions are not distributed — they route to buyback-and-burn. Misdirected votes still benefit all remaining holders.

See Immutable Parameters in `constitution.md`.
