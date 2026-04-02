# ixVectura — Slot 19

**Sector:** Treasuries / Fixed Income
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | SGOVon | 16% | ERC-20 | Tokenised iShares 0-3 Month Treasury Bond ETF |
| Theme Asset B | TLTon | 16% | ERC-20 | Tokenised iShares 20+ Year Treasury Bond ETF |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

## Profile

**Real-world analogue:** Treasury bond barbell strategy — short-duration T-bills (SGOV) paired with long-duration bonds (TLT), the classic fixed income barbell.

**Theme rationale:** SGOVon represents the risk-free rate (0–3 month T-bills). TLTon represents long-duration treasuries (20+ years). The pairing creates natural yield curve arbitrage — when rates rise, SGOV outperforms TLT; when rates fall, TLT outperforms SGOV. LPs profit from the rebalancing.

**Volume drivers:**
- Fed rate decisions (FOMC meetings drive massive treasury repricing)
- Yield curve steepening/flattening trades
- Flight-to-safety flows (treasuries are the ultimate safe haven)
- Duration rotation (short → long or long → short based on rate expectations)
- 24/7 treasury trading (TradFi bond markets are relatively illiquid)

**Risk profile:**
- Interest rate risk (TLT has high duration — 20%+ drawdowns in rate hike cycles)
- SGOVon is near-zero volatility (T-bill equivalent)
- The barbell creates natural IL from duration spread divergence
- Tokenised equity counterparty risk

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDC (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Tag revocation | Permanent if gauge lost after 4 consecutive failed cycles |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
