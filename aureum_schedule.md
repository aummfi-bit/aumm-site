# Project Aureum — Delivery Schedule

*PMO Master Plan — Fork to First Block*
*Sprint cadence: 2 weeks | Estimation: story points (SP) | Priority: P0 (blocker) → P3 (nice-to-have)*

---

## Programme Overview

| Parameter | Value |
|-----------|-------|
| Total estimated sprints | 16–20 (32–40 weeks) |
| New Solidity scope | ~4,500 LOC |
| Inherited verified code | Balancer V3 (Certora) — pool layer, vault, SOR, hooks, rate providers |
| Audit window | 6–8 weeks (external) |
| Testnet window | 4–6 weeks |
| Critical path | Smart contracts → Audit → Testnet → Mainnet deploy → First block |

---

## Workstream Map

| ID | Workstream | Owner | Dependency |
|----|-----------|-------|------------|
| WS-1 | Smart Contracts — Core | Solidity Lead | — |
| WS-2 | Smart Contracts — Governance | Solidity Lead | WS-1 partial |
| WS-3 | Smart Contracts — Anti-Gaming | Solidity Lead | WS-1 partial |
| WS-4 | Smart Contracts — Bootstrapping | Solidity Lead | WS-1, WS-3 |
| WS-5 | Smart Contracts — Treasury & Price Ceiling | Solidity Lead | WS-1 |
| WS-6 | Internal Testing & Fuzzing | Solidity Lead + QA | WS-1 through WS-5 |
| WS-7 | External Audit | Audit Firm | WS-6 complete |
| WS-8 | Frontend — Core App | Frontend Lead | WS-1 partial |
| WS-9 | Frontend — Dashboards & Governance UI | Frontend Lead | WS-2, WS-3 |
| WS-10 | Infrastructure & DevOps | DevOps | — |
| WS-11 | Testnet Deployment | All | WS-6, WS-8, WS-10 |
| WS-12 | Pool Preparation & Aggregator Integration | Architecture (Sagix) | WS-11 |
| WS-13 | Mainnet Launch | All | WS-7, WS-11, WS-12 |

---

## Phase 0: Foundation (Sprints 1–2)

*Fork, scaffold, development environment.*

### Sprint 1 — Repository & Architecture

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S1-01 | Fork Balancer V3 monorepo, strip branding, establish Aequilibrium namespace | 5 | P0 | Clean compile, all existing Balancer tests pass |
| S1-02 | Set up CI/CD pipeline (Foundry, GitHub Actions, coverage reports) | 3 | P0 | Green pipeline on every PR, coverage baseline established |
| S1-03 | Document inherited vs new contract boundaries | 2 | P0 | Architecture decision record (ADR) signed off |
| S1-04 | Define interface specs for all new contracts (AuMM, AuMT, CCB, Gauge, Fee Distributor) | 5 | P0 | Solidity interfaces committed, reviewed by team |
| S1-05 | Set up testnet deployment scripts (Sepolia or Holesky) | 3 | P1 | One-command deploy of inherited pool layer |
| S1-06 | Establish frontend repo, fork Balancer UI, strip branding | 3 | P1 | aumm.fi skeleton renders locally |

### Sprint 2 — Token Contracts & Emission Scaffolding

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S2-01 | Implement AuMM ERC-20 token contract (21M cap, immutable) | 5 | P0 | Mint function restricted to emission controller only; cap enforced; all ERC-20 tests pass |
| S2-02 | Implement per-block emission streaming logic | 8 | P0 | Correct emission rate for Era 1; halving trigger at block boundary; fuzz tests on edge cases |
| S2-03 | Implement treasury emission split (75%→50%→0% linear decline) | 5 | P0 | Treasury share matches schedule at any block; immutable after deploy |
| S2-04 | Implement AuMT tessera wrapper (LP position → governance token) | 5 | P0 | AuMT minted on pool join, burned on exit; USD value readable on-chain |
| S2-05 | Stub CCB interface (equal-weight distribution for Pioneer phase) | 3 | P1 | 25 Mercatūs Praecursorii receive 1/25th each; non-Mercatūs Praecursorii receive zero |
| S2-06 | Unit test suite for token contracts | 5 | P0 | 100% branch coverage on AuMM and AuMT; invariant tests on supply cap |

