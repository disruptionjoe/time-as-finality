# Executing the Triage Recommendation: three separable problems + harvest

Execution note, 2026-07-07. **Analysis is method, not evidence. No claim moves in any repo. From-memory physics
flagged.** Executes the recommendation of `meta-finding-triage-2026-07-07.md` (verdict: the "three lines -> one
unbuilt object" meta-finding was an ARTIFACT; the three problems are independent; harvest (B), pursue the two
un-gated lines now, park the third). Each line addressed to the grade it currently supports.

## Line 1 -- FINALITY: the operational discriminator, BUILT (un-gated, TaF-native)

`models/finality_records_vs_redundancy_discriminator.py`, exit 0. The blind reduction gave FINALITY its own
minimal object -- an operational discriminator, NOT GU's source action. Built on a minimal Krein carrier, it
makes T12''s "necessary-not-sufficient" precise:

- **Records-vs-redundancy is a well-defined FUNCTION of the admissible-operation algebra.** Recovery of the
  W- (mirror) difference into the physically-read-out W+ sector: **0 under the individual / positivity-preserving
  algebra** (block-diagonal, T12''s individual-accessible ops) -> REDUNDANCY; **0.76 under the full-Krein
  collective algebra** (W+<->W- boosts) -> RECORD.
- **The whole question collapses onto ONE sharp dichotomy:** is physicality defined by POSITIVITY (Turok-Bateman:
  physical = positivity-preserving = block-diagonal, so the ghost is gauge REDUNDANCY -- the STANDARD reading),
  or by the FULL KREIN structure (ghost-parity / Krein quantization: the negative-norm sector is physical, so
  collective ops are admissible -- RECORD)?
- **Honest lean: under the standard criterion (positivity), the verdict is REDUNDANCY.** The RECORD reading
  requires the non-standard ghost-parity bet that full-Krein collective operations are physically admissible.

**Status: this line is DONE at the grade available.** The discriminator is built; it confirms FINALITY needs no
source action to be STATED; and it reduces the entire finality residual to a single, crisp, previously-diffuse
bet (ghost-parity physicality). The one remaining question -- are collective full-Krein operations dynamically
realizable? -- is now isolated, and it ties to the ghost-parity/Krein-quantization synthesis
(`gu-formalization/canon/ghost-parity-krein-synthesis.md`), not to the GU source action.

## Line 2 -- COUNT: the index-that-outputs-3 probably does NOT exist (reinforces located-not-forced)

The blind reduction gave COUNT its minimal object -- "a Z-valued INDEX that outputs 3" -- and BOTH framings
flagged the load-bearing prior question: *does an integral (non-torsion) lift of the located mod-3 class exist
at all?* The earlier Z/3-vs-triality swing (`gu-formalization/explorations/big-swing-2026-07-07/
BLIND-SPOT-4-Z3-VS-TRIALITY-PERSPECTIVE-GATE.md`) already answered it via Barratt-Priddy-Quillen: the count is a
**COLORING** (mod-n torsion class), not a **MONOVARIANT** (integer); only `pi_0^s = Z` (cardinality) counts,
every higher stem is a coloring with no integer content, and `Hom(torsion, Z) = 0`. And the count's canonical
home `tmf_3 = Z/24` is still torsion (a Q/Z anomaly order), not an integer.

**Reconciliation: the object COUNT reduces to (an index outputting the integer 3) almost certainly does not
exist** -- the located class is a coloring with no integer lift. So the honest COUNT result is a **negative that
CONVERGES with `located-not-forced`**: the count is not index-derivable because it is the wrong kind of object
(a coloring / anomaly order, not a cardinality); it stays a posited external boundary datum. No new build is
warranted; the two independent lines (the paper's index-theoretic no-go and this reduction's coloring finding)
now agree. **Status: settled as a negative that strengthens the existing paper.**

## Line 3 -- MASS GAP: parked as a bounded option (per the recommendation)

