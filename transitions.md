# Transition Rules

*The launch timeline: from equal emissions to full protocol autonomy.*

---

## Launch Procedures: Months 0–13+

All launch mechanics described in this section are **immutable from block 0**. They execute on schedule and self-terminate.

### During the Pioneer Phase (months 0–10): Equal-Weight Pioneer Phase

**Pool creation is permissionless from block 0.** The Aequilibrium factory is open. Anyone can deploy any pool and provide liquidity, including to the 25 Pioneers.

**Emissions are split equally among the 25 Pioneer pools only.** No CCB/EMA weighting during this phase. Each Pioneer receives 1/25th of total LP emissions (after the treasury share). Non-Pioneer pools exist in the Sandbox — they can attract liquidity but receive zero emissions.

**Treasury emission phase:** A declining share of per-block emissions flows to the protocol treasury (75%→50% by month 6, 50%→0% by month 10). After month 10, the treasury never receives AuMM again.

**Month 2:** TVL measurement window opens for AuMM trading pool pricing.

**Month 6: AuMM Trading Pool Launch.**
- LPs vote (AuMT-weighted) on TVL-to-FDV multiple (5x–8x range)
- Treasury deploys AuMM / svZCHF / waEthUSDC / sUSDS (25% each), 0.75% swap fee
- 80% of treasury non-AuMM assets deposited; excess AuMM retained as stabilization inventory
- Buyback-and-burn begins one week later

**Months 6–10: Price Ceiling Stabilization.**
If 7-day SMA FDV > 200% of voted multiple, treasury sells AuMM at 0.75% of pool TVL per day. Proceeds deposited as permanent locked liquidity in qualifying Pioneer pools. Price reference is the internal AuMM/stablecoin pool price (oracle-free).

**Month 10: Hard Stop.**
- Stabilization shuts off permanently
- Treasury deposits max 80% of remaining stablecoin balance + corresponding AuMM at 30-day SMA (price-neutral)
- All leftover AuMM burned
- Treasury emission share hits 0% — permanent

### End of Month 10: PMAR Initialisation

All 25 Pioneer pool multipliers are set to 1.0. The PMAR begins collecting EMA(60) TVL ratio data for slope calculation. No governance vote — multipliers are fully automatic from this point forward.

### Month 11: Gauge Proposals Open

- Non-Pioneer pools can submit gauge proposals (burn 100 svZCHF/sUSDS equivalent in AuMM)
- All pools (Pioneer and non-Pioneer) begin ranking in the Efficiency Tournament
- Sandbox fast-track active: non-gauged pools reaching top 10% efficiency earn automatic gauge approval

### Months 11–12: CCB Transition

Emissions transition linearly from equal-weight to full CCB/EMA + PMAR allocation:

```
Day D weight = (1 - T) × equal_share + T × CCB_PMAR_share
T = (D - month_11_start) / (month_13_start - month_11_start)
```

At the start of month 11, T = 0 (100% equal weight). At the start of month 13, T = 1 (100% CCB/EMA × PMAR multipliers). The transition is smooth — no discontinuity, no cliff.

Bubble voting (multiplier [0.90–2.00]) activates for newly gauged pools during this period.

### Month 13 Day 1: Full Protocol Activation

- CCB/EMA fully active for all pools (Pioneer and non-Pioneer)
- Efficiency Tournament fully active — bottom 15% capped, excess redistributed
- Volume percentile floor at full discipline (15th percentile)
- New gauged pools receive emissions alongside the 25 Pioneers
- Incendiary Boost available for all gauged pools
- The protocol is now fully autonomous

The subsections above constitute the binding launch specification. All dates, parameters, and mechanisms are immutable from block 0.
