# Persistent Dynamical Reconciler

## Abstract

T17 builds a finite local-update model where a small reconciler subsystem
stores records, exposes them through an internally generated boundary, and
compares them without selecting a terminal observer window by hand.

The result is positive in a bounded toy setting. The model stores both true
and false records, compares two stored records, produces equal and unequal
decisions, and loses the decision when persistence is removed.

This strengthens the project's observer model, but only narrowly. It does not
model consciousness, derive a full physical observer, or replace the earlier
record-graph formalism.

## 1. Motivation

Earlier labs often asked what a specified observer, access set, or terminal
evaluation window could see. That was useful, but it left a structural
weakness:

> The observer boundary was often supplied from outside the dynamics.

T17 tests a more demanding object: a finite system whose record storage,
record access, and reconciliation arise inside the update rule.

## 2. Model

The model state is:

```text
(env_a, env_b, sensor_a, sensor_b, memory_a, memory_b,
 written_a, written_b, compared, decision)
```

The local update has five stages:

1. sensors copy their coupled environment cells;
2. memory cells latch the first sensed value;
3. written flags preserve the distinction between stored false and unwritten;
4. the comparator activates after both memory cells have written;
5. the decision bit records whether the two stored values agree.

The generated access boundary is the set of internal holders that become
causally wired into persistent memory or comparison:

```text
memory:A
memory:B
comparator
```

## 3. Why Written Flags Matter

Without written flags, a memory bit equal to `0` is ambiguous. It could mean:

- no record has been written; or
- a false-valued record has been written.

That ambiguity is not a minor implementation detail. It would make unequal
cases look like missing evidence. T17 therefore treats storage status and
stored value as separate state components.

## 4. Results

For input `(1, 1)`, the final state is:

```text
(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
```

The generated boundary is:

```text
comparator, memory:A, memory:B
```

The equality decision is `true`.

For input `(1, 0)`, the final state is:

```text
(1, 0, 1, 0, 1, 0, 1, 1, 1, 0)
```

The boundary is the same, but the equality decision is `false`.

Across all four input cases:

| Metric | Value |
| --- | ---: |
| both-memory-records fraction | `1.0` |
| comparison fraction | `1.0` |
| true decisions | `2` |
| false decisions | `2` |

## 5. Control

The no-persistence control allows sensor pulses but does not latch memory. At
the final state it has:

```text
records_at_final_state = 0
decision_at_final_state = None
```

This shows that the result depends on persistent internal record storage, not
on merely reading a transient signal.

## 6. Claim Verdict

T17 strengthens [D2](claims/D2-observer-as-record-bearing-system.md). A
reconciler can be represented as an internal dynamical subsystem rather than
only as an externally selected access window.

It also modestly strengthens [D1](claims/D1-physical-finality-definition.md):
the finality profile can be computed over internally generated records rather
than only over hand-authored record tokens.

The result also supports [C2](claims/C2-typed-compositional-finality.md) by
keeping stored value, write status, access boundary, finality profile, and
decision as distinct typed components.

Limits:

- The architecture is designed, not discovered by an evolutionary search.
- The system has only two memory records and one comparator.
- It does not include record degradation, erasure cost, copying, conflict
  repair, or dynamic boundary growth.
- It does not model consciousness or phenomenal time.

## 7. Next Work

The next useful extension is a persistent record ecology: a generated local
network where records can be copied, overwritten, degraded, contradicted, and
reconciled under explicit resource or channel constraints.

That would test whether T17's internal reconciler still works when storage is
not a perfect latch and when the access boundary is not fixed by a two-record
architecture.

## 8. Reproduction

```bash
python -m unittest tests.test_t17_persistent_reconciler -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t17
```

Machine-readable output:

- [results/t17-persistent-dynamical-reconciler-v0.1.json](results/t17-persistent-dynamical-reconciler-v0.1.json)

Focused result note:

- [results/t17-persistent-dynamical-reconciler-v0.1-results.md](results/t17-persistent-dynamical-reconciler-v0.1-results.md)
