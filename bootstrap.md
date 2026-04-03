# Bootstrap Rules

*How new pools enter the emission economy with governance gating and automatic emissions.*

---

## xxi. Cold-Start Design

### Pool Creation and Gauge Approval

**Pool creation is permissionless from block 0.** Anyone can deploy any pool with any token composition at any time. The Aequilibrium factory is open. This never changes.

A pool only becomes eligible for AuMM emissions after qualified LPs approve a gauge through governance. This is the single gatekeeping step. Without it, an attacker deploys a pool and immediately starts extracting emissions. With it, existing LPs must collectively decide that the new pool deserves a share of the emission budget.

**The eligibility criteria are immutable.** Once a gauge is approved, the pool must still meet every anti-gaming criterion to receive emissions. Governance cannot waive, modify, or relax these rules. A gauge vote says "this pool may compete for emissions." The contract decides whether it actually qualifies.

This separates the three concerns cleanly: permissionless creation (anyone can build, from day one), democratic gauge approval (LPs decide what competes), immutable rules (the contract enforces discipline, always).

Core emission allocation remains automatic and immutable.

## xxii. Incendiary Boost

Incendiary Boost remains a proof-of-conviction mechanism:

- operator escrows AuMM
- supplementary emissions stream for 30 days
- escrowed AuMM is burned
- all logic executes on-chain with no admin controls

## xxiii. Anti-Gaming Engine

Pools must meet ALL criteria to remain eligible for AuMM emissions:

| Criterion | Requirement | Rationale |
|-----------|-------------|-----------|
| Protocol version | Aequilibrium only | No legacy pool farming |
| ERC-4626 composition ("4626 Quality Gate") | **≥52%** yield-bearing tokens by weight. Each ERC-4626 token must have **≥$5M, 30 BTC, or 4,000,000 svZCHF (whichever is largest) in its underlying vault** (`totalAssets()`) to count toward the 52% threshold. | Ensures pools generate real protocol yield fees. Three independent currency-denominated floors (USD, BTC, CHF) prevent any single inflation or devaluation event from eroding the quality gate. |
| Minimum TVL | $10K **7-day SMA** (exempt during months 0–3 grace period) | Filters ghost pools. The 7-day SMA prevents flickering eligibility from intra-day price fluctuations — a pool at $10,001 that dips to $9,999 from a price move doesn't lose eligibility until the 7-day average drops below $10K. |
| Volume percentile floor | Graduated by pool age (see Graduated Grace Period below) | Benchmarks pool activity against protocol-wide distribution |
| Efficiency-based emission caps | Gauged pools ranked by efficiency ratio; bottom 15% capped (see Emission Efficiency Tournament below). **Activates at month 13 (after CCB transition).** | Throttles inefficient pools without reflexive disqualification. Price-agnostic. |
| No self-referential tokens | AuMM cannot be a pool component | Prevents circular farming |

All eligibility criteria are immutable from block 0. No governance vote can waive, modify, or relax these rules. The CCB multiplier applies automatically to the 28 Miliarium Aureum pools (see `theoretical_foundation.md` section vii and `formulas.md` F-8). No Bubble voting and no voting over emission allocation.

### Why TVL-Based Governance Eliminates the Wrapper Problem

In token-weighted governance (Balancer/Aura), bear markets enable cheap governance capture through lock multipliers and meta-governance amplifiers. AuMM carries zero governance power. AuMT governance weight equals the USD value of the LP position in qualified pools. To get 5% of governance power, you need 5% of protocol TVL in real capital. No lock multiplier. No boost. No amplifier. Bear market doesn't help the attacker — governance weight is TVL-denominated, not token-price-denominated.

**Wrappers and composability layers are welcome.** Convex/Aura-style vaults that hold AuMT carry full governance weight proportional to the underlying TVL. They cannot amplify governance because there's nothing to amplify. The TVL-based governance model IS the anti-capture mechanism.

Pools containing AuMT follow all the same rules as any other pool — permissionless creation, gauge approval via AuMT vote, full anti-gaming criteria.

### Graduated Grace Period

New pools need time to get discovered by aggregators, indexed by bots, and build organic volume. The graduated grace period introduces discipline incrementally, preserving the discovery layer while filtering out pools that never find traction.

