# Aureum Delivery Schedule (Consolidated)

## Phase 1 - Immutable Core

- finalize AuMM token with 21,000,000 hard cap
- implement per-block emission with halving every 10,512,000 blocks
- deploy immutable contracts with no admin, no multisig, no upgrade path

## Phase 2 - Equal regime (through Month 10)

- deploy and seed the 28 Miliarium Aureum pools
- activate equal 1/28 emission distribution through end of Month 10
- run telemetry and invariants for immutable execution checks

## Phase 2b - Transition (Months 11–12)

- run linear α blend from equal to CCB; verify midpoint α = 0.5 behavior

## Phase 3 - Automatic Regime Activation

- activate full CCB + PMAR from the first block after Year 1 (α = 1)
- verify EMA(60) and PMAR outputs match immutable constants
- validate no discretionary controls in production wiring

## Phase 4 - Audit and Publication

- complete external audit of all new tokenomics contracts
- publish immutable parameter manifest
- publish public verification guide for bytecode and parameters

See Immutable Parameters in `constitution.md`.
