# T257 Results: T252 Cover Locality Audit

## Aggregate Checks

- Parent cover count: 8
- Parent largest cover hub fraction: 1/4 (0.250)
- Deletion cover-count distribution: `[{'value': 6, 'count': 1}, {'value': 7, 'count': 8}]`
- Deletion cover-hub distribution: `[{'value': {'fraction': '2/7', 'float': 0.2857142857142857}, 'count': 9}]`
- Verdict: `ordinal_cover_locality_stable_under_deletion`

## Strongest Claim

The T252 parent has 8 cover relations and a largest cover hub fraction of 1/4; every deletion keeps the cover hub at 2/7.

## What This Improved

T257 adds a cover/locality-style view to the T252 deletion story, separating sparse cover structure from mere ordering fraction.

## What This Weakened Or Falsified

This further weakens the suspicion that the T252 control passes only because of a concentrated cover hub.

## Falsification Condition

T257 fails if cover relations are not the transitive reductions of the audited strict orders, or if finite cover sparsity is treated as an embedding theorem.

## S1 Update

S1 remains guarded; cover sparsity is still a finite filter.

## Claim Ledger Update

Do not update the claim ledger from T257 alone. Safe wording: the selected T252 witness has stable sparse cover summaries under single deletion.

## Open Blocker

The repo still lacks a selection rule explaining why this cover shape should occur naturally.

## Suggested Next

Use the same shape summaries on the T255 mutation neighborhood to separate positive neighbors from T126-obstructed cases.

## Not Claimed

These diagnostics do not estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, or settle S1.
