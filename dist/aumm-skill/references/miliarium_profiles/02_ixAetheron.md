<!-- GENERATED FROM aumm-site@5bd962473c7d8fa4e482777b368166a6252b49d8 miliarium_profiles/02_ixAetheron.md — DO NOT EDIT -->
# ixAetheron — Slot 02

**Sector:** ETH Staking
**Template:** Non-Standard (56% / 16% / 28%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | sfrxETH | 28% | ERC-4626 | Frax staked ETH — native ERC-4626 vault over frxETH |
| Yield Core B | wOETH | 28% | ERC-4626 | Origin wrapped OETH — native ERC-4626 vault over OETH (1:1 ETH) |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| LST Leg A | rETH | 14% | ERC-20 | Rocket Pool ETH — non-Lido LST |
| LST Leg B | weETH | 14% | ERC-20 | EtherFi weETH — non-Lido LST |

**ERC-4626 composition:** 56% (sfrxETH + wOETH) — exceeds 52% threshold.

## Profile

**Real-world analogue:** Non-Lido ETH-staking basket — a spread of the validator networks and staking custodians that settle Ethereum, deliberately outside the Lido monopoly.

**Theme rationale:** This pool is an **ETH-native, non-Lido staking basket** (no svZCHF). The two yield cores are **native ERC-4626** vaults — **sfrxETH** (Frax) and **wOETH** (Origin) — that accrue ETH-staking yield through their share price, with no external oracle and no Aave wrapper layer. The two theme legs hold the underlying LSTs directly — **rETH** (Rocket Pool) and **weETH** (EtherFi) — each priced by its own intrinsic exchange rate. Four independent non-Lido staking protocols (Frax, Origin, Rocket Pool, EtherFi) in one venue; svZCHF is skipped, ixEDEL stays as the routing anchor.

**Non-standard notes:**
- No svZCHF in the yield core — **ixCasper** (slot 03) is the sibling LST pool (Fluid vaults + Lido wstETH); ixAetheron is the **non-Lido** counterpart
- Yield cores are **native ERC-4626** (sfrxETH, wOETH) — share-price accrual, oracle-free, no wrapper-layer dependency
- LST legs (rETH, weETH) priced by their intrinsic exchange rate (Rocket Pool rate provider; weETH's own rate) — also oracle-free
- ERC-4626 composition 56% — a +4pp margin over the 52% gate

**Volume drivers:**
- LST rebalancing across protocols (sfrxETH ↔ wOETH ↔ rETH ↔ weETH rotation)
- ETH staking yield arbitrage between Frax / Origin / Rocket Pool / EtherFi
- Non-Lido staking demand (validator-set diversification away from Lido)
- Native ERC-4626 wrap/unwrap flows on the yield cores

**Risk profile:**
- ETH staking slashing risk (underlying validators across four protocols)
- Smart-contract risk on the native vault wrappers (Frax sfrxETH, Origin wOETH) and the Origin AMO peg
- LST de-peg / liquidity risk on rETH and weETH
- Higher IL risk (ETH-denominated cores vs the ERC-20 LST legs)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% (admitted vault classes) — met by sfrxETH (28%) + wOETH (28%) = 56% |
| Vault-Class Registry | All ERC-4626 tokens admitted at genesis (per [Bootstrap §xxiv-a](08_bootstrap.md)) |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (auto-registration via `registerGaugeFromComposition(pool)`, governance-only — no permissionless-activation check, optional 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
