<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 14_ux_ui.md — DO NOT EDIT -->
# UX / UI — Frontend Requirements

*Dashboard and interface elements for aumm.fi. This is a planning document — no code yet.*

---

## Scope split: MVP vs Post-MVP

This document lists the full UX/UI surface planned for aumm.fi. Per OQ-18, the frontend is developed as a separate repository (`aumm-app`) under its own plan, parallel to contract development in `aumm-deploy`.

**MVP — required for testnet (Holesky) and mainnet launch:**
- §xlvii Miliarium Aureum Pools — registry table with compositions, TVL, 24h volume, CCB multiplier, emission share
- §xlvi der Bodensee Pool — composition card, reserve depth, AuMM price, pool balances (from genesis)
- LP deposit/withdraw flows for every gauged pool + der Bodensee
- AuMT display — user's qualified AuMT per pool, pending AuMM emissions, time-in-pool status (14-day qualification, 6-month on-ramp)
- Governance interface — active proposals list, voting UI, proposal-submission UI (gauge proposals, gauge challenges, composition challenges, fee-change proposals)
- Swap interface — basic composite-swap via the constellation (can integrate with an aggregator initially rather than building routing from scratch)
- Block-based time displays — halving countdown, bootstrap milestones at `MONTH_6_END_BLOCK` / `MONTH_10_END_BLOCK`, Era transition countdowns (all expressed as blocks with calendar-time aliases per §xxix)

**Post-MVP — rolled out over subsequent protocol-months:**
- §xlv Protocol Overview Dashboard — TradingView-style charts, FDV/TVL ratios, historical data
- §xlvi advanced Bodensee views — inflow tracker breakdowns, bootstrap emission decay visualization
- Efficiency Tournament leaderboard with real-time rank updates
- Per-pool multiplier history visualization
- Incendiary Boost dashboard
- Constellation visualization — the 28+N gauged pools as an interactive graph
- Detailed governance analytics (voter participation, proposal history)
- Mobile app (native or PWA)

The MVP/post-MVP distinction is a planning tool — all of the sections below describe the eventual target state. Implementation priority follows the split above.

---

## xlv. Protocol Overview Dashboard

- [ ] **Emission schedule status** — current era, block emission rate, next halving countdown (blocks + estimated time), cumulative emitted vs 21M cap (progress bar); **der Bodensee bootstrap** — current bootstrap share % of block emission, blocks remaining until Month 10 end (when bootstrap reaches 0%)
- [ ] **TVL** — protocol-wide and per-pool, with EMA(60) overlay
- [ ] **FDV / FDV-to-TVL ratio** — chart with historical
- [ ] **TradingView-style charts** — TVL, FDV, FDV/TVL, AuMM price, all with the 60-day EMA plotted alongside spot
- [ ] **Trading volume** — 24h, 7d, 30d, all-time; protocol-wide and per-pool breakdown
- [ ] **Protocol fees** — 24h and all-time; split by swap-fee **protocol share** vs yield fees; **protocol-captured** stablecoin (sUSDS/svZCHF) inflow to der Bodensee (**protocol leg** of swap fees on other pools + yield skim) **vs** **in-pool** fees on der Bodensee trades (0.75% tier, LPs only) **vs** **LP residuals** on other pools (if subgraph exposes Vault LP fee leg)

---

## xlvi. der Bodensee Pool

- [ ] **Bootstrap emission decay** — current Bodensee share of block emission vs time (piecewise: 80% → 50% at `MONTH_6_END_BLOCK`, 50% → 0% at `MONTH_10_END_BLOCK`), small chart or progress ring; cumulative one-sided AuMM from bootstrap vs from fees
- [ ] **Pool composition card** — fixed weights **40% AuMM / 30% sUSDS / 30% svZCHF** (immutable, no decay); show 60% ERC-4626 yield-bearing share
- [ ] **Reserve depth** — total stablecoin (sUSDS + svZCHF) accumulated (from fee revenue + governance deposits + Incendiary Boost deposits)
- [ ] **AuMM price** — derived from pool reserves and fixed weights (no oracle)
- [ ] **Inflow tracker** — cumulative and trailing 30d **one-sided stablecoin** inflows to der Bodensee, broken down by source (**protocol share** of swap fees from **other** pools, yield skim, governance deposits, Incendiary Boost deposits); separately show **in-pool** swap-fee accrual for der Bodensee LPs (0.75% tier) if distinct in subgraph
- [ ] **Pool balances** — live AuMM, sUSDS, and svZCHF balances

---

## xlvii. Miliarium Aureum Pools

- [ ] **28-pool registry table** — slot, name, sector, template, composition, TVL, 24h volume, 24h fees, CCB multiplier, emission share %, status (Active / Warning / Disqualified)
- [ ] **Atomic liquidity supply** — per-pool LP depth, available liquidity at price levels
- [ ] **Sector grouping view** — Yield (01-07), Bonds (08-11), Crypto (12-16), Stocks (17-26), Metals (27-28) with sector-level aggregates
- [ ] **Individual pool pages** — composition table, TradingView chart (TVL, volume, fees), EMA(60) vs spot TVL, CCB multiplier history, emission share history, Incendiary Boost status, 4626 Quality Gate status

