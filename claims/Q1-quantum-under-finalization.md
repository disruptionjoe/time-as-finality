# Q1: Quantum Under-Finalization

## Claim

Quantum states can be real but not yet finalized as classical records in a particular observer-environment context.

## Class

Conjecture.

## Status

Partially supported.

## What This Does Not Claim

- It does not say quantum states are unreal.
- It does not say human consciousness collapses the wavefunction.
- It does not say decoherence alone solves the measurement problem.
- It does not restore naive local hidden variables.
- It does not allow faster-than-light signalling.

## Why It Might Be True

The quantum/classical transition is deeply tied to record formation, decoherence, pointer bases, environmental redundancy, and observer access. "Under-finalized" may help distinguish real quantum constraint from settled classical fact.

For entanglement, the safe finality chain is:

```text
entangled joint state
  -> local measurement interaction
  -> local record formation
  -> decoherence / environmental redundancy
  -> observer-relative finality
  -> later causal comparison
  -> globally reconciled correlation record
```

The key distinction is that an entangled joint constraint can be real before separated local observers share a classical finalized record. Shared classical finality requires causal reconciliation. The correlation is not a controllable faster-than-light message.

Proof-carrying language may help here: later comparison can certify a nonclassical joint constraint without implying that either local observer had full access to the global state or a hidden local answer in advance.

## How It Could Fail

- It adds no clarity beyond decoherence or quantum Darwinism.
- It smuggles in collapse without saying so.
- It cannot handle basis-dependence.
- It violates Bell/no-signalling constraints.
- It treats a later correlation record as if it were an earlier local hidden variable.
- It turns proof or verification language into an encrypted-message metaphor for entanglement.

## Tests

- [T2: Quantum Measurement Record Finality](../tests/T2-quantum-measurement-record-finality.md)
- [T6: Snowball Record Finality](../tests/T6-snowball-record-finality.md)
- [T21: Bell Contextuality Finality](../tests/T21-bell-contextuality-finality.md)
- [T22: D1 Physical Reduction Map](../tests/T22-d1-physical-reduction-map.md)
- [T23: Invariant-Preserving Transformations](../tests/T23-invariant-preserving-transformations.md)
- [T62: Noisy Measurement Access-Boundary Discriminator](../tests/T62-noisy-measurement-access-boundary.md)
- [T64: Stern-Gerlach Detector Access-Window Discriminator](../tests/T64-stern-gerlach-access-window.md)
- [T66: POVM Detector Calibration Obstruction](../tests/T66-povm-detector-calibration-obstruction.md)
- [T67: POVM Correlation Provenance Obstruction](../tests/T67-povm-correlation-provenance-obstruction.md)
- [T68: Intervention-Sensitive Detector Provenance](../tests/T68-intervention-sensitive-detector-provenance.md)
- [T70: Detector Provenance Robustness](../tests/T70-detector-provenance-robustness.md)
- [T72: Physical Provenance Protocol](../tests/T72-physical-provenance-protocol.md)
- [T74: Provenance Protocol Monte Carlo](../tests/T74-provenance-protocol-monte-carlo.md)

## T21 Result

[T21](../tests/T21-bell-contextuality-finality.md) gives Q1 a finite
contextuality model. Four CHSH-style local measurement contexts each have
valid local finality sections, but no global assignment satisfies all
contexts.

This supports the narrow under-finalization claim: local classical records can
be finalized in their own measurement contexts while a single global
noncontextual record assignment remains unavailable. The result is structural,
not a detector-level simulation.

The probability-bearing extension compares three CHSH regimes: classical
noncontextual score `2`, quantum Tsirelson score `2*sqrt(2)`, and PR-box
no-signalling score `4`. This sharpens Q1's claim: quantum contextuality sits
between global classical finality and post-quantum no-signalling consistency.
- [Proof-Carrying Record Finality](../open-problems/proof-carrying-record-finality.md)

## T22 Result

[T22](../tests/T22-d1-physical-reduction-map.md) gives Q1 the first executable
comparison requested by the quantum-Darwinism neighbor. In a binary
system-environment toy model, each informative environment fragment has
`I(S;E_i) = 1.0` bit and the noise fragment has `I(S;N1) = 0.0`.

With delta `0.1`, the information threshold is `0.9` bits. Raw accessible
environmental redundancy counts `E1`, `E2`, and `E3`, for a value of `3`.
After quotienting the correlated duplicate `E3` with `E1`, the
independence-corrected accessible redundancy is `2`, matching D1 holder
redundancy.

This partially supports Q1 only as a record-finality vocabulary for
environmental redundancy. It does not simulate quantum amplitudes,
decoherence dynamics, detector noise, or collapse.

## T2 v0.1 Result

[T2](../tests/T2-quantum-measurement-record-finality.md) extends T22 into a
small dynamical measurement model:

```text
S -> A -> E1, E2, E3
```

