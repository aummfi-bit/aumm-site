# Bootstrap Rules

*How new pools enter the emission economy with governance gating and automatic emissions.*

---

## xxi. Cold-Start Design

### Pool Creation and Gauge Approval

**Pool creation is permissionless from block 0.** Anyone can deploy any pool with any token composition at any time. The Aequilibrium factory is open. This never changes.

A pool only becomes eligible for AuMM emissions after qualified LPs approve a gauge through governance. This is the single gatekeeping step. **Without gauge approval: no emissions, no Incendiary Boost, no 90-day multiplier.** Without it, an attacker deploys a pool and immediately starts extracting emissions. With it, existing LPs must collectively decide that the new pool deserves a share of the emission budget.

**The eligibility criteria are immutable.** Once a gauge is approved, the pool must still meet every anti-gaming criterion to receive emissions. Governance cannot waive, modify, or relax these rules. A gauge vote says "this pool may compete for emissions." The contract decides whether it actually qualifies.

This separates the three concerns cleanly: permissionless creation (anyone can build, from day one), democratic gauge approval (LPs decide what competes), immutable rules (the contract enforces discipline, always).

Core emission allocation remains automatic and immutable.

### Sandbox and Fast-Track

**Sandbox** is the permissionless default state. Any pool deployed without a gauge operates in the Sandbox from block 0. Sandbox pools receive **zero** CCB emissions and no Incendiary Boost, but they are ranked in the Efficiency Tournament alongside gauged pools. This proves the protocol is open without creating an emission exploit vector — anyone can build and demonstrate performance before seeking gauge approval.

**Fast-Track Rule.** If a non-gauged Sandbox pool sustains **top 10% efficiency** in the Efficiency Tournament for **3 consecutive epochs (6 weeks)** without leaving the top 10%, it earns **automatic gauge approval** — no governance vote required. The deposit is waived. This creates a meritocratic path: pools that prove real capital efficiency earn emissions without needing to campaign for votes. After fast-track approval, the pool receives the standard 90-day gauge boost (1.2x CCB multiplier) and becomes eligible for Incendiary Boost.

### The Bootstrapping Sequence

| Phase | Days | Driver | Purpose |
|-------|------|--------|---------|
| Gauge approval | Day 0 | AuMT governance vote | Quality gate — pool must pass governance before any boost |
| Incendiary Boost | Days 1–30 | svZCHF/sUSDS escrow into der Bodensee | Proof of conviction — operator deepens the autonomous reserve |
| 90-day gauge boost | Days 1–90 | Fixed 1.2x CCB multiplier (automatic) | Cold-start emission ramp — expires without vote or renewal |
| CCB takeover | Day 91+ | 60-day EMA | Institutional stability — the pool is now permanent infrastructure |

All layers require gauge approval first. No pool can access the Incendiary Boost or the 90-day gauge boost without passing governance. At day 91, the fixed boost expires. By this point, a successful pool has 90 days of TVL data baked into its EMA. The mechanical CCB weight takes the baton seamlessly. Failed pools lose both the boost and the EMA weight — they die naturally.

### Two boosts, different purposes

The bootstrapping sequence provides two distinct emission boosts that serve different functions and can operate independently:

**90-day gauge boost (automatic).** Every newly approved gauge receives a fixed **1.2x CCB multiplier** for 90 days. This is automatic — it activates the moment the gauge passes governance and expires on its own, with no vote and no renewal. A pool can have the 90-day boost **without** Incendiary: the gauge boost is the baseline cold-start ramp that every approved pool gets for free.

**Incendiary Boost (operator-funded, stacks on top).** A pool operator can **optionally** escrow **svZCHF/sUSDS** into der Bodensee Pool (one-sided inflow via smart-contract escrow) to activate a 30-day supplementary emission stream on top of whatever the pool is already earning. A pool can have both the 90-day gauge boost **and** Incendiary running simultaneously — the effects stack. The gauge boost adjusts the multiplier inside the CCB score; Incendiary is a separate priority skim from the block emission (see §xxii below). They are mechanically independent.

## xxii. Incendiary Boost

Incendiary Boost is a proof-of-conviction bootstrap mechanism. A pool operator deposits svZCHF/sUSDS into a smart-contract-controlled escrow. The protocol emits AuMM to the pool equally over 30 days as a supplementary emission stream pegged to the 85th efficiency percentile. The escrowed svZCHF/sUSDS is deposited one-sided into der Bodensee Pool — the operator sacrifices conviction capital to activate the protocol's routing engine.

### The Efficiency Scalar

The Incendiary emission rate is pegged to the 85th percentile of the Efficiency Tournament, scaled by the pool's own performance:

```
E_inc = E_85th × (2 - R)
```

