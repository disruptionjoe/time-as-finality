# T35 Results: Projection-Obstruction Discovery Engine

Generated from `run_t35_discovery()`.

## Summary

T35 turns PO1 into a bounded finite exploration engine over generated
restriction-system projections.

Best supported hypothesis:

```text
H2 with H3 caution
```

The engine is generative inside the finite search space, but many generated
candidates are redundant. The result supports using T35 as a triage tool for
human mathematical investigation, not as theorem discovery.

## Counts

| Quantity | Count |
| --- | --- |
| Generated finite systems | 18 |
| Projection candidates | 172 |
| Positive PO1 candidates | 9 |
| Boundary non-definable candidates | 90 |
| Lossy non-obstructing candidates | 12 |
| Obstruction-removed candidates | 12 |
| Shared-obstruction candidates | 10 |
| Trivial local-failure candidates | 18 |
| Outside-PO1 candidates | 21 |

## Highest-Interest Generated Witness

The highest-interest generated witness is a four-patch positive PO1 candidate:

```text
a = b
b = c
c = d
a != d
```

This restricted system is locally satisfiable patch by patch but globally
inconsistent. The reducer reports all four patches are necessary for the
obstruction.

Representative candidate IDs:

```text
cand_052
cand_080
cand_164
```

## Rediscovery

The engine also rediscovers at least one prior PO1 signature from the T27-T34
comparison set. This supports H1: the framework can recover familiar PO1
patterns without domain-specific hints.

## Boundary and Counterexample Generation

T35 generated:

| Class | Witness type |
| --- | --- |
| boundary non-definable | missing source sites in a partial site map |
| lossy non-obstructing | profile loss into a globally satisfiable target |
| obstruction removed | obstructed richer source projected to clean endpoint |
| shared obstruction | richer and restricted systems both obstructed |
| trivial local failure | target fails locally rather than by gluing |

These are useful because they show the engine does not only search for
positives. It also generates negative and boundary controls.

## Recommendation

PO1 should remain `partially_supported`, with a new capability note:

```text
The finite framework has bounded generative value.
```

The next hostile test should be blinded. A future Arrow run should first encode
candidate finite systems, run the T35 classifier, and record the structural
prediction before any domain interpretation is used.

## Guardrails

- T35 does not claim automated theorem discovery.
- T35 generated candidates are mathematical prompts for human analysis.
- T35 does not use machine learning or domain heuristics.
- Generated finite structures do not by themselves prove scientific claims.
