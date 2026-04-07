# The Miliarium Aureum

The 28 pools are pre-defined at launch and locked from block 0.

### Scope

- **28** Miliarium Aureum pools (the founding constellation), immutable from block 0.
- Through **end of Month 10**, the **LP emission tranche** splits **equal** (**1/28** each). **Months 11–12** blend **linearly** from equal to CCB (see [Constitution](10_constitution.md)). **After Year 1**, **pure CCB** (EMA TVL × CCB multiplier). Incendiary Boost is a separate priority skim on the LP tranche (1 epoch per boost, any amount, once per epoch per pool).

### AuMM vs the 28 pools

**AuMM** is the reward **token** ([Tokenomics](04_tokenomics.md)), not a Miliarium slot. **der Bodensee Pool** (AuMM/sUSDS/svZCHF weighted pool, fixed 40/30/30) is at the end of this file — **Section xii** (bootstrap AuMM **Months 1–10** only).

### Canonical registry

The registry tables in Section xi are the binding list of pools and compositions (one ordered list **01–28**, split by sector for readability). Emission allocation is not vote-controlled; governance applies only to non-emission actions ([Constitution](10_constitution.md), [Bootstrap](08_bootstrap.md)).

---

## xi. Registry and structure

**Pool count:** **28** pools = **slots 01–28** (one pool per slot), fixed at launch.

