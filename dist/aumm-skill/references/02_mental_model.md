<!-- GENERATED FROM aumm-site@dd5fd5f210483395ca105ac7449c0a2202ed2a7f 02_mental_model.md — DO NOT EDIT -->
# Aureum Protocol

> **AuMM** is earned by **liquidity**: capital in productive pools, not hashrate or proof-of-work.  
> **Issuance** follows a **Bitcoin-style** schedule: **21M hard cap**, **4 year halving**. 
>
> The token is **AuMM**, on Ethereum.  
> Your capital is the liquidity at Aureum AMM. 
>
>
> The fees it generates deepen **der Bodensee**, the reserve behind the scarce token.  
>
>
> **Meet $AuMM**.

## i. One Line

An immutable fair-launch AMM with fixed Bitcoin-style issuance for **AuMM** and fully automatic on-chain allocation.

## i-a. The Thesis

The best AMM architecture in DeFi is about to lose its growth mechanism. The token is priced for terminal decline. But the code is open source, formally verified, and architecturally superior to every competitor. Project Aureum takes that code and replaces the broken tokenomics with a fair launch — the only way to earn tokens is to provide liquidity to productive pools. Let the market discover what formally verified multi-asset pools can do when the economic layer isn't sabotaged. The experiment hasn't failed. It hasn't happened.

## i-b. Why This Exists

Balancer V3 is the most advanced AMM architecture in DeFi: multi-asset weighted pools, ERC-4626 native yield, hooks, formal verification by Certora. The tokenomics failed anyway. Emissions went to legacy pools and governance staking — circular economics. Meta-governance capture concentrated power. The founding entity shut down. The team's last proposal: eliminate emissions entirely, removing the only mechanism external builders had to bootstrap new infrastructure.

The architecture deserves a second run under a clean economic model. Project Aureum forks the V3 smart contracts and replaces the tokenomics with a fair launch. Same verified core. Different economics. See [Appendices](13_appendices.md) for a detailed comparison to historical fair-launch failure modes, Yield Basis Hybrid Vaults, and competitive positioning against Uniswap, Curve, Aerodrome, and proprietary AMMs.

## ii. Core Principles

- **Fair launch.** No pre-mine, no team allocation, no VC, **no treasury wallet**. **100% of the LP emission tranche** goes to LPs from block 0; **Months 1–10** a piecewise-decaying share enters der Bodensee Pool as one-sided AuMM (80%→50% by Month 6, 50%→0% by Month 10; see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)).
- **Fixed supply.** 21,000,000 maximum. Per-block halving schedule. Declining emission rate.
- **Mining is LP.** Productive capital in, tokens out. No staking rewards. No bribe markets.
- **Anti-capture by design.** Governance power derives exclusively from active LP positions with a 6-month on-ramp.
- **Ethereum only.** Single chain. Maximum composability and aggregator coverage.
- **Immutable.** No multisig, no admin keys, no upgradeability, no pause. No emission voting; governance exists only for non-emission actions.
- **Continuous Capital Corporation.** Fully autonomous, rule-based — no discretionary treasury, no manual intervention. Capital allocation (CCB) and reserve management (der Bodensee Pool) are algorithmic and on-chain. Aligned with Dr. Luzius Meisser's CCC thesis and Frankencoin's implementation.

## ii-a. The Roman Infrastructure

The protocol's naming follows Roman infrastructure because the design does too.

The **Miliarium Aureum** (Golden Milestone) was the monument in the Roman Forum from which all distances in the Empire were measured. Every road radiated from it. Here, the Miliarium Aureum is the founding constellation of 28 pools — the routing hub connecting every pool through cross-pool arbitrage, shared aggregator paths, and deeper effective liquidity.

**AuMM** (Aureum Market Maker) is the reward token — mined by providing liquidity, backed by protocol revenue flowing into der Bodensee Pool. BTC-style scarcity.

