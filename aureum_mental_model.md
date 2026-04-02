# Aureum Protocol - Mental Model

## One Line

An immutable fair-launch AMM where emissions follow fixed Bitcoin-style issuance and automatic on-chain allocation only.

## Core Principles

1. No pre-mine, no VC allocation, no team allocation.
2. 21M max supply, per-block halving schedule.
3. No multisig, no admin keys, no upgradeability, no pause.
4. No emission voting; governance exists only for non-emission actions.
5. Automatic CCB + PMAR logic after Year 1.

## Emission Regimes

- **Months 0-12:** equal emissions to the 28 Miliarium Aureum pools.
- **Month 13 Day 1 onward:** pure EMA(60) TVL + PMAR automatic competition.

## Why It Matters

The protocol minimizes human discretion and maximizes deterministic execution. Allocation follows capital behavior, not governance behavior.

Proposal governance is still active for gauges, treasury, and fee proposals, and must rely on on-chain verifiable data only.

See Immutable Parameters in `constitution.md`.
