# T434 - Substrate-Law Admission Gate - v0.1 results

> Recorded-tier admission gate. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. Synthetic positive controls are gate calibration only, not real substrate evidence.

- Spec (frozen first): `tests/T434-substrate-law-admission-gate.md`
- Model: `models/substrate_law_admission_gate.py`
- Tests: `tests/test_substrate_law_admission_gate.py`
- Artifact JSON: `results/T434-substrate-law-admission-gate-v0.1.json`
- Run: `python -m pytest tests/test_substrate_law_admission_gate.py -q`

## Overall verdict: SUBSTRATE_LAW_ADMISSION_GATE_BUILT_CURRENT_T406_NOT_ADMITTED

The current T406 split remains unadmitted because no independent domain-native law or measured-dynamics packet forces the transition relation. Synthetic controls show the admissible shape for a future run but do not supply real physics or claim support.

## Gate Requirements

- law or measured-dynamics package frozen before pair selection
- one shared formula/protocol across both sides
- does not read the transition relation
- does not read hidden case labels
- uses declared substrate observables
- preserves fixed accounting
- derives the declared transition relation
- measured dynamics has enough repeated evidence and a negative control

## Candidate Audit

| candidate | admitted? | residue label | synthetic control? |
| --- | --- | --- | --- |
| bare_t406_main_pair | no | not_admitted_no_independent_law_or_measurement | no |
| transition_table_restatement | no | not_admitted_transition_table_restatement | no |
| post_hoc_conservation_selector | no | not_admitted_post_hoc_law | no |
| pair_specific_law | no | not_admitted_pair_specific_law | no |
| hidden_label_law | no | blocked_hidden_label_law | no |
| non_native_observable | no | not_admitted_non_native_observable | no |
| underpowered_measured_dynamics | no | not_admitted_underpowered_measured_dynamics | no |
| fixed_accounting_change_control | no | absorbed_by_fixed_accounting_completion | no |
| conservation_law_positive_control | yes | admitted_conservation_law_forced_transition_candidate | yes |
| measured_dynamics_positive_control | yes | admitted_measured_dynamics_forced_transition_candidate | yes |
| matched_transition_no_split_control | no | not_needed_no_capability_split | no |

## What this earns / does not earn

Earns: a reusable admission gate for the post-T406 burden. The current T406 transition split is not admitted; transition-table restatements, post hoc laws, hidden labels, non-native observables, underpowered measurements, and fixed-accounting changes are rejected.

Does not earn: a real substrate law, a physical-arrow theorem, a region-indexed discriminator success, a claim-ledger update, public posture movement, or cross-repo support.

Honest ceiling: Admission gate only. Synthetic controls show what would pass the gate; they do not name a real physical substrate law, do not discharge the region-indexed capability discriminator, and do not move claims.

## Recommended Next

- Do not repeat T406 by changing only the transition relation.
- Future Direction-A work must first supply a concrete law or measured-dynamics packet that clears T434.
- Treat admitted synthetic controls as gate calibration only, not evidence.
