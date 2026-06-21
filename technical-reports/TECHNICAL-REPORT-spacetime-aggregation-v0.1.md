# Spacetime Aggregation Toy Model

## Abstract

T16 gives the S1 open formal target its first executable model. It treats
observer-local finality domains as finite partial orders and asks whether
they can be glued into one global compatibility structure.

The result is positive but narrow. Compatible local domains glue into a
global partial order. Incompatible domains produce explicit obstruction
witnesses. The model also preserves incomparability, so successful gluing
does not imply a universal total order.

This is not a derivation of spacetime. It is a minimal formal target for what
"spacetime from finality aggregation" would have to mean before stronger
geometry is attempted.

## 1. Motivation

The 42-persona sprint identified the highest-upside speculative signal:

> classical spacetime may be the output of finality aggregation, not the arena
> in which finality occurs.

That sentence is too strong unless it is turned into a testable construction.
T16 supplies the smallest construction:

```text
observer-local finality domains
  -> overlap restriction checks
  -> global partial order, or obstruction
```

## 2. Model

A local finality domain is:

```text
(domain_id, events, local_order)
```

The local order must be acyclic. For any two domains with at least two shared
events, their induced order on the overlap must match exactly.

Aggregation succeeds if the union of all local orders is also acyclic.

The global output is:

```text
(events, transitive_closure(local_orders), cover_domains)
```

This is the model's minimal "spacetime-like" object: a shared partial order
compatible with the local domains.

## 3. Positive Case

The compatible-chain scenario has:

```text
left-diamond:  a < b < c
right-diamond: b < c < d
```

The overlap is `{b, c}` and both domains agree on `b < c`. The aggregate is:

```text
a < b < c < d
```

## 4. Obstruction Cases

The overlap-disagreement scenario has two domains that both see `a` and `b`,
but order them differently:

```text
a < b
b < a
```

The model rejects the gluing and returns the conflicting edges as the witness.

The global-cycle scenario has three individually valid local domains:

```text
a < b
b < c
c < a
```

Pairwise overlaps are too small to reveal a restriction disagreement, but the
union is cyclic. The model rejects the aggregate and returns the cycle.

## 5. Claim Verdict

T16 strengthens [S1](claims/S1-spacetime-consensus-envelope.md) only in the
sense that S1 now has an executable formal target. It does not promote S1 to
a physical derivation.

The result also supports [R1](claims/R1-relativity-no-global-commit-order.md)
because successful aggregation can still preserve incomparable pairs. A
global compatibility structure need not be a global total order.

## 6. Limits

- Event identity on overlaps is assumed by shared labels.
- Domains are finite partial orders, not manifolds.
- There is no metric, Lorentzian signature, curvature, or field dynamics.
- The construction is closer to a finite sheaf/gluing sanity check than to
  physics.

## 7. Next Work

The next step is to replace shared labels with explicit restriction maps
between local causal diamonds, then compute whether nontrivial obstruction
classes correspond to physically interpretable finality conflicts.

That connects T16 directly to [T13](tests/T13-finality-sheaf-cohomology.md).

## 8. Reproduction

```bash
python -m unittest tests.test_spacetime_aggregation -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t16
```

Machine-readable output:

- [results/spacetime-aggregation-v0.1.json](results/spacetime-aggregation-v0.1.json)

Focused result note:

- [results/spacetime-aggregation-v0.1-results.md](results/spacetime-aggregation-v0.1-results.md)
