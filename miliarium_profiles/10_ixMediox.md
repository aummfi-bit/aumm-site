# ixMediox — Slot 10

**Sector:** US Fixed Income (aggregate + TIPS)
**Template:** Standard (52% / 16% / 32%)

---

## Composition

Binding weights are in [`Miliarium_Aureum.md`](../Miliarium_Aureum.md) (Section xi, slot 10).

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| Yield Core A | svZCHF | 26% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |
| Yield Core B | waEthUSDC | 26% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Routing Anchor | ixEDEL | 16% | ERC-20 (DTF) | Cross-pool arbitrage routing |
| Theme Asset A | AGGon | 16% | ERC-20 | Tokenized AGG ETF |
| Theme Asset B | TIPon | 16% | ERC-20 | Tokenized TIP ETF |

## Profile

**Role:** Core US aggregate bonds plus inflation-linked Treasuries — duration and breakeven exposure in one sleeve.
