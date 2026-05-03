<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a miliarium_profiles/08_ixBrevis.md — DO NOT EDIT -->
# ixBrevis — Slot 08

**Sector:** US Fixed Income (short / ultra-short)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [Miliarium Aureum registry (Section xi)](../05_miliarium_aureum.md) (Section xi, slot 08).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | SGOVon | 16% | ERC-20 | Tokenized SGOV ETF |
| Theme Asset B | SHYon | 16% | ERC-20 | Tokenized SHY ETF |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

## Profile

**Real-world analogue:** Money market / short-duration bond fund — the cash-management sleeve of an institutional portfolio, holding T-bills and 1–3 year Treasuries.

**Theme rationale:** SGOVon (ultra-short US Treasury bills) and SHYon (1–3 year Treasuries) are the safest fixed-income exposures available on-chain. This pool anchors the bond constellation at the short end of the yield curve, paired with **ixAltrix** (high yield), **ixMediox** (aggregate + TIPS), and **ixLongus** (long Treasury).

**Volume drivers:**
- Rate decision flows (Fed funds rate directly impacts short-duration pricing)
- Flight-to-safety during equity sell-offs (short Treasuries are the first destination)
- Duration rotation within the bond constellation (ixBrevis ↔ ixLongus)
- Yield curve steepening/flattening trades

**Risk profile:**
- Very low duration risk (short-dated instruments)
- Tokenised ETF issuer risk (counterparty, regulatory)
- Minimal IL risk (short-duration bonds are quasi-stablecoins)
- Smart contract risk (Aave stataToken wrapper)

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

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md) | [Miliarium Aureum registry](../05_miliarium_aureum.md)