using reversible CNOT interactions in the `computational_z` pointer basis.
The model computes reduced pointer coherence, fragment mutual information,
environmental `R_delta`, and observer-relative D1 profiles.

The main positive result is a decohered-but-inaccessible case. After the first
environment copy, pointer coherence is `0.0`; after all copies,
environmental `R_delta` is `3`. But an outside observer with no access has:

```text
D1 = (0, 0, 0, 0)
```

This supports Q1's narrow claim that "decohered in the pointer basis" and
"final as a classical record for this observer" are distinct predicates in
the toy substrate. It also preserves the guardrail: T2 uses unitary dynamics
only and never selects a collapse outcome.

## T23 Result

[T23](../tests/T23-invariant-preserving-transformations.md) turns the T2 to
T22 quantum bridge into a typed invariant-preserving reduction:

```text
T2 global measurement state
  -> T2 local observer D1 view
  -> T22 reduction schema
```

The composition preserves:

```text
pointer_basis = computational_z
```

and the second reduction preserves holder redundancy, accessible support, and
observer-access indexing. This supports Q1 as part of a broader invariant
transport program, while keeping the same limits: no collapse, no Born-rule
derivation, no detector-level model, and no claim that quantum measurement is
equivalent to the other T23 domains.

## T62 Result

[T62](../tests/T62-noisy-measurement-access-boundary.md) weakens Q1 away from
new noisy measurement dynamics. It separates pointer decoherence,
Quantum-Darwinism-style environmental redundancy, and observer-relative D1
finality in a finite noisy-channel matrix.

The strongest positive result is the `redundant_but_inaccessible` witness:
environmental records can be redundant while an observer with no access window
has D1 profile `(0, 0, 0, 0)`. The main boundary is that
`decohered_not_darwinist` is already standard decoherence-versus-redundancy
territory. TaF adds only access-boundary and independence bookkeeping.

## T64 Result

[T64](../tests/T64-stern-gerlach-access-window.md) moves the T62 audit into a
Stern-Gerlach detector proxy with screen, electronics, log, archive, and weak
bath fragments. It preserves the access-boundary distinction but weakens Q1:
detector finality flips under plausible information-threshold choices.

T64 also adds a no-signalling guardrail. In the entangled-pair variant, remote
setting changes alter correlations but not the local noisy detector marginal.
The earned claim is therefore narrow: TaF can express an access-window and
independence-filter predicate over already formed detector records, but it has
no calibration-free Stern-Gerlach prediction yet.

## T66-T74 Detector Provenance Result

[T66](../tests/T66-povm-detector-calibration-obstruction.md) replaces declared
channel reliabilities with calibrated POVM response matrices and shows that
threshold/provenance underdetermination remains. [T67](../tests/T67-povm-correlation-provenance-obstruction.md)
then refutes the passive-correlation repair: copied archives and independent
readout chains can have identical pairwise agreement and phi correlation while
requiring opposite D1 independence partitions.

[T68](../tests/T68-intervention-sensitive-detector-provenance.md) gives a
conditional positive result. Intervention-sensitive provenance metadata can
fix the partition before D1 scoring through origin tags, perturbation response,
delayed-copy ancestry, and signed provenance DAG data.

[T70](../tests/T70-detector-provenance-robustness.md) stress-tests that repair.
The rule survives moderate single-channel degradation when redundant
authenticated provenance channels remain. It fails cleanly when trusted
channels are absent or contaminated: D1 is withheld rather than inferred from
passive similarity, partial-DAG thresholds, or semantic labels.

[T72](../tests/T72-physical-provenance-protocol.md) replaces Boolean
degradation flags with interval/probability protocol parameters: clock error,
signature failure, archive batching, trust boundaries, perturbation back-action,
and partial provenance-DAG observability. It shows robust recovery under
declared physical reliability bounds, an ambiguous withhold region, an ad hoc
threshold failure, and unsafe false-independence/false-dependence regimes.

[T74](../tests/T74-provenance-protocol-monte-carlo.md) converts that regime
table into a deterministic stress-prior audit. In `400` samples per family,
robust recovery survives in the `engineered_lab` family at rate `0.905`, while
it disappears entirely in the broader `mixed_lab` and `field_degraded`
families. Outside the engineered corner, the protocol mostly withholds D1
rather than fixing a provenance partition.

The detector branch of Q1 should therefore be stated as an
intervention-sensitive provenance/accounting framework over already formed
detector records under explicit physical protocol assumptions. It does not
recover detector finality from calibrated outcome statistics or passive
correlations alone, and it is not generically recoverable from provenance
metadata unless the apparatus sits in a narrow engineered protocol region.

## Contribution Needed

Replace T74's stress priors with calibration posteriors from one concrete
detector stack: measured clock distributions, signature failure probabilities,
archive batching, subsystem trust boundaries, perturbation back-action
matrices, and partial DAG observability. Only after that should the detector
branch be compared with decoherence, quantum Darwinism, relational QM,
consistent histories, many-worlds, and QBism.
