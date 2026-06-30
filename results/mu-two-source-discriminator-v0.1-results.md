# mu Two-Source Reversal-Cost Discriminator -- v0.1 Results

**Date:** 2026-06-30
**Verdict:** CONFIRM-WITH-CAVEATS (promotion trigger: FIRE-CONDITIONALLY)
**Backlog anchors:** MC-2 (two-source `mu` conjecture), WC-22 (CA causal-graph substrate), WC-23 (two-way
reversal-cost benchmark). Central work-item of the Temporal-Issuance driving hypothesis
(`temporal-issuance/DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE.md`).
**Artifacts:** `models/ca_harness.py` (verified primitives), `models/mu_experiment.py` (the 2x2 + gates +
decision rule), `models/mu_strengthen.py` (caveat-addressing passes), `models/mu_result.json`,
`models/mu_strengthen_result.json`.
**Process:** pre-registered spec produced by a design workflow (3 independent designs -> adversarial red-team
-> synthesis); result adversarially checked by a verification workflow (6 skeptics -> adjudicator); then two
strengthening passes addressing the adjudicator's caveats. This is exploration-grade; honest grade below.

## Question

Does finality's reversal cost `mu = (INFO bits, COMPUTE bit-ops)` have **two independent sources** --
thermodynamic (Landauer erasure) and computational-irreducibility -- or does it **collapse to one
thermodynamic axis** (in which case finality reduces to thermodynamics: a clean KILL, which is a success for
this kill-by-design program)?

## Method (brief; full detail in the code + the pre-registered spec)

- Substrate: elementary cellular automata on a periodic ring; first-order maps on `n` bits, second-order
  (reversibilized) maps on `2n` bits. Exact full `2^W` enumeration of the global state-transition graph.
- **INFO** (thermodynamic): logical irreversibility = per-step rate `E[log2 indeg]` on the recurrent set.
  **Exactly 0 for a bijection** (every in-degree 1 -> 0 bits; machine-checked, run rejected otherwise);
  `> 0` for non-injective maps.
- **COMP** (computational): `kappa = best_admissible_shortcut_bitops / naive_bitops` in `(0,1]`. Admissible =
  poly(n) build + sub-linear(L) query, verified exact on all states. Battery = global GF(2)-affine +
  affine-after-recoding + k-step block-affine. `kappa = 1` (IRREDUCIBLE) is a **one-sided, documented search
  failure**, never a proof of no shortcut.
- Cells: A (rev+red), **B (rev+irreducible -- isolates the computational source)**, **C (irrev+reducible --
  isolates the thermodynamic source)**, D (irrev+irreducible); plus nonlinear-but-reducible **controls E, C'**
  (conjugation by a Feistel) and **validity gates G1-G6**; replication via Rule 150 (for 90) and Rule 30
  (for 110). The KILL branch was genuinely reachable (e.g. if B came back reducible, or E came back
  irreducible).

## Result

**Double dissociation, all gates G1-G6 pass, replication holds:**

| cell | map | reversible? | INFO | COMP | reading |
|---|---|---|---|---|---|
| A | 2nd-order R90 | yes | 0 | reducible | control |
| **B** | **2nd-order R110** | **yes** | **0 (exact)** | **IRREDUCIBLE (kappa=1, all n)** | **thermo-free yet computationally hard** |
| **C** | **1st-order R90** | **no** | **> 0** | **reducible (kappa->0)** | **thermo-costly yet computationally cheap** |
| D | 1st-order R110 | no | > 0 | irreducible | realistic finality corner |
| E | conj 2nd-order R90 | yes | 0 | reducible | nonlinear control (G3) |
| C' | conj 1st-order R90 | no | > 0 | reducible | nonlinear control (G5) |

**A single-thermodynamic-axis collapse is falsified for the enumerable cases:** B is reversible (INFO=0,
machine-checked) yet not reduced by the battery; C is irreversible (INFO>0) yet reducible. The two axes
occupy both off-diagonal corners.

## Strengthening passes (addressing the verification caveats)

