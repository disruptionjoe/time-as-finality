# T64: Stern-Gerlach Detector Access-Window Discriminator

## Target Claims

- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T2: Quantum Measurement Record Finality](T2-quantum-measurement-record-finality.md)
- [T22: D1 Physical Reduction Map](T22-d1-physical-reduction-map.md)
- [T62: Noisy Measurement Access-Boundary Discriminator](T62-noisy-measurement-access-boundary.md)

## Purpose

T64 tests the most important open boundary left by T62: whether the
access-boundary distinction survives a detector-level measurement proxy.  The
model uses a Stern-Gerlach readout as a finite family of noisy binary detector
fragments rather than as an abstract list of channels.

The goal is not to explain collapse, derive Born probabilities, or improve on
standard decoherence.  The goal is to check whether TaF contributes anything
after the following are explicitly declared:

- detector fragment partition;
- fragment reliability and information threshold;
- observer access window;
- independence partition for duplicate records;
- no-signalling constraint for an entangled-pair variant.

## Setup

The detector proxy has five fragments:

1. `screen_spot`: transient spatial detector spot.
2. `photodiode_pulse`: local electronics pulse.
3. `local_log`: timestamped detector log.
4. `network_archive`: copy of the local log, not independent.
5. `thermal_bath_trace`: weak bath trace below the information threshold.

Each fragment is treated as a binary symmetric readout channel:

```text
I(S;F) = 1 - H_2(error)
```

where `error = 1 - reliability`.  A fragment contributes to raw
Quantum-Darwinism-style `R_delta` when it is available at observer time and its
information crosses the declared threshold.  It contributes to D1 holder
redundancy only when it is also inside the observer access boundary and belongs
to a distinct independence class.

The entangled-pair guardrail uses singlet-style joint probabilities with zero
local marginals.  Remote setting changes are allowed to change correlations but
must not change the local detector readout marginal.

## Witness Matrix

T64 contains five finite witnesses:

1. `local_lab_after_readout`: decoherence, detector redundancy, and local D1
   finality agree.
2. `redundant_but_before_access`: detector records exist, but the observer has
   no access window.
3. `single_channel_early_window`: one transient detector channel is accessible
   before redundant records exist.
4. `duplicate_archive_boundary`: raw accessible redundancy crosses threshold,
   but a copied archive does not add an independent holder class.
5. `high_threshold_fragility`: the same detector access window fails under a
   stricter information threshold.

## Success Criteria

1. The model realizes all witness classes with executable tests.
2. The threshold sweep identifies whether D1 finality is calibration-sensitive.
3. The no-signalling audit shows local detector marginals do not depend on
   remote setting choices.
4. The result weakens Q1 if thresholds or independence partitions are doing too
   much work.

## Failure Criteria

1. Decoherence is treated as collapse.
2. Remote setting changes alter the local detector readout marginal.
3. The result treats declared thresholds as predictions.
4. Archive copies are counted as independent detector holders.
5. The result claims a new Stern-Gerlach dynamics.

## Result

Implemented as T64 v0.1.

The strongest surviving claim is limited: TaF adds an access-window and
independence-filter predicate over already formed detector records.  It does
not add collapse, hidden variables, a Born-rule derivation, or a new noisy
measurement dynamics.

The main weakening is threshold sensitivity.  In the sweep, the detector can be
finalized at threshold `0.75` but not at threshold `0.9` for the same observer
time.  Therefore Q1 has no calibration-free measurement prediction yet.

## Reproduction

```bash
python -m unittest tests.test_stern_gerlach_access_window -v
python -m models.run_t64
```