**AuMT** (Aureum Market Tessera) is the proof-of-participation token. In Rome, a tessera was a small tablet — ticket, voucher, proof of identity. It proved you belonged and carried rights: entry, grain rations, assembly votes. Your AuMT proves your stake in the protocol's liquidity and carries equivalent rights: emissions and governance power.

**Aequilibrium** is the AMM engine — Latin for "equal balance." The pool layer powering every trade, every arb, every routing path. Balancer V3's Certora-verified smart contracts, reborn under a new economic model.

*All roads lead to the Miliarium Aureum. Your tessera proves you helped build them.*

### The Miniature Economy

The 28 Miliarium pools are structured as a **miniature economy**, not a random collection of liquidity venues. Each pool maps a distinct asset class from traditional finance — yield, bonds, crypto infrastructure, equities, metals — onto on-chain primitives. When tech sells off, capital rotates to treasuries or gold; the protocol captures fees on both legs. When DeFi booms, crypto infrastructure pools surge; the rest stay productive through native ERC-4626 yield. Sector rotation and correlation hedging mean that even in the worst macro environment, some sectors generate fees. See [Miliarium sectors](07_miliarium_sectors.md) for the full taxonomy.

**Why 28 pools.** Large enough to span five asset classes and weather macro rotation without one sector dominating. Small enough for the CCB multiplier engine to track each pool’s TVL on-chain every bi-weekly cycle. Fewer pools leave sector gaps that concentrate risk; more dilute the EMA signal and raise gas costs for per-pool multiplier updates. The number is immutable from block 0 — see [Constitution (§xxix)](10_constitution.md).

**The 28 are a blueprint, not the full economy.** The Miliarium pools anchor the CCB engine and guarantee structural fee generation across asset classes from genesis, but they don’t exhaust every token or market. Pool creation is permissionless, gauge activation is permissionless once eligibility criteria are met ([Bootstrap §xxi](08_bootstrap.md)), and emissions flow to any gauged pool per standard CCB rules. Missing a stablecoin, tokenized RWA, or crypto token? The path is a new pool and permissionless gauge activation — not a redesign. New pools route through the constellation’s connectors (ixEdelweiss, ixLibertas, ixCambio), generate yield from ERC-4626 vaults, and bootstrap via Incendiary Boost — the same user-funded cold-start mechanism available to every gauged pool.

