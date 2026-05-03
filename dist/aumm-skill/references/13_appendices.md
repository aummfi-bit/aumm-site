<!-- GENERATED FROM aumm-site@b15a02c85075a04fa6cfbf4884c7ebcb8aaf220a 13_appendices.md — DO NOT EDIT -->
# Appendices

## xxxvi. AMM Architecture: Aequilibrium

### Provenance: Balancer V3

Aequilibrium is Balancer V3's open-source, Certora-verified smart contracts with a new tokenomics layer on top. Pool math is byte-identical to the audited code. The table below shows what was inherited and what was built.

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
| Fee distributor | **New** | **100%** of the **protocol share** of swap fees on non–der Bodensee pools (**~50%** of charged fee; Vault **`protocolSwapFeePercentage`**) to Bodensee + **100%** yield skim to Bodensee; der Bodensee Pool **0.75%** swap fee **in pool** in full |
| Governance | **New** | LP-weighted voting (AuMT for protocol governance), 90-day gauge boost, no ve-locking |

### What's Unchanged (Critical)

Pool contracts, vault, SOR, hooks, and rate providers are **byte-identical** to the Certora-verified Balancer V3 code. The audit and formal verification apply directly. Only the tokenomics layer requires independent audit.

The LP trust proposition: *"The AMM you're depositing into is the same formally verified code. The token you're earning is different."*

### What's New (Requires Audit)

- AuMM token contract (ERC-20 with immutable supply cap and halving logic)
- AuMT pool token wrapper (Aureum Market Tessera)
- CCB emission engine (60-day EMA calculator, CCB multiplier computation with slope-based adjustments and dead zone — see [Constitution (§xxix)](10_constitution.md) for all numeric bounds)
- Incendiary Boost engine (svZCHF/sUSDS deposit into der Bodensee, 1-epoch (14-day) emission streaming, priority skim, once-per-epoch-per-pool lock)
- 90-day gauge boost (1.2x fixed CCB multiplier for new gauges, automatic expiry)
- CCB multiplier engine (slope calculation, dead zone, step adjustments, clamp — all immutable; see [Constitution (§xxix)](10_constitution.md))
- Sandbox fast-track (top 10% efficiency sustained for 3 epochs, automatic gauge approval)
- Emission distributor (per-block streaming with halving logic, CCB-driven weight updates)
- Gauge eligibility checker (on-chain criteria enforcement, graduated grace period, volume percentile ranking, hysteresis buffer, efficiency tournament with 3-epoch smoothing, gauge revocation logic)
- Miliarium Aureum pool registry (28 pools, non-transferable, revocation on gauge loss)
- Token supply tracker (cumulative emitted, net circulating)
- Minimum qualification period enforcer (14-day continuous hold check)
- Quorum calculator and timelock router
- Fee router (non–der Bodensee pools: **100%** of the **protocol share** of swap fees to Bodensee as one-sided stablecoin (sUSDS/svZCHF); **~50%** LP residual stays with originating-pool LPs; yield skim: **100%** Bodensee one-sided stablecoin; der Bodensee Pool: **0.75%** swap fee, **100%** in-pool to der Bodensee LPs)
- Governance voting (AuMT for protocol governance — with phased fourth root→cube root dampening)

Estimated audit scope: ~4,500 lines of new Solidity (CCB emission engine with 60-day EMA, CCB multiplier logic, 90-day gauge boost, Incendiary Boost deposit and priority skim, Sandbox fast-track, efficiency tournament logic, governance deposit routing to Bodensee, der Bodensee Pool fixed-weight three-token configuration, Miliarium Aureum pool registry, token supply tracking). The bulk of the protocol inherits Balancer V3's existing Certora audit coverage.

---

## xxxvii. Why Fair Launch AMMs Failed — And Why Aureum Won't

### The Fair Launch Graveyard

Fair launches were the gold standard in 2020 (Yearn, SushiSwap). Today they're nearly extinct. The reasons are structural.

**The Bootstrap Paradox.** An AMM needs liquidity to be useful. VC-backed projects pay from their war chest. Fair launches have none. No liquidity → high slippage → no traders → no fees → LPs leave → death spiral.

**The Builder Burnout Problem.** If 100% of tokens go to the community, who pays for audits ($100–250K), legal counsel, infrastructure, and the dev's rent? Most fair launch founders end up working for free while yield farmers dump.

**Governance Capture.** Fair launches distribute tokens based on liquidity provision. Whales bring massive capital on day one, earn the majority of "fair" tokens, and vote to redirect the treasury to themselves. Fair Launch becomes Whale Launch.

**The Death Spiral.** Most AMMs rely on their own token as the incentive. Token price drops → APR drops → LPs leave → protocol dies. VC-backed projects subsidize through bear markets. Fair launches have no cushion.

### The SushiSwap Autopsy

SushiSwap is the most instructive failure. Three causes.

