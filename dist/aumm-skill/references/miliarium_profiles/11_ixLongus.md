<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a miliarium_profiles/11_ixLongus.md — DO NOT EDIT -->
# ixLongus — Slot 11

**Sector:** US Fixed Income (long Treasury)
**Template:** Non-standard (single theme at 32%)

---

## Composition

Binding weights are in [Miliarium Aureum registry (Section xi)](../05_miliarium_aureum.md) (Section xi, slot 11).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme (long Treasury) | TLTon | **32%** | ERC-20 | Tokenized TLT (iShares 20+ Year Treasury Bond ETF) |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

**Non-standard notes:**
- Single theme asset at **32%** instead of two 16% theme tokens — full slot allocated to long-duration Treasury exposure
- Paired with **ixBrevis** (slot 08, short/ultra-short bonds) and **ixMediox** (slot 10, intermediate bonds) to span the full US yield curve within the Miliarium constellation

## Profile

**Real-world analogue:** Long-duration Treasury fund — equivalent to holding TLT or a 20+ year government bond position, with maximum duration sensitivity.

**Theme rationale:** TLTon tokenizes the iShares 20+ Year Treasury Bond ETF, providing on-chain access to the longest-duration segment of the US government bond market. A single 32% theme allocation concentrates the duration bet — when rates fall, ixLongus outperforms ixBrevis and ixMediox by a wide margin; when rates rise, it suffers the most. This asymmetry is intentional: it gives LPs and aggregator traders a clean instrument for duration-positioning on-chain.

**Volume drivers:**
- Interest rate expectations (Fed rate decisions, CPI prints, employment data)
- Duration rotation (long vs short bond trades during rate cycle turns)
- Flight to safety (Treasury demand spikes during equity sell-offs)
- Cross-pool arbitrage with ixBrevis (slot 08) and ixMediox (slot 10) — the three bond pools form a yield-curve trade surface

**Risk profile:**
- High duration risk (20+ year Treasuries can move 15–25% on rate cycles)
- TLTon tokenization risk (issuer, oracle, redemption mechanics)
- Inverse correlation with equities may reduce IL during stock sell-offs but amplify it during rate rises
- Single-theme concentration (no diversification within the theme sleeve)

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
