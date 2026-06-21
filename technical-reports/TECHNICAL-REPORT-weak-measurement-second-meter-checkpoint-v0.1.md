# Technical Report: Weak-Measurement Second-Meter Checkpoint v0.1

## Claim Under Test

T130 left one obvious loophole open: perhaps newer calorimetric or
energy-sensitive measurement work has finally produced the concrete
simultaneous second-meter platform that Q1C requires.

This checkpoint asks a narrow question as of 2026-06-20:

```text
Does any screened recent platform give a standard monitored weak-measurement
record plus a simultaneous independent physical meter, together with a
pre-registered fixed-standard-statistics witness where the second meter alone
changes the TaF verdict?
```

## Result

No screened source clears that gate.

The recent literature improves the hardware story but not the TaF witness
story:

1. thermal-detector superconducting-qubit readout demonstrates a real
   non-amplifier measurement chain, but it acts as a substitute readout rather
   than a simultaneous second axis held beside a fixed ordinary monitored
   trajectory;
2. nanocalorimetric trajectory work gives a real heat-sensitive detection
   record, but still as the measurement record whose clicks define the
   trajectory rather than as an additional verdict-changing axis over fixed
   standard statistics;
3. broadband pulsed homodyne with calorimeters shows that calorimeters can be
   incorporated into quadrature-style measurement constructions, but the object
   is a mode-measurement formalism, not a monitored superconducting-qubit
   platform with fixed ordinary trajectory statistics and a separate TaF meter.

The current strongest statement remains negative:

```text
Second-meter instrumentation is real, but the screened 2020-2025 literature
still does not provide the simultaneous fixed-statistics dual-meter witness
required to reopen Q1C.
```

## Sources Screened

- Bayan Karimi and Jukka P. Pekola, "Quantum trajectory analysis of single
  microwave photon detection by nanocalorimetry" (arXiv:2001.01943, January 7,
  2020).
- Andras M. Gunyho et al., "Single-Shot Readout of a Superconducting Qubit
  Using a Thermal Detector" (arXiv:2303.03668, March 7, 2023; later published
  in Nature Electronics 2024).
- Ezad Shojaee et al., "Broadband pulsed quadrature measurements with
  calorimeters" (arXiv:2503.00188, February 28, 2025).

## Why The Route Still Fails

### 1. Replacement readout is not the required witness

The 2023/2024 thermal-detector qubit-readout work matters because it proves
that a superconducting qubit can be read out through a thermal detector rather
than a parametric-amplifier voltage chain. That removes the objection that an
independent physical meter is pure speculation.

But it does not clear Q1C. The thermal detector is the readout chain. The
paper does not furnish a same-run comparison where ordinary monitored
statistics are held fixed and a second meter alone changes the TaF verdict.

### 2. Calorimetric trajectories are still ordinary trajectory records

The nanocalorimetry trajectory paper is even closer to the target because it
connects jump trajectories to heat-sensitive clicks. But the calorimetric
click sequence is still the record that defines the trajectory. It is not a
simultaneous auxiliary meter layered on top of a fixed homodyne or no-click
stream in a way that changes only the TaF verdict.

### 3. Calorimeter-assisted homodyne is the wrong object

The 2025 broadband pulsed homodyne paper is important because it shows that
calorimeters can participate in homodyne-like quadrature measurement
constructions. But that does not produce the monitored-qubit dual-meter object
the repo needs. It changes the measurement formalism itself. It does not name
an event-level monitored-qubit protocol with:

1. a standard weak-measurement record;
2. a simultaneous second physical meter;
3. fixed standard monitored statistics; and
4. a second-meter-only TaF verdict split.

## Current Strongest Claim

Q1C should now be stated more sharply:

```text
Weak measurement remains dormant not only because the old homodyne,
uncollapse, and jump-reversal routes fail, but also because the most relevant
screened recent second-meter literature still gives replacement readout or a
different measurement formalism rather than a simultaneous fixed-statistics
dual-meter witness.
```

## What This Improved

This checkpoint reduces a remaining ambiguity in the repo's weak-measurement
language. "Look for a second meter" is now too vague. The repo can ask for one
very specific object:

- one ordinary monitored weak-measurement record;
- one simultaneous independent physical meter;
- a pre-registered comparison with fixed ordinary monitored statistics; and
- a TaF verdict split caused only by the second meter.

Anything short of that is no longer a near-miss. It is a different readout
proposal or a different measurement task.

## What This Weakened Or Falsified

This weakens two softer rescue stories.

1. It is no longer enough to point to any superconducting calorimetric or
   thermal readout paper and say that Q1C now has "an independent meter."
2. It is no longer enough to point to calorimeter-assisted homodyne formalisms
   without also producing a monitored-qubit, same-standard-statistics witness.

## Falsification Condition

This checkpoint fails if a concrete platform or protocol supplies all of the
following:

1. a standard monitored weak-measurement record;
2. a simultaneous second physical meter fixed before analysis;
3. a comparison where the ordinary monitored statistics are fixed;
4. a TaF verdict change caused only by the second meter; and
5. a second-meter value that is not reconstructible from the first record plus
   control schedule.

If that object appears, Q1C should be reopened immediately.

## Claim Ledger Update

Q1C remains `dormant`.

Add this narrowing:

```text
Recent second-meter literature removes the "no hardware family exists" excuse,
but still fails the stronger simultaneity and fixed-standard-statistics gate.
```

## Open Blocker

The blocker is no longer "find any second meter." The blocker is:

```text
find one monitored-qubit protocol with simultaneous dual meters and a fixed-
statistics verdict split.
```

Without that object, weak measurement remains a reinstatement-only branch.

## Recommended Next Move

Stop scanning generic calorimetry papers for rhetorical support.

Search only for one of two objects:

1. a genuine simultaneous monitored-qubit dual-meter protocol; or
2. a clear impossibility or practical-obstruction note showing why standard
   weak-measurement platforms are structurally unlikely to furnish one.
