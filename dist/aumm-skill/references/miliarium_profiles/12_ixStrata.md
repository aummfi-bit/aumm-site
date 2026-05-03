<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/12_ixStrata.md — DO NOT EDIT -->
# ixStrata — Slot 12

**Sector:** Crypto Infrastructure
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | LINK | 16% | ERC-20 | Chainlink — oracle infrastructure governance |
| Theme Asset B | AAVE | 16% | ERC-20 | Aave — lending protocol governance |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

## Profile

**Real-world analogue:** DeFi infrastructure index — like owning shares in the data providers and banks that underpin financial markets.

**Theme rationale:** LINK and AAVE represent the two most critical DeFi infrastructure layers: oracles (data feeds) and lending (capital markets). Both have deep external liquidity and consistent aggregator volume.

**Volume drivers:**
- LINK/AAVE trading pairs (high external volume on Uniswap/Sushiswap)
- DeFi governance token rebalancing
- Oracle narrative cycles (Chainlink CCIP, staking)
- Aave governance events and protocol upgrades

**Risk profile:**
- Governance token volatility (LINK, AAVE can swing 30%+ in a week)
- Higher IL risk than stablecoin-only pools
- Smart contract risk (Aave stataToken wrapper)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDC (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