**1. The backdoor.** Chef Nomi controlled the dev fund and sold $14M of SUSHI. Admin keys hidden in the migration contract. The founder had a sell button the community didn't know about.

**2. Vampire attack dependency.** SushiSwap's entire TVL came from migrating Uniswap LPs via token incentives. Once incentives declined, LPs had no reason to stay. Rented liquidity.

**3. Immediate governance capture.** Large holders (FTX/Alameda) accumulated governance power through token purchases and directed treasury spending to their own interests. Token-weighted voting meant capital = control.

The deeper failure: SushiSwap was a fair launch of a **commodity product** — same Uniswap V2 pairs, same architecture, nothing novel. When incentives faded, there was no reason to use Sushi over Uniswap. The token was the only differentiator, and the token was losing value.

### How Aureum Addresses Every Failure Mode

| Failure Mode | What Killed Them | Aureum's Fix |
|-------------|-----------------|-------------|
| **Bootstrap Paradox** | No capital to seed liquidity | Founding team seeds pools with existing assets (ixEDEL, svZCHF). ERC-4626 pools generate 2-2.8% native yield from day one — LPs have a reason to stay before any AuMM emission has value. |
| **Builder Burnout** | Devs work for free, farmers dump | Founding team earns AuMM by being early LPs — the highest emission rate goes to the first providers. der Bodensee Pool accumulates **protocol-captured** revenue (**protocol share** of swap fees on other gauged pools + yield skim) from block 0 as one-sided stablecoin (sUSDS/svZCHF) inflows, plus **in-pool** swap fees on der Bodensee trades (**0.75%** at genesis), building autonomous reserve depth. No token sales fund development. |
| **Chef Nomi Backdoor** | Founder controls dev fund, sells | No admin keys. No migration contract. No treasury. **100% of the LP emission tranche** flows to LPs from block 0; **Months 1–10** the remainder of each block’s emission is one-sided AuMM into der Bodensee Pool on a piecewise decay (80%→50% by Month 6, 50%→0% by Month 10 — no wallet receives it). **Protocol-captured** revenue (**protocol share** of swap fees on other pools + yield fees) flows to der Bodensee Pool as one-sided stablecoin (sUSDS/svZCHF) inflows; **der Bodensee** swap fees (**0.75%** at genesis) stay **in pool** for LPs. No human can redirect revenue, change the supply curve, or extract bootstrap AuMM. The system is a Continuous Capital Corporation — fully rule-based from genesis. |
| **Vampire Attack Dependency** | Liquidity rented via incentives, leaves when APR drops | Constituent tokens (WBTC, cbBTC, PAXG, XAUt, sfrxUSD, stEURA, AAVE, LINK) trade $898M+ daily. Aggregator routing creates organic volume independent of incentives. ERC-4626 native yield provides floor return even at zero emissions. LPs have structural reasons to stay. |
| **Governance Capture** | Token-weighted voting = capital buys control | Protocol governance is AuMT-weighted — but only AuMT from emission-qualified pools counts. You cannot buy governance power on the open market. You must be providing liquidity to productive pools that meet every anti-gaming criterion. Phased dampening: fourth root in Era 0 (maximum compression at low TVL), cube root post-first-halving (TVL growth has naturally decentralised power). |
| **Death Spiral** | Token price drops → APR drops → LPs leave | Dual revenue streams: swap fees + ERC-4626 yield fees. Yield fees accrue regardless of AuMM price or trading volume. **Protocol-captured** revenue (one-sided stablecoin into der Bodensee) and **in-pool** der Bodensee swap fees deepen reserves, strengthening the AuMM price floor. BTC halving schedule means emissions decline predictably — the market prices the full curve from day one. |
| **Commodity Product** | No architectural moat → users leave when incentives fade | Multi-asset weighted pools, ERC-4626 native yield, hooks, constellation routing — these pool designs cannot exist on Uniswap, Curve, or Aerodrome. The moat is the architecture, not the token. LPs stay because no other venue offers the same capital efficiency. |

### The White Space

No Fair Launch AMMs exist in 2026 because the model is assumed dead. For commodity products with no structural moat and no native yield, it is.

Aureum launches with three things no previous fair launch had:

1. **Differentiated architecture** that cannot be replicated on any competing AMM
2. **Native yield** (ERC-4626) providing LP returns independent of token emissions
3. **Pre-built routing topology** (Miliarium Aureum) with $898M daily volume from constituent tokens already trading on-chain

The fair launch model failed on commodity AMMs. It has never been tried on formally verified, multi-asset, yield-bearing routing infrastructure with BTC-scarcity tokenomics and contract-enforced anti-gaming.

That experiment hasn't failed. It hasn't happened.

---

## xxxviii. Yield Basis Hybrid Vaults — Complementary Architecture

