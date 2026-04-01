# Aureum Protocol — Glossary

---

## Core Tokens

**AuMM** (Aureum Market Maker) — reward token. 21M fixed supply, emitted to LPs, burned via protocol revenue. Zero governance power.

**AuMT** (Aureum Market Tessera) — proof-of-participation token. Represents an active LP position. Carries all governance power.

---

## Core Systems

**Aequilibrium** — the AMM engine (Balancer V3 fork, byte-identical pool layer, new tokenomics layer).

**Continuous Central Bank (CCB)** — emission allocation engine using 60-day EMA of TVL.

**EMA** (Exponential Moving Average) — 60-day time-weighted TVL measure with ~21-day half-life; the CCB's "institutional memory."

---

## Emission & Bootstrapping

**Pioneer Pools** — 25 pre-defined foundational pools receiving equal emissions during months 0–10.

**Pioneer Multiplier (PMAR)** — automatic, deterministic emission weight [0.75–1.25] for Pioneer pools, recalculated at each bi-weekly cycle boundary by the Pioneer Multiplier Adjustment Rule. Not governance-voted.

**Incendiary Boost** — builder-funded emission boost; deposit AuMM → emitted over 30 days (permanently burned); priority skim reduces all other pools' emissions.

**Bubble Multiplier** — temporary governance boost [0.90–2.00] for new pools during first 90 days post-gauge-approval.

**Sandbox** — non-gauged pools that exist and attract liquidity but receive zero emissions until they earn a gauge (or fast-track via top 10% efficiency).

---

## Governance

**Tessera-Weighted Voting** — governance power = `(USD value of qualified LP × time_in_pool)^(1/4)`.

**Qualification Period** — 14 days of continuous LP before voting power begins; full weight reached at ~6 months.

**Withdrawal Reset** — any withdrawal of any amount resets governance power to zero; 14-day qualification and 6-month on-ramp restart.

---

## Anti-Gaming & Discipline

**Volume Percentile Floor** — minimum activity threshold relative to all pools (graduated: 5th → 10th → 15th percentile over months 0–13).

**Efficiency Tournament** — pools ranked by `(fees + yield revenue) / emissions`; bottom 15% capped; excess redistributed.

**4626 Quality Gate** — ≥52% of pool composition must be ERC-4626 yield-bearing vault tokens, each with ≥$5M / 30 BTC / 4M svZCHF underlying vault TVL.

---

## Economic

**Buyback and Burn** — 25% of swap fees + 25% of yield fees used to purchase and permanently destroy AuMM.

**Deflationary Crossover** — point at which burn rate exceeds emission rate, causing net supply contraction.

**Priority Skim** — Incendiary Boost emissions are subtracted from the fixed block reward before CCB distribution, directly diluting all other pools.
