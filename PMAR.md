# Miliarium Aureum Multiplier Adjustment Rule (PMAR)

*Immutable from block 0.*

---

## Purpose

PMAR is a deterministic, oracle-free multiplier engine over the 28 immutable Miliarium Aureum pools.

## Activation Window

- **Through end of Month 10:** equal **1/28** distribution; the CCB leg is not yet used for emissions (PMAR does not affect the equal tranche).
- **Months 11–12:** PMAR applies **inside the CCB leg** of the blended share `(1 − α) × (1/28) + α × CCB_share` (see `constitution.md`).
- **After Year 1:** PMAR is fully active **inside** pure CCB allocation (`TVL_EMA60 * PMAR_mult * Incendiary_mult`; see `constitution.md`).

## Fixed Rules

- step size: +/-0.05
- clamp: [0.75, 1.25]
- dead zone: 0.1% of ratio
- horizon: EMA(60)

## Core Update

```
M_i(t) = clamp(M_i(t-1) + delta_global + delta_intra_i, 0.75, 1.25)
```

## Immutable Reference

See Immutable Parameters in `constitution.md`.
