# ixEcosysthema — Slot 08

**Sector:** DeFi Ecosystem
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDT | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDT |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | FRAX | 16% | ERC-20 | Frax Finance stablecoin/governance |
| Theme Asset B | CHEX | 16% | ERC-20 | Chintai exchange token |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDT)

## Profile

**Real-world analogue:** DeFi ecosystem basket — exposure to stablecoin innovation (Frax) and real-world asset tokenisation infrastructure (Chintai).

**Theme rationale:** FRAX represents Frax Finance's ecosystem (frxETH, sfrxETH, sfrxUSD) — one of the most innovative stablecoin protocols. CHEX represents Chintai, a regulated exchange focused on tokenised real-world assets. Together they bridge DeFi yield innovation with RWA infrastructure.

**Volume drivers:**
- Frax ecosystem activity (sfrxETH staking, sfrxUSD savings rate)
- FRAX governance and tokenomics events
- CHEX exchange token demand
- RWA tokenisation narrative

**Risk profile:**
- Frax algorithmic stablecoin risk (partially collateralised history)
- CHEX lower liquidity (smaller market cap)
- Ecosystem concentration risk
- Regulatory risk (RWA tokenisation regulatory clarity)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDT (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| PMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Miliarium Aureum Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors; requires 2/3 protocol-wide tessera-weighted vote; replacement must preserve same asset type or similar economic properties) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [PMAR](../PMAR.md)
