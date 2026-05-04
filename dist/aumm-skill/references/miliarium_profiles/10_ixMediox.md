<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 miliarium_profiles/10_ixMediox.md — DO NOT EDIT -->
# ixMediox — Slot 10

**Sector:** US Fixed Income (aggregate + TIPS)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [Miliarium Aureum registry (Section xi)](../05_miliarium_aureum.md) (Section xi, slot 10).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | AGGon | 16% | ERC-20 | Tokenized AGG ETF |
| Theme Asset B | TIPon | 16% | ERC-20 | Tokenized TIP ETF |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

## Profile

**Real-world analogue:** Core bond fund with inflation protection — the balanced centre of a fixed-income allocation, combining investment-grade aggregate with TIPS.

**Theme rationale:** AGGon (iShares Core US Aggregate Bond ETF) and TIPon (iShares TIPS Bond ETF) pair broad investment-grade credit with inflation-linked Treasuries. This is the structural middle of the bond constellation: more duration than **ixBrevis**, less credit risk than **ixAltrix**, and shorter than **ixLongus**.

**Volume drivers:**
- Inflation data releases (CPI, PCE directly affect TIPS pricing)
- Duration rotation within the bond constellation
- Real yield arbitrage (TIPS breakeven vs nominal rates)
- Macro regime shifts (reflation → TIPS, disinflation → AGG)

**Risk profile:**
- Moderate duration risk (aggregate includes intermediate-to-long bonds)
- Inflation surprise risk (TIPS outperform during unexpected inflation, underperform during disinflation)
- Tokenised ETF issuer risk (counterparty, regulatory)
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
