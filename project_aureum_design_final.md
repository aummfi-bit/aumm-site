# Project Aureum — Protocol Design Document

*CONFIDENTIAL — Founding Team Only*
*Final Version — March 2026*
*aumm.fi*

---

## Pool Bootstrapping: The Cold Start Solution

The CCB's 60-day EMA creates a deliberate inertia — new pools have zero "memory" and earn minimal emissions for their first two months. This is a feature for established pools (anticyclical stability) but a problem for new pools (the cold start trap). Three mechanisms solve this without compromising the CCB's integrity. All three require gauge approval first.

### The Incendiary Boost (Proof-of-Burn Bootstrapping)

A pool operator deposits AuMM into a smart-contract-controlled position. That exact amount of AuMM is emitted to the pool equally over 30 days as a supplementary emission stream. This is not free — the operator burns conviction capital to activate the protocol's routing engine.

**The efficiency scalar.** The Incendiary emission rate is pegged to the 85th percentile of the Efficiency Tournament, scaled by the pool's own performance:

```
E_inc = E_85th × (2 - R)
```

Where `E_85th` is the emission density (AuMM per $1 TVL) of the pool at the 85th efficiency percentile, and `R` is the target pool's normalized efficiency rank (0 = most efficient, 1 = least efficient).

| Pool Efficiency | R | Multiplier (2 - R) | Effect |
|----------------|---|-------------------|--------|
| Most efficient in protocol | ≈ 0 | 2.0× | Massive reward for utility |
| At 85th percentile cutoff | ≈ 0.85 | 1.15× | Modest boost |
| Below 85th percentile | > 0.85 | < 1.15× | Diminishing returns |

**The priority skim — emission dilution by design.** Since total emissions are fixed (BTC-style hard cap), Incendiary Boosts are priority claims on block rewards. The protocol calculates total AuMM required for all active Incendiary Boosts, subtracts this from the block emission, then distributes the remainder via the CCB. **This means every active Incendiary Boost directly reduces emissions to all other pools.** Active, efficient new pools temporarily tax every existing pool's emission share. If five pools run simultaneous Incendiary Boosts, the entire protocol feels the dilution. This is intentional: the protocol subsidises its own future by skimming its own present. Stagnant pools relying on accumulated EMA weight see their emissions compressed, creating pressure to stay productive or lose share to the newcomers. The operator's escrowed AuMM is permanently burned — making AuMM scarcer for all holders long-term in exchange for the privilege of skipping the EMA queue.

**Renewal rule.** The Incendiary slot locks after 30 days. A second boost is only possible if the pool **is at or above the 85th percentile** in the Efficiency Tournament at the time of renewal request. A pool that stayed in the top 10% throughout its first boost qualifies immediately. No cycling boosts on underperforming pools.

**Anti-wash-trading.** The 30-day limit plus the efficiency rank requirement makes wash trading uneconomical: the attacker pays more in swap fees (routed to buyback-and-burn) than they can extract in boosted emissions. The protocol wins the fee-vs-emission spread.

### Bubble Voting (90-Day Governance Multiplier)

For the first 90 days after gauge approval, a new pool is eligible for a **Bubble multiplier** — a tessera-weighted governance vote with a wider range than Pioneer multipliers:

| Discrete Steps | 0.90 | 1.00 | 1.20 | 1.50 | 2.00 |
|---------------|------|------|------|------|------|

**Pioneer and Bubble multipliers stack.** A pool that earns a Pioneer tag at gauge approval receives both multipliers during its first 90 days: the Pioneer multiplier [0.90–1.10] and the Bubble multiplier [0.90–2.00]. After day 91, the Bubble expires and only the Pioneer multiplier remains. The founding Miliarium Aureum pools receive both multipliers from launch — they are simultaneously the first Pioneers and the first Bubble-eligible pools.

**The final Bubble multiplier is the tessera-weighted average of all votes cast for that pool.** This allows LPs to express strategic conviction: a 2.0× vote on a new Swiss Franc/Bitcoin pool signals strong ecosystem alignment. A 0.9× vote on a suspected wash-trading pool acts as a social consensus firewall.

**The hand-off.** At day 91, the Bubble expires. By this point, a successful pool has 90 days of TVL data baked into its EMA. The mechanical CCB weight "takes the baton" from the governance boost seamlessly. Failed pools lose both the Bubble and the EMA weight — they die naturally.

**Bubble votes occur every 6 weeks** (same cycle as Pioneer multiplier votes). Only qualified AuMT holders can vote.

### The Bootstrapping Sequence

| Phase | Days | Driver | Purpose |
|-------|------|--------|---------|
| Gauge approval | Day 0 | AuMT governance vote | Quality gate — pool must pass governance before any boost |
| Incendiary Boost | Days 1–30 | AuMM escrow by operator | Proof of conviction — builder buys into the ecosystem |
| Bubble Vote | Days 1–90 | Tessera-weighted multiplier [0.9–2.0] | Social alignment — LPs endorse or penalise the pool |
| CCB takeover | Day 91+ | 60-day EMA | Institutional stability — the pool is now permanent infrastructure |

All three layers require gauge approval first. No pool can access the Incendiary Boost or Bubble Vote without passing governance.

### The Permissionless Sandbox

Pool creation is permissionless from block 0. Any pool can be deployed without a gauge. Non-gauged pools operate in the **Sandbox**:

- They receive base EMA emissions only (no Incendiary Boost, no Bubble multiplier)
- They are ranked in the Efficiency Tournament alongside all other pools
- They have no governance voice (no Pioneer multiplier voting, no Bubble voting)

**The fast-track rule.** If a non-gauged Sandbox pool reaches the **top 10% efficiency** in the Efficiency Tournament organically — without any emission boost — it earns **automatic gauge approval**. No governance vote required. The protocol recognises proven productivity and removes the governance bottleneck.

This gives the protocol experimentation without emission risk. Builders can deploy, prove efficiency organically, and earn their way into full emission eligibility. The fast-track replaces politics with performance.

---
## Governance: The "LP = Power" Model

### Emission Direction: The CCB Engine

