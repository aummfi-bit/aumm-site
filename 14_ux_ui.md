# UX / UI — Frontend Requirements

*Dashboard and interface elements for aumm.fi. This is a planning document — no code yet.*

---

## 1. Protocol Overview Dashboard

- [ ] **Emission schedule status** — current era, block emission rate, next halving countdown (blocks + estimated time), cumulative emitted vs 21M cap (progress bar); **der Bodensee bootstrap** — current bootstrap share % of block emission, blocks remaining until Month 10 end (when bootstrap reaches 0%)
- [ ] **TVL** — protocol-wide and per-pool, with EMA(60) overlay
- [ ] **FDV / FDV-to-TVL ratio** — chart with historical
- [ ] **TradingView-style charts** — TVL, FDV, FDV/TVL, AuMM price, all with the 60-day EMA plotted alongside spot
- [ ] **Trading volume** — 24h, 7d, 30d, all-time; protocol-wide and per-pool breakdown
- [ ] **Protocol fees** — 24h and all-time; split by swap fees vs yield fees; **protocol-captured** svZCHF inflow to der Bodensee (swap fees on other pools + yield skim) **vs** **in-pool** fees on der Bodensee trades (0.75% tier, LPs only)

---

## 2. der Bodensee Pool

- [ ] **Bootstrap emission decay** — current Bodensee share of block emission vs time (80% → 0% linear by end of Month 10), small chart or progress ring; cumulative one-sided AuMM from bootstrap vs from fees
- [ ] **Weight decay visualisation** — current AuMM/svZCHF weights vs target (90/10 → 48/52), time remaining to stabilisation, progress bar or animated gauge
- [ ] **Reserve depth** — total svZCHF accumulated (from fee revenue + governance deposits + Incendiary escrow)
- [ ] **AuMM price** — derived from pool weights and reserves (no oracle)
- [ ] **Inflow tracker** — cumulative and trailing 30d **one-sided svZCHF** inflows to der Bodensee, broken down by source (protocol-captured swap share from **other** pools, yield skim after **svZCHF routing**, governance deposits, Incendiary escrow); separately show **in-pool** swap-fee accrual for der Bodensee LPs (0.75% tier) if distinct in subgraph
- [ ] **Pool composition** — live AuMM and svZCHF balances

---

## 3. Miliarium Aureum Pools

- [ ] **28-pool registry table** — slot, name, sector, template, composition, TVL, 24h volume, 24h fees, CCB multiplier, emission share %, status (Active / Warning / Disqualified)
- [ ] **Atomic liquidity supply** — per-pool LP depth, available liquidity at price levels
- [ ] **Sector grouping view** — Yield (01-07), Bonds (08-11), Crypto (12-16), Stocks (17-26), Metals (27-28) with sector-level aggregates
- [ ] **Individual pool pages** — composition table, TradingView chart (TVL, volume, fees), EMA(60) vs spot TVL, CCB multiplier history, emission share history, Incendiary Boost status, 4626 Quality Gate status

---

## 4. Efficiency Tournament & Rankings

- [ ] **Efficiency ranking table** — all gauged pools ranked by efficiency ratio (fees + yield revenue / emissions received), 3-epoch moving average
- [ ] **Tier indicators** — colour-coded: Safe (above 15th percentile), Warning (10th-15th), Cut (below 10th), with emission cap applied
- [ ] **CCB multipliers** — current value for each of the 28 Miliarium pools, bi-weekly update history, direction arrows (up/down/neutral)
- [ ] **Volume percentile floor** — per-pool status vs current threshold (5th → 10th → 15th graduated schedule)
- [ ] **Redistribution tracker** — how much excess emission from capped pools was redistributed and to whom

---

## 5. AuMM Token

- [ ] **Supply dashboard** — total emitted, circulating supply, era progress bar
- [ ] **Halving schedule** — visual timeline across eras 0-6+, current position highlighted
- [ ] **Emission rate** — current per-block rate, annual rate, daily rate
- [ ] **Emission regime indicator** — Equal (months 1-10) / Transition (months 11-12) / Pure CCB (post year 1), with current alpha value during transition

---

## 6. Governance

