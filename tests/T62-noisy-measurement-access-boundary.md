# T62: Noisy Measurement Access-Boundary Discriminator

## Target Claims

- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T2: Quantum Measurement Record Finality](T2-quantum-measurement-record-finality.md)
- [T22: D1 Physical Reduction Map](T22-d1-physical-reduction-map.md)

## Purpose

T62 tests whether the quantum-measurement thread can survive noisy partial
records without overclaiming. It separates three predicates:

- pointer decoherence;
- Quantum-Darwinism-style redundant environmental records;
- observer-relative D1 finality under a declared access boundary.

## Setup

The model uses binary noisy readout channels. Each environment fragment has:

- readout reliability;
- pointer-coherence suppression factor;
- holder identity;
- independence class;
- branch id.

For a uniform binary pointer, the fragment information is:

```text
I(S;F) = 1 - H_2(error)
```

where `error = 1 - reliability`. A fragment counts toward raw `R_delta` only
when its information crosses the declared threshold. It counts toward D1
holder redundancy only when it is also inside the observer access boundary and
belongs to a distinct independence class.

## Witness Matrix

T62 contains four finite witnesses:

1. `redundant_accessible_control`: decoherence, total redundancy, and D1
   observer finality agree.
2. `decohered_not_darwinist`: weak scattering suppresses pointer coherence
   but no individual fragment crosses the information threshold.
3. `redundant_but_inaccessible`: environmental records are redundant, but the
   observer has no access window.
4. `raw_duplicate_boundary`: raw fragment count crosses threshold, but a
   correlated duplicate is not an independent D1 holder.

## Success Criteria

1. The model realizes all four witness classes with executable tests.
2. The result does not claim new quantum dynamics.
3. The result states when TaF adds content beyond decoherence and when it does
   not.
4. The result supplies a falsification condition for Q1 in measurement terms.

## Failure Criteria

1. Decoherence is treated as collapse.
2. Raw environmental redundancy is treated as automatically final for all
   observers.
3. The access boundary or independence partition is arbitrary and cannot be
   physically justified in a detector-level model.
4. The result claims that TaF explains noisy decoherence better than existing
   decoherence or Quantum Darwinism.

## Result

Implemented as T62 v0.1.

The strongest surviving claim is not a new measurement dynamics claim. T62
supports only an access-boundary discriminator:

```text
decohered != environmentally redundant != final for this observer
```

## Reproduction

```bash
python -m unittest tests.test_noisy_measurement_access_boundary -v
python -m models.run_t62
```