---

## xlviii. Efficiency Tournament & Rankings

- [ ] **Efficiency ranking table** — all gauged pools ranked by efficiency ratio (fees + yield revenue / emissions received), 3-epoch moving average
- [ ] **Tier indicators** — colour-coded: Safe (above 15th percentile), Warning (10th-15th), Cut (below 10th), with emission cap applied
- [ ] **CCB multipliers** — current value for each of the 28 Miliarium pools, bi-weekly update history, direction arrows (up/down/neutral)
- [ ] **Volume percentile floor** — per-pool status vs current threshold (5th → 10th → 15th graduated schedule)
- [ ] **Redistribution tracker** — how much excess emission from capped pools was redistributed and to whom

---

## xlix. AuMM Token

- [ ] **Supply dashboard** — total emitted, circulating supply, era progress bar
- [ ] **Halving schedule** — visual timeline across eras 0-6+, current position highlighted
- [ ] **Emission rate** — current per-block rate, annual rate, daily rate
- [ ] **Emission regime indicator** — Equal (months 1-10) / Transition (months 11-12) / Pure CCB (post year 1), with current alpha value during transition

---

## l. Governance

- [ ] **Active proposals** — gauge approvals, gauge challenges, fee changes, composition challenges; status, quorum progress, time remaining, vote tally
- [ ] **Proposal history** — past votes with outcomes, turnout, deposit amounts
- [ ] **Quorum tracker** — current total qualified voting power, 20% threshold line
- [ ] **Deposit log** — all governance svZCHF/sUSDS deposits into der Bodensee Pool (linked to proposal)

---

## li. LP Position Manager

- [ ] **My positions** — per-pool AuMT holdings, USD value, emission earnings (accrued, claimed), governance power
- [ ] **Governance power calculator** — show current power based on (USD value x time held)^(1/4 or 1/3), qualification status (14-day minimum, 6-month ramp)
- [ ] **Emission estimator** — projected AuMM earnings per block/day/month based on current pool weights and LP share
- [ ] **Deposit / Withdraw** — pool entry and exit interface with IL estimate

---

## lii. Incendiary Boost

- [ ] **Active boosts** — which pools have active Incendiary Boost, epoch remaining, emission rate, deposit amount
- [ ] **Boost history** — past Incendiary Boost activations, svZCHF/sUSDS deposited, emission delivered, pool performance during boost
- [ ] **Priority skim impact** — how much of the current block emission is allocated to Incendiary claims vs CCB remainder

---

## liii. Constellation Routing — small-world network

- [ ] **Small-world graph visualisation** — network view of the 28 pools as a Watts–Strogatz graph: tight local clusters (each pool's 5 tokens × 10 internal pairs) connected by **two** shortcut layers (svZCHF in 26 pools, ixEDEL in 26 pools), with trade paths lighting up on activity. See [Mental model (§iii — Constellation Routing)](02_mental_model.md).
- [ ] **Dual-anchor routing volume** — how much volume is routed through the **svZCHF leg** vs the **ixEDEL leg** vs **both** simultaneously; per-anchor fee accrual.
- [ ] **Hub-and-spoke overlay** — ixEdelweiss as the ixEDEL price-discovery hub (46% ixEDEL); ixLibertas (USD-only, no anchors) and ixCambio (multi-currency FX) highlighted with routing stats.
- [ ] **Slot-exception markers** — ixHelvetia (svZCHF only), ixAetheron (ixEDEL only), ixLibertas (neither) called out so the graph correctly shows the three deliberate departures from the universal-connector pattern.

---

## liv. Sector Rotation View

- [ ] **Sector heatmap** — Yield / Bonds / Crypto / Stocks / Metals; colour by 24h fee generation or TVL change
- [ ] **Macro regime indicator** — qualitative view of which sectors are leading/lagging (maps to the correlation matrix in [Miliarium sectors](07_miliarium_sectors.md))
- [ ] **Sector-level TVL and volume aggregates** — time series per sector

---

## lv. Gauged Pools (Non-Miliarium)

- [ ] **Gauge registry** — all non-Miliarium gauged pools with status, TVL, efficiency rank, emission share
- [ ] **Sandbox pools** — non-gauged pools ranked by efficiency, Fast-Track progress (top 10% for 3 epochs = auto-gauge)
- [ ] **Gauge boost countdown** — 90-day boost timer for newly gauged pools (1.2x multiplier)

---

## lvi. Proof of Real Yield Dashboard

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
- [ ] **Total stablecoin (sUSDS + svZCHF) deposited into der Bodensee Pool** — cumulative inflows from protocol fee revenue, governance deposits, and Incendiary Boost deposits
- [ ] **der Bodensee Pool reserve depth** — current sUSDS + svZCHF reserves and AuMM-to-stablecoin ratio (visible from Month 6 onward)

See [Immutable Parameters (§xxix)](10_constitution.md).

---

## lvii. Notes

- All charts should support TradingView embed or similar interactive charting
- EMA(60) should be plottable alongside spot on every TVL chart
- Mobile-responsive; three themes already exist (Au / Day / Night)
- No oracle dependency — all data from on-chain contract reads
- Consider WebSocket or polling for live block-by-block emission updates
