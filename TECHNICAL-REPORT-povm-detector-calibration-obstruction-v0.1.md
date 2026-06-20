# Technical Report: POVM Detector Calibration Obstruction v0.1

## Claim Under Test

Q1 says quantum states can be real without yet being finalized as classical
records in a particular observer-environment context. T62 narrowed this to an
access-boundary discriminator. T64 moved that discriminator into a
Stern-Gerlach detector proxy, but it still declared binary channel reliabilities
and found threshold sensitivity.

T66 tests the next obvious repair: replace declared reliabilities with
calibrated binary POVM response matrices.

The report's posture is intentionally conservative. T66 does not claim new
quantum dynamics, collapse, a Born-rule derivation, or a detector simulation.

## Model

Each detector fragment is represented by a two-outcome response matrix:

```text
P(readout = + | spin = +)
P(readout = + | spin = -)
```

For a uniform binary source, the fragment information is:

```text
I(S;R) = H(R) - H(R|S)
```

The calibrated detector proxy contains:

| Fragment | Response `P(+|+)` | Response `P(+|-)` | Availability | Provenance class |
| --- | ---: | ---: | --- | --- |
| `screen_spot` | `0.995` | `0.015` | `1.0 <= t <= 3.0` | `screen_grain` |
| `photodiode_pulse` | `0.985` | `0.035` | `1.5 <= t <= 5.0` | `electronics` |
| `local_log` | `0.995` | `0.005` | `2.0 <= t <= 10.0` | `local_log` |
| `network_archive` | `0.995` | `0.005` | `4.0 <= t <= 20.0` | variable |
| `thermal_bath_trace` | `0.62` | `0.50` | `0.5 <= t <= 20.0` | `thermal_bath` |

Raw detector redundancy counts available fragments above the information
threshold. D1 holder redundancy counts only fragments that are both accessible
to the observer and independent under the declared provenance partition.

## Results

T66 preserves the T64 access-boundary distinction in calibrated-response
language:

- `povm_local_lab_after_readout`: threshold `0.75`, total `R_delta = 3`,
  independent accessible `R_delta = 3`, D1 profile `(3, 3, 1, 1)`.
- `povm_redundant_but_inaccessible`: threshold `0.75`, total `R_delta = 3`,
  D1 profile `(0, 0, 0, 0)`.

The stronger result is negative. POVM calibration alone does not determine the
D1 verdict.

First, the same local detector response at `t = 2.5` finalizes at threshold
`0.75` and fails to finalize at threshold `0.9`. The POVM response matrix did
not choose the threshold.

Second, `archive_copy_partition` and `archive_independent_partition` have the
same response matrices and same access window. Treating the archive as a copy
of the local log gives independent redundancy `2`, below the reconstruction
threshold `3`. Treating the archive as an independent provenance class gives
independent redundancy `3`, so D1 finalizes. The POVM response matrix did not
choose the provenance partition.

The no-signalling guardrail passes. In the finite singlet audit, remote setting
changes leave the local POVM readout marginal invariant.

## Current Strongest Claim

A calibrated binary POVM response lets TaF compute detector fragment
information and re-run the access-window discriminator. It does not determine
finality without independent threshold and provenance assumptions.

## Weakened Claim

Q1 is weaker after T66. It cannot claim a calibration-free Stern-Gerlach
prediction from POVM data alone. The same calibrated response data can support
different D1 verdicts under different threshold or provenance rules.

## Falsification Criterion

Q1 loses independent measurement content if either condition holds:

1. Detector physics cannot non-arbitrarily fix the information threshold and
   provenance/independence partition before D1 is evaluated.
2. Once those rules are fixed, D1 always equals standard fragment redundancy
   `R_delta`.

## What This Does Not Show

- It does not simulate a Stern-Gerlach magnet.
- It does not derive Born probabilities.
- It does not solve the measurement problem.
- It does not refute decoherence or Quantum Darwinism.
- It does not show that POVMs are insufficient for ordinary detector physics.
- It only shows that POVM response matrices alone are insufficient to fix TaF's
  D1 finality predicate.

## Next Work

Derive the independence partition from a detector provenance graph or measured
channel-correlation matrix. Then pre-register the information threshold before
comparing D1 with standard `R_delta`.

## Reproduction

```bash
python -m unittest tests.test_povm_detector_calibration_obstruction -v
python -m models.run_t66
```