Where `E_85th` is the emission density (AuMM per $1 TVL) of the pool at the 85th efficiency percentile, and `R` is the target pool's normalized efficiency rank (0 = most efficient, 1 = least efficient).

| Pool Efficiency | R | Multiplier (2 - R) | Effect |
|-----------------|------|-------------------|--------|
| Most efficient in protocol | ≈ 0 | 2.0x | Massive reward for utility |
| At 85th percentile cutoff | ≈ 0.85 | 1.15x | Modest boost |
| Below 85th percentile | > 0.85 | < 1.15x | Diminishing returns |

### Priority Skim

Since total emissions are fixed (BTC-style hard cap), Incendiary Boosts are priority claims on the **LP emission tranche** — i.e. **after** the der Bodensee bootstrap one-sided AuMM skim in Months 1–10 ([Protocol formulas (F-0)](11_formulas.md); zero thereafter). The protocol calculates total AuMM required for all active Incendiary Boosts, subtracts this from the LP tranche, then distributes the remainder via equal split or CCB. Every active Incendiary Boost directly reduces emissions to all other pools — active, efficient new pools temporarily tax every other pool's LP-tranche share. If five pools run simultaneous Incendiary Boosts, the entire protocol feels the dilution. The operator's escrowed svZCHF/sUSDS is deposited one-sided into der Bodensee Pool, deepening the autonomous reserve in exchange for the privilege of skipping the EMA queue.

### Renewal Rule

The Incendiary slot locks after 30 days. A second boost is only possible if the pool **is at or above the 85th percentile** in the Efficiency Tournament at the time of renewal request. No cycling boosts on underperforming pools.

### Anti-Wash-Trading

The 30-day limit plus the efficiency rank requirement makes wash trading uneconomical: the attacker pays more in swap fees (routed to der Bodensee Pool) than they can extract in boosted emissions. The protocol wins the fee-vs-emission spread.

### Immutable Parameters

All Incendiary Boost parameters are immutable from block 0: 30-day duration, 85th percentile peg, efficiency scalar formula, priority skim, and svZCHF/sUSDS escrow-to-Bodensee.

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

All eligibility criteria are immutable from block 0. No governance vote can waive, modify, or relax these rules. The CCB multiplier applies automatically to the 28 Miliarium pools (see [Theoretical foundations (§vii)](03_theoretical_foundation.md) and [Protocol formulas (F-8)](11_formulas.md); for numeric bounds, see [Constitution (§xxix)](10_constitution.md)). No voting over emission allocation. New gauges receive a **90-day 1.2x CCB multiplier** as a cold-start bootstrap — a fixed boost that expires automatically, with no vote and no renewal.

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
| Months 6–12 | 10th percentile | Exempt | Higher bar, still in discovery phase. |
| Month 13+ | 15th percentile | **Active** | Full discipline. Both volume percentile floor and efficiency-based emission caps apply. |

Percentile rankings are calculated against the protocol's own pool activity distribution — specifically, the trailing 3-epoch (6-week) rolling window of fee + yield revenue across all emission-eligible pools. This is a relative measure: as the protocol grows, the absolute bar rises organically.

**Gaming the grace period.** The exploit vector for the grace period is the gauge, not the pool. An attacker deploys a pool, gets a gauge approved, and milks the grace window before the fee/percentile checks activate. Switching deployer wallets or swapping one token to argue "different composition" doesn't help the attacker because the percentile floor is protocol-wide — a pool that generates no organic activity sits at the bottom of the distribution regardless of who deployed it or how many times it's been redeployed. The graduated percentile ramp is the natural defence: a pool earning zero fees can't stay above the 5th percentile for long, even with generous AuMM emission allocation.

### Hysteresis Buffer (Anti-Oscillation)

Binary thresholds with no dead zone create oscillation — a pool at the 14th percentile bounces between eligible and disqualified every cycle based on noise. The hysteresis buffer prevents random volatility from killing viable pools.

| Zone | Volume Percentile | Status | Action |
|------|------------------|--------|--------|
| **Safe** | Above 15th | Fully eligible | Normal emissions, no flags |
| **Warning** | 10th–15th | Flagged | Emissions continue normally. Pool must recover above the 15th percentile within 3 epochs (6 weeks). |
| **Cut** | Below 10th | Disqualified | Emissions cease immediately. Unallocated emissions are redistributed to remaining eligible pools. |

Emissions continue during the warning period. Cutting emissions from a pool in the warning zone reduces its attractiveness exactly when it needs to attract more volume — that's a death sentence disguised as a second chance. The 3-epoch recovery window gives the pool a genuine opportunity to recover while creating a hard deadline.

Re-qualification after disqualification requires the pool to sustain activity above the 15th percentile for 3 epochs (6 weeks) with no emissions. If it can generate organic activity without emission subsidies, it earned its way back.

