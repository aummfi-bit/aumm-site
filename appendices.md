# Appendices

## xxxvi. AMM Architecture: Aequilibrium

### Provenance: Balancer V3

Aequilibrium is derived from Balancer V3's open-source, Certora-verified smart contracts. The relationship is transparent: the pool layer is byte-identical to the audited code, the tokenomics layer is entirely new. The table below shows what was inherited and what was built.

| Component | Origin | Modifications |
|-----------|--------|--------------|
| Vault | Balancer V3 (Certora verified) | None |
| Weighted pools | Balancer V3 (Certora verified) | None |
| Stable pools | Balancer V3 (Certora verified) | None |
| Hooks (StableSurge etc.) | Balancer V3 (Certora verified) | None |
| ERC-4626 rate providers | Balancer V3 (Certora verified) | None |
| Smart Order Router | Balancer V3 | None |
| Gauge system | **Rewritten** | New emission logic, eligibility criteria, anti-gaming |
| Token contract | **New** | BTC-style emission schedule, immutable supply cap |
| Fee distributor | **New** | 50/50 swap fee split (LP/Bodensee) + 100% yield fee to Bodensee — all as one-sided svZCHF inflows |
| Governance | **New** | LP-weighted voting (AuMT for protocol governance), 90-day gauge boost, no ve-locking |

### What's Unchanged (Critical)

The pool contracts, vault, SOR, hooks, and rate providers are **byte-identical** to the Certora-verified Balancer V3 code. The audit and formal verification apply to these components. Only the tokenomics layer is new and requires independent audit.

This is important for LP trust: *"The AMM you're depositing into is the same formally verified code. The token you're earning is different."*

### What's New (Requires Audit)

- AuMM token contract (ERC-20 with immutable supply cap and halving logic)
- AuMT pool token wrapper (Aureum Market Tessera)
- CCB emission engine (60-day EMA calculator, CCB multiplier computation with slope-based adjustments and dead zone — see `constitution.md` §xxix for all numeric bounds)
- Incendiary Boost engine (AuMM escrow, 30-day emission streaming, efficiency scalar calculation, priority skim, renewal lock)
- 90-day gauge boost (1.2x fixed CCB multiplier for new gauges, automatic expiry)
- CCB multiplier engine (slope calculation, dead zone, step adjustments, clamp — all immutable; see `constitution.md` §xxix)
- Sandbox fast-track (top 10% efficiency sustained for 3 epochs, automatic gauge approval)
- Emission distributor (per-block streaming with halving logic, CCB-driven weight updates)
- Gauge eligibility checker (on-chain criteria enforcement, graduated grace period, volume percentile ranking, hysteresis buffer, efficiency tournament with 3-epoch smoothing, gauge revocation logic)
- Miliarium Aureum pool registry (28 pools, non-transferable, revocation on gauge loss)
- Token supply tracker (cumulative emitted, governance/Incendiary burns, net circulating)
- Minimum qualification period enforcer (14-day continuous hold check)
- Quorum calculator and timelock router
- Fee splitter (swap fees: 50/50 LP/Bodensee + yield fees: 100% Bodensee — all protocol-captured revenue as one-sided svZCHF inflows)
- Governance voting (AuMT for protocol governance — with phased fourth root→cube root dampening)

Estimated audit scope: ~4,500 lines of new Solidity (including CCB emission engine with 60-day EMA, CCB multiplier logic, 90-day gauge boost, Incendiary Boost escrow and efficiency scalar, Sandbox fast-track, efficiency tournament logic, AuMM governance deposit burns, der Bodensee Pool LBP weight decay engine, Miliarium Aureum pool registry, and token supply tracking). The bulk of the protocol inherits Balancer V3's existing Certora audit coverage.

---

