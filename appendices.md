## Appendix I - Architecture Provenance

Aequilibrium inherits Balancer V3 pool architecture and introduces a new immutable tokenomics and allocation layer.

## Appendix II - Pure Real DeFi Positioning

This design targets strict Real DeFi alignment:

- immutable from block 0
- no admin keys
- no multisig
- no voting over emissions
- no discretionary transition controls

## Appendix III - Emission Logic Summary

- Year 1 equal emission split across 28 Miliarium Aureum pools
- Post-Year-1 automatic CCB EMA(60) + PMAR allocation
- Bitcoin-style per-block halving schedule toward 21,000,000 cap

## Appendix IV - Reference

See Immutable Parameters in `constitution.md`.
