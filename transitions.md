# Transition Rules

*Timeline from equal emissions through a linear blend to fully automatic CCB.*

---

## xxvi. Launch Procedures

- Pool creation is permissionless from block 0.
- All launch mechanics are immutable from block 0.

Protocol **months** (Month 1 … Month 12) are fixed on-chain block ranges; **Year 1** is Months 1–12.

### Through end of Month 10 (equal regime)

- Emissions to the Miliarium Aureum tranche are split equally (**1/28**) across the 28 immutable pools.
- Non-Miliarium pools can exist and build liquidity but do not receive this equal tranche.

### Months 11–12 (two-month linear transition)

- **α** runs **linearly** from **0** at the **first block of Month 11** to **1** at the **last block of Year 1**.
- Each pool’s emission share is a blend of its equal one-twenty-eighth and its CCB-derived share for that block (see `constitution.md` and `formulas.md`).
- **Halfway** through this window, **α = 0.5** — the mix is **half** equal and **half** CCB.

### First block after Year 1 (full CCB)

- Allocation is **pure** CCB: each pool scored by smoothed TVL, PMAR multiplier, and Incendiary multiplier, normalized across eligible pools. See `constitution.md` and `formulas.md`.
- Allocation remains automatic: no voting, no Bubble multipliers, no discretionary transition council.
- Governance continues for non-emission proposals (gauges, treasury, fees) under immutable constraints.

### Post-activation

- Efficiency tournament and eligibility criteria apply automatically.
- Protocol continues under immutable, on-chain rules only.
- Proposal and voting workflows remain active for non-emission actions, with on-chain-data-only proposal validation.

See Immutable Parameters in `constitution.md`.
