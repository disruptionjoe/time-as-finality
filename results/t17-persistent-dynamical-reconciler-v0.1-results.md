# T17 Persistent Dynamical Reconciler Results

Result: T17 focused tests pass `8/8`; the current full branch suite passes
`91/91`.

## Mechanism

T17 uses a ten-bit local-update state:

```text
(env_a, env_b, sensor_a, sensor_b, memory_a, memory_b,
 written_a, written_b, compared, decision)
```

The written flags are necessary. Without them, a stored false value cannot be
distinguished from a memory cell that has never been written.

## Equal Case

For input `(1, 1)`, both memory cells store true and the comparator decision
is true.

```text
final state: (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
boundary: comparator, memory:A, memory:B
decision: true
profile A:   (1, 1, 1, 5)
profile B:   (1, 1, 1, 5)
profile A=B: (1, 1, 1, 5)
```

## Unequal Case

For input `(1, 0)`, the system stores one true record and one false record.
The comparator still activates and returns a false equality decision.

```text
final state: (1, 0, 1, 0, 1, 0, 1, 1, 1, 0)
boundary: comparator, memory:A, memory:B
decision: false
profile A:   (1, 1, 1, 5)
profile B:   (1, 1, 1, 5)
profile A=B: (1, 1, 1, 5)
```

This is the key correction over a truthy-memory toy model: false evidence is
still evidence.

## Sweep

The deterministic sweep evaluates the four possible environment inputs.

| Metric | Value |
| --- | ---: |
| cases | `4` |
| both-memory-records fraction | `1.0` |
| comparison fraction | `1.0` |
| true decision count | `2` |
| false decision count | `2` |

Every case generates the same internal access boundary:

```text
comparator, memory:A, memory:B
```

## No-Persistence Control

The control allows a pulse through the sensor layer but does not latch memory.
At the final state there are no internal records and no comparator decision.

```text
records_at_final_state: 0
decision_at_final_state: None
```

## Verdict

T17 supports a narrower and stronger D2 result than earlier observer-window
tests: a toy reconciler subsystem can be generated inside the local dynamics.

Limits:

- the subsystem architecture is still designed by the experimenter;
- the model has two records, not an open-ended record ecology;
- there is no phenomenal observer;
- there is no quantum, relativistic, or thermodynamic derivation.

## Reproduction

```bash
python -m unittest tests.test_t17_persistent_reconciler -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t17
```

Machine-readable output:

- [t17-persistent-dynamical-reconciler-v0.1.json](t17-persistent-dynamical-reconciler-v0.1.json)
