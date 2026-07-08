# T508 - BRST Cohomology Record-Admission Gate - v0.1 results

> TaF-side finite admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T508-brst-cohomology-record-admission-gate.md`
- Model: `models/brst_cohomology_record_admission_gate.py`
- Tests: `tests/test_brst_cohomology_record_admission_gate.py`
- Source gate: `tests/T507-finality-record-redundancy-double-gate.md`
- Artifact JSON: `results/T508-brst-cohomology-record-admission-gate-v0.1.json`

## Overall verdict: BRST_COHOMOLOGY_RECORD_GATE_BUILT_REVIEW_ONLY

T508 makes the post-T507 BRST burden explicit. In the finite fixture, a Q-exact mirror vector routes to redundancy; a Q-closed but non-exact mirror vector can be admitted only as a review target when the packet also pays T507's full-Krein operation and self-normalized hiddenness gates. Non-nilpotent, not-closed, post-hoc, missing-control, full-Born, claim/public, external-publication, and cross-repo shortcuts are rejected or blocked. This builds an intake gate; it does not decide the real physics.

## Decisions

| Packet | Admitted? | Label | Q^2=0? | Mirror closed? | Mirror exact? | Mirror nontrivial? | T507 double gate paid? | H dim | Missing requirements |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact_mirror_default | no | BRST_EXACT_REDUNDANCY_RECORDED | yes | yes | yes | no | no | 2 | none |
| nontrivial_mirror_full_krein_selfnorm | yes | ADMITTED_NONTRIVIAL_COHOMOLOGY_REVIEW_TARGET | yes | yes | no | yes | yes | 2 | none |
| nontrivial_mirror_full_born | no | REJECTED_NONTRIVIAL_BUT_FULL_BORN_VISIBLE | yes | yes | no | yes | no | 2 | none |
| nontrivial_mirror_no_recovery | no | REJECTED_NONTRIVIAL_BUT_NO_RECORD_RECOVERY | yes | yes | no | yes | no | 2 | none |
| non_nilpotent_control | no | REJECTED_NON_NILPOTENT_CONSTRAINT | no | no | yes | no | yes | -1 | nilpotency Q^2 = 0, mirror vector in ker(Q) |
| mirror_not_closed_control | no | REJECTED_MIRROR_NOT_Q_CLOSED | yes | no | no | no | yes | 2 | mirror vector in ker(Q) |
| post_hoc_q_shortcut | no | REJECTED_INCOMPLETE_CONSTRAINT_PACKET | yes | yes | no | yes | yes | 2 | predeclared constraint operator Q |
| missing_controls_shortcut | no | REJECTED_INCOMPLETE_CONSTRAINT_PACKET | yes | yes | no | yes | yes | 2 | declared quotient/cohomology object, Q-closed observable discipline, exact-mirror redundancy control, nontrivial-mirror review control |
| untyped_brst_shortcut | no | REJECTED_UNTYPED_BRST_ASSERTION | yes | yes | no | yes | yes | 4 | predeclared nilpotent constraint operator Q |
| claim_cross_repo_shortcut | no | BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT | yes | yes | no | yes | yes | 2 | none |

## Future Packet Minimum

- predeclare the constraint or gauge operator Q before selecting the mirror pair
- prove Q is nilpotent with Q^2 = 0
- prove the mirror vector is Q-closed
- decide exactness by membership in im(Q), not by assertion
- declare the cohomology quotient or physical-state quotient
- declare the Q-closed observable discipline
- include exact-mirror redundancy and nontrivial-mirror review controls
- pay T507's operation-algebra recovery controls
- pay T507's full-Born leakage and self-normalized hiddenness controls
- keep any nontrivial class review-only until physics-side constraints are supplied

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
