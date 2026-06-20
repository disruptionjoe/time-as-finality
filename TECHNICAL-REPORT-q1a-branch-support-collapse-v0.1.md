# Technical Report: Q1A Branch-Support Collapse v0.1

## Claim Under Test

T105 narrowed the surviving fixed-data Q1A branch to audited accessible
provenance support plus partition visibility. T109 asks whether branch support
still provides an independent escape from that reduction inside the current
finite witness language.

## Artifact

T109 audits two branch-support readings against the existing fixed-data family:

- the rooted-branch reading inherited from T2, where all accessible records in
  the current witness family descend from the same pointer-measurement root;
- the ordinary branch/history availability data already held fixed by T103's
  admissibility gate.

The audit combines:

- the full T105 visible-case family;
- the T103 branch-history changed control.

## Result

Branch support does not survive as an independent witness dimension in the
current Q1A family.

Under the rooted-branch reading:

```text
accessible provenance support = 0  -> branch support 0
accessible provenance support > 0  -> branch support 1
```

So every visible case with any audited accessible support has the same
single-root branch value. Branch support never splits a same-support class and
never supplies a new verdict-critical distinction after T105.

Under the ordinary branch/history reading, changing the branch-history data is
already inadmissible: T103's `branch_history_changed_control` is rejected by
the fixed-data gate because it changes standard quantum-side summaries.

## Current Strongest Claim

Q1A should not cite branch support as a live independent witness dimension in
the current fixed-data family. The branch story is presently one of two
non-results:

- single-root triviality on admissible visible cases; or
- inadmissible change to ordinary branch/history data.

## What This Improved

T109 closes a real loophole in the current claim language. Earlier summaries
could still point at branch support as a generic future rescue route. After
this audit, that is no longer justified for the current finite witness family.

## What This Weakened Or Falsified

This weakens Q1A again. The current fixed-data branch no longer has a generic
"perhaps branch support survives" fallback. Any serious future branch-support
upgrade must enlarge the witness language to include genuinely distinct causal
record channels rather than reusing the present single-root family.

## Falsification Condition

T109 stands unless one of the following happens:

- an admissible fixed-data witness in the current Q1A language exhibits
  different branch-support values while the standard quantum-side summaries
  remain fixed; or
- a new branch-support observable is introduced that is neither trivial on the
  current family nor equivalent to changing ordinary branch/history
  availability.

## Claim Ledger Update

Add T109 to Q1A:

```text
Branch support does not presently escape the accessible-class reduction. In
the current fixed-data witness family it is either the trivial single-root
value 1 on all nonzero-support cases or an inadmissible change to ordinary
branch/history availability.
```

## Open Blocker

The repo still lacks any finite quantum witness with genuinely distinct causal
record channels whose branch-support value can vary without changing the
standard quantum-side summaries already held fixed by T103/T105.

## Next Work

Two reasonable next moves remain:

- construct a larger witness family with multiple causally independent record
  channels that can change branch support without changing the fixed-data gate;
  or
- attack reversal cost next and test whether it also collapses under the same
  audit discipline.

## Reproduction

```bash
python -m unittest tests.test_q1a_branch_support_collapse -v
python -m models.run_t109
```
