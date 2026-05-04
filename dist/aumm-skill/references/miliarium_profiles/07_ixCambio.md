<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 miliarium_profiles/07_ixCambio.md — DO NOT EDIT -->
# ixCambio — Slot 07

**Sector:** Routing Infrastructure
**Template:** Non-Standard (6-token FX hub, 4626-heavy)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core / CHF anchor | svZCHF | 19% | ERC-4626 | Frankencoin savings vault — primary routing rail |
| 4626 EUR yield core | st-EURA | 18% | ERC-4626 | Angle Savings (EURA yield; implementation `SavingsNameable` extends OpenZeppelin `ERC4626Upgradeable`) |
| 4626 EUR yield core | aEURS | 18% | ERC-4626 | Aave V3 stataToken wrapper for Stasis EURS |
| Routing Anchor | ixEDEL | 15% | ERC-20 (Reserve DTF) | Cross-pool arbitrage routing (standard 15% connector weight) |
| GBP leg | tGBP | 15% | ERC-20 | Tokenised GBP stablecoin (no 4626 wrapper available at deployment time; if one appears, composition challenge can swap it in) |
| JPY leg | JPYC | 15% | ERC-20 | Regulated JPY stablecoin (JPYC Inc., Japan PSA-licensed; backed 1:1 by JGBs and bank deposits) |

**ERC-4626 composition:** 55% (svZCHF 19% + st-EURA 18% + aEURS 18%) — exceeds immutable 52% Quality Gate floor by 3 points.

## Profile

**Real-world analogue:** FX trading desk — a multi-currency exchange spanning CHF, EUR, GBP, USD, and JPY, with yield-bearing positions in CHF and EUR.

**Theme rationale:** ixCambio is the protocol's **global foreign exchange hub**. Five currencies (CHF, EUR, GBP, USD via ixEDEL basket, and JPY) in a single pool — enabling on-chain FX trading that traditionally requires separate pairs on Curve or Uniswap. JPYC is the first regulated Asian stablecoin in the Miliarium constellation, making ixCambio a true global FX venue rather than a Western-only hub. The pool directly competes with Curve's FXSwap (launched ZCHF/crvUSD at Stable Summit Cannes, March 2026) but captures multiple FX pairs from one LP position.

**Structural role:**
- Multi-currency FX routing (CHF ↔ EUR ↔ GBP ↔ USD ↔ JPY in one hop)
- Global DeFi gateway (EUR, GBP, CHF, JPY access)
- Yield on FX positions (svZCHF, st-EURA, aEURS are yield-bearing ERC-4626)
- ixEDEL routing with FX exposure
- First regulated Asian stablecoin integration (JPYC)

**Volume drivers:**
- EUR/USD, USD/JPY, CHF/EUR, GBP/USD forex flows
- European + Japanese stablecoin adoption (MiCA-compliant stablecoins, JPYC PSA-compliant)
- Cross-border remittances (EUR → CHF, GBP → EUR, USD → JPY)
- FX rate volatility events (ECB, SNB, BoE, BoJ rate decisions)
- Curve FXSwap competitive routing

**Risk profile:**
- FX volatility (EUR, GBP, CHF, JPY can move 2%+ on central bank decisions)
- JPYC regulatory risk (PSA-licensed, Japan-specific compliance)
- Regulatory risk across multiple jurisdictions (FX stablecoin regulation varies)
- Multi-currency IL (five currencies diverging creates complex IL dynamics)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (19%) + st-EURA (18%) + aEURS (18%) = 55% |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (specified-pool model, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role). The old pool persists with the fee-routing hook attached — see [Constitution (§xxvii)](10_constitution.md) and [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
