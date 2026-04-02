# The Miliarium Aureum

The 25 pools are pre-defined at launch and locked from block 0. No open slots.

### Scope

- There are **25** immutable Miliarium Aureum pools (the founding constellation).
- During Year 1 they receive equal emissions (1/25 each).
- After Year 1 they compete under automatic CCB EMA(60) + PMAR rules.

### Canonical registry

The tables below are the binding list of pools and compositions. Emission allocation is not vote-controlled; governance applies only to non-emission actions (see `constitution.md`, `bootstrap.md`).

---

## I — Registry and structure

All 25 Miliarium Aureum pools are pre-defined at launch and locked from block 0. No open slots. The 25 pools below constitute the complete founding infrastructure.

### The dual-anchor system: svZCHF + ixEDEL

Most **standard-template** pools (slots 01–22) contain both **svZCHF** (yield anchor — ERC-4626, Frankencoin savings rate ~3.75%, counts toward the 4626 Quality Gate) and **ixEDEL** (routing anchor — ERC-20, Reserve Protocol DTF, IL reduction via diversified basket, internal cross-pool arbitrage routing, strategic moat). **Connector pools** (slots 23–25) use the non-standard compositions in Section VI; **ixLibertas** has no ixEDEL by design.

### Standardised pool template

Standard-template Miliarium Aureum pools follow a consistent weight structure:

| Component | Weight | Role |
|-----------|--------|------|
| Yield Core (2 ERC-4626 tokens) | 52% (26% + 26%) | Meets 4626 Quality Gate. Generates protocol yield fees from block one. |
| Routing Anchor (ixEDEL) | 16% | Cross-pool arbitrage. Constellation routing connectivity. |
| Theme Assets (2 tokens) | 32% (16% + 16%) | Sector exposure. Drives aggregator volume from external markets. |

### I. The founding infrastructure (slots 01–05)

Core routing gates for crypto-native benchmarks.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 01 | **ixHelvetia** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% waEthUSDT / 16% USDC |
| 02 | **ixStrata** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% LINK / 16% AAVE |
| 03 | **ixForum** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% SKY / 16% LDO |
| 04 | **ixAppia** | 26% svZCHF / 26% sfrxUSD | 16% ixEDEL | 16% PAXG / 16% XAUt |
| 05 | **ixAugusta** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% WBTC / 16% cbBTC |

### II. The reserve and ecosystem empire (slots 06–09)

Consolidating the Sagix/Reserve stack, yield-bearing primitives, and ecosystem tokens.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 06 | **ixRegistrum** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% ETHPLUS / 16% OPEN |
| 07 | **ixBeneficium** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% ENA / 16% sUSDe |
| 08 | **ixEcosysthema** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% FRAX / 16% CHEX |
| 09 | **ixImperium** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% PENDLE / 16% EIGEN |

### III. ETH staking governance and DeFi infra (slots 10–11)

Capturing the ETH staking governance layer and DeFi lending infrastructure.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 10 | **ixCasper** | 27% waEthrETH / 27% waEthweETH | 15% ixEDEL | 15% RPL / 16% ETHFI |
| 11 | **ixAuxilium** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% Morpho / 16% SPK |

**ixCasper** — ETH staking governance pool. Non-standard composition: waEthrETH and waEthweETH are Aave V3 stataToken ERC-4626 wrappers for Rocket Pool's rETH and EtherFi's weETH respectively. ERC-4626 composition: 54% (both yield core tokens). RPL (Rocket Pool governance) and ETHFI (EtherFi governance) provide exposure to the staking protocol upside alongside the underlying staking yield.

### IV. The equity and index empire (slots 12–17)

TradFi indices, tokenised equity wrappers, and fintech.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 12 | **ixAureum** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% SPYon / 16% IVVon |
| 13 | **ixVictoria** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% QQQon / 16% QQQX |
| 14 | **ixGigantus** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% NVDAon / 16% TSLAon |
| 15 | **ixMajestas** | 26% svZCHF / 26% sfrxUSD | 16% ixEDEL | 16% MSFTon / 16% AAPLon |
| 16 | **ixMoneta** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% JPMon / 16% GSon |
| 17 | **ixMercatura** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% COIN / 16% HOOD |

### V. Macro, hard assets and global FX (slots 18–22)

