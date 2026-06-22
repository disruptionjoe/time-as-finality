# T170: Q1D Correlation-Record Guardrail

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [T21: Bell Contextuality Finality](T21-bell-contextuality-finality.md)

## Question

Can Q1D distinguish three record stages without smuggling in a hidden-variable
or signalling claim?

```text
local measurement record
  -> later causal comparison
  -> reconciled joint correlation record
```

## Motivation

T21 already shows that local CHSH contexts can have valid local sections while
no global noncontextual assignment exists. The remaining Q1D language risk is
temporal: a later reconciled correlation record can be misread as an earlier
local fact, or local finality can be allowed to depend on a remote setting.

T170 makes those failures executable.

## Setup

Audit seven finite boxes:

1. `classical_reconciled_baseline`
   A noncontextual deterministic baseline.
2. `quantum_contextual_reconciled_record`
   A Tsirelson-saturating no-signalling box whose correlation record is formed
   only after causal comparison.
3. `pr_box_no_signalling_guardrail_only`
   A no-signalling but post-quantum control.
4. `signalling_remote_setting_leak`
   Alice's local marginal depends on Bob's setting.
5. `hidden_variable_retrofit`
   The Tsirelson box is described as if it had earlier local hidden values.
6. `premature_correlation_export`
   The Tsirelson box's joint correlation is declared final at the separated
   local-record stage.
7. `pr_box_mislabelled_quantum_prediction`
   A PR-box control treated as a quantum prediction.

## Success Criteria

- The Tsirelson fixture is admissible only as guardrail language:
  no-signalling local records first, joint correlation record after causal
  comparison.
- Signalling marginals are null.
- Hidden-variable retrofits are null.
- Premature correlation export is null.
- PR-box controls remain post-quantum guardrail controls and cannot be labelled
  quantum predictions.
- The result does not claim new Bell inequalities, detector dynamics, collapse,
  or empirical quantum support.

## Failure Criteria

- A fixture with local marginal dependence is admitted.
- A CHSH-violating fixture is allowed to claim prior local hidden values.
- A later joint correlation is treated as locally finalized before comparison.
- A post-quantum no-signalling box is treated as a quantum prediction.
- The passing fixture is misread as a new measurement theory.

## Claim Impact

Q1D remains `guardrail_only`.

Add this sharpening:

```text
Local record-finality is constrained by local marginals. Joint correlation
finality is a later causal-reconciliation record. Q1D fails whenever finality
language makes the local record depend on a remote setting, treats a later
correlation as an earlier local hidden value, or labels post-quantum
no-signalling structure as a quantum prediction.
```

## Reproduction

```bash
python -m unittest tests.test_q1d_correlation_record_guardrail -v
python -m models.run_t170
```
