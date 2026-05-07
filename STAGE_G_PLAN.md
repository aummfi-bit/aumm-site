# Stage G Plan — aumm-site Spec Coherence Pass

**Status:** In progress. Bundle A complete; Bundle B in progress (3 of 9 sub-steps committed).
**Sibling plan:** `aumm-deploy/docs/STAGE_G_PLAN.md` — the implementation-side plan.
**Source of truth (aumm-deploy):**
- `docs/STAGE_G_PRECHECK_AUTO_GAUGE.md` — pivot decision record (propositions P-1–P-6, conflicts C-1–C-6)
- `docs/STAGE_G_NOTES.md` — design freeze (G-D1–G-D11)
- `docs/FINDINGS.md` OQ-G1–OQ-G4 — resolutions
**Scope:** Update this repo's spec docs to be coherent with the aumm-deploy Stage G auto-gauge pivot (locked 2026-05-05).

---

## Workflow

Every edit follows the §8e.1 cursor-prompt convention from `aumm-deploy/CLAUDE.md`:

- Claude Code (Opus high) authors a `### CURSOR PROMPT` + `### USER VERIFY` two-block §8e.1 prompt per sub-step.
- Cursor executes the file save and stops.
- User pastes verify output (`wc -l`, `shasum`, `grep`) back in their terminal.
- Claude Code (Sonnet for relay, Opus for non-trivial audit) verifies and authors the commit block.
- Sub-step prefix: `SG.<bundle><n>` (e.g., SG.A1, SG.B3).

---

## Bundle A — Sandbox fast-track deletions ✅ COMPLETE

Per precheck **P-5** (deprecate Sandbox fast-track) and **C-3** (aumm-site §xxi fast-track row must be amended).

| Sub-step | File | Edit | Commit | Status |
| --- | --- | --- | --- | --- |
| SG.A1 | `08_bootstrap.md` | drop Sandbox fast-track heading and rule paragraph | `ecfdba6` | ✅ |
| SG.A2 | `09_transitions.md` | delete Sandbox fast-track bullet | `2cc3258` | ✅ |
| SG.A3 | `12_aureum_glossary.md` | delete Fast-Track Rule glossary entry | `210f12a` | ✅ |
| SG.A4 | `13_appendices.md` | delete fast-track from audit scope list and bullet | `4407142` | ✅ |
| SG.A5 | `14_ux_ui.md` | remove Fast-Track progress from Sandbox pools dashboard bullet | `836d929` | ✅ |

Close-out grep at root after Bundle A: zero residual fast-track references at source-of-truth level. The `dist/aumm-skill/references/` mirror still has stale copies — resyncs in Bundle F via llms.txt regeneration.

---

## Bundle B — Four→three vote-type model ✅ COMPLETE

Per precheck **P-1** (replace gauge-approval vote with criteria gate) and **C-2** / **C-5** (FINDINGS OQ-10 four-vote-types → three).

| Sub-step | File | Edit | Commit | Status |
| --- | --- | --- | --- | --- |
| SG.B1 | `10_constitution.md` §xxvii | drop Gauge Proposal vote (four → three governance actions) | `74f58a5` | ✅ |
| SG.B2 | `17_faq.md` | governance section reframe (four → three; gauge proposal → permissionless activation) | `4794f0f` | ✅ |
| SG.B3 | `17_faq.md` | Anti-Gaming section reframe (gate-and-vote → gate-and-challenge) | `20d3214` | ✅ |
| SG.B4 | `12_aureum_glossary.md` §xxxv | drop Gauge Proposal from overview entry + delete standalone Gauge Proposal entry | `3eaf797` | ✅ |
| SG.B5 | `04_tokenomics.md` | "gauge approvals" → "gauge activation" at L61, L109, L234; four-vote-list reframe at L109 | `0d06915` | ✅ |
| SG.B6 | `02_mental_model.md` | rewrite L59 "gauge approval has a clear mechanism" → permissionless | `b3d94a0` | ✅ |
| SG.B7 | `05_miliarium_aureum.md` | reword L155 "gauge proposal, vote, 90-day boost" + L157 "gauge vote" path | `9fef6ae` | ✅ |
| SG.B8 | `06_miliarium_manifest.md` | reword L69 composition challenge replacement bootstrap path | `7cc92fc` | ✅ |
| SG.B9 | `14_ux_ui.md` | rewrite L86 "Active proposals — gauge approvals…" + L16 proposal list | `b1dae98` | ✅ |