| Pool Age | Volume Percentile Floor | Efficiency Caps | Notes |
|----------|------------------------|-----------------|-------|
| Months 0–3 | None | Exempt | Full experimentation window. Pool must still meet structural criteria (ERC-4626 composition, no self-referential tokens). |
| Months 3–6 | 5th percentile | Exempt | First signal required: pool must demonstrate it's not completely dead. |
| Months 6–12 | 10th percentile | Exempt | Higher bar, still in discovery phase. Treasury stabilization active. |
| Month 13+ | 15th percentile | **Active** | Full discipline. Both volume percentile floor and efficiency-based emission caps apply. Aligned with treasury exit. |

Percentile rankings are calculated against the protocol's own pool activity distribution — specifically, the trailing 2-epoch (4-week) rolling window of fee + yield revenue across all emission-eligible pools. This is a relative measure: as the protocol grows, the absolute bar rises organically.

**Gaming the grace period.** The exploit vector for the grace period is the gauge, not the pool. An attacker deploys a pool, gets a gauge approved, and milks the grace window before the fee/percentile checks activate. Switching deployer wallets or swapping one token to argue "different composition" doesn't help the attacker because the percentile floor is protocol-wide — a pool that generates no organic activity sits at the bottom of the distribution regardless of who deployed it or how many times it's been redeployed. The graduated percentile ramp is the natural defence: a pool earning zero fees can't stay above the 5th percentile for long, even with generous AuMM emission allocation.

### Hysteresis Buffer (Anti-Oscillation)

Binary thresholds with no dead zone create oscillation — a pool at the 14th percentile bounces between eligible and disqualified every cycle based on noise. The hysteresis buffer prevents random volatility from killing viable pools.

| Zone | Volume Percentile | Status | Action |
|------|------------------|--------|--------|
| **Safe** | Above 15th | Fully eligible | Normal emissions, no flags |
| **Warning** | 10th–15th | Flagged | Emissions continue normally. Pool must recover above the 15th percentile within 2 epochs (4 weeks). |
| **Cut** | Below 10th | Disqualified | Emissions cease immediately. Unallocated emissions are redistributed to remaining eligible pools. |

Emissions continue during the warning period. Cutting emissions from a pool in the warning zone reduces its attractiveness exactly when it needs to attract more volume — that's a death sentence disguised as a second chance. The 2-epoch recovery window gives the pool a genuine opportunity to recover while creating a hard deadline.

Re-qualification after disqualification requires the pool to sustain activity above the 15th percentile for 2 epochs (4 weeks) with no emissions. If it can generate organic activity without emission subsidies, it earned its way back.

### Emission Efficiency Tournament

The efficiency tournament is a relative ranking system that is entirely price-agnostic — designed to throttle inefficient pools without penalising productive pools during AuMM price appreciation.

All gauged pools **above $10K TVL** are ranked by their efficiency ratio — `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received` — using a **2-epoch (4-week) moving average** to prevent single-day glitches. Pools below $10K TVL are excluded from the ranking entirely and receive zero emissions regardless of gauge status. Higher ratio = more efficient (more revenue per unit of emission). The least efficient gauged pools receive hard emission caps regardless of their CCB-derived share:

| Efficiency Rank (gauged pools above $10K TVL) | Emission Cap | Effect |
|-----------------------------------------------|-------------|--------|
| Above 15th percentile | No cap | Full CCB emissions |
| 10th–15th percentile (bottom 15–10%) | 1% of total protocol emissions | Capped even if CCB share is higher |
| 5th–10th percentile (bottom 10–5%) | 0.5% of total protocol emissions | Harder cap |
| Below 5th percentile (bottom 5%) | 0.1% of total protocol emissions | Nearly starved |

The efficiency tournament activates at **month 13** of a pool's life (same as the volume percentile floor reaching full discipline).

**Excess emissions are redistributed.** When a pool is capped below its CCB-derived emission share, the excess is redistributed to uncapped pools pro-rata by their existing CCB share. This rewards productive pools rather than burning the excess.

The efficiency tournament is price-agnostic by design — it prevents the reflexive disqualification problem where a rising AuMM price would cause fixed revenue hurdles to fail productive pools.

**Self-correcting.** A pool gets capped → receives fewer emissions → its efficiency ratio improves next cycle → it climbs out. No death spiral.

