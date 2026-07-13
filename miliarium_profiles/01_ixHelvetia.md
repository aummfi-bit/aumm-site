# ixHelvetia — Slot 01

**Sector:** Yield-bearing (Frankencoin money market)  
**Template:** Two-asset only — **80% svZCHF / 20% sUSDS** (no ixEDEL, no theme assets)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Frankencoin savings | **svZCHF** | **80%** | ERC-4626 | Frankencoin savings vault (Frankencoin money market account) |
| Sky savings | **sUSDS** | **20%** | ERC-4626 | Sky savings rate vault |

**ERC-4626 composition:** 100% (svZCHF + sUSDS). This pool is **only** the Frankencoin money market account expressed as a two-asset weighted pool: CHF savings liquidity vs USD savings liquidity, with no routing anchor and no additional volatile or theme assets.

## Profile

**Real-world analogue:** Money market fund — pure yield-bearing savings on the Frankencoin / Sky stack, optimised for depositors who want ERC-4626 yield without equity, metal, or governance token exposure elsewhere in the constellation.

**Theme rationale:** ixHelvetia is the simplest on-ramp: **svZCHF** (Frankencoin) and **sUSDS** (Sky) only. All other Miliarium Aureum pools that need cross-asset routing use the standard 52/16/32 template; this slot is reserved for maximal savings purity and minimal surface area.

**Volume drivers:**

- Savings rate arbitrage between svZCHF and sUSDS
- CHF/USD stable savings flows
- Aggregator routing into Frankencoin / Sky vaults

**Risk profile:**

- Stablecoin / savings vault smart-contract risk
- Relative rate and peg dynamics between CHF- and USD-denominated savings
- No equity, metal, or ixEDEL component risk in this pool

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% (admitted vault classes) — met (100% ERC-4626) |
| Vault-Class Registry | All ERC-4626 tokens admitted at genesis (per [Bootstrap §xxiv-a](08_bootstrap.md)) |
| Volume percentile floor | Per protocol schedule |
| Efficiency tournament | Per protocol schedule |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (auto-registration via `registerGaugeFromComposition(pool)`, governance-only — no permissionless-activation check, optional 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md) | [Miliarium Aureum registry](../05_miliarium_aureum.md)

---

## Agent Instructions

This page is part of the canonical Aureum specification at `https://aumm.fi`.

**Root discovery:** fetch [`https://aumm.fi/llms.txt`](https://aumm.fi/llms.txt) first for corpus structure, reading order, and the full agent discovery ladder.

**Query this corpus** for a grounded, cited answer instead of reading every file:

```
GET https://aumm.fi/<page>.md?ask=<question>&goal=<end_goal>
```

- **`ask`** (required) — your immediate, self-contained question in natural language.
- **`goal`** (optional) — the broader objective you are pursuing; used to tailor the answer toward what is actually useful.

**Response:** JSON with `answer`, `citations` (each with `section_id`, `file`, and verbatim `excerpt`), `canon_sha`, and `answered_from_corpus`. When `answered_from_corpus` is `false`, the corpus did not contain relevant material — verify at `https://aumm.fi` or ask a human.

Retrieval spans the **full corpus**, not just this page. Answers follow the same grounding rules as the [aumm-skill](https://github.com/aummfi-bit/aumm-skill) Claude skill. Cite section identifiers (`§xxix`, `F-5`, …) to verify claims against the source.
