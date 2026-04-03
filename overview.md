# Overview

*Project Aureum at a glance.*

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

- **Through end of Month 10:** equal **1/28** split across the 28 Miliarium Aureum pools.
- **Months 11–12:** linear transition from equal to CCB (**α** from 0 to 1; **α = 0.5** at the midpoint — half equal, half CCB).
- **After Year 1:** pure CCB — **TVL EMA(60) × CCB multiplier** scores, normalized across eligible pools. Incendiary Boost is a separate priority skim (see `constitution.md`).
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

- **Fork risk.** Aequilibrium inherits Balancer V3's smart contract security via byte-identical pool contracts, but the new tokenomics contracts require independent audit. Until audited, the new code carries unverified risk.
- **Liquidity risk.** Genesis pools will have minimal TVL. Bootstrapping requires the founding team's capital and early LP adoption. If depth doesn't reach aggregator thresholds, the routing thesis never activates.
- **Regulatory risk.** Fair-launch tokens with no pre-mine have the strongest regulatory position (no securities argument), but the regulatory landscape is uncertain.
- **Team risk.** Founding team is small and self-funded. Key-person dependency is high in early phases.
- **Market risk.** Launching during a bear market or period of DeFi apathy could delay adoption regardless of architectural merit.

See Immutable Parameters in `constitution.md`.
