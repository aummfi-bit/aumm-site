<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 miliarium_profiles/13_ixForum.md — DO NOT EDIT -->
# ixForum — Slot 13

**Sector:** Crypto Infrastructure
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDT | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDT |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | SKY | 16% | ERC-20 | Sky (formerly MakerDAO) — stablecoin governance |
| Theme Asset B | LDO | 16% | ERC-20 | Lido — liquid staking governance |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDT)

## Profile

**Real-world analogue:** DeFi governance blue-chips — like owning shares in the central bank (Sky/Maker) and the largest custodian (Lido) of the crypto economy.

**Theme rationale:** SKY governs the largest decentralised stablecoin system (DAI/USDS). LDO governs the largest liquid staking protocol (stETH). Together they represent DeFi's two most systemically important governance tokens.

**Volume drivers:**
- SKY/LDO trading pairs (consistent aggregator volume)
- MakerDAO → Sky rebrand narrative
- Lido staking dominance debates and governance events
- Stablecoin policy changes (DSR adjustments drive SKY demand)

**Risk profile:**
- Governance token volatility
- Regulatory risk (Sky/Maker faces stablecoin regulation scrutiny)
- Lido market share risk (potential regulatory pressure on staking dominance)

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
