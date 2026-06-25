<!-- GENERATED FROM aumm-site@dd5fd5f210483395ca105ac7449c0a2202ed2a7f 08_bootstrap.md — DO NOT EDIT -->
# Bootstrap Rules

*How new pools enter the emission economy.*

---

## xxi. Cold-Start Design

### Pool Creation and Permissionless Gauge Activation

**Pool creation is permissionless from block 0.** Anyone can deploy any pool with any composition at any time. The Aequilibrium factory is open. This never changes.

A pool becomes eligible for AuMM emissions only after its gauge is **activated**. Activation is **permissionless** — any address can call **`activateGauge(pool)`** once the pool meets all immutable eligibility criteria (Quality Gate ≥52%, sustained TVL floor, pool-type whitelist, forbidden-token block clear) and the **anti-spam fee** is paid. **Without an active gauge: no emissions, no Incendiary Boost.** The contract enforces qualification — no governance vote admits a gauge.

**Eligibility criteria are immutable.** Activation cannot occur unless every immutable criterion is satisfied at the activation block, and the **Anti-Gaming Engine** (§xxiii) continues enforcing them every epoch thereafter. Governance cannot waive, modify, or relax these rules. The contract is the gate; no governance signal substitutes for criteria compliance.

Three concerns, cleanly separated: permissionless creation (anyone can build), permissionless gauge activation (any address can activate once criteria are met), immutable rules (the contract enforces discipline).

Core emission allocation remains automatic and immutable.

### Sandbox

**Sandbox** is the permissionless default. Any pool deployed without an active gauge operates in Sandbox from block 0. Zero CCB emissions, no Incendiary Boost eligibility — but ranked in the Efficiency Tournament alongside gauged pools. Anyone can build and demonstrate performance before activating a gauge.

### The Bootstrapping Sequence

| Phase | Days | Driver | Purpose |
|-------|------|--------|---------|
| Gauge activation | Once criteria met | Permissionless `activateGauge(pool)` + anti-spam fee | Quality gate — pool must pass criteria; no governance vote |
| Incendiary Boost | Any time | svZCHF/sUSDS deposit into der Bodensee | Proof of conviction — anyone can deepen the autonomous reserve to boost a pool |
| CCB allocation | Once active — ongoing | 60-day EMA | Emissions tracked by smoothed TVL via the standard CCB |

All other layers require an active gauge first. A successful pool builds TVL into its EMA over its first epochs, and the CCB takes over seamlessly. Failed pools lose the EMA weight and die naturally.

### Incendiary Boost (overview)

**Incendiary Boost (user-funded).** Anyone can deposit **any amount** of **svZCHF/sUSDS** into der Bodensee Pool (one-sided inflow) to activate a **1-epoch (14-day)** supplementary emission stream for a gauged pool, starting the next epoch. Incendiary is a priority skim from the block emission (see §xxii below) — not a CCB multiplier.

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

All eligibility criteria are immutable from block 0. No governance vote can waive, modify, or relax them. CCB multiplier applies automatically to the 28 Miliarium pools ([Theoretical foundations (§vii)](03_theoretical_foundation.md); [Protocol formulas (F-8)](11_formulas.md); bounds in [Constitution (§xxix)](10_constitution.md)). No voting over emission allocation.

### Why TVL-Based Governance Eliminates the Wrapper Problem

In token-weighted governance (Balancer/Aura), bear markets enable cheap capture through lock multipliers and meta-governance amplifiers. AuMM carries zero governance power. AuMT governance weight equals the USD value of the LP position in qualified pools. 5% of governance power requires 5% of protocol TVL in real capital. No lock multiplier. No boost. No amplifier. Bear markets don't help the attacker — governance is TVL-denominated, not token-price-denominated.

**Wrappers and composability layers are welcome.** Convex/Aura-style vaults holding AuMT carry full governance weight proportional to underlying TVL. They cannot amplify governance because there is nothing to amplify.

Pools containing AuMT follow all the same rules — permissionless creation, permissionless gauge activation, full anti-gaming criteria.

### Graduated Grace Period

New pools need time to get discovered by aggregators, indexed by bots, and build organic volume. The grace period introduces discipline incrementally — preserving the discovery layer while filtering pools that never find traction.

| Pool Age | Volume Percentile Floor | Efficiency Caps | Notes |
|----------|------------------------|-----------------|-------|
| Months 0–3 | None | Exempt | Full experimentation window. Pool must still meet structural criteria (ERC-4626 composition, no self-referential tokens). |
| Months 3–6 | 5th percentile | Exempt | First signal required: pool must demonstrate it's not completely dead. |
| Months 6–12 | 10th percentile | Exempt | Higher bar, still in discovery phase. |
| Month 13+ | 15th percentile | **Active** | Full discipline. Both volume percentile floor and efficiency-based emission caps apply. |

