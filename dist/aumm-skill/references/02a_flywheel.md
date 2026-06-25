<!-- GENERATED FROM aumm-site@dd5fd5f210483395ca105ac7449c0a2202ed2a7f 02a_flywheel.md — DO NOT EDIT -->
# The Flywheel

*Section **v.** of [Mental model](02_mental_model.md#v-the-flywheel) — read in context there.*

> The CCB directs emissions, **der Bodensee** captures revenue, the **Miliarium** generates it. Sections **i–iv** above look like three components. They are one closed circuit.

### v-a. The Circuit

Follow one dollar around the loop. It returns larger.

1. **Emissions recruit capital.** A fixed AuMM stream per block — **1.00 AuMM/block in Era 0** ([Tokenomics](04_tokenomics.md)) — pays LPs who deposit productive capital. The stream is fixed in *tokens*; its dollar value is `AuMM_per_block × AuMM_price`.
2. **Capital generates revenue.** Every dollar of TVL in an ERC-4626 pool yields from block 0; every trade pays a swap fee — the **Day-One Revenue Guarantee**, no volume required.
3. **Revenue deepens the reserve.** Protocol swap fees (**~50%** of charged fee) and the **10%** ERC-4626 yield skim route one-sided into der Bodensee as sUSDS/svZCHF; der Bodensee's **60%** stablecoin side compounds in-place via Rate Providers. Three inflows, one direction ([Tokenomics §x-a](04_tokenomics.md)).
4. **A deeper reserve reprices AuMM.** Fixed **40%** AuMM side; bootstrap one-sided inflow decays to **zero at Month 10** ([F-0](11_formulas.md)), after which AuMM enters only via swap. Weighted-pool math — fixed numerator, growing denominator — lifts price mechanically. No buyback, no burn, no discretion. **The pool is the value-capture mechanism.**
5. **Higher AuMM price raises every pool's APR.** Token-denominated emissions mean repricing lifts the dollar value of the same per-block stream — headline APR rises with **no new fee revenue**.
6. **Higher APR recruits more capital.** Step 1 again, one turn richer.

```
emissions → TVL → fees + 4626 yield → der Bodensee deepens
    → AuMM reprices up → AuMM-denominated APR rises → more TVL → …
```

Reflexive by construction: each turn's output is the next turn's input. The only external fuel is the first few turns of capital.

### v-b. Why the Loop Cannot Leak

Most token economies bleed at the seams — treasury sales, insider unlocks, buybacks that can reverse. Aureum closed every seam at block 0.

- **No treasury wallet** for discretionary AuMM sale. Bootstrap goes one-sided into the reserve; that channel zeroes at Month 10.
- **No insider allocation, cliff, or vesting.** What emits is what exists. Nothing sells into LPs from above.
- **No buyback to mis-route.** Value accrues through pool math, not a wallet that could dump.
- **No emission vote.** CCB allocation is mechanical ([Constitution §xxix](10_constitution.md)); governance cannot redirect the loop.

The loop has nowhere to lose value. *Der Bodensee: a lake that only gets deeper.*

### v-c. Where You Stand in the Loop

Same circuit from the protocol's view; three participant positions, three leverage profiles.

**The holder.** Buy and hold. You capture step 4 — repricing — at spot when you transact. No IL, no liquidity provided. Long a fixed numerator against a deepening reserve: the cleanest patience bet.

**The buyer-as-participant.** Buying AuMM from der Bodensee turns the wheel: your purchase deepens the reserve, thins the AuMM side, lifts price (step 4) and AuMM-denominated APR across eligible pools (step 5). Leverage is inverse to reserve depth — a shallow early reserve moves hard on the same buy that barely registers once mature. The early believer has the most wheel leverage for the same reason the wheel needs them most.

**The der Bodensee LP.** Provide AuMM into der Bodensee — the apex seat, where every revenue stream terminates and you own a pro-rata slice. Three returns stack:

- full **0.75%** in-pool swap fee on every trade, including every recruitment buy;
- in-place ERC-4626 yield on the **60%** stablecoin side via Rate Providers;
- repricing on your **40%** AuMM leg as the reserve deepens.

Cost: impermanent loss on the AuMM leg — sharp appreciation means net-selling AuMM vs. simply holding. Deep-conviction only: long AuMM, wear the rebalancing cost, collect the toll on everyone else's recruitment.

### v-d. The One Input the Loop Cannot Engineer

Every step above is unconditional — the mechanism runs whether or not anyone acts. But the magnitude of every step scales with one input the protocol can incentivize and cannot command: **TVL**. A flywheel is real once it turns; the open question is only whether the first turns happen — the cold-start.

Era 0 front-loads ~50% of supply, Incendiary Boost lets anyone fund a pool's ignition, and equal allocation through the first ten months keeps the field level until the EMA has data. These improve the odds of the first turn; they do not guarantee it. Aureum engineered away every endogenous risk — insider supply, discretionary dispositions, unlock overhang, redirectable emissions — and kept only the honest one: whether adoption arrives.
