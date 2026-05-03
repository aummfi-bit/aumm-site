<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a miliarium_profiles/23_ixColossix.md — DO NOT EDIT -->
# ixColossix — Slot 23

**Subclass:** Financials  
**Sector:** US Equities (asset managers & banks)  
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [Miliarium Aureum registry (Section xi)](../05_miliarium_aureum.md) (Section xi, slot 23).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | BLKon | 16% | ERC-20 | Tokenized BLK ETF |
| Theme Asset B | BACon | 16% | ERC-20 | Tokenized BAC ETF |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Financials sector fund — concentrated exposure to the largest asset manager and a major US bank, like a two-stock financials ETF.

**Theme rationale:** BLKon (BlackRock) and BACon (Bank of America) represent the two pillars of traditional finance infrastructure — asset management and commercial banking. This pool pairs with **ixMoneta** (JPM/GS for investment banking) for broad financial sector coverage.

**Volume drivers:**
- Interest rate decision flows (financials are rate-sensitive)
- Earnings season volatility (quarterly bank results)
- Sector rotation between financials and tech
- Credit cycle narratives (loan growth, asset management AUM)

**Risk profile:**
- Financial sector systemic risk (banking crises, credit events)
- Single-name concentration risk (two stocks)
- Tokenised equity issuer risk (counterparty, regulatory)
- Rate sensitivity (rising rates boost bank margins but hurt bond portfolios)

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