Percentile rankings use the protocol's own activity distribution — trailing 3-epoch (6-week) rolling window of fee + yield revenue across all emission-eligible pools. Relative measure: as the protocol grows, the absolute bar rises organically.

**Gaming the grace period.** The exploit vector is the gauge, not the pool. An attacker deploys a pool, activates its gauge, milks the grace window before percentile checks turn on. Switching deployer wallets or swapping one token doesn't help — the percentile floor is protocol-wide. A pool generating no organic activity sits at the bottom regardless of who deployed it or how many times it's been redeployed. A pool earning zero fees can't stay above the 5th percentile for long, even with generous emission allocation.

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

**Sacrificial lamb resistant.** Flooding the bottom 15% with junk pools to shield an extractive pool: each lamb needs $10K TVL, eligibility-criteria-passing composition, and the **anti-spam fee** (100 svZCHF or 125 sUSDS into der Bodensee) to activate. Twenty lambs = $200K+ capital at risk plus 2,000 svZCHF or 2,500 sUSDS in fees. Prohibitively expensive.

### Disqualification and Gauge Revocation

Two-stage process:

**Stage 1: Disqualification.** Below the 10th volume percentile (or failing structural criteria) — emissions cease immediately. Gauge remains intact. Recover above the 15th percentile for 3 epochs (6 weeks) with no emissions to re-qualify automatically.

**Stage 2: Gauge revocation.** Disqualified for **4 consecutive epochs (8 weeks)** — gauge permanently revoked. Restart requires a fresh **permissionless gauge activation** (100 svZCHF or 125 sUSDS anti-spam fee into der Bodensee) once eligibility criteria are restored. Dead pools don't hold gauge slots indefinitely.

### How the Criteria Interact

After month 13, a gauged pool must clear the volume floor (or be disqualified) AND survive the efficiency ranking (or be capped). Volume floor catches dead pools. Efficiency caps catch extractive pools. Neither alone suffices. Both self-correct — no governance vote required.

## xxiv. Governance Gating (Non-Emission)

### Governance Proposals

Any qualified AuMT holder can submit a governance proposal (fee parameter changes). Deposit: **1,000 svZCHF or 1,250 sUSDS**, one-sided into der Bodensee Pool. Automatic on submission, non-refundable.

**Swap-fee changes (within immutable bands):** `FEE_CHANGE_COOLDOWN_BLOCKS = BLOCKS_PER_EPOCH = 100,800` — no pool's swap fee can be changed more often than once per epoch. **Class-dependent bands:** Miliarium Aureum pools and non-Miliarium gauged pools use **0.01%–0.30%** (Miliarium genesis **0.03%**); der Bodensee uses **0.10%–1.00%** (genesis **0.75%**). For non-Miliarium pools, the **initial swap fee** is set as a parameter at **first successful gauge activation** (within the 0.01–0.30% band), so a separate fee-change proposal is not required when the pool is created.

**All** governance deposits — gauge challenge, fee proposal, composition challenge — and the **anti-spam fee** for permissionless gauge activation are **one-sided into der Bodensee Pool**. Same mechanic throughout. Filters spam, deepens the autonomous reserve, non-recoverable.

### Permissionless Gauge Activation

Gauge activation is **permissionless**. Once a pool meets all immutable eligibility criteria — **ERC-4626 Quality Gate ≥52%** by class-admitted weight, sustained **TVL floor**, **pool-type whitelist**, and **forbidden-token block** clear — any address can call **`activateGauge(pool)`**. No vote, no quorum, no governance gating.

**Anti-spam fee:** **100 svZCHF or 125 sUSDS**, one-sided into der Bodensee Pool via the shared swap-and-deposit rail. **Non-refundable** on success and on any failed criteria check. Filters spam-activation attempts on freshly-deployed pools that have not yet sustained criteria. Same routing as governance deposits, distinct classification: rate-limiter, not vote bond.

**No multiplier boost at activation.** The pool enters tournament accounting at base CCB multiplier `M_i = 1.0` and competes for emission share through the Efficiency Tournament (§xxiii) from the next epoch boundary. Cold-start support comes from Incendiary Boost (user-funded, optional) — see §xxii.

### Gauge Challenge

Any qualified AuMT holder can challenge an existing **non-Miliarium** gauge. **The 28 Miliarium Aureum pools cannot be gauge-challenged** — structural changes to those slots go exclusively through the **Composition Challenge** path below.

