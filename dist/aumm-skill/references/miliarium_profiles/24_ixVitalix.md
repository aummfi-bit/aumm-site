<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a miliarium_profiles/24_ixVitalix.md — DO NOT EDIT -->
# ixVitalix — Slot 24

**Sector:** Healthcare
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | LLYon | 16% | ERC-20 | Tokenised Eli Lilly & Co |
| Theme Asset B | NVOon | 16% | ERC-20 | Tokenised Novo Nordisk A/S |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** Pharma blue-chip fund — exposure to the two most valuable pharmaceutical companies, driven by the GLP-1/obesity drug revolution.

**Theme rationale:** Eli Lilly and Novo Nordisk are the two dominant players in the GLP-1 obesity/diabetes drug market — the largest pharmaceutical opportunity in a generation. LLY (Mounjaro/Zepbound) and NVO (Ozempic/Wegovy) together represent the defensive healthcare sector with blockbuster growth.

**Volume drivers:**
- Drug approval and clinical trial data releases (massive single-day moves)
- Quarterly earnings and revenue guidance
- GLP-1 market expansion news (new indications, competitor data)
- Defensive sector rotation (pharma rallies in risk-off environments)

**Risk profile:**
- Drug pipeline risk (clinical trial failures)
- Pricing/regulatory risk (drug pricing legislation, Medicare negotiations)
- Competition risk (new GLP-1 entrants)
- Lower volatility than tech (pharma is traditionally defensive)
- Tokenised equity counterparty risk

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
