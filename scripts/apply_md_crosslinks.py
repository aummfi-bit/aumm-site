#!/usr/bin/env python3
"""One-off helper: replace bare `NN_doc.md` cross-references with descriptive markdown links."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".cursor"}
SKIP_FILES = {"editorial_sprints.md", "apply_md_crosslinks.py"}


def iter_md():
    for p in ROOT.rglob("*.md"):
        if any(x in p.parts for x in SKIP_DIRS):
            continue
        if p.name in SKIP_FILES:
            continue
        yield p


# Longest / most specific patterns first
REPL: list[tuple[str, str]] = [
    # Multi-doc phrases
    (
        "see `08_bootstrap.md` §xxii and `10_constitution.md` §xxviii.",
        "see [Bootstrap (§xxii)](08_bootstrap.md) and [Constitution (§xxviii)](10_constitution.md).",
    ),
    (
        "see `08_bootstrap.md` §xxiv for worked examples and `10_constitution.md` §xxvii for the binding rule",
        "see [Bootstrap (§xxiv)](08_bootstrap.md) for worked examples and [Constitution (§xxvii)](10_constitution.md) for the binding rule",
    ),
    (
        "(`08_bootstrap.md` §xxi)",
        "([Bootstrap §xxi](08_bootstrap.md))",
    ),
    (
        "see `08_bootstrap.md` §xxi for gauge approval mechanics.",
        "see [Bootstrap (§xxi)](08_bootstrap.md) for gauge approval mechanics.",
    ),
    (
        "see `08_bootstrap.md` section xxiii.",
        "see [Bootstrap (section xxiii)](08_bootstrap.md).",
    ),
    (
        "See `08_bootstrap.md` section xxiii.",
        "See [Bootstrap (section xxiii)](08_bootstrap.md).",
    ),
    (
        "See `08_bootstrap.md` §xxiii.",
        "See [Bootstrap (§xxiii)](08_bootstrap.md).",
    ),
    (
        "see `08_bootstrap.md` §xxiii",
        "see [Bootstrap (§xxiii)](08_bootstrap.md)",
    ),
    (
        "See `10_constitution.md` §xxviii–xxix for the full rules and immutable parameters.",
        "See [Constitution (§§xxviii–xxix)](10_constitution.md) for the full rules and immutable parameters.",
    ),
    (
        "See `10_constitution.md` and `11_formulas.md`.",
        "See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).",
    ),
    (
        "see `10_constitution.md` and `11_formulas.md`.",
        "see the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).",
    ),
    (
        "See `10_constitution.md` and `11_formulas.md`",
        "See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md)",
    ),
    (
        "see `10_constitution.md` and `11_formulas.md`",
        "see the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md)",
    ),
    (
        "No vote. See `10_constitution.md` and `11_formulas.md`.",
        "No vote. See the [Constitution](10_constitution.md) and [Protocol formulas](11_formulas.md).",
    ),
    (
        "See `03_theoretical_foundation.md` (sections vi–vii) and `10_constitution.md` for the full mechanics.",
        "See [Theoretical foundations (§§vi–vii)](03_theoretical_foundation.md) and the [Constitution](10_constitution.md) for the full mechanics.",
    ),
    (
        "see `03_theoretical_foundation.md` §vii and `11_formulas.md` F-8; for numeric bounds, see `10_constitution.md` §xxix",
        "see [Theoretical foundations (§vii)](03_theoretical_foundation.md) and [Protocol formulas (F-8)](11_formulas.md); for numeric bounds, see [Constitution (§xxix)](10_constitution.md)",
    ),
    (
        "For the narrative explanation, see `03_theoretical_foundation.md` §vii; for the formal update rule, see `11_formulas.md` F-8.",
        "For the narrative explanation, see [Theoretical foundations (§vii)](03_theoretical_foundation.md); for the formal update rule, see [Protocol formulas (F-8)](11_formulas.md).",
    ),
    (
        "For the full explanation of how the EMA works and why, see `03_theoretical_foundation.md` §vi. For the formal definition, see `11_formulas.md` F-4. The EMA horizon is immutable — see `10_constitution.md` §xxix.",
        "For the full explanation of how the EMA works and why, see [Theoretical foundations (§vi)](03_theoretical_foundation.md). For the formal definition, see [Protocol formulas (F-4)](11_formulas.md). The EMA horizon is immutable — see [Constitution (§xxix)](10_constitution.md).",
    ),
    (
        "see `03_theoretical_foundation.md` §vi). The 28 Miliarium pools carry an algorithmic CCB multiplier (see `10_constitution.md` §xxix for bounds)",
        "see [Theoretical foundations (§vi)](03_theoretical_foundation.md)). The 28 Miliarium pools carry an algorithmic CCB multiplier ([Constitution §xxix](10_constitution.md) for bounds)",
    ),
    (
        "See `12_aureum_glossary.md` (section xxxv) for the full rule set.",
        "See [Glossary (section xxxv)](12_aureum_glossary.md) for the full rule set.",
    ),
    (
        "see `04_tokenomics.md` §x.",
        "see [Tokenomics (§x — Value capture)](04_tokenomics.md).",
    ),
    (
        "see `04_tokenomics.md` and `11_formulas.md` F-11.",
        "see [Tokenomics](04_tokenomics.md) and [Protocol formulas (F-11)](11_formulas.md).",
    ),
    (
        "See `04_tokenomics.md` and `11_formulas.md` F-11.",
        "See [Tokenomics](04_tokenomics.md) and [Protocol formulas (F-11)](11_formulas.md).",
    ),
    (
        "see `04_tokenomics.md`",
        "see [Tokenomics](04_tokenomics.md)",
    ),
    (
        "See `04_tokenomics.md`",
        "See [Tokenomics](04_tokenomics.md)",
    ),
    (
        "— **`04_tokenomics.md`**.",
        "— **[Tokenomics](04_tokenomics.md)**.",
    ),
    (
        "Read **`04_tokenomics.md`** for **AuMM**",
        "Read **[Tokenomics](04_tokenomics.md)** for **AuMM**",
    ),
    (
        "see `05_miliarium_aureum.md` §xii",
        "see [Miliarium Aureum registry (§xii — der Bodensee)](05_miliarium_aureum.md)",
    ),
    (
        "the ix-named registry in `05_miliarium_aureum.md`",
        "the ix-named registry in the [Miliarium Aureum registry](05_miliarium_aureum.md)",
    ),
    (
        "(`04_tokenomics.md`)",
        "([Tokenomics](04_tokenomics.md))",
    ),
    (
        "see `07_miliarium_sectors.md`",
        "see [Miliarium sectors](07_miliarium_sectors.md)",
    ),
    (
        "See `07_miliarium_sectors.md`",
        "See [Miliarium sectors](07_miliarium_sectors.md)",
    ),
    (
        "the correlation matrix in `07_miliarium_sectors.md`",
        "the correlation matrix in [Miliarium sectors](07_miliarium_sectors.md)",
    ),
    (
        "see `13_appendices.md` for a detailed comparison",
        "see [Appendices](13_appendices.md) for a detailed comparison",
    ),
    (
        "See `13_appendices.md` for a detailed comparison",
        "See [Appendices](13_appendices.md) for a detailed comparison",
    ),
    (
        "see `11_formulas.md` F-0",
        "see [Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md)",
    ),
    (
        "(see `11_formulas.md` F-0)",
        "([Protocol formulas — Bodensee bootstrap (F-0)](11_formulas.md))",
    ),
    (
        "see `11_formulas.md` F-11 for the formal composition definition.",
        "see [Protocol formulas — der Bodensee Pool composition (F-11)](11_formulas.md) for the formal composition definition.",
    ),
    (
        "See `11_formulas.md` F-11 for the formal composition definition.",
        "See [Protocol formulas — der Bodensee Pool composition (F-11)](11_formulas.md) for the formal composition definition.",
    ),
    (
        "see `11_formulas.md` (F-8); `12_aureum_glossary.md` covers",
        "see [Protocol formulas (F-8)](11_formulas.md); [Glossary](12_aureum_glossary.md) covers",
    ),
    (
        "see `11_formulas.md` F-4",
        "see [Protocol formulas (F-4)](11_formulas.md)",
    ),
    (
        "see `11_formulas.md` for the blend formula.",
        "see [Protocol formulas](11_formulas.md) for the blend formula.",
    ),
    (
        "See `11_formulas.md` for the blend formula.",
        "See [Protocol formulas](11_formulas.md) for the blend formula.",
    ),
    (
        "See `11_formulas.md` for the step-by-step formal sequence.",
        "See [Protocol formulas](11_formulas.md) for the step-by-step formal sequence.",
    ),
    (
        "see `11_formulas.md` for the step-by-step formal sequence.",
        "see [Protocol formulas](11_formulas.md) for the step-by-step formal sequence.",
    ),
    (
        "See `11_formulas.md` for the formal expression.",
        "See [Protocol formulas](11_formulas.md) for the formal expression.",
    ),
    (
        "see `11_formulas.md` for the formal expression.",
        "see [Protocol formulas](11_formulas.md) for the formal expression.",
    ),
    (
        "See `11_formulas.md` for all formal definitions.",
        "See [Protocol formulas](11_formulas.md) for all formal definitions.",
    ),
    (
        "see `11_formulas.md` for all formal definitions",
        "see [Protocol formulas](11_formulas.md) for all formal definitions",
    ),
    (
        "see `11_formulas.md`.",
        "see [Protocol formulas](11_formulas.md).",
    ),
    (
        "See `11_formulas.md`.",
        "See [Protocol formulas](11_formulas.md).",
    ),
    (
        "see `11_formulas.md`",
        "see [Protocol formulas](11_formulas.md)",
    ),
    (
        "See `11_formulas.md`",
        "See [Protocol formulas](11_formulas.md)",
    ),
    (
        "see `10_constitution.md` §xxviii",
        "see [Constitution (§xxviii)](10_constitution.md)",
    ),
    (
        "see `10_constitution.md` §xxix",
        "see [Constitution (§xxix)](10_constitution.md)",
    ),
    (
        "see `10_constitution.md`",
        "see [Constitution](10_constitution.md)",
    ),
    (
        "See `10_constitution.md`",
        "See [Constitution](10_constitution.md)",
    ),
    (
        "governance applies only to non-emission actions (see `10_constitution.md`, `08_bootstrap.md`).",
        "governance applies only to non-emission actions (see [Constitution](10_constitution.md), [Bootstrap](08_bootstrap.md)).",
    ),
    (
        "see `10_constitution.md`). **After Year 1**",
        "see [Constitution](10_constitution.md)). **After Year 1**",
    ),
    (
        "Months 11–12** blend **linearly** from equal to CCB (see `10_constitution.md`). **After Year 1**",
        "Months 11–12** blend **linearly** from equal to CCB (see [Constitution](10_constitution.md)). **After Year 1**",
    ),
    (
        "under the on-chain-data-only proposal rules in `10_constitution.md`. For full formal definitions of every formula, see `11_formulas.md`.",
        "under the on-chain-data-only proposal rules in [Constitution](10_constitution.md). For full formal definitions of every formula, see [Protocol formulas](11_formulas.md).",
    ),
    (
        "per **`08_bootstrap.md`**",
        "per **[Bootstrap](08_bootstrap.md)**",
    ),
    (
        "See `08_bootstrap.md` §xxiv",
        "See [Bootstrap (§xxiv)](08_bootstrap.md)",
    ),
    (
        "see `08_bootstrap.md` §xxiv",
        "see [Bootstrap (§xxiv)](08_bootstrap.md)",
    ),
    (
        "See `08_bootstrap.md`",
        "See [Bootstrap](08_bootstrap.md)",
    ),
    (
        "see `08_bootstrap.md`",
        "see [Bootstrap](08_bootstrap.md)",
    ),
    (
        "See `12_aureum_glossary.md`).",
        "See [Glossary](12_aureum_glossary.md)).",
    ),
    (
        "see `12_aureum_glossary.md`",
        "see [Glossary](12_aureum_glossary.md)",
    ),
    (
        "See `12_aureum_glossary.md`",
        "See [Glossary](12_aureum_glossary.md)",
    ),
    (
        "see `02_mental_model.md` §iii (Constellation Routing) and `miliarium_profiles/05_ixEdelweiss.md`.",
        "see [Mental model (§iii — Constellation routing)](02_mental_model.md) and [ixEdelweiss profile](miliarium_profiles/05_ixEdelweiss.md).",
    ),
    # Immutable Parameters — many variants
    (
        "See Immutable Parameters (`10_constitution.md` §xxix) for the full list. In short:",
        "See [Immutable Parameters (§xxix)](10_constitution.md) for the full list. In short:",
    ),
    (
        "**What governance cannot control:** See Immutable Parameters (`10_constitution.md` §xxix) for the full list.",
        "**What governance cannot control:** See [Immutable Parameters (§xxix)](10_constitution.md) for the full list.",
    ),
    (
        "For all numeric bounds (step size, clamp range, dead zone), see Immutable Parameters (`10_constitution.md` §xxix). For the formal update rule, see `11_formulas.md`.",
        "For all numeric bounds (step size, clamp range, dead zone), see [Immutable Parameters (§xxix)](10_constitution.md). For the formal update rule, see [Protocol formulas](11_formulas.md).",
    ),
    (
        "All numeric bounds (step size, clamp range, dead zone, EMA horizon) are **immutable from block 0** — see Immutable Parameters (`10_constitution.md` §xxix) for the exact values.",
        "All numeric bounds (step size, clamp range, dead zone, EMA horizon) are **immutable from block 0** — see [Immutable Parameters (§xxix)](10_constitution.md) for the exact values.",
    ),
    (
        "Step size, clamp bounds, and dead zone threshold are all immutable from block 0 — see Immutable Parameters (`10_constitution.md` §xxix) for exact values.",
        "Step size, clamp bounds, and dead zone threshold are all immutable from block 0 — see [Immutable Parameters (§xxix)](10_constitution.md) for exact values.",
    ),
    (
        "Pools growing too fast are automatically taxed; pools shrinking are automatically subsidized. For all numeric bounds (step size, clamp range, dead zone), see Immutable Parameters (`10_constitution.md` §xxix). For the narrative explanation, see `03_theoretical_foundation.md` §vii; for the formal update rule, see `11_formulas.md` F-8.",
        "Pools growing too fast are automatically taxed; pools shrinking are automatically subsidized. For all numeric bounds (step size, clamp range, dead zone), see [Immutable Parameters (§xxix)](10_constitution.md). For the narrative explanation, see [Theoretical foundations (§vii)](03_theoretical_foundation.md); for the formal update rule, see [Protocol formulas (F-8)](11_formulas.md).",
    ),
    (
        "**What is the step size on the CCB multiplier?** See Immutable Parameters (`10_constitution.md` §xxix) for the exact step size, clamp band, and dead zone — all immutable from block 0.",
        "**What is the step size on the CCB multiplier?** See [Immutable Parameters (§xxix)](10_constitution.md) for the exact step size, clamp band, and dead zone — all immutable from block 0.",
    ),
    (
        "within the immutable band** (see `10_constitution.md` §xxix). Net effect",
        "within the immutable band** (see [Constitution (§xxix)](10_constitution.md)). Net effect",
    ),
    (
        "**within the immutable band** (see `10_constitution.md` §xxix). Net effect",
        "**within the immutable band** (see [Constitution (§xxix)](10_constitution.md)). Net effect",
    ),
    (
        "See Immutable Parameters (`10_constitution.md` §xxix) for the exact step size, clamp band, and dead zone — all immutable from block 0.",
        "See [Immutable Parameters (§xxix)](10_constitution.md) for the exact step size, clamp band, and dead zone — all immutable from block 0.",
    ),
    (
        "See Immutable Parameters (`10_constitution.md` §xxix).",
        "See [Immutable Parameters (§xxix)](10_constitution.md).",
    ),
    (
        "see Immutable Parameters (`10_constitution.md` §xxix)",
        "see [Immutable Parameters (§xxix)](10_constitution.md)",
    ),
    (
        "All parameters listed here are **immutable from block 0**. See Immutable Parameters (`10_constitution.md` §xxix).",
        "All parameters listed here are **immutable from block 0**. See [Immutable Parameters (§xxix)](10_constitution.md).",
    ),
    (
        "*All formulas are immutable from block 0. See Immutable Parameters (`10_constitution.md` §xxix) for the full list.*",
        "*All formulas are immutable from block 0. See [Immutable Parameters (§xxix)](10_constitution.md) for the full list.*",
    ),
    (
        " — see Immutable Parameters (`10_constitution.md` §xxix) for the exact values",
        " — see [Immutable Parameters (§xxix)](10_constitution.md) for the exact values",
    ),
    (
        "the number is immutable from block 0 — see `10_constitution.md` §xxix.",
        "the number is immutable from block 0 — see [Constitution (§xxix)](10_constitution.md).",
    ),
    (
        "linear transition from equal to CCB (Continuous Central Bank — the protocol's fully automatic emission allocator; see `12_aureum_glossary.md`). **α**",
        "linear transition from equal to CCB (Continuous Central Bank — the protocol's fully automatic emission allocator; see [Glossary](12_aureum_glossary.md)). **α**",
    ),
    (
        "see `09_transitions.md`",
        "see [Transition rules](09_transitions.md)",
    ),
    (
        "See `09_transitions.md`",
        "See [Transition rules](09_transitions.md)",
    ),
]


def main():
    changed = []
    for path in iter_md():
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in REPL:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            changed.append(path.relative_to(ROOT))
    for c in sorted(changed):
        print(c)


if __name__ == "__main__":
    main()