Emission allocation is driven by the **Continuous Central Bank (CCB)** — not by direct gauge voting. Each pool's base emission weight is its 60-day EMA of on-chain TVL as a share of total protocol TVL. Capital allocates itself.

Governance participation is limited to **Pioneer multiplier voting**: tessera-weighted votes set each Pioneer pool's multiplier within [0.90–1.10] every bi-weekly cycle. This is the only emission-direction governance action. See **The Continuous Central Bank** section for the full formula and mechanics.

- **Voting power = dampened AuMT.** `(AuMT_value × time_in_pool)^(1/4)` — same formula as protocol governance. 14-day qualification, 6-month on-ramp, any withdrawal resets to zero. See **Governance** for details.
- The 50% LP bonus from swap fees distributes to LPs who participated in multiplier voting — creating an incentive to both provide liquidity and participate in governance.

Every bi-weekly governance cycle:
1. CCB recalculates each pool's 60-day EMA TVL weight
2. Active Incendiary Boosts are calculated as priority claims on block emissions
3. Per-block emission streaming adjusts at cycle boundary
4. LP bonus distributes to voting participants

Every 6-week multiplier vote:
1. Qualified LPs vote on Pioneer pool multipliers (discrete steps: 0.90, 0.95, 1.00, 1.05, 1.10)
2. Qualified LPs vote on Bubble multipliers for new pools in their 90-day window (discrete steps: 0.90, 1.00, 1.20, 1.50, 2.00)
3. Final multipliers = tessera-weighted average of votes cast per pool
4. Emission shares recalculated with updated multipliers

### Emissions Directed to Unqualified Pools

If the CCB directs emissions toward pools that do not meet eligibility criteria (see Anti-Gaming Criteria below), those emissions are **not distributed to the pool**. Instead, the equivalent AuMM value is routed to the **buyback-and-burn mechanism**. This means:

- Votes wasted on ineligible pools accelerate deflation
- There is no economic benefit to gaming the vote toward unqualified pools
- The protocol benefits even from misallocated votes
- Voters are incentivised to direct emissions to productive pools or accept that their misdirected votes burn supply (which still benefits all remaining holders)

### Protocol Governance (Non-Emission Decisions)

For decisions beyond emission direction (fee parameters, treasury, upgrades), governance power is proportional to **active LP position in emission-qualified pools only** (AuMT held in qualifying pools):

```
Era 1 (Year 0–4, pre-halving):   voting_power = (qualified_AuMT_value × time_in_pool)^(1/4)
Era 2 (post-first-halving):      voting_power = (qualified_AuMT_value × time_in_pool)^(1/3)
```

**`qualified_AuMT_value` is the USD-denominated value of the liquidity the tessera represents** — not the number of AuMT tokens held. Each tessera is a proportional claim on its pool's TVL. An AuMT representing a $50K position in ixAppia carries more governance weight than an AuMT representing a $5K position in a smaller pool, because the underlying locked value is different. Different pools have different TVLs and different token compositions; the governance formula normalises across all of them by pricing each tessera at the current market value of the liquidity it represents.

This ensures governance power reflects real economic commitment — not which pool you happen to be in, but how much capital you have at risk in productive pools.

The dampening exponent transitions from fourth root to cube root at the first halving block. This is a protocol-wide parameter shift — all positions recalculate under the new exponent, regardless of when they were opened. There is no two-tier governance class.

**Why the transition matters:**

- **Era 1 (fourth root):** A $100M position has 18× the governance weight of a $1K position. At low TVL, a single whale can represent 20%+ of the entire protocol. Maximum compression prevents single-actor capture when the protocol is most vulnerable. The whale still has more governance weight than a small LP — they just can't steamroll every vote.
- **Era 2 (cube root):** A $100M position has 46× the governance weight of a $1K position. By year 4, TVL growth has naturally diluted individual power — a $10M whale in a $200M protocol is 5%, not 20%. The ecosystem no longer needs training wheels. The exponent relaxes because the primary decentralization force is now TVL distribution, not governance math.

The transition trigger is the halving block itself — immutable in the contract, no governance vote required, no discretionary timing.

AuMT in pools that fail any eligibility criterion carries zero governance weight. This ensures governance power flows exclusively from productive capital — the same capital that earns emissions and generates protocol fees.

**Governance power for non-emission decisions derives exclusively from active, qualified AuMT positions. AuMT in non-qualified pools carries zero weight. Voting power cannot be purchased on the open market.**

### Minimum Qualification Period and Governance On-Ramp

**Days 0–14: Zero governance weight.** Voting power requires at least **14 days (one full governance cycle)** of continuous qualified AuMT holding before any contribution to the governance power calculation. During this period, `time_in_pool = 0` in the formula — the position is invisible to governance.

**Days 14–180: Governance on-ramp.** After the 14-day qualification, `time_in_pool` begins accruing from zero. Because the governance formula uses `(qualified_AuMT_value × time_in_pool)^(1/4)`, voting power grows sublinearly with time. An LP at day 14 has minimal power. By month 6 (day 180), they reach **full voting weight**. This 6-month on-ramp ensures that governance power reflects sustained commitment, not recent capital deployment.

**Any withdrawal resets everything to zero.** If an LP removes liquidity from a qualified pool — any amount, even 1% — their governance power for that position drops to zero immediately, `time_in_pool` resets to zero, and the 14-day qualification clock restarts from scratch. The 6-month on-ramp begins again.

This eliminates:
- **Flash-LP attacks:** Borrow capital, deposit, vote, withdraw in the same block or day
- **Snapshot-based manipulation:** Accumulate AuMT moments before a governance snapshot, then exit
- **Cycle-boundary gaming:** Deposit at the end of a cycle to vote, remove at the start of the next
- **Ghost governance:** Withdraw most liquidity while retaining outsized governance weight from original position's time-weighting
- **Capital-rotation attacks:** Deposit large capital, vote immediately, then move capital elsewhere — the 6-month on-ramp means new capital has negligible governance power

### Soft Quorum for Major Decisions

Not all governance decisions carry equal weight. Major changes require minimum participation to prevent low-turnout capture:

