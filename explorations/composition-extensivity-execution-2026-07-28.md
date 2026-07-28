# Composition/Extensivity Gate: Executed ρ₁ Witness and Full Check Slate (Un-T-Numbered Exploration Companion)

**Status:** review-only execution companion — deliberately un-T-numbered. This
run is the reopening packet's own fallback path, executed as written: *"run
the ρ₁ witness of the Setup as an un-T-numbered exploration companion (the
same discipline as the wave-3 note's overlay model) and re-submit this packet
with the run attached."* The owner still mints the T-number and still decides
whether the reopening is accepted; nothing here performs the reopening or
treats it as granted.
**Date:** 2026-07-28
**Executes:** the witness class, success criteria, and must-fail controls of
[proposed-composition-extensivity-gate-2026-07-28.md](proposed-composition-extensivity-gate-2026-07-28.md),
whose definitions bind verbatim throughout this note
**Builds on:** [T583](../tests/T583-capability-contract-v1.md),
[T584](../tests/T584-capability-invariance-morphism-gate.md),
[T585](../tests/T585-landauer-physical-capability-gate.md) (fixture class,
re-executed at run time as source-owned input, not consumed from cached
results), [T586](../tests/T586-record-capability-order-gate.md) (the
unique-producer record mechanism run across the composite boundary),
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md) (the stop and
boundary typing this run operates under),
[T588](../tests/T588-record-issuance-contract-fork-gate.md), and the wave-3
note
[landauer-rate-and-capability-indexed-discriminator-2026-07-27.md](landauer-rate-and-capability-indexed-discriminator-2026-07-27.md)
(the pre-registered extensivity kill this run adjudicates at fixture level)
**Model:**
[../models/composition_extensivity_probe.py](../models/composition_extensivity_probe.py)
(pure stdlib, deterministic — byte-identical output across repeat runs, no
randomness and no wall-clock values in the output; exit 0, all 11 checks pass;
run with `python3 -m models.composition_extensivity_probe` from the repository
root)
**Tags:** `finite_witness` · `execution_companion`

---

## Verdict

**Exit A of the packet's two-exit fork is the exit taken.** On the T585
fixture class, under the packet's declared parallel composition clause:

- **Envelope-level extensivity holds on independent composites**, bitwise
  after canonicalization, on all 36 grid composites:
  Env(C₁ ⊗ C₂) = Env(C₁) ⊕ Env(C₂), with domination sets equal,
  incomparability preserved, and no cross-namespace domination.
- **The record-coupled deviation Δ(ρ) behaves as the packet requires:**
  Δ(∅) = ∅ exactly where extensivity holds; Δ(ρ₁) ≠ ∅ at the witness
  configuration (superadditivity under coupling, as pre-registered);
  Δ(ρ₁) ⊆ Δ(ρ₂) on all 36 grid composites; Δ is invariant under
  componentwise T584 morphisms.
- **All four must-fail controls fail closed.** No control passed; the gate
  has teeth.
- **All T584 extension laws pass** (componentwise preservation, interchange
  square, swap symmetry, associativity, order-compatibility, both
  restriction laws).

Consequence, stated exactly as the packet pre-states it: the wave-3
discriminator spec's pre-registered extensivity kill **un-arms** (does not
fire) at the fixture-class level. The packet's own caveat is quoted verbatim
and inherited in full:

> Un-armed is not alive: canonical contextualization (Part 2 (ii) step 1)
> and a declared T584-invariant scalarization (step 2) remain open burdens
> before any density is actually constructed, and the differential-signature
> design study remains a separate owner decision.

Exit B did not trigger: additivity did not fail on any independent
composite, and no T584 extension law failed. The composition definition
proved coherent when implemented — the order-level ⊕ (namespaced disjoint
union of canonical frontiers with the product preorder) is well-defined on
the envelope representation, and the bitwise-after-canonicalization equality
test is decidable exactly as the packet claims.

## Pre-registered predictions vs outcomes

| # | prediction (registered in the packet, before this run) | outcome | status |
| --- | --- | --- | --- |
| 1 | Envelope extensivity holds on independent composites (additivity is the pre-registered expectation) | bitwise equality on 36/36 budget-pair grid composites; no new Pareto points, no new dominations, incomparability preserved | **CONFIRMED** |
| 2 | Δ(ρ₁) ≠ ∅: a frontier point of the coupled composite with no preimage in ⊕ | Δ(ρ₁) is exactly one canonical frontier point, `ns2::certify_cross_record_stability`, with no preimage in ⊕ and no lost points | **CONFIRMED** |
| 3 | Δ(ρ₁) ⊆ Δ(ρ₂) (monotone in coupling strength) | holds at the witness configuration (1 point ⊆ 2 points) and on 36/36 grid composites | **CONFIRMED** |
| 4 | Δ well-defined: T584-invariant; Δ(∅) = ∅ exactly when independent extensivity holds | Δ(ρ₁) unchanged under componentwise representation, gauge, and coarse-graining morphisms (4/4 legs); Δ(∅) = ∅ ⇔ extensivity on 36/36 | **CONFIRMED** |
| 5 | All four controls must fail (scalarized-capability, namespace-collision, budget-pooling, unequal-bath) | all four failed closed; none stood in for the envelope verdict | **CONFIRMED** |
| 6 | ⊗ satisfies the T584 extension laws (componentwise preservation, interchange, symmetry, order-compatibility, restriction laws) | 9/9 morphism-law rows pass | **CONFIRMED** |

