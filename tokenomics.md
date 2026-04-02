# Tokenomics

## ix. Token Design: AuMM (Aureum Market Maker)

### Supply Rules (Immutable from Block 0)

| Parameter | Value |
|-----------|-------|
| Token name | **AuMM** |
| Pool token | **AuMT** |
| Maximum supply | **21,000,000 AuMM** |
| Emission unit | Per-block reward |
| Halving interval | Every 10,512,000 blocks (~4 years) |
| Emission model | Bitcoin-style geometric halving |

### Emission Schedule

| Era | Years | Blocks per Era | Block Reward (AuMM) | Era Emission | Cumulative Supply | % of Total |
|-----|-------|----------------|---------------------|-------------|-------------------|------------|
| 0 | 0-4 | 10,512,000 | 1.00 | 10,512,000 | 10,512,000 | 50.06% |
| 1 | 4-8 | 10,512,000 | 0.50 | 5,256,000 | 15,768,000 | 75.09% |
| 2 | 8-12 | 10,512,000 | 0.25 | 2,628,000 | 18,396,000 | 87.60% |
| 3 | 12-16 | 10,512,000 | 0.125 | 1,314,000 | 19,710,000 | 93.86% |
| 4+ | ... | ... | halving continues | ... | approaches 21,000,000 | approaches 100% |

The old cycle-based emission table is removed. Emissions are specified only in per-block terms.

### Emission Distribution

- **Through end of Month 10 (Year 1):** emissions to the Miliarium tranche are split **equally** across the 28 pools (**1/28** each).
- **Months 11–12 (Year 1):** a **two-month linear transition** that blends each pool’s equal one-twenty-eighth share with its CCB-derived share, ramping linearly from pure equal at the start of Month 11 to pure CCB at the end of Year 1. At the midpoint, the mix is half equal and half CCB. See `constitution.md` and `formulas.md`.
- **After Year 1:** pure CCB weighting — each pool is scored by its smoothed TVL, MAMAR multiplier, and Incendiary multiplier, then normalized across all eligible pools. See `constitution.md` and `formulas.md`.
- No voting, no Bubble multipliers, and no discretionary overrides.

### Governance Clarification

Governance exists for non-emission actions only (gauge approvals/challenges, treasury proposals, fee proposals within immutable bounds). Emission allocation itself is never vote-controlled.

### Token Properties

- AuMM is liquid and carries zero governance power.
- AuMT is economic proof of active LP participation only.
- Value capture remains buyback-and-burn funded by protocol revenue.

## x. Value Capture

### Fee Splits

| Stream | Destination | Share |
|--------|-------------|-------|
| Swap fees | LP bonus | 50% |
| Swap fees | AuMM buyback and burn | 25% |
| Swap fees | Treasury | 25% |
| ERC-4626 yield fee (10% skim) | AuMM buyback and burn | 25% |
| ERC-4626 yield fee (10% skim) | Treasury | 75% |

### Immutable Reference

See Immutable Parameters in `constitution.md`.