Treasuries, energy, LSTs, and global fiat corridors.

| Slot | Pool Name | Yield Core (52%) | Anchor (16%) | Theme Assets (32%) |
|:-----|:----------|:-----------------|:-------------|:-------------------|
| 18 | **ixSalus** | 26% svZCHF / 26% sUSDS | 16% ixEDEL | 16% LLYon / 16% NVOon |
| 19 | **ixVectura** | 26% svZCHF / 26% waEthUSDC | 16% ixEDEL | 16% SGOVon / 16% TLTon |
| 20 | **ixCustodia** | 26% svZCHF / 26% waEthUSDT | 16% ixEDEL | 16% GLDon / 16% TIPon |
| 21 | **ixManes** | 26% fWSTETH / 26% fWETH | 16% ixEDEL | 16% svZCHF / 16% waEthwstETH |
| 22 | **ixViatica** | 26% svZCHF / 26% GHO | 16% ixEDEL | 16% fBRZ / 16% st-EURA |

### VI. Core connector pools (slots 23–25)

Anchor and infrastructure pools with non-standard compositions. These pools serve specialised routing and price discovery roles that require weight distributions outside the standard 52%/16%/32% template.

| Slot | Pool Name | Composition | Role |
|:-----|:----------|:-----------|:-----|
| 23 | **ixEdelweiss** | ixEDEL (46%), waEthUSDC (18%), waEthUSDT (18%), svZCHF (18%) | Primary ixEDEL price discovery venue. ixEDEL-heavy weighting concentrates liquidity for the routing anchor. |
| 24 | **ixLibertas** | scrvUSD (15%), PYUSD (15%), GHO (14%), sUSDS (14%), sfrxUSD (14%), USDT (14%), USDC (14%) | USD stablecoin hub. Seven-token pool spanning major USD stables and savings vaults. No ixEDEL — functions as a standalone deep-liquidity USD venue. |
| 25 | **ixCambio** | ixEDEL (20%), svZCHF (16%), st-EURA (16%), aEURS (16%), s-tGBP (16%), [Partner Stable] (16%) | FX hub. Multi-currency pool (CHF, EUR, GBP, USD) with yield-bearing stablecoins via Aave/Morpho vaults. Competes directly with Curve's FXSwap (launched ZCHF/crvUSD at Stable Summit Cannes, March 2026) but captures multiple FX pairs from one LP position. |

### Cross-pool arbitrage

With 25 pools sharing svZCHF and ixEDEL as common anchors, six arbitrage layers generate fees continuously: vault-rate arbitrage (ERC-4626 drift correction), CHF/USD forex arbitrage, multi-currency FX arbitrage, wrapped-asset arbitrage (gold-to-gold, BTC-to-BTC), cross-pool price arbitrage (25 pools × 2 shared anchors = dense routing graph), and external-internal arbitrage (constituent tokens trading $898M+ daily on Uniswap at higher fees).

### Miliarium Aureum benefits

**1. PMAR emission multiplier.** Miliarium Aureum pools are the only pools eligible for the automatic PMAR multiplier [0.75–1.25] (see **PMAR Specification**).

**2. Treasury liquidity deposits.** Revenue from treasury AuMM sales during the price ceiling stabilization is deposited as permanent locked liquidity into Miliarium Aureum pools meeting the 4626 Quality Gate and $10K+ TVL. The treasury can never withdraw.

**Permanent slots.** The 25 Miliarium Aureum slots are permanent protocol infrastructure — the number never decreases. If a pool underperforms due to sector rotation, the PMAR emission multiplier boosts it automatically (anticyclical by design). If specific tokens within a pool lack on-chain volume or cease to exist, any AuMT holder can initiate a **Miliarium Aureum Composition Challenge** to propose a new token composition that preserves the pool's function, sector theme, and template structure (see **Bootstrap Rules** and `constitution.md`).

### Pool profiles

Each Miliarium Aureum pool has a detailed structural profile documenting its sector classification, composition rationale, volume drivers, and risk characteristics. See the [miliarium_profiles/manifest.md](miliarium_profiles/manifest.md) directory for the full registry, [sector taxonomy](miliarium_profiles/sectors.md), and individual pool profiles.

---

See Immutable Parameters in `constitution.md`.
