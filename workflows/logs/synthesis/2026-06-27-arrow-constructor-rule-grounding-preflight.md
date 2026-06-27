---
document_type: synthesis_preflight
source_queue_item: fourth_batch_4
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/arrow-of-time-as-constructor-theorem.md
---

# Arrow Constructor Rule Grounding Preflight

## Status

Non-authoritative preflight artifact for fourth-batch task 4. This file does
not edit claim, roadmap, test, model, result, README, or open-problem surfaces.
It is not H7 promotion, not thermodynamic-arrow evidence, and not a physical
derivation of time's arrow.

## Read Surfaces

- `open-problems/arrow-of-time-as-constructor-theorem.md`.
- `tests/T18-finality-direction-theorem.md`.
- `tests/T152-metastable-record-deletion-screen.md`.
- `workflows/logs/synthesis/2026-06-27-h7-physical-deletion-substrate-preflight.md`.

## Preflight Question

T18 proves a conditional finite theorem: if transformations are admissible only
when no D1 coordinate decreases, strict finalization edges form an acyclic
partial order and their reverses are impossible under the same rule.

The missing burden is physical grounding of the rule:

```text
admissible(transform) iff D1(after) >= D1(before) componentwise
```

This preflight prepares a bounded artifact that asks whether a named finite
record substrate can justify that constructor rule without hiding absorber
data. The target is not to find a long-lived or high-cost record. The target is
to classify named transformations as possible, practically irreversible, or
constructor-impossible under matched accounting.

## Current Constraint

T152 blocks the simplest metastability shortcut. Finite barriers supply
lifetime and retention capability, but they do not by themselves make deletion
constructor-impossible. Infinite barriers and denied controls are constructor
or boundary stipulations unless the candidate gives a finite operational
reading.

The next artifact must therefore keep these fields visible before any arrow
language appears:

```text
barrier
reservoir
erasure_work_budget
blank_capacity
sink_or_export_history
observer_or_control_boundary
provenance
source_copy_status
reversible_control_access
task_horizon
```

## Frozen Object Required Before Execution

Any future executable packet must freeze one substrate and one transformation
family before evaluation.

| Field | Required content |
| --- | --- |
| `substrate_id` | Named finite physical record substrate. |
| `record_token` | Substrate-native encoding of the record. |
| `state_space` | Finite states audited by the packet. |
| `d1_profile_definition` | Four D1 coordinates used by T18, with substrate-native measurement rules. |
| `transformation_family` | Candidate writes, stabilizations, reads, deletions, restorations, and controls. |
| `strict_finalization_edge` | At least one before/after pair with a strict D1 increase. |
| `reverse_edge_candidate` | The reverse operation claimed impossible. |
| `absorber_vector` | Barrier, reservoir, sink, capacity, boundary, provenance, source-copy, and reversible-control data. |
| `allowed_control_class` | Controls available to decide possible versus impossible. |
| `practical_irreversibility_threshold` | Horizon or resource bound used only for the practical class. |
| `constructor_impossibility_rule` | Finite, substrate-native reason a reverse is impossible after all absorbers are matched. |

## Preflight Protocol

1. Freeze the substrate packet and D1 coordinate definitions.
2. Enumerate the declared transformation family.
3. Compute D1 profiles for all before/after pairs in the finite audit.
4. Mark strict finalization edges using the T18 rule.
5. For each strict edge, evaluate the reverse under the same matched absorber
   vector.
6. Classify each reverse as:

```text
possible_reversible
possible_practically_irreversible
constructor_impossible_after_full_accounting
undefined_missing_absorber_data
```

7. Run T152-style controls for finite barrier, infinite idealization,
   denied-control, hidden reservoir, hidden sink, and hidden source-copy cases.
8. Compare the resulting transformation relation with the D1-monotone
   admissibility rule.
9. Emit a verdict without updating any claim status.

## Acceptance Criteria

The next artifact is accepted as decision-grade only if all of the following
hold:

