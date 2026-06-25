# Dual-Record Opportunity Fixture v0.1 Results

Result: focused tests pass `5/5`.

Machine-readable output:

- [dual-record-opportunity-fixture-v0.1.json](dual-record-opportunity-fixture-v0.1.json)

## Status

This fixture implements the comparator frozen in Temporal Issuance E093.

It compares:

```text
A   single-record search
B0  limited fixed-latent opportunity search
B1  exact fixed-latent absorber panel
C   growing-adjacency opportunity search
```

## Frozen Landscape

```text
states: 0..10
start: 0
target: 10
budget: 8 proposal attempts
critical edge: 2 -> 7
```

The base graph traps monotone search at state `2`.

## Result Summary

```text
A  final state 2, target not reached
B0 final state 2, target not reached
C  generates 2 -> 7 and reaches target 10
B1 exposes latent 2 -> 7 and also reaches target 10
```

The bounded positive result is real relative to B0:

```text
C beats A and B0 under equal budget.
```

The source-side interpretation is absorbed by B1:

```text
B1 reproduces C when the critical edge is supplied as a fixed latent edge with
a matching access trigger.
```

## Effect Verdict

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

## What Survives

The dual-record idea survives as useful record-regime architecture:

```text
stable record: accepted path and provenance
opportunity record: failed probes, stuckness, latent exposure, generated edge
```

It is a good finite model for local-minimum escape and for separating stable
records from opportunity-edge records.

## What Does Not Survive

The fixture does not establish source-side issuance.

Reason:

```text
An exact fixed-latent graph plus matching access schedule reproduces the
growing-adjacency result.
```

## Guardrail

```text
Finite comparator only: C beating A/B0 is a bounded residue relative to the
declared limited comparator, not source issuance. B1 tests the exact
fixed-latent edge absorber.
```

## Reproduction

```bash
python -m unittest tests.test_dual_record_opportunity_fixture -v
python -m models.run_dual_record_opportunity_fixture --output results/dual-record-opportunity-fixture-v0.1.json
```
