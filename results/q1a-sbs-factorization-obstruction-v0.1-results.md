# T162 Results: Q1A SBS Factorization Obstruction

## Aggregate checks

- Visible enumeration cases: 240
- D1 factors through SBS closure key: True
- Same full SBS-data split found: False
- Raw redundancy is not sufficient: True
- Objectivity failures withhold: True
- Hidden partition withholds: True
- Nontrivial same-key variants exist: True
- Current family has no same-SBS split: True

## Closure fibers

| Closure key | Cases | D1 verdicts | Raw redundancies | Partitions |
| --- | ---: | --- | --- | --- |
| ['computational_z', 'sbs_failed_agreement', None, None, None] | 1 | ['withhold_sbs_objectivity_failed'] | [3] | 1 signatures |
| ['computational_z', 'sbs_failed_distinguishability', None, None, None] | 1 | ['withhold_sbs_objectivity_failed'] | [3] | 1 signatures |
| ['computational_z', 'sbs_failed_strong_independence', None, None, None] | 1 | ['withhold_sbs_objectivity_failed'] | [3] | 1 signatures |
| ['computational_z', 'sbs_no_access', None, None, None] | 16 | ['withhold_sbs_objectivity_failed'] | [0] | 15 signatures |
| ['computational_z', 'sbs_objective', 'z0', False, None] | 1 | ['withhold_partition_unavailable'] | [3] | 1 signatures |
| ['computational_z', 'sbs_objective', 'z0', True, 1] | 99 | ['not_finalized'] | [1, 2, 3, 4] | 15 signatures |
| ['computational_z', 'sbs_objective', 'z0', True, 2] | 103 | ['not_finalized'] | [2, 3, 4] | 14 signatures |
| ['computational_z', 'sbs_objective', 'z0', True, 3] | 22 | ['finalized'] | [3, 4] | 7 signatures |
| ['computational_z', 'sbs_objective', 'z0', True, 4] | 1 | ['finalized'] | [4] | 1 signatures |

## Hidden partition control

- Case: access_E1-E2-E3__partition_hidden
- SBS verdict: sbs_objective
- D1 verdict: withhold_partition_unavailable

## Objectivity failure controls

| Case | SBS verdict | D1 verdict |
| --- | --- | --- |
| sbs_disagreement_control | sbs_failed_agreement | withhold_sbs_objectivity_failed |
| sbs_distinguishability_control | sbs_failed_distinguishability | withhold_sbs_objectivity_failed |
| sbs_independence_control | sbs_failed_strong_independence | withhold_sbs_objectivity_failed |
| sbs_no_access_control | sbs_no_access | withhold_sbs_objectivity_failed |

## Strongest claim

Within the current Q1A already-formed-record verdict family, the D1 verdict factors through an SBS-importable closure key: pointer objectivity status, accessible pointer value, partition visibility, and audited accessible provenance-support count. Therefore the present Q1A family has no same-SBS-data verdict split; a full SBS signature refines this key, so fixing full SBS data cannot change the current D1 verdict.

## What this improved

T162 turns the N10 absorber into an executable obstruction. A future Q1A proposal now has to say whether it changes the imported SBS closure key, in which case it is absorbed bookkeeping, or keeps that key fixed and supplies a genuinely new physical dimension.

## What this weakened

This weakens Q1A as an internal quantum-record route. The current same-closure-key family cannot produce the same-SBS-data witness that N10 requires, and raw redundancy remains insufficient once SBS/objectivity and provenance support are granted.

## Falsification condition

T162 fails if an admissible Q1A witness fixes full SBS/strong-QD objectivity data, observer-accessible fragments, provenance partition, partition visibility, and audited accessible support count, but still changes the D1 verdict through a predeclared physical dimension that SBS or strong Quantum Darwinism cannot import as ordinary objectivity, access, provenance, or support data.

## Q1A update

Q1A should be treated as SBS-absorbed bookkeeping in the current family. Reopen it only with a same-SBS-closure-key split or a physical derivation of the partition/access rule that the SBS neighbor cannot import without new physics.

## Claim ledger update

Add T162 to Q1A: after N10, current Q1A verdicts factor through an SBS-importable closure key. No same-full-SBS-data verdict split exists in the enumerated family; Q1A remains bookkeeping_only.

## Open blocker

No named physical dimension currently varies at fixed SBS objectivity data, access subset, provenance partition, partition visibility, and audited accessible support count.

## Recommended next

Do not spend another autonomous run on Q1A unless a concrete same-SBS-closure-key split is named. Otherwise route quantum work to Q1B external packet acquisition, Q1C only if a platform tuple appears, or leave Q1 for another research line.
