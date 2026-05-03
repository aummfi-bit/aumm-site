<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a 07a_tokens.md — DO NOT EDIT -->
# Token inventory — Miliarium Aureum

*Deduplicated list of every token in the **28** Miliarium Aureum pools ([registry Section xi](05_miliarium_aureum.md)). **svZCHF** and **ixEDEL** are the **dual universal connectors** — both present in **26 of 28** Miliarium pools as cross-pool routing rails (svZCHF the deeper / primary at typically 26% as yield core, ixEDEL the secondary / arb-extraction layer at 16% as routing anchor). svZCHF additionally anchors the autonomous reserve (der Bodensee, governance deposits, Incendiary boosts, fee inflows). See [Mental model (§iii — Dual anchors)](02_mental_model.md). **Pool name(s)** for those two anchors left blank here. **Tokenised vault** holds pool / vault contract addresses (e.g. Balancer V3) where relevant; more entries as wired. Ethereum addresses, rate providers, and vaults are deployment-specific; blank until wired on-chain.*

| Token name | Ticker | Token type | Ethereum address | Rate providers | Tokenised vault | Tokenised vaults / notes | Pool name(s) |
|:-----------|:-------|:-----------|:-------------------|:---------------|:----------------|:---------------------------|:-------------|
| Aave (lending protocol governance) | AAVE | ERC-20 | 0x7Fc66500c84A76Ad7e9c93437bfc5ac33e2DDaE9 | | 0x1E9ea34eaB5e4EDDAb4170047232F296746F8b00 | Aave governance; Balancer NeoFi 6 | ixStrata |
| iShares Core US Aggregate Bond ETF (on-chain) | AGGon | ERC-20 | 0xfF7CF16aA2fFc463b996DB2f7B7cf0130336899D | | | Backed / tokenised ETF wrapper | ixMediox |
| Aave-wrapped EURS (Stasis Euro) | aEURS | ERC-4626 | | | | Stasis EURS underlying `0xdB25f211ab05B1C97d595516F45794528a807ad8`; Aave stata EURS on Ethereum mainnet not in [Aave address book](https://github.com/bgd-labs/aave-address-book) — verify when listed | ixCambio |
| Amazon (on-chain) | AMZNon | ERC-20 | 0xbb8774FB97436d23d74C1b882E8E9A69322cFD31 | | | Tokenised equity | ixNubix |
| Apple (on-chain) | AAPLon | ERC-20 | 0x14c3abF95Cb9C93a8b82C1CdCB76D72Cb87b2d4c | | | Tokenised equity | ixMagnix |
| AbbVie (on-chain) | ABBVon | ERC-20 | 0x7c7378143a9c8839e0502e2178F058F46c6ea504 | | | Tokenised equity | ixMedicix |
| Bank of America (on-chain) | BACon | ERC-20 | 0x576E9CA70e3a040c00d8139b0665a2b7b7B64844 | | | Tokenised equity | ixColossix |
| BlackRock (on-chain) | BLKon | ERC-20 | 0x7a0F89c1606f71499950AA2590d547c3975B728E | | | Tokenised equity | ixColossix |
| Coinbase Wrapped BTC | cbBTC | ERC-20 | 0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf | | | Coinbase custody BTC | ixAurebit |
| Coinbase (on-chain) | COIN | ERC-20 | 0xF042cfa86cf1D598a75Bdb55c3507a1F39f9493b | | | Tokenised equity | ixMercatura |
| Ether.fi governance token | ETHFI | ERC-20 | 0xFe0c30065B384F05761f15d0CC899D4F9F9Cc0eB | | 0x1E9ea34eaB5e4EDDAb4170047232F296746F8b00 | EtherFi; Balancer NeoFi 6 | ixAetheron |
| Reserve Protocol ETH+ (yield-bearing ETH basket) | ETHPLUS | ERC-20 | 0xE72B141DF173b999AE7c1aDcbF60Cc9833Ce56a8 | | | Reserve DTF | ixRegistrum |
| iShares Fallen Angels High Yield Bond ETF (on-chain) | FLHYon | ERC-20 | 0x54C1Ff361b402f66c13107421E6A431C3375EF24 | | | Tokenised ETF | ixAltrix |
| Flux BRZ (Brazilian Real stable) | fBRZ | ERC-20 | | | | [Flux docs](https://docs.fluxfinance.com/addresses) list no fBRZ; BRZ underlying e.g. `0x01d33fd36ec67c6ada32cf36b31e88ee190b1839` | ixViatica |
| Fluid Wrapped Ether | fWETH | ERC-4626 | 0x90551c1795392094FE6D29B758EcCD233cFAa260 | [fWETH rate provider](https://etherscan.io/address/0x8fC43e76874CaE40939eDeB90E5683258B63c508) | 0x90551c1795392094FE6D29B758EcCD233cFAa260 | Fluid → WETH; pool ([Etherscan](https://etherscan.io/address/0xb18fA0cb5DE8cecB8899AAE6e38b1B7ed77885dA)) | ixCasper |
| Fluid Wrapped liquid staked Ether 2.0 | fWSTETH | ERC-4626 | 0x2411802D8BEA09be0aF8fD8D08314a63e706b29C | [fWSTETH rate provider](https://etherscan.io/address/0x8Be2e3D4b85d05cac2dBbAC6c42798fb342aef45) | 0x2411802D8BEA09be0aF8fD8D08314a63e706b29C | Fluid → Lido wstETH; pool ([Etherscan](https://etherscan.io/address/0xb18fA0cb5DE8cecB8899AAE6e38b1B7ed77885dA)) | ixCasper |
| Aave GHO | GHO | ERC-4626 | 0xC71Ea051a5F82c67ADcF634c36FFE6334793D24C | [GHO rate provider](https://etherscan.io/address/0x851b73c4BFd5275D47FFf082F9e8B4997dCCB253) | 0xC71Ea051a5F82c67ADcF634c36FFE6334793D24C | Aave GHO ↔ Aave Prime GHO (Balancer V3 atomic wrap); yield-bearing where deployed | ixViatica, ixLibertas, ixAurebit, ixMoneta |
| Alphabet / Google (on-chain) | GOOGLon | ERC-20 | 0xbA47214eDd2bb43099611b208f75E4b42FDcfEDc | | | Tokenised equity | ixNubix |
| Goldman Sachs (on-chain) | GSon | ERC-20 | 0xdB57d9C14e357Fc01E49035a808779Df41E9B4e2 | | | Tokenised equity | ixMoneta |
| iShares iBoxx High Yield Corporate Bond ETF (on-chain) | HYGon | ERC-20 | 0xeD3618Bb8778F8eBBe2f241Da532227591771D04 | | | Tokenised ETF | ixAltrix |
| Robinhood (on-chain) | HOOD | ERC-20 | 0x998f02A9E343EF6E3E6f28700d5A20F839fD74E6 | | | Tokenised equity | ixMercatura |
| iShares Core S&P 500 ETF (on-chain) | IVVon | ERC-20 | 0x62cA254a363dc3c748e7E955c20447aB5bF06fF7 | | | Tokenised ETF | ixEquitix |
| Reserve Protocol DTF (routing basket) | ixEDEL | ERC-20 (DTF) | 0xe4a10951f962e6cB93Cb843a4ef05d2F99DB1F94 | | | Reserve Protocol — ixEDEL basket | |
| JPMorgan Chase (on-chain) | JPMon | ERC-20 | 0x03C1EC4CA9DBb168E6Db0DeF827c085999CBffaF | | | Tokenised equity | ixMoneta |
| Johnson & Johnson (on-chain) | JNJon | ERC-20 | 0xdd0E1e6162666a210905fFE8d368661B313c00e9 | | | Tokenised equity | ixMedicix |
| Lido DAO Token | LDO | ERC-20 | 0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32 | | | Lido DAO | ixForum |
| ChainLink Token | LINK | ERC-20 | 0x514910771AF9Ca656af840dff83E8264EcF986CA | | | Chainlink | ixStrata |
| Eli Lilly (on-chain) | LLYon | ERC-20 | 0xf192957AE52dB3eb088654403CC2eDeD014ae556 | | | Tokenised equity | ixVitalix |
| Morpho | Morpho | ERC-20 | 0x58D97B57BB95320F9a05dC918Aef65434969c2B2 | | 0x1E9ea34eaB5e4EDDAb4170047232F296746F8b00 | Morpho protocol; Balancer NeoFi 6 | ixDebitum |
| Microsoft (on-chain) | MSFTon | ERC-20 | 0xB812837b81a3a6b81d7CD74CfB19A7f2784555E5 | | | Tokenised equity | ixMagnix |
| NVIDIA (on-chain) | NVDAon | ERC-20 | 0x2D1F7226Bd1F780AF6B9A49DCC0aE00E8Df4bDEE | | | Tokenised equity | ixGigantus |
| Novo Nordisk (on-chain) | NVOon | ERC-20 | 0x28151F5888833D3d767C4d6945a0Ee50D1B193E3 | | | Tokenised equity | ixVitalix |
| Reserve Protocol OPEN (governance DTF) | OPEN | ERC-20 | 0x323c03c48660fE31186fa82c289b0766d331Ce21 | | | Reserve governance token | ixRegistrum |
| PAX Gold (Paxos) | PAXG | ERC-20 | 0x45804880De22913dAFE09f4980848ECE6EcbAf78 | | | Gold-backed | ixAurix |
| PayPal USD | PYUSD | ERC-20 | 0xb51EDdDD8c47856D81C8681EA71404Cec93E92c6 | [Aave Core PYUSD rate provider](https://etherscan.io/address/0xdd8AEBC13B3DFaF85e3B512d26681987aD2c43b2) | 0xb51EDdDD8c47856D81C8681EA71404Cec93E92c6 | PayPal USD; Aave Core PYUSD | ixLibertas |
| Pendle | PENDLE | ERC-20 | 0x808507121B80c02388fAd14726482e061B8da827 | | 0x1E9ea34eaB5e4EDDAb4170047232F296746F8b00 | Pendle; Balancer NeoFi 6 | |
| Invesco QQQ (on-chain) | QQQon | ERC-20 | 0x0e397938C1Aa0680954093495B70A9F5e2249aBa | | | Tokenised ETF | ixInnovix |
| Nasdaq xStock (QQQx) | QQQX | ERC-20 | 0xa753A7395cAe905Cd615Da0B82A53E0560f250af | | | xStock tokenised index; [CoinGecko — Nasdaq xStock](https://www.coingecko.com/en/coins/nasdaq-xstock) | ixInnovix |
| Rocket Pool Protocol | RPL | ERC-20 | 0xD33526068D116cE69F19A9ee46F0bd304F21A51f | | | Rocket Pool | ixAetheron |
| Frax USD | frxUSD | ERC-20 | 0xCAcd6fd266aF91b8AeD52aCCc382b4e165586E29 | | 0x4d968a5Db8dA0822A2F08840f553De4129aAe5F3 | Stake → **sfrxUSD** (Frax USD savings, ERC-4626, row below); Curve frxUSD–scrvUSD pool ([Curve deposit](https://www.curve.finance/dex/ethereum/pools/0x4d968a5db8da0822a2f08840f553de4129aae5f3/deposit)) | ixLibertas |
| Frax USD savings | sfrxUSD | ERC-4626 | 0xcf62F905562626CfcDD2261162a51fd02Fc9c5b6 | [sfrxUSD (Etherscan)](https://etherscan.io/token/0xcf62F905562626CfcDD2261162a51fd02Fc9c5b6) | 0xcf62F905562626CfcDD2261162a51fd02Fc9c5b6 | Frax staked frxUSD (ERC-4626); [docs](https://docs.frax.com/frxusd/stake-and-unstake-quickstart-ethereum) | ixLibertas, ixMagnix, ixAurix |
| Curve savings crvUSD | scrvUSD | ERC-4626 | 0x0655977FEb2f289A4aB78af67BAB0d17aAb84367 | | 0x4d968a5Db8dA0822A2F08840f553De4129aAe5F3 | Curve savings vault; frxUSD–scrvUSD pool ([Curve deposit](https://www.curve.finance/dex/ethereum/pools/0x4d968a5db8da0822a2f08840f553de4129aae5f3/deposit)) | ixLibertas |
| iShares 0–3 Month Treasury Bond ETF (on-chain) | SGOVon | ERC-20 | 0x8De5D49725550f7b318b2FA0f1B1F118E98E8D0F | | | Tokenised ETF | ixBrevis |
| iShares 1–3 Year Treasury Bond ETF (on-chain) | SHYon | ERC-20 | 0x5C424B9b60383FCE7fE7069D2a2B1047BCd04a73 | | | Tokenised ETF | ixBrevis |
| Sky (governance) | SKY | ERC-20 | 0x56072C95FAA701256059aa122697B133aDEd9279 | | 0x1E9ea34eaB5e4EDDAb4170047232F296746F8b00 | Sky; Balancer NeoFi 6 | ixForum |
| iShares Silver Trust (on-chain) | SLVon | ERC-20 | 0xF3e4872e6a4cF365888D93b6146a2bAA7348F1A4 | | | Tokenised ETF | ixMetallum |
| Spark | SPK | ERC-20 | 0xc20059e0317DE91738d13af027DfC4a50781b066 | | | Spark | ixDebitum |
| SPDR S&P 500 ETF (on-chain) | SPYon | ERC-20 | 0xFeDC5f4a6c38211c1338aa411018DFAf26612c08 | | | Tokenised ETF | ixEquitix |
| Syrup (Maple) | SYRUP | ERC-20 | 0x643C4E15d7d62Ad0aBeC4a9BD4b001aA3Ef52d66 | | 0x1E9ea34eaB5e4EDDAb4170047232F296746F8b00 | Maple Syrup; Balancer NeoFi 6 | |
| tGBP (tokenised GBP stablecoin) | tGBP | ERC-20 | 0x27f6c8289550fce67f6b50bed1f519966afe5287 | | | Tokenised GBP ([Etherscan](https://etherscan.io/token/0x27f6c8289550fce67f6b50bed1f519966afe5287)); tokenisedgbp.com | ixCambio |
| Staked EURA (Angle) | st-EURA | ERC-4626 | 0x004626A008B1aCdC4c74ab51644093b155e59A23 | [stEUR (Etherscan)](https://etherscan.io/address/0x004626A008B1aCdC4c74ab51644093b155e59A23) | 0x004626A008B1aCdC4c74ab51644093b155e59A23 | Angle stEUR (staked EURA); [CoinGecko — Angle Staked EURA](https://www.coingecko.com/en/coins/angle-staked-eura) | ixViatica, ixCambio |
| Savings USDS (Sky) | sUSDS | ERC-4626 | 0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD | [sUSDS rate provider](https://etherscan.io/address/0x1195be91e78ab25494c855826ff595eef784d47b) | 0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD | Sky savings rate vault | ixHelvetia, ixLibertas, ixRegistrum, ixDebitum, ixEquitix, ixNubix, ixColossix, ixVitalix, ixMedicix, ixMercatura |
| SavingsVault ZCHF (Frankencoin) | svZCHF | ERC-4626 | 0xE5F130253fF137f9917C0107659A4c5262abf6b0 | [svZCHF rate provider](https://etherscan.io/address/0xf32dc0ee2cc78dca2160bb4a9b614108f28b176c) | 0xE5F130253fF137f9917C0107659A4c5262abf6b0 | Frankencoin money market | |
| iShares TIPS Bond ETF (on-chain) | TIPon | ERC-20 | 0x2Df38cA485D01fC15e4FD85847ed26b7EF871c1c | | | Tokenised ETF | ixMediox |
| iShares 20+ Year Treasury Bond ETF (on-chain) | TLTon | ERC-20 | 0x992651BFeB9A0DCC4457610E284ba66D86489d4d | | | Tokenised ETF | ixLongus |
| Tesla (on-chain) | TSLAon | ERC-20 | 0xf6b1117ec07684D3958caD8BEb1b302bfD21103f | | | Tokenised equity | ixGigantus |
| USD Coin | USDC | ERC-20 | 0xD4fa2D31b7968E448877f69A96DE69f5de8cD23E | [waEthUSDC rate provider](https://etherscan.io/address/0x8f4E8439b970363648421C692dd897Fb9c0Bd1D9) | 0xD4fa2D31b7968E448877f69A96DE69f5de8cD23E | Circle; Wrapped Aave Ethereum USDC (waEthUSDC); Balancer V3 atomic wrap | ixLibertas |
| Tether USD | USDT | ERC-20 | 0x7Bc3485026Ac48b6cf9BaF0A377477Fff5703Af8 | [waEthUSDT rate provider](https://etherscan.io/address/0xEdf63cce4bA70cbE74064b7687882E71ebB0e988) | 0x7Bc3485026Ac48b6cf9BaF0A377477Fff5703Af8 | Tether; Balancer V3 atomic wrap ↔ waEthUSDT | ixLibertas |
| Wrapped Ether | WETH | ERC-20 | 0x0bfc9d54Fc184518A81162F8fB99c2eACa081202 | [waEthWETH rate provider](https://etherscan.io/address/0xBe7bE04807762Bc433911dD927fD54a385Fa91d6) | 0x0bfc9d54Fc184518A81162F8fB99c2eACa081202 | Wrapped Aave Ethereum WETH (waEthWETH); Balancer V3 atomic wrap | ixLibertas |
| Global X Uranium ETF (on-chain) | URAon | ERC-20 | 0xf98Ec282300892b3518B5cB996012b18d9B7D435 | | | Tokenised ETF | ixMetallum |
| Aave stataToken — Rocket Pool rETH | waEthrETH | ERC-4626 | 0xae78736Cd615f374D3085123A210448E74Fc6393 | [Rocket Pool ETH](https://etherscan.io/address/0x1a8F81c256aee9C640e14bB0453ce247ea0DFE6F) | | Aave V3 wrapper → rETH | ixAetheron |
| Aave stataToken — USDC | waEthUSDC | ERC-4626 | 0xD4fa2D31b7968E448877f69A96DE69f5de8cD23E | [waEthUSDC rate provider](https://etherscan.io/address/0x8f4E8439b970363648421C692dd897Fb9c0Bd1D9) | 0xD4fa2D31b7968E448877f69A96DE69f5de8cD23E | Wrapped Aave Ethereum USDC; Balancer V3 atomic wrap ↔ USDC | ixEdelweiss, ixBrevis, ixAltrix, ixMediox, ixLongus, ixStrata, ixInnovix |
| Aave stataToken — USDT | waEthUSDT | ERC-4626 | 0x7Bc3485026Ac48b6cf9BaF0A377477Fff5703Af8 | [waEthUSDT rate provider](https://etherscan.io/address/0xEdf63cce4bA70cbE74064b7687882E71ebB0e988) | 0x7Bc3485026Ac48b6cf9BaF0A377477Fff5703Af8 | Aave V3 wrapper → USDT; Balancer V3 atomic wrap ↔ USDT | ixEdelweiss, ixForum, ixGigantus, ixMetallum |
| Aave stataToken — WETH | waEthWETH | ERC-4626 | 0x0bfc9d54Fc184518A81162F8fB99c2eACa081202 | [waEthWETH rate provider](https://etherscan.io/address/0xBe7bE04807762Bc433911dD927fD54a385Fa91d6) | 0x0bfc9d54Fc184518A81162F8fB99c2eACa081202 | Wrapped Aave Ethereum WETH; Balancer V3 atomic wrap ↔ WETH | |
| Wrapped eETH | weETH | ERC-20 | 0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee | [weETH (Etherscan)](https://etherscan.io/address/0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee) | 0xBDbADc891BB95DEE80eBC491699228EF0f7D6fF1 | EtherFi weETH; Balancer pool hook | ixAetheron |
| Aave stataToken — EtherFi weETH | waEthweETH | ERC-4626 | 0x867b0CDC4B39a19945E616c29639b0390b39db3B | [weETH oracle (Aave)](https://etherscan.io/address/0x87625393534d5C102cADB66D37201dF24cc26d4C) | 0x867b0CDC4B39a19945E616c29639b0390b39db3B | Aave V3 Core `weETH_STATIC_A_TOKEN` → weETH; [Etherscan](https://etherscan.io/address/0x867b0CDC4B39a19945E616c29639b0390b39db3B) | ixAetheron |
| Wrapped liquid staked Ether 2.0 | wstETH | ERC-20 | 0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0 | | | Lido wstETH | ixCasper |
| Aave stataToken — Lido wstETH | waEthwstETH | ERC-4626 | 0x322AA5F5Be95644d6c36544B6c5061F072D16DF5 | [wstETH oracle (Aave)](https://etherscan.io/address/0xe1D97bF61901B075E9626c8A2340a7De385861Ef) | 0x322AA5F5Be95644d6c36544B6c5061F072D16DF5 | Aave V3 Core stataEthwstETH → wstETH; [Etherscan](https://etherscan.io/address/0x322AA5F5Be95644d6c36544B6c5061F072D16DF5). Aave **Lido** instance uses `0x775F661b0bD1739349b9A2A3EF60be277c5d2D29` instead | ixCasper |
| Wrapped BTC (BitGo) | WBTC | ERC-20 | 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599 | | | BitGo WBTC | ixAurebit |
| Tether Gold (XAUt) | XAUt | ERC-20 | 0x68749665FF8D2d112Fa859AA293F07A622782F38 | | | Gold token | ixAurix |
| JPY Coin (regulated Japanese yen stablecoin) | JPYC | ERC-20 | 0xE7C3D8C9a439feDe00D2600032D5dB0Be71C3c29 | | | Regulated JPY stablecoin (JPYC Inc., Japan PSA-licensed; backed 1:1 by JGBs and bank deposits) | ixCambio |

**Row count:** 71 unique tickers. **AuMM** is in **der Bodensee Pool** only — not a Miliarium slot ([Miliarium Aureum §xii](05_miliarium_aureum.md)).

See [Miliarium sectors](07_miliarium_sectors.md) · [Manifest](06_miliarium_manifest.md) · [Registry](05_miliarium_aureum.md).
