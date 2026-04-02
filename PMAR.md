# Pioneer Multiplier Adjustment Rule (PMAR)

**Addendum to the Continuous Central Bank (CCB) Section**
*Immutable from Block 0 — Activates at Month 11 (CCB Transition)*
*Final Version — April 2026*

---

## Purpose

The Pioneer Multiplier Adjustment Rule (PMAR) is a minimal, deterministic, oracle-free mechanism that automatically steers emission multipliers across the 25 immutable Mercatūs Praecursorii. It replaces governance-driven multiplier voting entirely. The system responds **solely** to the slope (first derivative) of two EMA(60) TVL ratios and applies simple **+/-0.05** adjustments:

- **Global adjustment**: When the Pioneer set as a whole loses share of protocol TVL, every Mercatūs Praecursorii receives a uniform **+0.05** boost. When the Pioneer set gains share, every pool receives a uniform **-0.05** penalty.
- **Per-pool adjustment**: Any individual Mercatūs Praecursorii that is gaining relative share inside the Pioneer constellation receives a **-0.05** intra adjustment; a pool losing relative share receives a **+0.05** boost.

All adjustments are additive, start from a neutral base of **1.0**, and remain strictly clamped to **[0.75, 1.25]**.

There is no normalisation step. Multipliers are relative — each pool's emission share is determined by:

```
share(pool_i) = (TVL_EMA60(pool_i) * M_i(t) * Incendiary_mult(pool_i)) / sum_all_pools(TVL_EMA60 * M * Incendiary_mult)
```

A higher multiplier means a larger share of the fixed per-block emission. The sum in the denominator absorbs any aggregate shift automatically.

---

## Activation and Base Values

- Applies **exclusively** to the 25 immutable Mercatūs Praecursorii (pre-tagged at launch).
- Non-Mercatūs Praecursorii are unaffected (pure CCB/EMA weighting; their multiplier is implicitly 1.0).
- **Activation**: Linear interpolation during the CCB transition (month 11 day 1 to month 13 day 1). Before month 11, Mercatūs Praecursorii receive equal emissions. On month 13 day 1, the full CCB + PMAR math applies. During the transition:

```
T = (D - month_11_start) / (month_13_start - month_11_start)
effective_share = (1 - T) * equal_share + T * CCB_PMAR_share
```

- **Initial multiplier**: Every Mercatūs Praecursorii starts at exactly **1.0**.
- All 25 Mercatūs Praecursorii have a minimum seed TVL at launch. If a pool's TVL approaches zero, its emission share approaches zero naturally via the TVL term in the numerator — no special-case handling required.

---

## Inputs (All On-Chain, Oracle-Free)

Recalculated at every bi-weekly governance cycle boundary using the 60-day EMA already maintained by the CCB engine.

**Global Pioneer ratio** — Pioneer share of protocol TVL:

```
r_P(t) = TVL_Pioneer_EMA60(t) / TVL_Protocol(t)
```

**Per-pool ratio** — each Mercatūs Praecursorii's share within the Pioneer constellation:

```
r_i(t) = TVL_i_EMA60(t) / TVL_Pioneer_EMA60(t)     for each Mercatūs Praecursorii i = 1..25
```

---

## Slope Calculation

```
slope_P(t) = r_P(t) - r_P(t-1)
slope_i(t) = r_i(t) - r_i(t-1)
```

Where `t-1` is the previous cycle boundary.

---

## Dead Zone

A dead zone prevents noise-driven oscillation when slopes hover near zero. If the absolute slope is below 0.1% of the ratio, the adjustment is zero:

```
epsilon_P = 0.001 * r_P(t)
epsilon_i = 0.001 * r_i(t)
```

If `|slope_P(t)| < epsilon_P`, the global adjustment is 0.
If `|slope_i(t)| < epsilon_i`, the intra-pool adjustment for pool i is 0.

---

## Adjustment Rules

**Global adjustment** (uniform to all 25 pools):

```
delta_global =
    +0.05   if slope_P(t) < -epsilon_P    (Pioneers losing overall share)
    -0.05   if slope_P(t) > +epsilon_P    (Pioneers gaining overall share)
     0      otherwise                      (within dead zone)
```

**Intra-pool adjustment** (per pool):

```
delta_intra_i =
    +0.05   if slope_i(t) < -epsilon_i    (pool losing share within Pioneers)
    -0.05   if slope_i(t) > +epsilon_i    (pool gaining share within Pioneers)
     0      otherwise                      (within dead zone)
```

**Raw multiplier update**:

```
M_i(t) = clamp( M_i(t-1) + delta_global + delta_intra_i,  0.75,  1.25 )
```

---

## Scenario Walkthrough

**Case**: Pool i is gaining TVL (`slope_i > epsilon_i`) while the Pioneer set as a whole is losing share of protocol TVL (`slope_P < -epsilon_P`).

- `delta_global = +0.05` (boost to every Mercatūs Praecursorii)
- `delta_intra_i = -0.05` (penalty to the gaining pool)
- **Net for pool i**: `+0.05 - 0.05 = 0` — no change to its multiplier.
- **Net for other Mercatūs Praecursorii** (those also losing intra-share): `+0.05 + 0.05 = +0.10`.

The gaining pool holds steady while the declining pools get boosted. The Pioneer set as a whole shifts emission weight upward (via higher multipliers in the score formula) relative to non-Mercatūs Praecursorii — exactly the anticyclical behaviour intended.

**Case**: All Mercatūs Praecursorii growing proportionally, Pioneer set gaining protocol share.

- `slope_P > epsilon_P` → `delta_global = -0.05`
- All `|slope_i| < epsilon_i` (proportional growth, no intra-change) → `delta_intra_i = 0`
- **Net for all Mercatūs Praecursorii**: `-0.05` each. Multipliers drift downward, reducing Pioneer emission share relative to non-Mercatūs Praecursorii. Protocol self-corrects against Pioneer dominance.

---

## Integration with CCB

The PMAR multiplier M_i(t) replaces the former governance-voted multiplier in the CCB score formula:

```
Score(pool_i) = TVL_EMA60(pool_i) * M_i(t) * Incendiary_mult(pool_i)
```

Where:
- `TVL_EMA60` is the 60-day exponential moving average of on-chain TVL
- `M_i(t)` is the PMAR multiplier (Mercatūs Praecursorii only; implicitly 1.0 for non-Mercatūs Praecursorii)
- `Incendiary_mult` is the Incendiary Boost multiplier (1.0 for most pools; > 1.0 for pools with an active burn-funded boost)

Each pool's share of per-block emissions is `Score(pool_i) / sum(all pool scores)`.

All other CCB disciplines (EMA weighting, Efficiency Tournament, eligibility criteria) remain orthogonal and unchanged.

---

## Guarantees

- **Bounded**: All multipliers stay inside [0.75, 1.25] at every step.
- **Anticyclical**: Group-level loss of share triggers a collective boost; internal crowding triggers relative penalties.
- **Stable**: The 0.1%-of-ratio dead zone prevents flip-flopping on noise.
- **Simplicity**: Only EMA(60) data already present in the CCB; two sign checks per pool (with dead zone); one clamp pass. Gas cost is negligible.
- **Immutability**: The entire rule set — including the +/-0.05 step size, [0.75, 1.25] clamp bounds, dead zone threshold (0.1% of ratio), and EMA horizon — is hard-coded and cannot be altered post-deployment.

---

*All roads lead from the Miliarium Aureum. The engine now steers them automatically.*
