# Aureum Protocol — Mental Model

*How Aureum works for intelligent readers.*

---

## I — One-Liner

A fair-launch AMM where the only way to mine the token is to provide liquidity to productive pools. BTC tokenomics. Aequilibrium engine. No pre-mine. No VC. No team allocation.

---

## II — The Thesis in One Paragraph

The best AMM architecture in DeFi is about to lose its growth mechanism. The token is priced for terminal decline. But the code is open source, formally verified, and architecturally superior to every competitor. Project Aureum takes that code, replaces the broken tokenomics with a fair launch where the only way to earn tokens is to provide liquidity to productive pools, and lets the market discover what formally verified multi-asset pools can do when the economic layer is designed correctly. The experiment hasn't failed. It hasn't happened.

---

## III — Why This Exists

Balancer V3 is the most advanced AMM architecture in DeFi — multi-asset weighted pools, ERC-4626 native yield, hooks, formal verification by Certora. But the protocol's tokenomics failed. Emissions directed to legacy pools and governance staking created circular economics. Meta-governance capture concentrated power. The founding entity shut down. The team proposed eliminating emissions entirely — removing the only mechanism through which external builders could bootstrap new infrastructure.

The architecture deserves a second chance under a clean economic model. Project Aureum forks the V3 smart contracts and replaces the tokenomics with a fair launch. Same verified core. Fundamentally different economics. (See **Appendix** for a detailed comparison to every historical fair-launch failure mode.) Aureum's anticyclical, productive-capital-first thesis is independently validated by Curve's Yield Basis Hybrid Vaults (March 2026), which solve the same problem — scaling AMM liquidity without reflexive fragility — through a complementary but architecturally orthogonal approach tied to crvUSD peg stability. (See **Appendix: Yield Basis Hybrid Vaults**.)

---

## IV — Core Principles

1. **Fair launch.** No pre-mine, no team allocation, no VC. Treasury emission phase (months 0–10) seeds protocol-owned liquidity only — see Launch Procedures for details.
2. **Fixed supply.** 21 million maximum. Halving schedule. Declining emission rate.
3. **Mining is LP.** Productive capital in, tokens out. No staking rewards or bribe markets.
4. **Anti-capture by design.** Governance power derives exclusively from active LP positions with a 6-month on-ramp.
5. **Ethereum only.** Single chain for maximum composability and aggregator coverage.

---

## V — The Roman Infrastructure

The protocol's naming follows the architecture of Roman infrastructure — because the design follows it too.

The **Miliarium Aureum** (Golden Milestone) was the monument in the Roman Forum from which all distances in the Empire were measured. Every road radiated from it. In this protocol, the Miliarium Aureum is the founding constellation of pools — the routing hub that connects every pool through cross-pool arbitrage, shared aggregator paths, and deeper effective liquidity.

**AuMM** (Aureum Market Maker) is the reward token — mined by providing liquidity, burned by the protocol. BTC-style scarcity.

**AuMT** (Aureum Market Tessera) is the proof-of-participation token — your tessera. In Rome, a tessera was a small tablet that served as a ticket, a voucher, or a token of identity. It proved you belonged and carried rights: entry, grain distribution, voting in assemblies. Your AuMT proves your stake in the protocol's liquidity and carries the same rights — emissions, governance power, LP bonus eligibility.

**Aequilibrium** is the AMM engine — Latin for "equal balance." The pool layer that powers every trade, every arb, every routing path. Derived from Balancer V3's Certora-verified smart contracts, reborn under a new economic model.

*All roads lead to the Miliarium Aureum. Your tessera proves you helped build them.*

---

## VI — How Aureum Works — Three Layers

### I. Capital Allocation (The Continuous Central Bank)

Which pools should receive emissions right now? Base weight = 60-day EMA of on-chain TVL (institutional memory). Small governance nudges via Pioneer multipliers [0.90–1.10] and Bubble multipliers [0.90–2.00]. Strictly zero-sum: total emissions are fixed by the halving schedule. Sustained capital commitment is rewarded. Short-term hype is ignored. Market crashes trigger higher relative yield (anticyclical floor). Think of it as a central bank that automatically rewards persistent liquidity, not speculation.

### II. Bootstrapping (Starting New Pools)

New pools have no EMA history, so they need a structured path to earn emissions. Three stacked mechanisms: (a) **Incendiary Boost** — builder deposits AuMM, protocol emits it back over 30 days, the deposit is permanently burned, making AuMM scarcer for all holders; must remain efficient to renew. (b) **Bubble Multiplier** — qualified LPs vote to boost or suppress new pools (0.90×–2.00×) for the first 90 days. (c) **EMA Takeover** — after ~90 days, emissions depend purely on real TVL via the CCB. The flow: conviction (Incendiary) → market endorsement (Bubble) → long-term reality (EMA).

### III. Discipline (Keeping the System Clean)

Aureum continuously filters unproductive pools. Volume percentile floor: must stay above minimum activity threshold. Efficiency tournament: revenue-per-emission ranking; bottom 15% capped, excess redistributed to productive pools. Graduated enforcement: warning zone before disqualification, gauge revocation after 4 consecutive failed cycles. Dead or extractive pools lose emissions or are removed entirely.

---

## VII — The Feedback Loop

LPs provide liquidity → earn AuMM. Pools generate real fees + ERC-4626 yield → protocol earns revenue. Revenue → buyback & burn AuMM. Supply decreases → each AuMM backs more protocol revenue. Higher yield per token → attracts more productive capital. Good pools gain share. Bad pools lose share or get removed. The system self-corrects.

---

## VIII — Governance in One Sentence

**Power = productive liquidity held over time.** No tokens to buy. No locks to game. You must provide liquidity, stay committed, and perform.

---

*Most DeFi systems ask "Who should decide?" Aureum asks "What should the system do automatically?" — and encodes the answer into immutable rules.*
