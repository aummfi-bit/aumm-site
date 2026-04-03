# Aureum Protocol

> Imagine mining BTC with capital, not electricity.  
> Imagine BTC with a buy back and burn program sponsored by real fees.  
> Imagine your capital is liquidity generating real fees that buy back and burn the scarce token.  
> Meet $AuMM.

## The Thesis

The best AMM architecture in DeFi is about to lose its growth mechanism. The token is priced for terminal decline. But the code is open source, formally verified, and architecturally superior to every competitor. Project Aureum takes that code, replaces the broken tokenomics with a fair launch where the only way to earn tokens is to provide liquidity to productive pools, and lets the market discover what formally verified multi-asset pools can do when the economic layer is designed correctly. The experiment hasn't failed. It hasn't happened.

## Why This Exists

Balancer V3 is the most advanced AMM architecture in DeFi — multi-asset weighted pools, ERC-4626 native yield, hooks, formal verification by Certora. But the protocol's tokenomics failed. Emissions directed to legacy pools and governance staking created circular economics. Meta-governance capture concentrated power. The founding entity shut down. The team proposed eliminating emissions entirely — removing the only mechanism through which external builders could bootstrap new infrastructure.

The architecture deserves a second chance under a clean economic model. Project Aureum forks the V3 smart contracts and replaces the tokenomics with a fair launch. Same verified core. Fundamentally different economics. See `appendices.md` for a detailed comparison to every historical fair-launch failure mode, Yield Basis Hybrid Vaults, and the competitive position against Uniswap, Curve, Aerodrome, and proprietary AMMs.

## i. One Line

An immutable fair-launch AMM where emissions follow fixed Bitcoin-style issuance and automatic on-chain allocation only.

## ii. Core Principles

- **Fair launch.** No pre-mine, no team allocation, no VC. Treasury emission phase (months 0–10) seeds protocol-owned liquidity only.
- **Fixed supply.** 21,000,000 maximum. Per-block halving schedule. Declining emission rate.
- **Mining is LP.** Productive capital in, tokens out. No staking rewards or bribe markets.
- **Anti-capture by design.** Governance power derives exclusively from active LP positions with a 6-month on-ramp.
- **Ethereum only.** Single chain for maximum composability and aggregator coverage.
- **Immutable.** No multisig, no admin keys, no upgradeability, no pause. No emission voting; governance exists only for non-emission actions.

## The Roman Infrastructure

The protocol's naming follows the architecture of Roman infrastructure — because the design follows it too.

The **Miliarium Aureum** (Golden Milestone) was the monument in the Roman Forum from which all distances in the Empire were measured. Every road radiated from it. In this protocol, the Miliarium Aureum is the founding constellation of 28 pools — the routing hub that connects every pool through cross-pool arbitrage, shared aggregator paths, and deeper effective liquidity.

**AuMM** (Aureum Market Maker) is the reward token — mined by providing liquidity, burned by the protocol. BTC-style scarcity.

**AuMT** (Aureum Market Tessera) is the proof-of-participation token — your tessera. In Rome, a tessera was a small tablet that served as a ticket, a voucher, or a token of identity. It proved you belonged and carried rights: entry, grain distribution, voting in assemblies. Your AuMT proves your stake in the protocol's liquidity and carries the same rights — emissions, governance power, LP bonus eligibility.

**Aequilibrium** is the AMM engine — Latin for "equal balance." The pool layer that powers every trade, every arb, every routing path. Derived from Balancer V3's Certora-verified smart contracts, reborn under a new economic model.

*All roads lead to the Miliarium Aureum. Your tessera proves you helped build them.*

## iii. Emission Regimes

- **Through end of Month 10:** emissions to the 28 immutable Miliarium Aureum pools are **purely equal** (**1/28** each). Other pools may exist but do not receive this equal tranche.
- **Months 11–12 (two-month transition):** blend linearly from equal to CCB over the window. At the midpoint, the mix is half equal and half CCB. See `formulas.md` for the blend formula.
- **After Year 1:** emissions follow only the CCB — each pool scored by smoothed TVL and CCB multiplier, normalized across eligible pools. No vote. See `constitution.md` and `formulas.md`.

## iv. Why It Matters

The protocol minimizes human discretion and maximizes deterministic execution. Allocation follows capital behavior, not governance behavior.

Proposal governance is still active for gauges, treasury, and fee proposals, and must rely on on-chain verifiable data only.

See Immutable Parameters in `constitution.md`.