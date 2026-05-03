<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a miliarium_profiles/06_ixLibertas.md — DO NOT EDIT -->
# ixLibertas — Slot 06

**Sector:** Routing Infrastructure
**Template:** Non-Standard (7-token stablecoin hub — no ixEDEL)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| USD Stable 1 | scrvUSD | 15% | ERC-4626 | Curve savings vault for crvUSD |
| USD Stable 2 | PYUSD | 15% | ERC-20 | PayPal USD stablecoin |
| USD Stable 3 | GHO | 14% | ERC-4626 | Aave GHO stablecoin |
| USD Stable 4 | sUSDS | 14% | ERC-4626 | Sky savings rate vault |
| USD Stable 5 | sfrxUSD | 14% | ERC-4626 | Frax savings vault |
| USD Stable 6 | USDT | 14% | ERC-20 | Tether USD |
| USD Stable 7 | USDC | 14% | ERC-20 | Circle USD Coin |

**No ixEDEL.** **ixHelvetia** (slot 01) also omits ixEDEL; here the absence is intentional for a pure seven-token USD hub.

**ERC-4626 composition:** 57% (scrvUSD + GHO + sUSDS + sfrxUSD) — exceeds 52% threshold.

## Profile

**Real-world analogue:** Money market fund — a deep, diversified USD liquidity pool spanning seven issuers, like a prime money market fund that holds T-bills from multiple sources.

**Theme rationale:** ixLibertas is the protocol's **universal USD on-ramp**. Seven stablecoins — covering every major issuer (Tether, Circle, PayPal, Aave, Sky, Frax, Curve) — in a single pool. Any USD stablecoin holder can enter Aureum through this pool with minimal slippage. The absence of ixEDEL is intentional: this pool serves as a standalone deep-liquidity venue, not a routing node.

**Structural role:**
- Universal USD entry point (any of 7 stablecoins)
- Stablecoin-to-stablecoin swap venue (largest on-chain stable swap pool)
- Yield aggregation across four ERC-4626 vaults simultaneously
- Backup routing path when ixEDEL pools are congested

**Volume drivers:**
- Stablecoin swaps (USDT ↔ USDC ↔ PYUSD ↔ GHO ↔ sUSDS ↔ sfrxUSD ↔ scrvUSD)
- Aggregator routing for stablecoin pairs
- Yield rate arbitrage between savings vaults (sUSDS vs sfrxUSD vs scrvUSD vs GHO)
- Stablecoin depeg events (massive volume during stress)

**Risk profile:**
- Stablecoin systemic risk (7 issuers diversify but don't eliminate)
- Individual depeg risk (USDT, PYUSD, algorithmic/collateral models)
- Smart contract risk across 4 different vault implementations
- Very low IL risk (all assets are USD-pegged)
- No ixEDEL exposure (no routing anchor risk, but also no DTF diversification)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by scrvUSD (15%) + GHO (14%) + sUSDS (14%) + sfrxUSD (14%) = 57% |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
