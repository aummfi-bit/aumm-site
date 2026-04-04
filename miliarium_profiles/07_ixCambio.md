# ixCambio — Slot 07

**Sector:** Routing Infrastructure
**Template:** Non-Standard (6-token FX hub)

---

## Composition

| Component | Token | Weight | Role |
|:----------|:------|:-------|:-----|
| ixEDEL | 20% | ERC-20 (DTF) | Cross-pool arbitrage routing (overweight vs standard 16%) |
| svZCHF | 16% | ERC-4626 | Swiss Franc anchor — Frankencoin savings vault |
| st-EURA | 16% | ERC-20 | Staked EURA — Angle Protocol Euro stablecoin |
| aEURS | 16% | ERC-4626 | Aave-wrapped EURS (Stasis Euro) |
| s-tGBP | 16% | ERC-20 | Staked tGBP — tokenised British Pound |
| [Partner Stable] | 16% | TBD | Reserved slot for strategic partner stablecoin |

**ERC-4626 composition:** 32% minimum (svZCHF + aEURS) — may require Partner Stable to be ERC-4626 to meet 52% gate, or may qualify under a non-standard exemption given its routing infrastructure role.

## Profile

**Real-world analogue:** FX trading desk — a multi-currency exchange spanning CHF, EUR, GBP, and USD, with yield-bearing positions in each currency.

**Theme rationale:** ixCambio is the protocol's **foreign exchange hub**. Four currencies (CHF, EUR, GBP, and USD via ixEDEL basket) in a single pool — enabling on-chain FX trading that traditionally requires separate pairs on Curve or Uniswap. The pool directly competes with Curve's FXSwap (launched ZCHF/crvUSD at Stable Summit Cannes, March 2026) but captures multiple FX pairs from one LP position.

**Structural role:**
- Multi-currency FX routing (CHF ↔ EUR ↔ GBP ↔ USD in one hop)
- European DeFi gateway (EUR, GBP, CHF access)
- Yield on FX positions (svZCHF, aEURS are yield-bearing)
- ixEDEL routing with FX exposure

**Volume drivers:**
- EUR/USD, CHF/EUR, GBP/USD forex flows
- European stablecoin adoption (MiCA-compliant stablecoins)
- Cross-border remittances (EUR → CHF, GBP → EUR)
- FX rate volatility events (ECB, SNB, BoE rate decisions)
- Curve FXSwap competitive routing

**Risk profile:**
- FX volatility (EUR, GBP, CHF can move 2%+ on central bank decisions)
- Partner Stable risk (TBD — depends on final selection)
- Regulatory risk (FX stablecoin regulation varies by jurisdiction)
- Multi-currency IL (four currencies diverging creates complex IL dynamics)
- 4626 Quality Gate compliance requires monitoring (currently borderline)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | Monitoring required — 32% confirmed ERC-4626; Partner Stable selection critical |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
