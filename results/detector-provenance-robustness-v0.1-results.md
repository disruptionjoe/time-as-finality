# T70 Results: Detector Provenance Robustness

Passive statistics held fixed: agreement 0.92; phi 0.84.

Strongest claim: T68 survives moderate single-channel degradation when redundant authenticated provenance channels remain. The D1 partition can still be fixed before finality scoring without inspecting the desired D1 verdict.

Weakened claim: The detector branch of Q1 depends on trusted provenance instrumentation. If clock, tag, intervention, and DAG evidence are jointly missing, forgeable, thresholded, or back-action contaminated, D1 must be withheld or else adds no detector-level content beyond externally supplied classes.

## Robustness table

| Regime | Verdict | Metadata used | Copied status | Independent status |
| --- | --- | --- | --- | --- |
| ideal_t68_metadata | survives | timing_plus_ancestry, authenticated_origin_tags, clean_perturbation_response, complete_signed_dag | determined | determined |
| clock_uncertainty_only | survives | authenticated_origin_tags, clean_perturbation_response, complete_signed_dag | determined | determined |
| tag_loss_only | survives | timing_plus_ancestry, clean_perturbation_response, complete_signed_dag | determined | determined |
| tag_spoofing_caught_by_dag_and_intervention | survives | timing_plus_ancestry, clean_perturbation_response, complete_signed_dag | determined | determined |
| perturbation_back_action_with_authenticated_records | survives | timing_plus_ancestry, authenticated_origin_tags, complete_signed_dag | determined | determined |
| archive_latency_hidden_but_signed_dag_remains | survives | authenticated_origin_tags, clean_perturbation_response, complete_signed_dag | determined | determined |
| dag_incomplete_tags_lost_back_action | fails_clean_abstention | none | undetermined_clean_abstention | undetermined_clean_abstention |
| partial_dag_threshold_only | fails_threshold_or_label_dependent | none | undetermined_threshold_or_label_dependent | undetermined_threshold_or_label_dependent |
| forged_tags_hidden_latency_incomplete_dag | fails_clean_abstention | none | undetermined_clean_abstention | undetermined_clean_abstention |

## Minimal metadata requirement

D1 detector finality is non-arbitrary only when the provenance partition is fixed by at least one authenticated dependence channel for copied records and at least one authenticated independence channel for independent records. In this witness family the usable channels are: clean perturbation response, authenticated origin tags, complete signed ancestry, or timing only when paired with ancestry and clock bounds. Passive similarity and partial-DAG thresholds are insufficient.

## Q1 recommendation

Keep Q1 partially supported, but state the detector contribution as an intervention-sensitive provenance/accounting framework. Do not claim provenance recovery from detector outcomes alone.

## Falsification condition

T70 would fail if degraded copied and independent witnesses with identical passive statistics can be classified non-arbitrarily without authenticated provenance channels, or if a physical implementation shows the required provenance channels cannot be made independent of the D1 outcome.

## Next move

Replace the boolean degradation flags with a physical protocol model: clock distributions, signature failure probabilities, archive batching, and intervention back-action matrices.
