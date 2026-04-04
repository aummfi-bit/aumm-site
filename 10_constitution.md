# Constitution

*The immutable operating law of Aureum.*

---

## xxvii. Protocol Control Model

### AUREUM Governance Actions (aumm.fi)

- **Gauge Proposal** — new pool **emission eligibility** (gauge approval); deposit **one-sided into der Bodensee Pool**. Details: [Bootstrap](08_bootstrap.md) §xxiv (Gauge Proposal).
- **Gauge Challenge** — **revoke** an existing gauge; deposit **one-sided into der Bodensee Pool**. Non-Miliarium targets: scaled deposit [F-12](11_formulas.md). **Miliarium Aureum (28):** flat deposit only — F-12 does not apply. Details: [Bootstrap](08_bootstrap.md) §xxiv (Gauge Challenge).
- **Fee proposals** — **swap / yield fee** changes **within immutable bounds**; deposit **one-sided into der Bodensee Pool**. Voting model: [Tokenomics](04_tokenomics.md) §ix (Governance); mechanics: [Bootstrap](08_bootstrap.md) §xxiv (Governance Proposals).
- **Miliarium Aureum Composition Challenge** — **2/3 supermajority** tessera-weighted vote to deprecate a pool and **replace** assets in-slot (like-for-like); deposit **one-sided into der Bodensee Pool**. Details: [Bootstrap](08_bootstrap.md) §xxiv (Miliarium Aureum Composition Challenge) and **### Composition Challenge Rule** below.

**All governance proposal deposits** — gauge approval, gauge challenge, fee proposals, and composition challenge — follow the **same treatment:** **one-sided inflow into der Bodensee Pool** in **svZCHF or sUSDS equivalent (whichever is higher)**, non-refundable, **no LP tokens** minted to the proposer; only the **amounts** differ (see table). No treasury wallet; no alternate routing.

Turnout minima and approval thresholds: **### Quorum and Deposit Requirements** below.

Aureum is immutable and non-custodial from block 0:

- no admin keys
- no multisig
- no upgradeability
- no pause function
- no voting over emissions
- no off-chain dependencies for core operation

All core contracts are immutable from block 0. Governance exists for non-emission actions only.

### Governance Scope (Non-Emission Only)

Qualified AuMT holders submit and vote on the **four governance actions** listed above. Governance cannot alter emission formulas, halving math, CCB multiplier constants, or other immutable parameters.

### Quorum and Deposit Requirements

| Decision Type | Minimum Turnout | Deposit (svZCHF/sUSDS, to der Bodensee Pool) | Approval Threshold | Failure Mode |
|--------------|-----------------|------------------------|--------------------|-------------|
| Gauge approval | 20% of total qualified voting power | 100 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Gauge challenge (revocation) — non-Miliarium gauged pool | 20% of total qualified voting power | Per [F-12](11_formulas.md): **max(10 BTC CHF equiv., 1,000,000 CHF × √((1−p_tvl)(1−p_eff)))** in svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Gauge challenge (revocation) — Miliarium Aureum (28 pools) | 20% of total qualified voting power | **1,000** svZCHF/sUSDS equivalent — **F-12 does not apply** | Simple majority | Auto-fail if turnout < 20% |
| Fee parameter changes | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Composition challenge | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | 2/3 supermajority | Auto-fail if turnout < 20% or < 2/3 approval |

All deposits are **paid one-sided into der Bodensee Pool** (same mechanic as other governance inflows: no LP tokens minted to the proposer), denominated in **svZCHF or sUSDS equivalent, whichever is higher at the time of submission** — preventing gaming via currency fluctuation. Non-refundable. Every governance action deepens der Bodensee Pool reserves. **Gauge challenge:** the scaled deposit in [F-12](11_formulas.md) applies only when the **target pool is not** one of the **28 Miliarium Aureum** registry pools; for those, use the **fixed 1,000** row above.

**Low-Turnout Safeguard.** Every proposal type requires a minimum turnout of **20% of total qualified voting power**. If turnout falls below 20%, the proposal is **automatically rejected** — no timelock, no fallback. The proposal must be resubmitted. This is uniform across all proposal types (see [Tokenomics](04_tokenomics.md) Low-Turnout Safeguard).

### Composition Challenge Rule (Miliarium Aureum)

Composition challenges are governance-gated non-emission actions and pass only with a **2/3 supermajority** of protocol-wide tessera-weighted votes. A single proposal may cover both theme assets in a pool if both have failed.

Pool token composition is immutable on-chain. A composition challenge does not swap tokens inside a deployed pool — it **deprecates** the old pool (gauge revoked, emissions cease) and **launches a replacement** into the same Miliarium slot, following the standard bootstrap path (gauge proposal, gauge vote, 90-day boost, optional Incendiary).

A valid composition update must preserve pool intent — **like-for-like** means:

- **Same sector** — the replacement must belong to the same asset class or market sector as the token it replaces
- **Same risk profile** — materially similar economic properties (volatility, yield type, credit exposure)
- **Same template role** — the replacement must fill the same structural role in the pool (yield core, routing anchor, or theme asset)

This mechanism activates only when an asset **ceases to function** (delisting, wrapper sunset, issuer failure). It is a renewal path, not a redesign path. See [Bootstrap (§xxiv)](08_bootstrap.md) for worked examples.

### Proposal Data Integrity Rule

All proposals must reference verifiable on-chain state only. A valid proposal must include contract addresses, block ranges, and deterministic on-chain metrics used by its rationale. Off-chain-only claims, unverifiable dashboards, social polling, or discretionary narratives are invalid.

## xxviii. Emission Operating Rules

