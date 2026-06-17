# Finality Direction Theorem Results

Result: T18 focused tests pass `6/6`.

## Model

Each state carries:

```text
D1 = (accessible support, holder redundancy, branch support, reversal cost)
```

A transformation is possible when no D1 dimension decreases.

## Search

The verifier checks:

```text
states = 402
transformations = 161202
strict finalization edges = 38205
impossible transformations = 122193
```

## Theorem Check

The theorem holds in the finite model:

```text
In a finite constructor model where admissible transformations are
D1-monotone, strict finalization induces an acyclic partial order; the reverse
of every strict finalization is impossible.
```

Checks:

| Check | Result |
| --- | --- |
| arrow graph acyclic | pass |
| strict finalization reverse impossible | pass |
| impossible transformations not closed under reversal | pass |
| arrow partial, not total | pass |

## Witnesses

Impossible reversal:

```text
s1-h0-b0-r1-k0 -> s0-h0-b0-r0-k0
```

Thermodynamic-divergence witness:

```text
s1-h0-b0-r1-k0 -> s1-h0-b0-r2-k0
```

D1 increases while the thermodynamic-cost proxy remains unchanged.

Incomparable pair:

```text
s1-h0-b0-r2-k0
s1-h0-b1-r1-k0
```

The arrow is a partial order, not a total ordering of all states.

## Verdict

T18 gives partial support to H7. It derives a finality-induced direction from
D1-monotone admissibility, while preserving the guardrails:

- it does not derive the thermodynamic arrow;
- it does not replace proper time;
- it does not claim physical systems necessarily instantiate the rule;
- it does not collapse finality into a total order.

## Reproduction

```bash
python -m unittest tests.test_finality_direction_theorem -v
python -m models.run_t18
```

Machine-readable output:

- [finality-direction-theorem-v0.1.json](finality-direction-theorem-v0.1.json)
