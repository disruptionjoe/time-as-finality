# T145 Results: Physical Record Deletion Fixed-Accounting Screen

## Summary

At fixed free-energy floor, blank-capacity change, sink state, observer boundary, provenance state, source-copy status, and reversible-control access, the current fixtures contain one real split: branch topology changes future branch-failure robustness. That is a capability/topology residue, not H7 arrow evidence, because the deletion reverse remains ordinary erasure accounting. All arrow-looking deletion splits change an absorber variable or belong to a non-deletion reverse-edge class.

## Audit Table

| Fixture | Class | Matched accounting | FOA split | Verdict |
| --- | --- | --- | --- | --- |
| `same_floor_branch_topology_split` | `physical_record_deletion` | `True` | `True` | `fixed_accounting_capability_split_not_arrow` |
| `correlated_uncopy_vs_blind_reset` | `physical_record_deletion` | `False` | `True` | `absorbed_by_erasure_work_accounting` |
| `one_bit_vs_two_bit_blind_reset` | `physical_record_deletion` | `False` | `True` | `absorbed_by_erasure_work_accounting` |
| `hidden_sink_export_control` | `physical_record_deletion` | `False` | `True` | `absorbed_by_sink_accounting` |
| `observer_access_revocation` | `boundary_access_loss` | `True` | `True` | `non_deletion_reverse_class` |
| `authority_provenance_revocation` | `authority_or_provenance_loss` | `True` | `True` | `non_deletion_reverse_class` |

## same_floor_branch_topology_split

- Source: T142 same-chain copy vs branch-spread copy
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `True`
- Absorber mismatch fields: `[]`
- D1 topology split: `True`
- Future operation: `survive_one_branch_failure`
- Future-operation split: `True`
- Reverse status: `ordinary_erasure_accounted`
- H7 upgrade candidate: `False`
- Verdict: `fixed_accounting_capability_split_not_arrow`
- Interpretation: same_floor_branch_topology_split preserves a task-specific capability split under matched accounting, but it does not block the deletion reverse. Treat it as FOA/topology residue, not H7 arrow evidence.

## correlated_uncopy_vs_blind_reset

- Source: T142 uncopy/erasure split
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `False`
- Absorber mismatch fields: `['erased_bits', 'beta_work_floor', 'reversible_control']`
- D1 topology split: `False`
- Future operation: `restore_blank_target_without_heat`
- Future-operation split: `True`
- Reverse status: `absorbed_by_reversible_control_and_erasure_cost`
- H7 upgrade candidate: `False`
- Verdict: `absorbed_by_erasure_work_accounting`
- Interpretation: correlated_uncopy_vs_blind_reset is absorbed: The split is real, but it is exactly the standard distinction between retaining the reversible source-copy handle and losing it before blind reset.

## one_bit_vs_two_bit_blind_reset

- Source: erasure-cost hostile control
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `False`
- Absorber mismatch fields: `['erased_bits', 'beta_work_floor', 'blank_capacity_delta']`
- D1 topology split: `True`
- Future operation: `pay_same_blind_reset_floor`
- Future-operation split: `True`
- Reverse status: `absorbed_by_erasure_cost`
- H7 upgrade candidate: `False`
- Verdict: `absorbed_by_erasure_work_accounting`
- Interpretation: one_bit_vs_two_bit_blind_reset is absorbed: Different deletion burden here is just different erased-bit and free-energy accounting.

## hidden_sink_export_control

- Source: T106/T116 sink-accounting warning
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `False`
- Absorber mismatch fields: `['sink_delta']`
- D1 topology split: `False`
- Future operation: `recover_deleted_history_from_sink`
- Future-operation split: `True`
- Reverse status: `absorbed_by_sink_state`
- H7 upgrade candidate: `False`
- Verdict: `absorbed_by_sink_accounting`
- Interpretation: hidden_sink_export_control is absorbed: The future-operation split comes from hidden exported history, not from fixed-accounting physical deletion.

## observer_access_revocation

- Source: T141 access grant reverse
- Reverse-edge class: `boundary_access_loss`
- Absorber vector matched: `True`
- Absorber mismatch fields: `[]`
- D1 topology split: `True`
- Future operation: `observer_can_read_record`
- Future-operation split: `True`
- Reverse status: `not_physical_record_deletion`
- H7 upgrade candidate: `False`
- Verdict: `non_deletion_reverse_class`
- Interpretation: observer_access_revocation is not physical record deletion. The record support can remain intact; only the observer access boundary changes.

## authority_provenance_revocation

- Source: T144 authority/provenance class
- Reverse-edge class: `authority_or_provenance_loss`
- Absorber vector matched: `True`
- Absorber mismatch fields: `[]`
- D1 topology split: `True`
- Future operation: `use_record_for_claim_review`
- Future-operation split: `True`
- Reverse status: `governance_not_thermodynamic`
- H7 upgrade candidate: `False`
- Verdict: `non_deletion_reverse_class`
- Interpretation: authority_provenance_revocation is not physical record deletion. The record can remain materially present while claim-review authority is revoked.

## Fixed-Accounting Capability Splits

- `same_floor_branch_topology_split`

## H7 Arrow Candidates

None.

## What Improved

T145 turns the T142/T144 open blocker into an executable screen. Future H7 deletion witnesses must now hold the absorber vector fixed and still block the reverse for substrate-native reasons.

## What Weakened

The common escape 'D1 topology differs at fixed erasure floor' is not enough for a physical arrow. It can support a task-specific future-operation split, but H7 needs a constructor-impossible physical deletion reverse after full accounting.

## Falsification Condition

T145 fails in H7's favor if a physically typed record substrate exhibits a physical_record_deletion pair with the full absorber vector matched, a task-natural future-operation split, and a reverse status of constructor_impossible_after_full_accounting.

## H7 Update

Add T145 to H7: fixed-accounting D1 topology splits are capability residue unless the physical deletion reverse is impossible after free-energy, capacity, sink, boundary, provenance, source-copy, and reversible-control accounting are matched.

## Claim Ledger Update

T145 screens the only remaining H7 physical-arrow class. At fixed absorber data, the current branch-topology split changes future operation availability but not reverse admissibility. Deletion-like arrow candidates are absorbed by changed erasure work, control handles, sink state, access boundary, or provenance class.

## Open Blocker

No physically typed record substrate currently gives a constructor-impossible physical deletion reverse under matched free-energy, capacity, sink, boundary, provenance, source-copy, and reversible-control data.

## Suggested Next

Either search for a substrate-native physical deletion candidate that clears the T145 gate, or demote H7's paper-facing role to a resource-accounting and reverse-edge audit discipline.
