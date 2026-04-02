# ixMoneta — Slot 16

**Sector:** Banking / Financials
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | GHO | 26% | ERC-4626 | Aave GHO stablecoin |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | JPMon | 16% | ERC-20 | Tokenised JPMorgan Chase & Co |
| Theme Asset B | GSon | 16% | ERC-20 | Tokenised Goldman Sachs Group Inc |

**ERC-4626 composition:** 52% (svZCHF + GHO)

## Profile

**Real-world analogue:** Bank stock fund — concentrated exposure to the two most important US financial institutions, the pillars of traditional banking.

**Theme rationale:** JPMorgan and Goldman Sachs are the two most systemically important US banks. JPM represents commercial + investment banking. GS represents pure investment banking and trading. Together they are the banking sector bellwether — when financials move, JPM and GS lead.

**Volume drivers:**
- Interest rate cycle sensitivity (banks are the most rate-sensitive sector)
- Quarterly earnings (JPM reports first among banks, sets the tone)
- Fed policy announcements driving bank stock repricing
- 24/7 financial sector trading demand

**Risk profile:**
- Interest rate risk (banks suffer when yield curve inverts)
- Regulatory risk (banking regulation, capital requirements)
- Credit cycle risk (loan loss provisions during recessions)
- Tokenised equity counterparty risk
- Moderate IL risk

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