---

## Bundle C — Permissionless activation + anti-spam fee terminology ✅ COMPLETE

Per precheck **P-1** and **P-6** (anti-spam fee reclassification). Mostly integrated into Bundle B FAQ rewrites; remaining call-sites in:

| Sub-step | File | Edit | Status |
| --- | --- | --- | --- |
| SG.C1 | `08_bootstrap.md` | reword §xxiv "gauge proposal" mechanic → permissionless activation + anti-spam fee | ✅ |
| SG.C2 | `09_transitions.md` | reword L33 "gauge proposals (100 svZCHF/sUSDS)" → permissionless activation w/ anti-spam fee | ✅ |
| SG.C3a | `08_bootstrap.md` §xxi | sweep §xxi (Cold-Start Design) — heading L9; doctrine patches L13/L15/L40 (criteria-gate, no LP-vote admission, 90-day boost only on named paths); terminology L17/L23/L34; table row L29 (AuMT vote → criteria gate); approach (B) per chat | ✅ |
| SG.C3b | `08_bootstrap.md` §xxiii | sweep §xxiii (Anti-Gaming Engine) — terminology L84; attacker scenario L99; sacrificial-lamb L138 (gauge-approval-vote → activation + anti-spam fee); revocation-restart L146 (new gauge proposal → re-activation post-criteria-restoration) | ✅ |
| SG.C3c | `08_bootstrap.md` §xxiv | sweep §xxiv (Governance Gating) post-SG.C1 — L158 (initial swap fee → first-activation parameter per C-1); L186 (composition-challenge "no separate gauge proposal" → auto-registration phrasing); L242 (worked-example checklist "Get a gauge approved… AuMT vote" → permissionless activation + anti-spam fee). Excludes lines already owned by SG.C1 (L160, L162–166) | ✅ |

---

## Bundle D — Vault-Class Registry + class-gated 52% numerator + Frankencoin veto §

Per precheck **OQ-G4** resolution. Substantial new doctrine:

| Sub-step | File | Edit | Status |
| --- | --- | --- | --- |
| SG.D1 | `04_tokenomics.md` §ix | insert canonical OQ-G4 numerator definition into Quality Gate paragraph | ✅ |
| SG.D2 | `08_bootstrap.md` | new section: Vault-Class Registry mechanism (admission, fingerprints, proposal+veto+auto-finalize+revoke) | ✅ |
| SG.D3 | `10_constitution.md` §xxvii | new subsection: Frankencoin-style veto model with tunable bounds; reword L53 "hooked at gauge approval" → "hooked at gauge activation"; reframe L54 composition-challenge follow-on (drop "supermajority vote supplies stronger consent than standard gauge approval" comparison; rephrase "No separate follow-up gauge proposal is needed" → "Replacement gauge auto-registers via `registerGaugeFromComposition(pool)` per G-D7 — no permissionless-activation criteria check, 90-day boost applies") | ✅ |
| SG.D4 | `10_constitution.md` §xxix | add Vault-Class tunable-bounds row (proposalBond ≥ antiSpamFee, vetoThreshold ≤ governanceQuorumThreshold, window ∈ [BLOCKS_PER_EPOCH, 3×BLOCKS_PER_EPOCH]) | ✅ |
| SG.D5 | `12_aureum_glossary.md` | new entries: Vault-Class Registry, Anti-Spam Fee, Permissionless Gauge Activation, three admission fingerprints (ImplementationAddress / FactoryAddress / BytecodeHash) | ✅ |
| SG.D6 | `13_appendices.md` | add Vault-Class Registry to audit scope list | ✅ |
| SG.D7 | `17_faq.md` | new FAQ entry: "How does a new pool get gauged?" — covers permissionless activation + Vault-Class Registry | ✅ |
| SG.D8 | `12_aureum_glossary.md` §xxxii-a | rewrite L45 "Gauge" entry: drop "Gauge approval is a governance vote — qualified AuMT holders decide…" → permissionless-criteria-gated framing (Quality Gate ≥52%, $10K TVL SMA, pool-type whitelist, forbidden-token block; no governance vote at activation; revocable via Gauge Challenge) | ✅ |
| SG.D9 | `02_mental_model.md` | add paragraph: Vault-Class Registry as the single surface where governance exercises class-admission discretion | ✅ |
| SG.D10 | `05_miliarium_aureum.md` | add callout: Miliarium genesis classes hard-coded at construction; cross-link to §xxiv-a | ✅ |
| SG.D11 | `14_ux_ui.md` | add VCR subsection: proposed classes queue, veto countdown, admitted-classes list; cross-link to §xxiv-a | ✅ |
| SG.D12 | `15_overview.md` | add Vault-Class Registry to major-mechanisms list with one-line description | ✅ |

