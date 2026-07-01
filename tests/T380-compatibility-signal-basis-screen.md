# T380: Compatibility Signal-Basis Screen

## Target Claims

R1, S1, D1, PO1, and the T379 open edge:

```text
Is the primitive c=1 two-channel compatibility-signal basis forced by
compatibility consistency, or is it still an imported lightcone axiom?
```

The target is a boundary result, not a full physical derivation.

## Setup

Work in a finite 1+1 compatibility module with lineage coordinates:

```text
left
right
```

Ask for a symmetric bilinear interval form:

```text
q(left, right) = a*left^2 + 2*b*left*right + c*right^2
```

The primitive signal-channel constraint is:

```text
q(channel) = 0
```

The main candidate is the T379 basis:

```text
left_signal  = (1, 0)
right_signal = (0, 1)
```

Controls:

- one null channel only
- two collinear channels
- three noncollinear primitive null channels
- an extra channel collinear with an existing primitive channel
- reciprocal vs nonreciprocal observer scaling

## Success Criteria

- Two independent null channels force the product interval up to scale.
- The normalized forced form is:

```text
q(left, right) = left * right
```

- Rest rendering gives left/right signal speeds `+1` and `-1`.
- Reciprocal scaling preserves the product interval.
- Nonreciprocal scaling fails to preserve it.
- One-channel and collinear controls do not force the relativistic basis.
- Three noncollinear primitive null channels overconstrain a 1+1 nondegenerate
  interval form.
- The forced form matches the generated T379 substrate intervals.

## Failure Criteria

- The product interval is inserted rather than solved from null constraints.
- A single compatibility direction is treated as enough.
- Three noncollinear primitive null channels are allowed in one 1+1
  nondegenerate interval form.
- The result claims compatibility alone derives the two-channel null basis.

## Known Constraints

This screen assumes:

- a 1+1 compatibility module,
- a symmetric bilinear interval,
- primitive signal channels are null,
- two independent primitive signal directions are available.

Those assumptions are not yet derived. The result only shows what follows once
they are granted.

## Contribution Needed

The next version should attack the imported object directly:

```text
derive or independently motivate the existence of exactly two independent
primitive null compatibility-signal directions.
```
