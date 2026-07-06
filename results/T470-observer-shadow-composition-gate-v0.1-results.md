# T470 - Observer-Shadow Composition Gate - v0.1 results

> First bounded run for `open-problems/observer-shadow-category.md`. No claim status, roadmap, README, North Star, public-posture, hard-policy, or cross-repo movement.

- Spec: `tests/T470-observer-shadow-composition-gate.md`
- Model: `models/observer_shadow_composition_gate.py`
- Tests: `tests/test_observer_shadow_composition_gate.py`
- Artifact JSON: `results/T470-observer-shadow-composition-gate-v0.1.json`
- Source open problem: `open-problems/observer-shadow-category.md`
- Reused fixtures: T37/T41 typed transport and T220 LossKernel factorization

## Overall verdict: OBSERVER_SHADOW_SCHEMA_BUILT_INDEXED_COMPLETION_REQUIRED_NO_PROMOTION

A shared observer-shadow audit-object schema can express both finite families, but verdict preservation is not automatic under endpoint-only composition. The first bounded run supports an indexed audit atlas, not a single global observer-shadow category.

## Family Summaries

| family | shared schema works? | indexed completion required? | strongest reading |
| --- | --- | --- | --- |
| typed_transport | True | True | Typed transport fits the shared schema only when the observer-shadow object carries path and accumulated-loss indices. Endpoint-only composition loses load-bearing data. |
| losskernel | True | True | LossKernel fits the same schema as a neighbor-visible factoring case. The only separating escape requires source-state completion, which T220 already routes back to absorption. |

## Morphism Checks

| check | family | same shadow? | capability equivalent? | protection preserved? | classification |
| --- | --- | --- | --- | --- | --- |
| transport_endpoint_only_collapse | typed_transport | True | False | False | composition_requires_path_index |
| transport_path_indexed_completion | typed_transport | False | False | True | separated_after_completion |
| losskernel_neighbor_factoring_preserves | losskernel | True | True | True | verdict_preserved |
| losskernel_hidden_source_omitted | losskernel | True | False | False | state_completion_required |
| losskernel_hidden_source_completed | losskernel | False | False | True | separated_after_completion |

## Future Packet Minimum

- declare source system, observer/access profile, shadow projection, capability object, and native comparison
- state which indices are part of the observer-shadow object before comparing morphisms
- include a positive preservation control where same shadow gives same capability
- include a negative or hostile control where omitted indices break preservation
- name the completion that repairs the bookkeeping and whether it routes to an absorber

## What This Does Not Earn

- observer-shadow category theorem
- North Star geometry proof
- D1, PO1, TF1, or LossKernel promotion
- physics or consciousness claim
- claim-ledger movement
- public-posture movement
