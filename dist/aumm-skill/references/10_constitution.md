<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 10_constitution.md — DO NOT EDIT -->
# Constitution

*The immutable operating law of Aureum.*

---

## xxvii. Protocol Control Model

### AUREUM Governance Actions (aumm.fi)

- **Gauge Proposal** — new pool **emission eligibility** (gauge approval); deposit **one-sided into der Bodensee Pool**. Details: [Bootstrap](08_bootstrap.md) §xxiv (Gauge Proposal).
- **Gauge Challenge** — **revoke** an existing **non-Miliarium** gauge; deposit **one-sided into der Bodensee Pool** per [F-12](11_formulas.md). **Miliarium Aureum (28) cannot be gauge-challenged** — use Composition Challenge instead. Details: [Bootstrap](08_bootstrap.md) §xxiv (Gauge Challenge).
- **Fee proposals** — **swap / yield fee** changes **within immutable bounds**; deposit **one-sided into der Bodensee Pool**. Voting model: [Tokenomics](04_tokenomics.md) §ix (Governance); mechanics: [Bootstrap](08_bootstrap.md) §xxiv (Governance Proposals).
- **Miliarium Aureum Composition Challenge** — **2/3 supermajority** tessera-weighted vote to deprecate a pool and **replace** assets in-slot (like-for-like); deposit **one-sided into der Bodensee Pool**. Details: [Bootstrap](08_bootstrap.md) §xxiv (Miliarium Aureum Composition Challenge) and **### Composition Challenge Rule** below.

**All governance proposal deposits** follow the **same treatment:** **one-sided inflow into der Bodensee Pool** in **svZCHF or sUSDS equivalent (whichever is higher)**, non-refundable, **no LP tokens** minted to the proposer; only **amounts** differ (see table below). No treasury wallet. No alternate routing.

Aureum is immutable and non-custodial from block 0:

- no admin keys
- no multisig
- no upgradeability
- no pause function
- no voting over emissions
- no off-chain dependencies for core operation

All core contracts immutable from block 0. Governance exists for non-emission actions only.

### Governance Scope (Non-Emission Only)

Qualified AuMT holders submit and vote on the **four actions** above. Governance cannot alter emission formulas, halving math, CCB multiplier constants, or other immutable parameters.

### Quorum and Deposit Requirements

| Decision Type | Minimum Turnout | Deposit (svZCHF/sUSDS, to der Bodensee Pool) | Approval Threshold | Failure Mode |
|--------------|-----------------|------------------------|--------------------|-------------|
| Gauge approval | 20% of total qualified voting power | 100 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Gauge challenge (revocation) — non-Miliarium gauged pools only | 20% of total qualified voting power | Per [F-12](11_formulas.md): **max(10 BTC CHF equiv., 1,000,000 CHF × √((1−p_tvl)(1−p_eff)))** in svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Fee parameter changes | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Composition challenge | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | 2/3 supermajority | Auto-fail if turnout < 20% or < 2/3 approval |

All deposits **one-sided into der Bodensee Pool** (no LP tokens minted to proposer), denominated in **svZCHF or sUSDS equivalent, whichever is higher at submission** — preventing gaming via currency fluctuation. Non-refundable. **Gauge challenges apply only to non-Miliarium gauged pools** — the 28 Miliarium Aureum pools cannot be gauge-challenged; structural changes go through the **Composition Challenge** path.

**Low-Turnout Safeguard.** Minimum turnout: **20% of total qualified voting power**. Below 20%, the proposal is **automatically rejected** — no timelock, no fallback. Uniform across all proposal types ([Tokenomics](04_tokenomics.md) Low-Turnout Safeguard).

### Composition Challenge Rule (Miliarium Aureum)

Governance-gated, **2/3 supermajority** of protocol-wide tessera-weighted votes. A single proposal may cover both theme assets if both have failed.

Pool composition is immutable on-chain. A composition challenge **deprecates** the old pool (gauge revoked, emissions cease) and **launches a replacement** into the same slot via the standard bootstrap path (90-day boost, optional Incendiary Boost).

