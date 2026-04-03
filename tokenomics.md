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

AuMM is a **100% liquid token**. There is no locking, no staking, no ve-mechanism, no wrapper. You hold AuMM, you can sell it at any time.

**AuMM carries zero governance power.** It does not vote on emissions, fee parameters, or any protocol decision. All governance — including emission direction — is AuMT-weighted (active LP positions in qualified pools). AuMM is a pure reward and value-capture token: earned by LPs, burned by the protocol.

AuMM accrues value exclusively through **buyback and burn** — the same mechanism as a corporate stock buyback programme. Protocol revenue is used to buy AuMM on the open market and permanently burn it. Circulating supply declines over time. Each remaining token represents a larger share of future protocol revenue. No yield farming. No APR on holding. Just scarcity.

## x. Value Capture

### Fee Splits

| Stream | Destination | Share |
|--------|-------------|-------|
| Swap fees | LP bonus | 50% |
| Swap fees | AuMM buyback and burn | 25% |
| Swap fees | Treasury | 25% |
| ERC-4626 yield fee (10% skim) | AuMM buyback and burn | 25% |
| ERC-4626 yield fee (10% skim) | Treasury | 75% |

### The Day-One Revenue Guarantee

Because ERC-4626 pools generate yield fee revenue regardless of trading volume, the protocol has treasury income from the first block. This is not dependent on routing, aggregator integration, or TVL growth. It's architectural. Every dollar of yield-bearing tokens in any pool generates protocol revenue automatically. During the treasury emission phase (months 0–10), this revenue accumulates alongside AuMM emissions, building the capital needed to seed the AuMM trading pool at month 6, fund the price ceiling stabilization mechanism, and activate buyback-and-burn from month 6 onward.

### The Deflationary Crossover

At scale, the combined buyback-and-burn from swap fees (25%) and yield fees (25% of 10%) can exceed the emission rate — making AuMM net deflationary despite ongoing LP mining rewards. BTC scarcity with productive backing.

### Immutable Reference

See Immutable Parameters in `constitution.md`.
