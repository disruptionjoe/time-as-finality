# Technical Report: Weak-Measurement Dual-Meter Screen v0.1

## Claim Under Test

After T91 and T93, the most plausible weak-measurement rescue is no longer a
better reconstruction of the same trajectory record. It is a dual-meter
platform: keep the standard monitored record, add an independent physical
meter, and ask whether that second meter can change the TaF verdict while the
standard monitored statistics stay fixed.

## Result

No currently identified platform clears that gate.

The literature does expose real second meters. Nanocalorimetry and bolometric
readout show that superconducting circuits can be monitored through absorbed
energy or temperature-sensitive detection rather than only through ordinary
microwave voltage amplification. But this does not yet rescue Q1C, for two
reasons:

1. the thermal or calorimetric channel is currently used as an alternative
   readout chain, not as a simultaneous independent axis held alongside a fixed
   standard trajectory record; and
2. no platform in the screened set names a pre-registered same-statistics
   witness where the standard monitored record is fixed but the second meter
   alone changes a TaF verdict.

The strongest earned statement is therefore negative:

```text
Real second-meter instrumentation exists for superconducting measurement, but
the repo still lacks a dual-meter weak-measurement platform that produces a
verdict-changing independent TaF axis under fixed standard monitored
statistics.
```

## Screened Platform Classes

| Platform class | What is real in the literature | Q1C verdict | Reason |
| --- | --- | --- | --- |
| standard homodyne / no-click monitoring | continuous monitored record of a superconducting qubit trajectory | `already_rejected` | T91 already showed the candidate TaF axis is reconstructed from the same monitored record |
| superconducting uncollapse / jump reversal | conditional reversal or warning-and-feedback control | `already_rejected` | T91 and T93 already showed the witness collapses to postselection or same-stream control |
| nanocalorimetric trajectory proposals | resistor/nanocalorimeter click stream tied to heat exchange or photon absorption | `alternate_record_not_independent_axis` | the calorimetric channel supplies a different measurement record, but not a fixed-statistics second axis held alongside an unchanged standard record |
| bolometric qubit readout | thermal detector readout of qubit state through absorbed power and electron-temperature response | `alternate_readout_not_dual_meter_witness` | the bolometer is a substitute readout chain; no witness is named where ordinary monitored statistics are fixed and the bolometric record alone changes TaF |

## Why The New Literature Does Not Yet Rescue Q1C

### 1. Dual-meter hardware exists, but mostly as replacement readout

The strongest new-looking candidate is bolometric or calorimetric detection.
Recent work shows a superconducting qubit can be read out through a thermal
detector rather than a parametric amplifier, and older calorimetry work argues
that temperature traces can monitor microwave-photon absorption events in
superconducting circuits. This matters because it proves that "independent
physical meter" is not science fiction.

But Q1C needs more than a second meter in the abstract. It needs a witness
shape in which the standard monitored trajectory statistics are fixed and the
second meter still changes the TaF verdict. The screened papers do not provide
that. The thermal channel is the measurement channel, not an independently
verdict-changing annotation on top of a fixed standard monitoring stream.

### 2. Alternative measurement is not the same as independent verdict content

Changing from I/Q amplification to a thermal detector can alter noise,
bandwidth, backaction, and what the lab natively records. That may be valuable
for engineering. But it does not, by itself, produce TaF-specific independent
content. If the second meter simply defines a different ordinary measurement
record, then TaF has not yet obtained the "same standard statistics, different
TaF verdict" witness required by T90 and T93.

### 3. Calorimetric trajectory language still tracks the measurement outcomes

The nanocalorimetry literature is especially close to the target because it
connects jump trajectories to calorimetric clicks. But the paper-screened
object is still a trajectory record of detection events. The repo has not yet
shown how to use that record as a second axis while holding an ordinary
homodyne/no-click record fixed. Without that same-statistics comparison, the
route is still an alternate instrumentation proposal, not a discriminator.

## Current Strongest Claim

Q1C should now be stated as:

```text
Weak measurement remains dormant even after screening calorimetric and thermal
readout candidates. A real second meter exists in the literature, but no
screened platform yet supplies a simultaneous dual-meter witness where the
independent meter changes the TaF verdict under fixed standard monitored
statistics.
```

## What This Improved

This report closes a specific loophole left open by T93. The repo no longer has
to speak vaguely about an "independent physical meter" as if no hardware family
even points in that direction. It can now say something sharper:

- second-meter hardware exists;
- it is experimentally serious; but
- it still does not clear the Q1C reinstatement gate.

That is stronger than either optimism or blanket dismissal.

## What This Weakened Or Falsified

This weakens the idea that weak measurement can be revived merely by pointing
to calorimetry, bolometry, or energy-sensitive detectors in superconducting
circuits.

It also weakens a softer escape hatch in the current prose: "independent meter"
should no longer be treated as a mostly unspecified future desideratum. The
repo has now screened the most obvious hardware family and found that it does
not yet deliver the needed fixed-statistics witness.

## Falsification Condition

This report fails if a concrete platform supplies all of the following:

1. a standard monitored weak-measurement record;
2. a simultaneous second physical meter fixed before analysis;
3. a same-standard-statistics comparison where the second meter alone changes
   the TaF verdict; and
4. a second-meter value that is not reconstructible from the first record and
   control schedule.

If that object is built or clearly specified, Q1C should be reopened
immediately.

## Sources Screened

- Mahdi Naghiloo, *Introduction to Experimental Quantum Measurement with
  Superconducting Qubits* (arXiv:1904.09291), for the baseline continuous
  monitoring picture.
- Bayan Karimi and Jukka P. Pekola, *Quantum trajectory analysis of single
  microwave photon detection by nanocalorimetry* (PRL 124, 170601, 2020;
  arXiv:2001.01943), for calorimetric trajectory detection.
- Laura Maccari et al., *Reaching the ultimate energy resolution of a quantum
  detector* (Nature Communications 11, 173, 2020), for absorber temperature
  traces and calorimetric quantum-trajectory motivation.
- András M. Gunyhó et al., *Single-shot readout of a superconducting qubit
  using a thermal detector* (Nature Electronics 7, 288-298, 2024), for a real
  thermal-detector readout chain in superconducting qubits.

## Claim Ledger Update

Q1C remains `dormant`.

Add the following narrowing:

```text
Second-meter hardware families now exist in the screened literature, but they
currently instantiate alternate readout chains rather than a simultaneous
dual-meter witness with fixed standard monitored statistics.
```

## Open Blocker

The missing object is now very specific: a simultaneous dual-meter experiment
with one ordinary weak-measurement record and one independent physical meter,
plus a pre-registered fixture where the ordinary monitored statistics stay
fixed and the second meter alone changes the admissible TaF verdict.

## Next Work

Either:

1. search for a genuine simultaneous dual-meter protocol, likely in a
   thermodynamic-trajectory or error-syndrome setting rather than standard
   single-stream weak measurement; or
2. stop treating Q1C as a near-term experiment route and move the active
   experimental frontier fully onto detector provenance until such a protocol
   exists.
