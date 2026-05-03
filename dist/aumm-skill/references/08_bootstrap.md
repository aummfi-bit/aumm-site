<!-- GENERATED FROM aumm-site@d7744a8bf6f825dd5e3b14a8b69cbeab462ce824 08_bootstrap.md — DO NOT EDIT -->
# Bootstrap Rules

*How new pools enter the emission economy.*

---

## xxi. Cold-Start Design

### Pool Creation and Gauge Approval

**Pool creation is permissionless from block 0.** Anyone can deploy any pool with any composition at any time. The Aequilibrium factory is open. This never changes.

A pool becomes eligible for AuMM emissions only after qualified LPs approve a gauge through governance. **Without gauge approval: no emissions, no Incendiary Boost, no 90-day gauge boost.** Existing LPs must collectively decide the new pool deserves a share of the emission budget.

**Eligibility criteria are immutable.** Once a gauge is approved, the pool must still meet every anti-gaming criterion. Governance cannot waive, modify, or relax these rules. A gauge vote says "this pool may compete." The contract decides whether it qualifies.

Three concerns, cleanly separated: permissionless creation (anyone can build), democratic gauge approval (LPs decide what competes), immutable rules (the contract enforces discipline).

Core emission allocation remains automatic and immutable.

### Sandbox and Fast-Track

**Sandbox** is the permissionless default. Any pool deployed without a gauge operates in Sandbox from block 0. Zero CCB emissions, no Incendiary Boost eligibility — but ranked in the Efficiency Tournament alongside gauged pools. Anyone can build and demonstrate performance before seeking gauge approval.

**Fast-Track Rule.** A non-gauged Sandbox pool sustaining **top 10% efficiency** for **3 consecutive epochs (6 weeks)** earns **automatic gauge approval** — no governance vote, deposit waived. Pools that prove capital efficiency earn emissions without campaigning for votes. After fast-track approval: standard 90-day gauge boost (1.2× CCB multiplier) and Incendiary Boost eligibility.

### The Bootstrapping Sequence

| Phase | Days | Driver | Purpose |
|-------|------|--------|---------|
| Gauge approval | Day 0 | AuMT governance vote | Quality gate — pool must pass governance before any boost |
| Incendiary Boost | Any time | svZCHF/sUSDS deposit into der Bodensee | Proof of conviction — anyone can deepen the autonomous reserve to boost a pool |
| 90-day gauge boost | Days 1–90 | Fixed 1.2x CCB multiplier (automatic) | Cold-start emission ramp — expires without vote or renewal |
| CCB takeover | Day 91+ | 60-day EMA | Institutional stability — the pool is now permanent infrastructure |

All layers require gauge approval first. At day 91, the fixed boost expires. A successful pool has 90 days of TVL data baked into its EMA by then — the CCB takes over seamlessly. Failed pools lose the boost and the EMA weight. They die naturally.

### Two boosts, different purposes

Two distinct boosts, different purposes, mechanically independent:

**90-day gauge boost (automatic).** Every newly approved gauge receives a fixed **1.2× CCB multiplier** for 90 days. Activates when the gauge passes, expires on its own — no vote, no renewal. The baseline cold-start ramp every approved pool gets for free.

**Incendiary Boost (user-funded, stacks on top).** Anyone can deposit **any amount** of **svZCHF/sUSDS** into der Bodensee Pool (one-sided inflow) to activate a **1-epoch (14-day)** supplementary emission stream for a gauged pool, starting the next epoch. Both boosts can run simultaneously. The gauge boost adjusts the multiplier inside the CCB score; Incendiary is a separate priority skim from the block emission (see §xxii below).

## xxii. Incendiary Boost

Proof-of-conviction bootstrap. Anyone deposits **any amount** of svZCHF/sUSDS **one-sided into der Bodensee Pool**. In return, the target pool receives a supplementary AuMM emission stream for **1 epoch (14 days)**, starting at the **next epoch boundary**. The deposit amount is entirely at the paying user's discretion — conviction capital sacrificed to deepen the autonomous reserve.

