> **Internal document — not part of the public protocol specification.**

# Aureum Delivery Schedule (Consolidated)

## Phase 1 - Immutable Core

- finalize AuMM token with 21,000,000 hard cap
- implement per-block emission with halving every 10,512,000 blocks
- deploy immutable contracts with no admin, no multisig, no upgrade path

## Phase 2 - Equal regime (through Month 10)

- deploy and seed 26 of the 28 Miliarium pools, slots 4 and 7 left open
- activate der Bodensee bootstrap emission (piecewise linear: 80% at genesis → 50% at end of Month 6 → 0% at end of Month 10; one-sided AuMM per [Protocol formulas (F-0)](11_formulas.md)), accruing per block and delivered in bounded flushes once der Bodensee is initialized
- initialize der Bodensee from the Stage B multisig as soon as it can after emissions start, with AuMM it earns as a staked liquidity provider of a Miliarium pool; the multisig keeps the founding BPT as an ordinary LP position
- activate equal 1/M of the **LP emission tranche** across the live Miliarium pools through end of Month 10
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