One unregistered refinement was found and is reported rather than smoothed —
see "Adverse-adjacent refinement" below: a declared ρ edge whose producing
record is *unattainable* yields Δ = ∅. This narrows the packet's
"generically" in the superadditivity statement; it contradicts nothing the
packet registered.

## What was implemented (the clause, as bound by the packet)

The probe implements the packet's composition clause on the T585 fixture
class, with every fork resolved the way the packet declares it:

- **Intensive restriction, fail-closed:** equal source theory, equal
  declared bath temperature, **equal-and-shared time budget** (the composite
  window is the shared 5.0, not the 10.0 a serial sum would model), equal
  error bound, equal horizon. Seven mutation probes (bath, time, error,
  horizon, source theory, overlapping regions, duplicate namespace) are each
  rejected with a typed reason; none silently normalizes.
- **Extensive budgets add under the declared partition:** energy,
  communication, and memory budgets add with each namespace's tasks charged
  only against that component's declared share. No pooling.
- **Tagged unions:** every task and record identifier carries its component
  namespace; the untagged merge is rejected.
- **Issuance stays namespaced:** a record is always issued into the
  producing component's namespace; ρ governs consumption only, is declared
  (never inferred), and admits cross-namespace edges only.
- **⊕ on envelopes:** namespaced disjoint union of canonical frontiers with
  the product preorder; comparison is bitwise after canonicalization, plus
  explicit domination-set and incomparability-set comparison (order-level,
  scalar-free throughout — no scalarization appears anywhere in the gate).

Component envelopes are computed by T585's own machinery (`envelope_for`);
T585 is re-executed at run time and its verdict checked, mirroring T586's
source-input discipline.

## Extensivity on independent composites

Grid: states {known (reset cost 0.0), biased (0.468995594), max_entropy
(1.0)} × energy shares {0.30, 0.75} per component = 36 independent
composites at equal bath 300 K, shared time 5.0, error 0.01, horizon
`single_reset_cycle`.

| test | result |
| --- | ---: |
| bitwise canonical equality Env(C₁⊗C₂) = Env(C₁) ⊕ Env(C₂) | 36 / 36 |
| domination sets equal (no new dominations) | 36 / 36 |
| incomparability preserved | 36 / 36 |
| cross-namespace dominations | 0 |
| Δ(∅) = ∅ exactly where extensivity holds | 36 / 36 |

## The record-coupled deviation Δ(ρ)

