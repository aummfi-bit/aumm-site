<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/21_ixNubix.md — DO NOT EDIT -->
# ixNubix — Slot 21

**Subclass:** Mega-cap tech  
**Sector:** US Equities (consumer internet)  
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [Miliarium Aureum registry (Section xi)](../05_miliarium_aureum.md) (Section xi, slot 21).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | GOOGLon | 16% | ERC-20 | Tokenized GOOGL ETF |
| Theme Asset B | AMZNon | 16% | ERC-20 | Tokenized AMZN ETF |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Consumer internet ETF — concentrated exposure to the two dominant platforms in search and e-commerce, like a focused mega-cap tech holding.

**Theme rationale:** GOOGLon (Alphabet) and AMZNon (Amazon) represent the consumer internet duopoly — advertising and cloud (Google) plus e-commerce and cloud (Amazon). This pool complements **ixGigantus** (NVDA/TSLA hardware) and **ixMagnix** (MSFT/AAPL software) for full mega-cap tech coverage.

**Volume drivers:**
- 24/7 single-name equity trading demand
- Earnings season volatility (GOOGL and AMZN report quarterly)
- Cross-venue arbitrage vs TradFi listings
- Sector rotation between tech sub-themes (hardware → software → internet)

**Risk profile:**
- Single-name concentration risk (two stocks, not a diversified index)
- US tech regulatory risk (antitrust, AI regulation)
- Tokenised equity issuer risk (counterparty, regulatory)
- Higher IL risk than broad index pools (single names are more volatile)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + sUSDS (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md) | [Miliarium Aureum registry](../05_miliarium_aureum.md)
