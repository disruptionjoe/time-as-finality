# T530 Results: T528 Generator Failure Router

## Verdict

- Verdict: `t528_failure_router_built_review_only`
- Source: `T528-s1-finality-native-generator-preflight-v0.1`
- T528 repaired-suite samples passing: 25/32 (0.7812)
- Failed samples routed: 7
- Primary failure axis: `ordering_fraction`
- Secondary failure axes: `height`, `largest_interval`, `width`
- Hard-gate failure count: 0

## Failure Summary By Size

| n | samples | pass count | failed count | pass rate |
| ---: | ---: | ---: | ---: | ---: |
| 8 | 8 | 7 | 1 | 7/8 (0.8750) |
| 12 | 8 | 5 | 3 | 5/8 (0.6250) |
| 16 | 8 | 8 | 0 | 8/8 (1.0000) |
| 20 | 8 | 5 | 3 | 5/8 (0.6250) |

## Failure Axes

| axis | failed samples | event counts | representatives | reading |
| --- | ---: | --- | --- | --- |
| `ordering_fraction` | 6 | 8, 12, 20 | n=8/seed=0, n=12/seed=5, n=12/seed=6, n=20/seed=3 | The two-receipt packet most often misses the random-control ordering fraction envelope; a next packet must address comparability density before tuning secondary diagnostics. |
| `height` | 3 | 12 | n=12/seed=2, n=12/seed=5, n=12/seed=6 | Height failures are secondary and cannot be repaired alone while the ordering-fraction miss remains. |
| `largest_interval` | 2 | 12, 20 | n=12/seed=6, n=20/seed=3 | Largest-interval failures appear in fewer samples and are not the primary blocker. |
| `width` | 1 | 12 | n=12/seed=6 | Width fails only once in the T528 sample set, so width-only repair is not a credible next primary packet. |
| `hard_t126_gate` | 0 | none | none | No executed T528 generator sample failed a hard T126 gate; the issue is repaired-suite calibration, not descent/canonicality collapse. |

## Next Packet Routing

| packet | classification | action | future target? | S1 evidence? | missing requirements | reason |
| --- | --- | --- | :---: | :---: | --- | --- |
| `axis_blind_more_receipts` | `rejected_primary_axis_not_addressed` | `reject` | False | False | addresses_ordering_fraction_failure, independent_naturality_or_neighbor_theory | The packet does not address the primary T528 failure axis: ordering_fraction. |
| `screen_tuned_receipt_mixture` | `rejected_screen_conditioned_repair` | `reject` | False | False | predeclared_packet, independent_naturality_or_neighbor_theory, hostile_controls, not_conditioned_on_t528_failure_screen | The packet tunes the law from the diagnostic it must clear. |
| `lorentzian_reference_reuse` | `blocked_s1_or_claim_movement_shortcut` | `stop` | False | False | finality_native_descent, no_imported_lorentzian_reference, no_s1_or_claim_movement | A failure router cannot move S1, claims, canon, or public posture. |
| `height_only_repair` | `rejected_primary_axis_not_addressed` | `reject` | False | False | addresses_ordering_fraction_failure, not_secondary_axis_only | The packet does not address the primary T528 failure axis: ordering_fraction. |
| `ordering_fraction_repair_without_naturality` | `rejected_missing_review_requirements` | `revise_before_review` | False | False | independent_naturality_or_neighbor_theory | The packet addresses the right axis but lacks review requirements. |
| `predeclared_ordering_fraction_measure_law` | `admitted_future_review_target` | `future_review_only` | True | False | none | The shape is admissible for future review, but no generator success or S1 evidence is created by T530. |

## Strongest Reading

T528 did not fail because the two-receipt generator collapsed the hard T126 gates. It failed because repaired-suite calibration axes, especially ordering fraction and then height, were not stable across sizes. The next packet should therefore be a predeclared finality-native measure or bridge that directly targets comparability density while keeping independent naturality and hostile controls visible.

## Recommended Next

Attempt a predeclared ordering-fraction measure-law packet: fix the record-domain law before sampling, justify its naturality outside the T525/T528 diagnostic, include hostile controls, and treat any pass as review-only until later Lorentzian, locality, covariance, embedding, and continuum burdens are paid.

## S1 Update

S1 remains `requires_added_assumption`. T530 routes the next S1 generator burden but supplies no new generator success and no S1 evidence.

## Claim Ledger Update

No claim-ledger update is earned. T530 is test-registry routing infrastructure only: no claim row, no S1 status movement, and no T223 reversal.

## Not Claimed

T530 does not derive spacetime, prove manifoldlikeness, establish a finality-native sprinkling law, repair T528, reverse T223, promote S1, change claim status, change canon, change public posture, authorize external publication, or support cross-repo truth.
