# Sector Taxonomy

*How the 25 Mercatūs Praecursorii map to a diversified on-chain economy.*

---

## Design Principle

The Pioneer constellation is structured as a **miniature economy** — not a random collection of liquidity pools. Each sector represents a distinct asset class or market segment found in traditional finance, mapped onto on-chain primitives. This ensures:

1. **Sector rotation dynamics** — when tech sells off, capital rotates to treasuries or gold; the protocol captures fees on both legs
2. **Aggregator diversity** — each sector attracts different external volume sources (crypto aggregators, equity wrappers, FX corridors)
3. **Correlation hedging** — uncorrelated theme assets reduce the chance of simultaneous volume collapse across all 25 pools
4. **Economic completeness** — LPs can express any macro view (risk-on, risk-off, sector bet) within the protocol

---

## Sector Definitions

### I. Crypto-Native (4 pools)

Exposure to the foundational infrastructure of DeFi and digital assets.

| Sector | Pools | Theme Assets | Real-World Analogue |
|:-------|:------|:-------------|:--------------------|
| **Crypto Infrastructure** | ixHelvetia, ixStrata, ixForum | waEthUSDT/USDC, LINK/AAVE, SKY/LDO | DeFi governance tokens — equivalent to owning shares in financial infrastructure companies |
| **Digital Gold / Bitcoin** | ixAugusta | WBTC/cbBTC | Bitcoin as digital store of value — equivalent to a gold ETF in TradFi |

**Volume drivers:** DEX aggregator routing (1inch, Paraswap, CowSwap), arbitrage between wrapped BTC variants, DeFi governance token trading.

### II. DeFi Ecosystem & Yield (5 pools)

The yield-bearing primitive layer and ecosystem protocol tokens.

| Sector | Pools | Theme Assets | Real-World Analogue |
|:-------|:------|:-------------|:--------------------|
| **DeFi Ecosystem** | ixRegistrum, ixBeneficium, ixEcosysthema, ixImperium | ETHPLUS/OPEN, ENA/sUSDe, FRAX/CHEX, PENDLE/EIGEN | Yield funds and ecosystem ETFs — exposure to DeFi's productive layer |
| **DeFi Lending Infra** | ixAuxilium | Morpho/SPK | Lending protocol governance — like owning shares in banks' lending divisions |

**Volume drivers:** Yield strategy rebalancing, ecosystem token accumulation, Ethena/Pendle/EigenLayer narratives.

### III. ETH Staking (1 pool)

The Ethereum proof-of-stake governance layer.

| Sector | Pools | Theme Assets | Real-World Analogue |
|:-------|:------|:-------------|:--------------------|
| **ETH Staking** | ixCasper | RPL/ETHFI | Staking infrastructure stocks — like owning shares in clearing houses |

**Volume drivers:** LST rebalancing, staking governance token demand, rETH/weETH arbitrage via Aave stataToken wrappers.

**Note:** ixCasper is non-standard — its yield core is waEthrETH/waEthweETH (Aave V3 stataToken ERC-4626 wrappers), not svZCHF-based. ERC-4626 composition: 54%.

### IV. TradFi Equities (6 pools)

Tokenised stocks and equity indices bridging traditional markets on-chain.

| Sector | Pools | Theme Assets | Real-World Analogue |
|:-------|:------|:-------------|:--------------------|
| **US Equities (Large Cap)** | ixAureum | SPYon/IVVon | S&P 500 index funds — broad US market exposure |
| **US Equities (Tech Index)** | ixVictoria | QQQon/QQQX | Nasdaq-100 — tech-heavy index exposure |
| **US Equities (Mega Cap Tech)** | ixGigantus, ixMajestas | NVDAon/TSLAon, MSFTon/AAPLon | Individual mega-cap tech stocks — concentrated single-name exposure |
| **Banking / Financials** | ixMoneta | JPMon/GSon | Bank stocks — traditional financial sector |
| **Fintech / Brokers** | ixMercatura | COIN/HOOD | Crypto-native fintech — bridges TradFi and DeFi |

**Volume drivers:** Tokenised equity wrappers (Ondo, Backed, Dinari ecosystem), 24/7 equities trading demand, US market hours arbitrage, sector rotation flows.