**Vault-Class Registry — the single discretionary surface.** Gauge activation, pool creation, and emission allocation are permissionless or mechanical; none rely on a vote. Class admission is the one exception: which ERC-4626 vault classes count toward the Quality Gate (the 52% wrapped-yield numerator that governs whether a pool's composition qualifies for full CCB scoring). The Vault-Class Registry runs a Frankencoin-style proposal + veto loop — anyone may propose a new class, AuMT holders veto within a fixed window, and unvetoed proposals auto-finalize without a positive vote. Three admission fingerprints — `ImplementationAddress`, `FactoryAddress`, `BytecodeHash` — match how ERC-4626 vaults deploy in practice. The genesis class set is hard-coded at construction. This is the only place governance exercises substantive class-admission discretion — see [Constitution (§xxix)](10_constitution.md).

## iii. How Aureum Works — Three Layers

### 1. Capital Allocation (The Continuous Central Bank)

Which pools should receive emissions right now? Base weight = 60-day EMA of on-chain TVL (see [Theoretical foundations (§vi-b)](03_theoretical_foundation.md)). The 28 Miliarium pools carry an algorithmic CCB multiplier ([Constitution §xxix](10_constitution.md) for bounds) that nudges their share based on TVL trends — no voting, no human override. Zero-sum: total emissions are fixed by the halving schedule. Sustained capital commitment is rewarded; short-term hype is not. Market crashes trigger higher relative yield (anticyclical floor). A central bank that automatically rewards persistent liquidity, not speculation. **Miliarium** LP returns include **AuMM emissions**, **ERC-4626 native yield**, and **~50%** of swap fees charged on the pool (the Vault LP residual); the **other ~50%** is the protocol share the hook routes to der Bodensee (**100%** of that leg). **Der Bodensee** LPs **additionally** earn the **full in-pool swap-fee tier** on the three-token pool (e.g. **0.75%** at genesis). **Protocol-captured** fee revenue (protocol swap share + yield skim) flows to der Bodensee Pool as one-sided stablecoin (sUSDS/svZCHF) inflows; **swap fees on trades inside der Bodensee** stay **in pool** in full for der Bodensee LPs — no separate treasury.

### 2. Bootstrapping (Starting New Pools)

New pools have no EMA history, so they need a path to earn emissions. **Incendiary Boost** is the cold-start mechanism — anyone deposits any amount of svZCHF/sUSDS one-sided into der Bodensee Pool, and the target pool receives a 1-epoch (14-day) supplementary AuMM stream starting next epoch; once per epoch per pool. After Incendiary's 14-day window, emissions depend purely on real TVL via the CCB. The sequence: conviction (Incendiary) → long-term reality (EMA).

### 3. Discipline (Keeping the System Clean)

Aureum continuously filters unproductive pools. Volume percentile floor: must stay above minimum activity threshold. Efficiency tournament: revenue-per-emission ranking; bottom 15% capped, excess redistributed to productive pools. Graduated enforcement: warning zone before disqualification, gauge revocation after 4 consecutive epochs. Dead or extractive pools lose emissions or are removed entirely.

### 4. Constellation Routing — a small-world network

The 28 Miliarium pools are not a flat hub-and-spoke and not a random graph. Topologically they form a **small-world network** in the sense of Watts and Strogatz (1998): a graph with **high local clustering** *and* **short global path lengths**, produced when a few **shortcut connections** are introduced into an otherwise locally clustered lattice. Real-world systems with this topology — power grids, neural networks, social graphs — combine specialised local processing with rapid global communication. The Miliarium Aureum is engineered for the same property.

**The local-cluster layer.** Each pool is a tightly-coupled local market: five tokens trading against each other through ten internal pairs at Balancer V3 weighted-pool prices. A trade that lives inside one pool never leaves its cluster — pure local processing, deep relative to its size.

**The shortcut layer (dual universal connectors).** Two tokens are wired into **26 of the 28** Miliarium pools as the **shortcut connections** that collapse global path length. **svZCHF** (Frankencoin savings, ERC-4626, deterministic Rate-Provider pricing, yield-bearing) is the **deeper, primary** routing rail — typically **26%** as yield core in standard pools (**80%** in ixHelvetia), oracle-free, with the lowest slippage variance and yield that retains LPs. **ixEDEL** (Reserve Protocol DTF, NAV-priced basket) is the **secondary** rail — typically **16%** as routing anchor (**46%** in ixEdelweiss, the price-discovery hub), with NAV mint/redeem cycles whose drift against pool prices opens a continuous arbitrage surface aggregators exploit around the clock. Because both anchors live in nearly every pool, **any asset is one or two routed hops from any other**: a swap from ixAurebit (wrapped BTC) to ixEquitix (equities) is pool A → svZCHF (or ixEDEL) → pool B, with fees on **both** legs of **both** anchors. Most cross-pool trades touch both rails simultaneously.

**The hub-and-spoke overlay.** Inside the small-world graph, **ixEdelweiss (slot 05)** is the dedicated price-discovery hub for ixEDEL — 46% ixEDEL, the deepest ixEDEL venue, and the Roman monument the constellation is named after. The other 25 ixEDEL-holding pools are spokes around it. Hub-and-spoke describes the **price-discovery** topology for ixEDEL specifically; the small-world graph describes the **full routed liquidity surface** across both universal connectors.

**On top of its routing role, svZCHF is also the autonomous-reserve anchor.** **der Bodensee Pool** (AuMM/sUSDS/svZCHF), protocol fee inflows, governance deposits, Incendiary Boost intake, and composition-challenge deposits all land as one-sided svZCHF (or sUSDS) into der Bodensee — the same CHF-anchored stable that routes inside every pool also stacks captured revenue and conviction capital into the autonomous reserve. ixEDEL has no equivalent reserve role. Balancer V3 Rate Providers on svZCHF and sUSDS make the reserve-side ERC-4626 weight yield-accruing in-place; see [Tokenomics §x-a](04_tokenomics.md) for the full mechanism.

**Slot exceptions (deliberate departures from the universal-connector pattern).** **ixHelvetia (01)** is the Frankencoin MMA — pure svZCHF/sUSDS, no ixEDEL bridge. **ixAetheron (02)** is the ETH-staking pool with an ETH-native yield core (sfrxETH / wOETH) — keeps the ixEDEL anchor but skips svZCHF. **ixLibertas (06)** is the seven-token USD stable hub — holds **neither** anchor, giving traders a pure stablecoin venue with no CHF or basket exposure. These three slots serve flows that should not pay the cross-anchor cost; they are exceptions inside the small-world graph, not failures of it.

This small-world / dual-anchor design is Aureum's inheritance of the original Sagix construction — see [Sagix — Miliarium Aureum](https://www.sagix.io/sagix-miliarium-aureum/), which uses the same Watts–Strogatz framing for the Balancer V3 pool graph, and the [Sagix four-layer framework](https://www.sagix.io/our-layer-framework/) for the venue / routing / anchor / reserve liquidity-risk decomposition the two rails operationalise.

In Roman terms: **svZCHF and ixEDEL are the two viae** (the roads connecting every province), **ixEdelweiss is the Miliarium Aureum** (the golden milestone from which every road is measured), and **each pool is a province** — locally self-sufficient, globally one or two roads away from any other.

## iv. Emission Regimes

- **Through end of Month 10:** each block, **der Bodensee bootstrap** AuMM (piecewise linear: 80% at genesis → 50% at end of Month 6 → 0% at end of Month 10) is deposited one-sided into der Bodensee Pool. The **LP tranche** goes **100%** to the 28 Miliarium pools, split **purely equal** (**1/28 of the LP tranche** each). No treasury share. Other pools may exist but do not receive this equal tranche.
- **Months 11–12 (two-month transition):** blend linearly from equal to CCB over the window. At the midpoint, the mix is half equal and half CCB. See [Protocol formulas](11_formulas.md) for the blend formula.
- **After Year 1:** emissions follow only the CCB — each pool scored by smoothed TVL and CCB multiplier, normalized across eligible pools. No vote. See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).

