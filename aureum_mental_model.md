# Aureum Protocol

> Imagine mining BTC with capital, not electricity.  
> Imagine BTC backed by an autonomous reserve funded by real fees.  
> Imagine your capital is liquidity generating real fees that deepen the reserve behind the scarce token.  
> Meet $AuMM.

## i. One Line

An immutable fair-launch AMM where emissions follow fixed Bitcoin-style issuance and automatic on-chain allocation only.

## The Thesis

The best AMM architecture in DeFi is about to lose its growth mechanism. The token is priced for terminal decline. But the code is open source, formally verified, and architecturally superior to every competitor. Project Aureum takes that code, replaces the broken tokenomics with a fair launch where the only way to earn tokens is to provide liquidity to productive pools, and lets the market discover what formally verified multi-asset pools can do when the economic layer is designed correctly. The experiment hasn't failed. It hasn't happened.

## Why This Exists

Balancer V3 is the most advanced AMM architecture in DeFi — multi-asset weighted pools, ERC-4626 native yield, hooks, formal verification by Certora. But the protocol's tokenomics failed. Emissions directed to legacy pools and governance staking created circular economics. Meta-governance capture concentrated power. The founding entity shut down. The team proposed eliminating emissions entirely — removing the only mechanism through which external builders could bootstrap new infrastructure.

The architecture deserves a second chance under a clean economic model. Project Aureum forks the V3 smart contracts and replaces the tokenomics with a fair launch. Same verified core. Fundamentally different economics. See `appendices.md` for a detailed comparison to every historical fair-launch failure mode, Yield Basis Hybrid Vaults, and the competitive position against Uniswap, Curve, Aerodrome, and proprietary AMMs.

## ii. Core Principles

- **Fair launch.** No pre-mine, no team allocation, no VC, **no treasury wallet**. **100% of the LP emission tranche** goes to LPs from block 0; **Months 1–10** a decaying share is one-sided AuMM into der Bodensee Pool (see `formulas.md` F-0).
- **Fixed supply.** 21,000,000 maximum. Per-block halving schedule. Declining emission rate.
- **Mining is LP.** Productive capital in, tokens out. No staking rewards or bribe markets.
- **Anti-capture by design.** Governance power derives exclusively from active LP positions with a 6-month on-ramp.
- **Ethereum only.** Single chain for maximum composability and aggregator coverage.
- **Immutable.** No multisig, no admin keys, no upgradeability, no pause. No emission voting; governance exists only for non-emission actions.
- **Continuous Capital Corporation.** Fully autonomous, rule-based system — no discretionary treasury, no manual intervention. Capital allocation (CCB) and reserve management (der Bodensee Pool) are algorithmic and on-chain. Aligned with Meisser's CCC thesis and Frankencoin's implementation.

## The Roman Infrastructure

The protocol's naming follows the architecture of Roman infrastructure — because the design follows it too.

The **Miliarium Aureum** (Golden Milestone) was the monument in the Roman Forum from which all distances in the Empire were measured. Every road radiated from it. In this protocol, the Miliarium Aureum is the founding constellation of 28 pools — the routing hub that connects every pool through cross-pool arbitrage, shared aggregator paths, and deeper effective liquidity.

**AuMM** (Aureum Market Maker) is the reward token — mined by providing liquidity, backed by protocol revenue flowing into der Bodensee Pool. BTC-style scarcity.

**AuMT** (Aureum Market Tessera) is the proof-of-participation token — your tessera. In Rome, a tessera was a small tablet that served as a ticket, a voucher, or a token of identity. It proved you belonged and carried rights: entry, grain distribution, voting in assemblies. Your AuMT proves your stake in the protocol's liquidity and carries the same rights — emissions, governance power, LP bonus eligibility.

**Aequilibrium** is the AMM engine — Latin for "equal balance." The pool layer that powers every trade, every arb, every routing path. Derived from Balancer V3's Certora-verified smart contracts, reborn under a new economic model.

*All roads lead to the Miliarium Aureum. Your tessera proves you helped build them.*

### The Miniature Economy

The 28 Miliarium pools are not a random collection of liquidity venues — they are structured as a **miniature economy**. Each pool represents a distinct asset class or market segment found in traditional finance (yield, bonds, crypto infrastructure, equities, metals), mapped onto on-chain primitives. When tech sells off, capital rotates to treasuries or gold; the protocol captures fees on both legs. When DeFi booms, crypto infrastructure pools surge; the rest stay productive through native ERC-4626 yield. Sector rotation dynamics, aggregator diversity, and correlation hedging ensure that even in the worst macro environment, some sectors generate fees. See `miliarium_profiles/sectors.md` for the full taxonomy.

**Why 28 pools.** Twenty-eight is large enough to span five distinct asset classes and weather macro rotation without any single sector dominating the constellation, yet small enough for the CCB multiplier engine to track each pool’s TVL individually on-chain every bi-weekly cycle. Fewer pools would leave sector gaps that concentrate risk; more would dilute the EMA signal and increase gas costs for per-pool multiplier updates. The number is immutable from block 0 — see `constitution.md` §xxix.

