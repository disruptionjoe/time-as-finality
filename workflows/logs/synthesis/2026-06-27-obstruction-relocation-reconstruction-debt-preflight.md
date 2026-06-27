---
document_type: synthesis_preflight
queue_item: 8
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/obstruction-relocation-reconstruction-debt.md
---

# Obstruction Relocation Reconstruction Debt Preflight

## Scope

This is a preflight artifact for the bounded audit proposed in
`open-problems/obstruction-relocation-reconstruction-debt.md`, tentatively named
`T102: Obstruction Relocation Audit`.

The run should test whether apparent obstruction removal under an
information-losing morphism is better classified as preservation,
degree-lowering, relocation into bookkeeping, genuine elimination, or
non-admissibility.

This preflight does not assert a conservation law and does not promote
obstruction relocation into a theorem.

The source open problem is marked dormant. This preflight keeps the line dormant
until a bounded audit exists with classified cases, a negative control, and at
least one non-circular reconstruction-debt observable.

## Preferred Language

Use:

```text
conservation-law temptation
obstruction relocation
reconstruction debt
obstruction accounting
degree-lowering flow
```

Avoid:

```text
conservation of obstruction
conservation of information
obstruction cannot be eliminated
```

The audit is allowed to preserve the intuition that reconstruction obligations
move, but it must not imply an invariant, equivalence relation, or balance
equation unless those are explicitly constructed.

## Candidate Cases

The next run should classify at least four existing artifacts or artifact
families from this list:

| Case | Expected obstruction surface to inspect |
| --- | --- |
| T39 | CSP obstruction with PO1 typed source/loss and admissibility layers |
| T63/T65 | global assignment failure as holonomy or causal-boundary obstruction |
| T68/T72/T74 | provenance cannot be inferred from outcomes; obligation moves to protocol assumptions or raw-log provenance |
| T73 | path dependence organized by composed LossKernel |
| Pati-Salam typed forgetting | preserved dimension versus lost `T3R` structure |

The executor should also include one negative control where a projected
obstruction genuinely disappears because the source obstruction is irrelevant
or non-admissible for the target.

## Required Per-Case Schema

Each case must fill the schema from the open problem:

```text
source_obstruction
projection_or_loss_morphism
target_obstruction
relocated_layer
reconstruction_debt_measure
failure_degree_before
failure_degree_after
classification
```

Allowed `relocated_layer` values:

```text
object_level_inconsistency
missing_provenance
forgotten_structure
losskernel_data
admissibility_conditions
accessible_witness_or_gap_data
protocol_assumptions
reconstruction_uncertainty
none
unresolved
```

Allowed `classification` values:

```text
preserved_obstruction
degree_lowered
relocated_to_losskernel
relocated_to_provenance
relocated_to_admissibility
relocated_to_gap
genuinely_eliminated
non_admissible_source_obstruction
unresolved
```

## Reconstruction-Debt Observables

At least one case must define a non-circular observable that is not merely a
prose restatement of `forgotten_structure`.

Allowed observable shapes include:

```text
fiber_multiplicity              number of source lifts over the same target data
witness_count_gap               missing witness obligations required to certify the target verdict
minimum_repair_fields           smallest named fields that restore reconstruction
posterior_ambiguity_bound       lower bound on reconstruction uncertainty
protocol_assumption_count       number of extra protocol assumptions required after projection
path_order_sensitivity          number of target-equivalent paths with different composed loss
```

The run must state why the observable is computed from the fixture rather than
copied from a LossKernel or metadata label.

## Preflight Protocol

1. Select four positive cases and one negative control before classification.
2. Freeze the source obstruction and projection or loss morphism for each case.
3. Record the target-side obstruction visible after projection.
4. Compute or bound one reconstruction-debt observable for at least one case.
5. Assign the relocated layer and classification from the controlled lists.
6. State whether each case shows relocation, degree-lowering, genuine
   elimination, non-admissibility, or unresolved behavior.
7. Decide whether the taxonomy compresses multiple results or merely renames
   metadata already present in each artifact.

## Acceptance Criteria

The audit is accepted as useful only if all of the following hold:

- At least four cases are classified using the same per-case schema.
- At least one negative control reports genuine elimination or
  non-admissibility rather than forced relocation.
- At least one reconstruction-debt observable is computed or bounded without
  circularly reading the LossKernel label back into the result.
- The audit distinguishes source obstruction, target visible obstruction, and
  relocated obligation.
- The verdict for each case is one of the allowed classifications.
- The final summary states whether the result supports a stable relocation
  taxonomy, only a review lens, or demotion of the conservation-law temptation.

## Null Or Demotion Conditions

Demote the line to a review lens if any of these occur:

- Every case reduces to "we chose to record the missing structure in metadata."
- The classification assumes every source obstruction must matter to every
  target.
- Reconstruction debt cannot be measured without circularly reading
  LossKernel labels back into the result.
- The taxonomy cannot distinguish relocation from genuine elimination.
- The negative control is forced into relocation despite target irrelevance or
  non-admissibility.
- The result needs exact conservation-law language to sound meaningful.

Null result language to preserve:

```text
The audit did not find a stable obstruction-relocation invariant or taxonomy.
The safe use is a review lens for tracking where reconstruction obligations are
bookkept after projection.
```

## No-Promotion Guardrails

- Do not call the result a conservation law.
- Do not claim obstruction, information, or reconstruction debt is conserved.
- Do not infer a cohomological degree hierarchy beyond the specific cases.
- Do not promote T102 or this preflight into a main research line.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, models, results, README,
  or open-problem files from this preflight.
- Do not treat relocation language as evidence that lost information is
  recoverable.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-t102-obstruction-relocation-audit.md
```

Required sections:

```text
case_selection
negative_control
per_case_schema_table
reconstruction_debt_observable
classification_table
taxonomy_compression_check
null_or_demotion_check
no_promotion_guardrail_check
verdict
```

Minimum machine-readable table columns:

```text
case_id
source_obstruction
projection_or_loss_morphism
target_obstruction
relocated_layer
reconstruction_debt_measure
failure_degree_before
failure_degree_after
classification
evidence_artifact
```

Permitted final verdicts:

```text
stable_relocation_taxonomy_candidate
review_lens_only
degree_lowering_only_under_named_hypotheses
demote_conservation_law_temptation
inconclusive_missing_observable
```
