---
document_type: synthesis_preflight
batch_item: fourth_batch_task_2
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/gap-presheaf-classification.md
---

# Gap Presheaf Classification Preflight

## Status

This completes fourth-batch task 2 as a synthesis/preflight artifact. It does
not edit `README`, `CLAIM-LEDGER`, `ROADMAP`, tests, models, results, or
open-problem files. It does not promote raw `H0(G)`, physical torsion, or a
universal classification theorem.

## Read Surfaces

- `open-problems/gap-presheaf-classification.md`.
- `tests/T56-sheaf-cohomology-apparent-finality.md`.
- `tests/T57-finality-reflection-property.md`.
- `tests/T58-gap-phantom-equivalence.md`.
- `tests/T113-gap-presheaf-classification.md`.
- `results/gap-presheaf-classification-v0.1-results.md`.
- `technical-reports/TECHNICAL-REPORT-gap-presheaf-classification-v0.1.md`.
- `workflows/logs/synthesis/2026-06-27-t19-t58-common-typed-gap-category-decision.md`.

## Preflight Verdict

The next work should define the typed subobject abstractly. T113 already
refutes raw `H0(G)` as too broad in the tested finite family and supports a
typed subobject with endpoint access, canonical ambient completion,
`F(U) subset A(U)`, and local incomparability.

The open burden is not "does raw `H0(G)` classify phantoms?" The preflight
answer is no. The open burden is:

```text
Can the typed subobject be defined without a witness-by-witness checklist, and
can it be compared to the T19 accessible-witness gap as a different typed
instance of the same degree-0 gap schema?
```

## Raw Versus Typed Language

Raw gap object:

```text
G(U) = A(U) - F(U)
```

Raw `H0(G)` means all compatible computed gap sections. It is diagnostic, but
not a classifier. T113 found extra raw gaps from noncanonical T53 repair and a
T58 local-reversal control.

Typed subobject:

```text
G_tau(U) = {s in A(U) - F(U) | tau_U(s)}
```

`tau_U` is a patch-local typing predicate that must be defined before the
witness family is evaluated.

For the T56/T57/T58/T113 order-pair track, the candidate predicate is:

```text
tau_U(a,b) holds iff
  endpoints a and b are accessible at U;
  the ambient completion used by A(U) is canonical;
  F(U) subset A(U);
  (a,b) is locally incomparable, not locally reversed or conflicting;
  restriction preserves the order-pair type and endpoint access predicate.
```

This is the object that may classify phantom incomparability in the tested
finite family. Raw `G` remains broader than the classifier.

## Abstract Definition Target

The next artifact must express the typed subobject without naming only the
current fixtures. Recommended abstract schema:

```text
TypedGapSubobject X_tau =
  (Patch, Section, type, rho, A, F, G, tau)

where:
  Patch is a finite observer-cover or patch poset.
  Section(U) is the typed section domain at U.
  rho_{U,V} is type-preserving restriction.
  A(U) is ambient content restricted to U.
  F(U) is local/apparent content at U.
  G(U) = A(U) - F(U).
  tau_U selects well-formed classifier sections.
```

Well-formedness gates:

```text
ambient_restriction: rho(A(U)) subset A(V)
local_reflection_or_frp: F(V) subset rho(F(U)) when required
extension_gate: F(U) subset A(U)
typing_stability: type(rho(s)) = type(s)
classifier_predicate_stability: tau_U(s) implies tau_V(rho(s)) when defined
canonical_ambient_gate: noncanonical completions are diagnostic only
```

The classification target is:

```text
typed global sections of G_tau classify phantom incomparability witnesses
in the declared finite family.
```

It is not:

```text
raw H0(G) classifies all possible gaps in arbitrary observer covers.
```

## T19 Comparison Gate

T19/T92 may be compared only at the typed degree-0 gap-schema level:

| Track | Section sort | Classifier target | Common structure | Boundary |
| --- | --- | --- | --- | --- |
| T56/T57/T58/T113 | Non-reflexive event-order pairs | Phantom incomparability | Ambient content present, local content missing | Needs endpoint access, canonical ambient completion, `F subset A`, local incomparability |
| T19/T92 | Unary typed propositions about an observer | Accessible-witness proposition gap | Ambient proposition true, local audit missing | Needs witness monotonicity, stable proposition typing, no semantic relabeling |

The comparison must not identify proposition sections with order-pair sections.
The only admissible common object is a typed degree-0 gap schema or category
whose section sort remains explicit.

## Acceptance Criteria

- Raw `H0(G)` and typed `G_tau` are separated in terminology and verdicts.
- The typed predicate `tau` is defined before examples are evaluated.
- The definition is abstract enough to apply outside the named T51/T52/T53/T56
  fixtures, even if the evidence remains finite.
- T57 Finality Reflection Property or an equivalent local-reflection condition
  is identified as load-bearing for restriction closure.
- T58 local-reversal controls and malformed `F(U) not subset A(U)` controls are
  rejected before phantom language is used.
- T53 noncanonical completions are quarantined as diagnostic, not canonical
  phantom witnesses.
- T19 comparison is included as a typed-schema comparison, not as an identity of
  presheaves or sections.
- The final verdict is one of:

```text
typed_subobject_definition_ready
typed_subobject_needs_more_controls
raw_h0_only_refuted_no_typed_replacement
classification_refuted_by_typed_counterexample
```

## Null Or Demotion Conditions

Demote the classification claim if any condition holds:

- The typed predicate is only a checklist over current positive examples.
- Raw `H0(G)` is used as the classifier despite known extra raw gaps.
- A typed gap section exists that is not an independently computed phantom.
- An independently computed phantom is absent from the typed subobject.
- Local reversal or local/ambient conflict is counted as phantom
  incomparability.
- A noncanonical T53 completion is treated as canonical evidence.
- The T19 comparison requires semantic relabeling between unary propositions
  and order pairs.
- The result depends on physical torsion, GU geometry, or imported sheaf
  language not represented by the TaF finite object.

Demotion language to preserve:

```text
Raw H0(G) remains a diagnostic gap inventory, not a classifier. The finite
phantom-incomparability classification is supported only for a typed subobject
with explicit well-formedness gates.
```

## No-Promotion Guardrails

- Do not claim raw `H0(G)` classifies phantom incomparability.
- Do not claim a universal gap classification theorem.
- Do not claim physical torsion, a torsion tensor, GU validation, or imported
  geometric structure.
- Do not claim that `F` sheafifies to `A`.
- Do not derive finality-arrow direction from this track.
- Do not merge T19 proposition gaps and T58 order-pair gaps into one untyped
  presheaf.
- Do not edit ledger, roadmap, tests, models, results, README, or open-problem
  files from this preflight.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-typed-gap-subobject-definition-card.md
```

Required fields:

```text
artifact_type: typed_gap_subobject_definition_card
section_sort:
patch_poset:
restriction_maps:
ambient_object_A:
local_object_F:
raw_gap_G:
typed_predicate_tau:
  endpoint_or_witness_access:
  canonical_ambient_completion:
  extension_gate_F_subset_A:
  local_incomparability_or_local_audit_gap:
  stable_typing:
restriction_closure_obligation:
classification_target:
positive_family:
negative_controls:
  raw_h0_extra_gap:
  local_reversal:
  noncanonical_completion:
  semantic_relabeling:
t19_comparison:
verdict:
claim_effect: none
no_promotion_guardrail_check:
```

If later authorized for implementation, the executable run should separately
report raw gaps, typed gaps, independent phantom witnesses, extras, and misses.
This preflight does not create or modify that implementation surface.
