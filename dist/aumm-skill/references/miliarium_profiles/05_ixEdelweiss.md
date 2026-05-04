<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 miliarium_profiles/05_ixEdelweiss.md — DO NOT EDIT -->
# ixEdelweiss — Slot 05

**Sector:** Routing Infrastructure
**Template:** Non-Standard (ixEDEL-heavy price discovery pool)

---

## Composition

| Component | Token | Weight | Standard | Role |
|:----------|:------|:-------|:---------|:-----|
| ixEDEL hub | ixEDEL | 46% | ERC-20 (DTF) | Primary price discovery — concentrated ixEDEL liquidity |
| Stablecoin A | waEthUSDC | 18% | ERC-4626 | Aave V3 stataToken wrapper for USDC |
| Stablecoin B | waEthUSDT | 18% | ERC-4626 | Aave V3 stataToken wrapper for USDT |
| Stablecoin C | svZCHF | 18% | ERC-4626 | Frankencoin savings vault (~3.75% yield) |

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
| CCB multiplier | Immutable band, initialised at 1.0 — see [Constitution (§xxix)](10_constitution.md) |
| Composition challenge | If tokens lack volume or cease to exist, a Miliarium Aureum Composition Challenge can deprecate this pool and launch a replacement into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Requires 2/3 protocol-wide tessera-weighted vote; replacement must be like-for-like (same sector, risk, template role) — see [Bootstrap (§xxiv)](08_bootstrap.md) |

## Cross-References

- [Manifest](../06_miliarium_manifest.md) | [Sectors](../07_miliarium_sectors.md) | [CCB Multiplier](../03_theoretical_foundation.md)
