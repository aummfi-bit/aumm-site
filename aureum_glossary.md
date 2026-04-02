# Aureum Protocol - Glossary

## Core Tokens

- **AuMM**: reward token with 21,000,000 max supply and immutable halving schedule.
- **AuMT**: LP participation token proving active liquidity position.

## Core Systems

- **Aequilibrium**: AMM engine.
- **CCB**: automatic emission allocator using EMA(60) TVL.
- **PMAR**: automatic multiplier rule for Miliarium Aureum pools.
- **EMA(60)**: 60-day exponential moving average of TVL.

## Launch Structure

- **Miliarium Aureum**: 25 immutable founding pools, locked at launch.
- **Year 1 Equal Regime**: emissions split equally across the 25 pools.
- **Post-Year-1 Automatic Regime**: CCB + PMAR allocation with no voting.

## Controls

- no admin keys
- no multisig
- no upgradability
- no pause function
- no voting over emissions

## Governance

- **Gauge Proposal**: submit gauge request with AuMM burn deposit.
- **Gauge Challenge**: challenge/revoke active gauge with AuMM burn deposit.
- **Treasury Proposal**: qualified AuMT voting path for treasury disbursement via timelock.
- **On-Chain-Only Proposal Rule**: every proposal must cite verifiable on-chain state.

See Immutable Parameters in `constitution.md`.
