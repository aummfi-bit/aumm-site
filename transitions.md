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
- Equal 1/28 emission begins across the 28 Miliarium pools. **100% of emissions go to LPs from block 0** — there is no treasury emission share.
- Non-Miliarium pools can exist and build liquidity but receive no emissions.
- der Bodensee Pool launches at genesis with **90% AuMM / 10% svZCHF** weights. Linear time-decay begins.
- Protocol fee revenue starts flowing into der Bodensee Pool as one-sided svZCHF inflows.

**Month 2 — TVL measurement window opens.**
- On-chain TVL data begins accumulating for EMA(60) signal.

**Months 1–18 — der Bodensee Pool weight decay active.**
- AuMM weight declines linearly from 90% → 48%; svZCHF weight rises from 10% → 52%.
- Buyback-and-burn activates as soon as der Bodensee Pool has sufficient AuMM liquidity for market purchases.
- Price discovery is forced by time-decay + real revenue inflows — no oracle, no manual trigger.

**Month 11 — Gauge proposals open, CCB transition begins.**
- Non-Miliarium pools can submit gauge proposals (burn 100 svZCHF/sUSDS equivalent in AuMM).
- All pools begin ranking in the Efficiency Tournament.
- Sandbox fast-track active: non-gauged pools sustaining top 10% efficiency for 3 epochs (6 weeks) earn automatic gauge approval.
- CCB transition begins: **α** runs **linearly** from **0** at the first block of Month 11 to **1** at the last block of Year 1.
- Each pool's emission share is a blend of its equal one-twenty-eighth and its CCB-derived share. At the midpoint, **α = 0.5** — half equal, half CCB.
- Pools that performed well under equal allocation may see their share decline if their TVL lags the protocol average. This is by design — the transition rewards sustained capital, not historical incumbency.

**End of Year 1 — CCB transition complete.**
- α = 1. Allocation is pure CCB.

**Month 18 — der Bodensee Pool weights stabilize.**
- Weights reach final state: 48% AuMM / 52% svZCHF. Fixed permanently from this point.
- Protocol fee revenue continues flowing into der Bodensee Pool indefinitely.

### After Year 1 (full CCB)

- Allocation is **pure** CCB: each pool scored by smoothed TVL and CCB multiplier, normalized across eligible pools. See `constitution.md` and `formulas.md`.
- Allocation remains automatic: no voting, no discretionary multipliers, no transition council.
- Efficiency tournament fully active — bottom 15% capped, excess redistributed.
- Volume percentile floor at full discipline (15th percentile).
- New gauged pools receive emissions alongside the 28 Miliarium pools.
- Incendiary Boost available for all gauged pools.
- Governance continues for non-emission proposals (gauges, fees) under immutable constraints.
- der Bodensee Pool continues receiving all protocol fee revenue as one-sided svZCHF inflows.

### Post-activation

- Efficiency tournament and eligibility criteria apply automatically.
- Protocol continues under immutable, on-chain rules only.
- Proposal and voting workflows remain active for non-emission actions, with on-chain-data-only proposal validation.

See Immutable Parameters (`constitution.md` §xxix).