Witness configuration (the packet's, verbatim): two biased one-bit Landauer
cells, energy 0.75 + 0.75 under the declared partition, task families
{erase_to_standard_record, certify_record_stability} × {ns1, ns2}.

| composite | frontier size | Δ points | Δ induced dominations |
| --- | ---: | ---: | ---: |
| independent (ρ = ∅) | 4 | 0 | 0 |
| ⊗_ρ₁ (ns1 record → ns2 cross-certify) | 5 | 1 | 0 |
| ⊗_ρ₂ = ρ₁ + symmetric edge | 6 | 2 | 0 |

Δ(ρ₁) is exactly the packet's predicted object — one canonical frontier
point with no preimage in ⊕:

| task | success | energy | time | comm | memory | error |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `ns2::certify_cross_record_stability` | 0.995 | 0.05 | 0.2 | 0.1 | 0.1 | 0.002 |

Across the coupled grid: Δ(ρ₁) ≠ ∅ on 18/36 composites, Δ(ρ₂) ≠ ∅ on 27/36,
and Δ(ρ₁) ⊆ Δ(ρ₂) on 36/36. The counts decompose exactly: Δ(ρ₁) is nonempty
precisely when ns1 can execute erase inside its declared share (known
always; biased only at 0.75; max_entropy never = 18), and Δ(ρ₂) is nonempty
unless *both* producers are starved (36 − 9 = 27).

**Δ invariance on T584 orbits (4/4):** joule representation on the producer,
bit-label gauge swap on the producer, gauge swap on the consumer, and
declared coarse-graining on the consumer each leave Δ(ρ₁) unchanged — the
producer-side legs matter, because Δ flows through the record layer: the
producing record's attainability is itself a gauge/representation invariant.

## The ρ₁ witness — the contract question, made concrete

The packet's reopening argument turns on one question the current
record-issuance contract does not answer: *when declared contexts compose,
into which namespace is a record issued, and which tasks may consume records
across the composite boundary?* The run exhibits that different answers
change measured capability:

| contract answer | cross task executable? | frontier | Δ points |
| --- | :---: | ---: | ---: |
| issued into producer namespace; no cross consumption (ρ = ∅) | no | 4 | 0 |
| issued into producer namespace; ns2 may consume ns1's record (ρ₁) | yes | 5 | 1 |
| issued into producer namespace; symmetric consumption (ρ₂) | yes | 6 | 2 |
| record silently re-namespaced across the boundary | — | rejected: `SILENT_REISSUE_ACROSS_BOUNDARY` | — |
| ρ₁ declared but producer starved (ns1 share 0.30 < reset cost 0.468995594) | no | 3 | 0 |

Supporting fail-closed exhibits, all executed: a cross point smuggled into
an independent composite without a declared ρ is inadmissible (task not in
the composite family; envelope unchanged); a same-namespace ρ edge is
rejected (`RHO_EDGE_NOT_CROSS_NAMESPACE`); the unique-producer guard raises
on double production of a record id — T586's admission mechanism, running
across the composite boundary exactly as the packet's counterexample
specifies. This is the executed form of the packet's sharper-counterexample
claim: the composite has an executable task (`certify_cross_record_stability`
in ns2) that neither component has alone, and whether it exists depends only
on the undeclared issuance/consumption clause, not on any component's own
declaration.

## Must-fail controls (all failed closed — the gate has teeth)

| control | what had to fail | outcome |
| --- | --- | --- |
| scalarized-capability | a summed composite scalar standing in for the envelope verdict | two independent composites (known⊗known vs biased⊗biased) with equal scalar totals — 4 = 4 frontier points, success sums 3.988 = 3.988 — while the native relation is `SUPERSET`: the scalar collapses a distinction the native order keeps; rejected as a T583 failure-criterion violation |
| namespace-collision | the untagged task/record-vocabulary merge | rejected `UNTAGGED_NAMESPACE_COLLISION`; the merge would change the native envelope (3 frontier values collapse to 2 — cross-cell domination erases the biased cell's erase point) and doubly produces `r_erased_standard`, violating unique production |
| budget-pooling | reallocating shares across the declared partition counted as capability | pooling 0.30/0.75 → 1.00/0.05 makes `ns1::erase_to_standard_record` feasible (a point neither component affords under the declared partition); classified `RESOURCE_BUDGET_COMPLETION` by T583's own assessor; both partitions remain extensive (Δ = ∅), so the pooled gain never enters any deviation set — never synergy |
| unequal-bath | composition at unequal declared temperatures | rejected `UNEQUAL_BATH_TEMPERATURE` (300 K vs 350 K); no envelope produced, no silent kBT ln 2 renormalization across baths |

## T584 morphism legs (9/9)

| law | result |
| --- | :---: |
| componentwise representation change (joule round-trip on one component) preserves the composite envelope | pass |
| componentwise gauge change (bit-label swap) preserves the composite envelope | pass |
| declared irrelevant coarse-graining preserves envelope and physical payload | pass |
| interchange square: (f₁ ⊗ f₂) ∘ ι_i = ι_i ∘ f_i, and f₁ ⊗ f₂ preserves the composite envelope | pass |
| swap symmetry C₁⊗C₂ → C₂⊗C₁ preserves the envelope | pass |
| associativity ((C₁⊗C₂)⊗C₃ vs C₁⊗(C₂⊗C₃), three-cell) | pass |
| order-compatibility: component covers imply composite cover | pass |
| restriction law, independent: Env(C₁⊗C₂) restricted to namespace i equals ι_i(Env(C_i)) | pass |
| restriction law, coupled: restriction covers ι_i(Env(C_i)) and never loses capability; strict growth exactly in the consuming namespace | pass |

## The two-exit verdict

**Exit A.** Per the packet's "What The Gate Feeds": extensivity holds on
independent composites and Δ is well-behaved, so "a capability rate
*density* becomes definable on independent scaffolds, with Δ the candidate
correction term sourced by cross-namespace record coupling," and the wave-3
pre-registered extensivity kill **un-arms** — it does not fire. The
"un-armed is not alive" caveat is quoted in the Verdict above and applies
without dilution: two named burdens (canonical contextualization; a
declared, T584-invariant, ⊔-additive scalarization) stand between this
result and any actual density, and the differential-signature design study
remains a separate owner decision.

**Exit B did not trigger, and was genuinely live.** The implementation was
built so that an ill-defined ⊕, a grid additivity failure, or any T584
extension-law failure would flip the exit and the exit string; none did.

## Honest notes on strength of evidence

- **Exact equality is partly by construction.** Under the declared partition
  rule, the independent composite's admissibility test per namespace is
  literally the component's own test, so grid equality certifies the
  *coherence* of the clause (that a composition satisfying all the T584 laws
  and fail-closed restrictions simultaneously exists on this fixture class)
  rather than a surprising empirical fact. The packet frames the burden the
  same way — decidable and executable — and the genuinely falsifiable legs
  here were the morphism laws, the controls, and Δ's three requirements.
- **Adverse-adjacent refinement, recorded rather than smoothed:** the
  packet's "under any ρ ≠ ∅ the coupled composite has executable tasks
  neither component has alone, so generically Env(C₁⊗_ρC₂) ⊋ ⊕" acquires a
  measured boundary: a declared edge whose producing record is unattainable
  inside the producer's share yields Δ = ∅ (18 of 36 ρ₁-coupled grid
  composites). Δ is sourced by *attainable* cross-namespace records, not by
  edge declarations. This strengthens the measure reading of Δ (it cannot be
  inflated by declaring dead edges) and slightly sharpens what "coupling
  strength" means: monotonicity in ρ holds, but the increments land only
  where producers are live.
- **Shallow embedding.** The interchange square and (f₁ ⊗ f₂) are executed
  at envelope level over componentwise-morphed cells, not over an abstract
  morphism category; associativity and symmetry are executed over a flat
  component tuple. That matches the packet's declared-contract construction,
  but a deeper categorical formalization would be a separate object.
- **Fixture-class scope.** Two (three, for associativity) one-bit Landauer
  cells, six states, two budget levels, one declared cross-task point. All
  counts are fixture-specific; only the structure is claimed to be exercised.

## Known Physics Constraints

- The only physical source input remains T585's bounded Landauer-style
  erasure cost, re-executed as source-owned input. Nothing else physical
  enters the run.
- The equal-bath restriction did its load-bearing job here as designed:
  unequal-temperature composition is rejected outright, so no heat-engine
  channel can contaminate Δ as a record-coupling measure, by construction
  rather than by measurement.
- The extensive/intensive organization is the contract-level analogy the
  packet declares; nothing here derives a thermodynamic law.
- **No rate constant is established or used; no collapse model is endorsed;**
  the GRW/CSL/Diósi–Penrose comparators of the wave-3 note do not appear.
- Nothing in the run derives time, temporal order, or issuance. Firebreak
  inherited from T587's boundary typing and asserted in the model's output:
  Δ, like any capability delta, is never counted as a record-order edge, an
  issuance, or a temporal quantity by itself.

## What This Does Not Claim

- **No T-number is minted and no reopening is performed.** This run is the
  attachment the packet's fallback path asks for; the owner mints the
  T-number, decides adoption, and decides whether the reopening is accepted.
  No results file is written under `results/`; the model prints its payload
  and exits.
- **No claim movement.** No claim-ledger, Canon Index, hypothesis, Lane,
  or public-posture change; the T585/T586/T587/T588 verdicts are untouched.
- **No density is constructed.** Exit A un-arms a kill; it does not build
  the object the kill guarded. Canonical contextualization and a declared
  T584-invariant scalarization remain open, unattempted burdens.
- **Capability remains T583's operational, executable-task measure and
  nothing else** — not consciousness, not cognition, not awareness, not
  agency. Δ is a task-envelope difference, not a mind-adjacent quantity.
- **No bearing on the foliation branch.** ⊗ composes declared contexts, not
  spacetime slicings.
- **Superadditivity under record coupling is now a fixture-class witness,
  not a general theorem;** independent-composite extensivity is a
  fixture-class result under this clause, not a universal capability law.

## Provenance

- Executed 2026-07-28 against repository main `74e18ce`, as the fallback
  path of
  [proposed-composition-extensivity-gate-2026-07-28.md](proposed-composition-extensivity-gate-2026-07-28.md)
  (Contribution Needed, final sentence).
- Model: `models/composition_extensivity_probe.py`; run command
  `python3 -m models.composition_extensivity_probe`; exit 0; all 11 checks
  pass; output verified byte-identical across two consecutive runs (no
  randomness, no wall-clock values).
- Verdict string emitted by the run:
  `COMPOSITION_EXTENSIVITY_WITNESS_EXECUTED_EXIT_A_INDEPENDENT_ENVELOPE_EXTENSIVITY_HOLDS_REVIEW_ONLY`.
- The packet file carries a dated "Execution attached" pointer to this note
  and the model — that pointer is the re-submission the fallback path
  specifies; everything past that pointer is owner territory.
