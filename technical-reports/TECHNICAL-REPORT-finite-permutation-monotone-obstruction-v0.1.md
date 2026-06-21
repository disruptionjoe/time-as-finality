# Technical Report: Finite-Permutation Monotone Obstruction v0.1

## Claim Under Test

H7 says finality structure can induce an observer-relative temporal direction
when admissible transformations are monotone in D1 finality. T18 proves this
as a conditional constructor theorem. T80, T82, T84, and T106 weaken the
physical-arrow reading by showing that reversible local dynamics, persistent
memory, cyclic memory, and bounded reversible compression do not by themselves
produce a strict finality monotone after all relevant degrees of freedom are
included.

T110 asks for the general finite obstruction behind T106.

## Result

Let a finite closed reversible system be represented by a permutation
`p: X -> X`. Every orbit of `p` is a finite cycle:

```text
x0 -> x1 -> ... -> x(k-1) -> x0
```

Let `F: X -> R` be a scalar finality score. If `F` is nondecreasing along every
transition edge, then:

```text
F(x0) <= F(x1) <= ... <= F(x(k-1)) <= F(x0)
```

Therefore all inequalities are equalities. `F` is constant on that orbit. The
same argument applies orbit-by-orbit to any finite permutation.

So a strict scalar H7-style finality monotone cannot live inside a finite
closed reversible state space. A strict arrow requires at least one assumption
to change: openness, erasure, fresh blank capacity, non-invertible coarse
graining, postselection, excluded environment, time-dependent scoring, or a
different non-scalar structure with its own theorem.

## Executable Audit

The model applies the theorem to the T106 closed accounted-support cycle:

```text
0, 1, 3, 4, 4, 5, 7, 5, 4, 4, 3, 1, 0
```

The forward branch has strict increases, but the closed cycle has decreases.
The plateau control is nondecreasing only because it is constant. Exhaustive
cycle enumeration for lengths 2 through 7 over three score values finds:

- nondecreasing assignments exactly equal constant assignments;
- zero strict nondecreasing assignments;
- every strict increase is accompanied by a decrease elsewhere on the same
  cycle.

## Current Strongest Claim

In any finite closed reversible system represented by a permutation, a scalar
finality score that is nondecreasing along every physical step is constant on
each orbit. Strict H7-style increase cannot be generated inside the closed
bounded state space.

## What This Improved

T110 generalizes T106 from one bounded-sink witness to a finite theorem-level
obstruction. It identifies exactly what a future H7 model must declare before
claiming a physical arrow: an open boundary, an irreversible/coarse-grained
projection, an explicit resource sink, a constructor restriction, or a
non-scalar structure with new hypotheses.

## What This Weakened Or Falsified

This does not falsify T18. T18 remains a conditional theorem: if admissible
transformations are D1-monotone, strict finalization induces a direction.

T110 weakens the physical-arrow reading of H7. Closed bounded reversible
dynamics cannot supply a strict scalar finality monotone. The surviving H7
content is open-system/resource accounting or a stipulated admissibility
relation, not a new derivation of the thermodynamic arrow.

## Falsification Condition

T110 is falsified only by a finite closed reversible model with a strict
D1-relevant scalar monotone on every transition edge and no excluded
environment, erasure, fresh blank capacity, postselected branch, non-invertible
quotient, or time-dependent scoring rule. Otherwise the model has left the
theorem's assumptions.

## Claim Ledger Update

Add T110 to H7:

```text
H7 remains partially supported only as a conditional constructor or open-system
resource-accounting claim. T110 proves the finite permutation obstruction:
nondecreasing scalar finality on a closed reversible orbit is constant, so any
strict increase on the forward branch requires omitted return degrees of
freedom or a non-reversible/coarse-grained boundary.
```

## Open Blocker

The project still lacks a physically grounded open-system H7 model that adds
thermodynamic or coarse-grained direction without merely renaming standard
entropy export.

## Next Work

Either demote H7 to a constructor/resource-accounting lemma in claim-facing
prose, or build an explicit open Markov/coarse-grained record model and compare
its arrow to standard entropy production.

## Reproduction

```bash
python -m unittest tests.test_finite_permutation_monotone_obstruction -v
python -m models.run_t110
```
