# Constitution

*The immutable operating law of Aureum.*

---

## xxvii. Protocol Control Model

Aureum is immutable and non-custodial from block 0:

- no admin keys
- no multisig
- no upgradeability
- no pause function
- no voting over emissions
- no off-chain dependencies for core operation

All core contracts are immutable from block 0. Governance exists for non-emission actions only.

### Governance Scope (Non-Emission Only)

Qualified AuMT holders can submit proposals and vote on:

- gauge approvals
- gauge challenges (revocation)
- treasury disbursements
- fee parameter changes within immutable bounds
- Miliarium Aureum composition challenges

Governance cannot alter emission formulas, halving math, CCB multiplier constants, or other immutable parameters.

### Quorum and Deposit Requirements

| Decision Type | Minimum Turnout | Deposit (AuMM, burned) | Approval Threshold | Failure Mode |
|--------------|-----------------|------------------------|--------------------|-------------|
| Gauge approval | 20% of total qualified voting power | 100 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Gauge challenge (revocation) | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Fee parameter changes | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Treasury spends >10% of balance | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Simple majority | Auto-fail if turnout < 20% |
| Composition challenge | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | 2/3 supermajority | Auto-fail if turnout < 20% or < 2/3 approval |

All deposits are denominated in **svZCHF or sUSDS equivalent, whichever is higher at the time of submission** — preventing gaming via currency fluctuation. Non-refundable. Every governance action creates deflationary pressure on AuMM.

**Low-Turnout Safeguard.** Every proposal type requires a minimum turnout of **20% of total qualified voting power**. If turnout falls below 20%, the proposal is **automatically rejected** — no timelock, no fallback. The proposal must be resubmitted. This is uniform across all proposal types (see `tokenomics.md` Low-Turnout Safeguard).

### Composition Challenge Rule (Miliarium Aureum)

Composition challenges are governance-gated non-emission actions and pass only with a **2/3 supermajority** of protocol-wide tessera-weighted votes. A single proposal may cover both theme assets in a pool if both have failed.

Pool token composition is immutable on-chain. A composition challenge does not swap tokens inside a deployed pool — it **deprecates** the old pool (gauge revoked, emissions cease) and **launches a replacement** into the same Miliarium slot, following the standard bootstrap path (gauge proposal, gauge vote, 90-day boost, optional Incendiary).

A valid composition update must preserve pool intent — **like-for-like** means:

- **Same sector** — the replacement must belong to the same asset class or market sector as the token it replaces
- **Same risk profile** — materially similar economic properties (volatility, yield type, credit exposure)
- **Same template role** — the replacement must fill the same structural role in the pool (yield core, routing anchor, or theme asset)

This mechanism activates only when an asset **ceases to function** (delisting, wrapper sunset, issuer failure). It is a renewal path, not a redesign path. See `bootstrap.md` §xxiv for worked examples.

### Proposal Data Integrity Rule

All proposals must reference verifiable on-chain state only. A valid proposal must include contract addresses, block ranges, and deterministic on-chain metrics used by its rationale. Off-chain-only claims, unverifiable dashboards, social polling, or discretionary narratives are invalid.

## xxviii. Emission Operating Rules

*Narrative treatment: `theoretical_foundation.md` (sections vi and vii).*

Protocol **months** (Month 1 … Month 12) are defined on-chain as fixed block ranges from genesis; **Year 1** is Months 1–12 inclusive.

### Equal regime (through end of Month 10)

- From **genesis through the final block of Month 10**, 100% of block emissions to the Miliarium Aureum tranche are split **equally** across the **28** Miliarium pools (**1/28** each).

### Transition regime (Months 11–12)

**Months 11–12** linearly blend **equal 1/28** with the **CCB** share for each immutable pool. A blend parameter runs from zero (pure equal) at the first block of Month 11 to one (pure CCB) at the last block of Year 1. At the midpoint of the window the mix is exactly half equal and half CCB. The CCB leg uses the same score as post–Year-1 (smoothed TVL × CCB multiplier). See `formulas.md` for the formal blend formula.

### Full CCB (from Year 1 end onward)

Incendiary Boost claims are skimmed from the block emission first; the remainder is what the CCB splits. Each pool carries a 60-day exponential moving average of its on-chain TVL (see `theoretical_foundation.md` §vi for the canonical EMA explanation). The CCB scores each eligible pool by combining its smoothed TVL with its CCB multiplier (Miliarium pools only; all others use a neutral value), then normalizes scores across all eligible pools to produce fractional shares. CCB multipliers update bi-weekly for the 28 Miliarium pools only, within the immutable band defined in §xxix below. No voting layer, no human override. See `formulas.md` for all formal definitions.

## xxix. Immutable Parameters (Canonical Source)

This section is the **single canonical source** for all immutable protocol parameters. Every other document that references these values should cite this section rather than restating them inline.

These parameters are immutable because they define the boundaries within which the protocol can never be gamed, captured, or inflated. They fall into three classes: **economic constants** (supply cap, halving schedule, fee splits) that guarantee scarcity and revenue flow; **anti-gaming safeguards** (CCB multiplier bounds, EMA horizon, eligibility criteria) that prevent reflexive manipulation; and **anti-capture mechanics** (governance dampening exponents, withdrawal reset, qualification periods) that ensure no single actor can dominate the protocol regardless of capital size.

The following are immutable from block 0 and cannot be changed by any means:

- Maximum AuMM supply: 21,000,000
- Emission halving schedule and block emission rates
- Fee splits, including 25% protocol revenue to AuMM buyback-and-burn
- CCB multiplier rules: step size ±0.05, clamp [0.75, 1.25], dead zone 0.1%, EMA(60) horizon
- List of 28 Miliarium Aureum pools (locked at launch; see `Miliarium_Aureum.md`)
- Core AMM mathematics, CCB formula, and eligibility criteria
- Any withdrawal resets AuMT power
- No admin keys, no multisig, no upgradability, no pause functions

## xxx. Treasury Model

- Treasury is fully on-chain and non-custodial from genesis.
- No privileged signer exists.
- Treasury execution is contract-enforced only.
- Treasury spends require successful qualified AuMT vote and timelock execution.

### Allocation

| Category | Share | Notes |
|----------|-------|-------|
| Audits & Security | 40% | Ongoing audit coverage, bug bounties, formal verification |
| Development | 30% | Smart contract maintenance, frontend, integrations |
| Operations | 20% | Infrastructure, RPC, subgraph, monitoring |
| Reserve | 10% | Emergency fund |

The treasury never sells AuMM to fund operations. AuMM received during the treasury emission phase (months 0–10) is used exclusively for protocol-owned liquidity: seeding the AuMM trading pool at month 6 and operating the price ceiling stabilization mechanism (months 6–12). After month 10, the treasury never receives new AuMM — the ceiling continues using existing inventory until month 12. All leftover AuMM is burned at month 12. Development, audits, and operations are funded entirely from stablecoin fee revenue.

