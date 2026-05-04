<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 miliarium_profiles/14_ixAurebit.md — DO NOT EDIT -->
# ixAurebit — Slot 14

**Sector:** Digital Gold / Bitcoin
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | GHO | 26% | ERC-4626 | Aave GHO stablecoin |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | WBTC | 16% | ERC-20 | Wrapped Bitcoin (BitGo custody) |
| Theme Asset B | cbBTC | 16% | ERC-20 | Coinbase Wrapped Bitcoin |

**ERC-4626 composition:** 52% (svZCHF + GHO)

## Profile

**Real-world analogue:** Bitcoin ETF — equivalent to holding BTC through a regulated custody wrapper, the digital store of value.

**Theme rationale:** WBTC and cbBTC are the two dominant wrapped Bitcoin tokens on Ethereum. Together they represent the primary on-chain access point for Bitcoin exposure. The dual-wrapper design captures arbitrage between issuers (BitGo vs Coinbase custody).

**Volume drivers:**
- Bitcoin price movements (highest-volume crypto asset globally)
- WBTC ↔ cbBTC arbitrage (different custodians, same underlying)
- BTC-to-stablecoin rotation during volatility
- Institutional Bitcoin allocation flows

**Risk profile:**
- Bitcoin price volatility (high — 50%+ drawdowns historically)
- Custodian risk (BitGo for WBTC, Coinbase for cbBTC)
- WBTC governance controversy (BitGo custody changes)
- Higher IL risk due to BTC/stablecoin divergence

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + GHO (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