## xxxvii. Why Fair Launch AMMs Failed — And Why Aureum Won't

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
| **Builder Burnout** | Devs work for free, farmers dump | Founding team earns AuMM by being early LPs — the highest emission rate goes to the first providers. der Bodensee Pool accumulates all protocol-captured revenue (50% swap fees + 100% yield fees) from block 0 as one-sided svZCHF inflows, building autonomous reserve depth. No token sales fund development. |
| **Chef Nomi Backdoor** | Founder controls dev fund, sells | No admin keys. No migration contract. No treasury. 100% of emissions flow to LPs from block 0. All protocol-captured revenue flows to one immutable destination: der Bodensee Pool (autonomous LBP reserve with linear weight decay) as one-sided svZCHF inflows. No human can redirect revenue, change the supply curve, or extract AuMM. The system is a Continuous Capital Corporation — fully rule-based from genesis. |
| **Vampire Attack Dependency** | Liquidity rented via incentives, leaves when APR drops | Constituent tokens (WBTC, cbBTC, PAXG, XAUt, sfrxUSD, stEURA, AAVE, LINK) trade $898M+ daily. Aggregator routing creates organic volume independent of incentives. ERC-4626 native yield provides floor return even at zero emissions. LPs have structural reasons to stay. |
| **Governance Capture** | Token-weighted voting = capital buys control | Protocol governance is AuMT-weighted — but only AuMT from emission-qualified pools counts. You cannot buy governance power on the open market. You must be providing liquidity to productive pools that meet every anti-gaming criterion. Phased dampening: fourth root in Era 0 (maximum compression at low TVL), cube root post-first-halving (TVL growth has naturally decentralised power). |
| **Death Spiral** | Token price drops → APR drops → LPs leave | Dual revenue streams: swap fees + ERC-4626 yield fees. Yield fees accrue regardless of AuMM price or trading volume. All protocol-captured revenue deepens der Bodensee Pool reserves, strengthening the AuMM price floor. BTC halving schedule means emissions decline predictably — the market prices the full curve from day one. |
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

## xxxviii. Yield Basis Hybrid Vaults — Complementary Architecture