**Upstream design.** The 28-pool small-world construction with **two** universal connectors — **svZCHF** (deterministic CHF-anchored reserve rail) and **ixEDEL** (secondary cross-pool routing / arbitrage rail) embedded as shortcut hubs in every pool — is the original [Sagix Miliarium Aureum](https://www.sagix.io/sagix-miliarium-aureum/), live on Balancer V3 Ethereum mainnet, sitting on top of the [Sagix four-layer liquidity-risk framework](https://www.sagix.io/our-layer-framework/). Aureum keeps the dual-anchor backbone and refines two slots — **01 ixHelvetia** (Frankencoin MMA, no ixEDEL) and **06 ixLibertas** (USD stable hub, no ixEDEL) — where pure CHF or pure USD flows are deliberately kept off the ixEDEL basket bridge. See [Mental model (§iii — Dual anchors)](02_mental_model.md) and [Theoretical foundations (§v)](03_theoretical_foundation.md).

One ordered list (01 → 28), **split by sector** for readability; rows, weights, and names are unchanged from the full sequence. **Standard** pools: **52% / 16% / 32%** (two ERC-4626 yield cores, ixEDEL anchor, two theme assets) unless noted. **Connectors 05 (ixEdelweiss), 06 (ixLibertas), 07 (ixCambio)** use non-standard compositions. **Slot 11 (ixLongus):** non-standard single theme at **32%** (TLTon). **Slot 01 (ixHelvetia):** Frankencoin MMA (**no ixEDEL**). **Slot 06 (ixLibertas):** USD stable hub (**no ixEDEL**).

### Standardised pool template (where applicable)

| Component | Weight | Role |
|-----------|--------|------|
| Yield Core (2 ERC-4626 tokens) | 52% (26% + 26%) | Meets 4626 Quality Gate. Generates protocol yield fees from block one. |
| Routing Anchor (ixEDEL) | 16% | Cross-pool arbitrage. Constellation routing connectivity. |
| Theme Assets (2 tokens) | 32% (16% + 16%) | Sector exposure. Drives aggregator volume from external markets. |

Each pool’s weights are shown in three columns — **Yield core**, **Routing** (ixEDEL where used), **Theme** — with *ticker* then *%*. **—** means that bucket has no weight. Non-standard pools may combine tokens in one column or use a single theme leg (see ixLongus). The Yield table uses HTML so **slots 01 and 06** can merge cells when routing and theme are empty, and **slot 05** can merge **Routing + Theme** for **ixEDEL** (price-discovery / routing + theme).

### Yield — slots 01–07

Savings, staking / LST, FX, ixEDEL price-discovery venue, USD hub, and multi-currency FX connectors.

<table>
<thead>
<tr><th align="left">Slot</th><th align="left">Pool</th><th align="left">Yield core</th><th align="left">Routing</th><th align="left">Theme</th></tr>
</thead>
<tbody>
<tr>
<td>01</td>
<td><strong>ixHelvetia</strong></td>
<td colspan="3">svZCHF 80%, sUSDS 20%</td>
</tr>
<tr>
<td>02</td>
<td><strong>ixAetheron</strong></td>
<td>waEthrETH 27%, waEthweETH 27%</td>
<td>ixEDEL 15%</td>
<td>RPL 15%, ETHFI 16%</td>
</tr>
<tr>
<td>03</td>
<td><strong>ixCasper</strong></td>
<td>fWSTETH 26%, fWETH 26%</td>
<td>ixEDEL 16%</td>
<td>svZCHF 16%, waEthwstETH 16%</td>
</tr>
<tr>
<td>04</td>
<td><strong>ixViatica</strong></td>
<td>svZCHF 26%, GHO 26%</td>
<td>ixEDEL 16%</td>
<td>fBRZ 16%, st-EURA 16%</td>
</tr>
<tr>
<td>05</td>
<td><strong>ixEdelweiss</strong></td>
<td>waEthUSDC 18%, waEthUSDT 18%, svZCHF 18%</td>
<td colspan="2">ixEDEL 46% (routing + theme)</td>
</tr>
<tr>
<td>06</td>
<td><strong>ixLibertas</strong></td>
<td colspan="3">scrvUSD 15%, PYUSD 15%, GHO 14%, sUSDS 14%, sfrxUSD 14%, USDT 14%, USDC 14%</td>
</tr>
<tr>
<td>07</td>
<td><strong>ixCambio</strong></td>
<td>svZCHF 16%</td>
<td>ixEDEL 20%</td>
<td>st-EURA 16%, aEURS 16%, s-tGBP 16%, [Partner Stable] 16%</td>
</tr>
</tbody>
</table>

### Bonds — slots 08–11

US fixed-income sleeves (short / HY / core+TIPS / long Treasury), placed after yield and before crypto in slot order.

| Slot | Pool | Yield core | Routing | Theme |
|:-----|:-----|:-----------|:--------|:------|
| 08 | **ixBrevis** | svZCHF 26%, waEthUSDC 26% | ixEDEL 16% | SGOVon 16%, SHYon 16% |
| 09 | **ixAltrix** | svZCHF 26%, waEthUSDC 26% | ixEDEL 16% | HYGon 16%, FLHYon 16% |
| 10 | **ixMediox** | svZCHF 26%, waEthUSDC 26% | ixEDEL 16% | AGGon 16%, TIPon 16% |
| 11 | **ixLongus** | svZCHF 26%, waEthUSDC 26% | ixEDEL 16% | TLTon 32% (non-standard single theme) |

### Crypto-native governance & protocols — slots 12–16

DeFi infrastructure, wrapped BTC, and lending / ecosystem governance tokens.

| Slot | Pool | Yield core | Routing | Theme |
|:-----|:-----|:-----------|:--------|:------|
| 12 | **ixStrata** | svZCHF 26%, waEthUSDC 26% | ixEDEL 16% | LINK 16%, AAVE 16% |
| 13 | **ixForum** | svZCHF 26%, waEthUSDT 26% | ixEDEL 16% | SKY 16%, LDO 16% |
| 14 | **ixAurebit** | svZCHF 26%, GHO 26% | ixEDEL 16% | WBTC 16%, cbBTC 16% |
| 15 | **ixRegistrum** | svZCHF 26%, sUSDS 26% | ixEDEL 16% | ETHPLUS 16%, OPEN 16% |
| 16 | **ixDebitum** | svZCHF 26%, sUSDS 26% | ixEDEL 16% | Morpho 16%, SPK 16% |

### Stocks — slots 17–26

Tokenised equities; **Subclass** narrows the sleeve (ETF vs index vs mega-cap vs sector).

| Slot | Pool | Subclass | Yield core | Routing | Theme |
|:-----|:-----|:---------|:-----------|:--------|:------|
| 17 | **ixEquitix** | Broad ETF | svZCHF 26%, sUSDS 26% | ixEDEL 16% | SPYon 16%, IVVon 16% |
| 18 | **ixInnovix** | Tech index | svZCHF 26%, waEthUSDC 26% | ixEDEL 16% | QQQon 16%, QQQX 16% |
| 19 | **ixGigantus** | Mega-cap tech | svZCHF 26%, waEthUSDT 26% | ixEDEL 16% | NVDAon 16%, TSLAon 16% |
| 20 | **ixMagnix** | Mega-cap tech | svZCHF 26%, sfrxUSD 26% | ixEDEL 16% | MSFTon 16%, AAPLon 16% |
| 21 | **ixNubix** | Mega-cap tech | svZCHF 26%, sUSDS 26% | ixEDEL 16% | GOOGLon 16%, AMZNon 16% |
| 22 | **ixMoneta** | Financials | svZCHF 26%, GHO 26% | ixEDEL 16% | JPMon 16%, GSon 16% |
| 23 | **ixColossix** | Financials | svZCHF 26%, sUSDS 26% | ixEDEL 16% | BLKon 16%, BACon 16% |
| 24 | **ixVitalix** | Healthcare | svZCHF 26%, sUSDS 26% | ixEDEL 16% | LLYon 16%, NVOon 16% |
| 25 | **ixMedicix** | Healthcare | svZCHF 26%, sUSDS 26% | ixEDEL 16% | JNJon 16%, ABBVon 16% |
| 26 | **ixMercatura** | Fintech | svZCHF 26%, sUSDS 26% | ixEDEL 16% | COIN 16%, HOOD 16% |

### Metals — slots 27–28

Physical gold vs silver / uranium ETF themes.

| Slot | Pool | Yield core | Routing | Theme |
|:-----|:-----|:-----------|:--------|:------|
| 27 | **ixAurix** | svZCHF 26%, sfrxUSD 26% | ixEDEL 16% | PAXG 16%, XAUt 16% |
| 28 | **ixMetallum** | svZCHF 26%, waEthUSDT 26% | ixEDEL 16% | SLVon 16%, URAon 16% |

---

### Cross-pool arbitrage

Shared **svZCHF** and **ixEDEL** across most pools create arbitrage layers: vault-rate drift, CHF/USD forex, multi-currency FX, wrapped-asset (gold, BTC), cross-pool price, and external DEX flow.

### Miliarium Aureum benefits

**1. CCB emission multiplier.** Miliarium pools are the only pools eligible for the automatic CCB multiplier (see [Theoretical foundations (§vii)](03_theoretical_foundation.md) and [Protocol formulas (F-8)](11_formulas.md); for numeric bounds, see [Constitution (§xxix)](10_constitution.md)).

**2. der Bodensee Pool revenue routing.** **Protocol-captured** fee revenue — **swap fees on non–der Bodensee pools (100%)** plus **ERC-4626 yield fees (100% of the 10% skim)** — flows into der Bodensee Pool as one-sided stablecoin (sUSDS/svZCHF) inflows, deepening the autonomous reserve. **Swap fees on trades inside der Bodensee Pool** (0.75%) accrue **in pool** to der Bodensee LPs — see [Tokenomics (§x — Value capture)](04_tokenomics.md).

**Permanent slots.** The 28 slots never decrease. If a pool underperforms due to sector rotation, the CCB emission multiplier boosts it automatically (anticyclical by design). If specific tokens within a pool lack on-chain volume or cease to exist, any AuMT holder can initiate a **Miliarium Aureum Composition Challenge**. Pool composition is immutable on-chain, so the challenge follows a deprecate-and-replace path: old gauge revoked, replacement pool launched into the same slot via the standard bootstrap path (gauge proposal, vote, 90-day boost). Like-for-like means same sector, same risk, same template role ([Bootstrap (§xxiv)](08_bootstrap.md) for worked examples; [Constitution (§xxvii)](10_constitution.md) for the binding rule).

**Beyond the 28.** The Miliarium pools are a curated blueprint, not the full economy. Missing a token or asset class? New permissionless pool and a gauge vote — not a composition challenge. [Bootstrap](08_bootstrap.md) §xxi covers gauge approval mechanics.

### Pool profiles

Each Miliarium pool has one profile: **`miliarium_profiles/NN_ixCanonicalName.md`** (slot `NN` = first column in Section xi). In the site UI: **Miliarium ▾** → **Manifest** (full registry table), **Sectors** (taxonomy), **Registry** (this document). Links: [manifest](06_miliarium_manifest.md) · [sector taxonomy](07_miliarium_sectors.md). **This document is canonical** for slot order, pool names, compositions, and stock subclasses.

---

## xii. der Bodensee Pool (not a Miliarium slot)

The **28** Miliarium pools in **Section xi** are the full **Miliarium Aureum** founding set. **AuMM** is separate — the **reward token**, not a numbered ix slot.

**der Bodensee Pool** — autonomous reserve and AuMM trading venue. **Three-token weighted pool** (**AuMM / sUSDS / svZCHF**) with **fixed weights 40% / 30% / 30%**, immutable from block 0. **Protocol-captured** fee revenue from **other** pools (swap fees + ERC-4626 yield fees) flows one-sided into the stablecoin side (sUSDS/svZCHF). **Swap fee inside der Bodensee:** **0.75%**, **100%** retained **in pool** for der Bodensee LPs. **60%** of pool TVL (sUSDS + svZCHF) earns native ERC-4626 vault yield. **Hidden from UI Months 0–6**; visible and tradeable from Month 6 onward. **Not emission-eligible** — AuMM cannot sit in an emission-eligible pool. Not one of the immutable ix pools above.

**Emissions:** **Months 1–10**, der Bodensee receives a **piecewise-linear decaying one-sided AuMM bootstrap** (**80% → 50%** by end of Month 6, then **50% → 0%** by end of Month 10; see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)). **After Month 10**, the bootstrap channel is **permanently zero** — der Bodensee never receives AuMM via emission again. **AuMM** is also **minted** to LPs of the **28** Miliarium pools (and gauge-eligible pools per **[Bootstrap](08_bootstrap.md)**) from the **LP emission tranche**. der Bodensee LPs earn **swap fees** (0.75% tier, in-pool) on their liquidity but do **not** receive the per-block **LP-tranche** stream (that accrues to the 28 + gauges).

| Concept | What it is |
|:--------|:-----------|
| **AuMM (token)** | Emission, halving, and fee routing — **[Tokenomics](04_tokenomics.md)**. |
| **der Bodensee Pool** | AuMM/sUSDS/svZCHF weighted pool with fixed 40/30/30 composition; autonomous reserve; **Months 1–10** one-sided AuMM bootstrap (piecewise decay); **after Month 10**, no AuMM via emission to this pool. |

**Summary:** **Section xi** = locked founding pools and LP-tranche emission destinations. **[Tokenomics](04_tokenomics.md)** = AuMM the asset. This section = **der Bodensee Pool** vs the **28** Miliarium pools.

---

See [Immutable Parameters (§xxix)](10_constitution.md).
