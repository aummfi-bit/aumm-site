# ixHelvetia — Slot 01

**Sector:** Crypto Infrastructure
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | waEthUSDT | 16% | ERC-20 | Aave-wrapped USDT — stablecoin volume magnet |
| Theme Asset B | USDC | 16% | ERC-20 | Circle USDC — highest-volume stablecoin |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Stablecoin money market — equivalent to a high-liquidity USD/CHF cash management fund with DeFi infrastructure yield.

**Theme rationale:** waEthUSDT and USDC are the two highest-volume stablecoins on Ethereum. This pool is the primary on-ramp — any stablecoin holder can enter the Aureum ecosystem through ixHelvetia without taking directional exposure.

**Volume drivers:**
- Stablecoin routing (USDT ↔ USDC ↔ sUSDS ↔ svZCHF)
- DEX aggregator flow (1inch, CowSwap, Paraswap)
- CHF/USD forex arbitrage via svZCHF ↔ USDC spread
- ERC-4626 vault rate arbitrage between svZCHF and sUSDS

**Risk profile:**
- Stablecoin depeg risk (USDT, USDC)
- Aave wrapper risk (waEthUSDT smart contract)
- Low IL risk — all components are stablecoin-adjacent

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + sUSDS (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Pioneer Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
