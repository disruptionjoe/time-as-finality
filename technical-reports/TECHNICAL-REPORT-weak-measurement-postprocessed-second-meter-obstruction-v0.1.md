# Technical Report: Weak-Measurement Postprocessed Second-Meter Obstruction v0.1

## Claim Under Test

After T130 and T135, weak measurement no longer needs "some second meter." It
needs a simultaneous dual-meter witness where the ordinary monitored record is
held fixed and the second meter alone can change the admissible TaF verdict.

T137 asks a more exact question:

```text
If a proposed second meter is only a downstream transform of the ordinary
monitored record, can it ever supply that fixed-record witness?
```

## Result

No.

If the second meter `Z` is conditionally screened off by the ordinary monitored
record `Y`, meaning `P(Z | B, Y) = P(Z | Y)` for the branch-relevant variable
`B`, then `Z` cannot produce a branch-sensitive split once `Y` is fixed. It may
be physically distinct hardware, but it is not an independent TaF axis in the
only sense Q1C needs.

That yields a sharper null class:

```text
Simultaneous downstream second meters are null for Q1C.
```

## Executable Witness Family

T137 uses three finite witness families with the same ordinary monitored
channel:

1. `exact_duplicate_meter`
   The second meter is an exact copy of the ordinary monitored record.
2. `noisy_downstream_meter`
   The second meter is a noisy downstream transform of the ordinary monitored
   record.
3. `branch_sensitive_independent_meter`
   The second meter depends on branch-relevant structure not screened off by
   the ordinary monitored record.

The first two are null. The third is not evidence for TaF, but it identifies
the minimal structural escape hatch.

## Why This Matters

The repo's weak-measurement language previously risked treating "extra hardware"
as progress by itself. T137 blocks that move.

The relevant distinction is not:

- one meter versus two meters.

It is:

- a second channel that is screened off by the first record; versus
- a second channel that still carries branch-sensitive information after the
  first record is fixed.

Only the second object could ever reopen Q1C.

## What This Improved

T137 converts the phrase "independent second meter" into an operational test.

That matters for both literature triage and platform design:

1. a thermal or calorimetric channel does not help merely because it is built
   from different hardware;
2. a simultaneous auxiliary log does not help merely because it is recorded in
   parallel;
3. a second meter helps only if it escapes conditional determination by the
   ordinary monitored record.

## What This Weakened Or Falsified

This weakens a common fallback rescue:

```text
Even if the second meter does not replace the ordinary readout, maybe any
parallel auxiliary channel already counts as the missing TaF axis.
```

T137 says no. Parallelism is not enough. Physical distinctness is not enough.
Conditional non-redundancy is the real gate.

## Boundary Of The Result

T137 is not a no-go theorem for all dual-meter experiments.

It does not show that a branch-sensitive simultaneous second meter is
impossible. The executable `branch_sensitive_independent_meter` witness exists
precisely to show the logical escape class.

What T137 does show is narrower and more useful:

```text
If the second meter is only a downstream transform of the ordinary monitored
record, it cannot supply the fixed-record split that Q1C requires.
```

## Updated Strongest Claim

Q1C should now be stated this way:

```text
Weak measurement remains dormant unless a monitored-qubit platform names a
calibrated, pre-registered second meter that is not conditionally screened off
by the ordinary monitored record and that changes the admissible TaF verdict
while the ordinary monitored statistics are fixed.
```

## Falsification Condition

T137 fails if a platform supplies a second meter that is demonstrably only a
downstream kernel of the standard monitored record yet still yields a
pre-registered fixed-record TaF verdict split.

That would mean the screening-off criterion used here is too weak or wrongly
posed.

## Open Blocker

The blocker is now more specific than "find a simultaneous dual meter."

The blocker is:

```text
find one monitored-qubit protocol where the auxiliary meter couples to branch-
relevant structure that is not recoverable from the ordinary trajectory record
or its downstream transforms.
```

## Recommended Next Move

Do not spend another hour scanning generic second-meter literature.

Search only for one of these two objects:

1. a monitored-qubit protocol with a branch-sensitive auxiliary meter that
   provably escapes screening-off by the ordinary record; or
2. a stronger physical obstruction showing that standard weak-measurement
   architectures make such a meter structurally unlikely.
