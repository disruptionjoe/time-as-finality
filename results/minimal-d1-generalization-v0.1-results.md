# Minimal D1 Generalization v0.1 Results

## Command

```bash
python -m models.run_t25
```

Focused tests:

```bash
python -m unittest tests.test_minimal_d1_generalization -v
```

## Verdict

T25 does not support jumping directly to full sheaf language or a full IPT
representation theorem.

The best-supported hypothesis is:

```text
H3: another finite local-to-global structure is required.
```

The smallest earned object is a finite graph-indexed D1 restriction system:

```text
local D1 profiles
+ observer sites
+ trusted transport edges
+ optional patch constraints
```

## Hypothesis Comparison

| Hypothesis | T25 status | Verdict |
| --- | --- | --- |
| H0: scalar D1 is sufficient | rejected for multiscale claims | retain only for fixed-observer or uniform cases |
| H1: vector D1 is sufficient | partially supported but insufficient | useful for observer-distribution snapshots |
| H2: field-valued D1 is required | partially supported | field-like data is required when transport or gluing matters |
| H3: another finite local-to-global structure is required | best supported | graph-indexed restriction system is smallest adequate object |
| H4: no canonical generalization is justified | not best supported | too pessimistic for current finite evidence |

## Theorem Ladder

| Theorem attempt | Reached | Result |
| --- | --- | --- |
| Scalar Recovery Theorem | yes | scalar D1 recovers under uniform/fixed-observer assumptions |
| Vector Sufficiency Theorem | yes | vector D1 suffices when profiles diverge but transport/gluing are trivial |
| Transport Necessity Theorem | yes | same vector can have different trust-path reachability |
| Gluing Obstruction Theorem | yes | locally satisfiable patches need not globalize |
| Morphism Theorem | yes, local only | one-site IPT factorization succeeds for quantum redundancy reduction |
| IPT Representation Theorem | no | deferred because current IPTs lack site maps and restriction-map commutation |

## Informative Failures

Scalar failure:

```text
stratified_access_delay
```

Scalar aggregates erase the difference between live local/lab finality and
institutional non-finality.

Vector failure:

```text
connected_same_vector
partitioned_same_vector
```

The observer-profile vector is identical, but transport reachability differs.

Gluing failure:

```text
contextual_gluing_obstruction
```

Each local patch is satisfiable, but no global assignment exists.

IPT representation failure:

```text
full_ipt_representation
```

The current IPT type preserves named invariants but does not yet carry site
maps or restriction-map commutation data. This is a real boundary, not a test
failure.

## Recommendation

Adopt the finite graph-indexed D1 restriction system as the next formal target.

Retain scalar D1 for fixed-observer and uniform cases. Use vector D1 when only
observer distribution matters. Use graph restriction data when transport or
gluing matters. Defer full sheaf semantics and full IPT representation until
the graph-indexed structure is stable.