**Four operational rules (OQ-7 resolution):**

1. **Deprecation = gauge revoked only.** The old pool persists on-chain as a Sandbox-style pool. It still exists, still accepts swaps, still earns ERC-4626 native yield for its LPs. It loses: AuMM emissions, CCB multiplier, and Miliarium Registry slot status.
2. **The fee-routing hook stays attached for life.** The deprecated pool keeps routing **100% of the Vault-assigned protocol share** of each swap fee to der Bodensee Pool via the still-attached hook (see **Fee routing** below — **~50%** of the charged swap fee; the **~50% LP residual** stays with originating-pool LPs). The protocol benefits from any residual trading activity on the deprecated pool; the LPs just don't earn AuMM for keeping it open. Once a pool is hooked at gauge approval, it remains a fee source for the life of the pool.
3. **Specified-pool model.** The composition challenge proposal must reference the **address of an already-deployed candidate pool** with the proposed composition. The 2/3 supermajority vote is binary on that specific pool. On approval, the Miliarium Registry updates the slot pointer, the replacement is automatically gauge-eligible (the supermajority vote supplies stronger consent than standard gauge approval), and the 90-day gauge boost applies as usual. No separate follow-up gauge proposal is needed.
4. **No LP migration assistance.** Old-pool LPs hold their existing AuMT, can withdraw at will, and may choose to enter the new pool independently. No special migration mechanic — a token failure in one pool would have everyone withdrawing anyway. The market handles migration for free.

**AuMT governance weight follows the gauge.** The moment a pool's gauge is revoked — whether by composition challenge, gauge challenge, 4-consecutive-disqualified-epoch automatic revocation, or any other path — the AuMT for that pool drops to **zero governance weight** at that block. The LP's other entitlements continue: pool-share-of-tokens, ERC-4626 native yield, and the **LP residual** of swap fees on that pool (**~50%** of the charged fee — Vault accounting; the hook still routes the **protocol share** to der Bodensee). Only governance power is lost.

**Like-for-like** means:

- **Same sector** — the replacement must belong to the same asset class or market sector as the token it replaces
- **Same risk profile** — materially similar economic properties (volatility, yield type, credit exposure)
- **Same template role** — the replacement must fill the same structural role in the pool (yield core, routing anchor, or theme asset)

Like-for-like is enforced two ways: programmatic checks at the registry level for properties the contract can verify (token-type composition, weight bounds, 4626 Quality Gate compliance), and semantic checks via the governance review itself (sector-fit, risk-equivalence, template-role-fit).

Activates only when an asset **ceases to function** (delisting, wrapper sunset, issuer failure). Renewal, not redesign. Worked examples in [Bootstrap (§xxiv)](08_bootstrap.md).

### Proposal Data Integrity Rule

All proposals must reference verifiable on-chain state only — contract addresses, block ranges, and deterministic on-chain metrics. Off-chain-only claims, unverifiable dashboards, social polling, or discretionary narratives are invalid.

## xxviii. Emission Operating Rules

*Narrative treatment: [Theoretical foundations](03_theoretical_foundation.md) (§§vi–vii; EMA §vi-b).*

Protocol **months** (Month 1 … Month 12) are defined on-chain as fixed block ranges from genesis; **Year 1** is Months 1–12 inclusive.

### Equal regime (through end of Month 10)

- Each block’s emission splits between **der Bodensee bootstrap** and the **LP tranche**. Bootstrap is **piecewise linear**: **80% at genesis → 50% at end of Month 6**, then **50% → 0% by end of Month 10**; minted as **one-sided AuMM** into der Bodensee Pool (no LP tokens). See [Protocol formulas (F-0)](11_formulas.md).
- Through the final block of Month 10, the **LP tranche** is split **equally** — **1/28** each (not 1/28 of the full block emission while bootstrap is positive). **100%** to LPs — no treasury wallet.

### Transition regime (Months 11–12)