- [ ] **Active proposals** — gauge approvals, gauge challenges, fee changes, composition challenges; status, quorum progress, time remaining, vote tally
- [ ] **Proposal history** — past votes with outcomes, turnout, deposit amounts
- [ ] **Quorum tracker** — current total qualified voting power, 20% threshold line
- [ ] **Deposit log** — all governance svZCHF/sUSDS deposits into der Bodensee Pool (linked to proposal)

---

## 7. LP Position Manager

- [ ] **My positions** — per-pool AuMT holdings, USD value, emission earnings (accrued, claimed), governance power
- [ ] **Governance power calculator** — show current power based on (USD value x time held)^(1/4 or 1/3), qualification status (14-day minimum, 6-month ramp)
- [ ] **Emission estimator** — projected AuMM earnings per block/day/month based on current pool weights and LP share
- [ ] **Deposit / Withdraw** — pool entry and exit interface with IL estimate

---

## 8. Incendiary Boost

- [ ] **Active boosts** — which pools have active Incendiary, time remaining, emission rate (pegged to 85th percentile), efficiency scalar
- [ ] **Boost history** — past Incendiary activations, svZCHF/sUSDS escrowed, emission delivered, pool performance during boost
- [ ] **Priority skim impact** — how much of the current block emission is allocated to Incendiary claims vs CCB remainder

---

## 9. Constellation Routing

- [ ] **ixEDEL routing visualisation** — network graph showing the 26 ixEDEL-connected pools, ixEdelweiss as hub, trade paths lighting up on activity
- [ ] **Cross-pool arbitrage volume** — how much volume is routed through ixEDEL legs
- [ ] **Connector pools** — ixEdelweiss (hub), ixLibertas (USD), ixCambio (FX) highlighted with routing stats

---

## 10. Sector Rotation View

- [ ] **Sector heatmap** — Yield / Bonds / Crypto / Stocks / Metals; colour by 24h fee generation or TVL change
- [ ] **Macro regime indicator** — qualitative view of which sectors are leading/lagging (maps to the correlation matrix in [Miliarium sectors](07_miliarium_sectors.md))
- [ ] **Sector-level TVL and volume aggregates** — time series per sector

---

## 11. Gauged Pools (Non-Miliarium)

- [ ] **Gauge registry** — all non-Miliarium gauged pools with status, TVL, efficiency rank, emission share
- [ ] **Sandbox pools** — non-gauged pools ranked by efficiency, Fast-Track progress (top 10% for 3 epochs = auto-gauge)
- [ ] **Gauge boost countdown** — 90-day boost timer for newly gauged pools (1.2x multiplier)

---

## 12. Proof of Real Yield Dashboard

Per-pool yield transparency that reframes how LPs evaluate returns.

**Per pool:**

| Metric | Definition |
|--------|-----------|
| Real yield % | Portion of returns from swap fees + ERC-4626 vault yield (non-inflationary sources) |
| Emission yield % | Portion from AuMM emissions (inflationary) |
| Efficiency score | Pool's efficiency ratio vs. protocol average |
| Revenue per $1 of emissions | How much protocol revenue each dollar of emission generates |

**The framing:** *"This pool earns 68% of returns from real yield, not inflation."*

Most AMMs report a single blended APR mixing real revenue with token emissions. LPs see "80% APR" without knowing 75% is inflation diluting the token they're earning. Aureum separates the two.

An Aerodrome LP comparing "80% APR" against Aureum's "12% real yield + 15% emission yield" shifts from "which number is bigger" to "which return is sustainable." Lower headline APR, higher quality return. The dashboard makes that argument visually.

**Token supply transparency.** The dashboard also publishes in real time:

- [ ] **Total AuMM emitted** — cumulative tokens distributed to LPs since block 0
- [ ] **Total svZCHF deposited into der Bodensee Pool** — cumulative inflows from protocol fee revenue, governance deposits, and Incendiary Boost escrow
- [ ] **der Bodensee Pool reserve depth** — current svZCHF reserves and AuMM/svZCHF ratio

See [Immutable Parameters (§xxix)](10_constitution.md).

---

## Notes

- All charts should support TradingView embed or similar interactive charting
- EMA(60) should be plottable alongside spot on every TVL chart
- Mobile-responsive; three themes already exist (Au / Day / Night)
- No oracle dependency — all data from on-chain contract reads
- Consider WebSocket or polling for live block-by-block emission updates