MASS GAP is the ONLY line that genuinely reduces to GU's source action, which the specification triage found
**PARTIAL** (bare form types; definiteness gated on the unbuilt Y14 geometry; kinetic operator a non-unique
3-parameter family -> "count may be observer-relative"). Per the recommendation, this is **not** a build
target now -- it is a bounded option, contingent on GU's own program building the stabilized-twisted action on
Y14. No effort committed here; parked with its precise gate recorded. (Note: the non-uniqueness of the kinetic
operator independently re-derives "located, not forced" from the action side and ties the count's
non-uniqueness to the observer/system gauge -- a cross-check, not a new claim.)

## Harvest (B): the GU-independent methodological yield of the session

The triage's core point: the durable value of this work is largely GU-independent and already banked. Indexed
here so it is not lost when the physics lines are parked:

- **Category-theoretic method correctives** (CT-1 Name-the-Category, CT-2 Prefer-the-Limit, CT-3
  Check-Presentation-Equivalence + the dinosaur guard) --
  `ai-epistemology/field-guide/branch-5-evolvability/category-theoretic-method-correctives.md`, registry-logged.
- **Explanatory Realism Discipline** (inference to the best, hardest-to-vary explanation; unobservable != mere
  choice) -- `ai-epistemology/METHOD.md`.
- **The de-correlation / reduce-twice discriminator** for routing-induced (manufactured) convergence -- which
  just caught this program's OWN over-lumping (the retracted meta-finding). A reusable immune response.
- **The boundary-adapter-as-functor machinery** (`models/boundary_adapter_functor*.py`, `boundary_adapter_second_ti.py`)
  -- two independently-forced adapters into the proven `D1Cat`; a concrete template for turning an
  analogy-grade bridge into a checked functor, GU-independent.
- **The FINALITY discriminator** (this note, Line 1) -- TaF-native, GU-independent, and the one piece of the
  finality account that survives as a live (if promissory) explanandum after the best-explanation swing.
- **The physics-from-a-finite-observer frame** at organizing-principle grade (NOT a winning explanation of the
  arrow -- the swing settled that) -- `physics-from-a-finite-observer-and-the-observer-system-gauge-2026-07-07.md`.

## Net program state after execution

The program does not have one load-bearing wall. It has three independent problems: **FINALITY** reduced to a
built discriminator and a single isolated bet (done at grade); **COUNT** settled as a negative that reinforces
`located-not-forced` (the index doesn't exist; the count stays posited); **MASS GAP** parked on the PARTIAL GU
source action. The physics claims sit at organizing-principle / promissory grade; the methodological and
mathematical machinery is the banked, GU-independent value. No claim moves in any repo.

## Verifier note (main loop)

Line 1 built and run (exit 0); its verdict leans REDUNDANCY under the standard positivity criterion and isolates
the record reading to the ghost-parity bet -- an honest lean against the home team's hoped-for reading, on the
existing carrier, no source action needed. Line 2 is a negative reconciliation that strengthens an existing
paper, not a new claim. Line 3 is explicitly NOT built (parked per recommendation). Harvest is an index of
already-filed GU-independent artifacts. Nothing here promotes any claim; from-memory physics flagged. -- main loop

## Governed artifact pointer: T507

T507 (`tests/T507-finality-record-redundancy-double-gate.md`) now carries the repo-governed executable version
of Line 1. It preserves the negative default: positivity-preserving/block-diagonal operations recover no W-
difference, while full-Krein recovery plus self-normalized observation is admitted only as a hidden-record
review target. T507 does not decide BRST exactness, Krein quantization, source-action truth, mass-gap evidence,
claim status, public posture, external publication, or cross-repo truth.

## Governed artifact pointer: T508

T508 (`tests/T508-brst-cohomology-record-admission-gate.md`) now converts the
remaining BRST/exactness bottleneck for Line 1 into a finite admission gate. In
the synthetic fixture, an exact mirror routes to redundancy; a Q-closed but
non-exact mirror is admitted only as a review target when T507's full-Krein and
self-normalized gates are also paid. This sharpens the next packet burden
without deciding real BRST exactness, BRST nontriviality, source-action truth,
mass-gap evidence, claim status, public posture, external publication, or
cross-repo truth.
