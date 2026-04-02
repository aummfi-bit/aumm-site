# Miliarium Aureum Multiplier Adjustment Rule (PMAR)

*Immutable from block 0.*

---

## Purpose

PMAR is a deterministic, oracle-free multiplier engine over the 25 immutable Miliarium Aureum pools.

## Activation Window

- Before end of Year 1: equal distribution regime is active.
- **After the last block of Year 1 (Month 13 Day 1):** PMAR is fully active inside CCB allocation.

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
