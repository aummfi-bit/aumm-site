# ixMagnix — Slot 20

**Sector:** US Equities (Mega Cap Tech)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sfrxUSD | 26% | ERC-4626 | Frax savings vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | MSFTon | 16% | ERC-20 | Tokenised Microsoft Corp |
| Theme Asset B | AAPLon | 16% | ERC-20 | Tokenised Apple Inc |

**ERC-4626 composition:** 52% (svZCHF + sfrxUSD)

## Profile

**Real-world analogue:** Blue-chip tech stock pair — the two largest companies by market cap, representing stable mega-cap tech exposure with lower volatility than NVDA/TSLA.

**Theme rationale:** Microsoft and Apple are the world's two most valuable companies. Unlike the NVDA/TSLA pair in ixGigantus, MSFT/AAPL offer lower-volatility, dividend-paying mega-cap exposure. This is the "quality tech" pool — defensive within the equity sector.

**Volume drivers:**
- Earnings cycles (MSFT and AAPL report quarterly, driving volume)
- Dividend flows (both pay dividends — tokenised dividend capture)
- 24/7 trading demand for the world's most held stocks
- Institutional rebalancing (MSFT/AAPL are top holdings in most portfolios)

**Risk profile:**
- Lower volatility than ixGigantus (MSFT/AAPL are more stable)
- Still single-stock concentration risk (two names)
- Tokenised equity counterparty risk
- Moderate IL risk (less volatile than NVDA/TSLA but still equity vs stablecoin)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + sfrxUSD (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Miliarium Aureum Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors; requires 2/3 protocol-wide tessera-weighted vote; replacement must preserve same asset type or similar economic properties) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [CCB Multiplier](../theoretical_foundation.md)
