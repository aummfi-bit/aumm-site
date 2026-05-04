<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 miliarium_profiles/18_ixInnovix.md — DO NOT EDIT -->
# ixInnovix — Slot 18

**Sector:** US Equities (Tech Index)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | QQQon | 16% | ERC-20 | Tokenised Invesco QQQ Trust (Nasdaq-100) |
| Theme Asset B | QQQX | 16% | ERC-20 | Tokenised Nuveen Nasdaq 100 Dynamic Overwrite (covered call) |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

## Profile

**Real-world analogue:** Nasdaq-100 index fund with income overlay — tech-heavy US equity exposure plus a covered call income strategy.

**Theme rationale:** QQQon tracks the Nasdaq-100 (tech-heavy). QQQX is a covered call variant that sells options on the same index for income. The pairing captures both directional tech exposure and yield-enhanced tech exposure — LPs get natural arbitrage between the two strategies.

**Volume drivers:**
- Tech sector earnings cycles (FAANG reporting drives volatility)
- QQQon ↔ QQQX strategy arbitrage (growth vs income)
- 24/7 Nasdaq-100 price discovery
- Risk-on capital allocation (tech is the first sector to rally)

**Risk profile:**
- Tech sector concentration risk (top 10 holdings = ~50% of index)
- Higher volatility than S&P 500 (tech-heavy = higher beta)
- Tokenised equity issuer risk
- QQQX covered call strategy may underperform in strong bull markets

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDC (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
