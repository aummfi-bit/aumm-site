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

## Risk Notes

- New tokenomics and automation contracts still require full audit.
- Early TVL bootstrapping remains execution-sensitive.

See Immutable Parameters in `constitution.md`.
