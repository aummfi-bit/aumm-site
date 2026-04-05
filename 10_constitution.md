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

Pool composition is immutable on-chain. A composition challenge **deprecates** the old pool (gauge revoked, emissions cease) and **launches a replacement** into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost, optional Incendiary Boost).

**Like-for-like** means:

- **Same sector** — the replacement must belong to the same asset class or market sector as the token it replaces
- **Same risk profile** — materially similar economic properties (volatility, yield type, credit exposure)
- **Same template role** — the replacement must fill the same structural role in the pool (yield core, routing anchor, or theme asset)

Activates only when an asset **ceases to function** (delisting, wrapper sunset, issuer failure). Renewal, not redesign. Worked examples in [Bootstrap (§xxiv)](08_bootstrap.md).

### Proposal Data Integrity Rule

All proposals must reference verifiable on-chain state only — contract addresses, block ranges, and deterministic on-chain metrics. Off-chain-only claims, unverifiable dashboards, social polling, or discretionary narratives are invalid.

## xxviii. Emission Operating Rules

*Narrative treatment: [Theoretical foundations](03_theoretical_foundation.md) (§§vi–vii; EMA §vi-b).*

Protocol **months** (Month 1 … Month 12) are defined on-chain as fixed block ranges from genesis; **Year 1** is Months 1–12 inclusive.

### Equal regime (through end of Month 10)

- Each block’s emission splits between **der Bodensee bootstrap** and the **LP tranche**. Bootstrap: **80% of block emission at genesis**, decaying **linearly to zero** by the **final block of Month 10**; minted as **one-sided AuMM** into der Bodensee Pool (no LP tokens). See [Protocol formulas (F-0)](11_formulas.md).
- Through the final block of Month 10, the **LP tranche** is split **equally** — **1/28** each (not 1/28 of the full block emission while bootstrap is positive). **100%** to LPs — no treasury wallet.

### Transition regime (Months 11–12)

**Months 11–12** linearly blend **equal 1/28** with the **CCB** share. Blend parameter: zero (pure equal) at the first block of Month 11 → one (pure CCB) at the last block of Year 1. At midpoint, exactly half and half. The CCB leg uses the same score as post–Year-1 (smoothed TVL × CCB multiplier). Formal blend formula in [Protocol formulas](11_formulas.md). (Bootstrap is zero from Month 11; LP tranche = full block emission.)

### Full CCB (from Year 1 end onward)

Incendiary Boost claims (1 epoch / 14 days each, any deposit amount, once per epoch per pool) are skimmed from the **LP emission tranche** (after bootstrap skim; post–Month 10 the tranche is the full block emission) **before** the CCB splits the remainder. Each pool carries a 60-day EMA of on-chain TVL ([Theoretical foundations §vi-b](03_theoretical_foundation.md)). The CCB scores each eligible pool by combining smoothed TVL with its CCB multiplier (Miliarium pools only; others use a neutral value), then normalizes to produce fractional shares. Multipliers update bi-weekly for the 28 only, within the immutable band in §xxix below. No voting, no human override. Formal definitions in [Protocol formulas](11_formulas.md).

## xxix. Immutable Parameters (Canonical Source)

**Single canonical source** for all immutable protocol parameters. Other documents should cite this section rather than restating values.

Three classes: **economic constants** (supply cap, halving schedule, fee splits) guaranteeing scarcity and revenue flow; **anti-gaming safeguards** (CCB multiplier bounds, EMA horizon, eligibility criteria) preventing reflexive manipulation; **anti-capture mechanics** (governance dampening exponents, withdrawal reset, qualification periods) ensuring no single actor dominates regardless of capital size.

Immutable from block 0, cannot be changed by any means:

- Maximum AuMM supply: 21,000,000
- Emission halving schedule and block emission rates
- Fee routing (**swap fees on Miliarium and other non–der Bodensee pools**): 100% to der Bodensee Pool as one-sided svZCHF inflows. **ERC-4626 yield fee (10% skim):** 100% to der Bodensee Pool as one-sided svZCHF inflows
- **der Bodensee Pool** (**AuMM/svZCHF LBP only**): **0.75%** swap fee on trades in this pool; **100%** of those swap fees accrue to **der Bodensee LPs** (retained in the pool — not routed through the protocol fee pipeline)
- der Bodensee Pool parameters: **genesis seed liquidity** — **1 AuMM** and **1 svZCHF** deposited at pool creation (protocol-deployed, immutable); start weights 90% AuMM / 10% svZCHF, end weights 48% AuMM / 52% svZCHF, 18-month linear decay, **protocol-captured** revenue from other pools as one-sided svZCHF inflows, **Months 1–10** one-sided AuMM bootstrap (80% at genesis → 0% at end of Month 10, linear decay)
- CCB multiplier rules: step size ±0.05, clamp [0.75, 1.25], dead zone 0.1%, EMA(60) horizon
- List of 28 Miliarium Aureum pools (locked at launch; see [Miliarium Aureum registry](05_miliarium_aureum.md))
- Core AMM mathematics, CCB formula, and eligibility criteria
- Governance dampening exponents: fourth root (Era 0, years 0–4), cube root (Era 1+, from first halving block onward) — transition is permanent and occurs once
- Any withdrawal resets AuMT power
- No admin keys, no multisig, no upgradability, no pause functions

## xxx. No Treasury

No treasury. No entity or wallet receives AuMM for discretionary use. No mechanism holds discretionary funds or disburses capital by vote. **der Bodensee Pool** receives **Months 1–10** bootstrap AuMM as **one-sided pool deposits** (not extractable, no LP tokens minted). **Protocol-captured** revenue — **swap fees on non–der Bodensee pools** plus **ERC-4626 yield fees (10% skim)** — flows automatically and entirely to **der Bodensee Pool** as one-sided svZCHF. **Swap fees inside der Bodensee** (0.75%) stay with **der Bodensee LPs**. CCC philosophy: capital allocation is algorithmic, revenue flows are rule-based, no separate treasury can be captured, redirected, or extracted from. Fully autonomous from block 0.

