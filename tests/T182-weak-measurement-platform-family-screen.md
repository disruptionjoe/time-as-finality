# T182: Weak-Measurement Platform Family Screen

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [N9: Q1C Platform Candidate Census](../literature/N9-q1c-platform-candidate-census.md)

## Question

Can the current named Q1C-adjacent platform families be classified
algorithmically rather than by prose judgment, and does any named family remain
live after that screen?

## Motivation

N9 already did the literature work, but it still leaves a reviewer with a soft
objection:

```text
maybe one of those platform families is closer to a live Q1C route than the
note says
```

T182 removes that softness by making the census executable.

## Setup

Screen six named source-backed families:

1. homodyne trajectory platforms;
2. jump-reversal / uncollapse control platforms;
3. microwave photon-counter replacement readout;
4. thermal-detector replacement readout;
5. nanocalorimetric trajectory platforms;
6. calorimeter-assisted broadband quadrature platforms.

Treat two hypothetical positive controls as admissible:

1. a monitored-qubit extra-environment channel that is not screened off by the
   full ordinary record and freezes the T166 packet;
2. an enlarged instrument that preserves the full standard record under a
   declared eventwise back-projection and freezes the T166 packet.

## Success Criteria

- Every named family lands in a specific null or blocked class.
- The two live Q1C architecture classes still admit explicit positive controls.
- No named family is quietly promoted just because it sounds like a second
  meter.
- The census becomes reproducible without re-reading the literature note.

## Failure Criteria

- A named family is rejected only by hand-waving rather than a typed screen.
- Honest readout replacement is confused with a simultaneous auxiliary channel.
- Task-changed platforms are treated as monitored-qubit evidence.
- Positive controls for the live Q1C classes are accidentally ruled out.

## Claim Impact

Q1C remains `dormant`.

The sharper statement is:

```text
The currently named Q1C-adjacent platform families are now executable null or
blocked classes. None instantiate a live extra-environment auxiliary channel or
an honest enlarged instrument with a preserved full-standard target and
back-projection.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_platform_family_screen -v
python -m models.run_t182
```
