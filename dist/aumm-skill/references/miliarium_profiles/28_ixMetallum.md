<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/28_ixMetallum.md — DO NOT EDIT -->
# ixMetallum — Slot 28

**Sector:** Silver & uranium (ETFs)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDT | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDT |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | SLVon | 16% | ERC-20 | Tokenised iShares Silver Trust (SLV) |
| Theme Asset B | URAon | 16% | ERC-20 | Tokenised Global X Uranium ETF (URA) |

**ERC-4626 composition:** 52% (svZCHF + waEthUSDT)

## Profile

**Real-world analogue:** Listed industrial and energy metals — silver (precious / industrial) and uranium (nuclear fuel equities) via highly liquid ETFs.

**Theme rationale:** **SLVon** is silver-bullion exposure (SLV). **URAon** is uranium miners and the nuclear fuel cycle (URA). **ixAurix** (slot 27) holds **physical gold** tokens only (PAXG/XAUt). **GLDon** and **IAUon** are **gold** ETFs — they are not the themes here; silver and uranium live in this slot.

**Volume drivers:**
- Silver: industrial demand, gold-beta, USD strength
- Uranium: nuclear policy, power demand, miner equities
- ETF premium/discount vs spot and underlying NAV
- Cross-commodity rotation vs gold (ixAurix)

**Risk profile:**
- Equity and commodity beta (URA miners differ from spot uranium oxide)
- Silver volatility
- Tokenised ETF counterparty risk

## Performance Discipline

| Criterion | Requirement |
|:----------|:------------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + waEthUSDT (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
