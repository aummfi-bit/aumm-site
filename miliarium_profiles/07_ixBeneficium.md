# ixBeneficium — Slot 07

**Sector:** DeFi Ecosystem
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | ENA | 16% | ERC-20 | Ethena governance token |
| Theme Asset B | sUSDe | 16% | ERC-20 | Ethena staked USDe (yield-bearing synthetic dollar) |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDC)

## Profile

**Real-world analogue:** Synthetic dollar fund — exposure to Ethena's delta-neutral yield strategy, the fastest-growing stablecoin primitive.

**Theme rationale:** ENA and sUSDe represent Ethena, which generates yield through basis trading (long spot ETH + short perp). sUSDe is the yield-bearing staked version of USDe. This pool captures one of DeFi's highest-yield stablecoin strategies.

**Volume drivers:**
- Ethena yield farming and sUSDe staking flows
- ENA governance token trading (high speculative interest)
- sUSDe ↔ USDe arbitrage
- Basis trade yield fluctuations driving rebalancing

**Risk profile:**
- Ethena delta-neutral strategy risk (funding rate reversal)
- sUSDe depeg risk during negative funding periods
- High ENA volatility (governance/speculative token)
- Counterparty risk (centralised exchange funding rate exposure)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDC (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Miliarium Aureum Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors; requires 2/3 protocol-wide tessera-weighted vote; replacement must preserve same asset type or similar economic properties) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
