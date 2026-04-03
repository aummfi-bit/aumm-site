# ixAetheron — Slot 02

**Sector:** ETH Staking
**Template:** Non-Standard (54% / 15% / 31%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | waEthrETH | 27% | ERC-4626 | Aave V3 stataToken wrapper for Rocket Pool rETH |
| Yield Core B | waEthweETH | 27% | ERC-4626 | Aave V3 stataToken wrapper for EtherFi weETH |
| Routing Anchor | ixEDEL | 15% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | RPL | 15% | ERC-20 | Rocket Pool governance token |
| Theme Asset B | ETHFI | 16% | ERC-20 | EtherFi governance token |

**ERC-4626 composition:** 54% (waEthrETH + waEthweETH) — exceeds 52% threshold.

## Profile

**Real-world analogue:** Staking infrastructure fund — like owning shares in the clearing houses and custodians that settle transactions.

**Theme rationale:** This pool uses an **ETH-native** yield core (no svZCHF): waEthrETH and waEthweETH are Aave V3 stataToken wrappers that earn both staking yield AND Aave lending yield simultaneously. RPL and ETHFI provide governance exposure to the two largest non-Lido staking protocols.

**Non-standard notes:**
- No svZCHF in the yield core — **ixCasper** (slot 03) also uses non–Frankencoin yield cores (Flux LST vaults); here the pair is specifically rETH/weETH **Aave stataTokens**
- Yield core generates dual yield: ETH staking rewards + Aave V3 supply rate
- Slightly higher ERC-4626 composition (54%) due to rounding of non-standard weights

**Volume drivers:**
- LST rebalancing (rETH ↔ weETH rotation)
- Staking governance token demand (RPL, ETHFI)
- ETH staking yield arbitrage between protocols
- Aave stataToken wrapping/unwrapping flows

**Risk profile:**
- ETH staking slashing risk (underlying rETH, weETH validators)
- Aave V3 stataToken smart contract risk (wrapper layer)
- RPL tokenomics risk (Rocket Pool bond requirements)
- Higher IL risk (ETH-denominated yield core vs ERC-20 theme assets)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by waEthrETH (27%) + waEthweETH (27%) = 54% |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Miliarium Aureum Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors; requires 2/3 protocol-wide tessera-weighted vote; replacement must preserve same asset type or similar economic properties) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [CCB Multiplier](../theoretical_foundation.md)
