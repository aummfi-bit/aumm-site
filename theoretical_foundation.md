## I - Theoretical Foundations

The CCB draws from established lines of research:

- pro-cyclicality in DeFi incentive design
- rule-based monetary issuance
- low-pass signal filtering (EMA)
- automatic stabilizers in complex systems
- governance minimization for attack-surface reduction

## II - CCB: Fully Automatic Allocation

The Continuous Central Bank allocates emissions with no voting input.

### Activation Sequence

- Months 0-12: equal emissions across the 25 Miliarium Aureum pools.
- Month 13 Day 1 onward: full CCB + PMAR allocation.

### Core Formula

```
TVL_EMA_pool(today) = alpha * TVL_spot(today) + (1 - alpha) * TVL_EMA_pool(yesterday)
alpha = 2 / (60 + 1)

Score(pool_i) = TVL_EMA60(pool_i) * PMAR_mult(pool_i) * Incendiary_mult(pool_i)
share(pool_i) = Score(pool_i) / sum(all pool scores)
```

### Design Consequence

- Capital is the only allocation signal.
- Emission rules are deterministic and immutable.
- Human governance is removed from allocation logic.
- Governance remains available for non-emission actions under on-chain-data-only proposal constraints.

## III - PMAR Role

PMAR is deterministic and oracle-free, with fixed immutable parameters in `constitution.md`.

## IV - Immutable Reference

See Immutable Parameters in `constitution.md`.