**The 28 are a blueprint, not the full economy.** The Miliarium pools anchor the CCB engine and guarantee structural fee generation across asset classes from genesis — but they are not meant to exhaust every possible token or market. Pool creation is permissionless, gauge approval has a clear mechanism (`bootstrap.md` §xxi), and emissions flow to any gauged pool per the standard CCB rules. If a stablecoin, tokenized RWA, or crypto token is missing from the 28, the path is a new pool and a gauge vote — not a composition challenge. The community is encouraged to monitor the market for new opportunities (emerging stablecoins, new tokenized equity or bond wrappers, crypto tokens with meaningful volume) and expand the ecosystem. The Miliarium system is plug-and-play: new pools route through the constellation’s connectors (ixEdelweiss, ixLibertas, ixCambio), generate yield from ERC-4626 vaults, and bootstrap via Incendiary and gauge boost mechanics — the same infrastructure the 28 founding pools use.

## iii. How Aureum Works — Three Layers

### 1. Capital Allocation (The Continuous Central Bank)

Which pools should receive emissions right now? Base weight = 60-day EMA of on-chain TVL (see `theoretical_foundation.md` §vi). The 28 Miliarium pools carry an algorithmic CCB multiplier (see `constitution.md` §xxix for bounds) that nudges their share based on TVL trends — no voting, no human override. Strictly zero-sum: total emissions are fixed by the halving schedule. Sustained capital commitment is rewarded. Short-term hype is ignored. Market crashes trigger higher relative yield (anticyclical floor). Think of it as a central bank that automatically rewards persistent liquidity, not speculation. All protocol-captured fee revenue flows to der Bodensee Pool (the autonomous reserve) as one-sided svZCHF inflows — there is no separate treasury.

### 2. Bootstrapping (Starting New Pools)

New pools have no EMA history, so they need a structured path to earn emissions. Two stacked mechanisms: (a) **Incendiary Boost** — operator escrows svZCHF/sUSDS into der Bodensee Pool; the protocol emits AuMM to the pool over 30 days as a supplementary stream pegged to the 85th efficiency percentile; must remain efficient to renew. (b) **90-day gauge boost** — new gauges receive a fixed 1.2x CCB multiplier for 90 days, expiring automatically with no vote and no renewal. After ~90 days, emissions depend purely on real TVL via the CCB. The flow: conviction (Incendiary) → cold-start ramp (gauge boost) → long-term reality (EMA).

### 3. Discipline (Keeping the System Clean)

Aureum continuously filters unproductive pools. Volume percentile floor: must stay above minimum activity threshold. Efficiency tournament: revenue-per-emission ranking; bottom 15% capped, excess redistributed to productive pools. Graduated enforcement: warning zone before disqualification, gauge revocation after 4 consecutive epochs. Dead or extractive pools lose emissions or are removed entirely.

### 4. Constellation Routing

Twenty-six of the 28 Miliarium pools hold **ixEDEL** as a routing anchor (typically 16% of weight; ixAetheron uses 15% due to its non-standard ETH-native yield core). When a trader swaps between any two pools — say ixAurebit (wrapped BTC) to ixEquitix (equities) — the trade routes through ixEDEL: pool A sells ixEDEL, ixEdelweiss reprices it, pool B buys ixEDEL. Fees are generated on **both legs** of the route, and the shared token creates a continuous arbitrage surface that aggregators exploit 24/7.

**ixEdelweiss (slot 05)** is the routing hub — the Miliarium Aureum monument itself. It holds 46% ixEDEL and exists primarily for price discovery and deep cross-pool routing. The other 25 ixEDEL-holding pools are spokes: they each carry a 16% ixEDEL anchor that connects them to the hub and to each other.

**ixLibertas (slot 06)** is the exception — the USD stable hub holds no ixEDEL. It serves as a standalone stablecoin routing venue (seven USD-denominated stables), providing a direct USD on-ramp without the volatility of the ixEDEL routing path. Not every trade needs to cross the ixEDEL bridge; pure stablecoin flows route through ixLibertas instead.

In Roman terms: **ixEDEL is the via** (the road that connects every province), **ixEdelweiss is the Miliarium Aureum** (the golden milestone from which every road is measured), and **each pool is a province** connected by the shared road network.

## iv. Emission Regimes

- **Through end of Month 10:** each block, **der Bodensee bootstrap** AuMM (80% at genesis, linear decay to 0% by end of Month 10) is deposited one-sided into der Bodensee Pool. The **LP tranche** goes **100%** to the 28 Miliarium pools, split **purely equal** (**1/28 of the LP tranche** each). No treasury share. Other pools may exist but do not receive this equal tranche.
- **Months 11–12 (two-month transition):** blend linearly from equal to CCB over the window. At the midpoint, the mix is half equal and half CCB. See `formulas.md` for the blend formula.
- **After Year 1:** emissions follow only the CCB — each pool scored by smoothed TVL and CCB multiplier, normalized across eligible pools. No vote. See `constitution.md` and `formulas.md`.

**Why equal first.** The equal regime gives all 28 Miliarium pools identical treatment regardless of TVL — intentional, because the EMA needs approximately 60 days of on-chain data before it produces a meaningful signal. Allocating by TVL from block 0 would reward whichever pool attracted the earliest whale, not sustained capital. Equal allocation bootstraps the entire constellation before the EMA has real data to work with.

**Why a two-month transition.** An abrupt switch from equal to CCB at a single block would cause overnight emission shocks — pools that were receiving 1/28 could suddenly receive much more or much less. The two-month linear blend gives LPs and operators time to observe the CCB’s scoring in real time and adjust positions. Pools that performed well under equal allocation may see their share decline if their TVL lags the protocol average; pools that attracted deep, sticky capital will see their share rise. This is by design — the transition rewards sustained capital commitment, not historical incumbency.

