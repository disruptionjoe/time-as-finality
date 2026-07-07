# T497 - Bounded Retrieval Source-Checked Stack Gate - v0.1 results

> Computation-lane composite explanation only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T497-bounded-retrieval-source-checked-stack-gate.md`
- Model: `models/bounded_retrieval_source_checked_stack_gate.py`
- Tests: `tests/test_bounded_retrieval_source_checked_stack_gate.py`
- Source note: `literature/N18-bounded-retrieval-copying-lower-bound-sources.md`
- Progress lanes: `open-problems/composite-absorber-stack-progress-lanes.md`
- Artifact JSON: `results/T497-bounded-retrieval-source-checked-stack-gate-v0.1.json`

## Overall verdict: BOUNDED_RETRIEVAL_SOURCE_CHECKED_STACK_BUILT_COMPOSITE_EXPLANATION

Across finite binary streams of length 2 through 8, full-history visibility factors arbitrary indexed retrieval, while last-2 committed state has growing arbitrary-retrieval spread once length exceeds 2 and still factors its native retained-suffix task. N18 source-checks copying/retrieval workload language for this computation lane, but T497 admits only composite absorber explanation and review-target status.

## Source Checks

| Source | Checked? | Supports retrieval workload? | Blocks overread | Allowed use |
| --- | --- | --- | --- | --- |
| jelassi_2024_copying | yes | yes | Does not imply physics or TaF novelty; scope is copying/retrieval workloads. | Primary support for source-checked bounded retrieval workload language. |
| gu_dao_2023_mamba | yes | no | Blocks simplistic SSM-bad readings; selective/input-dependent state matters. | Architecture caveat for any SSM comparison. |
| schlag_2021_fast_weights | yes | yes | Blocks naive full-attention-is-unbounded-history readings; fast-weight memory has capacity structure. | Memory-programming caveat for attention/linear-attention comparisons. |

## Absorber Stack

| Absorber | Status | Granted form | Effect |
| --- | --- | --- | --- |
| full_history_access | granted_and_tested | The full stream is visible. | Arbitrary indexed retrieval factors through visibility. |
| bounded_retained_state_summary | granted_and_tested | Only the last k bits are visible as committed state. | Arbitrary indexed retrieval has non-singleton spread for n > k. |
| native_retained_task_control | granted_and_tested | The task asks only for the retained suffix. | The bounded summary factors its native task. |
| source_checked_copying_retrieval_workload | source_checked | N18 sources permit computation-side copying/retrieval workload language. | The lane can use lower-bound-source status as review scaffolding, not as theorem import. |
| architecture_caveat_stack | granted | Fixed latent state, selective state, and fast-weight memory distinctions are not collapsed. | Naive SSM/attention polarity and physics overreads are blocked. |

## Finite Length Checks

| Length | Projection | Capability | Factors? | Max spread | Expected spread | Label |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 2 | full_history | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 2 | last_2_state | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 2 | last_2_state | last_2_suffix_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 3 | full_history | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 3 | last_2_state | arbitrary_retrieval | no | 2 | 2 | EXPECTED_STACK_BEHAVIOR |
| 3 | last_2_state | last_2_suffix_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 4 | full_history | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 4 | last_2_state | arbitrary_retrieval | no | 4 | 4 | EXPECTED_STACK_BEHAVIOR |
| 4 | last_2_state | last_2_suffix_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 5 | full_history | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 5 | last_2_state | arbitrary_retrieval | no | 8 | 8 | EXPECTED_STACK_BEHAVIOR |
| 5 | last_2_state | last_2_suffix_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 6 | full_history | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 6 | last_2_state | arbitrary_retrieval | no | 16 | 16 | EXPECTED_STACK_BEHAVIOR |
| 6 | last_2_state | last_2_suffix_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 7 | full_history | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 7 | last_2_state | arbitrary_retrieval | no | 32 | 32 | EXPECTED_STACK_BEHAVIOR |
| 7 | last_2_state | last_2_suffix_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 8 | full_history | arbitrary_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |
| 8 | last_2_state | arbitrary_retrieval | no | 64 | 64 | EXPECTED_STACK_BEHAVIOR |
| 8 | last_2_state | last_2_suffix_retrieval | yes | 1 | 1 | EXPECTED_STACK_BEHAVIOR |

## Reading Decisions

| Reading | Admitted? | Label | Action | Reason |
| --- | --- | --- | --- | --- |
| bounded_retrieval_composite_explanation | yes | ADMITTED_COMPOSITE_ABSORBER_EXPLANATION | record | The stack explains native retention success plus arbitrary retrieval failure under bounded committed state. |
| complexity_theorem_import | no | REJECTED_THEOREM_IMPORT_SHORTCUT | reject | T497 source-checks theorem neighborhood but does not reproduce or prove the source theorem. |
| physics_mechanism_import | no | REJECTED_PHYSICS_MECHANISM_IMPORT | reject | N18 supports a computation-side retrieval workload only, not a physics mechanism. |
| attention_quantum_copyability_revival | no | REJECTED_NAIVE_COPYABILITY_REVIVAL | reject | Architecture retrieval/copying comparisons do not map to unknown quantum-state copyability. |
| public_or_cross_repo_shortcut | no | BLOCKED_PUBLIC_OR_CROSS_REPO_SHORTCUT | stop | Source checking a computation-side workload does not authorize public posture or cross-repo truth movement. |

## What this earns / does not earn

Earns: source-backed computation-lane composite explanation for why bounded committed summaries can preserve native retained tasks while losing arbitrary indexed retrieval.

Does not earn: SSM/Transformer theorem proof, quantum copyability, physics mechanism, claim-ledger movement, public-posture movement, or cross-repo truth movement.

Honest ceiling: T497 is a source-checked computation-lane composite explanation and finite review target. It does not prove an SSM/Transformer theorem, does not claim physics mechanism, does not assert attention equals quantum copyability, and does not move claim ledger, roadmap, README, North Star, public posture, hard policy, external publication, or cross-repo truth.

## Recommended Next

If the lane continues, build a theorem-facing packet that restates one checked copying/retrieval lower-bound theorem with its exact assumptions, then compare that theorem's state model to the T497 finite capability-spread fixture.