**Governance-capture resistant.** Even if a pool accumulates large TVL and earns a large CCB share while generating minimal fees, the protocol ranks its efficiency ratio at the bottom of the set. Despite a high CCB share, it receives at most 0.1% of emissions. The excess is redistributed to productive pools.

**Sacrificial lamb resistant.** An attacker tries to flood the bottom 15% with junk pools to shield their extractive pool from capping. Each lamb pool needs $10K TVL to enter the ranking, a gauge approval vote (burning 100 svZCHF/sUSDS equivalent in AuMM), and LP governance approval. Twenty lamb pools = $200K+ in capital at risk plus 2,000 equivalent in AuMM burned. The $10K TVL floor makes the attack prohibitively expensive.

### Disqualification and Gauge Revocation

Pools that fail the anti-gaming criteria face a two-stage process:

**Stage 1: Disqualification.** A pool that falls below the 10th volume percentile (or fails other structural criteria) is disqualified — emissions cease immediately. The gauge remains intact. If the pool recovers above the 15th percentile for 2 epochs (4 weeks) with no emissions, it re-qualifies automatically.

**Stage 2: Gauge revocation.** A pool that remains disqualified for **4 consecutive epochs (8 weeks)** has its gauge permanently revoked. To restart emissions, the pool operator must submit a new gauge proposal (burn 100 svZCHF/sUSDS equivalent in AuMM) and win a fresh AuMT governance vote. This prevents dead pools from holding gauge slots indefinitely.

### How the Criteria Interact

After month 13, a gauged pool must clear the volume floor (or be disqualified) AND survive the efficiency ranking (or be capped). Volume floor catches dead pools. Efficiency caps catch extractive pools. Neither alone is sufficient. Both are self-correcting — no governance vote required.

## xxiv. Governance Gating (Non-Emission)

### Governance Proposals

Any qualified AuMT holder can submit a governance proposal — fee parameter changes, treasury spending. Proposals require burning **1,000 svZCHF or sUSDS equivalent (whichever is higher) worth of AuMM**. The AuMM is burned automatically on submission — non-refundable regardless of outcome.

Every governance action creates deflationary pressure on AuMM. The deposit filters spam (proposers must hold and sacrifice AuMM), funds no one (tokens are destroyed, not transferred), and tightens supply. Self-regulating.

### Gauge Proposal

Any qualified AuMT holder may submit a gauge proposal requesting emission eligibility for a new pool. Submission deposit: **100 svZCHF or sUSDS equivalent (whichever is higher) worth of AuMM (burned)** — lower than other governance proposals because gauge requests are lower-stakes. If the pool fails the immutable criteria, the contract kills it automatically. The governance vote is a lightweight check on whether the pool deserves to compete, not a major protocol decision.

If approved by vote, the pool becomes emission-eligible subject to immutable criteria checks.

### Gauge Challenge

Any qualified AuMT holder can challenge an existing gauge if the pool is perceived as gaming or extractive. Challenge deposit: **1,000 svZCHF or sUSDS equivalent (whichever is higher) worth of AuMM (burned)**. A challenge triggers a governance vote: if the challenge succeeds (majority votes to revoke), the gauge is removed and the pool loses emission eligibility. If the challenge fails, the AuMM is still burned — the challenger accepted that risk.

This creates a community enforcement layer on top of the immutable anti-gaming criteria. The contract catches pools that fail the volume percentile floor or the efficiency caps automatically. Gauge challenges catch pools that technically pass the criteria but are extractive in ways the contract can't detect — coordinated wash trading, circular routing schemes, or pools that exist solely to farm emissions for a single actor.

### Miliarium Aureum Composition Challenge

- Any qualified AuMT holder may submit a composition challenge proposal.
- Proposal passes only with **2/3 protocol-wide tessera-weighted approval**.
- Composition intent is binding: replacement token must be same asset type or economically similar.
- This mechanism is for like-for-like renewal only; pool function and economic role must remain intact.

### On-Chain-Only Proposal Rule

Every proposal must reference only verifiable on-chain data (addresses, block ranges, and contract-derived metrics). Proposals based on off-chain-only claims are invalid.

## xxv. Immutable Reference

See Immutable Parameters in `constitution.md`.
