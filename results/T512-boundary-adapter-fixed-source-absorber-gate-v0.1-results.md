# T512 - Boundary Adapter Fixed-Source Absorber Gate - v0.1 results

> TaF-side fixed-source absorber gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T512-boundary-adapter-fixed-source-absorber-gate.md`
- Model: `models/boundary_adapter_fixed_source_absorber_gate.py`
- Tests: `tests/test_boundary_adapter_fixed_source_absorber_gate.py`
- Source gate: `tests/T511-boundary-adapter-finality-gate.md`
- Artifact JSON: `results/T512-boundary-adapter-fixed-source-absorber-gate-v0.1.json`

## Overall verdict: BOUNDARY_ADAPTER_FIXED_SOURCE_ABSORBER_GATE_BUILT_REVIEW_ONLY

T512 admits one synthetic review target only when a fixed source inventory is predeclared and fails to contain or generate the candidate record while the finality handle remains inadmissible and the ledger remains conserved. Fixed-source containment, fixed-source generation, post-hoc source completion, missing source inventory, admissible handles, source-crossing language, and cross-repo identity shortcuts are absorbed, rejected, or blocked.

## Decisions

| Packet | Admitted? | Label | Fixed source absorbs? | Absorber tested? | Post-hoc source? | Undo handle admissible? | Ledger conserved? | Missing requirements | Blocked shortcuts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| predeclared_nonfixed_source_review_target | yes | ADMITTED_NONFIXED_SOURCE_REVIEW_TARGET | no | yes | no | no | yes | none | none |
| fixed_source_disclosure_control | no | ABSORBED_BY_FIXED_SOURCE_DISCLOSURE | yes | yes | no | no | yes | none | none |
| fixed_source_generation_control | no | ABSORBED_BY_FIXED_SOURCE_GENERATION | yes | yes | no | no | yes | none | none |
| posthoc_source_inventory_shortcut | no | REJECTED_POSTHOC_SOURCE_COMPLETION | no | no | yes | no | yes | predeclared source inventory, predeclared fixed source inventory | none |
| missing_source_inventory_shortcut | no | REJECTED_MISSING_FIXED_SOURCE_ABSORBER | no | no | no | no | yes | fixed richer source inventory, predeclared source inventory, fixed richer source inventory | none |
| admissible_undo_handle_control | no | REJECTED_HANDLE_ADMISSIBLE_NOT_FINAL | no | yes | no | yes | yes | none | none |
| source_crossing_language_shortcut | no | REJECTED_SOURCE_CROSSING_NOT_ABSORBER_TEST | no | no | no | no | yes | fixed richer source inventory, predeclared source inventory, undo or readout handle, handle inadmissibility proof | none |
| cross_repo_identity_shortcut | no | BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT | no | yes | no | no | yes | none | claim_movement, cross_repo_truth_movement |

## Future Packet Minimum

- predeclare the fixed richer source inventory before choosing the witness
- state whether the candidate record is already contained in that source
- state whether predeclared source generators can form the candidate record
- distinguish access-schedule disclosure from nonfixed-source review targets
- keep the operation/readout class and undo/readout handle fixed before scoring
- prove handle inadmissibility and ledger conservation after absorber pressure
- include fixed-source disclosure and fixed-source generation controls
- block post-hoc source completion and cross-repo identity shortcuts

## What This Does Not Earn

- real GU/TaF/TI boundary adapter
- source crossing
- GU support for Time as Finality
- Time as Finality support for GU
- Temporal Issuance support for Time as Finality
- physics-side irreversibility claim
- universal ledger
- hidden central server
- claim-ledger movement
- roadmap movement
- README movement
- North Star movement
- public-posture movement
- hard-policy movement
- external publication
- cross-repo truth movement