Curve's Yield Basis protocol (March 2026) independently validated the same core thesis Aureum is built on: sustainable AMM growth requires tying TVL expansion to productive capital, not reflexive incentives. Their Hybrid Vaults solve this by requiring LPs to deposit crvUSD (earning ~4.5% scrvUSD yield) before unlocking BTC/ETH pool capacity — directly supporting the crvUSD peg while scaling. The mechanism is architecturally orthogonal to Aureum's CCB: Yield Basis enforces anticyclicality at the user level (stable-first deposit → personal cap), while Aureum enforces it at the protocol level (EMA-weighted emissions + immutable anti-gaming gates + 52% ERC-4626 Quality Gate). Both reject reflexive liquidity mining. Both force conviction capital upfront. The key divergence: Yield Basis depends on an external stablecoin peg (crvUSD + Curve DAO credit line), while Aureum's stability layer is entirely internal and oracle-free. Aureum's routing anchor (ixEDEL) has no peg to defend — its NAV arb surface generates continuous cross-pool fees without the catastrophic depeg risk that Hybrid Vaults were specifically engineered to mitigate. The two designs compose well: a future gauge-approved Aureum pool could include scrvUSD as an ERC-4626 component if it meets the $5M vault floor, giving LPs access to both yield layers simultaneously. Source: [@yieldbasis, March 30 2026](https://x.com/yieldbasis/status/2038610652194037966).

---

## xxxix. Competitive Position

### LP Advantage Over Uniswap

| Feature | Uniswap V3 Pair | Aureum Pool |
|---------|----------------|-------------|
| Trading pairs per position | 1 | 10+ (per multi-token pool) |
| Yield on idle capital | 0% | 2.0–2.8% (ERC-4626 native) |
| IL profile | Full directional exposure to one pair | Dampened — correlated assets diversify directional risk |
| Fee tier | 0.05–0.3% | 0.01–0.05% (attracts routing) |
| Active management required | Yes (range adjustments) | No (weighted pools are set-and-forget) |
| Yield sources | Swap fees only | Swap fees + vault yield + cross-pool arb fees + AuMM mining |

### Protocol Comparison

| Feature | Balancer V3 | Uniswap V4 | Curve | Aerodrome | **Aureum** |
|---------|-------------|-----------|-------|-----------|-----------|
| Multi-asset pools | Yes | No | No | No | Yes |
| ERC-4626 native | Yes | No | No | No | Yes |
| Hooks | Yes | Yes | No | No | Yes |
| Formal verification | Yes | No | No | No | Yes (inherited) |
| Fair launch | No | No | No | No | Yes |
| BTC tokenomics | No | No | No | No | Yes |
| No team allocation | No | No | No | No | Yes |
| Anti-gaming criteria | No | N/A | No | No | Yes |
| LP = miner | No | No | No | Partial | Yes |
| LP = governor | No | No | No | No | Yes |
| Emissions to governance staking | Yes (80/20) | N/A | Yes (veCRV) | No | No (banned) |
| Constellation routing network | No | No | No | No | Yes (ixEDEL hub by network effect) |
| Autonomous reserve (der Bodensee Pool) from day 1 | No | No | No | No | Yes |

### The Prop AMM Contrast

The table above compares Aureum to other public AMMs. But the most instructive contrast is with proprietary AMMs — the "dark AMMs" that now dominate Solana routing, processing tens of billions in monthly volume with zero public TVL.

Prop AMMs proved the thesis that winning aggregator routing is the entire game. A single team supplies all liquidity from proprietary capital, runs active market-making algorithms with off-chain pricing oracles, and captures volume purely by being the cheapest fill when an aggregator routes a trade. No frontend, no brand, no retail awareness needed. Just better execution.

The model works. And it is architecturally the opposite of Aureum on every dimension:

| Dimension | Proprietary AMM | Aureum |
|-----------|----------------|--------|
| Liquidity source | Team-supplied, closed | Public, permissionless LP |
| Pricing logic | Private algorithms, off-chain oracles | On-chain weighted pool math, formally verified |
| Transparency | Opaque — users cannot assess fairness or execution quality | Fully transparent — pool weights, fees, and rules are on-chain |
| Governance | None — one team controls all parameters | AuMT-weighted — LPs govern protocol decisions |
| Token distribution | Insider-heavy — typically 90%+ to foundation, team, ecosystem with vesting | Zero pre-mine — no treasury, 100% of emissions to LPs from block 0. All protocol-captured revenue flows to der Bodensee Pool (autonomous reserve) as one-sided svZCHF inflows. |
| Failure mode | Single team goes down, 35%+ of chain volume disappears | Permissionless — no single point of failure, pools exist independently |
| Chain dependency | Requires sub-second block times for active quoting — Solana-native | Passive LP model designed for Ethereum's 12-second blocks |
| LP participation | None — users cannot provide liquidity or earn fees | Core design — LP is the only way to earn tokens and governance power |

Prop AMMs solved the routing problem through centralisation. Aureum solves the same problem through architecture — multi-asset pools with native yield, constellation routing, and aggregator-competitive fees — without concentrating control in a single team. The question is whether decentralised infrastructure can match the execution quality of a proprietary trading desk. The ERC-4626 yield floor, the multi-pair capital efficiency, and the cross-pool arbitrage engine are the mechanisms that make it possible.

---

## xl. Proof of Real Yield Dashboard

The aumm.fi frontend displays per-pool yield transparency that reframes how LPs evaluate returns.

**Per pool, the dashboard shows:**

| Metric | Definition |
|--------|-----------|
| Real yield % | Portion of returns from swap fees + ERC-4626 vault yield (non-inflationary sources) |
| Emission yield % | Portion from AuMM emissions (inflationary) |
| Efficiency score | Pool's efficiency ratio vs. protocol average |
| Revenue per $1 of emissions | How much protocol revenue each dollar of emission generates |

**The framing:** *"This pool earns 68% of returns from real yield, not inflation."*

Most AMMs report a single blended APR that mixes real revenue with token emissions. LPs see "80% APR" without knowing that 75% of it is inflation that dilutes the token they're earning. Aureum separates the two, making the quality of returns visible.

When an Aerodrome LP compares "80% APR" against Aureum's "12% real yield + 15% emission yield," the conversation shifts from "which number is bigger" to "which return is sustainable." Lower headline APR, higher quality return. The dashboard makes that argument visually without saying a word about competitors.

**Token supply transparency.** The dashboard also publishes in real time:

- **Total AuMM emitted** — cumulative tokens distributed to LPs since block 0
- **Total AuMM burned** — cumulative tokens destroyed through governance deposits and Incendiary Boost escrow burns
- **Net circulating supply** — emitted minus burned
- **der Bodensee Pool reserve depth** — total svZCHF inflows and current AuMM/svZCHF ratio

See Immutable Parameters (`constitution.md` §xxix).

---

