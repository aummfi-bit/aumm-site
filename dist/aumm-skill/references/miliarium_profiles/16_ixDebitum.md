<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 miliarium_profiles/16_ixDebitum.md — DO NOT EDIT -->
# ixDebitum — Slot 16

**Sector:** DeFi Lending Infra
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | Morpho | 16% | ERC-20 | Morpho — permissionless lending governance |
| Theme Asset B | SPK | 16% | ERC-20 | Spark (Sky ecosystem) — lending protocol governance |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Lending sector index — like owning shares in the challenger banks disrupting traditional lending.

**Theme rationale:** Morpho and SPK (Spark) represent the next generation of DeFi lending. Morpho is a permissionless lending optimiser that sits on top of Aave/Compound. Spark (formerly Spark Protocol) is the lending arm of the Sky/Maker ecosystem. Both compete with and complement Aave.

**Volume drivers:**
- Morpho governance token demand (growing TVL narrative)
- SPK ecosystem integration with Sky/Maker
- Lending protocol competition narratives
- DeFi lending rate arbitrage driving token demand

**Risk profile:**
- Governance token volatility (Morpho, SPK)
- SPK ecosystem dependency on Sky/Maker
- Lending protocol smart contract risk
- Competition risk (Aave dominance)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by svZCHF (26%) + sUSDS (26%) |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
