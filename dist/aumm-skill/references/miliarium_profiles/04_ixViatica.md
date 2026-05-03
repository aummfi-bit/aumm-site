<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/04_ixViatica.md — DO NOT EDIT -->
# ixViatica — Slot 04

**Sector:** FX / Emerging Markets
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | GHO | 26% | ERC-4626 | Aave GHO stablecoin |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | fBRZ | 16% | ERC-20 | Flux Finance BRZ vault (Brazilian Real stablecoin) |
| Theme Asset B | st-EURA | 16% | ERC-4626 | Angle Savings (EURA yield; implementation `SavingsNameable` extends OpenZeppelin `ERC4626Upgradeable`) |

**ERC-4626 composition:** 68% (svZCHF 26% + GHO 26% + st-EURA 16%)

## Profile

**Real-world analogue:** Emerging market FX fund — exposure to Brazilian Real and Euro corridors, the on-chain forex desk for non-USD currencies.

**Theme rationale:** fBRZ provides access to the Brazilian Real (BRL) — one of the highest-volume emerging market currencies. st-EURA provides Euro exposure through Angle Protocol's staked Euro stablecoin. This pool captures FX demand that TradFi forex markets serve, but on-chain and 24/7.

**Volume drivers:**
- BRL/USD and EUR/USD forex flows (remittances, trade settlement)
- Brazilian crypto market demand (Brazil is a top-5 crypto market)
- Euro stablecoin demand (growing European DeFi market)
- CHF/EUR/BRL triangular arbitrage via svZCHF anchor
- Emerging market currency volatility events

**Risk profile:**
- BRL volatility (emerging market currency — can move 5%+ in a day)
- Euro stablecoin regulatory risk (MiCA compliance)
- Angle Protocol smart contract risk (st-EURA)
- Flux Finance smart contract risk (fBRZ wrapper)
- Higher IL risk due to FX pair divergence

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + GHO (26%) + st-EURA (16%) = 68% |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