### Rules

- **Any gauged pool** can be boosted.
- **Anyone** can pay for a boost — not limited to pool operators.
- **Once per epoch per pool.** A pool can be boosted as many times as people want, but only once per epoch. A new boost for the same pool cannot start until the current boost epoch ends.
- **Deposit amount:** user's choice. The full amount goes one-sided into der Bodensee Pool — no LP tokens minted, non-refundable.

### Priority Skim

Total emissions are fixed (BTC-style hard cap), so Incendiary Boosts are priority claims on the **LP emission tranche** — **after** the der Bodensee bootstrap skim in Months 1–10 (piecewise decay: 80%→50% by Month 6, 50%→0% by Month 10; see [Protocol formulas (F-0)](11_formulas.md); zero thereafter). The protocol calculates total AuMM required for all active boosts, subtracts from the LP tranche, distributes the remainder via equal split or CCB. Every active Incendiary Boost directly reduces emissions to all other pools. The depositor's svZCHF/sUSDS deepens der Bodensee in exchange for skipping the EMA queue.

### Immutable Parameters

All parameters immutable from block 0: 1-epoch (14-day) duration, priority skim, svZCHF/sUSDS deposit to der Bodensee.

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

All eligibility criteria are immutable from block 0. No governance vote can waive, modify, or relax them. CCB multiplier applies automatically to the 28 Miliarium pools ([Theoretical foundations (§vii)](03_theoretical_foundation.md); [Protocol formulas (F-8)](11_formulas.md); bounds in [Constitution (§xxix)](10_constitution.md)). No voting over emission allocation. New gauges: **90-day 1.2× CCB multiplier** — expires automatically, no vote, no renewal.

### Why TVL-Based Governance Eliminates the Wrapper Problem

In token-weighted governance (Balancer/Aura), bear markets enable cheap capture through lock multipliers and meta-governance amplifiers. AuMM carries zero governance power. AuMT governance weight equals the USD value of the LP position in qualified pools. 5% of governance power requires 5% of protocol TVL in real capital. No lock multiplier. No boost. No amplifier. Bear markets don't help the attacker — governance is TVL-denominated, not token-price-denominated.

**Wrappers and composability layers are welcome.** Convex/Aura-style vaults holding AuMT carry full governance weight proportional to underlying TVL. They cannot amplify governance because there is nothing to amplify.

Pools containing AuMT follow all the same rules — permissionless creation, gauge approval via AuMT vote, full anti-gaming criteria.

### Graduated Grace Period

New pools need time to get discovered by aggregators, indexed by bots, and build organic volume. The grace period introduces discipline incrementally — preserving the discovery layer while filtering pools that never find traction.

| Pool Age | Volume Percentile Floor | Efficiency Caps | Notes |
|----------|------------------------|-----------------|-------|
| Months 0–3 | None | Exempt | Full experimentation window. Pool must still meet structural criteria (ERC-4626 composition, no self-referential tokens). |
| Months 3–6 | 5th percentile | Exempt | First signal required: pool must demonstrate it's not completely dead. |
| Months 6–12 | 10th percentile | Exempt | Higher bar, still in discovery phase. |
| Month 13+ | 15th percentile | **Active** | Full discipline. Both volume percentile floor and efficiency-based emission caps apply. |

Percentile rankings use the protocol's own activity distribution — trailing 3-epoch (6-week) rolling window of fee + yield revenue across all emission-eligible pools. Relative measure: as the protocol grows, the absolute bar rises organically.

**Gaming the grace period.** The exploit vector is the gauge, not the pool. An attacker deploys a pool, gets a gauge approved, milks the grace window before percentile checks activate. Switching deployer wallets or swapping one token doesn't help — the percentile floor is protocol-wide. A pool generating no organic activity sits at the bottom regardless of who deployed it or how many times it's been redeployed. A pool earning zero fees can't stay above the 5th percentile for long, even with generous emission allocation.

### Hysteresis Buffer (Anti-Oscillation)

