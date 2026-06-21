# Technical Report: Q1A Reversal-Cost Collapse v0.1

## Claim Under Test

T105 reduced the current fixed-data Q1A family to audited accessible
provenance support plus partition visibility. T109 then showed that branch
support is not an independent escape hatch in that family. T118 asks whether
reversal cost remains a live independent witness dimension.

## Artifact

T118 audits the full T105 visible-case family and one hidden-partition
control. It keeps fixed:

- pointer basis;
- reduced coherence;
- fragment mutual-information summaries;
- accessible raw redundancy within each case;
- ordinary branch/history availability.

It then tests the strongest reversal-cost proxy still admissible inside that
gate:

- the number of audited accessible provenance classes that would need to be
  erased or overwritten to destroy the record;
- withhold the proxy when the provenance partition is unavailable.

The T103 branch-history changed control is reused to ensure that richer undo
language is not smuggled in by changing ordinary quantum-side data.

## Result

Reversal cost does not survive as an independent witness dimension in the
current fixed-data Q1A family.

Within the admissible family:

```text
reversal_cost_proxy = withhold      if the provenance partition is unavailable
                     = support_count otherwise
```

So the only admissible reversal-cost proxy is identical to the audited
accessible provenance-support count. It never splits a same-support class and
adds no verdict content beyond the T105 reduction.

Any richer reversal-cost reading would require new physical structure not
present in the current witness language: undo dynamics, a calibrated work
meter, a control protocol, or postselected reversal data. Those are not part
of the fixed-data gate and cannot be imported without changing the question.

## Current Strongest Claim

Q1A should not cite reversal cost as a live independent witness dimension in
the current fixed-data family. The present evidence supports only an audited
record-accounting discipline over already formed records. Reversal-cost
language is currently just a restatement of how many audited accessible record
classes would need to be erased or overwritten.

## What This Improved

T118 closes the last obvious Q1A loophole inside the current fixed-data
family. The repo can now say directly that branch support and reversal cost
both fail as rescue routes there, so the surviving evidence is fully reduced
to audited accessible support plus partition visibility.

## What This Weakened Or Falsified

This weakens Q1A again. The current fixed-data family no longer supports even
a weak suggestion that multiple D1 dimensions remain independently active.
Inside that family, all remaining verdict content is counting discipline, not
new measurement structure.

## Falsification Condition

T118 stands unless one of the following happens:

- an admissible fixed-data witness in the current Q1A language exhibits
  different reversal-cost values at the same audited accessible
  provenance-support count while ordinary quantum-side summaries remain fixed;
  or
- a physically calibrated undo observable is introduced that is neither post
  hoc nor equivalent to counting audited accessible record classes.

## Claim Ledger Update

Add T118 to Q1A:

```text
Reversal cost does not presently escape the accessible-class reduction. In the
current fixed-data witness family its only admissible proxy is the number of
audited accessible provenance classes that would need to be erased or
overwritten, so it adds no independent verdict content.
```

## Open Blocker

The repo still lacks a finite quantum witness with a physically calibrated
undo or erasure observable that can vary while decoherence, fragment
information summaries, raw redundancy, branch/history availability, and
audited accessible support stay fixed.

## Next Work

Two reasonable next moves remain:

- build a genuinely dynamic witness with a predeclared undo observable that
  survives the fixed-data gate; or
- demote paper-facing Q1A language so it states plainly that current evidence
  is fully reduced to audited record-accounting discipline.

## Reproduction

```bash
python -m unittest tests.test_q1a_reversal_cost_collapse -v
python -m models.run_t118
```
