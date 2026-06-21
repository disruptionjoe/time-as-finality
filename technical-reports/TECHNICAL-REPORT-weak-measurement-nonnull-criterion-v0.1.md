# Technical Report: Weak-Measurement Non-Null Criterion v0.1

## Claim Under Test

T132 asks what would make the open weak-measurement route a genuine Time as
Finality discriminator rather than a relabeling of standard monitored-record
statistics.

## Result

The criterion is now executable rather than rhetorical. In the finite audit,
six common protocol shapes fail and exactly one minimal candidate shape
survives:

```text
pre-registered rule
+ event-level or intervention-defined independent D1 axis
+ fixed ordinary decoherence/redundancy verdict
+ changed TaF verdict
```

This is not empirical support for Q1C. It is the narrow admissible shape that
any future weak-measurement proposal must instantiate before it deserves more
modeling effort.

## Executable Audit

T132 classifies seven protocol shapes.

| Protocol shape | Verdict | Why it fails or survives |
| --- | --- | --- |
| `threshold_only_homodyne` | `null_same_record_derivation` | only re-thresholds the same monitored trajectory |
| `semantic_partition_relabel` | `null_unpreregistered_or_post_hoc` | uses an after-the-fact label rather than a measured rule |
| `same_record_branch_live` | `null_same_record_derivation` | branch-live variable is reconstructed from the same record |
| `constant_branch_support_family` | `null_constant_branch_support` | branch support cannot separate verdicts if fixed by construction |
| `undo_energy_proxy` | `null_monotone_proxy_cost` | undo energy is only a monotone proxy, not an operational axis |
| `independent_meter_not_decisive` | `independent_but_not_decisive` | an independent meter exists but does not change the TaF verdict |
| `preregistered_channel_intervention_candidate` | `candidate_non_null_protocol` | the minimum admissible shape survives, but no real platform instantiates it |

## Current Strongest Claim

Q1C should be stated more narrowly:

```text
Weak measurement is non-null only if a pre-registered, event-level or
intervention-defined D1 axis changes the TaF verdict while the standard
decoherence/redundancy verdict stays fixed.
```

That is a gate, not a prediction.

## What This Improved

T132 removes ambiguity about what counts as progress on the weak-measurement
route. A serious reader can now ask a proposed platform four concrete
questions:

1. Was the rule fixed before analysis?
2. Is the extra axis actually measured or intervention-defined?
3. Are ordinary decoherence/redundancy summaries held fixed?
4. Does the extra axis change the TaF verdict?

If any answer is no, the route is null in the current TaF framing.

## What This Weakened Or Falsified

This weakens the remaining weak-measurement frontier in three ways.

1. Different threshold choices on the same trajectory no longer count as
   progress.
2. Constant branch-support families no longer count as latent rescue routes.
3. Independent meters that never change the verdict do not rescue Q1C.

The effect is to turn T12 from a suggestive experiment idea into a standing
obstruction unless a platform names a real independent axis.

## Falsification Condition

T132 would fail if either of the following occurs:

1. a same-record or post hoc protocol legitimately changes the TaF verdict
   while standard statistics are fixed; or
2. the surviving candidate shape is shown to be reconstructible from the same
   monitored record after all.

## Open Blocker

No real weak-measurement platform in the repo currently supplies a measured,
verdict-changing independent axis satisfying the gate.

## Claim Ledger Update

Q1 should remain `demoted` as an umbrella, and Q1C should remain `dormant`.
The new precision is:

```text
Q1C is a standing reinstatement gate. It is not revived by a second label,
second threshold, constant branch count, or monotone undo proxy. It reopens
only after one concrete independent measured axis changes the TaF verdict under
fixed standard monitored statistics.
```

## Recommended Next Move

Try exactly one platform-specific instantiation: a monitored protocol with a
duplicated-versus-independent record-class intervention or another measured
provenance axis. If that cannot be specified before modeling, demote T12 from
experimental route to permanent obstruction note.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_nonnull_criterion -v
python -m models.run_t132
```
