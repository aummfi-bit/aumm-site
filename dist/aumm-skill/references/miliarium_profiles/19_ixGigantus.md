<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/19_ixGigantus.md — DO NOT EDIT -->
# ixGigantus — Slot 19

**Sector:** US Equities (Mega Cap Tech)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDT | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDT |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | NVDAon | 16% | ERC-20 | Tokenised NVIDIA Corp |
| Theme Asset B | TSLAon | 16% | ERC-20 | Tokenised Tesla Inc |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDT)

## Profile

**Real-world analogue:** Mega-cap tech stock pair — concentrated exposure to the two most volatile and traded mega-cap names: the AI chip leader and the EV/energy leader.

**Theme rationale:** NVIDIA and Tesla are the highest-volume single stocks in US markets. Both drive massive retail and institutional trading. On-chain, they attract 24/7 speculative and hedging demand that TradFi can't serve outside market hours.

**Volume drivers:**
- Earnings volatility (NVDA and TSLA both move 10%+ on earnings)
- AI narrative cycles (NVIDIA = the picks-and-shovels play)
- Tesla news flow (Elon Musk, EV demand, energy storage)
- After-hours and weekend trading demand
- NVDAon ↔ TSLAon sector rotation within tech

**Risk profile:**
- Extreme single-stock volatility (both can move 20%+ in a week)
- High IL risk (large divergence between theme assets and stablecoin yield core)
- Concentration risk (two names, not an index)
- Tokenised equity counterparty risk

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDT (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
