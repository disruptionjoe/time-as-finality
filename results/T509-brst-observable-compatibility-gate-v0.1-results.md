# T509 - BRST Observable Compatibility Gate - v0.1 results

> TaF-side finite quotient/readout gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T509-brst-observable-compatibility-gate.md`
- Model: `models/brst_observable_compatibility_gate.py`
- Tests: `tests/test_brst_observable_compatibility_gate.py`
- Source gate: `tests/T508-brst-cohomology-record-admission-gate.md`
- Artifact JSON: `results/T509-brst-observable-compatibility-gate-v0.1.json`

## Overall verdict: BRST_OBSERVABLE_COMPATIBILITY_GATE_BUILT_RECOVERY_BLOCKED

T509 makes the T508 observable/readout burden explicit. The T507-style full-Krein recovery of a mirror difference is rejected in the finite BRST fixture because it does not descend through the quotient. A chain-map operation can create W+ representative leakage, but W+ readout is not exact-invariant, so that leakage is rejected as gauge-representative dependence. Only a direct exact-invariant cohomology readout is admitted, and only as a review target rather than hidden-record or physics evidence.

## Decisions

| Packet | Admitted? | Label | Operation descends? | Readout descends? | W+ recovery | Cohomology readout delta | Representative leakage? | Missing requirements |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t508_full_krein_recovery | no | REJECTED_RECOVERY_OPERATION_NOT_BRST_COMPATIBLE | no | no | 7.586e-01 | 7.586e-01 | no | none |
| chain_map_representative_leakage | no | REJECTED_EXACT_REPRESENTATIVE_LEAKAGE | yes | no | 1.000e+00 | 1.000e+00 | yes | none |
| direct_cohomology_observable | yes | ADMITTED_COHOMOLOGY_OBSERVABLE_REVIEW_TARGET | yes | yes | 0.000e+00 | 1.000e+00 | no | none |
| cohomology_scaling_control | yes | ADMITTED_COHOMOLOGY_OBSERVABLE_REVIEW_TARGET | yes | yes | 0.000e+00 | 2.000e+00 | no | none |
| exact_mirror_redundancy_control | no | BRST_EXACT_REDUNDANCY_RECORDED | yes | no | 0.000e+00 | 1.000e+00 | no | none |
| wplus_observable_shortcut | no | REJECTED_NON_DESCENDING_READOUT | yes | no | 0.000e+00 | 0.000e+00 | no | exact-invariant readout |
| post_hoc_readout_shortcut | no | REJECTED_INCOMPLETE_OBSERVABLE_PACKET | yes | yes | 0.000e+00 | 1.000e+00 | no | predeclared exact-invariant readout |
| missing_controls_shortcut | no | REJECTED_INCOMPLETE_OBSERVABLE_PACKET | yes | yes | 0.000e+00 | 1.000e+00 | no | exact-mirror redundancy control, non-descending recovery-operation control, exact-representative leakage control, direct cohomology-observable control |
| claim_cross_repo_shortcut | no | BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT | yes | yes | 0.000e+00 | 1.000e+00 | no | none |

## Future Packet Minimum

- predeclare Q, the quotient/cohomology object, operation algebra, and readout
- prove the recovery operation descends through the BRST quotient
- prove the readout annihilates exact representative shifts
- include a non-descending full-Krein recovery control
- include an exact-representative leakage control
- include exact-mirror redundancy and direct cohomology-observable controls
- treat direct cohomology readout as review-only until physics-side constraints are supplied
- do not treat W+ representative leakage as a hidden physical record

## What This Does Not Earn

- real BRST exactness decision
- real BRST cohomology nontriviality decision
- Krein-retention quantization accepted as physical
- full-Krein collective operations accepted as physically admissible
- self-normalized observer convention accepted as physical
- hidden mirror record claim
- source-action truth
- mass-gap evidence
- claim-ledger movement
- roadmap movement
- README movement
- North Star movement
- public-posture movement
- hard-policy movement
- external publication
- cross-repo truth movement
