# ixCustodia — Slot 20

**Sector:** Gold / Inflation Protection
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDT | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDT |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | GLDon | 16% | ERC-20 | Tokenised SPDR Gold Shares ETF |
| Theme Asset B | TIPon | 16% | ERC-20 | Tokenised iShares TIPS Bond ETF |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDT)

## Profile

**Real-world analogue:** Inflation hedge basket — gold ETF plus Treasury Inflation-Protected Securities, the two primary inflation protection instruments.

**Theme rationale:** GLDon (gold ETF) and TIPon (TIPS bonds) are the two most common inflation hedges in TradFi portfolios. Gold protects against monetary debasement. TIPS protect against CPI inflation. Together they form a comprehensive inflation protection basket.

**Volume drivers:**
- Inflation data releases (CPI, PPI, PCE reports)
- Fed policy announcements (rate decisions, QE/QT)
- Geopolitical risk events (gold demand spikes)
- Real yield movements (TIPS reprice on real yield changes)
- Gold ↔ TIPS rotation based on inflation expectations

**Risk profile:**
- Gold price volatility (moderate — lower than equities)
- TIPS interest rate sensitivity (duration risk)
- Inflation expectation risk (if inflation falls, both underperform)
- Tokenised ETF counterparty risk
- Lower IL risk than equity pools (both assets are relatively stable)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDT (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Tag revocation | Permanent if gauge lost after 4 consecutive failed cycles |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
