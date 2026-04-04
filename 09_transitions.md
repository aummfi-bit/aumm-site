# Transition Rules

*Timeline from equal emissions through a linear blend to fully automatic CCB.*

---

## xxvi. Launch Procedures

- Pool creation is permissionless from block 0.
- All launch mechanics described below are **immutable from block 0**. They execute on schedule and self-terminate.

Protocol **months** (Month 1 … Month 12) are fixed on-chain block ranges; **Year 1** is Months 1–12.

### Month-by-Month Timeline

**Month 1 — Genesis.**
- Aequilibrium factory opens. Pool creation is permissionless.
- **der Bodensee bootstrap emissions** begin: **80%** of each block’s emission is minted as **one-sided AuMM** into der Bodensee Pool (no LP tokens). The **remaining ~20%** is the **LP tranche**, split **1/28** across the 28 Miliarium pools. **100% of the LP tranche** goes to LPs from block 0 — there is no treasury wallet.
- Non-Miliarium pools can exist and build liquidity but receive no emissions.
- der Bodensee Pool launches at genesis with **1 AuMM** and **1 svZCHF** seed liquidity and **90% AuMM / 10% svZCHF** weights. Linear time-decay begins. **Swap fee on trades inside der Bodensee:** **0.75%**, fully retained **in pool** for der Bodensee LPs.
- **Protocol-captured** fee revenue (swap fees on **other** pools + ERC-4626 yield fees) starts flowing into der Bodensee Pool as one-sided svZCHF inflows.

**Month 2 — TVL measurement window opens.**
- On-chain TVL data begins accumulating for EMA(60) signal.

**Months 1–10 — der Bodensee emission bootstrap (linear decay).**
- The Bodensee share of block emission decays **linearly** from **80% at genesis** to **0%** at the **final block of Month 10**. The LP tranche grows correspondingly (20% → 100% of block emission). Weighted-pool math prices AuMM alongside one-sided svZCHF fee inflows.

**Months 1–18 — der Bodensee Pool weight decay active.**
- AuMM weight declines linearly from 90% → 48%; svZCHF weight rises from 10% → 52%.
- **Protocol-captured** fee revenue from **other** pools enters der Bodensee Pool as one-sided svZCHF inflows from block 0; **swap fees on trades inside der Bodensee** (0.75%) accrue **in pool** to der Bodensee LPs.
- Price discovery is forced by time-decay + real revenue inflows — no oracle, no manual trigger.

**End of Month 10 — Bootstrap emissions complete.**
- Bodensee AuMM bootstrap share reaches **zero**. **100%** of each block’s emission is the LP tranche, still split **1/28** across the 28 Miliarium pools until Month 11.

**Month 11 — Gauge proposals open, CCB transition begins.**
- Non-Miliarium pools can submit gauge proposals (deposit 100 svZCHF/sUSDS into der Bodensee Pool).
- All pools begin ranking in the Efficiency Tournament.
- Sandbox fast-track active: non-gauged pools sustaining top 10% efficiency for 3 epochs (6 weeks) earn automatic gauge approval.
- CCB transition begins: **α** runs **linearly** from **0** at the first block of Month 11 to **1** at the last block of Year 1.
- Each pool's emission share is a blend of its equal one-twenty-eighth and its CCB-derived share. At the midpoint, **α = 0.5** — half equal, half CCB.
- Pools that performed well under equal allocation may see their share decline if their TVL lags the protocol average. This is by design — the transition rewards sustained capital, not historical incumbency.

**End of Year 1 — CCB transition complete.**
- α = 1. Allocation is pure CCB.

**Months 13–18 — CCB vs LBP weight decay (two clocks).**
- **Emissions:** The **α** blend finishes at the **last block of Year 1** (α = 1). From **Month 13** onward, allocation is **already** pure CCB — there is **no** second emission transition in Months 13–18. Those months are **not** a CCB ramp; they are just the first half of **Year 2** while the LBP story is still catching up.
- **der Bodensee Pool weights:** Linear weight decay runs **18 months** from genesis and **ends at Month 18** (90/10 → 48/52). Months 13–18 only finish that **weight** curve; they do **not** change CCB formulas.

**Month 18 — der Bodensee Pool weights stabilize.**
- Weights reach final state: 48% AuMM / 52% svZCHF. Fixed permanently from this point.
- Protocol fee revenue continues flowing into der Bodensee Pool indefinitely.

### After Year 1 (full CCB)

- Allocation is **pure** CCB: each pool scored by smoothed TVL and CCB multiplier, normalized across eligible pools. See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).
- Allocation remains automatic: no voting, no discretionary multipliers, no transition council.
- Efficiency tournament fully active — bottom 15% capped, excess redistributed.
- Volume percentile floor at full discipline (15th percentile).
- New gauged pools receive emissions alongside the 28 Miliarium pools.
- Incendiary Boost available for all gauged pools.
- Governance continues for non-emission proposals (gauges, fees) under immutable constraints.
- **Protocol-captured** fees (swap fees on other pools + ERC-4626 yield skim) continue to der Bodensee Pool as one-sided svZCHF inflows; **swap fees on trades inside der Bodensee** (0.75%) stay **in pool** for der Bodensee LPs.

### Post-activation

- Efficiency tournament and eligibility criteria apply automatically.
- Protocol continues under immutable, on-chain rules only.
- Proposal and voting workflows remain active for non-emission actions, with on-chain-data-only proposal validation.

See [Immutable Parameters (§xxix)](10_constitution.md).