---

## Phase 1: Core Engine (Sprints 3–6)

*CCB, fee distribution, governance power formula.*

### Sprint 3 — Continuous Central Bank (CCB)

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S3-01 | Implement 60-day EMA calculator (on-chain TVL tracking per pool) | 8 | P0 | EMA updates at cycle boundary; half-life ~21 days verified; gas benchmarked |
| S3-02 | Implement CCB score formula: `TVL_EMA × PMAR_mult × Incendiary_mult` | 5 | P0 | Each pool's share = score / sum(all scores); total emission = block_emission at all times |
| S3-03 | Implement two-step Incendiary subtraction (priority skim before CCB distribution) | 5 | P0 | Incendiary claims deducted first; remainder distributed via CCB; sum = block_emission |
| S3-04 | Implement PMAR engine (slope calculation, dead zone, +/-0.05 adjustments, [0.75–1.25] clamping) | 5 | P0 | Multiplier updates at cycle boundary; slopes computed from EMA(60) ratios; dead zone at 0.1% of ratio; range enforced [0.75–1.25] |
| S3-05 | CCB integration tests (multi-pool, multi-cycle simulation) | 8 | P0 | 100-cycle simulation with varying TVL, deposits, withdrawals; emission invariant holds |

### Sprint 4 — Fee Distribution & Buyback

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S4-01 | Implement fee splitter: swap fees (50% LP bonus / 25% buyback / 25% treasury) | 5 | P0 | Correct split on every swap; LP bonus proportional to governance participation |
| S4-02 | Implement yield fee splitter: ERC-4626 yield (25% buyback / 75% treasury) | 5 | P0 | 10% skim on vault yield accrual; correct 25/75 split |
| S4-03 | Implement buyback-and-burn contract (market buy AuMM from trading pool + permanent burn) | 5 | P0 | AuMM purchased at market; sent to burn address; supply tracker updated |
| S4-04 | Implement token supply tracker (emitted, burned, net circulating, 30-day burn rate) | 3 | P1 | Real-time on-chain reads; matches manual calculation |
| S4-05 | Fee distribution integration tests | 5 | P0 | End-to-end: swap → fee split → buyback → burn → supply decrease verified |

### Sprint 5 — Governance Power Formula

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S5-01 | Implement governance power: `(AuMT_value × time_in_pool)^(1/4)` | 5 | P0 | Fourth root computed correctly; time accrues per block; Era 2 cube root transition at halving block |
| S5-02 | Implement 14-day qualification period (zero weight before qualification) | 3 | P0 | `time_in_pool = 0` for first 14 days; begins accruing at day 15 |
| S5-03 | Implement withdrawal reset (any withdrawal → power to zero, clock restarts) | 5 | P0 | Even 1 wei withdrawal triggers full reset; fuzz tested with partial withdrawals |
| S5-04 | Implement 6-month on-ramp (sublinear growth to full weight) | 3 | P0 | Power at day 14 ≈ minimal; power at day 180 ≈ full; curve matches formula |
| S5-05 | Implement tessera-weighted voting for Pioneer multipliers (discrete inputs → continuous average) | 5 | P0 | Voters choose from [0.90, 0.95, 1.00, 1.05, 1.10]; result is weighted average |
| S5-06 | Governance power fuzz tests and invariant checks | 5 | P0 | No governance power without qualifying LP; whale-resistance ratio verified |

### Sprint 6 — Governance Actions & Quorum

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S6-01 | Implement gauge approval voting (AuMM deposit burned, simple majority) | 5 | P0 | 100 svZCHF/sUSDS equivalent in AuMM burned on submission; vote tallied correctly |
| S6-02 | Implement gauge challenge / revocation voting | 3 | P1 | 1,000 equivalent burned; simple majority to revoke |
| S6-03 | Implement soft quorum for major decisions (20% threshold, timelock, auto-fail) | 5 | P0 | Fee changes, treasury spends, upgrades require quorum; timelock enforced |
| S6-04 | Implement unqualified-vote-to-burn router | 3 | P0 | Emissions directed to ineligible pools → routed to burn address |
| S6-05 | Implement 6-week voting cycle clock (Pioneer + Bubble multiplier votes) | 3 | P0 | Cycle boundaries enforced; votes only accepted during window |
| S6-06 | Full governance integration test suite | 5 | P0 | Propose → vote → execute → verify state change; quorum fail path tested |

