# ixBrevis — Slot 08

**Sector:** US Fixed Income (short / ultra-short)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [`Miliarium_Aureum.md`](../Miliarium_Aureum.md) (Section xi, slot 08).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | SGOVon | 16% | ERC-20 | Tokenized SGOV ETF |
| Theme Asset B | SHYon | 16% | ERC-20 | Tokenized SHY ETF |

## Profile

**Role:** Ultra-short government and short-duration bond ETF exposure — cash-like and short-rate sensitivity within the bond sleeve.
