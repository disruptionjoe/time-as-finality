# T127 Results: Same-Neighbor-Data LossKernel Audit

## Aggregate checks

- Strict separation found: False
- Positive attempt absorbed: True
- Label-only control collapses: True
- Endpoint-difference control rejected: True
- Path-metadata control rejected: True
- Same-neighbor alias collapses: True
- Absorbed-loss control demoted: True

## Pair audits

| Pair | Classification | Same neighbor data | Left verdict | Right verdict | First absorber |
| --- | --- | --- | --- | --- | --- |
| `positive_attempt` | `absorbed_by_neighbor` | `False` | `candidate_witness_obligation` | `demote_non_attribution_relevant_loss` | `csp_explanation` |
| `label_only_control` | `label_only` | `False` | `candidate_witness_obligation` | `candidate_witness_obligation` | `label_bookkeeping` |
| `endpoint_difference_control` | `invalid_quotient` | `False` | `candidate_witness_obligation` | `inadmissible_no_target_obstruction` | `csp_explanation` |
| `path_metadata_control` | `invalid_quotient` | `False` | `candidate_witness_obligation` | `candidate_witness_obligation` | `path_sensitive_bookkeeping` |
| `same_neighbor_alias` | `demote` | `True` | `candidate_witness_obligation` | `candidate_witness_obligation` | `none` |

## Pair: positive_attempt

- Left case: `positive_attempt_mixed_lifts`
- Right case: `positive_attempt_uniform_false`
- Classification: `absorbed_by_neighbor`
- Same neighbor data: `False`
- Differing neighbor fields: `['csp', 'lenses', 'effect_annotations']`
- First absorber: `csp_explanation`
- Left obligation: `[['left_keep', 'right_keep']]`
- Right obligation: `[]`
- Interpretation: The apparent distinction is already visible to an allowed neighbor package before LossKernel is consulted.

## Pair: label_only_control

- Left case: `label_only_control_a`
- Right case: `label_only_control_b`
- Classification: `label_only`
- Same neighbor data: `False`
- Differing neighbor fields: `['naive_loss_labels', 'path_labels']`
- First absorber: `label_bookkeeping`
- Left obligation: `[['left_keep', 'right_keep']]`
- Right obligation: `[['left_keep', 'right_keep']]`
- Interpretation: Different free labels do not create a new attribution verdict when the source-derived obligation is unchanged.

## Pair: endpoint_difference_control

- Left case: `endpoint_difference_control_a`
- Right case: `endpoint_difference_control_b`
- Classification: `invalid_quotient`
- Same neighbor data: `False`
- Differing neighbor fields: `['csp', 'provenance', 'abstract_interpretation', 'lenses', 'effect_annotations', 'category']`
- First absorber: `csp_explanation`
- Left obligation: `[['left_keep', 'right_keep']]`
- Right obligation: `[]`
- Interpretation: Endpoint behavior changed, so the pair is not admissible evidence for same-neighbor-data separation.

## Pair: path_metadata_control

- Left case: `path_metadata_control_a`
- Right case: `path_metadata_control_b`
- Classification: `invalid_quotient`
- Same neighbor data: `False`
- Differing neighbor fields: `['path_labels']`
- First absorber: `path_sensitive_bookkeeping`
- Left obligation: `[['left_keep', 'right_keep']]`
- Right obligation: `[['left_keep', 'right_keep']]`
- Interpretation: Path labels changed. This is path-sensitive bookkeeping, not strict quotient survival.

## Pair: same_neighbor_alias

- Left case: `same_neighbor_alias_a`
- Right case: `same_neighbor_alias_b`
- Classification: `demote`
- Same neighbor data: `True`
- Differing neighbor fields: `[]`
- First absorber: `none`
- Left obligation: `[['left_keep', 'right_keep']]`
- Right obligation: `[['left_keep', 'right_keep']]`
- Interpretation: When every neighbor-visible package is the same, the deterministic source-derived obligation and verdict collapse as well.

## Single-case audits

### absorbed_loss_control

- Classification: `demote`
- Verdict: `demote_non_attribution_relevant_loss`
- Obligation: `[]`
- Interpretation: Non-empty loss with uniform lift verdicts is not attribution-relevant for the strict T127 gate.


## Strongest claim

No strict same-neighbor-data LossKernel witness survives in the current finite fixture family. Every attempted separation is either absorbed because an allowed neighbor package already changes, a label-only or path-metadata variant, an endpoint-difference control, or an absorbed-loss case with no source-derived witness obligation.

## What this improved

T127 turns the strongest remaining TF1 gate into an executable negative audit. The repo no longer needs to leave same-neighbor-data separation open by default for the current finite witness family.

## What this weakened

This weakens the LossKernel program again. In the tested family, a typed source-derived obligation does not produce a prior-art-separated attribution verdict once CSP, provenance, abstraction, lens, effect, path, and categorical packages are held to the same standard.

## Falsification condition

T127 fails in TF1's favor only if a future finite pair keeps every declared neighbor-visible package fixed and still yields different derived obligations or attribution verdicts. No such pair exists in the current audit.

## TF1 update

TF1 remains an open formal target, but T127 removes the default hope that same-neighbor-data quotient separation will emerge automatically from the current finite LossKernel semantics.

## Claim ledger update

Add T127 to TF1: the same-neighbor-data audit is negative on the current finite fixture family. Apparent separations are absorbed by neighbor-visible CSP/provenance/abstraction/lens/effect/path/category data, or collapse as label-only, endpoint-difference, or absorbed-loss controls.

## Open blocker

The only remaining non-redundant value is a canonical normal form or integration vocabulary for source-derived witness obligations. That is weaker than a prior-art-separated theorem.

## Recommended next

Stop treating same-neighbor-data separation as the default TF1 rescue. Either formalize LossKernel purely as integration vocabulary, or shift effort to T125/T126 where internal mathematical movement is still live.