Challenge deposit is the **greater** of **10 BTC** (CHF equivalent) and **1,000,000 CHF** × **√((1 − p_tvl)(1 − p_eff))**, with **p_tvl** and **p_eff** defined as **rank/N** elite-tail fractions per [F-12](11_formulas.md). The **entire** amount is converted to **svZCHF, or 1.25× the svZCHF amount in sUSDS**, and deposited **one-sided into der Bodensee Pool** — not to the challenged pool, not to a treasury wallet.

Challenge triggers a governance vote: majority votes to revoke → gauge removed, emissions lost. **The deposit goes to der Bodensee Pool regardless of outcome** — non-refundable whether the challenge succeeds or fails. The challenger accepted that risk.

Community enforcement layer on top of immutable anti-gaming criteria. The contract catches pools failing volume or efficiency thresholds automatically. Gauge challenges catch pools that technically pass but are extractive in ways the contract can't detect — coordinated wash trading, circular routing, or single-actor emission farming.

### Miliarium Aureum Composition Challenge

Pool token composition is immutable on-chain — no mechanism to swap a token inside a deployed contract. A composition challenge follows a **deprecate-and-replace** path. **Deposit:** **1,000 svZCHF or 1,250 sUSDS, one-sided into der Bodensee Pool** — same routing as fee proposals ([Constitution §xxvii](10_constitution.md)).

1. **Governance vote** — a qualified AuMT holder submits a composition challenge proposal that references the **address of an already-deployed candidate pool** (specified-pool model). It passes only with **2/3 protocol-wide tessera-weighted approval**.
2. **Deprecation** — the old pool's gauge is revoked; emissions cease; the old pool persists on-chain with the fee-routing hook still attached.
3. **Slot update** — the Miliarium Registry points the slot to the approved replacement pool; the replacement gauge is **auto-registered** via `registerGaugeFromComposition(pool)` (governance-only entry point) — no separate permissionless activation, no anti-spam fee. Optional Incendiary Boost applies as normal.

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
2. **Composition Challenge proposal.** Any qualified AuMT holder submits a proposal referencing the candidate pool's address. Deposit: 1,000 svZCHF or 1,250 sUSDS, one-sided into der Bodensee.
3. **Vote.** 2/3 supermajority of protocol-wide tessera-weighted votes. Like-for-like evaluation by voters: same sector (Crypto / BTC), same risk profile (BTC wrapper with different custodian — Threshold Network multi-party computation vs Coinbase custody), same template role (Theme Asset B).
4. **Approval actions (atomic in the approval transaction).** The governance contract calls `MiliariumRegistry.replaceSlot(14, newPoolAddress)`. The old ixAurebit pool's gauge is revoked; the new pool's gauge is auto-registered via `registerGaugeFromComposition`.
5. **Post-approval state.**
   - Old ixAurebit pool: persists on-chain, no AuMM emissions, fee-routing hook still attached (residual trading: **protocol share** to Bodensee, **LP residual** to LPs), LPs can hold or withdraw at will, AuMT for the old pool drops to **zero governance weight**.
   - New ixAurebit pool: active gauge, receives AuMM emissions per CCB; new LP positions earn AuMM emissions and governance weight (subject to 14-day qualification + 6-month on-ramp).
   - Market behavior: LPs of the old pool withdraw naturally as cbBTC's redemption window narrows. The new pool attracts liquidity because it's the only emission-eligible BTC pool in slot 14.

**What this example illustrates:**
- No forced LP migration mechanism is needed — the market handles it for free.
- The fee-routing hook stays attached to the deprecated pool for life, so Bodensee continues to receive the **protocol share** of swap fees while LPs retain the **LP residual**.
- Slot 14's identity persists across the composition change; the registry maps slot → current pool address, not slot → immutable pool address.

#### The 28 are a blueprint, not the full economy

The 28 Miliarium pools are a curated blueprint for CCB execution — diversified foundation ensuring structural fee generation across asset classes from day one. **Not** meant to exhaust every token or market.

If a token, stablecoin, or asset class is missing from the 28, the path is **not** a composition challenge. It is:

1. **Deploy a new pool** — permissionless from block 0
2. **Activate the gauge** — once eligibility criteria are met (Quality Gate ≥52%, sustained TVL floor, pool-type whitelist, forbidden-token block clear), any address can call `activateGauge(pool)` with the **anti-spam fee** (100 svZCHF or 125 sUSDS into der Bodensee). No vote, no proposal.
3. **Earn emissions** — through the standard CCB rules and Incendiary Boost. There is no multiplier boost at activation; cold-start support comes from user-funded Incendiary Boost.

