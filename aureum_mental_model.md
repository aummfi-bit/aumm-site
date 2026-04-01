# Aureum Protocol — Mental Model

*How Aureum works for intelligent readers.*

---

## How Aureum Works — Three Layers

### 1. Capital Allocation (The Continuous Central Bank)

Which pools should receive emissions right now? Base weight = 60-day EMA of on-chain TVL (institutional memory). Small governance nudges via Pioneer multipliers [0.90–1.10] and Bubble multipliers [0.90–2.00]. Strictly zero-sum: total emissions are fixed by the halving schedule. Sustained capital commitment is rewarded. Short-term hype is ignored. Market crashes trigger higher relative yield (anticyclical floor). Think of it as a central bank that automatically rewards persistent liquidity, not speculation.

### 2. Bootstrapping (Starting New Pools)

New pools have no EMA history, so they need a structured path to earn emissions. Three stacked mechanisms: (a) **Incendiary Boost** — builder deposits AuMM, protocol emits it back over 30 days, the deposit is permanently burned, making AuMM scarcer for all holders; must remain efficient to renew. (b) **Bubble Multiplier** — qualified LPs vote to boost or suppress new pools (0.90×–2.00×) for the first 90 days. (c) **EMA Takeover** — after ~90 days, emissions depend purely on real TVL via the CCB. The flow: conviction (Incendiary) → market endorsement (Bubble) → long-term reality (EMA).

### 3. Discipline (Keeping the System Clean)

Aureum continuously filters unproductive pools. Volume percentile floor: must stay above minimum activity threshold. Efficiency tournament: revenue-per-emission ranking; bottom 15% capped, excess redistributed to productive pools. Graduated enforcement: warning zone before disqualification, gauge revocation after 4 consecutive failed cycles. Dead or extractive pools lose emissions or are removed entirely.

---

## The Feedback Loop

LPs provide liquidity → earn AuMM. Pools generate real fees + ERC-4626 yield → protocol earns revenue. Revenue → buyback & burn AuMM. Supply decreases → each AuMM backs more protocol revenue. Higher yield per token → attracts more productive capital. Good pools gain share. Bad pools lose share or get removed. The system self-corrects.

---

## Governance in One Sentence

**Power = productive liquidity held over time.** No tokens to buy. No locks to game. You must provide liquidity, stay committed, and perform.

---

*Most DeFi systems ask "Who should decide?" Aureum asks "What should the system do automatically?" — and encodes the answer into immutable rules.*
