# T495 - Bounded-Record Retrieval Bottleneck Gate - v0.1 results

> Finite capability-audit toy only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T495-bounded-record-retrieval-bottleneck-gate.md`
- Model: `models/bounded_record_retrieval_bottleneck_gate.py`
- Tests: `tests/test_bounded_record_retrieval_bottleneck_gate.py`
- Source exploration: `explorations/finality-as-computation-state-vs-attention-2026-07-07.md`
- Artifact JSON: `results/T495-bounded-record-retrieval-bottleneck-gate-v0.1.json`

## Overall verdict: BOUNDED_RETRIEVAL_BOTTLENECK_BUILT_RETENTION_AXIS_ONLY

In the finite five-bit stream space, full-history visibility factors arbitrary indexed retrieval, but last-2 and parity committed states have non-singleton arbitrary-retrieval spreads. The same bounded states pass native positive controls for retained suffix or parity queries. The useful computation analogy is therefore a typed retention bottleneck, not the failed copyability mapping.

## Scenario Evaluation

| Scenario | Factors? | Label | Max spread | Interpretation |
| --- | --- | --- | --- | --- |
| full_history_arbitrary_retrieval_control | yes | PRESERVATION_CONTROL_PASSED | 1 | Full retention is the positive preservation control. |
| last2_state_arbitrary_retrieval_bottleneck | no | BOTTLENECK_DETECTED_AS_EXPECTED | 8 | The bounded state loses arbitrary retrieval capability: old bits vary across a fixed visible committed state. |
| last2_state_suffix_retrieval_control | yes | PRESERVATION_CONTROL_PASSED | 1 | Bounded state is sufficient for the task it explicitly retains. |
| parity_state_parity_task_control | yes | PRESERVATION_CONTROL_PASSED | 1 | A summary can preserve its native declared task. |
| parity_state_arbitrary_retrieval_bottleneck | no | BOTTLENECK_DETECTED_AS_EXPECTED | 16 | Parity retention is not arbitrary record retrieval. |

## Reading Evaluation

| Reading | Admitted? | Label | Action | Reason |
| --- | --- | --- | --- | --- |
| retention_axis_capability_probe | yes | ADMITTED_RETENTION_AXIS_CAPABILITY_PROBE | record | The bounded-state retrieval bottleneck is admitted as a finite review target for C(R)-style capability language. |
| naive_attention_quantum_copyability_mapping | no | REJECTED_NAIVE_COPYABILITY_MAPPING | reject | The gate preserves retrieval for stored classical records; it does not map unknown quantum states to copyable records. |
| physics_mechanism_import | no | REJECTED_PHYSICS_MECHANISM_IMPORT | reject | The finite retention-axis fixture is not a decoherence, Standard Model, or physical mechanism result. |
| complexity_theorem_shortcut | no | REJECTED_COMPLEXITY_THEOREM_SHORTCUT | reject | Finite enumeration can motivate a lower-bound target, but it is not itself an SSM/Transformer theorem. |
| public_or_cross_repo_update_shortcut | no | BLOCKED_PUBLIC_OR_CROSS_REPO_UPDATE | stop | A repo-local finite screen does not authorize public posture or cross-repo truth movement. |

## What this earns / does not earn

Earns: a finite capability bottleneck for arbitrary retrieval under bounded committed records, with positive controls for retained suffix and parity tasks.

Does not earn: a quantum, Standard Model, decoherence, physics-mechanism, SSM/Transformer lower-bound, claim-ledger, public-posture, or cross-repo result.

Honest ceiling: Finite capability-audit toy only. T495 supports the information-retention axis named by the computation exploration: full-history access determines arbitrary retrieval while bounded committed summaries do not. It does not prove a quantum, Standard Model, decoherence, or complexity-theorem claim; does not assert that physics is literally a Transformer or SSM; and does not move claim ledger, roadmap, README, North Star, public posture, hard policy, external publication, or cross-repo truth.

## Recommended Next

- If this lane continues, cite real SSM/attention lower-bound sources before importing any theorem language.
- Use T495 as a finite C(R)-style review target for bounded-record retrieval, not as physics support.
- Keep the naive attention/quantum copyability mapping demoted unless a separate typed packet repairs it.