**Months 11–12** linearly blend **equal 1/28** with the **CCB** share. Blend parameter: zero (pure equal) at the first block of Month 11 → one (pure CCB) at the last block of Year 1. At midpoint, exactly half and half. The CCB leg uses the same score as post–Year-1 (smoothed TVL × CCB multiplier). Formal blend formula in [Protocol formulas](11_formulas.md). (Bootstrap is zero from Month 11; LP tranche = full block emission.)

### Full CCB (from Year 1 end onward)

Incendiary Boost claims (1 epoch / 14 days each, any deposit amount, once per epoch per pool) are skimmed from the **LP emission tranche** (after bootstrap skim; post–Month 10 the tranche is the full block emission) **before** the CCB splits the remainder. Each pool carries a 60-day EMA of on-chain TVL ([Theoretical foundations §vi-b](03_theoretical_foundation.md)). The CCB scores each eligible pool by combining smoothed TVL with its CCB multiplier (Miliarium pools only; others use a neutral value), then normalizes to produce fractional shares. Multipliers update bi-weekly for the 28 only, within the immutable band in §xxix below. No voting, no human override. Formal definitions in [Protocol formulas](11_formulas.md).

## xxix. Immutable Parameters (Canonical Source)

**Single canonical source** for all immutable protocol parameters. Other documents should cite this section rather than restating values.

Three classes: **economic constants** (supply cap, halving schedule, fee splits) guaranteeing scarcity and revenue flow; **anti-gaming safeguards** (CCB multiplier bounds, EMA horizon, eligibility criteria) preventing reflexive manipulation; **anti-capture mechanics** (governance dampening exponents, withdrawal reset, qualification periods) ensuring no single actor dominates regardless of capital size.

Immutable from block 0, cannot be changed by any means.

**Canonical principle:** block numbers are the canonical time unit everywhere in the protocol. Calendar-time terms (month, year, week, day, epoch, "90 days," "14 days," "60-day EMA") are **aliases** for block counts. The contracts only ever deal with block numbers; calendar-time readings in documentation are approximations for human comprehension.

### Supply and emission

- Maximum AuMM supply: 21,000,000
- Emission halving schedule and block emission rates

### Canonical time constants (12-second blocks)

| Constant | Value (blocks) | Calendar alias | Used in |
|:---------|:---------------|:---------------|:--------|
| `BLOCKS_PER_DAY` | 7,200 | 1 day | EMA daily sampling (F-4), per-day rates |
| `BLOCKS_PER_WEEK` | 50,400 | 7 days | General reference |
| `BLOCKS_PER_EPOCH` | 100,800 | 14 days ("bi-weekly") | Incendiary Boost duration (F-2), CCB multiplier cadence (F-8), efficiency tournament smoothing unit, fee-change cooldown |
| `BLOCKS_PER_MONTH` | 219,000 | ~30.4 days | F-0 piecewise boundaries, Month 10 bootstrap termination, Month 11–12 transition, Month 13 efficiency-tournament activation |
| `BLOCKS_PER_QUARTER` | 657,000 | ~91.25 days | General reference |
| `BLOCKS_PER_YEAR` | 2,628,000 | 365 days (exact) | Year 1 / transition-complete boundary, era-quarter boundary, F-9 governance dampening era boundaries |
| `BLOCKS_PER_ERA` | 10,512,000 | 1,460 days (4 × 365) | Halving interval; F-9 governance dampening transition (Era 0 → Era 1+) |

### Derived time boundaries