---

## Phase 2: Anti-Gaming & Bootstrapping (Sprints 7–9)

*Efficiency tournament, Incendiary Boost, Bubble voting, Sandbox.*

### Sprint 7 — Anti-Gaming Stack

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S7-01 | Implement 4626 Quality Gate checker (≥52% composition, vault TVL floors: $5M / 30 BTC / 4M svZCHF) | 5 | P0 | On-chain read of vault `totalAssets()`; triple-currency floor evaluated; disqualification on failure |
| S7-02 | Implement $10K TVL floor (7-day SMA, graduated grace period) | 5 | P0 | 7-day SMA computed; grace schedule (5th → 10th → 15th percentile) enforced by month |
| S7-03 | Implement efficiency tournament (revenue/emissions ranking, 2-epoch smoothing) | 8 | P0 | Pools ranked; bottom 15% capped; excess redistributed; 2-epoch average prevents single-day glitches |
| S7-04 | Implement gauge revocation after 4 consecutive failed cycles | 3 | P0 | Counter increments on fail, resets on pass; gauge removed at 4; Pioneer tag revoked |
| S7-05 | Anti-gaming integration tests (multi-pool, adversarial scenarios) | 8 | P0 | Wash trading, flash deposit, sacrificial lamb, ghost governance attack vectors tested |

### Sprint 8 — Incendiary Boost & Bubble Voting

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S8-01 | Implement Incendiary Boost escrow (AuMM deposit → 30-day emission stream) | 5 | P0 | AuMM locked in contract; emitted linearly over 30 days; permanently burned on completion |
| S8-02 | Implement efficiency scalar: `E_85th × (2 - R)` | 5 | P0 | Correct calculation of 85th percentile density; rank-based multiplier applied |
| S8-03 | Implement Incendiary renewal lock (must be ≥85th percentile to renew) | 3 | P0 | Second boost blocked unless efficiency threshold met |
| S8-04 | Implement Bubble multiplier voting (0.90–2.00 range, 90-day window, tessera-weighted) | 5 | P0 | Window starts at gauge approval; expires at day 91; multiplier = weighted average |
| S8-05 | Implement Sandbox fast-track (top 10% efficiency → automatic gauge) | 3 | P1 | Non-gauged pool reaching threshold triggers automatic gauge creation |
| S8-06 | Bootstrapping integration tests | 5 | P0 | Incendiary + Bubble + EMA handoff tested across 120-day simulation |

### Sprint 9 — Treasury & Price Ceiling

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S9-01 | Implement AuMM trading pool deployment logic (month 6 trigger) | 5 | P0 | TVL-to-FDV vote mechanism; 80% treasury deployment; correct pool composition |
| S9-02 | Implement TVL measurement window (months 2–6, time-weighted average) | 3 | P0 | Recency-weighted; manipulation-resistant; feeds pricing formula |
| S9-03 | Implement price ceiling (7-day SMA, 200% FDV trigger, 0.75% daily sell rate) | 5 | P0 | Reads internal pool price (oracle-free); sell rate enforced; proceeds to Mercatūs Praecursorii |
| S9-04 | Implement month-10 hard stop (final deposit, excess burn, emission share → 0%) | 3 | P0 | All mechanisms deactivate permanently; leftover AuMM burned; treasury share = 0 forever |
| S9-05 | Implement Mercatūs Praecursorii locked liquidity (treasury deposits permanent, no withdrawal) | 3 | P0 | Deposit function succeeds; withdraw function reverts always |
| S9-06 | Treasury lifecycle integration test (months 0–10 full simulation) | 8 | P0 | Emission decline, pool deployment, ceiling activation/deactivation, final burn all verified |

---

## Phase 3: Integration & Hardening (Sprints 10–12)

*Full system integration, internal audit, fuzzing campaigns.*

