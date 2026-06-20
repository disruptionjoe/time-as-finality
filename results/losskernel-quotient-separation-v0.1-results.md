# T99 Results: LossKernel Quotient Separation

## Cases

| Case | Family | Naive labels | Verdict | Purpose |
| --- | --- | --- | --- | --- |
| collision_path_relevant_witness | same_naive_quotient_collision | branch_selector | admissible_typed_attribution | Same ordinary endpoint data as the decorative path, but the lost branch_selector is a source-side witness resolving the target ambiguity. |
| collision_path_decorative_label | same_naive_quotient_collision | branch_selector | inadmissible_label_only_metadata | Same ordinary endpoint data and same naive lost label, but the lost branch_selector is only a display annotation. |
| same_typed_alias_a | same_typed_control | branch_selector | admissible_typed_attribution | Control: an alias of the relevant typed witness should collapse. |
| same_typed_alias_b | same_typed_control | branch_selector | admissible_typed_attribution | Control: same typed loss data should not create a new distinction. |
| endpoint_difference_control | endpoint_difference_control | branch_selector | inadmissible_no_target_obstruction | Control: same lost label but a different unobstructed endpoint is not evidence for quotient survival. |

## Naive quotient groups

| Group | Cases | Verdicts | Naive collision | Typed witness separates |
| --- | --- | --- | --- | --- |
| naive_quotient_group_1 | collision_path_relevant_witness, collision_path_decorative_label | admissible_typed_attribution, inadmissible_label_only_metadata | True | True |
| naive_quotient_group_2 | same_typed_alias_a, same_typed_alias_b | admissible_typed_attribution, admissible_typed_attribution | False | False |
| naive_quotient_group_3 | endpoint_difference_control | inadmissible_no_target_obstruction | False | False |

## Audit flags

- Naive label kernel fails quotient gate: True
- Typed witness kernel separates collision: True
- Same-typed control collapses: True
- Endpoint-difference control excluded: True

## Strongest claim

The label-only LossKernel does not survive the quotient gate: two paths can share endpoints, ordinary composite map, endpoint behavior, and naive lost-label set while receiving opposite attribution verdicts. A typed witness kernel separates them only if LossKernel records source-anchored witness obligations, not just lost labels.

## What this improved

T99 turns the open quotient-survival worry into an executable audit. It shows exactly where the current T73 union law is too weak and what extra data would be required for TF1 to become a serious attribution object.

## What this weakened

This weakens LossKernel promotion. The current powerset-union object is not enough for quotient/prior-art separation. Without source-anchored witness obligations, LossKernel remains a provenance/effect-style annotation.

## Falsification condition

Reject theorem-level TF1 language if future LossKernel definitions cannot canonically derive witness obligations from the morphism and source/target structures, or if those obligations collapse to ordinary provenance labels under the same quotient.

## TF1 update

TF1 remains an open formal target. T99 supplies a conditional salvage path: typed loss must include source witnesses that resolve target obstructions. Label-only loss is refuted as a sufficient object for the quotient gate.

## Claim ledger update

Add T99 to TF1: naive label-union LossKernel fails quotient survival; only a source-anchored witness-obligation kernel separates same-endpoint, same-map, same-behavior, same-label fixtures, so TF1 remains open and cannot be promoted from T73.

## Open blocker

The typed witness obligations in T99 are still fixture-declared. The next blocker is canonical derivation: the obligation must be computed from a morphism and finite restriction systems, not hand-attached as metadata.

## Recommended next

Rebuild one T34 or T37 fixture with explicit source sections and target obstruction certificates, then derive the T99 witness obligation mechanically from the restriction map.
