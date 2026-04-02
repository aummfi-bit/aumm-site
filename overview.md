# Overview

*Project Aureum — the protocol at a glance.*

---

## Proof of Real Yield Dashboard

The aumm.fi frontend displays per-pool yield transparency that reframes how LPs evaluate returns:

**Per pool, the dashboard shows:**
- **Real yield %** — the portion of returns from swap fees + ERC-4626 vault yield (non-inflationary sources)
- **Emission yield %** — the portion from AuMM emissions (inflationary)
- **Efficiency score** — the pool's efficiency ratio vs. protocol average
- **Revenue per $1 of emissions** — how much protocol revenue each dollar of emission generates

**The framing:**

*"This pool earns 68% of returns from real yield, not inflation."*

Most AMMs report a single blended APR that mixes real revenue with token emissions. LPs see "80% APR" without knowing that 75% of it is inflation that dilutes the token they're earning. Aureum separates the two, making the quality of returns visible.

This is a competitive weapon. When an Aerodrome LP compares "80% APR" against Aureum's "12% real yield + 15% emission yield," the conversation shifts from "which number is bigger" to "which return is sustainable." Lower headline APR, higher quality return. The dashboard makes that argument visually without saying a word about competitors.

---

## Founding Team

| Role | Contributor | Brings |
|------|------------|--------|
| Architecture & Thesis | **Sagix** | Pool design, routing topology, aggregator relationships, cross-protocol integrations (Frankencoin, Reserve), published research |
| Smart Contracts | **TBD** | Solidity expertise, governance vault infrastructure, Balancer V3 codebase familiarity |
| Frontend & UX | **TBD** | Frontend experience, emission dashboard, LP interface |
| Founding Liquidity | **TBD** (aligned capital partner) | Seed capital for genesis pools, long-term LP commitment |

**The founding team earns tokens by being early LPs.** Same mechanism as everyone else. The only advantage is being first — deploying pools, providing initial liquidity, and earning the highest emission rate before anyone else arrives. As more LPs join, per-LP emissions decline. Early believers rewarded. No allocation. No vesting.

---

## Treasury

### Source

Protocol fee revenue flows to the treasury as defined in the **Value Capture** section (25% of swap fees + 75% of ERC-4626 yield fees). These are **stablecoin revenues** — the treasury's operating budget.

**The treasury never sells AuMM to fund operations.** AuMM received during the treasury emission phase (months 0–10) is used exclusively for protocol-owned liquidity: seeding the AuMM trading pool at month 6 and operating the price ceiling stabilization mechanism (months 6–10). Stabilization sale proceeds are deposited as permanently locked liquidity in Mercatūs Praecursorii — not converted to stablecoins for team spending. All leftover AuMM is burned at month 10. After month 10, the treasury never receives AuMM again. Development, audits, and operations are funded entirely from stablecoin fee revenue. This is the "no team allocation" guarantee: the team cannot extract value through AuMM sales.

### Use

| Category | Allocation | Notes |
|----------|-----------|-------|
| Audits & Security | 40% | Ongoing audit coverage, bug bounties, formal verification |
| Development | 30% | Smart contract maintenance, frontend, integrations |
| Operations | 20% | Infrastructure, RPC, subgraph, monitoring |
| Reserve | 10% | Emergency fund |

### Governance

Treasury spending requires governance vote (AuMT-weighted, qualified pool LPs only). No single party controls treasury. Multi-sig with founding team members initially, transitioning to LP-elected council after Year 1.

---

## Risk Factors

**Fork risk.** Aequilibrium inherits Balancer V3's smart contract security via byte-identical pool contracts, but the new tokenomics contracts require independent audit. Until audited, the new code carries unverified risk.

**Liquidity risk.** Genesis pools will have minimal TVL. Bootstrapping requires the founding team's capital and early LP adoption. If depth doesn't reach aggregator thresholds, the routing thesis never activates.

**Regulatory risk.** Fair-launch tokens with no pre-mine have the strongest regulatory position (no securities argument), but the regulatory landscape is uncertain.

**Balancer response.** Balancer could modify their revamp to preserve emissions, making the fork less necessary. Or they could challenge the fork through non-legal means (community pressure, aggregator lobbying).

**Team risk.** Founding team is small and self-funded. Key-person dependency is high in early phases.

**Market risk.** Launching during a bear market or period of DeFi apathy could delay adoption regardless of architectural merit.
