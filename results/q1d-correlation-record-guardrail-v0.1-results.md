# T170 Results: Q1D Correlation-Record Guardrail

## Scenario audits

| Scenario | No-signalling | Max CHSH | Stage | Classification | Rejected language |
| --- | --- | ---: | --- | --- | --- |
| `classical_reconciled_baseline` | `True` | `2.0` | `after_causal_comparison` | `classical_reconciliation_baseline` | Reject upgrading this guardrail into measurement dynamics or a new inequality. |
| `quantum_contextual_reconciled_record` | `True` | `2.82842712474619` | `after_causal_comparison` | `admissible_contextual_reconciliation_record` | Reject upgrading this guardrail into measurement dynamics or a new inequality. |
| `pr_box_no_signalling_guardrail_only` | `True` | `4.0` | `after_causal_comparison` | `postquantum_no_signalling_guardrail_only` | Reject upgrading this guardrail into measurement dynamics or a new inequality. |
| `signalling_remote_setting_leak` | `False` | `0.0` | `local_record_stage` | `null_signalling_local_record` | Reject any claim that local finality can depend on a remote setting. |
| `hidden_variable_retrofit` | `True` | `2.82842712474619` | `after_causal_comparison` | `null_hidden_variable_overclaim` | Reject any claim that a later CHSH-violating correlation record was already an earlier local hidden fact. |
| `premature_correlation_export` | `True` | `2.82842712474619` | `local_record_stage` | `null_premature_correlation_record` | Reject any claim that the joint correlation is locally finalized before the parties can compare records. |
| `pr_box_mislabelled_quantum_prediction` | `True` | `4.0` | `after_causal_comparison` | `null_postquantum_as_quantum_prediction` | Reject treating a post-quantum no-signalling box as a quantum prediction. |

## Strongest claim

Q1D can safely say that no-signalling contextual correlations may produce local records first and a joint correlation record only after causal comparison. It cannot say that the later correlation was already an earlier local hidden fact, and it cannot let local record-finality depend on a remote setting.

## What this improved

T170 makes the reconciliation-time boundary executable. Future Q1 language now has finite null controls for signalling marginals, hidden-variable retrofits, premature correlation export, and post-quantum boxes mislabelled as quantum predictions.

## What this weakened

This weakens Q1D's positive content to admissible language only. The passing quantum fixture adds no measurement dynamics, no new Bell inequality, no collapse account, and no empirical discriminator.

## Falsification condition

T170 fails if a model can keep no-signalling local marginals, violate the classical CHSH bound within the quantum Tsirelson limit, treat the correlation record as available only after causal comparison, avoid prior-local-value language, and still require rejection by the Q1D guardrail.

## Q1D update

Q1D remains guardrail-only. The current safe formulation is a stage rule: local record-finality is local-marginal constrained; joint correlation finality is a later causal-reconciliation record.

## Claim ledger update

Add T170 to Q1D: no-signalling contextual correlations are admissible only when local records do not depend on remote settings and the joint correlation is recorded after causal comparison. Signalling, hidden-variable retrofits, premature correlation export, and post-quantum-as-quantum readings are null.

## Open blocker

No theorem connects this finite stage guardrail to a general decoherent-histories, algebraic-QFT, or detector-level account of classical record formation.

## Recommended next

Use T170 as a prose gate for Q1D. Do not add more Bell-style toy models unless they introduce a new typed capability object or bridge the stage rule into a mature quantum-record framework.