| Constant | Formula | Used in |
|:---------|:--------|:--------|
| `MONTH_6_END_BLOCK` | `genesis + 6 × BLOCKS_PER_MONTH` | F-0 first piecewise boundary (80%→50%) |
| `MONTH_10_END_BLOCK` | `genesis + 10 × BLOCKS_PER_MONTH` | F-0 second piecewise boundary (bootstrap permanently zero) |
| `YEAR_1_END_BLOCK` | `genesis + BLOCKS_PER_YEAR` | F-3 transition endpoint (α = 1) |
| `MONTH_13_START_BLOCK` | `genesis + 12 × BLOCKS_PER_MONTH + 1` | Efficiency tournament activation |
| `FIRST_HALVING_BLOCK` | `genesis + BLOCKS_PER_ERA` | Era 0 → Era 1 transition; F-9 governance dampening exponent shift |
| `GAUGE_BOOST_DURATION_BLOCKS` | 648,000 | 90-day gauge boost (literal 90 × `BLOCKS_PER_DAY`) |
| `INCENDIARY_BOOST_DURATION_BLOCKS` | 100,800 | = `BLOCKS_PER_EPOCH` |

### EMA parameters

- `EMA_HORIZON_DAYS = 60` (informational; the actual constant is alpha)
- `EMA_ALPHA_NUMERATOR = 2`, `EMA_ALPHA_DENOMINATOR = 61` (so `alpha = 2/61 ≈ 0.0328`)
- `TWAP_WINDOW_BLOCKS = 720` (1 hour — intra-day TWAP used to sample TVL at each daily EMA update, prevents block-timing manipulation)
- Sampling cadence: once per `BLOCKS_PER_DAY`; each sample is the 720-block TWAP ending at the sample boundary. See [F-4](11_formulas.md).

### Fee routing

