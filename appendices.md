# Appendices

## xxxvi. Architecture Provenance

Aequilibrium inherits Balancer V3 pool architecture and introduces a new immutable tokenomics and allocation layer.

## xxxvii. Pure Real DeFi Positioning

This design targets strict Real DeFi alignment:

- immutable from block 0
- no admin keys
- no multisig
- no voting over emissions
- no discretionary transition controls

## xxxviii. Emission Logic Summary

- Through Month 10: equal 1/28 emission split across 28 Miliarium Aureum pools
- Months 11–12: linear transition (α: 0 → 1) to CCB
- After Year 1: pure automatic CCB EMA(60) + PMAR allocation
- Bitcoin-style per-block halving schedule toward 21,000,000 cap

## xxxix. Reference

See Immutable Parameters in `constitution.md`.
