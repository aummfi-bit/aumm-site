<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/27_ixAurix.md — DO NOT EDIT -->
# ixAurix — Slot 27

**Sector:** Gold / Commodities
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sfrxUSD | 26% | ERC-4626 | Frax savings vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | PAXG | 16% | ERC-20 | Paxos Gold — 1:1 physical gold backing |
| Theme Asset B | XAUt | 16% | ERC-20 | Tether Gold — 1:1 physical gold backing |

**ERC-4626 composition:** 52% (svZCHF + sfrxUSD)

## Profile

**Real-world analogue:** Physical gold fund — equivalent to holding allocated gold bars in a vault, tokenised for 24/7 trading.

**Theme rationale:** PAXG and XAUt are the two largest tokenised gold instruments on Ethereum. Both are backed 1:1 by physical gold in custody. This slot is **physical gold only** — no silver (tokenised silver and uranium ETF exposure is **ixMetallum**, slot 28).

This pool captures the on-chain gold market and provides a flight-to-safety destination within the protocol.

**Volume drivers:**
- Gold price volatility (geopolitical events, inflation fears)
- PAXG ↔ XAUt arbitrage (two issuers, same underlying)
- Flight-to-safety flows during crypto drawdowns
- Gold-to-stablecoin rotation during risk-on periods

**Risk profile:**
- Gold price volatility (moderate — gold is relatively stable vs equities)
- Custodian risk (Paxos, Tether custody of physical gold)
- Redemption risk (both tokens are redeemable for physical, creating arbitrage floors)
- Low smart contract risk (simple ERC-20 transfers)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + sfrxUSD (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