| Decision Type | Quorum Requirement | Deposit (in AuMM, burned) | Failure Mode |
|--------------|-------------------|--------------------------|-------------|
| Pioneer multiplier voting | No quorum (6-week cycle) | None | Tessera-weighted average of votes cast per Pioneer pool |
| Bubble multiplier voting | No quorum (6-week cycle) | None | Tessera-weighted average of votes cast per new pool (first 90 days) |
| Gauge approval | No quorum | 100 svZCHF/sUSDS equivalent | Simple majority of votes cast |
| Gauge challenge | No quorum | 1,000 svZCHF/sUSDS equivalent | Simple majority to revoke; gauge removed if passed |
| Fee parameter changes | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail if quorum not met |
| Treasury spends >10% of balance | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail → 14-day timelock + public review |
| Fee distribution split changes (after Year 4) | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail → 14-day timelock + public review |
| Protocol upgrades | 20% of total qualified voting power | 1,000 svZCHF/sUSDS equivalent | Auto-fail → 14-day timelock + public review |

All governance deposits are paid in **AuMM and burned automatically**. The deposit amount is denominated in **svZCHF or sUSDS equivalent, whichever is higher at the time of submission** — preventing gaming via currency fluctuation. Gauge proposals: 100 equivalent. All other proposals and challenges: 1,000 equivalent. Non-refundable. Every governance action creates deflationary pressure on AuMM.

Uncontested proposals with very low turnout do not pass silently. They either auto-fail or route to a timelock with a mandatory public review period. This prevents a small coordinated group from pushing through structural changes while the broader LP community is inactive.

**Anti-Market Buying:** Only active liquidity providers in **emission-qualified pools** possess governance voting power. AuMT held in pools that do not meet eligibility criteria carries zero voting weight. You cannot buy governance power on the open market, and you cannot earn it by parking capital in unproductive pools. You must be providing liquidity to pools that meet every anti-gaming criterion.

Fourth root (Era 1) then cube root (Era 2) dampens whale dominance — maximum compression when the protocol is smallest and most vulnerable, relaxing as TVL growth naturally decentralizes power. Time-weighting rewards commitment without requiring lock mechanisms.

**What governance controls:**
- Pioneer pool multipliers via 6-weekly tessera-weighted voting (constrained to [0.90–1.10] per pool)
- Bubble multipliers via 6-weekly tessera-weighted voting for new pools in their first 90 days (constrained to [0.90–2.00])
- Gauge approval (AuMT vote to grant a pool emission eligibility — requires 100 svZCHF/sUSDS equivalent in AuMM, burned). **Available from month 11 onward only.**
- Gauge revocation (AuMT vote to remove a gauge via challenge — requires 1,000 svZCHF/sUSDS equivalent in AuMM, burned)
- Fee parameters (swap fee %, yield fee %)
- Treasury allocation (within defined bounds)
- Protocol upgrades (with timelock)

**What governance cannot control:** See **Permanent Protocol Rules** section for the full list of immutable parameters. In short: emission schedule, maximum supply, CCB engine parameters (60-day EMA, Pioneer multiplier range, Bubble multiplier range, Incendiary Boost mechanics, Sandbox fast-track threshold), governance dampening transition, eligibility criteria, Pioneer pool tags, fee distribution split (first 4 years), and all launch mechanics (months 0–13) are immutable in contract.

---


## Pool Creation and Gauge Approval

**Pool creation is permissionless from block 0.** Anyone can deploy any pool with any token composition at any time. The Aequilibrium factory is open. This never changes.

### Gauge Approval

A pool only becomes eligible for AuMM emissions after qualified LPs approve a gauge through governance. This is the single gatekeeping step. Without it, an attacker deploys a pool and immediately starts extracting emissions. With it, existing LPs must collectively decide that the new pool deserves a share of the emission budget.

**The eligibility criteria are immutable.** Once a gauge is approved, the pool must still meet every anti-gaming criterion to receive emissions. Governance cannot waive, modify, or relax these rules. A gauge vote says "this pool may compete for emissions." The contract decides whether it actually qualifies.

This separates the three concerns cleanly: permissionless creation (anyone can build, from day one), democratic gauge approval (LPs decide what competes), immutable rules (the contract enforces discipline, always).

### Governance Proposals

Any AuMT holder can submit a governance proposal — fee parameter changes, treasury spending, protocol upgrades. Proposals require burning **1,000 svZCHF or sUSDS equivalent (whichever is higher) worth of AuMM**. The AuMM is burned automatically on submission — non-refundable regardless of outcome.

**Gauge proposals** (requesting emission eligibility for a new pool) require burning **100 svZCHF or sUSDS equivalent (whichever is higher) worth of AuMM** — lower than other governance proposals because gauge requests are lower-stakes. If the pool fails the immutable criteria, the contract kills it automatically. The governance vote is a lightweight check on whether the pool deserves to compete, not a major protocol decision.

Every governance action creates deflationary pressure on AuMM. The deposit filters spam (proposers must hold and sacrifice AuMM), funds no one (tokens are destroyed, not transferred), and tightens supply. Self-regulating.

### Gauge Challenges

Any AuMT holder can challenge an existing gauge if the pool is perceived as gaming or extractive. Challenges require burning **1,000 svZCHF or sUSDS equivalent (whichever is higher) worth of AuMM**. A challenge triggers a governance vote: if the challenge succeeds (majority votes to revoke), the gauge is removed and the pool loses emission eligibility. If the challenge fails, the AuMM is still burned — the challenger accepted that risk.

This creates a community enforcement layer on top of the immutable anti-gaming criteria. The contract catches pools that fail the volume percentile floor or the efficiency caps automatically. Gauge challenges catch pools that technically pass the criteria but are extractive in ways the contract can't detect — coordinated wash trading, circular routing schemes, or pools that exist solely to farm emissions for a single actor.


---


## Anti-Gaming Criteria

Pools must meet ALL criteria to remain eligible for AuMM emissions:

