# T468 - Coarse-Graining Positive-Control Independence - v0.1 results

> Audit only. No claim status, roadmap, README, North Star, public-posture, hard-policy, or cross-repo movement.

- Spec: `tests/T468-coarse-graining-positive-control-independence.md`
- Model: `models/coarse_graining_positive_control_independence.py`
- Tests: `tests/test_coarse_graining_positive_control_independence.py`
- Artifact JSON: `results/T468-coarse-graining-positive-control-independence-v0.1.json`
- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`
- Prior gate: `results/T467-valid-coarse-graining-admissibility-gate-v0.1-results.md`

## Overall verdict: T467_POSITIVE_CONTROLS_COLLAPSE_TASK_GATE_LOAD_BEARING

T467's two admitted positive controls are extensionally the same partition on a binary two-holder fixture. They first separate at three holders, where finality-band and local-count coarse-grainings diverge. The cheap-xor probe also shows that finality-task semantics is load-bearing: bounded access and cost alone do not select a valid finality coarse-graining.

## Positive-Control Partition Comparison

| holder width | state count | finality-band classes | local-count classes | identical? |
| --- | --- | --- | --- | --- |
| 1 | 2 | 2 | 2 | True |
| 2 | 4 | 3 | 3 | True |
| 3 | 8 | 3 | 4 | False |
| 4 | 16 | 3 | 5 | False |

Minimum holder width for positive-control independence: `3`.

## Task Semantics Probe

A cheap accessible xor partition is rejected when no finality-native task is declared, but it would pass the mechanical budget gate if the task flag were simply asserted. Future packets therefore need a task-naturalness audit, not just access and cost fields.

| case | decision | route | blockers |
| --- | --- | --- | --- |
| without finality task | not_admitted | NO_FINALIZED_RECORD_TASK | no_finalized_record_task |
| with task label asserted | admitted_for_review | BOUNDED_OBSERVER_CERTIFIABLE | none |

## Future Packet Minimum

- use at least three binary holders or a multi-valued fixture when claiming independent positive controls
- include a cheap accessible non-finality partition as a hostile control
- supply a predeclared task-naturalness account rather than only a boolean finality-task flag
- keep bounded certification, certified record, and observer-creates-truth guardrails from T467

## What This Does Not Earn

- D1 promotion
- T10 superselection result
- T29 projection-obstruction promotion
- observer-theory equivalence theorem
- physics or consciousness claim
- claim-ledger movement
- public-posture movement
