# Spacetime Aggregation Toy Model Results

Result: T16 focused tests pass `6/6`; the current full branch suite passes
`29/29`.

## Model

Each observer-local finality domain is a finite partial order:

```text
domain = (events, local finality order)
```

Aggregation checks:

1. local domains are acyclic;
2. restrictions agree on shared overlaps;
3. the union of local orders remains acyclic.

If all checks pass, the output is a global partial order. If a check fails,
the output is an obstruction witness.

## Positive Case

Two domains glue:

```text
left-diamond:  a < b < c
right-diamond: b < c < d
```

Their shared overlap is `{b, c}`, and both agree that `b < c`.

The global order is:

```text
a < b < c < d
```

## Overlap Obstruction

Two domains disagree on their shared events:

```text
observer-left:  a < b
observer-right: b < a
```

The model reports:

```text
kind: overlap_disagreement
events: a, b
witness_edges: a < b, b < a
```

## Global Cycle Obstruction

Three locally valid domains can still fail globally:

```text
ab-domain: a < b
bc-domain: b < c
ca-domain: c < a
```

No pairwise overlap contains enough structure to detect the problem, but the
union is cyclic. The model reports:

```text
kind: global_cycle
witness_edges: a < b, b < c, c < a
```

## Partial Structure

The model also accepts non-total global structures:

```text
left-chain:  a < b
right-chain: c < d
```

The global result keeps `a` and `c` incomparable. This preserves the project's
no-universal-present guardrail.

## Verdict

T16 gives S1 its first executable formal target: spacetime aggregation means
gluing observer-local finality domains into a global compatibility structure
when possible, and reporting explicit obstructions when not.

Limits:

- The output is only a finite partial order.
- There is no metric, manifold, curvature, or Lorentzian signature.
- Event identity on overlaps is assumed by labels rather than derived.
- This is not a derivation of spacetime.

## Reproduction

```bash
python -m unittest tests.test_spacetime_aggregation -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t16
```

Machine-readable output:

- [spacetime-aggregation-v0.1.json](spacetime-aggregation-v0.1.json)
