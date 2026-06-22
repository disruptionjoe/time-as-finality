# T177: Q1 Absorber-Owned Field Intake

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [Q1A: Access-Boundary Record Accounting](../claims/Q1A-access-boundary-record-accounting.md)
- [Q1B: Detector Provenance Admissibility](../claims/Q1B-detector-provenance-admissibility.md)
- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md)

## Question

Can Q1 get a single pre-branch intake screen that blocks false reopenings
caused by changing absorber-owned fields?

## Motivation

Q1A, Q1B, Q1C, and Q1D now have strong local gates, but a future proposal can
still look new by moving the goalposts: change the SBS closure data, relax
detector governance, fix only a coarse ordinary record, or use contextuality
language as a hidden-variable repair.

The highest-value move is a negative one with positive controls: define the
intake screen that rejects those false moves while naming the exact proposal
shapes that would reopen a branch.

## Success Criteria

- Reject Q1A proposals that change SBS/strong-QD/provenance closure fields
  rather than splitting D1 at the same closure key.
- Reject Q1B proposals without a real deployment packet satisfying the current
  manifest, reviewable-row, five-domain, mandatory-quorum, and freeze burdens.
- Reject Q1C proposals that lack a T166 packet, fix only a coarse ordinary
  record, or show no typed positive verdict-risk lift.
- Reject Q1D signalling, hidden-variable, or premature joint-record language.
- Admit hypothetical positive controls for the exact Q1A, Q1B, and Q1C shapes
  that would justify further work.

## Failure Criteria

- The screen is presented as a no-go theorem for quantum measurement.
- All proposals are rejected by construction, with no falsifying positive
  control.
- Changing absorber-owned state is counted as new TaF residue.
- Q1D language permits signalling or hidden-variable retrofits.

## Claim Impact

Q1 remains a roadmap umbrella. Future quantum-measurement work must first pass
the T177 intake screen, then the relevant child-branch gate.

## Reproduction

```bash
python -m unittest tests.test_q1_absorber_owned_field_intake -v
python -m models.run_t177
```
