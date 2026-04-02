# The Miliarium Aureum

The 28 pools are pre-defined at launch and locked from block 0. No open slots.

### Scope

- There are **28** immutable Miliarium Aureum pools (the founding constellation).
- During Year 1 they receive equal emissions (1/28 each).
- After Year 1 they compete under automatic CCB EMA(60) + PMAR rules.

### AuMM vs the 28 pools

**AuMM** is the reward **token** (`tokenomics.md`), not a Miliarium slot. The **AuMM / svZCHF · sUSDS** trading layer is at the end of this file — **Section II** (no emissions to that pool).

### Canonical registry

The registry tables in Section I are the binding list of pools and compositions (one ordered list **01–28**, split by sector for readability). Emission allocation is not vote-controlled; governance applies only to non-emission actions (see `constitution.md`, `bootstrap.md`).

---

## I — Registry and structure

**Pool count:** **28** pools = **slots 01–28** (one pool per slot), fixed at launch.

The registry below is **one ordered list** (01 → 28). It is **split into separate tables by sector** only for readability; rows, weights, and names are unchanged from the full sequence. **Standard** pools follow **52% / 16% / 32%** (two ERC-4626 yield cores, ixEDEL anchor, two theme assets) unless noted. **Connector** pools **05 (ixEdelweiss), 06 (ixLibertas), 07 (ixCambio)** use non-standard compositions. **Slot 11 (ixLongus)** uses a **non-standard** single theme at **32%** (TLTon). **Slot 01 (ixHelvetia)** is Frankencoin MMA (**no ixEDEL**). **Slot 06 (ixLibertas)** is the USD stable hub (**no ixEDEL**).

### Standardised pool template (where applicable)

| Component | Weight | Role |
|-----------|--------|------|
| Yield Core (2 ERC-4626 tokens) | 52% (26% + 26%) | Meets 4626 Quality Gate. Generates protocol yield fees from block one. |
| Routing Anchor (ixEDEL) | 16% | Cross-pool arbitrage. Constellation routing connectivity. |
| Theme Assets (2 tokens) | 32% (16% + 16%) | Sector exposure. Drives aggregator volume from external markets. |

### Yield — slots 01–07

Savings, staking / LST, FX, ixEDEL price-discovery venue, USD hub, and multi-currency FX connectors.

| Slot | Pool | Class | Subclass | Composition (summary) |
|:-----|:-----|:------|:---------|:------------------------|
| 01 | **ixHelvetia** | Yield | — | 80% svZCHF / 20% sUSDS |
| 02 | **ixAetheron** | Yield | — | 27% waEthrETH / 27% waEthweETH / 15% ixEDEL / 15% RPL / 16% ETHFI |
| 03 | **ixCasper** | Yield | — | 26% fWSTETH / 26% fWETH / 16% ixEDEL / 16% svZCHF / 16% waEthwstETH |
| 04 | **ixViatica** | Yield | — | 26% svZCHF / 26% GHO / 16% ixEDEL / 16% fBRZ / 16% st-EURA |
| 05 | **ixEdelweiss** | Yield | — | 46% ixEDEL · 18% waEthUSDC · 18% waEthUSDT · 18% svZCHF |
| 06 | **ixLibertas** | Yield | — | 15% scrvUSD · 15% PYUSD · 14% GHO · 14% sUSDS · 14% sfrxUSD · 14% USDT · 14% USDC |
| 07 | **ixCambio** | Yield | — | 20% ixEDEL · 16% svZCHF · 16% st-EURA · 16% aEURS · 16% s-tGBP · 16% [Partner Stable] |

### Bonds — slots 08–11

US fixed-income sleeves (short / HY / core+TIPS / long Treasury), placed after yield and before crypto in slot order.

| Slot | Pool | Class | Subclass | Composition (summary) |
|:-----|:-----|:------|:---------|:------------------------|
| 08 | **ixBrevis** | Bonds | — | 26% svZCHF / 26% waEthUSDC / 16% ixEDEL / 16% SGOVon / 16% SHYon |
| 09 | **ixAltrix** | Bonds | — | 26% svZCHF / 26% waEthUSDC / 16% ixEDEL / 16% HYGon / 16% FLHYon |
| 10 | **ixMediox** | Bonds | — | 26% svZCHF / 26% waEthUSDC / 16% ixEDEL / 16% AGGon / 16% TIPon |
| 11 | **ixLongus** | Bonds | — | 26% svZCHF / 26% waEthUSDC / 16% ixEDEL / 32% TLTon (non-standard) |

### Crypto-native governance & protocols — slots 12–16

DeFi infrastructure, wrapped BTC, and lending / ecosystem governance tokens.

| Slot | Pool | Class | Subclass | Composition (summary) |
|:-----|:-----|:------|:---------|:------------------------|
| 12 | **ixStrata** | Crypto | — | 26% svZCHF / 26% waEthUSDC / 16% ixEDEL / 16% LINK / 16% AAVE |
| 13 | **ixForum** | Crypto | — | 26% svZCHF / 26% waEthUSDT / 16% ixEDEL / 16% SKY / 16% LDO |
| 14 | **ixAurebit** | Crypto | — | 26% svZCHF / 26% GHO / 16% ixEDEL / 16% WBTC / 16% cbBTC |
| 15 | **ixRegistrum** | Crypto | — | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% ETHPLUS / 16% OPEN |
| 16 | **ixDebitum** | Crypto | — | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% Morpho / 16% SPK |

