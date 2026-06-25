<!-- GENERATED FROM aumm-site@cbf2f197c4e40a6398aea53483cefc9311cea393 sagix/sagix_miliarium_aureum.md — DO NOT EDIT -->
# Sagix Miliarium Aureum

**Canonical source (Sagix Apothecary):** https://www.sagix.io/sagix-miliarium-aureum/
**Original publication date (from page):** 2026-03-11

**Note:** This file is part of the Aureum / Project documentation canon mirrored from Sagix for offline reference and AI tooling. Protocol mechanics and numeric parameters at `aumm.fi` take precedence where they conflict with interpretive essays.

---
**Dual-anchor AMMs and the small-world routing problem**

>  _"The real safe haven was never the asset. It was the market depth."_ — The bank war: central vs. decentralized money, [_sagix.io/decentralized-money_](https://www.sagix.io/decentralized-money/)

[ The four-layer framework: a complete liquidity risk assessment for DeFiThe complete DDD Episode 9 four-layer liquidity framework: pool depth, backstops, pipes, and hubs. From Jackson’s Bank War to Rothschild’s London nexus, 200 years of financial plumbing failures reveal what actually makes a DeFi position liquid under stress.![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/icon/IMG_6106-7-134.JPG)Sagix ApothecarySagix![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/thumbnail/Gemini_Generated_Image_8ctyua8ctyua8cty.png)](https://www.sagix.io/our-layer-framework/)

The US dollar did not become the global settlement currency because the Federal Reserve mandated it. It became the global settlement currency because private banks in London discovered that routing transactions through dollars was cheaper than routing them through anything else. A French bank lending to a Japanese manufacturer settled in USD not because either party was American but because deep dollar markets already existed in both directions. Once enough markets connected through the dollar, the system fed itself: more liquidity attracted more usage, more usage deepened liquidity [1]. **By the mid-1980s, there were more Eurodollars circulating offshore than domestic dollars inside the United States** [2]. The dollar's dominance was an emergent property of market infrastructure, not a policy decision.

The mechanism that produced this outcome was the cross-rate hub. In foreign exchange markets, most currency pairs do not trade directly. A GBP-to-JPY trade executes as GBP to USD to JPY. The dollar sits at the center not because it is the best currency but because it has the deepest liquidity across the most pairs, making it the cheapest intermediate step [3]. Any asset that occupies that hub position in a routing graph captures volume from trades that have nothing to do with the asset itself. The hub does not need demand. It needs depth. Depth generates routing. Routing generates volume. Volume deepens liquidity. The loop compounds.

This article examines what happens when you put two partially correlated hubs into the same pool graph instead of one, and why the resulting topology generates more volume, tighter arbitrage, and more resilient routing than either hub alone. The historical precedent is the Eurodollar clearing system. The modern application is a dual-anchor AMM architecture built on Balancer V3.

## **The single-hub problem in AMM design**

Most multi-asset AMM pools anchor around a single stable reference asset, typically a dollar stablecoin. Curve's 3pool uses USDT, USDC, and DAI. Balancer weighted pools often pair volatile tokens against a single stablecoin. The anchor provides the stable axis around which volatile tokens trade. Aggregators route through the anchor because its price is predictable and its slippage is low.

This works. But it leaves volume on the table. When only one anchor exists in a pool, every intra-pool swap between two volatile assets routes through the same path. There is no alternative route to compare against, no second pricing surface to arbitrage, and no redundancy if the anchor's liquidity thins during stress. The routing graph is a star: all roads lead to one center. If the center degrades, the entire pool degrades.

![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/2026/03/Gemini_Generated_Image_4bulcv4bulcv4bul-2.png)On June 26, 1974, German regulators shut down Bankhaus Herstatt in the middle of the business day. Herstatt's American counterparties had already paid out Deutsche Marks on their side of foreign exchange trades but had not yet received the corresponding dollars. The time-zone gap between Frankfurt and New York meant their payments were irrevocable but their receipts were not. ****Over the three days following Herstatt's failure, gross funds transferred through the interbank system declined by approximately 60%,**** not because money had been destroyed, but because banks stopped trusting the pipes.

The Eurodollar system had a similar structure before it matured. Early offshore dollar markets concentrated in London. A single clearing hub served most transactions [4]. **Exchange controls implemented by the UK in 1957, following the Suez crisis, catalyzed Eurodollar innovation** [5], but the initial architecture was fragile precisely because it depended on a single routing center. As the market expanded to Zurich, Frankfurt, Singapore, and Tokyo, the system gained resilience. Multiple clearing nodes meant a disruption in one center did not paralyze the network. The average path between any two counterparties remained short because the hubs were interconnected, while each regional market maintained high local clustering [1]. This is, formally, a small-world network: high clustering with short average path length [6].

## **Two hubs, three layers of arbitrage**

The Miliarium Aureum architecture, named after the golden milestone in the Roman Forum from which all imperial distances were measured, embeds two partially correlated anchors into every pool in a connected graph of Balancer V3 multi-asset pools [7]. The first anchor is svZCHF, a yield-bearing ERC-4626 savings token [17] whose exchange rate is read directly from its issuing contract via Balancer's Rate Provider, producing deterministic, oracle-free pricing [8]. svZCHF is issued by Frankencoin, a decentralized Swiss franc stablecoin designed as a Continuous Capital Corporation [15], where the savings module functions as an on-chain deposit facility. The second anchor is ixEDEL, a diversified token fund (DTF) built on Reserve Protocol, whose Net Asset Value is determined by its underlying basket of crypto assets, gold, and stablecoins, approximately 25% of which is itself svZCHF [7].

![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/2026/03/Gemini_Generated_Image_dtqlo8dtqlo8dtql.png)

Every pool in the system contains both anchors: svZCHF at approximately 26% weight and ixEDEL at approximately 16% weight, alongside volatile bridge tokens like cbBTC, LINK, AAVE, LDO, XAUT, or sUSDS [7]. Each pool generates ten internal trading pairs. Combined across the three multi-asset pools (ixAQUA, ixSTRATA, ixFORUM) and the base svZCHF/ZCHF pool, the system creates over thirty pairs and cross-pool routes, all touching both anchors.

The critical design insight is that the two anchors have partially independent price dynamics, and this asymmetry creates additional arbitrage volume that would not exist in a single-anchor design. Three distinct layers of arbitrage operate simultaneously.

**Layer one: yield drift.** svZCHF appreciates against its base currency at a predictable rate of approximately 3.75% APY [8]. This slow, continuous drift means the svZCHF/ZCHF base pool is never in equilibrium. Bots correct the drift mechanically, generating persistent swap volume that exists in bear markets as reliably as in bull markets. This is structural volume, not speculative. It is a function of the yield accrual rate, not market sentiment.

**Layer two: NAV arbitrage.** ixEDEL can be minted at Net Asset Value through Reserve Protocol and sold into pools, or bought from pools and redeemed at NAV. The arbitrage band is approximately 0.1% [7]. When operational, this creates continuous ixEDEL trading activity that propagates through every pool in the system, generating svZCHF swaps as a side effect because svZCHF is in every pool ixEDEL touches.

**Layer three: cross-anchor arbitrage.** This is the bonus layer that only exists because both anchors coexist in every pool. svZCHF drifts slowly and predictably. ixEDEL's NAV moves with crypto markets (approximately 13% BTC, 21% gold, 21% sUSDS in the underlying basket). When BTC drops 5%, ixEDEL's price shifts but svZCHF stays stable [7]. The two routing paths through any given pool temporarily diverge in pricing, creating a cross-anchor arbitrage opportunity that bots trade to equalize. The partial correlation between the anchors, ixEDEL holds roughly 25% svZCHF, ensures the system stays coherent while allowing enough independent movement to generate persistent arb.

Every time ixEDEL's volatile components move, bots trade to equalize the two routing paths, generating volume through both anchors simultaneously. This is volume that a single-anchor pool cannot produce because it requires two pricing surfaces to diverge and reconverge.

## **Small-world topology on Balancer V3**

In 1998, Watts and Strogatz published their landmark paper demonstrating that networks with high local clustering and short average path lengths, what they called small-world networks, emerge when a few long-range connections are introduced into a regular lattice [6]. **The defining property is that path length drops dramatically with only a small number of shortcut connections, while clustering remains high** [9]. Real-world systems from power grids to neural networks to social graphs exhibit this topology, and its efficiency properties are well understood: high clustering supports specialized local processing, while short paths enable rapid global communication [10].

The Miliarium Aureum pool graph is a small-world network by construction. Each pool is a tightly clustered local market where five tokens trade against each other through ten internal pairs. svZCHF and ixEDEL, present in every pool, act as the shortcut connections that create short global paths between any two assets in the system [7]. A swap from cbBTC (in ixAQUA) to LDO (in ixFORUM) does not need to traverse the entire graph. It routes through svZCHF or ixEDEL in two hops because both hubs appear in both pools.

![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/2026/03/Gemini_Generated_Image_au16luau16luau16.png)

For Balancer V3 specifically, this topology has operational implications. Aggregators (1inch, CowSwap, Matcha, Paraswap) optimize for three variables: lowest slippage, lowest fees, lowest gas [7]. They are indifferent to token narratives. If a route through svZCHF or ixEDEL produces the best execution, the aggregator routes through it. The dual-anchor design means aggregators can split a single trade across both paths simultaneously, sending the majority through svZCHF (deeper, deterministic pricing via Rate Provider) and the remainder through ixEDEL (shallower, NAV-priced) to minimize total price impact [7]. This split routing is itself evidence that the dual-anchor topology is generating routing efficiency that a single-anchor pool cannot match.

The Balancer V3 Core Pool mechanism makes this architecture self-funding. Because svZCHF is ERC-4626 compliant, pools containing it at 50% or more yield-bearing composition qualify for Core Pool status [11]. Balancer takes a 10% fee on yield accrual and recycles it as BAL emissions to liquidity providers [8]. The base svZCHF/ZCHF pool currently delivers a confirmed base APR of 2.63%, rising to 4.03% with veBAL boost [8]. The gauge passed as BIP-913 with 100% approval [12]. This is not speculative incentive farming. It is yield recycling funded by the structural characteristics of the token, not by inflationary emissions.

The natural division of labor between the two anchors is worth stating precisely. svZCHF is the primary routing vehicle: deeper per pool (62% more weight than ixEDEL), deterministic pricing via Rate Provider, minimal slippage variance, with yield that attracts and retains LPs. ixEDEL is the secondary routing vehicle and arbitrage extraction layer: NAV mechanics create continuous mint/redeem cycles, cross-pool bridging connects isolated asset clusters, and its volatility-driven price movements generate the cross-anchor arb that is the third layer of volume [7]. They are complementary, not competitive. Together they generate more total volume than either alone because their price dynamics are independent enough to create cross-anchor arb but correlated enough to keep the system coherent.

## **The Eurodollar lesson: what happens when the clearing layer fails**

The Eurodollar system's fatal weakness was not in the dollars themselves. It was in the trust layer connecting the clearing nodes. Offshore Eurodollars were bank liabilities, not Federal Reserve obligations. A dollar in a London bank was a promise by that bank, not a fact verified by the issuer [1]. During the 2008 financial crisis, banks doubted each other's dollar holdings. **The LIBOR-OIS spread, which had historically hovered around 10 basis points, spiked to an all-time high of 364 basis points in October 2008** [13]. The interbank market froze. **The Federal Reserve created emergency swap lines that reached over $580 billion outstanding by December 2008, accounting for more than 25% of the Fed's total assets** [14]. The deepest, most liquid routing currency in human history nearly seized because the infrastructure connecting its clearing nodes depended on counterparty trust, and that trust evaporated overnight.

![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/2026/03/Gemini_Generated_Image_8sz8t8sz8t8sz8t8.png)

The dual-anchor Balancer architecture eliminates this failure mode at the protocol level. svZCHF's price is not a bank's promise. It is read directly from the issuing contract via Balancer's Rate Provider. The exchange rate is deterministic, on-chain accounting rather than market speculation [8]. There is no counterparty trust required, no interbank balance sheet to doubt, no spread that can explode during a crisis. When the pool price deviates from the contract rate, bots correct it mechanically. ixEDEL's NAV is similarly verifiable on-chain through Reserve Protocol's transparent basket [7]. Both anchors are trustworthy not because of reputation but because the accounting is deterministic and public.

The resilience properties extend to the network topology. If one pool in the Miliarium Aureum is stressed, whether from a bridge token depeg, a flash crash in a volatile component, or a temporary liquidity drain, aggregators instantly reroute through the parallel paths that exist in every other pool sharing the same two hubs. This is the small-world property at work: removing a single cluster node does not disconnect the graph because the shortcut connections (svZCHF and ixEDEL) maintain short paths between all remaining clusters [6]. Compare this to the standard DeFi liquidity model, where a stablecoin's deepest pool sits on a single venue. If that venue is exploited or drained, the stablecoin loses its primary market in one event. DAI concentrated on Curve's 3pool. FRAX concentrated on Curve. LUSD relied heavily on one Curve pair. Depth without distribution is fragility wearing the mask of strength.

![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/2026/03/Gemini_Generated_Image_x61nftx61nftx61n.png)

## **What this means for AMM routing design**

The pattern from Eurodollar history is clear: routing infrastructure compounds. Once aggregators encode paths through a hub as preferred routes, displacing that position requires a competitor to build deeper liquidity across the same number of pools simultaneously, a far harder task than draining a single pool [7]. The Miliarium Aureum is designed to exploit this compounding property on Balancer V3. As pools deepen, more trades route through the dual anchors. More routing generates more fees. More fees attract more LPs. Deeper pools attract yet more routing. The asset pair at the center of this loop becomes a routing hub not by design decree but by gravitational pull.

The open question is whether the system can cross the depth threshold where aggregators begin treating the dual-anchor pools as preferred routes. Liquidity networks behave like phase transitions: below a critical size, aggregators ignore them entirely; above it, they dominate routing [7]. There is little middle ground. The phased deployment strategy, base pool first, multi-asset roads second, is designed to cross the threshold at each layer before activating the next. But the risk that fragmentation outpaces network effects during the bootstrap phase is real and should not be minimized.

If the threshold is crossed, the implications for Balancer V3 extend beyond a single pool graph. The dual-anchor topology is a general design pattern: any pair of partially correlated, deterministically priced tokens can serve as parallel routing hubs across a family of multi-asset pools, generating three-layer arbitrage (drift, NAV, cross-anchor) that produces structural volume independent of market sentiment. 

![](https://storage.ghost.io/c/dc/15/dc152460-95bc-4abf-b4f4-c7e17de2bad2/content/images/2026/03/Gemini_Generated_Image_3ed5de3ed5de3ed5.png)

**The Watts-Strogatz insight applies: you do not need many shortcut connections to collapse path lengths across a network [6]. Two well-placed hubs in every pool may be sufficient to turn an isolated collection of liquidity venues into a connected routing system that aggregators treat as a single, deep market.**

## Sign up for Sagix Apothecary

Sophisticated DeFi portfolio strategies for all market conditions. Sagix Apothecary combines historical financial wisdom with expert analysis for discerning enthusiasts willing to learn..

Subscribe

Email sent! Check your inbox to complete your signup. 

No spam. Unsubscribe anytime.

The Eurodollar system took two decades to reach critical mass. DeFi routing operates on compressed timescales because aggregators discover and encode optimal paths algorithmically rather than through human relationships. Whether the Miliarium Aureum can compress the Eurodollar's gravitational accumulation into months rather than decades depends on one variable: whether the initial depth is sufficient for aggregators to notice. Everything after that is compounding.

* * *

## **The Druid Deep Dive — Series Bibliography**

This article is part of the Druid Deep Dive series exploring historical parallels in monetary infrastructure. The full series is available at sagix.io:

[_Episode 3 — The Suffolk System: America’s First Clearing House_](https://www.sagix.io/episode-3-the-suffolk-system-americas-first-clearing-house/)

[ _Episode 6 — The Panic of 1907: When One Man Became the Fed_](https://www.sagix.io/ddd6/)

[ _Episode 7 — Baring Brothers: The Original “Too Big to Fail”_](https://www.sagix.io/baring/)

[ _Episode 9, Part 1 — The Bank War: Central vs. Decentralized Money_](https://www.sagix.io/decentralized-money/)

[ _Episode 9, Part 2 — The Eurodollar Shadow: When Dollars Escape Their Makers_](https://www.sagix.io/the-druid-deep-dive-episode-9-part-2-the-eurodollar-shadow-when-dollars-escape-their-makers/)

[ _Episode 9, Part 3 — Eurodollar Mechanics and the Offshore Dollar Machine_](https://www.sagix.io/ddd-9-part-3/)

[ _Episode 9, Part 4 — From Eurodollars to DeFi: The Routing Thesis_](https://www.sagix.io/ddd9p4/)

[ _The Four-Layer Framework: A Complete Liquidity Risk Assessment for DeFi_](https://www.sagix.io/our-layer-framework/)

## **Sources and references**

[1] Schenk, Catherine R. "The Origins of the Eurodollar Market in London: 1955–1963." Explorations in Economic History, Vol. 35, No. 2 (1998): 221–238.

[2] "Eurodollar." Wikipedia. Historical market size data, citing BIS annual reports. Available: https://en.wikipedia.org/wiki/Eurodollar

[3] Bank for International Settlements. "Triennial Central Bank Survey of Foreign Exchange and Over-the-Counter Derivatives Markets." BIS, 2022. US dollar as cross-rate hub.

[4] Menand, Lev & Younger, Josh. "The Hidden History of Eurodollars, Part 1: Cold War Origins." Bloomberg Odd Lots, January 2025.

[5] Restrepo-Echavarria, P. & Wen, Y. "Bretton Woods and Growth of Eurodollar Market." Federal Reserve Bank of St. Louis, On the Economy Blog. January 2022. Available: https://www.stlouisfed.org/on-the-economy/2022/january/bretton-woods-growth-eurodollar-market

[6] Watts, Duncan J. & Strogatz, Steven H. "Collective dynamics of 'small-world' networks." Nature, Vol. 393 (1998): 440–442. Available: http://snap.stanford.edu/class/cs224w-readings/watts98smallworld.pdf

[7] Sagix Apothecary. "Deep Markets for a Safer Frankencoin: Balancer Liquidity Infrastructure for Liquidation Stability and ZCHF Adoption." Technical proposal, March 2026.

[8] BIP-913. "Enable Gauges for svZCHF/ZCHF and ixEDEL/USDC on Ethereum." Balancer Governance Forum. Available: https://forum.balancer.fi/t/bip-913-enable-gauges-for-svzchf-zchf-and-ixedel-usdc-on-ethereum/6970

[9] Newman, M.E.J. "Models of the Small World." Journal of Statistical Physics, Vol. 101, Nos. 3/4 (2000): 819–841.

[10] Telesford, Q.K. et al. "The Ubiquity of Small-World Networks." Brain Connectivity, Vol. 1, No. 5 (2011): 367–375. PMC3604768.

[11] Balancer Documentation. "Core Pools." Available: https://docs.balancer.fi/partner-onboarding/onboarding-overview/core-pools.html

[12] Balancer Governance. BIP-913 voting results, 100% approval.

[13] "Overnight indexed swap." Wikipedia. LIBOR-OIS spread historical data. See also: Federal Reserve Bank of San Francisco Economic Letter, January 2009. Available: https://www.frbsf.org/economic-research/publications/economic-letter/2009/january/libor-financial-crisis/

[14] Fleming, Michael J. & Klagge, Nicholas J. "The Federal Reserve's Foreign Exchange Swap Lines." Federal Reserve Bank of New York, Current Issues in Economics and Finance, Vol. 16, No. 4 (2010). Available: https://www.newyorkfed.org/medialibrary/media/research/current_issues/ci16-4.pdf

[15] Meisser, Luzius. "Essays in Decentralized Finance." Doctoral dissertation, University of Zurich. Available: https://app.frankencoin.com/thesis-frankencoin.pdf

[16] Meisser, Luzius & Maire, Basile. "Frankencoin." SNB-CIF Conference on Cryptoassets and Financial Innovation, June 2022. Protocol documentation: https://www.frankencoin.com/

[17] ERC-4626 Tokenized Vault Standard. Ethereum Improvement Proposals. Available: https://ethereum.org/developers/docs/standards/tokens/erc-4626/

[18] Rolnick, Arthur J. & Weber, Warren E. "The Free Banking Era: New Evidence on Laissez-Faire Banking." Federal Reserve Bank of Minneapolis, Quarterly Review, Vol. 9, No. 3 (1985). Suffolk Banking System analysis: [_sagix.io/episode-3-the-suffolk-system_](https://www.sagix.io/episode-3-the-suffolk-system-americas-first-clearing-house/)

[19] Bruner, Robert F. & Carr, Sean D. The Panic of 1907: Lessons Learned from the Market’s Perfect Storm. John Wiley & Sons, 2007. See also: [_sagix.io/ddd6_](https://www.sagix.io/ddd6/)

* * *

## **Legal disclaimers and disclosures**

**Educational purpose only:** This content is provided exclusively for educational and historical research purposes. It should not be construed as investment advice, financial planning guidance, policy recommendations, or official economic analysis. Any contemporary parallels or policy discussions are presented as academic analysis, not recommendations for action. Historical patterns provide context for learning but do not predict future financial system outcomes or investment performance.

**AI-assisted research disclosure:** This historical analysis was researched and written with substantial assistance from artificial intelligence technology (Claude, Anthropic). While extensive efforts were made to verify all statistical claims, citations, and institutional analysis against authoritative sources, readers should independently verify any information before relying on it for academic, professional, investment, or policy purposes.

**Accuracy and liability limitations:** While extensive effort has been made to ensure historical accuracy through authoritative sources, the authors make no warranties about completeness, accuracy, or currency of information. Historical interpretation involves scholarly judgment and academic debate. Economic data may contain revisions, measurement inconsistencies, or reporting variations across different time periods and institutional sources.

**Liability protections:** The authors, publishers, and Sagix Apothecary assume no responsibility for errors, omissions, or consequences arising from the use of this information. This includes any errors that may result from AI assistance in research, writing, or data analysis. Users assume full responsibility for any decisions or actions taken based on this content.

**Investment risk warning:** Historical financial analysis does not constitute investment advice or recommendations. Past performance, whether historical or hypothetical, does not guarantee future results. All investments carry risk of loss, and readers should conduct their own research and consult qualified financial advisors before making investment decisions.

**No professional relationship:** This content does not create any professional, advisory, fiduciary, or client relationship between the reader and Sagix Apothecary, its authors, or affiliated entities. Readers seeking financial, investment, legal, regulatory, or policy guidance should consult qualified professionals licensed in their jurisdiction.

**Methodological note:** This analysis synthesizes findings from multiple Federal Reserve Bank research departments, National Bureau of Economic Research publications, peer-reviewed academic journals, and authoritative government historical records. The numbered citation system allows readers to verify specific claims against original sources rather than relying on secondary interpretations. All quantitative data and statistical analyses are drawn from the referenced academic literature rather than independent calculation.

**Contemporary financial systems:** References to modern financial systems, cryptocurrency protocols, or DeFi mechanisms are made for educational comparison purposes only. These comparisons do not constitute endorsements, recommendations, or predictions about the performance or suitability of any current financial products or services.

Last updated: March 2026 | Series: The Druid Deep Dive |Publisher: The Genesis Address LLC
