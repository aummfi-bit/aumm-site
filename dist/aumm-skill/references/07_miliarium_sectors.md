<!-- GENERATED FROM aumm-site@793427c1c6d9e06890c7f2fb32a61466eeacfcf5 07_miliarium_sectors.md — DO NOT EDIT -->
# Sector Taxonomy

*How the 28 Miliarium pools map to a diversified on-chain economy.*

Binding compositions, slot order, and stock subclasses are in [Miliarium Aureum](05_miliarium_aureum.md) (**slots 01–28**). Connector pools are **05–07** (Edelweiss, Libertas, Cambio). One profile per pool: **`NN_ixCanonicalName.md`** in [manifest](06_miliarium_manifest.md). **Deduplicated token list (ticker, ERC type, pools):** [07a_tokens.md](07a_tokens.md).

## xvi. Mapping and slot ranges

### Mapping to registry categories

| Category | Pools (canonical names) |
|:---------|:------------------------|
| Yield-bearing | ixHelvetia, ixAetheron, ixCasper, ixViatica, ixEdelweiss, ixLibertas, ixCambio |
| Bonds | ixBrevis, ixAltrix, ixMediox, ixLongus |
| Crypto-native governance & protocols | ixStrata, ixForum, ixAurebit, ixRegistrum, ixDebitum |
| Stocks | ixEquitix, ixInnovix, ixGigantus, ixMagnix, ixNubix, ixMoneta, ixColossix, ixVitalix, ixMedicix, ixMercatura |
| Metals | ixAurix, ixMetallum |

Stock **subclasses** (broad ETF, tech index, mega-cap tech, financials, healthcare, fintech) are in the [Miliarium Aureum](05_miliarium_aureum.md) Section xi registry (Stocks table).

### Slot ranges (canonical)

| Slots | Class | Role |
|:------|:------|:-----|
| 01–07 | Yield | Savings, LST/staking, flux LST, FX corridors, ixEDEL venue, USD hub, multi-currency FX |
| 08–11 | Bonds | Short / ultra-short, HY, aggregate + TIPS, long Treasury |
| 12–16 | Crypto-native | DeFi infrastructure, wrapped BTC, ecosystem and lending governance |
| 17–26 | Stocks | Tokenised equities (see subclasses in Section xi Stocks table) |
| 27–28 | Metals | Physical gold; silver + uranium ETFs |

---

## xvii. Design Principle

The Miliarium Aureum is a **miniature economy**, not a random collection of liquidity pools. (Conceptual introduction: [Mental model — The Miniature Economy](02_mental_model.md).) Each sector maps a distinct asset class from traditional finance onto on-chain primitives:

- **Sector rotation dynamics** — when tech sells off, capital rotates to treasuries or gold; the protocol captures fees on both legs
- **Aggregator diversity** — each sector attracts different external volume sources (crypto aggregators, equity wrappers, FX corridors)
- **Correlation hedging** — uncorrelated theme assets reduce the chance of simultaneous volume collapse across all 28 Miliarium pools
- **Economic completeness** — LPs can express any macro view (risk-on, risk-off, sector bet) within the protocol

---

## xviii. Sector definitions (canonical names)

### Yield (slots 01–07)

| Pool | Profile | Notes |
|:-----|:--------|:------|
| [ixHelvetia](01_ixHelvetia.md) | Frankencoin MMA | **80% svZCHF / 20% sUSDS** — not a standard 52/16/32 pool; no ixEDEL |
| [ixAetheron](02_ixAetheron.md) | ETH staking | waEthrETH / waEthweETH; non-standard weights |
| [ixCasper](03_ixCasper.md) | LST / Flux | fWSTETH / fWETH; svZCHF appears as theme |
| [ixViatica](04_ixViatica.md) | FX / EM | fBRZ / st-EURA |
| [ixEdelweiss](05_ixEdelweiss.md) | ixEDEL price discovery | Non-standard connector |
| [ixLibertas](06_ixLibertas.md) | USD stable hub | No ixEDEL |
| [ixCambio](07_ixCambio.md) | Multi-currency FX | Non-standard connector |