### Sprint 10 — System Integration

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S10-01 | End-to-end integration: deploy all contracts, 25 Mercatūs Praecursorii, run 100-block simulation | 8 | P0 | All emissions correct; fees split correctly; governance power accrues; anti-gaming fires |
| S10-02 | Month 11–12 CCB transition test (equal-weight → full CCB linear interpolation) | 5 | P0 | `T` parameter transitions smoothly; no discontinuity at month 13 boundary |
| S10-03 | Pioneer tag registry integration (25 pools tagged, revocation tested, locked deposits verified) | 3 | P0 | All 25 pools tagged; revocation removes tag; treasury deposit locks verified |
| S10-04 | Gas optimization pass on all new contracts | 5 | P1 | Gas per operation benchmarked; no function exceeds 500K gas; CCB cycle update < 1M gas |
| S10-05 | Deployment script finalization (deterministic deploy, salt-based CREATE2) | 3 | P1 | Same addresses on testnet and mainnet; deploy is repeatable |

### Sprint 11 — Fuzzing & Invariant Testing

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S11-01 | Echidna/Medusa fuzzing campaign on AuMM supply invariants | 5 | P0 | No path to exceed 21M; no path to negative supply; 10M+ iterations |
| S11-02 | Echidna/Medusa fuzzing on CCB emission invariants | 5 | P0 | Total emitted per block = scheduled rate; no pool receives negative emissions |
| S11-03 | Echidna/Medusa fuzzing on governance power (no power without LP, withdrawal reset) | 5 | P0 | No governance power without qualifying position; reset path verified |
| S11-04 | Formal property checks on fee distribution (sum of splits = total fee) | 3 | P0 | Mathematical invariant: LP_bonus + buyback + treasury = total_fee for every swap |
| S11-05 | Attack simulation: flash loan governance, sandwich on buyback, MEV on emission claim | 5 | P0 | All attack vectors tested; no profitable exploit path found |

### Sprint 12 — Internal Audit & Documentation

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S12-01 | Internal code review (line-by-line on all ~4,500 LOC of new code) | 8 | P0 | Every function reviewed by at least 2 team members; findings documented |
| S12-02 | NatSpec documentation on all public/external functions | 5 | P0 | Every function, event, and error has NatSpec; auto-generated docs render correctly |
| S12-03 | Deployment runbook (step-by-step mainnet deployment procedure) | 3 | P0 | Tested on testnet; no ambiguity; rollback procedure documented |
| S12-04 | Prepare audit package (code, tests, architecture docs, threat model) | 5 | P0 | Single zip deliverable for auditor; includes all dependencies |
| S12-05 | Threat model document (attack surfaces, mitigations, residual risks) | 3 | P1 | Covers all new contracts; maps to anti-gaming criteria in design doc |

---

## Phase 4: External Audit (Sprints 13–15)

*Audit firm engagement, finding remediation, re-review.*

### Sprint 13 — Audit Kickoff

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S13-01 | Deliver audit package to selected firm | 1 | P0 | Package received; kickoff call completed; timeline agreed |
| S13-02 | Auditor onboarding (architecture walkthrough, threat model review) | 2 | P0 | Auditors confirm understanding of CCB, anti-gaming, and governance mechanics |
| S13-03 | Begin frontend development of aumm.fi (parallel track) | 8 | P1 | Pool list, deposit/withdraw flows, wallet connection functional |
| S13-04 | Begin Proof of Real Yield Dashboard (parallel track) | 5 | P1 | Real yield % vs emission yield % displayed per pool; data from subgraph |

### Sprint 14 — Audit In Progress + Frontend

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S14-01 | Respond to auditor questions and clarifications | 3 | P0 | All questions answered within 48 hours |
| S14-02 | Frontend: governance voting UI (Pioneer multiplier, gauge approval, challenges) | 5 | P1 | Vote submission, result display, cycle countdown functional |
| S14-03 | Frontend: token supply dashboard (emitted, burned, net circulating, burn rate) | 3 | P1 | Real-time on-chain reads; chart of supply over time |
| S14-04 | Frontend: pool creation flow with routing graph visualization | 5 | P2 | Shows ixEDEL connectivity benefit; estimated cross-pool arb volume |
| S14-05 | Set up monitoring and alerting (emission rate, TVL, fee accrual, anomaly detection) | 3 | P1 | Alerts on: emission deviation, TVL cliff, fee distribution failure |