Binary thresholds with no dead zone create oscillation — a pool at the 14th percentile bounces between eligible and disqualified every cycle on noise. The hysteresis buffer prevents that.

| Zone | Volume Percentile | Status | Action |
|------|------------------|--------|--------|
| **Safe** | Above 15th | Fully eligible | Normal emissions, no flags |
| **Warning** | 10th–15th | Flagged | Emissions continue normally. Pool must recover above the 15th percentile within 3 epochs (6 weeks). |
| **Cut** | Below 10th | Disqualified | Emissions cease immediately. Unallocated emissions are redistributed to remaining eligible pools. |

Emissions continue during the warning period. Cutting emissions from a struggling pool reduces its attractiveness exactly when it needs volume — a death sentence disguised as a second chance. The 3-epoch window gives genuine recovery time with a hard deadline.

Re-qualification requires sustaining above the 15th percentile for 3 epochs (6 weeks) with no emissions. Generate organic activity without subsidies, earn your way back.

### Emission Efficiency Tournament

A relative ranking system, entirely price-agnostic — throttles inefficient pools without penalising productive pools during AuMM price appreciation.

All gauged pools **above $10K TVL** ranked by efficiency ratio — `(swap_fees + ERC-4626_yield_revenue_to_DAO) / emissions_received` — using a **3-epoch (6-week) moving average**. Below $10K TVL: excluded from ranking, zero emissions regardless of gauge status. Higher ratio = more efficient. The least efficient gauged pools receive hard caps regardless of CCB-derived share:

| Efficiency Rank (gauged pools above $10K TVL) | Emission Cap | Effect |
|-----------------------------------------------|-------------|--------|
| Above 15th percentile | No cap | Full CCB emissions |
| 10th–15th percentile (bottom 15–10%) | 1% of total protocol emissions | Capped even if CCB share is higher |
| 5th–10th percentile (bottom 10–5%) | 0.5% of total protocol emissions | Harder cap |
| Below 5th percentile (bottom 5%) | 0.1% of total protocol emissions | Nearly starved |

Activates at **month 13** of a pool's life (same as the volume floor reaching full discipline).

**Excess emissions are redistributed.** When a pool is capped below its CCB-derived share, the excess goes to uncapped pools pro-rata by CCB share.

Price-agnostic by design — prevents the reflexive disqualification problem where a rising AuMM price causes fixed revenue hurdles to fail productive pools.

**Self-correcting.** A pool gets capped → receives fewer emissions → its efficiency ratio improves next cycle → it climbs out. No death spiral.

**Governance-capture resistant.** A pool with large TVL and large CCB share but minimal fees ranks at the bottom. Despite a high CCB share, it receives at most 0.1% of emissions. Excess redistributed to productive pools.

**Sacrificial lamb resistant.** Flooding the bottom 15% with junk pools to shield an extractive pool: each lamb needs $10K TVL, a gauge approval vote (100 svZCHF/sUSDS into der Bodensee), and LP approval. Twenty lambs = $200K+ capital at risk plus 2,000 svZCHF/sUSDS deposited. Prohibitively expensive.

### Disqualification and Gauge Revocation

Two-stage process:

**Stage 1: Disqualification.** Below the 10th volume percentile (or failing structural criteria) — emissions cease immediately. Gauge remains intact. Recover above the 15th percentile for 3 epochs (6 weeks) with no emissions to re-qualify automatically.

**Stage 2: Gauge revocation.** Disqualified for **4 consecutive epochs (8 weeks)** — gauge permanently revoked. Restart requires a new gauge proposal (100 svZCHF/sUSDS into der Bodensee) and a fresh AuMT vote. Dead pools don't hold gauge slots indefinitely.

### How the Criteria Interact

After month 13, a gauged pool must clear the volume floor (or be disqualified) AND survive the efficiency ranking (or be capped). Volume floor catches dead pools. Efficiency caps catch extractive pools. Neither alone suffices. Both self-correct — no governance vote required.

## xxiv. Governance Gating (Non-Emission)

### Governance Proposals

