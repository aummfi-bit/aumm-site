# The Miliarium Aureum

The 28 pools are pre-defined at launch and locked from block 0. No open slots.

### Scope

- There are **28** immutable Miliarium Aureum pools (the founding constellation).
- Through **end of Month 10**, emissions are **equal** (1/28 each). **Months 11–12** blend **linearly** from equal to CCB (see `constitution.md`). **After Year 1**, allocation is **pure CCB** (EMA TVL × MAMAR × Incendiary).

### AuMM vs the 28 pools

**AuMM** is the reward **token** (`tokenomics.md`), not a Miliarium slot. The **AuMM / svZCHF · sUSDS** trading layer is at the end of this file — **Section xii** (no emissions to that pool).

### Canonical registry

The registry tables in Section xi are the binding list of pools and compositions (one ordered list **01–28**, split by sector for readability). Emission allocation is not vote-controlled; governance applies only to non-emission actions (see `constitution.md`, `bootstrap.md`).

---

## xi. Registry and structure

**Pool count:** **28** pools = **slots 01–28** (one pool per slot), fixed at launch.

The registry below is **one ordered list** (01 → 28). It is **split into separate tables by sector** only for readability; rows, weights, and names are unchanged from the full sequence. **Standard** pools follow **52% / 16% / 32%** (two ERC-4626 yield cores, ixEDEL anchor, two theme assets) unless noted. **Connector** pools **05 (ixEdelweiss), 06 (ixLibertas), 07 (ixCambio)** use non-standard compositions. **Slot 11 (ixLongus)** uses a **non-standard** single theme at **32%** (TLTon). **Slot 01 (ixHelvetia)** is Frankencoin MMA (**no ixEDEL**). **Slot 06 (ixLibertas)** is the USD stable hub (**no ixEDEL**).

### Standardised pool template (where applicable)

| Component | Weight | Role |
|-----------|--------|------|
| Yield Core (2 ERC-4626 tokens) | 52% (26% + 26%) | Meets 4626 Quality Gate. Generates protocol yield fees from block one. |
| Routing Anchor (ixEDEL) | 16% | Cross-pool arbitrage. Constellation routing connectivity. |
| Theme Assets (2 tokens) | 32% (16% + 16%) | Sector exposure. Drives aggregator volume from external markets. |

In the sector tables below, each pool’s weights are shown in three columns — **Yield core**, **Routing** (ixEDEL where used), and **Theme** — with *ticker* then *%*. Use **—** when that bucket has no weight (e.g. no ixEDEL in ixHelvetia / ixLibertas). Non-standard pools may combine multiple tokens in one column or use a single theme leg (see ixLongus). The Yield table uses HTML so **slots 01 and 06** can merge **Yield core + Routing + Theme** into one cell when routing and theme are empty, and **slot 05** can merge **Routing + Theme** into a single cell for **ixEDEL** (price-discovery / routing + theme).

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

With shared **svZCHF** and **ixEDEL** across most pools, arbitrage layers include vault-rate drift, CHF/USD forex, multi-currency FX, wrapped-asset (e.g. gold, BTC), cross-pool price, and external DEX flow.

### Miliarium Aureum benefits

**1. MAMAR emission multiplier.** Miliarium Aureum pools are the only pools eligible for the automatic MAMAR multiplier [0.75–1.25] (see **MAMAR Specification**).

**2. Treasury liquidity deposits.** Revenue from treasury AuMM sales during the price ceiling stabilization is deposited as permanent locked liquidity into Miliarium Aureum pools meeting the 4626 Quality Gate and $10K+ TVL. The treasury can never withdraw.

**Permanent slots.** The 28 Miliarium Aureum slots are permanent protocol infrastructure — the number never decreases. If a pool underperforms due to sector rotation, the MAMAR emission multiplier boosts it automatically (anticyclical by design). If specific tokens within a pool lack on-chain volume or cease to exist, any AuMT holder can initiate a **Miliarium Aureum Composition Challenge** to propose a new token composition that preserves the pool's function, sector theme, and template structure (see **Bootstrap Rules** and `constitution.md`).

### Pool profiles

Each immutable pool has one profile: **`miliarium_profiles/NN_ixCanonicalName.md`** (slot `NN` = first column in Section xi). In the site UI, open **Miliarium ▾** in the nav for **Manifest** (full registry table), **Sectors** (taxonomy), and **Registry** (this document). The same links work here: [manifest](miliarium_profiles/manifest.md) · [sector taxonomy](miliarium_profiles/sectors.md). **This document is canonical** for slot order, pool names, compositions, and stock subclasses.

---

## xii. AuMM pool (not a Miliarium slot)

The **28** pools in **Section xi** are the full **Miliarium Aureum** founding set. **AuMM** is separate: it is the **reward token**, not a numbered ix slot.

**AuMM trading pool** — AMM liquidity where **AuMM** trades against the protocol’s savings rails: **svZCHF** (Frankencoin savings vault) and **sUSDS** (Sky savings). Typical structure: **AuMM / svZCHF** and **AuMM / sUSDS** (or a routed graph that prices AuMM off both). This is **price discovery and swap depth** for the reward token; it is **not** one of the immutable ix pools above.

**Emissions:** The AuMM pool receives **no** protocol emissions. **AuMM** is what gets **minted** and **paid** to LPs of the **28** Miliarium pools (and gauge-eligible pools per **`bootstrap.md`**). LPs in the AuMM/svZCHF and AuMM/sUSDS venues earn **swap fees** only, **not** the per-block emission stream.

| Concept | What it is |
|:--------|:-----------|
| **AuMM (token)** | Emission, halving, and fee routing to buyback-and-burn — **`tokenomics.md`**. |
| **AuMM pool** | Trading against **svZCHF** and **sUSDS**; **no emissions** to this pool. |

**Summary:** Read **Section xi** for the **only** locked founding pools and emission destinations. Read **`tokenomics.md`** for **AuMM** the asset; this section defines the **AuMM / svZCHF · sUSDS** trading layer vs the **28** Miliarium pools.

---

See Immutable Parameters in `constitution.md`.