- **C1 (held-out recoding discovery):** with the exact handed Feistel **excluded** from the battery, the
  search **rediscovers a different linearizing recoding** (`F1(1,0,1)`) for E at n=4,5,6. So COMP detects
  nonlinear reducibility it was *not* handed -> **gate G3 is earned by search, not by construction** (defeats
  the "COMP = affine-after-pre-loaded-recoding" deflation), within the searched recoding family.
- **C2 (B robustness):** B survives a broadened single- and two-round Feistel search (`kappa=1`, n=4,5,6) ->
  its irreducibility is robust to a strictly stronger search, not an artifact of a 3-member battery.
- **C3 (population, all 256 rules):** the off-diagonal combinations are **generic, not curated** -- the
  reversible-yet-irreducible corner (cell-B class) is **240/256 second-order rules**, and the
  irreversible-yet-reducible corner (cell-C class) is the 8 first-order affine-non-injective rules. **Honest
  nuance:** within the *first-order* population alone, reversibility implies affine (phi = 0.70, the B-corner
  is empty there); the dissociation requires the second-order reversibilization, but there it is the rule
  (240/256), not a hand-picked exception.

## What this establishes (precise, defensible -- honest grade)

- **Shown (robust):** `INFO` and `COMP` are distinct, dissociable functionals of a single dynamical reversal
  operation; the Landauer axis alone is insufficient to account for reversal cost on these dynamics. Both
  off-diagonal corners are populated by many rules. (This is MC-2, scoped.)
- **Shown only operationally / weakly:** the second axis as "battery-null reducibility." It is one-sided, and
  cell B's hardness is conjecture-backed (Cook universality of Rule 110), not proven here.
- **NOT shown:** (a) that the second axis *is* computational irreducibility in the strong sense -- it is
  "non-affine non-reducibility relative to the searched recoding family"; (b) that `INFO` and `COMP` are
  coordinates of *one* measure `mu` (the bundling is a theory-side overlay, not tested as jointness); (c)
  full statistical independence -- the population shows dissociability and generic off-diagonal occupancy, but
  reversibility and affineness are correlated *within* the first-order family.

## Residual caveats (ranked) + resolving tests

1. **One-sidedness / conjecture-dependence of B.** "Irreducible" = battery-null; B leans on the 110
   conjecture. *Resolve:* a positive lower bound on B's shortcut cost (turns search-failure into fact), or a
   thermo-free-yet-hard witness whose hardness is not Cook-derived.
2. **CA -> finality bridge.** The CA `mu` is the cost of inverting one deterministic global map; finality's
   `mu` is "rising reversal cost across distinct holders," a multi-agent functional the CA cannot instantiate
   (no holders, no sharing). A third axis (holder redundancy) is structurally invisible here. *Resolve:* a
   separate leg instantiating finality-across-holders and testing for a third axis.
3. **"One measure" is assumed, not shown.** State MC-2's `mu` as an abstract reversal-cost functional the CA
   *instantiates*, not a measured joint object.

## Scope

Confirms (caveated) **only MC-2** -- the two-source structure of the reversal-cost functional -- in its
single-system, categorical, operational form. Leaves entirely open: observer-issuance itself, the
multi-holder reversal dimension, H1-gated sharing, and the CA->finality isomorphism. **This is one
necessary-ish leg of the driving hypothesis, far from sufficient; it must not be read as advancing
observer-issuance.**

## Promotion-trigger status

**FIRE-CONDITIONALLY.** `mu` now exists and produced a falsifiable, non-vacuously-confirmed structure with a
genuinely reachable KILL branch. The TI driving hypothesis's promotion trigger is recorded as **conditionally
fired for the scoped MC-2 leg**; full spin-out into an integration repo awaits (a) converting B's battery-null
to a positive hardness fact (or de-correlating it from the 110 conjecture), and (b) the observer / multi-holder
legs that this experiment does not touch.

## Highest-value next experiment

Instantiate the **multi-holder reversal-cost dimension** (the actual finality functional: cost rising across
distinct record-holders) and test whether it is a third axis orthogonal to INFO and COMP -- this both
addresses caveat 2 and is the first step from "reversal cost on a map" toward "finality across observers,"
i.e., toward the observer-issuance hypothesis proper.
