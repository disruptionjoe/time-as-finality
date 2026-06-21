# Technical Report: Weak-Measurement Full-Record Sufficiency Boundary v0.1

## Claim Under Test

T137 ruled out simultaneous second meters that are downstream transforms of the
ordinary monitored record. But that still left one ambiguity:

```text
What exactly counts as "the ordinary monitored record" when Q1C says standard
statistics are held fixed?
```

If that phrase is interpreted too loosely, a proposal can cheat by fixing only
a coarse summary of the trajectory, then using an auxiliary channel to refine
hidden distinctions already present in the full event-level log.

T139 asks whether that move should count as a Q1C reopening.

## Result

No.

The relevant fixed object for Q1C is the full pre-registered event-level
ordinary monitored record, not a dashboard, thresholded export, plotted
average, or other coarsened summary of it.

That yields a sharper null class:

```text
A second meter is null for Q1C when it only produces a branch split against a
coarsened summary of the standard record, while the split vanishes once the
full event-level standard record is fixed.
```

## Executable Witness Families

T139 implements three finite cases.

| Scenario | Coarse-summary split | Full-record split | Classification |
| --- | --- | --- | --- |
| `coarse_summary_refinement_only` | yes | no | `null_coarse_summary_loophole` |
| `full_record_downstream_meter` | no | no | `null_full_record_downstream` |
| `branch_sensitive_extra_meter` | yes | yes | `candidate_full_record_escape` |

The first case is the load-bearing one. It shows that an auxiliary meter can
look useful only because the standard record was described too coarsely.

## Why This Matters

Without T139, the weak-measurement branch can reopen by accident.

A proposal could say:

1. hold the "ordinary monitored statistics" fixed;
2. read an auxiliary meter in parallel;
3. observe a verdict split; and
4. conclude that TaF found a new axis.

But if step 1 fixed only a coarse summary rather than the full event-level
trajectory, the auxiliary meter may just be unpacking distinctions already
contained in the ordinary log. That is not a new branch/provenance/undo-cost
observable. It is a refinement of an underspecified state description.

## Current Strongest Claim

Q1C should now be stated this way:

```text
Weak measurement remains dormant unless a monitored-qubit platform names a
calibrated, pre-registered auxiliary meter that changes the admissible TaF
verdict after conditioning on the full event-level ordinary monitored record,
not merely after conditioning on a coarsened summary of that record.
```

## What This Improved

T139 upgrades the phrase "ordinary monitored statistics held fixed" from vague
prose to an admissibility boundary:

- coarse export fixed is not enough;
- thresholded summary fixed is not enough;
- plotted trajectory statistics fixed are not enough;
- the full pre-registered event-level standard log must be fixed.

That makes future platform triage cheaper and more honest.

## What This Weakened Or Falsified

This weakens a softer rescue path for Q1C:

```text
Even if the auxiliary meter is reconstructed from the same physical run, it may
still count as independent if it splits cases within the same ordinary summary.
```

T139 says that is not enough. If the split disappears once the complete
ordinary transcript is held fixed, the proposal is null.

## Boundary Of The Result

T139 is not a no-go theorem for all dual-meter experiments.

It does not show that a branch-sensitive auxiliary meter is impossible. The
`branch_sensitive_extra_meter` witness exists precisely to mark the logical
escape class.

The result is narrower:

```text
Same-summary separation does not count unless it survives conditioning on the
full event-level standard record.
```

## Falsification Condition

T139 fails if a second meter that is conditionally determined by the full
event-level ordinary monitored record can still produce a pre-registered
fixed-full-record TaF verdict split.

That would mean the full-record screening-off criterion used here is too weak
or misposed.

## Open Blocker

No named monitored-qubit platform in the repo currently supplies an auxiliary
meter that is explicitly shown to escape screening-off by the full standard
trajectory record.

## Claim Ledger Update

Q1C remains `dormant`.

Add this sharpening:

```text
For Q1C, "ordinary monitored statistics held fixed" means the full
pre-registered event-level standard record. Auxiliary meters that only refine a
coarsened ordinary summary are null.
```

## Recommended Next Move

Search only for one of these two objects:

1. a dual-meter protocol whose auxiliary channel remains verdict-changing after
   conditioning on the complete ordinary monitored transcript; or
2. a stronger physical obstruction showing why standard weak-measurement
   architectures are unlikely to supply such a channel.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_full_record_sufficiency_boundary -v
python -m models.run_t139
```