### Bundle D amendments — post-pivot cross-bundle sweep

Triggered by the 2026-05-05 design-freeze landings (G-D11 asymmetric anti-spam fee, G-D12 90-day boost deprecation in aumm-deploy/docs/STAGE_G_NOTES.md). Cross-bundle sweep — files in Bundle B/C/D scopes touched.

| Sub-step | Scope | Edit | Status |
| --- | --- | --- | --- |
| SG.AMEND-1 | 9 files (cross-bundle) | drop 90-day gauge boost from spec — Incendiary Boost is the sole cold-start mechanism | ✅ |
| SG.AMEND-2 | 6 files (cross-bundle) | asymmetric anti-spam fee sweep — 100 svZCHF / 125 sUSDS canonical; 1:1.25 ratio framing for governance deposits (1,000/1,250) and sacrificial-lamb (2,000/2,500) | ✅ |
| SG.AMEND-3 | 3 files (cross-bundle) | wording fixes — pool-type whitelist ≠ VCR scope; anti-spam canonical value in glossary; four → three governance actions per SG.D3; `activateGauge(pool)` row in constitution swap-fee table | ✅ |

---

## Bundle E — F-10 cohort rewrite, growth-signal doctrine, threshold events, vault-floor downgrade

Per precheck **P-2**, **P-3**, **P-4** and **G-D3** (top-15% favored cohort with caps as anti-concentration controls).

| Sub-step | File | Edit | Status |
| --- | --- | --- | --- |
| SG.E1 | `11_formulas.md` F-10 | top-15%-favored-cohort framing; rewrite caps as top-cohort anti-concentration; 3-epoch smoothing tag; defer numeric tuning to aumm-deploy G1.x | ✅ |
| SG.E2 | `09_transitions.md` Month 11+ | growth-signal doctrine note (losing top-tier emissions = intended) | ✅ |
| SG.E3 | `14_ux_ui.md` | threshold-event dashboard items per STAGE_G_NOTES.md event schema | ✅ |
| SG.E4 | `11_formulas.md` F-12 | reword L289 "or new gauge approval" → "or new permissionless gauge activation" | ✅ |
| SG.E5 | `17_faq.md` L161+L221, `13_appendices.md` L105 | vault-floor wording → Vault-Class Registry framing (OQ-G4) | ✅ |

---

## Bundle F — Cross-link cleanup + miliarium_profiles/ batched + llms.txt regeneration

Final pass: legacy cross-links, 28-pool profile sweep, and AI-skill bundle regeneration.

| Sub-step | Scope | Edit | Status |
| --- | --- | --- | --- |
| SG.F1 | `15_overview.md`, `README.md`, `script.md`, `09_transitions.md`, `14_ux_ui.md`, `13_appendices.md`, `17_faq.md` | legacy cross-link cleanup (gauge approval → activation, four → three); `09_transitions.md` L52 bottom-15%-capped wording → favored-cohort framing; `14_ux_ui.md` L68 Safe/Warning/Cut tier indicators → favored/residual cohort badges; `13_appendices.md` + `17_faq.md` stale gauge-approved wording sweep | ✅ `6055af5` (README.md + 17_faq.md scanned clean, 0 edits needed) |
| SG.F.M1 | `miliarium_profiles/` (28 files) | vault-floor row downgrade per OQ-G4 — row label `Vault TVL floor` → `Vault-Class Registry`, content reframed to genesis admission (per [Bootstrap §xxiv-a](08_bootstrap.md)) | ✅ `38e1a40` (bundled with M2+M3) |
| SG.F.M2 | `miliarium_profiles/` (28 files) | 4626 Quality Gate row class-admission qualifier — `≥52% — met` → `≥52% (admitted vault classes) — met`, per-pool composition data preserved | ✅ `38e1a40` (bundled with M1+M3) |
| SG.F.M3 | `miliarium_profiles/` (28 files) | composition challenge row wording — `(gauge proposal, vote, 90-day boost)` and `(specified-pool model, 90-day boost)` → `(auto-registration via `registerGaugeFromComposition(pool)`, governance-only — no permissionless-activation check, optional 90-day boost)` per Constitution §xxvii + Bootstrap §xxiv (boost remains available) | ✅ `38e1a40` (bundled with M1+M2) |
| SG.F2 | `llms.txt`, `llms-full.txt`, `dist/aumm-skill/references/` | regeneration to resync with all canonical edits | ✅ `d6ea52d` (script-driven via `python3 scripts/generate_llms_manifest.py --skill-out dist/aumm-skill`; `llms.txt` surveyed and needs no edits — content remains spec-correct) |