**Why equal first.** The EMA needs ~60 days of on-chain data before it produces a meaningful signal. Allocating by TVL from block 0 would reward whichever pool attracted the earliest whale, not sustained capital. So all 28 Miliarium pools get identical treatment regardless of TVL until the EMA has real data.

**Why a two-month transition.** An abrupt switch from equal to CCB at a single block would cause overnight emission shocks — pools receiving 1/28 could suddenly get much more or much less. The two-month linear blend gives LPs and operators time to watch the CCB’s scoring in real time and adjust positions. Pools that attracted deep, sticky capital see their share rise; pools coasting on equal allocation see it fall. The transition rewards sustained capital commitment, not historical incumbency.

## v. The Flywheel

> The CCB directs emissions, **der Bodensee** captures revenue, the **Miliarium** generates it. Sections **i–iv** above look like three components. They are one closed circuit.

### v-a. The Circuit

Follow one dollar around the loop. It returns larger.

1. **Emissions recruit capital.** A fixed AuMM stream per block — **1.00 AuMM/block in Era 0** ([Tokenomics](04_tokenomics.md)) — pays LPs who deposit productive capital. The stream is fixed in *tokens*; its dollar value is `AuMM_per_block × AuMM_price`.
2. **Capital generates revenue.** Every dollar of TVL in an ERC-4626 pool yields from block 0; every trade pays a swap fee — the **Day-One Revenue Guarantee**, no volume required.
3. **Revenue deepens the reserve.** Protocol swap fees (**~50%** of charged fee) and the **10%** ERC-4626 yield skim route one-sided into der Bodensee as sUSDS/svZCHF; der Bodensee's **60%** stablecoin side compounds in-place via Rate Providers. Three inflows, one direction ([Tokenomics §x-a](04_tokenomics.md)).
4. **A deeper reserve reprices AuMM.** Fixed **40%** AuMM side; bootstrap one-sided inflow decays to **zero at Month 10** ([F-0](11_formulas.md)), after which AuMM enters only via swap. Weighted-pool math — fixed numerator, growing denominator — lifts price mechanically. No buyback, no burn, no discretion. **The pool is the value-capture mechanism.**
5. **Higher AuMM price raises every pool's APR.** Token-denominated emissions mean repricing lifts the dollar value of the same per-block stream — headline APR rises with **no new fee revenue**.
6. **Higher APR recruits more capital.** Step 1 again, one turn richer.

