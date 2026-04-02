# ixCasper — Slot 03

**Sector:** LST / Staking Derivatives
**Template:** Standard (52% / 16% / 32%) — Non-standard token assignment

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | fWSTETH | 26% | ERC-4626 | Flux Finance vault for Lido wstETH |
| Yield Core B | fWETH | 26% | ERC-4626 | Flux Finance vault for WETH |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | svZCHF | 16% | ERC-4626 | Frankencoin savings vault (appears as theme, not yield core) |
| Theme Asset B | waEthwstETH | 16% | ERC-4626 | Aave V3 stataToken wrapper for wstETH |

**ERC-4626 composition:** 84% (fWSTETH + fWETH + svZCHF + waEthwstETH) — significantly exceeds 52% threshold.

## Profile

**Real-world analogue:** Staking derivatives desk — concentrated exposure to ETH liquid staking yields through multiple lending protocols simultaneously.

**Theme rationale:** This is the protocol's deepest LST pool. The yield core uses Flux Finance vaults (fWSTETH, fWETH) for Lido/ETH lending yield. The theme assets add svZCHF (CHF anchor, also yield-bearing) and waEthwstETH (Aave wrapper for Lido wstETH). Four of five non-ixEDEL tokens are ERC-4626, making this the highest yield-density pool in the constellation.

**Non-standard notes:**
- svZCHF appears as a theme asset (16%) rather than its usual yield core position
- All four non-ixEDEL tokens are ERC-4626 yield-bearing (84% total)
- Yield core uses Flux Finance instead of Aave/Sky
- Dual wstETH exposure: fWSTETH (Flux) + waEthwstETH (Aave)

**Volume drivers:**
- LST arbitrage (fWSTETH ↔ waEthwstETH across lending protocols)
- Staking yield rate arbitrage (Flux vs Aave supply rates)
- ETH staking demand cycles
- wstETH/ETH peg monitoring and rebalancing

**Risk profile:**
- Lido smart contract risk (wstETH underlying)
- Flux Finance smart contract risk (newer lending protocol)
- ETH staking slashing risk
- Concentrated LST exposure (low diversification)
- Lower IL risk (all assets are ETH-correlated or stablecoin)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met with 84% ERC-4626 composition |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Miliarium Aureum Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors; requires 2/3 protocol-wide tessera-weighted vote; replacement must preserve same asset type or similar economic properties) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
