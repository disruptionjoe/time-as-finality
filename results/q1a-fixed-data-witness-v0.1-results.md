# T103 Results: Q1A Fixed-Data Witness

Baseline case: `independent_records_fixed_data`

## Cases

| Case | Fixed standard data | Raw redundancy | Independent support | D1 verdict | Gate verdict |
| --- | --- | --- | --- | --- | --- |
| independent_records_fixed_data | True | 3 | 3 | finalized | passes_fixed_data_gate |
| copied_archive_fixed_data | True | 3 | 2 | not_finalized | passes_fixed_data_gate |
| partition_hidden_fixed_data | True | 3 | n/a | withhold_partition_unavailable | passes_fixed_quantum_data_but_withholds_d1 |
| coherence_changed_control | False | 3 | n/a | invalid_fixed_data_gate | reject_standard_data_changed |
| raw_redundancy_changed_control | False | 2 | n/a | invalid_fixed_data_gate | reject_standard_data_changed |
| branch_history_changed_control | False | 3 | n/a | invalid_fixed_data_gate | reject_standard_data_changed |

## Audit flags

- Fixed-data internal witness exists: True
- Negative controls rejected: True
- Hidden partition withholds: True
- External measurement distinction earned: False

## Strongest claim

Q1A now has an internal fixed-data witness: decoherence/pointer-basis evidence, fragment-information summaries, accessible raw redundancy, and ordinary branch/history availability can be held fixed while D1 changes from finalized to not_finalized solely because the independence partition treats a record as an independent copy versus a copied archive. This is not yet an external measurement-theory distinction; it is an access/provenance accounting predicate over already formed records.

## What this improved

T103 converts the T102 blocker into an executable gate with positive and negative controls. The repo can now distinguish a valid fixed-data Q1A witness from invalid cases that changed coherence, raw redundancy, or branch/history availability.

## What this weakened

The witness also weakens Q1A's physics ambition. The only surviving delta is carried by an independence/provenance predicate; if decoherence, Quantum Darwinism, consistent histories, RQM, QBism, or Everettian accounts admit that same predicate, Q1A collapses to bookkeeping.

## Falsification condition

Demote Q1A if every fixed-data D1 change requires adding a provenance or independence partition that neighboring frameworks can adopt without changing their physics, or if no physically auditable procedure fixes the partition before D1 scoring.

## Q1 update

Q1A clears the internal fixed-data gate only as record independence accounting. It still does not earn new measurement dynamics, collapse content, Born-rule content, or empirical quantum support.

## Claim ledger update

Add T103 to Q1: a fixed-data witness exists internally because the same decoherence, fragment-information, raw-redundancy, and branch/history summaries can yield finalized versus not_finalized D1 verdicts when only the independence partition changes. This upgrades Q1A only to conditional record-accounting support; external distinctness remains unearned if the partition is ordinary provenance bookkeeping.

## Open blocker

The partition is still fixture-declared. The next blocker is a physically auditable derivation of record independence that is fixed before D1 scoring and not just imported as TaF vocabulary.

## Recommended next

Derive the T103 independence partition from event-level detector or environment-fragment provenance, then test whether Quantum Darwinism with provenance-aware fragment partitioning already absorbs the same verdict.