### Emission Efficiency Tournament

The efficiency tournament is a relative ranking system that is entirely price-agnostic — designed to throttle inefficient pools without penalising productive pools during AuMM price appreciation.

All gauged pools **above $10K TVL** are ranked by their efficiency ratio — `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received` — using a **3-epoch (6-week) moving average** to prevent single-day glitches. Pools below $10K TVL are excluded from the ranking entirely and receive zero emissions regardless of gauge status. Higher ratio = more efficient (more revenue per unit of emission). The least efficient gauged pools receive hard emission caps regardless of their CCB-derived share:

| Efficiency Rank (gauged pools above $10K TVL) | Emission Cap | Effect |
|-----------------------------------------------|-------------|--------|
| Above 15th percentile | No cap | Full CCB emissions |
| 10th–15th percentile (bottom 15–10%) | 1% of total protocol emissions | Capped even if CCB share is higher |
| 5th–10th percentile (bottom 10–5%) | 0.5% of total protocol emissions | Harder cap |
| Below 5th percentile (bottom 5%) | 0.1% of total protocol emissions | Nearly starved |

The efficiency tournament activates at **month 13** of a pool's life (same as the volume percentile floor reaching full discipline).

**Excess emissions are redistributed.** When a pool is capped below its CCB-derived emission share, the excess is redistributed to uncapped pools pro-rata by their existing CCB share. This rewards productive pools rather than wasting the excess.

The efficiency tournament is price-agnostic by design — it prevents the reflexive disqualification problem where a rising AuMM price would cause fixed revenue hurdles to fail productive pools.

**Self-correcting.** A pool gets capped → receives fewer emissions → its efficiency ratio improves next cycle → it climbs out. No death spiral.

**Governance-capture resistant.** Even if a pool accumulates large TVL and earns a large CCB share while generating minimal fees, the protocol ranks its efficiency ratio at the bottom of the set. Despite a high CCB share, it receives at most 0.1% of emissions. The excess is redistributed to productive pools.

**Sacrificial lamb resistant.** An attacker tries to flood the bottom 15% with junk pools to shield their extractive pool from capping. Each lamb pool needs $10K TVL to enter the ranking, a gauge approval vote (depositing 100 svZCHF/sUSDS into der Bodensee Pool), and LP governance approval. Twenty lamb pools = $200K+ in capital at risk plus 2,000 svZCHF/sUSDS deposited. The $10K TVL floor makes the attack prohibitively expensive.

### Disqualification and Gauge Revocation

Pools that fail the anti-gaming criteria face a two-stage process:

**Stage 1: Disqualification.** A pool that falls below the 10th volume percentile (or fails other structural criteria) is disqualified — emissions cease immediately. The gauge remains intact. If the pool recovers above the 15th percentile for 3 epochs (6 weeks) with no emissions, it re-qualifies automatically.

**Stage 2: Gauge revocation.** A pool that remains disqualified for **4 consecutive epochs (8 weeks)** has its gauge permanently revoked. To restart emissions, the pool operator must submit a new gauge proposal (deposit 100 svZCHF/sUSDS into der Bodensee Pool) and win a fresh AuMT governance vote. This prevents dead pools from holding gauge slots indefinitely.

### How the Criteria Interact

After month 13, a gauged pool must clear the volume floor (or be disqualified) AND survive the efficiency ranking (or be capped). Volume floor catches dead pools. Efficiency caps catch extractive pools. Neither alone is sufficient. Both are self-correcting — no governance vote required.

## xxiv. Governance Gating (Non-Emission)

### Governance Proposals

Any qualified AuMT holder can submit a governance proposal — fee parameter changes. Proposals require depositing **1,000 svZCHF or sUSDS (whichever is higher)** one-sided into der Bodensee Pool. The deposit is automatic on submission — non-refundable regardless of outcome.

Every governance action deepens der Bodensee Pool reserves. The deposit filters spam (proposers must hold and sacrifice AuMM), deepens the autonomous reserve, and is non-recoverable. Self-regulating.

### Gauge Proposal

Any qualified AuMT holder may submit a gauge proposal requesting emission eligibility for a new pool. Submission deposit: **100 svZCHF or sUSDS (whichever is higher), deposited one-sided into der Bodensee Pool** — lower than other governance proposals because gauge requests are lower-stakes. If the pool fails the immutable criteria, the contract kills it automatically. The governance vote is a lightweight check on whether the pool deserves to compete, not a major protocol decision.

If approved by vote, the pool becomes emission-eligible subject to immutable criteria checks.

### Gauge Challenge