---

## Completion log

| Sub-step | Commit | Δ lines | Date |
| --- | --- | --- | --- |
| SG.A1 | `ecfdba6` | −2 | 2026-05-05 |
| SG.A2 | `2cc3258` | −1 | 2026-05-05 |
| SG.A3 | `210f12a` | −1 | 2026-05-05 |
| SG.A4 | `4407142` | −1 | 2026-05-05 |
| SG.A5 | `836d929` | 0 | 2026-05-05 |
| SG.B1 | `74f58a5` | −2 | 2026-05-05 |
| SG.B2 | `4794f0f` | 0 | 2026-05-05 |
| SG.B3 | `20d3214` | 0 | 2026-05-05 |
| SG.B4 | `3eaf797` | −1 | 2026-05-05 |
| SG.B5 | `0d06915` | 0 | 2026-05-05 |
| SG.B6 | `b3d94a0` | 0 | 2026-05-05 |
| SG.B7 | `9fef6ae` | 0 | 2026-05-05 |
| SG.B8 | `7cc92fc` | 0 | 2026-05-05 |
| SG.B9 | `b1dae98` | 0 | 2026-05-05 |
| SG.C1  | `81013bb` | +2 | 2026-05-05 |
| SG.C2  | `47b8e5b` |  0 | 2026-05-05 |
| SG.C3a | `22ff001` |  0 | 2026-05-05 |
| SG.C3b | `7e6eb78` |  0 | 2026-05-05 |
| SG.C3c | `5216631` |  0 | 2026-05-05 |
| SG.AMEND-1 | `055d89f` | −8 | 2026-05-05 |
| SG.AMEND-2 | `0c9f948` |  0 | 2026-05-05 |
| SG.AMEND-3 | `55ea7d8` |  0 | 2026-05-05 |
| SG.D9 | `3364e15` | +2 | 2026-05-06 |
| SG.D10 | `7af9b3e` | +2 | 2026-05-06 |
| SG.D11 | `0df47d0` | +8 | 2026-05-06 |
| SG.D2 | `471be2b` | +31 | 2026-05-06 |
| SG.D3 | `5d3b3ff` | +6 | 2026-05-06 |
| SG.D4 | `932b20f` | +10 | 2026-05-06 |
| SG.D5 | `f8b4c8b` | +9 | 2026-05-06 |
| SG.D6 | `4506e9b` | +1 | 2026-05-06 |
| SG.D7 | `0e1dc07` | +14 | 2026-05-06 |
| SG.D1 | `be06c1d` | +8 | 2026-05-06 |
| SG.D8 | `d9a101f` | 0 | 2026-05-06 |
| SG.D12 | `89f319b` | +1 | 2026-05-06 |
| SG.E4 | `1c50732` | 0 | 2026-05-06 |
| SG.E1 | `ad90be3` | +9 | 2026-05-06 |
| SG.E2 | `c0da205` | +4 | 2026-05-06 |
| SG.E3 | `1828c17` | +3 | 2026-05-06 |
| SG.E5 | `9c1cd5d` | 0 | 2026-05-06 |
| SG.F1 | `6055af5` | 0 | 2026-05-06 |
| SG.F.M1+M2+M3 | `38e1a40` | 0 (28 files × 84 in/out, line counts unchanged) | 2026-05-06 |
| SG.F2 | `d6ea52d` | +94 (53 files: 28 profiles + 17 canon docs + sagix essays + `_canon.json` SHA refresh; `llms.txt` 0 edits) | 2026-05-07 |
| SG.F1-followup | `35fd4f5` | 0 (script.md L40 — Vault TVL floor → Vault-Class Registry; deferred from SG.F1, unblocked by SG.F.M1) | 2026-05-07 |