Any qualified AuMT holder can submit a governance proposal (fee parameter changes). Deposit: **1,000 svZCHF or sUSDS (whichever is higher)**, one-sided into der Bodensee Pool. Automatic on submission, non-refundable.

**Swap-fee changes (within immutable bands):** `FEE_CHANGE_COOLDOWN_BLOCKS = BLOCKS_PER_EPOCH = 100,800` — no pool's swap fee can be changed more often than once per epoch. **Class-dependent bands:** Miliarium Aureum pools and non-Miliarium gauged pools use **0.01%–0.30%** (Miliarium genesis **0.03%**); der Bodensee uses **0.10%–1.00%** (genesis **0.75%**). **Non-Miliarium gauge approval** includes the **initial swap fee** as a gauge parameter (within the 0.01–0.30% band), so a separate fee-change proposal is not required when the pool is created.

**All** governance deposits — gauge proposal, gauge challenge, fee proposal, composition challenge — are **one-sided into der Bodensee Pool**. Same mechanic throughout. Filters spam, deepens the autonomous reserve, non-recoverable.

### Gauge Proposal

Any qualified AuMT holder may submit a gauge proposal for a new pool. Deposit: **100 svZCHF or sUSDS (whichever is higher), one-sided into der Bodensee Pool** — lower than other proposals because gauge requests are lower-stakes. If the pool fails immutable criteria, the contract kills it automatically.

If approved, the pool becomes emission-eligible subject to immutable criteria checks.

### Gauge Challenge

Any qualified AuMT holder can challenge an existing **non-Miliarium** gauge. **The 28 Miliarium Aureum pools cannot be gauge-challenged** — structural changes to those slots go exclusively through the **Composition Challenge** path below.

Challenge deposit is the **greater** of **10 BTC** (CHF equivalent) and **1,000,000 CHF** × **√((1 − p_tvl)(1 − p_eff))**, with **p_tvl** and **p_eff** defined as **rank/N** elite-tail fractions per [F-12](11_formulas.md). The **entire** amount is converted to **svZCHF or sUSDS (whichever is higher)** and deposited **one-sided into der Bodensee Pool** — not to the challenged pool, not to a treasury wallet.

Challenge triggers a governance vote: majority votes to revoke → gauge removed, emissions lost. **The deposit goes to der Bodensee Pool regardless of outcome** — non-refundable whether the challenge succeeds or fails. The challenger accepted that risk.

Community enforcement layer on top of immutable anti-gaming criteria. The contract catches pools failing volume or efficiency thresholds automatically. Gauge challenges catch pools that technically pass but are extractive in ways the contract can't detect — coordinated wash trading, circular routing, or single-actor emission farming.

### Miliarium Aureum Composition Challenge

Pool token composition is immutable on-chain — no mechanism to swap a token inside a deployed contract. A composition challenge follows a **deprecate-and-replace** path. **Deposit:** **1,000 svZCHF or sUSDS (whichever is higher), one-sided into der Bodensee Pool** — same routing as fee proposals ([Constitution §xxvii](10_constitution.md)).

1. **Governance vote** — a qualified AuMT holder submits a composition challenge proposal that references the **address of an already-deployed candidate pool** (specified-pool model). It passes only with **2/3 protocol-wide tessera-weighted approval**.
2. **Deprecation** — the old pool's gauge is revoked; emissions cease; the old pool persists on-chain with the fee-routing hook still attached.
3. **Slot update** — the Miliarium Registry points the slot to the approved replacement pool; the replacement is **automatically gauge-eligible** with the **90-day gauge boost** (no separate gauge proposal). Optional Incendiary Boost applies as normal.

A single proposal may cover **both** theme assets simultaneously if both have failed — forum discussion builds consensus on the pair before the on-chain vote.

Composition intent is binding: replacement must be the same asset type or economically similar. **Like-for-like** = same sector, same risk profile, same template role (yield core vs routing anchor vs theme asset). Renewal path, not redesign.

#### What qualifies as "economically similar"

Assets cease to exist — tokens get delisted, wrappers lose support, issuers shut down. The goal is to maintain the Miliarium Aureum as a functioning economy, not to pick winners.

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

