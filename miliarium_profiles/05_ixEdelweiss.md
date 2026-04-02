# ixEdelweiss — Slot 05

**Sector:** Routing Infrastructure
**Template:** Non-Standard (ixEDEL-heavy price discovery pool)

---

## Composition

| Component | Token | Weight | Role |
|:----------|:------|:-------|:-----|
| ixEDEL | 46% | ERC-20 (DTF) | Primary price discovery — concentrated ixEDEL liquidity |
| waEthUSDC | 18% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| waEthUSDT | 18% | ERC-4626 | Aave V3 stataToken wrapper for USDT |
| svZCHF | 18% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |

**ERC-4626 composition:** 54% (waEthUSDC + waEthUSDT + svZCHF) — exceeds 52% threshold.

## Profile

**Real-world analogue:** Designated market maker — like the specialist firm on a stock exchange floor that provides continuous two-sided quotes for a specific security.

**Theme rationale:** ixEdelweiss exists for one purpose: **ixEDEL price discovery**. With 46% weight in ixEDEL, this is the deepest ixEDEL liquidity venue in the protocol. Every cross-pool arbitrage route that touches ixEDEL passes through here. The three stablecoin vaults (USDC, USDT, CHF) provide the pricing anchors.

**Structural role:**
- Primary ixEDEL ↔ USD price reference
- Cross-pool routing hub (most pools use a **16% ixEDEL** slice; **ixHelvetia** and **ixLibertas** do not — see registry; rebalancing among ixEDEL-anchored pools still concentrates through here)
- ixEDEL basket rebalancing (ixEDEL is a Reserve Protocol DTF; any constituent drift creates arbitrage with this pool)

**Volume drivers:**
- Cross-pool arbitrage across ixEDEL-anchored pools
- ixEDEL basket composition changes
- New LP entries/exits in pools that hold ixEDEL for routing
- Stablecoin rotation via the three anchor stables

**Risk profile:**
- ixEDEL basket risk (Reserve Protocol DTF composition)
- Concentrated exposure to a single non-stablecoin asset (46% ixEDEL)
- Smart contract risk (Reserve Protocol DTF + Aave wrappers)
- Higher IL risk during ixEDEL price discovery phases

## Performance Discipline

| Criterion | Requirement |
|:----------|:-----------|
| 4626 Quality Gate | ≥52% — met by waEthUSDC (18%) + waEthUSDT (18%) + svZCHF (18%) = 54% |
| Vault TVL floor | Each vault ≥$5M / 30 BTC / 4M svZCHF |
| Volume percentile floor | 5th (months 3–6) → 10th (months 6–12) → 15th (month 13+) |
| Efficiency tournament | Bottom 15% → emission cap (month 13+) |
| MAMAR multiplier | [0.75–1.25], initialised at 1.0 |
| Composition challenge | If tokens lack volume or cease to exist, composition renewable via Miliarium Aureum Composition Challenge (base cost 100,000 svZCHF/1 BTC/100,000 sUSDS equiv × dynamic factors; requires 2/3 protocol-wide tessera-weighted vote; replacement must preserve same asset type or similar economic properties) |

## Cross-References

- [Manifest](manifest.md) | [Sectors](sectors.md) | [MAMAR](../MAMAR.md)