### Sprint 15 — Audit Findings & Remediation

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S15-01 | Receive audit report | 1 | P0 | Report received and reviewed by full team |
| S15-02 | Triage findings (Critical / High / Medium / Low / Informational) | 2 | P0 | All Critical and High findings have remediation plan |
| S15-03 | Fix all Critical and High findings | 8 | P0 | Fixes committed, tested, and submitted for re-review |
| S15-04 | Fix Medium findings (where feasible) | 5 | P1 | Each Medium finding: fixed or documented as accepted risk |
| S15-05 | Auditor re-review of fixes | 2 | P0 | Auditor confirms all Critical/High fixes are correct |
| S15-06 | Final audit report published | 1 | P0 | Clean report (or accepted-risk annotations) available for public reference |

---

## Phase 5: Testnet & Launch Prep (Sprints 16–18)

*Public testnet, aggregator integration, pool preparation.*

### Sprint 16 — Testnet Deployment

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S16-01 | Deploy all contracts to testnet (Sepolia/Holesky) | 3 | P0 | All 25 Mercatūs Praecursorii live; emissions streaming; governance functional |
| S16-02 | Founding team testnet walkthrough (deposit, earn, vote, withdraw) | 2 | P0 | Every user flow tested by at least 2 team members |
| S16-03 | Testnet stress test (high-frequency deposits/withdrawals, cycle boundaries) | 5 | P0 | No reverts; emission invariants hold; gas within limits |
| S16-04 | Frontend connected to testnet (aumm.fi staging environment) | 3 | P0 | Full UX functional against testnet contracts |
| S16-05 | Subgraph deployment and indexer verification | 3 | P1 | Pool data, emission data, governance data indexed correctly |

### Sprint 17 — Aggregator Integration & Pool Prep

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S17-01 | Verify Aequilibrium SOR compatibility with existing Balancer V3 aggregator integrations | 3 | P0 | At least 2 aggregators (1inch, CoW) successfully route through testnet pools |
| S17-02 | Prepare seed liquidity for 25 Mercatūs Praecursorii (asset sourcing, wallet setup) | 3 | P0 | All 25 pool compositions confirmed; assets acquired or committed |
| S17-03 | Prepare ERC-4626 buffer initialization for all yield-bearing tokens | 5 | P0 | Balancer V3 buffers initialized for: svZCHF, sUSDS, waEthUSDC, waEthUSDT, sfrxUSD, GHO, waEthrETH, waEthweETH, fWSTETH, fWETH, waEthwstETH, sUSDe, scrvUSD |
| S17-04 | Verify all Mercatūs Praecursorii token compositions against design doc | 2 | P0 | 25 pools × weights × token addresses verified; no mismatches |
| S17-05 | DNS and hosting for aumm.fi (production) | 2 | P1 | Domain resolves; SSL; CDN; frontend deploys from CI |
| S17-06 | Bug bounty program launched (Immunefi or equivalent) | 2 | P1 | Scope defined; reward tiers set; publicly listed |

### Sprint 18 — Final Pre-Launch

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S18-01 | Mainnet dry run (deploy to mainnet fork, simulate 30 days of operations) | 5 | P0 | All mechanics function identically to testnet; no regressions |
| S18-02 | Multisig setup for treasury operations | 2 | P0 | N-of-M multisig deployed; signers confirmed; test transactions executed |
| S18-03 | Deployment rehearsal (step-by-step runbook execution on fork) | 3 | P0 | Runbook followed exactly; all addresses recorded; no deviations |
| S18-04 | Emergency procedures documented (pause paths, contact tree, incident response) | 2 | P1 | Procedures reviewed; team acknowledges roles |
| S18-05 | Go/No-Go decision meeting | 1 | P0 | All P0 items complete; audit clean; testnet stable; team consensus |

---

## Phase 6: Mainnet Launch (Sprint 19)

*First block.*

### Sprint 19 — Genesis