*Narrative treatment: [Theoretical foundations](03_theoretical_foundation.md) (§§vi–vii; EMA §vi-b).*

Protocol **months** (Month 1 … Month 12) are defined on-chain as fixed block ranges from genesis; **Year 1** is Months 1–12 inclusive.

### Equal regime (through end of Month 10)

- Each block’s emission is split between **der Bodensee bootstrap** and the **LP tranche**. The bootstrap share is **80% of block emission at genesis**, decaying **linearly to zero** by the **final block of Month 10**; it is minted as **one-sided AuMM** into der Bodensee Pool (no LP tokens). See [Protocol formulas (F-0)](11_formulas.md).
- From **genesis through the final block of Month 10**, the **LP tranche** (after the bootstrap skim) is split **equally** across the **28** Miliarium pools — **1/28 of the LP tranche** each (not 1/28 of the full block emission while the bootstrap share is positive). **100% of the LP tranche** goes to LPs — no treasury wallet.

### Transition regime (Months 11–12)

**Months 11–12** linearly blend **equal 1/28** with the **CCB** share for each immutable pool. A blend parameter runs from zero (pure equal) at the first block of Month 11 to one (pure CCB) at the last block of Year 1. At the midpoint of the window the mix is exactly half equal and half CCB. The CCB leg uses the same score as post–Year-1 (smoothed TVL × CCB multiplier). See [Protocol formulas](11_formulas.md) for the formal blend formula. (Bootstrap is zero from Month 11 onward; the LP tranche equals the full block emission.)

### Full CCB (from Year 1 end onward)

Incendiary Boost claims are skimmed from the **LP emission tranche** (after any der Bodensee bootstrap skim; post–Month 10 the tranche is the full block emission) **before** the CCB splits the remainder. Each pool carries a 60-day exponential moving average of its on-chain TVL (see [Theoretical foundations (§vi-b — EMA)](03_theoretical_foundation.md) for the canonical EMA explanation). The CCB scores each eligible pool by combining its smoothed TVL with its CCB multiplier (Miliarium pools only; all others use a neutral value), then normalizes scores across all eligible pools to produce fractional shares. CCB multipliers update bi-weekly for the 28 Miliarium pools only, within the immutable band defined in §xxix below. No voting layer, no human override. See [Protocol formulas](11_formulas.md) for all formal definitions.

## xxix. Immutable Parameters (Canonical Source)

This section is the **single canonical source** for all immutable protocol parameters. Every other document that references these values should cite this section rather than restating them inline.

These parameters are immutable because they define the boundaries within which the protocol can never be gamed, captured, or inflated. They fall into three classes: **economic constants** (supply cap, halving schedule, fee splits) that guarantee scarcity and revenue flow; **anti-gaming safeguards** (CCB multiplier bounds, EMA horizon, eligibility criteria) that prevent reflexive manipulation; and **anti-capture mechanics** (governance dampening exponents, withdrawal reset, qualification periods) that ensure no single actor can dominate the protocol regardless of capital size.

The following are immutable from block 0 and cannot be changed by any means:

- Maximum AuMM supply: 21,000,000
- Emission halving schedule and block emission rates
- Fee splits (**swap fees on Miliarium and other non–der Bodensee pools**): 50% to LP bonus; 50% to der Bodensee Pool as one-sided svZCHF inflows. **ERC-4626 yield fee (10% skim):** 100% to der Bodensee Pool as one-sided svZCHF inflows
- **der Bodensee Pool** (**AuMM/svZCHF LBP only**): **0.75%** swap fee on trades in this pool; **100%** of those swap fees accrue to **der Bodensee LPs** (retained in the pool — not split to the protocol-wide 50/50 route)
- der Bodensee Pool parameters: **genesis seed liquidity** — **1 AuMM** and **1 svZCHF** deposited at pool creation (protocol-deployed, immutable); start weights 90% AuMM / 10% svZCHF, end weights 48% AuMM / 52% svZCHF, 18-month linear decay, **protocol-captured** revenue from other pools as one-sided svZCHF inflows, **Months 1–10** one-sided AuMM bootstrap (80% at genesis → 0% at end of Month 10, linear decay)
- CCB multiplier rules: step size ±0.05, clamp [0.75, 1.25], dead zone 0.1%, EMA(60) horizon
- List of 28 Miliarium Aureum pools (locked at launch; see [Miliarium Aureum registry](05_miliarium_aureum.md))
- Core AMM mathematics, CCB formula, and eligibility criteria
- Governance dampening exponents: fourth root (Era 0, years 0–4), cube root (Era 1+, from first halving block onward) — transition is permanent and occurs once
- Any withdrawal resets AuMT power
- No admin keys, no multisig, no upgradability, no pause functions

## xxx. No Treasury

There is no treasury. The protocol has no entity or wallet that receives AuMM for discretionary use, and no mechanism that holds discretionary funds or disburses capital by vote. **der Bodensee Pool** receives **Months 1–10** bootstrap AuMM as **one-sided pool deposits** (not extractable, no LP tokens minted — same class as one-sided svZCHF fee inflows). **Protocol-captured** revenue — **50% of swap fees on non–der Bodensee pools** plus **100% of ERC-4626 yield fees** — flows automatically to **der Bodensee Pool** as one-sided svZCHF inflows. The **other 50%** of those swap fees returns to LPs on those pools as LP bonus. **Swap fees on trades inside der Bodensee Pool** (0.75% fee tier) stay with **der Bodensee LPs** in the pool. This design follows the Continuous Capital Corporation (CCC) philosophy: capital allocation is algorithmic, revenue flows are rule-based, and there is no separate treasury that can be captured, redirected, or extracted from. The system is fully autonomous from block 0.

