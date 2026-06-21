# Technical Report: Stern-Gerlach Detector Access-Window Discriminator v0.1

## Claim Under Test

Q1 says quantum states can be real without yet being finalized as classical
records in a particular observer-environment context.  T62 narrowed this to an
access-boundary discriminator over noisy record channels.  T64 tests whether
that narrowed claim survives a detector-level Stern-Gerlach proxy.

The report's posture is deliberately weak: T64 does not claim new quantum
dynamics, collapse, hidden variables, or a Born-rule derivation.

## Model

The detector is represented by five binary readout fragments:

| Fragment | Role | Reliability | Availability | Independence class |
| --- | --- | ---: | --- | --- |
| `screen_spot` | transient detector spot | `0.985` | `1.0 <= t <= 3.0` | `screen_grain` |
| `photodiode_pulse` | local electronics pulse | `0.97` | `1.5 <= t <= 5.0` | `electronics` |
| `local_log` | timestamped local log | `0.99` | `2.0 <= t <= 10.0` | `local_log` |
| `network_archive` | copied archive of the log | `0.99` | `4.0 <= t <= 20.0` | `local_log` |
| `thermal_bath_trace` | weak bath trace | `0.62` | `0.5 <= t <= 20.0` | `thermal_bath` |

For each fragment, the information score is:

```text
I(S;F) = 1 - H_2(1 - reliability)
```

Raw detector redundancy counts currently available fragments above the
information threshold.  D1 holder redundancy counts only fragments that are
both accessible to the observer and independent under the declared independence
partition.

Pointer coherence is represented only by a multiplicative suppression proxy
over fragments that have started by observer time.  This is a toy
decoherence proxy, not a Hamiltonian simulation.

## Results

T64 reproduces the T62 access-boundary separation in a detector-shaped model:

- `local_lab_after_readout`: total `R_delta = 3`, independent accessible
  `R_delta = 3`, D1 profile `(3, 3, 1, 2)`.
- `redundant_but_before_access`: total `R_delta = 3`, independent accessible
  `R_delta = 0`, D1 profile `(0, 0, 0, 0)`.
- `duplicate_archive_boundary`: accessible raw `R_delta = 3`, independent
  accessible `R_delta = 2`, so archive copying overcounts finality.

The threshold sweep is the most important weakening.  At `t = 2.5`, the local
detector window is finalized at information threshold `0.75` but not at
threshold `0.9`.  At `t = 4.5`, the same flip occurs after the screen spot has
expired and the archive mirror has appeared.  Therefore detector-level D1 is
not a calibration-free prediction in this model.

The no-signalling audit passes.  In a singlet-style entangled-pair variant, the
local noisy detector readout marginal remains `0.5` under all tested remote
settings for both local settings.  This is a guardrail, not a derivation of
quantum correlations.

## Current Strongest Claim

In the T64 Stern-Gerlach toy detector, TaF adds at most an observer-access and
independence-filter predicate over already formed detector records.  It does
not add collapse or new noisy measurement dynamics.

## Weakened Claim

Q1 is weaker after T64.  The detector-finality verdict can flip under plausible
information-threshold choices.  Unless the threshold, access window, and
independence partition are physically justified before evaluation, D1 is only
bookkeeping over standard detector-record structure.

## Falsification Criterion

Q1 loses independent measurement content if either condition holds:

1. Detector physics fixes admissible access windows and independence classes
   such that D1 always equals standard fragment redundancy `R_delta`.
2. Detector physics cannot specify those inputs non-arbitrarily.

## What This Does Not Show

- It does not simulate a Stern-Gerlach magnet.
- It does not derive Born probabilities.
- It does not solve the measurement problem.
- It does not refute decoherence or Quantum Darwinism.
- It does not claim that an observer's knowledge changes a remote marginal.

## Next Work

Replace the declared binary channels with a calibrated detector model: a POVM,
scattering response curve, or explicit detector-noise dataset that fixes
fragment reliabilities, access windows, and independence classes before the D1
predicate is evaluated.

## Reproduction

```bash
python -m unittest tests.test_stern_gerlach_access_window -v
python -m models.run_t64
```
