# ixImperium — Slot 09

**Sector:** DeFi Ecosystem
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | GHO | 26% | ERC-4626 | Aave GHO stablecoin |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | PENDLE | 16% | ERC-20 | Pendle Finance — yield tokenisation governance |
| Theme Asset B | EIGEN | 16% | ERC-20 | EigenLayer — restaking governance |

**ERC-4626 composition:** 52% (svZCHF + GHO)

## Profile

**Real-world analogue:** DeFi yield infrastructure index — like owning shares in the yield curve and the security market simultaneously.

**Theme rationale:** PENDLE and EIGEN represent DeFi's two most important yield infrastructure primitives. Pendle tokenises future yield (creating fixed/variable rate markets). EigenLayer extends Ethereum security to new protocols (restaking). Both are critical yield-bearing infrastructure.

**Volume drivers:**
- Pendle yield market expiries and rollovers (high-volume events)
- EIGEN restaking narrative and AVS launches
- Yield strategy rebalancing (fixed vs variable rate shifts)
- Both tokens have deep aggregator routing on Uniswap

**Risk profile:**
- High governance token volatility (PENDLE, EIGEN)
- Pendle smart contract complexity (yield tokenisation)
- EigenLayer slashing risk (restaking penalties)
- Narrative-driven demand (both tokens are momentum-sensitive)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + GHO (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Tag revocation | Permanent if gauge lost after 4 consecutive failed cycles |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
