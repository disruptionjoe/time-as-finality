# T144: Q1A Current-Family Closure

## Route

Quantum measurement / classical records.

## Question

After T105, T109, and T118, is there any current internal Q1A verdict content
left beyond partition visibility plus audited accessible provenance-support
count?

## Motivation

T105 reduced the surviving fixed-data Q1A branch to a thresholded accessible
provenance-support classifier. T109 showed branch support is trivial or
inadmissible in the current family. T118 showed reversal cost collapses to the
same support count unless a physically calibrated undo observable is added.

The highest-value Q1A move is therefore not another toy witness. It is a
closure audit that tells future runs what they must beat before reopening Q1A.

## Success Criteria

- Reuse T105/T109/T118 rather than introducing a new witness family.
- State the current quotient that preserves all present Q1A verdict content.
- Verify that D1, branch support, and reversal-cost proxies factor through
  that quotient.
- Preserve the raw-redundancy control: raw fragment count alone is still not
  sufficient.
- State the exact same-closure-key escape gate for future Q1A work.

## Failure Criteria

- The audit is presented as a theorem about quantum measurement in general.
- The closure quotient erases the access/provenance distinction and collapses
  back to raw redundancy.
- The note implies Q1A is experimentally upgraded rather than internally
  closed.

## Claim Impact

Q1A remains bookkeeping-only. The current family is closed under the declared
D1 dimensions: all live verdict content is partition visibility plus audited
accessible provenance-support count. Reopen Q1A only with a fixed-standard-data
witness that matches that closure key but still changes the D1 verdict through
a predeclared physical dimension, or with a partition rule that neighboring
frameworks cannot import without adding new physics.

## Reproduction

```bash
python -m unittest tests.test_q1a_current_family_closure -v
python -m models.run_t144
```
