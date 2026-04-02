# Miliarium Aureum Multiplier Adjustment Rule (PMAR)

*Immutable from block 0.*

---

## Purpose

PMAR is a deterministic, oracle-free multiplier engine over the 28 immutable Miliarium Aureum pools.

## Activation Window

- **Through end of Month 10:** equal **1/28** distribution; the CCB leg is not yet used for emissions (PMAR does not affect the equal tranche).
- **Months 11–12:** PMAR applies **inside the CCB leg** of the blended transition share (see `constitution.md` and `formulas.md`).
- **After Year 1:** PMAR is fully active **inside** pure CCB allocation, where each pool's score combines smoothed TVL, PMAR multiplier, and Incendiary multiplier (see `constitution.md` and `formulas.md`).

## Fixed Rules

- step size: +/-0.05
- clamp: [0.75, 1.25]
- dead zone: 0.1% of ratio
- horizon: EMA(60)

## Core Update

Each bi-weekly cycle, a Miliarium pool's multiplier is adjusted by a protocol-wide step (macro TVL direction) and a pool-specific step (pool TVL vs Miliarium average), then clamped to the [0.75, 1.25] band. Initial multiplier is 1.00. See `formulas.md` for the formal update rule.

## Immutable Reference

See Immutable Parameters in `constitution.md`.
