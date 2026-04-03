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

## xxiii. Eligibility and Competition

- Pools compete under immutable eligibility criteria and efficiency ranking.
- MAMAR applies automatically as defined in `MAMAR.md`.
- No Bubble voting and no voting over emission allocation.

## xxiv. Governance Gating (Non-Emission)

### Gauge Proposal

- Any qualified AuMT holder may submit a gauge proposal.
- Submission deposit: **100 svZCHF/sUSDS equivalent in AuMM (burned)**.
- If approved by vote, the pool becomes emission-eligible subject to immutable criteria checks.

### Gauge Challenge

- Any qualified AuMT holder may challenge an active gauge.
- Challenge deposit: **1,000 svZCHF/sUSDS equivalent in AuMM (burned)**.
- If challenge vote passes, gauge is revoked.

### General Governance Proposal

- Any qualified AuMT holder may submit treasury/fee proposals.
- Submission deposit: **1,000 svZCHF/sUSDS equivalent in AuMM (burned)**.

### Miliarium Aureum Composition Challenge

- Any qualified AuMT holder may submit a composition challenge proposal.
- Proposal passes only with **2/3 protocol-wide tessera-weighted approval**.
- Composition intent is binding: replacement token must be same asset type or economically similar.
- This mechanism is for like-for-like renewal only; pool function and economic role must remain intact.

### On-Chain-Only Proposal Rule

Every proposal must reference only verifiable on-chain data (addresses, block ranges, and contract-derived metrics). Proposals based on off-chain-only claims are invalid.

## xxv. Immutable Reference

See Immutable Parameters in `constitution.md`.
