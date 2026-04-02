# Bootstrap Rules

*How new pools enter the emission economy with governance gating and automatic emissions.*

---

## XXI — Cold-Start Design

The protocol keeps permissionless pool creation while limiting governance to non-emission actions.

- Any builder can deploy pools from block 0.
- Core emission allocation remains automatic and immutable.

## XXII — Incendiary Boost

Incendiary Boost remains a proof-of-conviction mechanism:

- operator escrows AuMM
- supplementary emissions stream for 30 days
- escrowed AuMM is burned
- all logic executes on-chain with no admin controls

## XXIII — Eligibility and Competition

- Pools compete under immutable eligibility criteria and efficiency ranking.
- PMAR applies automatically as defined in `PMAR.md`.
- No Bubble voting and no voting over emission allocation.

## XXIV — Governance Gating (Non-Emission)

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

## XXV — Immutable Reference

See Immutable Parameters in `constitution.md`.
