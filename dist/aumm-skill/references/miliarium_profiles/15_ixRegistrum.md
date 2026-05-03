<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/15_ixRegistrum.md — DO NOT EDIT -->
# ixRegistrum — Slot 15

**Sector:** DeFi Ecosystem
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | ETHPLUS | 16% | ERC-20 | Reserve Protocol ETH+ (yield-bearing ETH basket) |
| Theme Asset B | OPEN | 16% | ERC-20 | Reserve Protocol governance token |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Ecosystem ETF — exposure to the Reserve Protocol stack, a diversified tokenised fund issuer.

**Theme rationale:** ETHPLUS is a Reserve Protocol DTF (Diversified Tokenised Fund) providing diversified yield-bearing ETH exposure. OPEN is the Reserve Protocol governance token. This pool consolidates the Sagix/Reserve ecosystem within Aureum.

**Volume drivers:**
- Reserve Protocol ecosystem growth and DTF adoption
- ETHPLUS rebalancing and arbitrage
- OPEN governance token demand
- Cross-pollination with ixEDEL (also a Reserve Protocol DTF)

**Risk profile:**
- Reserve Protocol smart contract risk
- DTF basket composition risk (ETHPLUS underlying assets)
- Governance token volatility (OPEN)
- Ecosystem concentration risk

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

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
