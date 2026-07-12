# T528 Results: S1 Finality-Native Generator Preflight

## Verdict

- Verdict: `s1_finality_native_generator_preflight_rejects_first_packet`
- Generator: `two_receipt_finality_generator`
- Repaired-suite samples passing: 25/32 (0.7812)
- Main packet classification: `rejected_repaired_suite_incomplete`
- Main packet counts as S1 evidence: `False`
- Hostile controls rejected: `True`

## Generator Basis

Generate record events with two independent local receipt orders. Declare x<y only when both receipt orders place x before y. The packet uses local receipt comparability, not imported Lorentzian light-cone coordinates, and is audited against the T525 repaired suite.

## Pass Summary By Size

| n | samples | pass count | pass rate |
| ---: | ---: | ---: | ---: |
| 8 | 8 | 7 | 7/8 (0.8750) |
| 12 | 8 | 5 | 5/8 (0.6250) |
| 16 | 8 | 8 | 8/8 (1.0000) |
| 20 | 8 | 5 | 5/8 (0.6250) |

## Failed Sample Audits

| n | seed | T126 class | frac | height | width | max interval | reason |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 8 | 0 | `order_dimension_obstruction` | 3/4 (0.7500) | 5 | 3 | 5 | order-dimension quarantined, but ordering_fraction_outside_t525_band |
| 12 | 2 | `passes_filter_only` | 6/11 (0.5455) | 7 | 4 | 8 | height_outside_t525_band |
| 12 | 5 | `order_dimension_obstruction` | 49/66 (0.7424) | 7 | 4 | 7 | order-dimension quarantined, but ordering_fraction_outside_t525_band, height_outside_t525_band |
| 12 | 6 | `order_dimension_obstruction` | 23/33 (0.6970) | 7 | 3 | 9 | order-dimension quarantined, but ordering_fraction_outside_t525_band, height_outside_t525_band, width_outside_t525_band, largest_interval_outside_t525_band |
| 20 | 3 | `order_dimension_obstruction` | 11/19 (0.5789) | 7 | 7 | 16 | order-dimension quarantined, but ordering_fraction_outside_t525_band, largest_interval_outside_t525_band |
| 20 | 4 | `order_dimension_obstruction` | 123/190 (0.6474) | 7 | 6 | 13 | order-dimension quarantined, but ordering_fraction_outside_t525_band |
| 20 | 7 | `order_dimension_obstruction` | 117/190 (0.6158) | 7 | 5 | 13 | order-dimension quarantined, but ordering_fraction_outside_t525_band |

## Hostile Controls

| control | n | T126 class | repaired pass | reason |
| --- | ---: | --- | :---: | --- |
| `one_channel_chain_control` | 8 | `rank_width_obstruction` | False | hard T126 gate rejected: rank_width_obstruction |
| `hub_order_control` | 8 | `hub_nonlocality_obstruction` | False | hard T126 gate rejected: hub_nonlocality_obstruction |

## Packet Decisions

| packet | classification | future target? | counts as S1 evidence? | missing requirements | reason |
| --- | --- | :---: | :---: | --- | --- |
| `two_receipt_finality_generator` | `rejected_repaired_suite_incomplete` | False | False | repaired_suite_all_samples_pass, independent_naturality_or_neighbor_theory | Not all executed samples pass the repaired S1 suite. |
| `screen_conditioned_survivor_law` | `rejected_screen_conditioned_generator` | False | False | predeclared_generator, finality_domain_descent, not_conditioned_on_repaired_suite_success, hostile_controls, later_lorentzian_constraints_named, independent_naturality_or_neighbor_theory | Conditioning the law on diagnostic success is circular. |
| `lorentzian_import_promotion_shortcut` | `blocked_s1_promotion_shortcut` | False | False | finality_domain_descent, no_imported_lorentzian_coordinates, independent_naturality_or_neighbor_theory, no_overclaim_language, no_s1_promotion_request | A preflight or imported reference law cannot promote S1. |
| `future_full_burden_generator_packet` | `admitted_future_full_burden_review_target` | True | False | none | The shape is admissible for future review, but no samples exist yet. |

## Strongest Reading

The first TaF-native-looking two-receipt packet is not enough. It avoids explicit target-spacetime coordinates, but only 25 of 32 multi-size samples pass the repaired S1 suite, so it is rejected before S1 evidence or posture movement.

## What This Improved

T528 converts T526's suggested next step into an executable intake screen. Future generator packets now need all repaired-suite samples to pass, independent naturality or neighbor-theory support, hostile controls, and no imported Lorentzian coordinate shortcut.

## Missing Object

A predeclared finality-native generator, measure law, or continuum bridge whose samples pass the repaired suite across sizes, whose naturality is justified independently of the diagnostic, and whose later Lorentzian causal, metric, covariance, locality, and embedding constraints are named before promotion pressure.

## Falsification Condition

T528 fails if the packet counts an incomplete repaired-suite pass as S1 evidence, admits a screen-conditioned generator, imports Lorentzian coordinates as the source law, or changes S1/claim/canon posture from a preflight result.

## S1 Update

S1 remains `requires_added_assumption`. T528 rejects the first two-receipt finality-native generator packet as incomplete and therefore does not reverse T223 or promote S1.

## Claim Ledger Update

No claim-ledger update is earned. T528 is a test-registry preflight only: no claim row, no S1 status movement, and no T223 reversal.

## Suggested Next

Try a stronger predeclared generator or bridge with independent naturality support and all T525 repaired-suite samples passing, or route S1 effort to a separate formal entry point.

## Not Claimed

T528 does not derive spacetime, prove manifoldlikeness, establish a TaF-native sprinkling law, reconstruct a Lorentzian metric, prove an embedding or continuum theorem, reverse T223, or promote S1. It is a finite generator-preflight packet only.