### Bonds (slots 08–11)

| Pool | Profile | Theme sleeve |
|:-----|:--------|:---------------|
| [ixBrevis](08_ixBrevis.md) | Short / ultra-short | SGOVon / SHYon |
| [ixAltrix](09_ixAltrix.md) | High yield | HYGon / FLHYon |
| [ixMediox](10_ixMediox.md) | Core + TIPS | AGGon / TIPon |
| [ixLongus](11_ixLongus.md) | Long Treasury | TLTon **32%** (non-standard single theme) |

### Crypto-native (slots 12–16)

| Pool | Profile | Theme |
|:-----|:--------|:------|
| [ixStrata](12_ixStrata.md) | DeFi infra | LINK / AAVE |
| [ixForum](13_ixForum.md) | DeFi infra | SKY / LDO |
| [ixAurebit](14_ixAurebit.md) | Wrapped BTC | WBTC / cbBTC |
| [ixRegistrum](15_ixRegistrum.md) | Ecosystem | ETHPLUS / OPEN |
| [ixDebitum](16_ixDebitum.md) | Lending governance | Morpho / SPK |

### TradFi equities (slots 17–26)

| Pool | Profile | Subclass (see Section xi) |
|:-----|:--------|:----------------------------|
| [ixEquitix](17_ixEquitix.md) | Broad index | Broad ETF |
| [ixInnovix](18_ixInnovix.md) | Nasdaq-style | Tech index |
| [ixGigantus](19_ixGigantus.md) | Single-name tech | Mega-cap tech |
| [ixMagnix](20_ixMagnix.md) | Single-name tech | Mega-cap tech |
| [ixNubix](21_ixNubix.md) | Consumer internet | Mega-cap tech |
| [ixMoneta](22_ixMoneta.md) | Banks | Financials |
| [ixColossix](23_ixColossix.md) | Asset managers / banks | Financials |
| [ixVitalix](24_ixVitalix.md) | Pharma | Healthcare |
| [ixMedicix](25_ixMedicix.md) | Pharma | Healthcare |
| [ixMercatura](26_ixMercatura.md) | Brokers | Fintech |

### Metals (slots 27–28)

| Pool | Profile | Theme |
|:-----|:--------|:------|
| [ixAurix](27_ixAurix.md) | Gold | PAXG / XAUt |
| [ixMetallum](28_ixMetallum.md) | Silver / uranium | SLVon / URAon |

---

## xix. Sector Correlation Matrix (Qualitative)

How sectors move relative to each other during macro regimes:

| Regime | Crypto | DeFi Yield | Equities | Banking | Gold | Treasuries | Pharma | FX |
|:-------|:-------|:-----------|:---------|:--------|:-----|:-----------|:-------|:---|
| **Risk-On** | ++ | ++ | ++ | + | - | - | 0 | 0 |
| **Risk-Off** | -- | - | -- | - | ++ | ++ | + | + |
| **Inflation** | + | + | - | - | ++ | -- | 0 | + |
| **DeFi Summer** | ++ | ++ | 0 | 0 | 0 | 0 | 0 | 0 |
| **Rate Hikes** | - | 0 | - | + | - | -- | 0 | + |
| **Crypto Winter** | -- | -- | 0 | 0 | + | + | 0 | 0 |

*++/-- = strong positive/negative correlation, +/- = moderate, 0 = neutral*

Structural defence against protocol-wide volume collapse. Even in the worst macro environment, some sectors generate fees.

---

## xx. Cross-References

- Pool compositions and weights → [Miliarium Aureum](05_miliarium_aureum.md)
- CCB emission multipliers → [Theoretical Foundation § vii](03_theoretical_foundation.md) · [Formulas F-8](11_formulas.md) · [Immutable Parameters](10_constitution.md) §xxix
- Performance discipline → [Constitution: Anti-Gaming Criteria](10_constitution.md)
- Bootstrapping mechanics → [Bootstrap Rules](08_bootstrap.md)
- Individual pool profiles → [Manifest](06_miliarium_manifest.md)