```
emissions → TVL → fees + 4626 yield → der Bodensee deepens
    → AuMM reprices up → AuMM-denominated APR rises → more TVL → …
```

Reflexive by construction: each turn's output is the next turn's input. The only external fuel is the first few turns of capital.

### v-b. Why the Loop Cannot Leak

Most token economies bleed at the seams — treasury sales, insider unlocks, buybacks that can reverse. Aureum closed every seam at block 0.

- **No treasury wallet** for discretionary AuMM sale. Bootstrap goes one-sided into the reserve; that channel zeroes at Month 10.
- **No insider allocation, cliff, or vesting.** What emits is what exists. Nothing sells into LPs from above.
- **No buyback to mis-route.** Value accrues through pool math, not a wallet that could dump.
- **No emission vote.** CCB allocation is mechanical ([Constitution §xxix](10_constitution.md)); governance cannot redirect the loop.

The loop has nowhere to lose value. *Der Bodensee: a lake that only gets deeper.*

### v-c. Where You Stand in the Loop

Same circuit from the protocol's view; three participant positions, three leverage profiles.

**The holder.** Buy and hold. You capture step 4 — repricing — at spot when you transact. No IL, no liquidity provided. Long a fixed numerator against a deepening reserve: the cleanest patience bet.

**The buyer-as-participant.** Buying AuMM from der Bodensee turns the wheel: your purchase deepens the reserve, thins the AuMM side, lifts price (step 4) and AuMM-denominated APR across eligible pools (step 5). Leverage is inverse to reserve depth — a shallow early reserve moves hard on the same buy that barely registers once mature. The early believer has the most wheel leverage for the same reason the wheel needs them most.

**The der Bodensee LP.** Provide AuMM into der Bodensee — the apex seat, where every revenue stream terminates and you own a pro-rata slice. Three returns stack:

- full **0.75%** in-pool swap fee on every trade, including every recruitment buy;
- in-place ERC-4626 yield on the **60%** stablecoin side via Rate Providers;
- repricing on your **40%** AuMM leg as the reserve deepens.

Cost: impermanent loss on the AuMM leg — sharp appreciation means net-selling AuMM vs. simply holding. Deep-conviction only: long AuMM, wear the rebalancing cost, collect the toll on everyone else's recruitment.

### v-d. The One Input the Loop Cannot Engineer

Every step above is unconditional — the mechanism runs whether or not anyone acts. But the magnitude of every step scales with one input the protocol can incentivize and cannot command: **TVL**. A flywheel is real once it turns; the open question is only whether the first turns happen — the cold-start.

Era 0 front-loads ~50% of supply, Incendiary Boost lets anyone fund a pool's ignition, and equal allocation through the first ten months keeps the field level until the EMA has data. These improve the odds of the first turn; they do not guarantee it. Aureum engineered away every endogenous risk — insider supply, discretionary dispositions, unlock overhang, redirectable emissions — and kept only the honest one: whether adoption arrives.