| Criterion | Requirement | Rationale |
|-----------|-------------|-----------|
| Protocol version | Aequilibrium only | No legacy pool farming |
| ERC-4626 composition ("4626 Quality Gate") | **≥52%** yield-bearing tokens by weight. Each ERC-4626 token must have **≥$5M, 30 BTC, or 4,000,000 svZCHF (whichever is largest) in its underlying vault** (`totalAssets()`) to count toward the 52% threshold. | Ensures pools generate real protocol yield fees. Three independent currency-denominated floors (USD, BTC, CHF) prevent any single inflation or devaluation event from eroding the quality gate. |
| Minimum TVL | $10K **7-day SMA** (exempt during months 0–3 grace period) | Filters ghost pools. The 7-day SMA prevents flickering eligibility from intra-day price fluctuations — a pool at $10,001 that dips to $9,999 from a price move doesn't lose eligibility until the 7-day average drops below $10K. |
| Volume percentile floor | Graduated by pool age (see Graduated Grace Period below) | Benchmarks pool activity against protocol-wide distribution |
| Efficiency-based emission caps | Gauged pools ranked by efficiency ratio; bottom 15% capped (see Emission Efficiency Tournament below). **Activates at month 13 (after CCB transition).** | Throttles inefficient pools without reflexive disqualification. Price-agnostic. |
| No self-referential tokens | AuMM cannot be a pool component | Prevents circular farming |

### Why TVL-Based Governance Eliminates the Wrapper Problem

In token-weighted governance (Balancer/Aura), bear markets enable cheap governance capture through lock multipliers and meta-governance amplifiers. AuMM carries zero governance power. AuMT governance weight equals the USD value of the LP position in qualified pools. To get 5% of governance power, you need 5% of protocol TVL in real capital. No lock multiplier. No boost. No amplifier. Bear market doesn't help the attacker — governance weight is TVL-denominated, not token-price-denominated.

**Wrappers and composability layers are welcome.** Convex/Aura-style vaults that hold AuMT carry full governance weight proportional to the underlying TVL. They cannot amplify governance because there's nothing to amplify. The TVL-based governance model IS the anti-capture mechanism.

Pools containing AuMT follow all the same rules as any other pool — permissionless creation, gauge approval via AuMT vote, full anti-gaming criteria.

### Graduated Grace Period

New pools need time to get discovered by aggregators, indexed by bots, and build organic volume. A static kill switch applied too early makes the protocol's "permissionless pool creation" pitch hollow in practice. The graduated grace period introduces discipline incrementally, preserving the discovery layer while filtering out pools that never find traction.

| Pool Age | Volume Percentile Floor | Efficiency Caps | Notes |
|----------|------------------------|-----------------|-------|
| Months 0–3 | None | Exempt | Full experimentation window. Pool must still meet structural criteria (ERC-4626 composition, no self-referential tokens). |
| Months 3–6 | 5th percentile | Exempt | First signal required: pool must demonstrate it's not completely dead. |
| Months 6–12 | 10th percentile | Exempt | Higher bar, still in discovery phase. Treasury stabilization active. |
| Month 13+ | 15th percentile | **Active** | Full discipline. Both volume percentile floor and efficiency-based emission caps apply. Aligned with treasury exit. |

Percentile rankings are calculated against the protocol's own pool activity distribution — specifically, the trailing 4-week rolling window of fee + yield revenue across all emission-eligible pools. This is a relative measure: as the protocol grows, the absolute bar rises organically.

**Gaming the grace period.** The exploit vector for the grace period is the gauge, not the pool. An attacker deploys a pool, gets a gauge approved via governance vote, votes emissions to it, and milks the grace window before the fee/percentile checks activate. Switching deployer wallets or swapping one token to argue "different composition" doesn't help the attacker because the percentile floor is protocol-wide — a pool that generates no organic activity sits at the bottom of the distribution regardless of who deployed it or how many times it's been redeployed. The graduated percentile ramp is the natural defence: a pool earning zero fees can't stay above the 5th percentile for long, even with generous AuMM emission allocation.

### Hysteresis Buffer (Anti-Oscillation)

Binary thresholds with no dead zone create oscillation — a pool at the 14th percentile bounces between eligible and disqualified every governance cycle based on noise. The hysteresis buffer prevents random volatility from killing viable pools.

| Zone | Volume Percentile | Status | Action |
|------|------------------|--------|--------|
| **Safe** | Above 15th | Fully eligible | Normal emissions, no flags |
| **Warning** | 10th–15th | Flagged | Emissions continue normally. Pool must recover above the 15th percentile within 2 governance cycles (4 weeks). |
| **Cut** | Below 10th | Disqualified | Emissions cease immediately. Unallocated emissions route to buyback-and-burn. |

**Critical design choice:** Emissions continue during the warning period. Cutting emissions from a pool in the warning zone reduces its attractiveness exactly when it needs to attract more volume — that's a death sentence disguised as a second chance. The 2-cycle recovery window gives the pool a genuine opportunity to recover while creating a hard deadline.

Re-qualification after disqualification requires the pool to sustain activity above the 15th percentile for one full rolling window (4 weeks) with no emissions. If it can generate organic activity without emission subsidies, it earned its way back.

### Emission Efficiency Tournament

The efficiency tournament is a relative ranking system that is entirely price-agnostic — designed to throttle inefficient pools without penalising productive pools during AuMM price appreciation.

**The mechanic.** All gauged pools **above $10K TVL** are ranked by their efficiency ratio — `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received` — using a **2-epoch (4-week) moving average** to prevent single-day glitches. Pools below $10K TVL are excluded from the ranking entirely and receive zero emissions regardless of gauge votes. Higher ratio = more efficient (more revenue per unit of emission). The least efficient gauged pools — those at the bottom of the ranking — receive hard emission caps regardless of how many governance votes they receive:

| Efficiency Rank (gauged pools above $10K TVL) | Emission Cap | Effect |
|--------------------------------------|-------------|--------|
| Above 15th percentile | No cap | Full emissions as voted |
| 10th–15th percentile (bottom 15–10%) | 1% of total protocol emissions | Capped even if votes say more |
| 5th–10th percentile (bottom 10–5%) | 0.5% of total protocol emissions | Harder cap |
| Below 5th percentile (bottom 5%) | 0.1% of total protocol emissions | Nearly starved |

The efficiency tournament activates at **month 13** of a pool's life (same as the volume percentile floor reaching full discipline).