### Stocks — slots 17–26

Tokenised equities; **Subclass** narrows the sleeve (ETF vs index vs mega-cap vs sector).

| Slot | Pool | Class | Subclass | Composition (summary) |
|:-----|:-----|:------|:---------|:------------------------|
| 17 | **ixEquitix** | Stocks | Broad ETF | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% SPYon / 16% IVVon |
| 18 | **ixInnovix** | Stocks | Tech index | 26% svZCHF / 26% waEthUSDC / 16% ixEDEL / 16% QQQon / 16% QQQX |
| 19 | **ixGigantus** | Stocks | Mega-cap tech | 26% svZCHF / 26% waEthUSDT / 16% ixEDEL / 16% NVDAon / 16% TSLAon |
| 20 | **ixMagnix** | Stocks | Mega-cap tech | 26% svZCHF / 26% sfrxUSD / 16% ixEDEL / 16% MSFTon / 16% AAPLon |
| 21 | **ixNubix** | Stocks | Mega-cap tech | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% GOOGLon / 16% AMZNon |
| 22 | **ixMoneta** | Stocks | Financials | 26% svZCHF / 26% GHO / 16% ixEDEL / 16% JPMon / 16% GSon |
| 23 | **ixColossix** | Stocks | Financials | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% BLKon / 16% BACon |
| 24 | **ixVitalix** | Stocks | Healthcare | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% LLYon / 16% NVOon |
| 25 | **ixMedicix** | Stocks | Healthcare | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% JNJon / 16% ABBVon |
| 26 | **ixMercatura** | Stocks | Fintech | 26% svZCHF / 26% sUSDS / 16% ixEDEL / 16% COIN / 16% HOOD |

### Metals — slots 27–28

Physical gold vs silver / uranium ETF themes.

| Slot | Pool | Class | Subclass | Composition (summary) |
|:-----|:-----|:------|:---------|:------------------------|
| 27 | **ixAurix** | Metals | — | 26% svZCHF / 26% sfrxUSD / 16% ixEDEL / 16% PAXG / 16% XAUt |
| 28 | **ixMetallum** | Metals | — | 26% svZCHF / 26% waEthUSDT / 16% ixEDEL / 16% SLVon / 16% URAon |

---

### Cross-pool arbitrage

With shared **svZCHF** and **ixEDEL** across most pools, arbitrage layers include vault-rate drift, CHF/USD forex, multi-currency FX, wrapped-asset (e.g. gold, BTC), cross-pool price, and external DEX flow.

### Miliarium Aureum benefits

**1. PMAR emission multiplier.** Miliarium Aureum pools are the only pools eligible for the automatic PMAR multiplier [0.75–1.25] (see **PMAR Specification**).

**2. Treasury liquidity deposits.** Revenue from treasury AuMM sales during the price ceiling stabilization is deposited as permanent locked liquidity into Miliarium Aureum pools meeting the 4626 Quality Gate and $10K+ TVL. The treasury can never withdraw.

**Permanent slots.** The 28 Miliarium Aureum slots are permanent protocol infrastructure — the number never decreases. If a pool underperforms due to sector rotation, the PMAR emission multiplier boosts it automatically (anticyclical by design). If specific tokens within a pool lack on-chain volume or cease to exist, any AuMT holder can initiate a **Miliarium Aureum Composition Challenge** to propose a new token composition that preserves the pool's function, sector theme, and template structure (see **Bootstrap Rules** and `constitution.md`).

### Pool profiles

Each immutable pool has one profile: **`miliarium_profiles/NN_ixCanonicalName.md`** (slot `NN` = first column in Section I). In the site UI, open **Miliarium ▾** in the nav for **Manifest** (full registry table), **Sectors** (taxonomy), and **Registry** (this document). The same links work here: [manifest](miliarium_profiles/manifest.md) · [sector taxonomy](miliarium_profiles/sectors.md). **This document is canonical** for slot order, pool names, compositions, and stock subclasses.

---

## II — AuMM pool (not a Miliarium slot)

The **28** pools in **Section I** are the full **Miliarium Aureum** founding set. **AuMM** is separate: it is the **reward token**, not a numbered ix slot.

**AuMM trading pool** — AMM liquidity where **AuMM** trades against the protocol’s savings rails: **svZCHF** (Frankencoin savings vault) and **sUSDS** (Sky savings). Typical structure: **AuMM / svZCHF** and **AuMM / sUSDS** (or a routed graph that prices AuMM off both). This is **price discovery and swap depth** for the reward token; it is **not** one of the immutable ix pools above.

**Emissions:** The AuMM pool receives **no** protocol emissions. **AuMM** is what gets **minted** and **paid** to LPs of the **28** Miliarium pools (and gauge-eligible pools per **`bootstrap.md`**). LPs in the AuMM/svZCHF and AuMM/sUSDS venues earn **swap fees** only, **not** the per-block emission stream.

| Concept | What it is |
|:--------|:-----------|
| **AuMM (token)** | Emission, halving, and fee routing to buyback-and-burn — **`tokenomics.md`**. |
| **AuMM pool** | Trading against **svZCHF** and **sUSDS**; **no emissions** to this pool. |

**Summary:** Read **Section I** for the **only** locked founding pools and emission destinations. Read **`tokenomics.md`** for **AuMM** the asset; this section defines the **AuMM / svZCHF · sUSDS** trading layer vs the **28** Miliarium pools.

---

See Immutable Parameters in `constitution.md`.
