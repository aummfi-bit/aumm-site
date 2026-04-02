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

Governance cannot alter emission formulas, halving math, PMAR constants, or other immutable parameters.

### Composition Challenge Rule (Miliarium Aureum)

Composition challenges are governance-gated non-emission actions and pass only with a **2/3 supermajority** of protocol-wide tessera-weighted votes.

A valid composition update must preserve pool intent:

- replacement token must represent the same asset class, or
- replacement token must have materially similar economic properties (risk/yield/exposure profile)

This is a like-for-like renewal path, not a free-form redesign path.

### Proposal Data Integrity Rule

All proposals must reference verifiable on-chain state only. A valid proposal must include contract addresses, block ranges, and deterministic on-chain metrics used by its rationale. Off-chain-only claims, unverifiable dashboards, social polling, or discretionary narratives are invalid.

## xxviii. Emission Operating Rules

*Narrative treatment: `theoretical_foundation.md` (sections vi and vii).*

Protocol **months** (Month 1 … Month 12) are defined on-chain as fixed block ranges from genesis; **Year 1** is Months 1–12 inclusive.

### Equal regime (through end of Month 10)

- From **genesis through the final block of Month 10**, 100% of block emissions to the Miliarium Aureum tranche are split **equally** across the **28** immutable pools (**1/28** each).

### Transition regime (Months 11–12)

**Months 11–12** linearly blend **equal 1/28** with the **CCB** share for each immutable pool. **α** runs from **0** at the first block of Month 11 to **1** at the last block of Year 1.

```
share_i(block) = (1 − α(block)) × (1/28) + α(block) × CCB_share_i(block)
```

At the **midpoint** of the window, **α = 0.5** (half equal, half CCB). **CCB_share_i** uses the same score as post–Year-1 (PMAR and Incendiary inside the CCB leg).

### Full CCB (from Year 1 end onward)

**Incendiary Boost** is skimmed from the block reward first; **Remaining** is what the CCB splits. **TVL_EMA60** is a **per-pool** 60-day EMA of on-chain TVL (**α = 2/(60+1)**). **PMAR_mult** applies **only** to the 28 Miliarium pools; for other eligible pools use **1**. **CCB_share** normalizes over **eligible** pools only.

```
Remaining(block) = block_reward(block) − Incendiary_claims(block)

TVL_EMA_pool(today) = alpha × TVL_spot(today) + (1 − alpha) × TVL_EMA_pool(yesterday)
alpha = 2 / (60 + 1)

Score(pool_i) = TVL_EMA60(pool_i) × PMAR_mult(pool_i) × Incendiary_mult(pool_i)

CCB_share_i = Score(pool_i) / sum(all eligible pool scores)
```

**PMAR** (Miliarium only), bi-weekly:

```
M_i(t) = clamp(M_i(t−1) + delta_global + delta_intra_i, 0.75, 1.25)
```

No voting layer, no Bubble multiplier, no human override.

## xxix. Immutable Parameters

The following are immutable from block 0 and cannot be changed by any means:

- Maximum AuMM supply: 21,000,000
- Emission halving schedule and per-block rewards
- Fee splits, including 25% protocol revenue to AuMM buyback-and-burn
- PMAR rules: step size +/-0.05, clamp [0.75, 1.25], dead zone 0.1%, EMA(60) horizon
- List of 28 Miliarium Aureum pools (locked at launch; see `Miliarium_Aureum.md`)
- Core AMM mathematics, CCB formula, and eligibility criteria
- Any withdrawal resets AuMT power
- No admin keys, no multisig, no upgradability, no pause functions

## xxx. Treasury Model

- Treasury is fully on-chain and non-custodial from genesis.
- No privileged signer exists.
- Treasury execution is contract-enforced only.
- Treasury spends require successful qualified AuMT vote and timelock execution.

