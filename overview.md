# Overview

*Project Aureum at a glance.*

---

## How to Read This Documentation

Two tracks, depending on what you need:

**LP / Investor track** — understand the opportunity and the economics:

| Step | File | What you learn |
|:-----|:-----|:---------------|
| 1 | `overview.md` (this file) | Protocol character, team, risk factors |
| 2 | `aureum_mental_model.md` | Three-layer architecture, emission regimes, constellation routing |
| 3 | `tokenomics.md` §ix–x | Token design, fee splits, value capture, deflationary crossover |
| 4 | Any pool profile in `miliarium_profiles/` | Composition, sector thesis, volume drivers for one pool |
| 5 | `appendices.md` §xxxvii, §xxxix | Why fair-launch AMMs failed before and how Aureum differs; competitive position |

**Builder / Auditor track** — understand the contract logic and formal rules:

| Step | File | What you learn |
|:-----|:-----|:---------------|
| 1 | `theoretical_foundation.md` | Research foundations, CCB narrative, multiplier engine — read this first for context on the systems the other files formalize |
| 2 | `constitution.md` | Immutable parameters, governance scope, emission operating rules |
| 3 | `formulas.md` | Every formula: EMA, CCB score, multiplier update, governance power |
| 4 | `bootstrap.md` §xxi–xxv | Anti-gaming engine, Incendiary Boost, gauge gating |
| 5 | `appendices.md` §xxxvi | AMM architecture provenance, audit scope |

### File index

| File | Purpose | Primary audience |
|:-----|:--------|:-----------------|
| `overview.md` | Protocol at a glance — character, team, risks | Everyone |
| `aureum_mental_model.md` | Conceptual architecture: thesis, principles, three layers, emission regimes, routing | LP / Investor |
| `tokenomics.md` | Token design, emission schedule, fee splits, governance model, value capture | LP / Investor |
| `theoretical_foundation.md` | Research foundations, CCB allocation narrative, multiplier engine | Builder / Auditor |
| `formulas.md` | Formal definitions of every protocol formula | Builder / Auditor |
| `constitution.md` | Immutable operating law: governance scope, emission rules, parameter list | Builder / Auditor |
| `bootstrap.md` | Pool bootstrapping: gauge gating, Incendiary Boost, anti-gaming criteria | Builder / Auditor |
| `transitions.md` | Month-by-month launch timeline from equal through CCB | Both |
| `Miliarium_Aureum.md` | Canonical registry of the 28 Miliarium pools: compositions, sector tables | Both |
| `miliarium_profiles/` | One profile per pool plus manifest and sector taxonomy | LP / Investor |
| `aureum_glossary.md` | Term definitions and system summaries | Both |
| `appendices.md` | AMM architecture, fair-launch analysis, Yield Basis, competitive position | Both |

---

## Protocol Character

- Fair launch
- Immutable from block 0
- No multisig
- No admin keys
- No voting over emissions
- Oracle-free core operation

## Treasury

- Treasury revenue is stablecoin-denominated protocol revenue.
- Treasury custody is fully on-chain and non-custodial from genesis.
- No founding-team signer, council, or progressive decentralization phase.
- Treasury spending is governance-gated (qualified AuMT vote + timelock), with no multisig path.

## Emission Regime

- **Through end of Month 10:** equal **1/28** split across the 28 Miliarium pools.
- **Months 11–12:** linear transition from equal to CCB (Continuous Central Bank — the protocol's fully automatic emission allocator; see `aureum_glossary.md`). **α** from 0 to 1; **α = 0.5** at the midpoint — half equal, half CCB.
- **After Year 1:** pure CCB — **TVL EMA(60) × CCB multiplier** scores, normalized across eligible pools. Incendiary Boost is a separate priority skim. See `constitution.md` §xxviii–xxix for the full rules and immutable parameters.
- No governance voting controls emission allocation.

## Governance (Non-Emission)

- Gauge proposal and gauge challenge votes are active.
- Treasury and fee proposals are active within immutable bounds.
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

See Immutable Parameters (`constitution.md` §xxix).
