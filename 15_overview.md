# Overview

*Project Aureum at a glance.*

---

## How to Read This Documentation

Two tracks, depending on what you need:

**LP / Investor track** — understand the opportunity and the economics:

| Step | File | What you learn |
|:-----|:-----|:---------------|
| 1 | [Overview](15_overview.md) (this file) | Protocol character, team, risk factors |
| 2 | [Mental model](02_mental_model.md) | Three-layer architecture, emission regimes, constellation routing |
| 3 | [Tokenomics](04_tokenomics.md) §ix–x | Token design, fee splits, value capture |
| 4 | Any pool profile in [miliarium_profiles/](miliarium_profiles/) | Composition, sector thesis, volume drivers for one pool |
| 5 | [Appendices](13_appendices.md) §xxxvii, §xxxix | Why fair-launch AMMs failed before and how Aureum differs; competitive position |

**Builder / Auditor track** — understand the contract logic and formal rules:

| Step | File | What you learn |
|:-----|:-----|:---------------|
| 1 | [Theoretical foundations](03_theoretical_foundation.md) | Research foundations, CCB narrative, multiplier engine — read this first for context on the systems the other files formalize |
| 2 | [Constitution](10_constitution.md) | Immutable parameters, governance scope, emission operating rules |
| 3 | [Protocol formulas](11_formulas.md) | Every formula: EMA, CCB score, multiplier update, governance power |
| 4 | [Bootstrap](08_bootstrap.md) §xxi–xxv | Anti-gaming engine, Incendiary Boost, gauge gating |
| 5 | [Appendices](13_appendices.md) §xxxvi | AMM architecture provenance, audit scope |

### File index

| File | Purpose | Primary audience |
|:-----|:--------|:-----------------|
| [Overview](15_overview.md) | Protocol at a glance — character, team, risks | Everyone |
| [Mental model](02_mental_model.md) | Conceptual architecture: thesis, principles, three layers, emission regimes, routing | LP / Investor |
| [Tokenomics](04_tokenomics.md) | Token design, emission schedule, fee splits, governance model, value capture | LP / Investor |
| [Theoretical foundations](03_theoretical_foundation.md) | Research foundations, CCB allocation narrative, multiplier engine | Builder / Auditor |
| [Protocol formulas](11_formulas.md) | Formal definitions of every protocol formula | Builder / Auditor |
| [Constitution](10_constitution.md) | Immutable operating law: governance scope, emission rules, parameter list | Builder / Auditor |
| [Bootstrap](08_bootstrap.md) | Pool bootstrapping: gauge gating, Incendiary Boost, anti-gaming criteria | Builder / Auditor |
| [Transition rules](09_transitions.md) | Month-by-month launch timeline from equal through CCB | Both |
| [Miliarium Aureum registry](05_miliarium_aureum.md) | Canonical registry of the 28 Miliarium pools: compositions, sector tables | Both |
| [miliarium_profiles/](miliarium_profiles/) | One profile per pool plus manifest and sector taxonomy | LP / Investor |
| [Glossary](12_aureum_glossary.md) | Term definitions and system summaries | Both |
| [Appendices](13_appendices.md) | AMM architecture, fair-launch analysis, Yield Basis, competitive position | Both |

---

## Protocol Character

- Fair launch
- Immutable from block 0
- No multisig
- No admin keys
- No voting over emissions
- Oracle-free core operation

## No Treasury

There is no treasury. All protocol revenue flows automatically to one immutable destination:

- **der Bodensee Pool** — **protocol-captured** revenue: **50% of swap fees on other pools** + **100% of ERC-4626 yield fees** as one-sided svZCHF inflows; **0.75%** swap fee on **trades inside der Bodensee** stays **in pool** for der Bodensee LPs.

The remaining **50%** of swap fees on **those other pools** returns directly to their LPs as LP bonus. No founding-team signer, council, or progressive decentralization phase. No wallet receives AuMM for discretionary use — **Months 1–10** bootstrap AuMM is one-sided into der Bodensee Pool only (see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)). The system is a Continuous Capital Corporation (CCC) from block 0.

## Emission Regime

- **Through end of Month 10:** each block, a **decaying der Bodensee bootstrap** (80% at genesis → 0% at end of Month 10) is minted as one-sided AuMM into der Bodensee Pool; the **LP tranche** is split **1/28** across the 28 Miliarium pools. **100% of the LP tranche** goes to LPs from block 0 — no treasury share.
- **Months 11–12:** linear transition from equal to CCB (Continuous Central Bank — the protocol's fully automatic emission allocator; see [Glossary](12_aureum_glossary.md)). **α** from 0 to 1; **α = 0.5** at the midpoint — half equal, half CCB.
- **After Year 1:** pure CCB — **TVL EMA(60) × CCB multiplier** scores, normalized across eligible pools. Incendiary Boost is a priority skim on the LP tranche. See [Constitution (§§xxviii–xxix)](10_constitution.md) for the full rules and immutable parameters.
- No governance voting controls emission allocation.

## Governance (Non-Emission)

- Gauge proposal and gauge challenge votes are active.
- Fee proposals are active within immutable bounds.
- All proposals must reference verifiable on-chain data only.

## Founding Team

| Role | Contributor | Brings |
|------|------------|--------|
| Architecture & Thesis | **Sagix** | Pool design, routing topology, aggregator relationships, cross-protocol integrations (Frankencoin, Reserve), published research |
| Smart Contracts | **TBD** | Solidity expertise, governance vault infrastructure, Balancer V3 codebase familiarity |
| Frontend & UX | **TBD** | Frontend experience, emission dashboard, LP interface |
| Founding Liquidity | **TBD** (aligned capital partner) | Seed capital for genesis pools, long-term LP commitment |

The founding team earns tokens by being early LPs — same mechanism as everyone else. The only advantage is being first: deploying pools, providing initial liquidity, and earning the highest emission rate before anyone else arrives. As more LPs join, per-LP emissions decline. Early believers rewarded. No allocation. No vesting.

## Risk Factors

- **Fork risk.** Aequilibrium (the protocol's AMM engine, derived from Balancer V3's Certora-verified contracts) inherits Balancer V3's smart contract security via byte-identical pool contracts, but the new tokenomics contracts require independent audit. Until audited, the new code carries unverified risk.
- **Liquidity risk.** Genesis pools will have minimal TVL. Bootstrapping requires the founding team's capital and early LP adoption. If depth doesn't reach aggregator thresholds, the routing thesis never activates.
- **Regulatory risk.** Fair-launch tokens with no pre-mine have the strongest regulatory position (no securities argument), but the regulatory landscape is uncertain.
- **Team risk.** Founding team is small and self-funded. Key-person dependency is high in early phases.
- **Market risk.** Launching during a bear market or period of DeFi apathy could delay adoption regardless of architectural merit.

See [Immutable Parameters (§xxix)](10_constitution.md).
