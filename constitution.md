# Constitution

*The immutable operating law of Aureum.*

---

## I. Protocol Control Model

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

Governance cannot alter emission formulas, halving math, PMAR constants, or other immutable parameters.

### Composition Challenge Rule (Miliarium Aureum)

Composition challenges are governance-gated non-emission actions and pass only with a **2/3 supermajority** of protocol-wide tessera-weighted votes.

A valid composition update must preserve pool intent:

- replacement token must represent the same asset class, or
- replacement token must have materially similar economic properties (risk/yield/exposure profile)

This is a like-for-like renewal path, not a free-form redesign path.

### Proposal Data Integrity Rule

All proposals must reference verifiable on-chain state only. A valid proposal must include contract addresses, block ranges, and deterministic on-chain metrics used by its rationale. Off-chain-only claims, unverifiable dashboards, social polling, or discretionary narratives are invalid.

## II. Emission Operating Rules

### Year 1 Equal Distribution

- Months 0-12: 100% of block emissions are distributed equally across the 28 immutable Miliarium Aureum pools (1/28 each).

### Post-Year-1 Automatic Distribution

- Starting at Month 13 Day 1 (after the final block of Year 1), emissions are allocated purely by on-chain formula:

```
Score(pool_i) = TVL_EMA60(pool_i) * PMAR_mult(pool_i) * Incendiary_mult(pool_i)
share(pool_i) = Score(pool_i) / sum(all pool scores)
```

There is no voting layer, no Bubble multiplier, and no human override.

## III. Immutable Parameters

The following are immutable from block 0 and cannot be changed by any means:

- Maximum AuMM supply: 21,000,000
- Emission halving schedule and per-block rewards
- Fee splits, including 25% protocol revenue to AuMM buyback-and-burn
- PMAR rules: step size +/-0.05, clamp [0.75, 1.25], dead zone 0.1%, EMA(60) horizon
- List of 28 Miliarium Aureum pools (locked at launch; see `Miliarium_Aureum.md`)
- Core AMM mathematics, CCB formula, and eligibility criteria
- Any withdrawal resets AuMT power
- No admin keys, no multisig, no upgradability, no pause functions

## IV. Treasury Model

- Treasury is fully on-chain and non-custodial from genesis.
- No privileged signer exists.
- Treasury execution is contract-enforced only.
- Treasury spends require successful qualified AuMT vote and timelock execution.

