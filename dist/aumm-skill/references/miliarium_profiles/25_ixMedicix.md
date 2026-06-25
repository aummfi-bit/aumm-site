<!-- GENERATED FROM aumm-site@cbf2f197c4e40a6398aea53483cefc9311cea393 miliarium_profiles/25_ixMedicix.md — DO NOT EDIT -->
# ixMedicix — Slot 25

**Subclass:** Healthcare  
**Sector:** US Equities (pharma / healthcare)  
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [Miliarium Aureum registry (Section xi)](../05_miliarium_aureum.md) (Section xi, slot 25).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | JNJon | 16% | ERC-20 | Tokenized JNJ ETF |
| Theme Asset B | ABBVon | 16% | ERC-20 | Tokenized ABBV ETF |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Diversified pharma fund — established healthcare blue-chips with strong dividend histories, like the defensive sleeve of a balanced equity portfolio.

**Theme rationale:** JNJon (Johnson & Johnson) and ABBVon (AbbVie) are diversified pharma giants with defensive characteristics — stable revenue, high dividends, low beta vs the broad market. This pool pairs with **ixVitalix** (LLY/NVO for growth pharma) for full healthcare sector coverage.

**Volume drivers:**
- Healthcare sector rotation (defensive during risk-off, lagging during risk-on)
- Drug pipeline and FDA approval events
- Dividend and quality narratives (JNJ and ABBV are classic dividend aristocrats)
- Cross-venue arbitrage vs TradFi listings

**Risk profile:**
- Drug pipeline risk (patent cliffs, FDA rejections)
- Single-name concentration risk (two stocks)
- Tokenised equity issuer risk (counterparty, regulatory)
- Lower volatility than tech pools but higher than bond pools

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% (admitted vault classes) — met by svZCHF (26%) + sUSDS (26%) |
| Vault-Class Registry | All ERC-4626 tokens admitted at genesis (per [Bootstrap §xxiv-a](08_bootstrap.md)) |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (auto-registration via `registerGaugeFromComposition(pool)`, governance-only — no permissionless-activation check, optional 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md) | [Miliarium Aureum registry](../05_miliarium_aureum.md)