**Excess emissions are redistributed.** When a pool is capped below its voted emission weight, the excess is redistributed to uncapped pools pro-rata by their existing voted emission weight. This rewards productive pools rather than burning the excess.

The efficiency tournament is price-agnostic by design — it prevents the reflexive disqualification problem where a rising AuMM price would cause fixed revenue hurdles to fail productive pools.

**Self-correcting.** A pool gets capped → receives fewer emissions → its efficiency ratio improves next cycle → it climbs out. No death spiral.

**Governance-capture resistant.** A group of voters colludes to send 50% of emissions to a pool with zero fees. The protocol sees the pool's efficiency ratio is the worst in the set. It's ranked in the bottom 5%. Despite having 50% of the votes, it receives 0.1% of emissions. The other 49.9% is redistributed to productive pools.

**Sacrificial lamb resistant.** An attacker tries to flood the bottom 15% with junk pools to shield their extractive pool from capping. Each lamb pool needs $10K TVL to enter the ranking, a gauge approval vote (burning 100 svZCHF/sUSDS equivalent in AuMM), and LP governance approval. Twenty lamb pools = $200K+ in capital at risk plus 2,000 equivalent in AuMM burned. The $10K TVL floor makes the attack prohibitively expensive.

### Disqualification and Gauge Revocation

Pools that fail the anti-gaming criteria face a two-stage process:

**Stage 1: Disqualification.** A pool that falls below the 10th volume percentile (or fails other structural criteria) is disqualified — emissions cease immediately. The gauge remains intact. If the pool recovers above the 15th percentile for one full rolling window (4 weeks) with no emissions, it re-qualifies automatically.

**Stage 2: Gauge revocation.** A pool that remains disqualified for **4 consecutive governance cycles (8 weeks)** has its gauge permanently revoked. To restart emissions, the pool operator must submit a new gauge proposal (burn 100 svZCHF/sUSDS equivalent in AuMM) and win a fresh AuMT governance vote. This prevents dead pools from holding gauge slots indefinitely.

### How the Criteria Interact

After month 13, a gauged pool must clear the volume floor (or be disqualified) AND survive the efficiency ranking (or be capped). Volume floor catches dead pools. Efficiency caps catch extractive pools. Neither alone is sufficient. Both are self-correcting — no governance vote required.

---


## AMM Architecture: Aequilibrium

### Provenance: Balancer V3

Aequilibrium is derived from Balancer V3's open-source, Certora-verified smart contracts. The relationship is transparent: the pool layer is byte-identical to the audited code, the tokenomics layer is entirely new. The table below shows what was inherited and what was built.

| Component | Origin | Modifications |
|-----------|--------|--------------|
| Vault | Balancer V3 (Certora verified) | None |
| Weighted pools | Balancer V3 (Certora verified) | None |
| Stable pools | Balancer V3 (Certora verified) | None |
| Hooks (StableSurge etc.) | Balancer V3 (Certora verified) | None |
| ERC-4626 rate providers | Balancer V3 (Certora verified) | None |
| Smart Order Router | Balancer V3 | None |
| Gauge system | **Rewritten** | New emission logic, eligibility criteria, anti-gaming, unqualified-vote-to-burn |
| Token contract | **New** | BTC-style emission schedule, immutable supply cap |
| Fee distributor | **New** | 50/25/25 swap fee split + yield fee split + buyback-and-burn |
| Governance | **New** | LP-weighted voting (AuMT for all decisions — emission direction and protocol governance), no ve-locking |

### What's Unchanged (Critical)

The pool contracts, vault, SOR, hooks, and rate providers are **byte-identical** to the Certora-verified Balancer V3 code. The audit and formal verification apply to these components. Only the tokenomics layer is new and requires independent audit.

This is important for LP trust: *"The AMM you're depositing into is the same formally verified code. The token you're earning is different."*

### What's New (Requires Audit)

- AuMM token contract (ERC-20 with immutable supply cap and halving logic)
- AuMT pool token wrapper (Aureum Market Tessera)
- CCB emission engine (60-day EMA calculator, Pioneer multiplier voting with tessera-weighted averaging, zero-sum normalization)
- Incendiary Boost engine (AuMM escrow, 30-day emission streaming, efficiency scalar calculation, priority skim, renewal lock)
- Bubble multiplier voting (90-day window, tessera-weighted averaging, expiry logic)
- Sandbox fast-track (top 10% efficiency detection, automatic gauge approval)
- Emission distributor (per-block streaming with halving logic, CCB-driven weight updates)
- Gauge eligibility checker (on-chain criteria enforcement, graduated grace period, volume percentile ranking, hysteresis buffer, efficiency tournament with 2-epoch smoothing, gauge revocation logic)
- Pioneer pool tag registry (25 pre-defined pools, non-transferable, revocation on gauge loss, locked treasury deposits)
- Token supply tracker (cumulative emitted, cumulative burned, net circulating, burn rate)
- Minimum qualification period enforcer (14-day continuous hold check)
- Quorum calculator and timelock router
- Unqualified-vote-to-burn router
- Fee splitter (swap fees: 50/25/25 + yield fees: 25/75)
- Governance voting (AuMT for all decisions — emission direction and protocol governance — with phased fourth root→cube root dampening)

Estimated audit scope: ~4,500 lines of new Solidity (including CCB emission engine with 60-day EMA, Pioneer and Bubble multiplier voting, Incendiary Boost escrow and efficiency scalar, Sandbox fast-track, efficiency tournament logic, AuMM-burn governance hooks, price ceiling mechanism, Pioneer pool tag system, and token supply tracking). The bulk of the protocol inherits Balancer V3's existing Certora audit coverage.

---


---

## Proof of Real Yield Dashboard

The aumm.fi frontend displays per-pool yield transparency that reframes how LPs evaluate returns:

**Per pool, the dashboard shows:**
- **Real yield %** — the portion of returns from swap fees + ERC-4626 vault yield (non-inflationary sources)
- **Emission yield %** — the portion from AuMM emissions (inflationary)
- **Efficiency score** — the pool's efficiency ratio vs. protocol average
- **Revenue per $1 of emissions** — how much protocol revenue each dollar of emission generates

**The framing:**

*"This pool earns 68% of returns from real yield, not inflation."*

