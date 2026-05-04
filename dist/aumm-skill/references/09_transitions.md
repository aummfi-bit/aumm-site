<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 09_transitions.md — DO NOT EDIT -->
# Transition Rules

*Timeline from equal emissions through a linear blend to fully automatic CCB.*

---

## xxvi. Launch Procedures

- Pool creation is permissionless from block 0.
- All launch mechanics described below are **immutable from block 0**. They execute on schedule and self-terminate.

Protocol **months** (Month 1 … Month 12) are fixed on-chain block ranges of `BLOCKS_PER_MONTH = 219,000` each, starting from the genesis block; **Year 1** = Months 1–12 = `BLOCKS_PER_YEAR = 2,628,000` blocks (exactly 365 calendar days at 12-second blocks). All month/year boundaries are deterministic from genesis. See [Constitution §xxix](10_constitution.md) for the full canonical time-constant table.

### Month-by-Month Timeline

**Month 1 — Genesis.**
- Aequilibrium factory opens. Pool creation is permissionless.
- **der Bodensee bootstrap emissions** begin: **80%** of each block’s emission minted as **one-sided AuMM** into der Bodensee Pool (no LP tokens). The **remaining ~20%** is the **LP tranche**, split **1/28** across the 28 Miliarium pools. **100%** to LPs from block 0 — no treasury wallet.
- Non-Miliarium pools can exist and build liquidity but receive no emissions.
- der Bodensee Pool launches as a **three-token weighted pool** with **fixed weights 40% AuMM / 30% sUSDS / 30% svZCHF** (immutable from block 0, no time-decay). **Swap fee inside der Bodensee:** **0.75%** at genesis (governance-adjustable within 0.10–1.00% band per [Constitution §xxix](10_constitution.md)), fully retained **in pool** for der Bodensee LPs.
- **Protocol-captured** fee revenue (**protocol share** of swap fees on **other** gauged pools + ERC-4626 yield fees) starts flowing into der Bodensee as one-sided stablecoin (sUSDS/svZCHF) inflows.

**Month 2 — TVL measurement window opens.**
- On-chain TVL data begins accumulating for EMA(60) signal.

**Months 1–10 — der Bodensee emission bootstrap (piecewise-linear decay).**
- Bodensee share decays **linearly from 80% to 50%** between genesis and the **final block of Month 6**, then **linearly from 50% to 0%** between Month 6 and the **final block of Month 10**. LP tranche grows correspondingly (20% → 50% → 100%). Weighted-pool math reprices AuMM as one-sided stablecoin fee inflows deepen the reserve side. No founder-set price, no governance-voted multiple — the reserve ratio **is** the market price from genesis.

**End of Month 10 — Bootstrap emissions complete.**
- Bootstrap share reaches **zero**. **100%** of each block’s emission is the LP tranche, still **1/28** across the 28 Miliarium pools until Month 11.

**Month 11 — Gauge proposals open, CCB transition begins.**
- Non-Miliarium pools can submit gauge proposals (100 svZCHF/sUSDS into der Bodensee).
- All pools begin ranking in the Efficiency Tournament.
- Sandbox fast-track active: non-gauged pools sustaining top 10% efficiency for 3 epochs (6 weeks) earn automatic gauge approval.
- CCB transition begins: **α** runs from **0** (first block of Month 11) to **1** (last block of Year 1).
- Each pool's share blends its equal one-twenty-eighth with its CCB-derived share. At midpoint, **α = 0.5** — half equal, half CCB.
- Pools coasting on equal allocation may see their share decline if TVL lags the protocol average. The transition rewards sustained capital, not incumbency.

**End of Year 1 — CCB transition complete.**
- α = 1. Allocation is pure CCB.

**End of Month 10 — der Bodensee bootstrap channel closes permanently.**
- Bootstrap share reaches **zero**. The treasury/bootstrap channel is **immutable at zero from this block forward** — der Bodensee never receives AuMM via emission again. The AuMM side of the pool is fixed; only swap-ins by traders can add AuMM after this point.

**After Month 10 — Reserve grows from fees alone.**
- Stablecoin fee inflows continue indefinitely. Weighted-pool math reprices AuMM mechanically as the stablecoin side deepens against a capped AuMM side. No buyback, no burn, no market purchases.

### After Year 1 (full CCB)

- **Pure** CCB: each pool scored by smoothed TVL and CCB multiplier, normalized across eligible pools. See [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).
- Automatic: no voting, no discretionary multipliers, no transition council.
- Efficiency tournament fully active — bottom 15% capped, excess redistributed.
- Volume percentile floor at full discipline (15th percentile).
- New gauged pools receive emissions alongside the 28 Miliarium pools.
- Incendiary Boost available for all gauged pools.
- Governance continues for non-emission proposals (gauges, fees) under immutable constraints.
- **Protocol-captured** fees (**protocol share** of swap fees on other pools + ERC-4626 yield skim) continue to der Bodensee as one-sided stablecoin (sUSDS/svZCHF); **swap fees inside der Bodensee** (0.75%) stay **in pool** in full for der Bodensee LPs.

### Post-activation

- Efficiency tournament and eligibility criteria apply automatically.
- Protocol continues under immutable, on-chain rules only.
- Proposal and voting workflows remain active for non-emission actions, with on-chain-data-only proposal validation.

See [Immutable Parameters (§xxix)](10_constitution.md).
