---
document_type: synthesis_preflight
batch_item: fifth_batch_task_8
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_result: results/q1d-correlation-record-guardrail-v0.1-results.md
---

# Q1D Correlation-Record Stage Guardrail Preflight

## Scope

This note completes fifth-batch task 8 as a synthesis/preflight artifact. It
does not update Q1D, Q1, detector language, tests, results, models, or the claim
ledger.

The purpose is to freeze the record-stage rule from T170 so future Q1D prose
cannot promote a later reconciled correlation into an earlier local fact.

## Grounding Readout

Read surfaces used:

- `results/q1d-correlation-record-guardrail-v0.1-results.md`.
- `tests/T170-q1d-correlation-record-guardrail.md`.
- `claims/Q1D-contextuality-no-signalling-guardrail.md`.
- `CLAIM-LEDGER.md` Q1D row and T170 change-log pointers.
- `workflows/logs/best-next-move/2026-06-27-fifth-10-research-orchestration.md`.

Current baseline:

- Q1D is `guardrail_only`.
- T170 admits no-signalling local records followed by later causal comparison.
- T170 rejects signalling marginals, hidden-variable retrofits, premature
  correlation export, and PR-box-as-quantum readings.
- The passing quantum fixture adds no measurement dynamics, no new Bell
  inequality, no collapse account, and no empirical discriminator.

## Frozen Stage Rule

The admissible sequence is:

```text
local measurement record
  -> later causal comparison
  -> reconciled joint correlation record
```

Required stage meanings:

| Stage | Admissible claim | Rejected claim |
| --- | --- | --- |
| Local record stage | Each party has local records constrained by local marginals. | A local record depends on a remote setting. |
| Causal comparison stage | Records can be compared only when causal access permits. | The joint correlation is already locally finalized before comparison. |
| Joint correlation stage | The reconciled correlation record can classify the run after comparison. | The later correlation was an earlier local hidden value. |

Boundary controls from T170:

| Control | Required classification |
| --- | --- |
| Classical reconciled baseline | `classical_reconciliation_baseline` |
| Tsirelson no-signalling contextual record | `admissible_contextual_reconciliation_record` |
| PR-box no-signalling control | `postquantum_no_signalling_guardrail_only` |
| Signalling remote-setting leak | `null_signalling_local_record` |
| Hidden-variable retrofit | `null_hidden_variable_overclaim` |
| Premature correlation export | `null_premature_correlation_record` |
| PR box labelled quantum | `null_postquantum_as_quantum_prediction` |

Allowed preflight verdicts:

```text
stage_guardrail_admissible
local_stage_underdeclared
no_signalling_guard_failed
hidden_variable_retrofit_null
premature_export_null
postquantum_boundary_failed
new_bell_theorem_overclaim_null
```

## Boundary Preservation

No-signalling boundary:

```text
P(local outcome | local setting, remote setting)
  must not vary with the remote setting at the local record stage.
```

Tsirelson/post-quantum boundary:

```text
classical CHSH <= 2
quantum Tsirelson control <= 2.82842712474619
PR-box no-signalling control = 4
```

The PR-box control may be useful as a guardrail stressor, but it must not be
called a quantum prediction. The Tsirelson fixture may be called admissible only
as staged record language, not as a new inequality or measurement theory.

## Acceptance Criteria

This preflight satisfies fifth-batch task 8 if the next artifact:

- Separates local record stage from later joint correlation stage.
- Keeps local record finality constrained by local marginals.
- Requires causal comparison before joint-correlation finality.
- Preserves the classical, Tsirelson, and PR-box boundary labels.
- Rejects signalling marginals.
- Rejects hidden-variable retrofits.
- Rejects premature correlation export.
- Rejects PR-box-as-quantum language.
- Keeps Q1D `guardrail_only`.
- Returns one of the allowed verdicts above.

## Null Or Demotion Conditions

Treat a proposed Q1D update as null or demote it to guardrail-only residue if
any of the following occur:

- Local outcomes or local record finality depend on remote settings.
- A later CHSH-violating correlation is described as an earlier local hidden
  fact.
- The joint correlation record is declared available before causal comparison.
- A post-quantum no-signalling box is labelled a quantum prediction.
- The artifact claims a new Bell theorem, new contextuality inequality, collapse
  model, measurement dynamics, or empirical discriminator.
- Detector-level record formation is asserted without a separate detector or
  decoherent-histories bridge.
- Q1D is used to reopen Q1, Q1A, Q1B, or Q1C.

Null result language to preserve:

```text
The candidate failed the Q1D stage guardrail. The safe residue is only the
standard record-stage constraint: local records first, joint correlation after
causal comparison, with no signalling, no hidden-variable retrofit, and no
post-quantum-as-quantum language.
```

## No-Promotion Guardrails

- Do not promote Q1D above `guardrail_only` from this preflight.
- Do not claim a new Bell theorem, new contextuality inequality, or new quantum
  prediction.
- Do not claim local finality depends on remote settings.
- Do not claim a later joint correlation was an earlier local hidden value.
- Do not claim the reconciled joint correlation is locally finalized before
  causal comparison.
- Do not use PR-box controls as quantum predictions.
- Do not edit `README`, `CLAIM-LEDGER`, `ROADMAP`, tests, models, results, or
  open-problem files from this preflight.

## Next Executable Artifact Shape

Recommended next synthesis artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-q1d-stage-language-gate.md
```

Required sections:

```text
candidate_q1d_sentence
local_record_stage_claim
causal_comparison_stage_claim
joint_correlation_stage_claim
local_marginal_check
chsh_boundary_label
tsirelson_boundary_check
postquantum_control_check
hidden_variable_retrofit_check
premature_export_check
allowed_verdict
no_promotion_guardrail_check
```

If later authorized for implementation, use a bounded language/admissibility
screen:

```text
tests/TXXX-q1d-stage-language-gate.md
models/q1d_stage_language_gate.py
results/q1d-stage-language-gate-v0.1-results.md
```

Do not create those implementation surfaces from this preflight.
