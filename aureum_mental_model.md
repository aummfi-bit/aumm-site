# Aureum Protocol - Mental Model

Imagine mining BTC with capital, not electricity. Your liquidity generates real fees that buy back and burn the scarce token. Meet $AuMM.

## I — One Line

An immutable fair-launch AMM where emissions follow fixed Bitcoin-style issuance and automatic on-chain allocation only.

## II — Core Principles

- No pre-mine, no VC allocation, no team allocation.
- 21M max supply, per-block halving schedule.
- No multisig, no admin keys, no upgradeability, no pause.
- No emission voting; governance exists only for non-emission actions.
- Automatic CCB allocation after the transition (EMA TVL, PMAR, and Incendiary terms per `constitution.md`).

## III — Emission Regimes

- **Through end of Month 10:** emissions to the 28 immutable Miliarium Aureum pools are **purely equal** (**1/28** each). Other pools may exist but do not receive this equal tranche.
- **Months 11–12 (two-month transition):** blend **linearly** from equal to CCB: **share = (1 − α) × (1/28) + α × CCB_share**, with **α** from **0 → 1** over the window. At the **midpoint**, **α = 0.5** — **half** equal, **half** CCB.
- **After Year 1:** **α = 1** — emissions follow **only** the CCB formula (no vote): **TVL EMA(60) × PMAR × Incendiary**, normalized across **eligible** pools. See **`constitution.md`** and **`theoretical_foundation.md`**.

## IV — Why It Matters

The protocol minimizes human discretion and maximizes deterministic execution. Allocation follows capital behavior, not governance behavior.

Proposal governance is still active for gauges, treasury, and fee proposals, and must rely on on-chain verifiable data only.

See Immutable Parameters in `constitution.md`.
