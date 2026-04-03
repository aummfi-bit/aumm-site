# Aureum Protocol

> Imagine mining BTC with capital, not electricity.  
> Imagine BTC with a buy back and burn program sponsored by real fees.  
> Imagine your capital is liquidity generating real fees that buy back and burn the scarce token.  
> Meet $AuMM.

## i. One Line

An immutable fair-launch AMM where emissions follow fixed Bitcoin-style issuance and automatic on-chain allocation only.

## ii. Core Principles

- No pre-mine, no VC allocation, no team allocation.
- 21M max supply, per-block halving schedule.
- No multisig, no admin keys, no upgradeability, no pause.
- No emission voting; governance exists only for non-emission actions.
- Automatic CCB allocation after the transition (EMA TVL, CCB multiplier, and Incendiary terms per `constitution.md`).

## iii. Emission Regimes

- **Through end of Month 10:** emissions to the 28 immutable Miliarium Aureum pools are **purely equal** (**1/28** each). Other pools may exist but do not receive this equal tranche.
- **Months 11–12 (two-month transition):** blend linearly from equal to CCB over the window. At the midpoint, the mix is half equal and half CCB. See `formulas.md` for the blend formula.
- **After Year 1:** emissions follow only the CCB — each pool scored by smoothed TVL, CCB multiplier, and Incendiary multiplier, normalized across eligible pools. No vote. See `constitution.md` and `formulas.md`.

## iv. Why It Matters

The protocol minimizes human discretion and maximizes deterministic execution. Allocation follows capital behavior, not governance behavior.

Proposal governance is still active for gauges, treasury, and fee proposals, and must rely on on-chain verifiable data only.

See Immutable Parameters in `constitution.md`.