<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/09_ixAltrix.md — DO NOT EDIT -->
# ixAltrix — Slot 09

**Sector:** US Fixed Income (high yield)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [Miliarium Aureum registry (Section xi)](../05_miliarium_aureum.md) (Section xi, slot 09).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | HYGon | 16% | ERC-20 | Tokenized HYG ETF |
| Theme Asset B | FLHYon | 16% | ERC-20 | Tokenized FLHY ETF |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

## Profile

**Real-world analogue:** High-yield corporate bond fund — the credit-risk sleeve of a fixed-income portfolio, capturing spread premium above Treasuries.

**Theme rationale:** HYGon (iShares iBoxx High Yield Corporate Bond ETF) and FLHYon (Franklin High Yield Corporate ETF) provide exposure to below-investment-grade US corporate debt. This is the risk-on end of the bond constellation, pairing with **ixBrevis** (cash-like) and **ixMediox** (aggregate + TIPS) for a complete credit spectrum.

**Volume drivers:**
- Credit spread widening/tightening events
- Risk-on/risk-off rotation (high yield correlates with equities)
- Duration rotation within the bond constellation (ixAltrix ↔ ixBrevis)
- Rate cut/hike narratives (high yield benefits from cuts)

**Risk profile:**
- Credit risk (high-yield bonds can lose 10–20% in spread widening events)
- Tokenised ETF issuer risk (counterparty, regulatory)
- Higher IL risk than ixBrevis (HY bonds are more volatile)
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
