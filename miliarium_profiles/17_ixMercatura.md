# ixMercatura — Slot 17

**Sector:** Fintech / Brokers
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | COIN | 16% | ERC-20 | Coinbase Global Inc (native ERC-20) |
| Theme Asset B | HOOD | 16% | ERC-20 | Tokenised Robinhood Markets Inc |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Crypto-native fintech fund — exposure to the two companies that bridge traditional brokerage with crypto markets.

**Theme rationale:** Coinbase and Robinhood are the two most important retail-facing crypto/fintech platforms. COIN is a native ERC-20 (Coinbase is on-chain native). HOOD represents the retail trading revolution. Together they are the gateway between TradFi users and DeFi.

**Volume drivers:**
- Crypto market cycle correlation (COIN revenue = crypto trading volume)
- Retail trading sentiment (HOOD rises with retail participation)
- Regulatory clarity events (SEC actions on Coinbase drive massive volume)
- Crypto bull/bear cycle amplification (both are leveraged plays on crypto adoption)

**Risk profile:**
- Crypto market cycle risk (both companies' revenue is highly correlated with crypto volume)
- Regulatory risk (Coinbase SEC lawsuit, crypto regulation)
- Competition risk (new entrants, DEX growth reducing CEX relevance)
- High single-stock volatility
- Tokenised equity counterparty risk (HOOD; COIN is native ERC-20)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + sUSDS (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Miliarium Aureum Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors; requires 2/3 protocol-wide tessera-weighted vote; replacement must preserve same asset type or similar economic properties) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
