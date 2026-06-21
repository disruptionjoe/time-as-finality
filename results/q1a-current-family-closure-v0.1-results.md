# T144 Results: Q1A Current-Family Closure

## Aggregate checks

- Closure classifier matches D1: True
- D1 factors through closure key: True
- Branch support factors through closure key: True
- Reversal cost factors through closure key: True
- Raw redundancy is not sufficient: True
- Branch support load-bearing: False
- Reversal cost load-bearing: False
- Current family closed under declared dimensions: True

## Closure fibers

| Partition visible | Accessible support | Cases | D1 verdicts | Raw redundancies | Branch supports | Reversal-cost proxies |
| --- | --- | ---: | --- | --- | --- | --- |
| False | None | 1 | ['withhold_partition_unavailable'] | [3] | [] | [] |
| True | 0 | 5 | ['not_finalized'] | [0] | [0] | [0] |
| True | 1 | 22 | ['not_finalized'] | [1, 2, 3] | [1] | [1] |
| True | 2 | 12 | ['not_finalized'] | [2, 3] | [1] | [2] |
| True | 3 | 1 | ['finalized'] | [3] | [1] | [3] |

## Hidden partition control

- Case: access_E1-E2-E3__partition_hidden
- D1 verdict: withhold_partition_unavailable
- Closure verdict: withhold_partition_unavailable


## Strongest claim

The current enumerated Q1A fixed-data family is closed under the declared D1 dimensions: the D1 verdict factors through exactly the T105 closure key, namely partition visibility plus audited accessible provenance-support count. Raw accessible redundancy cannot replace that key, but branch support and reversal-cost proxies add no independent verdict content in this family.

## What this improved

T144 converts the scattered T105/T109/T118 demotions into one reusable closure test. A reviewer can now see the exact quotient that preserves all current Q1A verdict content and the exact condition a future Q1A witness must violate.

## What this weakened

This weakens Q1A by removing the last internal ambiguity in the current family. Q1A is not presently a measurement-dynamics claim; it is an access/provenance bookkeeping rule over already formed records unless a future witness splits the closure key.

## Falsification condition

T144 fails if an admissible Q1A witness keeps ordinary quantum-side summaries fixed, shares the same access cut and provenance-aware partition, matches the audited accessible support count, and still changes the D1 verdict through a predeclared physical dimension. It also fails if branch support or a calibrated undo/erasure observable varies at fixed closure key without changing standard data.

## Q1A update

Q1A should be stated as current-family closed: all present verdict content is captured by partition visibility plus audited accessible provenance support. Reopen Q1A only with a same-closure key verdict split or with a physical partition rule that cannot be imported by the neighboring framework without adding new physics.

## Claim ledger update

Add T144 to Q1A: the current fixed-data family is closed under accessible support, branch support, and reversal-cost audits. The surviving quotient is partition visibility plus audited accessible provenance-support count; no current internal Q1A dimension escapes that quotient.

## Open blocker

The repo still lacks a physically grounded same-support Q1A witness: fixed standard quantum summaries, shared audited partition, same accessible provenance support, and a nonabsorbed D1 verdict split.

## Recommended next

Do not add another Q1A finite record toy model unless it targets the same-closure-key escape gate. If no such target is available, spend quantum effort on an external Q1B packet or leave Q1 for a different route.