| ID | Story | SP | Priority | Acceptance Criteria |
|----|-------|----|----------|-------------------|
| S19-01 | Deploy all contracts to Ethereum mainnet (deterministic addresses) | 3 | P0 | All contracts verified on Etherscan; addresses match testnet dry run |
| S19-02 | Deploy 25 Mercatūs Praecursorii with founding gauges | 5 | P0 | All 25 pools live; weights match design doc; gauges active |
| S19-03 | Initialize all ERC-4626 buffers on Balancer V3 Vault | 3 | P0 | All yield-bearing tokens have initialized buffers; wrap/unwrap functional |
| S19-04 | Seed initial liquidity in Mercatūs Praecursorii | 3 | P0 | Founding team deposits in priority pools; TVL > $10K per pool |
| S19-05 | Verify emission streaming (first blocks) | 2 | P0 | AuMM accruing to LP positions; treasury share = 75%; non-Pioneer = 0 |
| S19-06 | Verify fee distribution (first swaps) | 2 | P0 | Swap fees split 50/25/25; yield fees split 25/75 |
| S19-07 | Frontend goes live at aumm.fi | 1 | P0 | Production deployment; all pools visible; deposit/withdraw functional |
| S19-08 | Monitoring active and verified | 1 | P0 | Dashboards green; alerts configured; on-call rotation confirmed |
| S19-09 | First block confirmed | — | P0 | Emissions streaming. Protocol is live. |

---

## Post-Launch Milestones (Reference)

These are protocol milestones from the design doc, not development sprints. Included for timeline context.

| Month | Milestone |
|-------|-----------|
| 0 | Genesis — 25 Mercatūs Praecursorii, equal-weight emissions, treasury at 75% |
| 2 | TVL measurement window opens |
| 6 | AuMM trading pool launch; buyback-and-burn begins; treasury at 50% |
| 6–10 | Price ceiling stabilization active |
| 10 | Hard stop — treasury at 0%, excess AuMM burned, PMAR initialised (all multipliers = 1.0) |
| 11 | Gauge proposals open; efficiency ranking begins; CCB transition starts |
| 12 | CCB transition completes |
| 13 | Full protocol activation — CCB, efficiency tournament, new gauged pool emissions |
| ~48 | First halving — emission rate drops 50%; governance dampening transitions to cube root |

---

## Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| Audit delays | Shifts mainnet by equal duration | Medium | Engage auditor early (Sprint 10); parallel frontend work during audit |
| Critical audit finding requiring architectural change | 2–4 sprint delay | Low | Comprehensive internal review + fuzzing before audit; threat model pre-shared |
| ERC-4626 buffer incompatibility with new vault tokens | Pool cannot use intended token | Medium | Test every vault token against Balancer V3 fork tests before pool design finalization |
| Aggregator integration friction | Reduced routing volume at launch | Medium | SOR is byte-identical to Balancer V3; existing integrations should work; verify on testnet |
| Key person dependency (single Solidity dev) | Schedule collapse if unavailable | High | Document all decisions; pair program critical sections; ensure at least 2 people can deploy |
| Gas cost exceeds budget for CCB cycle update | CCB unusable on mainnet | Low | Gas benchmarking in Sprint 10; optimize or batch if needed |
| Testnet ≠ mainnet behavior (block times, gas dynamics) | Unexpected failures at launch | Low | Mainnet fork dry run (Sprint 18) catches discrepancies |

---

## Definition of Done (Global)

Every story is complete when:

1. Code committed to main branch and passing CI
2. Unit tests cover all branches (100% for P0 stories)
3. Integration test demonstrates the feature in a multi-contract context
4. NatSpec documentation on all public functions
5. Peer review by at least one other team member
6. No known Critical or High severity issues
7. Gas benchmarks recorded (for on-chain operations)

---

## Sprint Velocity Tracking

| Sprint | Planned SP | Delivered SP | Burndown Notes |
|--------|-----------|-------------|----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| ... | | | |

*Updated at the end of each sprint during retrospective.*

---

## RACI Matrix (Key Decisions)

| Decision | Responsible | Accountable | Consulted | Informed |
|----------|-----------|------------|-----------|----------|
| Contract architecture | Solidity Lead | Sagix | Auditor | Team |
| Pool compositions & weights | Sagix | Sagix | Solidity Lead | Team |
| Audit firm selection | Sagix | Sagix | Solidity Lead | Team |
| Go/No-Go for mainnet | All | Sagix | Auditor | Community |
| Frontend UX decisions | Frontend Lead | Sagix | — | Team |
| Emergency pause execution | On-call engineer | Sagix | Solidity Lead | Team |
| Token parameter changes | N/A (immutable) | N/A | N/A | N/A |
