# T513 - Cap_TI Reconciliation Protocol Gate - v0.1 results

> TaF-side protocol-grounding gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T513-cap-ti-reconciliation-protocol-gate.md`
- Model: `models/cap_ti_reconciliation_protocol_gate.py`
- Tests: `tests/test_cap_ti_reconciliation_protocol_gate.py`
- Source spec: `open-problems/cap-ti-capability-object-spec.md`
- Artifact JSON: `results/T513-cap-ti-reconciliation-protocol-gate-v0.1.json`

## Overall verdict: CAP_TI_RECONCILIATION_PROTOCOL_GATE_BUILT_REVIEW_ONLY

T513 turns the Cap_TI reconciliation-round formula into a finite review packet shape: beta, timing metric, observer-pair schedule, hierarchy capacity, reconciliation unit, and controls must be predeclared, and measured rounds must match ceil(n^(1 - beta)). The synthetic high-beta packet requires fewer rounds than the matched low-beta packet, while same-beta controls match. This is protocol grounding only, not Cap_TI promotion or Temporal Issuance source truth.

## Protocol Interpretation

- Continuous formula: `R_continuous(n, beta) = n^(1 - beta)`
- Finite rounds: `ceil(n^(1 - beta))`
- Hierarchy capacity: `ceil(n^beta)`
- Round reading: One round may reconcile at most one hierarchy-capacity batch of observer disagreements under the predeclared schedule.

## Decisions

| Packet | Admitted? | Label | Expected rounds | Measured rounds | Hierarchy capacity | Missing requirements | Blocked shortcuts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hierarchical_protocol_high_beta | yes | ADMITTED_PROTOCOL_GROUNDING_REVIEW_TARGET | 3 | 3 | 23 | none | none |
| hierarchical_protocol_low_beta | yes | ADMITTED_PROTOCOL_GROUNDING_REVIEW_TARGET | 8 | 8 | 8 | none | none |
| same_beta_null_control_a | yes | ADMITTED_PROTOCOL_GROUNDING_REVIEW_TARGET | 6 | 6 | 13 | none | none |
| same_beta_null_control_b | yes | ADMITTED_PROTOCOL_GROUNDING_REVIEW_TARGET | 6 | 6 | 13 | none | none |
| formula_only_shortcut | no | REJECTED_FORMULA_ONLY_NOT_PROTOCOL | 3 | 3 | 23 | finite reconciliation protocol, reconciliation unit, observer-pair schedule, hierarchy capacity | none |
| topology_only_shortcut | no | ABSORBED_BY_TOPOLOGY_ONLY_NO_TIMING_METRIC | 3 | 3 | 23 | timing metric | none |
| posthoc_beta_shortcut | no | REJECTED_POSTHOC_BETA | 3 | 3 | 23 | predeclared beta metric | none |
| hidden_timing_shortcut | no | REJECTED_HIDDEN_TIMING_SHORTCUT | 3 | 3 | 23 | timing metric | none |
| round_mismatch_control | no | REJECTED_PROTOCOL_ROUND_MISMATCH | 3 | 4 | 23 | none | none |
| promotion_or_cross_repo_shortcut | no | BLOCKED_GOVERNANCE_OR_CROSS_REPO_SHORTCUT | 3 | 3 | 23 | none | claim_movement, h7_promotion, temporal_issuance_source_truth, cross_repo_truth_movement, external_publication |

## Future Packet Minimum

- predeclare beta and its timing metric before pair selection
- declare the finite reconciliation unit and observer-pair schedule
- declare hierarchy capacity as ceil(n^beta)
- map continuous R(beta) to integer protocol rounds as ceil(n^(1 - beta))
- include high-beta and low-beta positive controls under matched freeze data
- include same-beta null controls
- match causal order, entropy, and gluing topology before scoring beta
- reject formula-only, topology-only, post-hoc beta, and hidden-timing shortcuts

## What This Does Not Earn

- Cap_TI promotion
- Temporal Issuance source truth
- H7 support
- physical-substrate theorem
- source-object contract completion
- claim-ledger movement
- canon verdict movement
- roadmap movement
- README movement
- North Star movement
- public-posture movement
- hard-policy movement
- external publication
- cross-repo truth movement