Any qualified AuMT holder can challenge an existing gauge if the pool is perceived as gaming or extractive. Challenge deposit: **1,000 svZCHF or sUSDS (whichever is higher), deposited one-sided into der Bodensee Pool**. A challenge triggers a governance vote: if the challenge succeeds (majority votes to revoke), the gauge is removed and the pool loses emission eligibility. If the challenge fails, the deposit is still in Bodensee — the challenger accepted that risk.

This creates a community enforcement layer on top of the immutable anti-gaming criteria. The contract catches pools that fail the volume percentile floor or the efficiency caps automatically. Gauge challenges catch pools that technically pass the criteria but are extractive in ways the contract can't detect — coordinated wash trading, circular routing schemes, or pools that exist solely to farm emissions for a single actor.

### Miliarium Aureum Composition Challenge

Pool token composition is immutable on-chain — there is no mechanism to swap a token inside a deployed pool contract. A composition challenge therefore follows a **deprecate-and-replace** path:

1. **Governance vote** — a qualified AuMT holder submits a composition challenge proposal. It passes only with **2/3 protocol-wide tessera-weighted approval**.
2. **Deprecation** — the old pool's gauge is revoked; emissions cease and the pool enters wind-down.
3. **New pool launch** — a replacement pool with the updated composition is deployed into the same Miliarium slot, following the standard bootstrap path: gauge proposal, gauge vote, and — if approved — the 90-day gauge boost and optional Incendiary Boost apply as normal.

A single proposal may cover **both** theme assets simultaneously if both have failed — forum discussion builds consensus on the pair before the on-chain vote.

Composition intent is binding: the replacement token must be the same asset type or economically similar. **Like-for-like** means: same sector, same risk profile, same template role (yield core vs routing anchor vs theme asset). This is a renewal path, not a redesign path.

#### What qualifies as "economically similar"

The composition challenge exists because assets cease to exist — tokens get delisted, wrappers lose support, issuers shut down. The goal is to maintain the Miliarium Aureum as a functioning representation of the economy, not to pick winners.

**Crypto tokens:**

| Scenario | Replacement | Valid? | Reasoning |
|:---------|:------------|:-------|:----------|
| cbBTC delisted | tBTC or WBTC | **Yes** | Same asset type — wrapped Bitcoin |
| cbBTC delisted | Tokenized BTC ETF | **Likely yes** | Same underlying exposure (Bitcoin), different wrapper — requires 2/3 to judge |
| cbBTC delisted | Bitcoin L2 token (e.g., STX) | **No** | An L2 governance token is not Bitcoin, just as ARB or OP are not ETH |
| cbBTC delisted | PAXG | **No** | Different asset class entirely (gold vs Bitcoin) |

**Tokenized equities:**

| Scenario | Replacement | Valid? | Reasoning |
|:---------|:------------|:-------|:----------|
| Company acquired or merged | Acquirer or merged entity | **Yes** | Direct successor — same economic exposure continues |
| Company ceases to exist | Same-sector peer | **Yes** | E.g., Goldman Sachs → Morgan Stanley, Eli Lilly → Bristol-Myers Squibb |
| Company ceases to exist | Different-sector company | **No** | Violates same-sector requirement |

This is not a stock-picking exercise. Composition challenges activate when an asset **ceases to function**, and the replacement preserves the pool's role in the constellation.

#### The 28 are a blueprint, not the full economy

The 28 Miliarium pools are a curated economic blueprint for CCB execution — a diversified foundation that ensures the protocol has structural fee generation across asset classes from day one. They are **not** meant to exhaust every possible token or market.

If a token, stablecoin, or asset class is missing from the 28, the path is **not** a composition challenge. It is:

1. **Deploy a new pool** — permissionless from block 0
2. **Get a gauge approved** — submit a proposal, deposit svZCHF/sUSDS into der Bodensee Pool, win the AuMT vote
3. **Earn emissions** — through the standard CCB rules, Incendiary Boost, and 90-day gauge boost

The Miliarium system is plug-and-play: new pools route through the constellation's connectors (ixEdelweiss, ixLibertas, ixCambio), generate yield from ERC-4626 vaults, and bootstrap via Incendiary and gauge boost mechanics — the same infrastructure the 28 founding pools use.

**The community is actively encouraged** to monitor the market for new opportunities and propose new pools: emerging stablecoins, new tokenized RWAs (e.g., Ondo products — new bond or equity wrappers), and crypto tokens with meaningful trading volume. A thriving ecosystem of gauged pools beyond the 28 is the design intent — the Miliarium pools are the anchor, not the ceiling.

### On-Chain-Only Proposal Rule

Every proposal must reference only verifiable on-chain data (addresses, block ranges, and contract-derived metrics). Proposals based on off-chain-only claims are invalid.

## xxv. Immutable Reference

See [Immutable Parameters (§xxix)](10_constitution.md).