**Non–der Bodensee gauged pools — swap fees (Balancer V3 hook).** Each such pool registers with **`protocolSwapFeePercentage = 50e16`** (50% — saturating the Vault's **`MAX_PROTOCOL_SWAP_FEE_PERCENTAGE`**). That registration is **immutable** — no governance path changes the **protocol vs LP** split on swap fees. **OQ-11** governs only the **per-pool swap-fee rate** within the bands below. On every swap, **~50%** of the charged swap fee is the **LP residual** (stays with originating-pool LPs via Vault accounting); **~50%** is the **protocol share**. The `IHooks` contract on `onAfterSwap` settles **100% of that protocol share** to der Bodensee (swap-to-svZCHF + one-sided add — OQ-2). This is **not** "100% of gross swap fee volume" — it is **100% of the protocol-extractable leg** (capped at half the total fee).

- **Protocol share** of swap fees on **non–der Bodensee gauged pools**: **100%** of that share routed to der Bodensee Pool as one-sided svZCHF deposits. Implemented as a Balancer V3 hook on `onAfterSwap`, atomic per swap.
- **LP residual** of swap fees on **non–der Bodensee gauged pools**: **~50%** of the charged swap fee — retained for LPs of the originating pool (Vault invariant; not an Aureum allocation choice).
- ERC-4626 yield fee (10% skim) on **non–der Bodensee gauged pools**: **100%** of the skim routed to der Bodensee Pool as one-sided svZCHF deposits (separate from the swap-fee split). **Der Bodensee is excluded from yield-fee collection** — its own ERC-4626 holdings (60% of pool TVL, svZCHF + sUSDS) compound in-pool via Rate Providers, and skimming Bodensee's own yield would be a circular no-op. The skim mechanism extracts yield from *other* pools and deposits it into Bodensee.
- Swap fees on **der Bodensee**: **100%** retained in-pool for der Bodensee LPs (full **0.75%** tier on the three-token pool at genesis). Not routed through the protocol fee pipeline.

### Swap fee bands (rate governable within band, destination immutable)

| Pool class | Band (min–max) | Genesis default | Notes |
|:-----------|:---------------|:----------------|:------|
| Miliarium Aureum (the 28) | **0.01% – 0.30%** | **0.03%** | Hardcoded at deployment; adjustable via governance vote within band |
| Non-Miliarium gauged | **0.01% – 0.30%** | Set by gauge-approval vote | Initial fee set by the same vote that approves the gauge |
| Der Bodensee | **0.10% – 1.00%** | **0.75%** | Hardcoded at deployment; adjustable via governance vote within band |

- `FEE_CHANGE_COOLDOWN_BLOCKS = BLOCKS_PER_EPOCH = 100,800` — any pool can have its swap fee changed at most once per epoch (prevents rapid-fire manipulation; aligns with bi-weekly CCB cadence).

### der Bodensee Pool parameters

- Fixed weights **40% AuMM / 30% sUSDS / 30% svZCHF** — immutable from block 0, no time-decay.
- **Three-token weighted pool**, AuMM/sUSDS/svZCHF only.
- Months 1–10 one-sided AuMM bootstrap per [F-0](11_formulas.md) (piecewise linear: 80% at genesis → 50% at `MONTH_6_END_BLOCK` → 0% at `MONTH_10_END_BLOCK`). After `MONTH_10_END_BLOCK`, bootstrap channel is permanently zero.
- **Not emission-eligible** (AuMM cannot be in emission-eligible pools — no self-referential tokens).
- **Rate Providers** configured on svZCHF and sUSDS at registration — the pool natively accrues their underlying yield in-place via weighted-pool math acting on rate-scaled balances.

### Gauge-challenge deposit (F-12 support)

- `BTC_WRAPPERS` — registered set of wrapped-BTC tokens used for the BTC/CHF reference price (initial set: WBTC, cbBTC). Governance-extensible via standard proposal when new wrappers enter the ecosystem.
- `FALLBACK_DEPOSIT_FLOOR` — the F-12 10-BTC-equivalent calculation uses spot prices averaged across all gauged pools holding any `BTC_WRAPPERS` token; the F-12 max-of-two-formulas rule ensures the deposit stays meaningful under any BTC price regime.

### CCB multiplier rules (Miliarium pools only)

- Step size: ±0.05
- Clamp: [0.75, 1.25]
- Dead zone: 0.1%
- EMA horizon: 60 days (per `BLOCKS_PER_DAY` sampling with 720-block TWAP per sample)

### Registry and math

- List of 28 Miliarium Aureum pools: locked at launch by slot (see [Miliarium Aureum registry](05_miliarium_aureum.md)). **Slot is permanent; the pool at a slot may change via composition challenge per §xxvii.**
- Core AMM mathematics, CCB formula, and eligibility criteria

### Governance

- Governance dampening exponents: fourth root (Era 0, years 0–4), cube root (Era 1+, from `FIRST_HALVING_BLOCK` onward) — transition is permanent and occurs once
- Any withdrawal resets AuMT governance power
- AuMT governance weight requires active gauged-pool status — when a pool's gauge is revoked, the AuMT for that pool drops to zero governance weight at that block (other LP entitlements continue — see §xxvii Composition Challenge Rule)
- No admin keys, no multisig, no upgradability, no pause functions — *except:* at the one-time Stage B→governance migration, the Stage B multisig retains an emergency-only role for `BLOCKS_PER_YEAR` blocks (~12 months) post-migration, after which the multisig clause dies permanently. The multisig has no authority thereafter, ever.

## xxx. No Treasury

No treasury. No entity or wallet receives AuMM for discretionary use. No mechanism holds discretionary funds or disburses capital by vote. **der Bodensee Pool** receives **Months 1–10** bootstrap AuMM as **one-sided pool deposits** (not extractable, no LP tokens minted) on the piecewise decay schedule of [F-0](11_formulas.md); after the final block of Month 10, the bootstrap channel is **permanently zero**. **Protocol-captured** revenue — the **protocol share** of swap fees on non–der Bodensee gauged pools (**100%** of that share per §xxix; **~50%** of charged swap fee volume) plus **ERC-4626 yield fees (100% of the 10% skim on non–der Bodensee gauged pools)** — flows automatically to **der Bodensee Pool** as one-sided svZCHF deposits (per §xxix). **LP residuals** on those swap fees (**~50%** of charged fee) are not protocol revenue — they stay with originating-pool LPs. **Swap fees inside der Bodensee** (0.75% at genesis) stay with **der Bodensee LPs** in full. CCC philosophy: capital allocation is algorithmic, revenue flows are rule-based, no separate treasury can be captured, redirected, or extracted from. Fully autonomous from block 0.