Most AMMs report a single blended APR that mixes real revenue with token emissions. LPs see "80% APR" without knowing that 75% of it is inflation that dilutes the token they're earning. Aureum separates the two, making the quality of returns visible.

This is a competitive weapon. When an Aerodrome LP compares "80% APR" against Aureum's "12% real yield + 15% emission yield," the conversation shifts from "which number is bigger" to "which return is sustainable." Lower headline APR, higher quality return. The dashboard makes that argument visually without saying a word about competitors.

---

## Permanent Protocol Rules

The following parameters are immutable in the smart contracts. No governance vote, no multisig, no admin key can modify them. They are the protocol's constitution.

**Emission schedule.** 21M maximum supply. BTC-style halving every ~4 years. Per-block streaming. Immutable from block 0.

**Governance dampening transition.** Fourth root (Era 1, pre-halving) → cube root (Era 2, post-halving). Triggered at halving block. No governance vote. All positions recalculate.

**Any withdrawal = governance reset.** Full details in Governance section.

**Eligibility criteria.** ERC-4626 composition ≥52% with $5M/30 BTC/4M svZCHF vault TVL floor per token. Volume percentile floors. Efficiency-based emission caps. Grace period schedule. Gauge revocation after 4 consecutive failed cycles. None of this can be changed.

**Pioneer pool tags.** All 28 pre-defined at launch, locked from block 0. No open slots. Governance-steerable multiplier [0.90–1.10]. Non-transferable. Revoked on gauge loss. No replacements ever.

**Continuous Central Bank (CCB).** Emission allocation driven by 60-day EMA of on-chain TVL. Zero-sum normalization against fixed emission schedule. Pioneer multiplier range [0.90–1.10] in discrete steps. Bubble multiplier range [0.90–2.00] for first 90 days post-gauge-approval. Multiplier votes every 6 weeks. Tessera-weighted average determines final multipliers. All parameters immutable. (Oracle-free design detailed in the CCB section.)

