# Invariant-Preserving Transformations v0.1 Results

## Command

```bash
python -m models.run_t23
```

Focused tests:

```bash
python -m unittest tests.test_invariant_preserving_transformations -v
```

## Verdict

T23 gives the project a typed invariant-transport kernel, but not a finished
independent theory.

| Criterion | Result |
| --- | --- |
| Typed IPT definition exists | pass |
| Same interface expresses three domains | pass |
| Composition law executable | pass |
| Obstruction condition executable | pass |
| Relationship taxonomy has all four levels | pass |
| Equivalence claim avoided | pass |
| Mathematical independence | proto-independent |

## Positive Cases

| Transformation | Class | Preserved invariants | Allowed losses |
| --- | --- | --- | --- |
| observer_access_restriction | reduction | pointer_basis, system_record_correlation | environment_r_delta_total, inaccessible_records, global_state_amplitudes |
| consensus_record_quorum_safety_transfer | homology | holder_count, quorum_threshold, quorum_intersection_safety, conflict_exclusion | protocol_rounds, engineered_messages, byzantine_intent |
| quantum_measurement_to_reduction_schema | reduction | pointer_basis, holder_redundancy, accessible_support, observer_access_indexed | unitary_history, global_amplitudes, decoherence_timeline, branch_support_detail |

## Obstruction Case

The weak-quorum boundary triggers a named obstruction:

```text
weak_quorum: n = 4, q = 2, so 2q > n is false
```

The model reports that `quorum_intersection_safety` is not preserved across
the attempted boundary transformation.

## Composition Checks

The positive composition:

```text
observer_access_restriction
  -> quantum_measurement_to_reduction_schema
```

preserves the requested invariant:

```text
pointer_basis = computational_z
```

The obstruction composition:

```text
consensus_record_quorum_safety_transfer
  -> record_safety_to_weak_quorum_boundary
```

does not preserve:

```text
quorum_intersection_safety
```

because the weak-quorum obstruction is triggered.

## Repo Recommendation

IPT is **proto-independent**. The same typed interface now expresses observer
access restriction, consensus-record theorem transfer, and quantum redundancy
extraction, and the finite composition theorem is executable.

It should remain inside Time as Finality for now. A separate repository becomes
justified only after IPT has a stronger representation theorem and at least one
domain not inherited from the existing TaF test suite.
