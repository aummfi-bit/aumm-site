> **Internal document — not part of the public protocol specification.**

# Aureum Delivery Schedule (Consolidated)

## Phase 1 - Immutable Core

- finalize AuMM token with 21,000,000 hard cap
- implement per-block emission with halving every 10,512,000 blocks
- deploy immutable contracts with no admin, no multisig, no upgrade path

## Phase 2 - Equal regime (through Month 10)

- deploy and seed the 28 Miliarium pools
- activate der Bodensee bootstrap emission (piecewise linear: 80% at genesis → 50% at end of Month 6 → 0% at end of Month 10; one-sided AuMM per [Protocol formulas (F-0)](11_formulas.md))
- activate equal 1/28 of the **LP emission tranche** through end of Month 10
- run telemetry and invariants for immutable execution checks

## Phase 2b - Transition (Months 11–12)

- run linear α blend from equal to CCB; verify midpoint α = 0.5 behavior

## Phase 3 - Automatic Regime Activation

- activate full CCB (multiplier + Incendiary Boost) from the first block after Year 1 (α = 1)
- verify EMA(60) and CCB multiplier outputs match immutable constants
- validate no discretionary controls in production wiring

## Phase 4 - Audit and Publication

- complete external audit of all new tokenomics contracts
- publish immutable parameter manifest
- publish public verification guide for bytecode and parameters

See [Immutable Parameters (§xxix)](10_constitution.md).