**Incendiary Boost.** 30-day supplementary emission funded by operator AuMM escrow. Emission rate pegged to 85th percentile efficiency × (2 - pool's efficiency rank). Priority claim on block rewards. Renewal only after pool enters 85th percentile in Efficiency Tournament. All parameters immutable.

**Sandbox fast-track.** Non-gauged pools reaching top 10% efficiency organically earn automatic gauge approval. No governance vote. Immutable threshold.

**Fee distribution split.** Immutable for first 4 years. Governance-adjustable only after first halving.

**Governance proposal deposits.** All paid in AuMM, burned automatically. Denominated in svZCHF or sUSDS equivalent (whichever is higher). 100 equivalent for gauge proposals, 1,000 for all other governance. Non-refundable. This is immutable.

---


## Founding Team

| Role | Contributor | Brings |
|------|------------|--------|
| Architecture & Thesis | **Sagix** | Pool design, routing topology, aggregator relationships, cross-protocol integrations (Frankencoin, Reserve), published research |
| Smart Contracts | **TBD** | Solidity expertise, governance vault infrastructure, Balancer V3 codebase familiarity |
| Frontend & UX | **TBD** | Frontend experience, emission dashboard, LP interface |
| Founding Liquidity | **TBD** (aligned capital partner) | Seed capital for genesis pools, long-term LP commitment |

**The founding team earns tokens by being early LPs.** Same mechanism as everyone else. The only advantage is being first — deploying pools, providing initial liquidity, and earning the highest emission rate before anyone else arrives. As more LPs join, per-LP emissions decline. Early believers rewarded. No allocation. No vesting.

---


---


## Treasury

### Source

Protocol fee revenue flows to the treasury as defined in the **Value Capture** section (25% of swap fees + 75% of ERC-4626 yield fees). These are **stablecoin revenues** — the treasury's operating budget.

**The treasury never sells AuMM to fund operations.** AuMM received during the treasury emission phase (months 0–10) is used exclusively for protocol-owned liquidity: seeding the AuMM trading pool at month 6 and operating the price ceiling stabilization mechanism (months 6–10). Stabilization sale proceeds are deposited as permanently locked liquidity in Pioneer pools — not converted to stablecoins for team spending. All leftover AuMM is burned at month 10. After month 10, the treasury never receives AuMM again. Development, audits, and operations are funded entirely from stablecoin fee revenue. This is the "no team allocation" guarantee: the team cannot extract value through AuMM sales.

### Use

| Category | Allocation | Notes |
|----------|-----------|-------|
| Audits & Security | 40% | Ongoing audit coverage, bug bounties, formal verification |
| Development | 30% | Smart contract maintenance, frontend, integrations |
| Operations | 20% | Infrastructure, RPC, subgraph, monitoring |
| Reserve | 10% | Emergency fund |

### Governance

Treasury spending requires governance vote (AuMT-weighted, qualified pool LPs only). No single party controls treasury. Multi-sig with founding team members initially, transitioning to LP-elected council after Year 1.

---


## Competitive Position

### LP Advantage Over Uniswap

| Feature | Uniswap V3 Pair | Aureum Pool |
|---------|----------------|-------------|
| Trading pairs per position | 1 | 10+ (per multi-token pool) |
| Yield on idle capital | 0% | 2.0–2.8% (ERC-4626 native) |
| IL profile | Full directional exposure to one pair | Dampened — correlated assets diversify directional risk |
| Fee tier | 0.05–0.3% | 0.01–0.05% (attracts routing) |
| Active management required | Yes (range adjustments) | No (weighted pools are set-and-forget) |
| Yield sources | Swap fees only | Swap fees + vault yield + cross-pool arb fees + AuMM mining |

### Protocol Comparison

| Feature | Balancer V3 | Uniswap V4 | Curve | Aerodrome | **Aureum** |
|---------|-------------|-----------|-------|-----------|-----------|
| Multi-asset pools | ✅ | ❌ | ❌ | ❌ | ✅ |
| ERC-4626 native | ✅ | ❌ | ❌ | ❌ | ✅ |
| Hooks | ✅ | ✅ | ❌ | ❌ | ✅ |
| Formal verification | ✅ | ❌ | ❌ | ❌ | ✅ (inherited) |
| Fair launch | ❌ | ❌ | ❌ | ❌ | ✅ |
| BTC tokenomics | ❌ | ❌ | ❌ | ❌ | ✅ |
| No team allocation | ❌ | ❌ | ❌ | ❌ | ✅ |
| Anti-gaming criteria | ❌ | N/A | ❌ | ❌ | ✅ |
| LP = miner | ❌ | ❌ | ❌ | Partial | ✅ |
| LP = governor | ❌ | ❌ | ❌ | ❌ | ✅ |
| Emissions to governance staking | ✅ (80/20) | N/A | ✅ (veCRV) | ❌ | ❌ (banned) |
| Unqualified votes → burn | ❌ | N/A | ❌ | ❌ | ✅ |
| Constellation routing network | ❌ | ❌ | ❌ | ❌ | ✅ (ixEDEL hub by network effect) |
| Buyback-and-burn from day 1 | ❌ | ❌ | ❌ | ❌ | ✅ |

### The Prop AMM Contrast

The table above compares Aureum to other public AMMs. But the most instructive contrast is with proprietary AMMs — the "dark AMMs" that now dominate Solana routing, processing tens of billions in monthly volume with zero public TVL.

Prop AMMs proved the thesis that winning aggregator routing is the entire game. A single team supplies all liquidity from proprietary capital, runs active market-making algorithms with off-chain pricing oracles, and captures volume purely by being the cheapest fill when an aggregator routes a trade. No frontend, no brand, no retail awareness needed. Just better execution.

The model works. And it is architecturally the opposite of Aureum on every dimension:

| Dimension | Proprietary AMM | Aureum |
|-----------|----------------|--------|
| Liquidity source | Team-supplied, closed | Public, permissionless LP |
| Pricing logic | Private algorithms, off-chain oracles | On-chain weighted pool math, formally verified |
| Transparency | Opaque — users cannot assess fairness or execution quality | Fully transparent — pool weights, fees, and rules are on-chain |
| Governance | None — one team controls all parameters | AuMT-weighted — LPs govern emission direction and protocol decisions |
| Token distribution | Insider-heavy — typically 90%+ to foundation, team, ecosystem with vesting | Zero pre-mine — declining treasury share (75%→50%→0% over months 0–10) for protocol-owned pool seeding, 100% to LPs after month 10 |
| Failure mode | Single team goes down, 35%+ of chain volume disappears | Permissionless — no single point of failure, pools exist independently |
| Chain dependency | Requires sub-second block times for active quoting — Solana-native | Passive LP model designed for Ethereum's 12-second blocks |
| LP participation | None — users cannot provide liquidity or earn fees | Core design — LP is the only way to earn tokens and governance power |

Prop AMMs solved the routing problem through centralisation. Aureum solves the same problem through architecture — multi-asset pools with native yield, constellation routing, and aggregator-competitive fees — without concentrating control in a single team. The question is whether decentralised infrastructure can match the execution quality of a proprietary trading desk. The ERC-4626 yield floor, the multi-pair capital efficiency, and the cross-pool arbitrage engine are the mechanisms that make it possible.

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

### End of Month 10: First Pioneer Multiplier Vote

Qualified LPs cast the first tessera-weighted vote on Pioneer multipliers [0.90–1.10] for all 25 pools. This is the first governance action on emission allocation.

### Month 11: Gauge Proposals Open

- Non-Pioneer pools can submit gauge proposals (burn 100 svZCHF/sUSDS equivalent in AuMM)
- All pools (Pioneer and non-Pioneer) begin ranking in the Efficiency Tournament
- Sandbox fast-track active: non-gauged pools reaching top 10% efficiency earn automatic gauge approval

### Months 11–12: CCB Transition

Emissions transition linearly from equal-weight to full CCB/EMA allocation:

```
Day D weight = (1 - T) × equal_share + T × CCB_EMA_share
T = (D - month_11_start) / (month_13_start - month_11_start)
```

At the start of month 11, T = 0 (100% equal weight). At the start of month 13, T = 1 (100% CCB/EMA × multipliers). The transition is smooth — no discontinuity, no cliff.

Bubble voting (multiplier [0.90–2.00]) activates for newly gauged pools during this period.

### Month 13 Day 1: Full Protocol Activation

- CCB/EMA fully active for all pools (Pioneer and non-Pioneer)
- Efficiency Tournament fully active — bottom 15% capped, excess redistributed
- Volume percentile floor at full discipline (15th percentile)
- New gauged pools receive emissions alongside the 25 Pioneers
- Incendiary Boost available for all gauged pools
- The protocol is now fully autonomous

The subsections above constitute the binding launch specification. All dates, parameters, and mechanisms are immutable from block 0.

---

## Risk Factors

**Fork risk.** Aequilibrium inherits Balancer V3's smart contract security via byte-identical pool contracts, but the new tokenomics contracts require independent audit. Until audited, the new code carries unverified risk.

**Liquidity risk.** Genesis pools will have minimal TVL. Bootstrapping requires the founding team's capital and early LP adoption. If depth doesn't reach aggregator thresholds, the routing thesis never activates.

**Regulatory risk.** Fair-launch tokens with no pre-mine have the strongest regulatory position (no securities argument), but the regulatory landscape is uncertain.

**Balancer response.** Balancer could modify their revamp to preserve emissions, making the fork less necessary. Or they could challenge the fork through non-legal means (community pressure, aggregator lobbying).

**Team risk.** Founding team is small and self-funded. Key-person dependency is high in early phases.

**Market risk.** Launching during a bear market or period of DeFi apathy could delay adoption regardless of architectural merit.

---


## The Miliarium Aureum: Pioneer Pools

All 25 Pioneer pools are pre-defined at launch and locked from block 0. No open slots. No governance vote to add or replace Pioneers. The 25 pools below constitute the complete founding infrastructure.

### The Dual-Anchor System: svZCHF + ixEDEL

Every Pioneer pool contains both **svZCHF** (yield anchor — ERC-4626, Frankencoin savings rate ~3.75%, counts toward the 4626 Quality Gate) and **ixEDEL** (routing anchor — ERC-20, Reserve Protocol DTF, IL reduction via diversified basket, internal cross-pool arbitrage routing, strategic moat). Together they create a unified routing hub where all 25 pools are interconnected through shared anchor tokens.

### Standardised Pool Template

All Pioneer pools follow a consistent weight structure:

| Component | Weight | Role |
|-----------|--------|------|
| Yield Core (2 ERC-4626 tokens) | 52% (26% + 26%) | Meets 4626 Quality Gate. Generates protocol yield fees from block one. |
| Routing Anchor (ixEDEL) | 16% | Cross-pool arbitrage. Constellation routing connectivity. |
| Theme Assets (2 tokens) | 32% (16% + 16%) | Sector exposure. Drives aggregator volume from external markets. |

### I. The Founding Infrastructure (Slots 01–05)

Core routing gates for crypto-native benchmarks.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 01 | **ixHelvetia** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% waEthUSDT / 16% USDC |
| 02 | **ixStrata** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% LINK / 16% AAVE |
| 03 | **ixForum** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% SKY / 16% LDO |
| 04 | **ixAppia** | 26% svZCHF / 26% sfrxUSD | 16% ixEDEL | 16% PAXG / 16% XAUt |
| 05 | **ixAugusta** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% WBTC / 16% cbBTC |

### II. The Reserve & Ecosystem Empire (Slots 06–09)

Consolidating the Sagix/Reserve stack, yield-bearing primitives, and ecosystem tokens.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 06 | **ixRegistrum** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% ETHPLUS / 16% OPEN |
| 07 | **ixBeneficium** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% ENA / 16% sUSDe |
| 08 | **ixEcosysthema** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% FRAX / 16% CHEX |
| 09 | **ixImperium** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% PENDLE / 16% EIGEN |

### III. ETH Staking Governance & DeFi Infra (Slots 10–11)

Capturing the ETH staking governance layer and DeFi lending infrastructure.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 10 | **ixCasper** | 27% waEthrETH / 27% waEthweETH | 15% ixEDEL | 15% RPL / 16% ETHFI |
| 11 | **ixAuxilium** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% Morpho / 16% SPK |

**ixCasper** — ETH staking governance pool. Non-standard composition: waEthrETH and waEthweETH are Aave V3 stataToken ERC-4626 wrappers for Rocket Pool's rETH and EtherFi's weETH respectively. ERC-4626 composition: 54% (both yield core tokens). RPL (Rocket Pool governance) and ETHFI (EtherFi governance) provide exposure to the staking protocol upside alongside the underlying staking yield.

### IV. The Equity & Index Empire (Slots 12–17)

TradFi indices, tokenised equity wrappers, and fintech.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 12 | **ixAureum** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% SPYon / 16% IVVon |
| 13 | **ixVictoria** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% QQQon / 16% QQQX |
| 14 | **ixGigantus** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% NVDAon / 16% TSLAon |
| 15 | **ixMajestas** | 26% svZCHF / 26% sfrxUSD | 16% ixEDEL | 16% MSFTon / 16% AAPLon |
| 16 | **ixMoneta** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% JPMon / 16% GSon |
| 17 | **ixMercatura** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% COIN / 16% HOOD |

### V. Macro, Hard Assets & Global FX (Slots 18–22)

Treasuries, energy, LSTs, and global fiat corridors.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 18 | **ixSalus** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% LLYon / 16% NVOon |
| 19 | **ixVectura** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% SGOVon / 16% TLTon |
| 20 | **ixCustodia** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% GLDon / 16% TIPon |
| 21 | **ixManes** | 26% fWSTETH / 26% fWETH | 16% ixEDEL | 16% svZCHF / 16% waEthwstETH |
| 22 | **ixViatica** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% fBRZ / 16% st-EURA |

### VI. Core Connector Pools (Slots 23–25)

Anchor and infrastructure pools with non-standard compositions. These pools serve specialised routing and price discovery roles that require weight distributions outside the standard 52%/16%/32% template.

| Slot | Pool Name | Composition | Role |
|:-----|:----------|:-----------|:-----|
| 23 | **ixEdelweiss** | ixEDEL (46%), waEthUSDC (18%), waEthUSDT (18%), svZCHF (18%) | Primary ixEDEL price discovery venue. ixEDEL-heavy weighting concentrates liquidity for the routing anchor. |
| 24 | **ixLibertas** | scrvUSD (15%), PYUSD (15%), GHO (14%), sUSDS (14%), sfrxUSD (14%), USDT (14%), USDC (14%) | USD stablecoin hub. Seven-token pool spanning major USD stables and savings vaults. No ixEDEL — functions as a standalone deep-liquidity USD venue. |
| 25 | **ixCambio** | ixEDEL (20%), svZCHF (16%), st-EURA (16%), aEURS (16%), s-tGBP (16%), [Partner Stable] (16%) | FX hub. Multi-currency pool (CHF, EUR, GBP, USD) with yield-bearing stablecoins via Aave/Morpho vaults. Competes directly with Curve's FXSwap (launched ZCHF/crvUSD at Stable Summit Cannes, March 2026) but captures multiple FX pairs from one LP position. |

### Cross-Pool Arbitrage

With 25 pools sharing svZCHF and ixEDEL as common anchors, six arbitrage layers generate fees continuously: vault-rate arbitrage (ERC-4626 drift correction), CHF/USD forex arbitrage, multi-currency FX arbitrage, wrapped-asset arbitrage (gold-to-gold, BTC-to-BTC), cross-pool price arbitrage (25 pools × 2 shared anchors = dense routing graph), and external-internal arbitrage (constituent tokens trading $898M+ daily on Uniswap at higher fees).

### Pioneer Benefits

**1. Governance-steerable emission multiplier.** Pioneer pools are the only pools eligible for the CCB governance multiplier [0.90–1.10] (see **The Continuous Central Bank** section).

**2. Treasury liquidity deposits.** Revenue from treasury AuMM sales during the price ceiling stabilization is deposited as permanent locked liquidity into Pioneer pools meeting the 4626 Quality Gate and $10K+ TVL. The treasury can never withdraw.

**Tag revocation:** If a Pioneer pool loses its gauge or emission eligibility, the tag is permanently revoked. No replacement. The number of active Pioneer slots only decreases.

