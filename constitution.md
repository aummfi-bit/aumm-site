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

Protocol **months** (Month 1 … Month 12) are defined on-chain as fixed block ranges from genesis; **Year 1** is Months 1–12 inclusive.

### Equal regime (through end of Month 10)

- From **genesis through the final block of Month 10**, 100% of block emissions to the Miliarium Aureum tranche are split **equally** across the **28** immutable pools (**1/28** each).

### Transition regime (Months 11–12)

- **Months 11 and 12** are a **two-month linear transition** from pure equal allocation to pure CCB allocation.
- Let **equal_share_i = 1/28** for each immutable pool, and **CCB_share_i** be the normalized share from the CCB score (below) for that block.
- Let **α** increase **linearly** from **0** at the **first block of Month 11** to **1** at the **last block of Year 1** (final block of Month 12). At every block in the transition:

```
share_i(block) = (1 - α(block)) * equal_share_i + α(block) * CCB_share_i(block)
```

- At the **temporal midpoint** of the transition window (halfway between the start of Month 11 and the end of Year 1), **α = 0.5** — emissions are **halfway** between the equal method and the full CCB method for that block.
- **CCB_share** uses the same score definition as post–Year-1 (PMAR and Incendiary terms apply inside the CCB leg).

### Full CCB (from Year 1 end onward)

- From the **first block after Year 1** (and equivalently **α = 1** at the last block of Year 1), emissions follow **only** the CCB formula:

```
Score(pool_i) = TVL_EMA60(pool_i) * PMAR_mult(pool_i) * Incendiary_mult(pool_i)
CCB_share_i = Score(pool_i) / sum(all eligible pool scores)
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