### V. Macro & Hard Assets (4 pools)

Commodities, bonds, and inflation-protection instruments.

| Sector | Pools | Theme Assets | Real-World Analogue |
|:-------|:------|:-------------|:--------------------|
| **Gold / Commodities** | ixAppia | PAXG/XAUt | Physical gold — the original store of value |
| **Gold / Inflation Protection** | ixCustodia | GLDon/TIPon | Gold ETF + TIPS — inflation hedging basket |
| **Treasuries / Fixed Income** | ixVectura | SGOVon/TLTon | US government bonds — risk-free rate benchmark |
| **Pharma / Healthcare** | ixSalus | LLYon/NVOon | Pharmaceutical blue-chips — defensive sector |

**Volume drivers:** Flight-to-safety flows (treasuries, gold), macro rotation (risk-off trades), healthcare sector demand, TIPS rebalancing.

### VI. Staking & FX (2 pools)

Liquid staking derivatives and foreign exchange corridors.

| Sector | Pools | Theme Assets | Real-World Analogue |
|:-------|:------|:-------------|:--------------------|
| **LST / Staking Derivatives** | ixManes | svZCHF/waEthwstETH | Staking derivatives desk — concentrated LST exposure |
| **FX / Emerging Markets** | ixViatica | fBRZ/st-EURA | Forex pairs — BRL and EUR corridors, emerging market access |

**Volume drivers:** LST/ETH arbitrage, Lido wstETH demand, FX corridor flows (BRL remittances, EUR/USD spread trading).

**Note:** ixManes is non-standard — its yield core is fWSTETH/fWETH (Flux Finance vaults), with svZCHF appearing as a theme asset rather than yield core.

### VII. Routing Infrastructure (3 pools)

Non-standard pools serving structural roles in the protocol's routing graph.

| Sector | Pools | Composition | Real-World Analogue |
|:-------|:------|:-----------|:--------------------|
| **ixEDEL Price Discovery** | ixEdelweiss | ixEDEL (46%), waEthUSDC (18%), waEthUSDT (18%), svZCHF (18%) | Primary market maker — like a designated market maker on an exchange |
| **USD Stablecoin Hub** | ixLibertas | 7-token USD stablecoin pool (no ixEDEL) | Money market fund — deep USD liquidity venue |
| **FX Hub** | ixCambio | ixEDEL (20%), svZCHF/st-EURA/aEURS/s-tGBP/Partner (16% each) | FX trading desk — multi-currency with yield-bearing stablecoins |

**Volume drivers:** Cross-pool routing (all 25 pools connect through these hubs), stablecoin arbitrage, FX spread capture, ixEDEL price discovery.

---

## Sector Correlation Matrix (Qualitative)

Understanding how sectors move relative to each other during macro regimes:

| Regime | Crypto | DeFi Yield | Equities | Banking | Gold | Treasuries | Pharma | FX |
|:-------|:-------|:-----------|:---------|:--------|:-----|:-----------|:-------|:---|
| **Risk-On** | ++ | ++ | ++ | + | - | - | 0 | 0 |
| **Risk-Off** | -- | - | -- | - | ++ | ++ | + | + |
| **Inflation** | + | + | - | - | ++ | -- | 0 | + |
| **DeFi Summer** | ++ | ++ | 0 | 0 | 0 | 0 | 0 | 0 |
| **Rate Hikes** | - | 0 | - | + | - | -- | 0 | + |
| **Crypto Winter** | -- | -- | 0 | 0 | + | + | 0 | 0 |

*++/-- = strong positive/negative correlation, +/- = moderate, 0 = neutral*

This diversity is the structural defence against protocol-wide volume collapse. Even in the worst macro environment, some sectors generate fees.

---

## Cross-References

- Pool compositions and weights → [Mercatūs Praecursorii](../Mercatus_Praecursorii.md)
- PMAR emission multipliers → [PMAR Specification](../PMAR.md)
- Performance discipline → [Constitution: Anti-Gaming Criteria](../constitution.md)
- Bootstrapping mechanics → [Bootstrap Rules](../bootstrap.md)
- Individual pool profiles → [Manifest](manifest.md)