Curve's Yield Basis protocol (March 2026) independently validated the same core thesis: sustainable AMM growth requires tying TVL expansion to productive capital, not reflexive incentives. Their Hybrid Vaults require LPs to deposit crvUSD (earning ~4.5% scrvUSD yield) before unlocking BTC/ETH pool capacity — directly supporting the crvUSD peg while scaling. Architecturally orthogonal to Aureum's CCB: Yield Basis enforces anticyclicality at the user level (stable-first deposit → personal cap); Aureum enforces it at the protocol level (EMA-weighted emissions + immutable anti-gaming gates + 52% ERC-4626 Quality Gate). Both reject reflexive liquidity mining. Both force conviction capital upfront. The key divergence: Yield Basis depends on an external stablecoin peg (crvUSD + Curve DAO credit line); Aureum's stability layer is entirely internal and oracle-free. Aureum's routing anchor (ixEDEL) has no peg to defend — its NAV arb surface generates continuous cross-pool fees without the catastrophic depeg risk Hybrid Vaults were engineered to mitigate. The two designs compose well: a future gauge-approved Aureum pool could include scrvUSD as an ERC-4626 component if it meets the $5M vault floor, giving LPs access to both yield layers simultaneously. Source: [@yieldbasis, March 30 2026](https://x.com/yieldbasis/status/2038610652194037966).

---

## xxxix. Competitive Position

### LP Advantage Over Uniswap

| Feature | Uniswap V3 Pair | Aureum Pool |
|---------|----------------|-------------|
| Trading pairs per position | 1 | 10+ (per multi-token pool) |
| Yield on idle capital | 0% | 2.0–2.8% (ERC-4626 native) |
| IL profile | Full directional exposure to one pair | Dampened — correlated assets diversify directional risk |
| Fee tier | 0.05–0.3% | 0.01–0.30% (Miliarium genesis 0.03%, governance-adjustable within band with 14-day cooldown; der Bodensee 0.10–1.00% band, genesis 0.75%) |
| Active management required | Yes (range adjustments) | No (weighted pools are set-and-forget) |
| Yield sources | Swap fees only | ERC-4626 native yield (≥52% of pool) + AuMM emissions + cross-pool arb fees + swap-fee LP residual[^swap-residual] |

[^swap-residual]: For **Miliarium** (and other non–der Bodensee gauged) pools, swap-fee yield to LPs is the **LP residual — ~50%** of the pool's charged swap fee (OQ-11 sets the **rate**; the **50/50** split is the Vault **`protocolSwapFeePercentage`** invariant). The **other ~50%** is the **protocol share** the hook settles to der Bodensee (**100%** of that leg). **Der Bodensee** LPs earn the **full in-pool tier** (e.g. **0.75%** on the AuMM/sUSDS/svZCHF pool) — unchanged. See [Constitution §xxix — Fee routing](10_constitution.md).

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

The table above compares Aureum to public AMMs. The more instructive contrast is with proprietary AMMs — the "dark AMMs" dominating Solana routing, processing tens of billions in monthly volume with zero public TVL.

Prop AMMs proved that winning aggregator routing is the entire game. One team supplies all liquidity from proprietary capital, runs active algorithms with off-chain oracles, captures volume by being the cheapest fill. No frontend, no brand, no retail awareness. Just better execution.

The model works — and is architecturally opposite to Aureum on every dimension:

| Dimension | Proprietary AMM | Aureum |
|-----------|----------------|--------|
| Liquidity source | Team-supplied, closed | Public, permissionless LP |
| Pricing logic | Private algorithms, off-chain oracles | On-chain weighted pool math, formally verified |
| Transparency | Opaque — users cannot assess fairness or execution quality | Fully transparent — pool weights, fees, and rules are on-chain |
| Governance | None — one team controls all parameters | AuMT-weighted — LPs govern protocol decisions |
| Token distribution | Insider-heavy — typically 90%+ to foundation, team, ecosystem with vesting | Zero pre-mine — no treasury; **LP tranche** to LPs from block 0; **Months 1–10** piecewise-decaying bootstrap AuMM one-sided into der Bodensee Pool. **Protocol-captured** revenue (**protocol share** of swap fees on other pools + yield skim) flows to der Bodensee Pool (autonomous reserve) as one-sided stablecoin (sUSDS/svZCHF) inflows; **der Bodensee** swap fees (**0.75%** at genesis) stay **in pool**. |
| Failure mode | Single team goes down, 35%+ of chain volume disappears | Permissionless — no single point of failure, pools exist independently |
| Chain dependency | Requires sub-second block times for active quoting — Solana-native | Passive LP model designed for Ethereum's 12-second blocks |
| LP participation | None — users cannot provide liquidity or earn fees | Core design — LP is the only way to earn tokens and governance power |

Prop AMMs solved routing through centralization. Aureum solves it through architecture — multi-asset pools with native yield, constellation routing, aggregator-competitive fees — without concentrating control in one team. Whether decentralized infrastructure can match proprietary execution quality is the open question. The ERC-4626 yield floor, multi-pair capital efficiency, and cross-pool arbitrage engine are the mechanisms that make it possible.

---
