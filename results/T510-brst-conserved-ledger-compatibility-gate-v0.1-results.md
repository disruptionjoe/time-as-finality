# T510 - BRST Conserved Ledger Compatibility Gate - v0.1 results

> TaF-side finite record/ledger gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T510-brst-conserved-ledger-compatibility-gate.md`
- Model: `models/brst_conserved_ledger_compatibility_gate.py`
- Tests: `tests/test_brst_conserved_ledger_compatibility_gate.py`
- Source gate: `tests/T509-brst-observable-compatibility-gate.md`
- Artifact JSON: `results/T510-brst-conserved-ledger-compatibility-gate-v0.1.json`

## Overall verdict: BRST_CONSERVED_LEDGER_GATE_BUILT_STABILITY_REVIEW_ONLY

T510 reprices T509's direct cohomology readout as a conserved ledger problem. A stable direct cohomology ledger and an exact-representative-noise control are admitted only as review targets. A quotient-descending dynamics that scales the mirror class is rejected because the ledger drifts; a full-Krein boost is rejected because it does not descend through the quotient; ordinary W+ ledger language is rejected because the readout is not exact-invariant.

## Decisions

| Packet | Admitted? | Label | Dynamics descends? | Readout descends? | Ledger conserved? | Ledger drift | Cohomology readout delta | Exact representative noise | Missing requirements |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| conserved_direct_cohomology_ledger | yes | ADMITTED_CONSERVED_COHOMOLOGY_LEDGER_REVIEW_TARGET | yes | yes | yes | 0.000e+00 | 1.000e+00 | 0.000e+00 | none |
| exact_representative_noise_control | yes | ADMITTED_CONSERVED_COHOMOLOGY_LEDGER_REVIEW_TARGET | yes | yes | yes | 0.000e+00 | 1.000e+00 | 5.000e-01 | none |
| cohomology_scaling_drift_control | no | REJECTED_NONCONSERVED_COHOMOLOGY_LEDGER | yes | yes | no | 5.000e-01 | 1.000e+00 | 0.000e+00 | dynamics-conserved quotient ledger |
| full_krein_dynamics_shortcut | no | REJECTED_DYNAMICS_NOT_BRST_COMPATIBLE | no | yes | no | 6.586e-01 | 1.000e+00 | 5.579e-01 | none |
| wplus_ledger_shortcut | no | REJECTED_NON_DESCENDING_LEDGER_READOUT | yes | no | yes | 0.000e+00 | 0.000e+00 | 0.000e+00 | exact-invariant ledger readout |
| exact_mirror_redundancy_control | no | BRST_EXACT_REDUNDANCY_RECORDED | yes | no | yes | 0.000e+00 | 1.000e+00 | 0.000e+00 | none |
| non_nilpotent_constraint_control | no | REJECTED_NON_NILPOTENT_CONSTRAINT | yes | no | yes | 0.000e+00 | 1.000e+00 | 0.000e+00 | nilpotency Q^2 = 0 |
| missing_controls_shortcut | no | REJECTED_INCOMPLETE_LEDGER_PACKET | yes | yes | yes | 0.000e+00 | 1.000e+00 | 0.000e+00 | non-descending dynamics control, ledger drift control, exact-representative noise control |
| claim_cross_repo_shortcut | no | BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT | yes | yes | yes | 0.000e+00 | 1.000e+00 | 0.000e+00 | none |

## Future Packet Minimum

- predeclare Q, the quotient/cohomology object, dynamics, and readout
- prove the dynamics descends through the BRST quotient
- prove the readout annihilates exact representative shifts
- prove the quotient readout is conserved by the declared dynamics
- include non-descending dynamics and ledger-drift controls
- include exact-representative noise and exact-mirror redundancy controls
- treat conserved cohomology readout as review-only until physics-side constraints are supplied
- do not treat W+ representative leakage or drifting cohomology as a hidden physical record

## What This Does Not Earn

- unitarity theorem
- physical inner product selection
- real BRST exactness decision
- real BRST cohomology nontriviality decision
- Krein-retention quantization accepted as physical
- full-Krein collective operations accepted as physically admissible
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
