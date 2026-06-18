# D1 Restriction System v0.1 Results

## Command

```bash
python -m models.run_t26
```

Focused tests:

```bash
python -m unittest tests.test_d1_restriction_system -v
```

## Verdict

T26 supports formalizing the T25 recommendation as a finite mathematical object:

```text
D1RestrictionSystem
```

Best-supported hypothesis:

```text
H1: finite graph-indexed D1 restriction system is sufficient.
```

## Definition Tested

```text
D1RestrictionSystem =
  finite observer sites
  one local D1 profile per site
  one proposition value per site
  trusted transport edges
  optional overlap tests
  optional finite patch constraints
  scalar and vector projection maps
  compatibility and global-section predicates
```

## Theorem Ladder

| Theorem attempt | Reached | Result |
| --- | --- | --- |
| Minimal Axiom Sufficiency Theorem | yes | all reused T25 systems validate |
| Scalar Recovery Theorem | yes | scalar D1 recovers in the uniform case |
| Vector Recovery Theorem | yes | vector D1 is faithful in the trusted-chain case |
| Graph Necessity Theorem | yes | same vector can have different trusted reachability |
| Gluing Obstruction Theorem | yes | local patch witnesses need not globalize |
| Restriction Morphism Theorem | yes | positive and failed morphisms are distinguished |
| IPT Representation Theorem | no | deferred because current IPT objects lack site maps and restriction commutation |

## Morphism Results

Positive case:

```text
trusted_transport_relabeling
```

This preserves local D1 profiles, trusted reachability, and obstruction status.

Failed case:

```text
connected_to_partitioned_transport
```

This is blocked by:

```text
trust_path_not_preserved
```

## Informative Failures

- Scalar D1 is not generally faithful as a global object.
- Vector D1 is not generally faithful when transport matters.
- Local compatibility does not guarantee a global section.
- T23 IPT does not yet contain the site-map and restriction-map data required
  for full D1 restriction representation.

## Recommendation

Adopt `D1RestrictionSystem` as the repo's next formal D1 extension.

Retain scalar D1 as a fixed-site or uniform projection. Retain vector D1 as an
observer-distribution projection. Use graph and patch data for transport and
gluing claims. Defer full sheaf and full IPT representation claims until
restriction-morphism composition is tested.