New pools route through the constellation's connectors (ixEdelweiss, ixLibertas, ixCambio), generate yield from ERC-4626 vaults, and bootstrap via Incendiary Boost — the 28 founding pools were seeded at genesis. The Miliarium pools are the anchor, not the ceiling.

### On-Chain-Only Proposal Rule

Every proposal must reference only verifiable on-chain data (addresses, block ranges, and contract-derived metrics). Proposals based on off-chain-only claims are invalid.

## xxiv-a. Vault-Class Registry

The protocol's discretion surface narrows to **one question**: which ERC-4626 token classes count toward the **52% Quality Gate numerator** ([Tokenomics §ix](04_tokenomics.md)). Pool deployment, gauge activation (§xxiv), and pool composition are all permissionless; class admission is the single decision governance retains. Admissions issue through a **Frankencoin-inspired proposal-and-veto pattern** — vigilant minorities can block bad admissions, while legitimate admissions auto-finalize without active vote pressure.

A pool may include any tokens. Weight in any 4626 token whose class is **not** admitted contributes **0** to the 52% numerator and falls into the ≤48% complement.

### Class Admission Mechanism (Proposal → Veto Window → Auto-Finalize)

- **Proposal.** Any address calls `proposeVaultClass(admissionType, admissionValue, constraintsHash)` paying a **non-refundable bond** in svZCHF. The bond routes one-sided into der Bodensee Pool via the same swap-and-deposit rail used for the anti-spam fee and governance proposal deposits — no burn, no treasury accumulation.
- **Veto window.** Bounded block range during which qualified AuMT holders may invoke `vetoProposal(id)`. The proposal is rejected if cumulative AuMT-weighted veto support meets the **veto threshold**.
- **Auto-finalize.** Window expires without a successful veto → proposal **auto-executes in a single transaction**; the class enters the registry. No two-stage `finalize`-then-`execute` — single-tx state transition on window expiry, minimizing stuck-state surface.
- **Revocation.** Governance may invoke `revokeVaultClass(id)` to denounce a previously-admitted class. Revocation is **revocable-with-grandfather**: it blocks **new** numerator credit at the next epoch boundary; **existing** gauges are not force-revoked but face the standard graduated grace period from §xxiii if they fall below 52% as a result.

Bond, veto threshold, and veto window are tunables locked in [Constitution §xxix](10_constitution.md) under non-regressable bounds: **`proposalBond ≥ antiSpamFee`** (class admission must not undercut the simpler permissionless-activation fee); **`vetoThreshold ≤ governanceQuorumThreshold`** (a vigilant minority must reach the veto bar at lower weight than full proposal quorum); **veto window ∈ `[BLOCKS_PER_EPOCH, 3 × BLOCKS_PER_EPOCH]`** (long enough for governance reaction, short enough to avoid stalling legitimate admissions).

### Admission Fingerprints (Three Types, Proposer-Stated)

A `VaultClassProposal` declares its `admissionType` from one of three fingerprint kinds. Each carries a different threat model; the proposer selects which fits the class being admitted, and the veto mechanism is the protocol's check on that judgement.

- **`ImplementationAddress`** — admits a specific implementation behind a proxy. Future implementations behind the same proxy automatically inherit admission. Trust delegated to the proxy admin's upgrade discipline.
- **`FactoryAddress`** — admits all current and future vaults from a specific factory. Trust delegated to the factory's deployment policy.
- **`BytecodeHash`** — admits exact bytecode match. Future-proof against unannounced implementation rotation; conversely, blocks legitimate upgrades without a fresh proposal.

Glossary definitions in [Glossary §xxxii](12_aureum_glossary.md).

### Genesis Seeding (Constructor-Hardcoded)

The Miliarium-pool ERC-4626 vault classes — waEthUSDC, ixEDEL, sUSDS-class wrappers, and the remainder per per-pool profiles in [miliarium_profiles/](miliarium_profiles/) — are admitted at deploy via **constructor-hardcoded constants** in `VaultClassRegistry.sol`. No one-shot seeding admin entrypoint.

The genesis class set is **bytecode-immutable**. Future classes enter via the `proposeVaultClass` + veto flow once on-chain governance is live. Pre-governance, the registry is frozen at its constructor-seeded set; pools using only genesis-admitted 4626 classes can be gauged permissionlessly through `activateGauge` (§xxiv).

## xxv. Immutable Reference

See [Immutable Parameters (§xxix)](10_constitution.md).
