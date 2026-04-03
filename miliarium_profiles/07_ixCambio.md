# ixCambio — Slot 07

**Sector:** Routing Infrastructure
**Template:** Non-Standard (6-token FX hub)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Routing Anchor | ixEDEL | 20% | ERC-20 (DTF) | Cross-pool arbitrage routing (overweight vs standard 16%) |
| CHF Stable | svZCHF | 16% | ERC-4626 | Swiss Franc anchor — Frankencoin savings vault |
| EUR Stable A | st-EURA | 16% | ERC-20 | Staked EURA — Angle Protocol Euro stablecoin |
| EUR Stable B | aEURS | 16% | ERC-4626 | Aave-wrapped EURS (Stasis Euro) |
| GBP Stable | s-tGBP | 16% | ERC-20 | Staked tGBP — tokenised British Pound |
| USD Stable | sDAI | 16% | ERC-4626 | Maker/Sky savings DAI — USD stable yield |

**ERC-4626 composition:** 48% (svZCHF + aEURS + sDAI) — requires non-standard exemption from the 52% gate given its routing infrastructure role. See `bootstrap.md` §xxiii.

## Profile

**Real-world analogue:** FX trading desk — a multi-currency exchange spanning CHF, EUR, GBP, and USD, with yield-bearing positions in each currency.

**Theme rationale:** ixCambio is the protocol's **foreign exchange hub**. Four currencies (CHF, EUR, GBP, USD via ixEDEL basket) in a single pool — enabling on-chain FX trading that traditionally requires separate pairs on Curve or Uniswap. The pool directly competes with Curve's FXSwap (launched ZCHF/crvUSD at Stable Summit Cannes, March 2026) but captures multiple FX pairs from one LP position.

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
- sDAI smart contract risk (Maker/Sky DSR vault)
- Regulatory risk (FX stablecoin regulation varies by jurisdiction)
- Multi-currency IL (four currencies diverging creates complex IL dynamics)
- 4626 Quality Gate compliance requires monitoring (currently borderline)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | 48% ERC-4626 (svZCHF + aEURS + sDAI) — non-standard exemption for routing infrastructure |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see `constitution.md` §xxix |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see `bootstrap.md` §xxiv |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [CCB Multiplier](../theoretical_foundation.md)
