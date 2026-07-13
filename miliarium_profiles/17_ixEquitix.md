# ixEquitix — Slot 17

**Sector:** US Equities (Large Cap)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | sUSDS | 26% | ERC-4626 | Sky savings rate vault |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | SPYon | 16% | ERC-20 | Tokenised SPDR S&P 500 ETF |
| Theme Asset B | IVVon | 16% | ERC-20 | Tokenised iShares Core S&P 500 ETF |

**ERC-4626 composition:** 52% (svZCHF + sUSDS)

## Profile

**Real-world analogue:** S&P 500 index fund — the benchmark for US large-cap equity exposure, available 24/7 on-chain.

**Theme rationale:** SPYon and IVVon are tokenised versions of the two largest S&P 500 ETFs ($500B+ combined AUM in TradFi). Both track the same index, creating natural arbitrage. This is the broadest US equity exposure available in the protocol.

**Volume drivers:**
- 24/7 equity trading demand (TradFi markets close, on-chain doesn't)
- SPYon ↔ IVVon arbitrage (same underlying index, different issuers)
- US market hours ↔ off-hours price discovery
- Macro rotation flows (risk-on → equities, risk-off → treasuries/gold)

**Risk profile:**
- US equity market risk (S&P 500 drawdowns)
- Tokenised equity issuer risk (counterparty, regulatory)
- Off-hours pricing risk (weekend/holiday price gaps)
- Regulatory risk (tokenised securities evolving legal framework)

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% (admitted vault classes) — met by svZCHF (26%) + sUSDS (26%) |
| Vault-Class Registry | All ERC-4626 tokens admitted at genesis (per [Bootstrap §xxiv-a](08_bootstrap.md)) |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (auto-registration via `registerGaugeFromComposition(pool)`, governance-only — no permissionless-activation check, optional 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)

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
