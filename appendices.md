## Appendix I — Why Fair Launch AMMs Failed — And Why Aureum Won't

### The Fair Launch Graveyard

Fair launches were the gold standard in 2020 (Yearn, SushiSwap). Today they're nearly extinct. The reasons are structural:

**The Bootstrap Paradox.** An AMM needs liquidity to be useful. VC-backed projects pay for liquidity mining from their war chest. Fair launches have no war chest. No liquidity → high slippage → no traders → no fees → LPs leave → death spiral.

**The Builder Burnout Problem.** If 100% of tokens go to the community, who pays for audits ($100-250K), legal counsel, infrastructure, and the dev's rent? Most fair launch founders end up working for free while yield farmers dump their tokens for profit.

**Governance Capture.** Fair launches distribute tokens based on liquidity provision. Whales bring massive capital on day one, earn the majority of "fair" tokens, and vote to redirect the treasury to themselves. A "Fair Launch" becomes a "Whale Launch."

**The Death Spiral.** Most AMMs rely on their own token as the incentive. Token price drops → APR drops → LPs leave → protocol dies. VC-backed projects subsidise during bear markets using their treasury. Fair launches have no cushion.

### The SushiSwap Autopsy

SushiSwap is the most instructive failure. Three specific causes:

**1. The backdoor.** Chef Nomi controlled the dev fund and sold $14M of SUSHI. The "fair launch" had admin keys hidden in the migration contract. The founder had a sell button the community didn't know about.

**2. Vampire attack dependency.** SushiSwap's entire TVL came from migrating Uniswap LPs through token incentives. Once incentives declined, LPs had no structural reason to stay. The liquidity was rented, not earned.

**3. Immediate governance capture.** Large holders (FTX/Alameda) accumulated governance power through token purchases and directed treasury spending to their own interests. Token-weighted voting meant capital = control.

The deeper structural failure: SushiSwap was a fair launch of a **commodity product** — same Uniswap V2 pairs, same architecture, nothing novel. When incentives faded, there was no reason to use Sushi over Uniswap. The token was the only differentiator, and the token was losing value.

### How Aureum Addresses Every Failure Mode

| Failure Mode | What Killed Them | Aureum's Fix |
|-------------|-----------------|-------------|
| **Bootstrap Paradox** | No capital to seed liquidity | Founding team seeds pools with existing assets (ixEDEL, svZCHF). ERC-4626 pools generate 2-2.8% native yield from day one — LPs have a reason to stay before any AuMM emission has value. |
| **Builder Burnout** | Devs work for free, farmers dump | Founding team earns AuMM by being early LPs — the highest emission rate goes to the first providers. Treasury funded by protocol fees (25% swap + 75% yield), not by token sales. Audit costs funded by treasury once fees accumulate. |
| **Chef Nomi Backdoor** | Founder controls dev fund, sells | No admin keys. No migration contract. The treasury receives a declining share of emissions (75%→50%→0% over months 0–10) for seeding the AuMM trading pool and operating a price ceiling that converts overvaluation into pool depth. Deployed at a governance-voted multiple, capped at 80% of treasury assets. Excess AuMM serves as stabilization inventory (months 6–10), then burned at month 10. Treasury emission share hits zero permanently at month 10. All mechanisms immutable in contract. No human can change the supply curve or the stabilization rules. |
| **Vampire Attack Dependency** | Liquidity rented via incentives, leaves when APR drops | Constituent tokens (WBTC, cbBTC, PAXG, XAUt, sfrxUSD, stEURA, AAVE, LINK) trade $898M+ daily. Aggregator routing creates organic volume independent of incentives. ERC-4626 native yield provides floor return even at zero emissions. LPs have structural reasons to stay. |
| **Governance Capture** | Token-weighted voting = capital buys control | Protocol governance is AuMT-weighted — but only AuMT from emission-qualified pools counts. You cannot buy governance power on the open market. You must be providing liquidity to productive pools that meet every anti-gaming criterion. Phased dampening: fourth root in Era 1 (maximum compression at low TVL), cube root post-first-halving (TVL growth has naturally decentralised power). |
| **Death Spiral** | Token price drops → APR drops → LPs leave | Dual revenue streams: swap fees + ERC-4626 yield fees. Yield fees accrue regardless of AuMM price or trading volume. Buyback-and-burn creates deflationary pressure that partially offsets price declines. BTC halving schedule means emissions decline predictably — the market prices the full curve from day one. |
| **Commodity Product** | No architectural moat → users leave when incentives fade | Multi-asset weighted pools, ERC-4626 native yield, hooks, constellation routing — these pool designs cannot exist on Uniswap, Curve, or Aerodrome. The moat is the architecture, not the token. LPs stay because no other venue offers the same capital efficiency. |

### The White Space

There are no Fair Launch AMMs in 2026 because most people assume the model can't work. They're right — for commodity products with no structural moat and no native yield.

Aureum is different because it launches with three things no previous fair launch had:

1. **A differentiated architecture** that cannot be replicated on any competing AMM
2. **Native yield** (ERC-4626) that provides LP returns independent of token emissions
3. **A pre-built routing topology** (Miliarium Aureum) with $898M daily volume opportunity from constituent tokens already trading on-chain

The fair launch model failed when applied to commodity AMMs. It has never been tried on a formally verified, multi-asset, yield-bearing routing infrastructure with BTC-scarcity tokenomics and contract-enforced anti-gaming.

That experiment hasn't failed. It hasn't happened.

---

## Appendix II — Yield Basis Hybrid Vaults — Complementary Architecture

Curve's Yield Basis protocol (March 2026) independently validated the same core thesis Aureum is built on: sustainable AMM growth requires tying TVL expansion to productive capital, not reflexive incentives. Their Hybrid Vaults solve this by requiring LPs to deposit crvUSD (earning ~4.5% scrvUSD yield) before unlocking BTC/ETH pool capacity — directly supporting the crvUSD peg while scaling. The mechanism is architecturally orthogonal to Aureum's CCB: Yield Basis enforces anticyclicality at the user level (stable-first deposit → personal cap), while Aureum enforces it at the protocol level (EMA-weighted emissions + immutable anti-gaming gates + 52% ERC-4626 Quality Gate). Both reject reflexive liquidity mining. Both force conviction capital upfront. The key divergence: Yield Basis depends on an external stablecoin peg (crvUSD + Curve DAO credit line), while Aureum's stability layer is entirely internal and oracle-free. Aureum's routing anchor (ixEDEL) has no peg to defend — its NAV arb surface generates continuous cross-pool fees without the catastrophic depeg risk that Hybrid Vaults were specifically engineered to mitigate. The two designs compose well: a future gauge-approved Aureum pool could include scrvUSD as an ERC-4626 component if it meets the $5M vault floor, giving LPs access to both yield layers simultaneously. Source: [@yieldbasis, March 30 2026](https://x.com/yieldbasis/status/2038610652194037966).

---

*This document is confidential and intended for founding team discussion only. Do not distribute.*
