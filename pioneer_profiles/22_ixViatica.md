# ixViatica — Slot 22

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
| Theme Asset B | st-EURA | 16% | ERC-20 | Staked EURA (Angle Protocol Euro stablecoin) |

**ERC-4626 composition:** 52% (svZCHF + GHO)

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
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + GHO (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Tag revocation | Permanent if gauge lost after 4 consecutive failed cycles |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
