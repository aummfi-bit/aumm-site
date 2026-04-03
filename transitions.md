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
- Equal 1/28 emission begins across the 28 Miliarium pools.
- Non-Miliarium pools can exist and build liquidity but receive no emissions.
- Treasury emission phase starts: a declining share of per-block emissions flows to the protocol treasury (75% initially, declining to 50% by month 6, then to 0% by month 10).

**Month 2 — TVL measurement window opens.**
- On-chain TVL data begins accumulating for AuMM trading pool pricing.

**Month 6 — AuMM trading pool launch.**
- Treasury seeds the AuMM / svZCHF · sUSDS trading pool using accumulated protocol revenue at **FDV/TVL = 1**.
- Buyback-and-burn activates one week later.
- Price ceiling stabilization mechanism begins (see `tokenomics.md`).

**Months 6–12 — Price ceiling stabilization active.**
- Ceiling metric: EMA(21) of FDV/TVL = (21M × AuMM price) / total protocol TVL. Pool seeded at FDV/TVL = 1.
- When EMA(21) of FDV/TVL ≥ 2, treasury sells 0.75% of the AuMM pool's balance per day until EMA drops below 2.
- Sale proceeds deposited as permanent locked liquidity in the lowest-TVL Miliarium pools meeting the 4626 Quality Gate.
- Capped at 80% of treasury assets. If inventory runs out, the mechanism stops naturally.

**Month 10 — Treasury emission share drops to 0%.**
- Treasury receives no new AuMM after this point — permanent.
- Price ceiling continues using existing stabilization inventory through month 12.

**Month 11 — Gauge proposals open, CCB transition begins.**
- Non-Miliarium pools can submit gauge proposals (burn 100 svZCHF/sUSDS equivalent in AuMM).
- All pools begin ranking in the Efficiency Tournament.
- Sandbox fast-track active: non-gauged pools sustaining top 10% efficiency for 3 epochs (6 weeks) earn automatic gauge approval.
- CCB transition begins: **α** runs **linearly** from **0** at the first block of Month 11 to **1** at the last block of Year 1.
- Each pool's emission share is a blend of its equal one-twenty-eighth and its CCB-derived share. At the midpoint, **α = 0.5** — half equal, half CCB.
- Pools that performed well under equal allocation may see their share decline if their TVL lags the protocol average. This is by design — the transition rewards sustained capital, not historical incumbency.

**Month 12 — Hard stop.**
- Price ceiling stabilization shuts off permanently.
- Treasury deposits max 80% of remaining stablecoin balance plus corresponding AuMM at 30-day SMA price (price-neutral entry).
- All leftover AuMM burned.

**End of Year 1 — CCB transition complete.**
- α = 1. Allocation is pure CCB.

### After Year 1 (full CCB)

- Allocation is **pure** CCB: each pool scored by smoothed TVL and CCB multiplier, normalized across eligible pools. See `constitution.md` and `formulas.md`.
- Allocation remains automatic: no voting, no discretionary multipliers, no transition council.
- Efficiency tournament fully active — bottom 15% capped, excess redistributed.
- Volume percentile floor at full discipline (15th percentile).
- New gauged pools receive emissions alongside the 28 Miliarium pools.
- Incendiary Boost available for all gauged pools.
- Governance continues for non-emission proposals (gauges, treasury, fees) under immutable constraints.

### Post-activation

- Efficiency tournament and eligibility criteria apply automatically.
- Protocol continues under immutable, on-chain rules only.
- Proposal and voting workflows remain active for non-emission actions, with on-chain-data-only proposal validation.

See Immutable Parameters (`constitution.md` §xxix).
