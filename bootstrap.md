# Bootstrap Rules

*How new pools earn their way into the emission economy.*

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

**Pioneer PMAR and Bubble multipliers stack.** A pool that earns a Pioneer tag at gauge approval receives both multipliers during its first 90 days: the PMAR multiplier [0.75–1.25] and the Bubble multiplier [0.90–2.00]. After day 91, the Bubble expires and only the PMAR multiplier remains. The founding Miliarium Aureum pools receive both multipliers from launch — they are simultaneously the first Pioneers and the first Bubble-eligible pools.

**The final Bubble multiplier is the tessera-weighted average of all votes cast for that pool.** This allows LPs to express strategic conviction: a 2.0× vote on a new Swiss Franc/Bitcoin pool signals strong ecosystem alignment. A 0.9× vote on a suspected wash-trading pool acts as a social consensus firewall.

**The hand-off.** At day 91, the Bubble expires. By this point, a successful pool has 90 days of TVL data baked into its EMA. The mechanical CCB weight "takes the baton" from the governance boost seamlessly. Failed pools lose both the Bubble and the EMA weight — they die naturally.

**Bubble votes occur every 6 weeks.** Only qualified AuMT holders can vote.

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
- They have no governance voice (no PMAR eligibility, no Bubble voting)

**The fast-track rule.** If a non-gauged Sandbox pool reaches the **top 10% efficiency** in the Efficiency Tournament organically — without any emission boost — it earns **automatic gauge approval**. No governance vote required. The protocol recognises proven productivity and removes the governance bottleneck.

This gives the protocol experimentation without emission risk. Builders can deploy, prove efficiency organically, and earn their way into full emission eligibility. The fast-track replaces politics with performance.

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

### Pioneer Composition Challenge

Pioneer pools may also be challenged for token-composition renewal using the same 1,000 svZCHF-equivalent AuMM burn. This allows the protocol to adapt to changing market conditions while keeping the 25 Pioneer slots permanently allocated to the Miliarium Aureum routing core.

**Composition constraints.** The proposed new composition must preserve the pool's function and sector theme. A composition challenge swaps like-for-like: a tokenised equity for another tokenised equity, an ERC-4626 vault that ceased to exist for another qualifying vault. The pool's template structure (52%/16%/32% or its non-standard equivalent), sector classification, and role within the routing constellation must remain intact. The new composition must pass the ERC-4626 Quality Gate (≥52%) and all other eligibility criteria.

**Dynamic cost formula.** The base deposit for a Pioneer Composition Challenge is **100,000 svZCHF, 1 BTC, or 100,000 sUSDS equivalent (whichever is greatest) worth of AuMM**, scaled by two factors:

```
Pioneer_Challenge_Cost = Base × (1 + TVL_share_i) × (1 - Rank_percentile_i)
```

Where:
- `Base` = 100,000 svZCHF, 1 BTC, or 100,000 sUSDS equivalent — whichever is greatest at the time of submission
- `TVL_share_i` = pool's TVL as a percentage of total Pioneer constellation TVL (e.g. 0.08 if the pool holds 8% of Pioneer TVL)
- `Rank_percentile_i` = pool's efficiency rank percentile within the protocol (0 = worst performer, 1 = best performer)

| Pool State | TVL Share | Efficiency Rank | Cost Multiplier | Effective Cost |
|:-----------|:----------|:----------------|:----------------|:---------------|
| Dead pool (token delisted) | ~0% | 0th percentile | 1.00 × 1.00 = 1.00 | ~100,000 svZCHF equiv |
| Underperforming pool | 2% | 15th percentile | 1.02 × 0.85 = 0.87 | ~87,000 svZCHF equiv |
| Average pool | 4% | 50th percentile | 1.04 × 0.50 = 0.52 | ~52,000 svZCHF equiv |
| High-performing pool | 8% | 90th percentile | 1.08 × 0.10 = 0.11 | ~11,000 svZCHF equiv |
| Top performer | 12% | 99th percentile | 1.12 × 0.01 = 0.01 | ~1,000 svZCHF equiv |

The formula makes dead pools (where tokens have genuinely ceased to exist) cost the full base rate, while well-performing pools are nearly free to challenge — but governance would reject frivolous challenges anyway. Three independent currency-denominated floors (svZCHF, BTC, sUSDS) prevent any single devaluation event from cheapening the challenge cost.

The AuMM is burned on submission, non-refundable. A governance vote (simple majority of qualified AuMT holders) decides whether the new composition is approved. If approved, the pool's tokens are migrated to the new composition. If rejected, the AuMM is still burned.