- A named finite substrate and record token are frozen before scoring.
- The D1 profile is computed from substrate-native data rather than assigned by
  narrative.
- The transformation family includes both forward and reverse candidates.
- At least one strict finalization edge is identified.
- All absorber fields listed above are matched or explicitly marked as missing.
- A reverse classified as constructor-impossible is not merely high-cost,
  finite-rate unlikely, control-denied, source-copy hidden, sink-limited, or
  horizon-limited.
- Practical irreversibility and constructor impossibility are kept as separate
  verdict classes.
- The thermodynamic-cost proxy, if present, is recorded as a side channel and
  not used to orient the edge.
- The final relation remains a partial order or partial preorder, not a hidden
  total order.
- The verdict is one of:

```text
rule_grounded_for_named_substrate
practical_only_no_constructor_grounding
null_absorbed_by_T152_controls
insufficient_packet
```

`rule_grounded_for_named_substrate` means only that one finite substrate packet
is worth promoting to a later audit. It does not promote H7 or the arrow
constructor theorem.

## Null Or Demotion Conditions

Demote the candidate to null for constructor-rule grounding if any condition
holds:

- No named finite substrate is supplied.
- The claimed impossible reverse is only finite-barrier metastability.
- The reverse becomes available after restoring matched work, reservoir, sink,
  blank capacity, source-copy, provenance, or reversible-control data.
- The result depends on an infinite barrier, perfect code, exact
  superselection rule, or horizon-only inaccessibility without finite
  operational content.
- Observer access denial is confused with substrate-native impossibility.
- The D1 coordinates are chosen after seeing which direction should pass.
- The edge orientation is inherited from entropy, coordinate time, proper time,
  or a thermodynamic cost proxy.
- The relation collapses into a total order over states.
- The packet hides absorber data in the definition of admissibility.

Null result language to preserve:

```text
The named substrate did not ground the constructor admissibility rule. The
observed asymmetry is currently practical irreversibility, boundary/control
restriction, or absorber-accounting residue, not physical constructor evidence
for H7.
```

## No-Promotion Guardrails

- Do not change H7 out of `weakened_conditional`.
- Do not call T18 a physical theorem; it remains conditional on the
  admissibility rule.
- Do not call finite metastability, long lifetime, high erasure cost, or denied
  control a constructor impossibility.
- Do not convert a single substrate packet into a general arrow-of-time claim.
- Do not claim a thermodynamic-arrow derivation, low-entropy replacement, or
  cosmological boundary-condition result.
- Do not use this preflight to edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests,
  models, results, README, or open-problem files.
- Do not promote from `rule_grounded_for_named_substrate`; that verdict only
  authorizes a later, narrower audit.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-arrow-constructor-rule-grounding-run-card.md
```

Required run-card sections:

```text
substrate_packet
d1_profile_definition
transformation_family
strict_finalization_edges
reverse_edge_audit
absorber_vector_match
T152_controls
thermodynamic_side_channel
partial_order_check
verdict
no_promotion_guardrail_check
```

Minimum verdict record:

```text
artifact_type: arrow_constructor_rule_grounding_run_card
substrate_id:
record_token:
strict_edge_id:
reverse_edge_id:
absorber_vector_matched: true | false
reverse_class:
  possible_reversible | possible_practically_irreversible |
  constructor_impossible_after_full_accounting |
  undefined_missing_absorber_data
thermodynamic_proxy_used_for_orientation: false
T152_control_result:
final_verdict:
  rule_grounded_for_named_substrate |
  practical_only_no_constructor_grounding |
  null_absorbed_by_T152_controls |
  insufficient_packet
claim_impact: no_status_change
```

If later authorized for implementation, convert the run-card into a
test/model/results triplet only after a frozen packet exists:

```text
tests/TXXX-arrow-constructor-rule-grounding.md
models/run_arrow_constructor_rule_grounding.py
results/arrow-constructor-rule-grounding-v0.1-results.md
```

