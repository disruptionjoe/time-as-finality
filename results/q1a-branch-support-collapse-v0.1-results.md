# T109 Results: Q1A Branch-Support Collapse

## Aggregate checks

- Rooted branch support constant on nonzero-support cases: True
- Rooted branch support varies only with zero-access boundary: True
- Rooted branch support splits any same-support class: False
- Branch-history changes leave fixed-data gate: True
- Any load-bearing branch-support witness in current family: False

## Support to rooted-branch mapping

| Case | Accessible provenance support | D1 verdict | Rooted branch support |
| --- | --- | --- | --- |
| access_none__partition_E1__E2__E3 | 0 | not_finalized | 0 |
| access_none__partition_E1-E2__E3 | 0 | not_finalized | 0 |
| access_none__partition_E1-E3__E2 | 0 | not_finalized | 0 |
| access_none__partition_E1__E2-E3 | 0 | not_finalized | 0 |
| access_none__partition_E1-E2-E3 | 0 | not_finalized | 0 |
| access_E1__partition_E1__E2__E3 | 1 | not_finalized | 1 |
| access_E1__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E1__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E1__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E1__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1__E2__E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E2__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E1-E2__partition_E1__E2__E3 | 2 | not_finalized | 1 |
| access_E1-E2__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E1-E2__partition_E1-E3__E2 | 2 | not_finalized | 1 |
| access_E1-E2__partition_E1__E2-E3 | 2 | not_finalized | 1 |
| access_E1-E2__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1__E2__E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E3__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E1-E3__partition_E1__E2__E3 | 2 | not_finalized | 1 |
| access_E1-E3__partition_E1-E2__E3 | 2 | not_finalized | 1 |
| access_E1-E3__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E1-E3__partition_E1__E2-E3 | 2 | not_finalized | 1 |
| access_E1-E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E2-E3__partition_E1__E2__E3 | 2 | not_finalized | 1 |
| access_E2-E3__partition_E1-E2__E3 | 2 | not_finalized | 1 |
| access_E2-E3__partition_E1-E3__E2 | 2 | not_finalized | 1 |
| access_E2-E3__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E2-E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E1-E2-E3__partition_E1__E2__E3 | 3 | finalized | 1 |
| access_E1-E2-E3__partition_E1-E2__E3 | 2 | not_finalized | 1 |
| access_E1-E2-E3__partition_E1-E3__E2 | 2 | not_finalized | 1 |
| access_E1-E2-E3__partition_E1__E2-E3 | 2 | not_finalized | 1 |
| access_E1-E2-E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |

## Strongest claim

Branch support is not a surviving independent lever in the current fixed-data Q1A family. Under the rooted-branch reading inherited from T2, every visible case with any audited accessible support has branch support 1 because all accessible records descend from the same pointer-measurement root; zero-support cases alone drop to 0. Under the ordinary branch/history reading, any change already violates T103's fixed-data gate. So branch support does not presently escape the T105 accessible-class reduction.

## What this improved

T109 removes a vague future-work loophole. The repo can now say exactly why branch support is not yet a live rescue route for Q1A: in the current witness language it is either trivial or already counted as changed standard quantum-side data.

## What this weakened

This weakens Q1A again. The remaining fixed-data branch no longer has a generic 'maybe branch support saves it' escape clause. Any future branch-support upgrade must enlarge the witness language to include genuinely distinct causal record channels rather than relabeling the existing single-root family.

## Falsification condition

T109 fails only if an admissible fixed-data witness in the current Q1A language exhibits different branch-support values while keeping standard quantum-side summaries fixed, or if a new branch-support observable is introduced that is neither trivial on the current family nor equivalent to changing ordinary branch/history availability.

## Q1A update

Q1A should not cite branch support as a live independent witness dimension in the current fixed-data family. At present the branch story is either single-root triviality or an inadmissible change to ordinary branch/history data.

## Claim ledger update

Add T109 to Q1A: branch support does not presently escape the accessible-class reduction. In the current fixed-data witness family it is either the trivial single-root value 1 on all nonzero-support cases or an inadmissible change to ordinary branch/history availability.

## Open blocker

The repo still lacks any finite quantum witness with genuinely distinct causal record channels whose branch-support value can vary without changing the standard quantum-side summaries already held fixed by T103/T105.

## Recommended next

Either construct a witness with multiple causally independent record channels that survive the fixed-data gate, or shift the next Q1A attack to reversal cost and test whether that dimension also collapses under the same audit discipline.