Not a stock-picking exercise. Composition challenges activate when an asset **ceases to function**; the replacement preserves the pool's role in the constellation.

### Worked example: Composition Challenge (cbBTC → tBTC scenario)

**Setup:** ixAurebit (slot 14) holds WBTC 16% + cbBTC 16% as its two BTC-wrapper theme assets. Hypothetically, Coinbase announces the sunsetting of cbBTC — the wrapper will cease minting within 90 days, and redemption will be available for a further 180 days before full delisting.

**Flow:**

1. **Candidate pool deployment (permissionless, any block).** Any party can deploy a replacement pool via the standard Balancer V3 `WeightedPoolFactory`. Example composition: svZCHF 26% + GHO 26% + ixEDEL 16% + WBTC 16% + tBTC 16% — identical yield-core and routing components, with tBTC (Threshold Network's decentralized BTC wrapper) substituting for cbBTC as the Theme Asset B leg. This is a deployed pool with a real address and a Quality Gate check.
2. **Composition Challenge proposal.** Any qualified AuMT holder submits a proposal referencing the candidate pool's address. Deposit: 1,000 svZCHF/sUSDS equivalent, one-sided into der Bodensee.
3. **Vote.** 2/3 supermajority of protocol-wide tessera-weighted votes. Like-for-like evaluation by voters: same sector (Crypto / BTC), same risk profile (BTC wrapper with different custodian — Threshold Network multi-party computation vs Coinbase custody), same template role (Theme Asset B).
4. **Approval actions (atomic in the approval transaction).** The governance contract calls `MiliariumRegistry.replaceSlot(14, newPoolAddress)`. The old ixAurebit pool's gauge is revoked; the new pool is automatically gauge-approved with a 90-day CCB multiplier boost (1.2×).
5. **Post-approval state.**
   - Old ixAurebit pool: persists on-chain, no AuMM emissions, fee-routing hook still attached (residual trading: **protocol share** to Bodensee, **LP residual** to LPs), LPs can hold or withdraw at will, AuMT for the old pool drops to **zero governance weight**.
   - New ixAurebit pool: active gauge, receives AuMM emissions per CCB, 90-day 1.2× boost, new LP positions earn AuMM emissions and governance weight (subject to 14-day qualification + 6-month on-ramp).
   - Market behavior: LPs of the old pool withdraw naturally as cbBTC's redemption window narrows. The new pool attracts liquidity because it's the only emission-eligible BTC pool in slot 14.

**What this example illustrates:**
- No forced LP migration mechanism is needed — the market handles it for free.
- The fee-routing hook stays attached to the deprecated pool for life, so Bodensee continues to receive the **protocol share** of swap fees while LPs retain the **LP residual**.
- Slot 14's identity persists across the composition change; the registry maps slot → current pool address, not slot → immutable pool address.

#### The 28 are a blueprint, not the full economy

The 28 Miliarium pools are a curated blueprint for CCB execution — diversified foundation ensuring structural fee generation across asset classes from day one. **Not** meant to exhaust every token or market.

If a token, stablecoin, or asset class is missing from the 28, the path is **not** a composition challenge. It is:

1. **Deploy a new pool** — permissionless from block 0
2. **Get a gauge approved** — submit a proposal, deposit svZCHF/sUSDS into der Bodensee Pool, win the AuMT vote
3. **Earn emissions** — through the standard CCB rules, Incendiary Boost, and 90-day gauge boost

New pools route through the constellation's connectors (ixEdelweiss, ixLibertas, ixCambio), generate yield from ERC-4626 vaults, and bootstrap via Incendiary and gauge boost mechanics — the same infrastructure the 28 founding pools use. The Miliarium pools are the anchor, not the ceiling.

### On-Chain-Only Proposal Rule

Every proposal must reference only verifiable on-chain data (addresses, block ranges, and contract-derived metrics). Proposals based on off-chain-only claims are invalid.

## xxv. Immutable Reference

See [Immutable Parameters (§xxix)](10_constitution.md).
