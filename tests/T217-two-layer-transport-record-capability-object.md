# T217: Two-Layer Transport / Record Capability Object

## Target Claims

- T215 fixed-network record-finality split
- T216 absorber audit
- Capability Projection typing discipline

## Origin

The latest run shows that transport and record-finality capabilities must not
be collapsed into one scalar.

## Formal Target

Type the two-layer capability object:

```text
K = K_flow x K_record
Cap(Y) = (C_flow(D,q), record_reconstructable(policy))
```

with native comparison:

```text
R_K = equality or task-threshold comparison coordinatewise.
```

## Setup / Fixtures

Use:

```text
same network
different record policies
```

from T215.

## Positive Control

The record coordinate distinguishes append-only from overwrite policies even
when `C_flow` is fixed.

## Negative Control

If the task asks only for transport latency, the record coordinate is out of
scope and must not be smuggled in.

## Absorber Pass

The product object is audit discipline, not proof of a new law. Each coordinate
must grant its native absorber.

## Results

The two-layer object prevents the previous mistake pattern:

```text
do not infer record finality from transport timing alone;
do not treat transport absorption as record-finality absorption.
```

## Verdict: narrowed

Promising as a typed audit object, narrowed because each coordinate is
absorber-owned until a same-native-state residue is found.

## Falsification Conditions

Demote if future witnesses choose product coordinates after seeing the split
instead of declaring the task first.

## Next Step

T218 packages the reviewer-safe statement.
