# T110 Results: Finite-Permutation Monotone Obstruction

## Strongest claim

In any finite closed reversible system represented by a permutation, a scalar finality score that is nondecreasing along every physical step is constant on each orbit. Strict H7-style increase cannot be generated inside the closed bounded state space.

## Closed T106 cycle

- Score sequence: `[0, 1, 3, 4, 4, 5, 7, 5, 4, 4, 3, 1, 0]`
- Edge deltas: `[1, 2, 1, 0, 1, 2, -2, -1, 0, -1, -2, -1, 0]`
- Nondecreasing on all edges: `False`
- Has strict increase: `True`
- Has decrease: `True`
- Strict nondecreasing possible: `False`

the closed reversible score is not monotone; any strict increase is paid back by a decrease on the same finite orbit

## Plateau control

- Nondecreasing on all edges: `True`
- Constant on each orbit: `True`
- Verdict: nondecreasing is possible only because the score is constant on each closed permutation orbit

## Exhaustive finite-cycle check

| Cycle length | Assignments | Nondecreasing | Constant | Strict without decrease | Theorem holds |
| --- | ---: | ---: | ---: | ---: | --- |
| 2 | 9 | 3 | 3 | 0 | True |
| 3 | 27 | 3 | 3 | 0 | True |
| 4 | 81 | 3 | 3 | 0 | True |
| 5 | 243 | 3 | 3 | 0 | True |
| 6 | 729 | 3 | 3 | 0 | True |
| 7 | 2187 | 3 | 3 | 0 | True |

## Open-branch control

- Score sequence: `[0, 1, 3, 4, 4, 5, 7]`
- Nondecreasing: `True`
- Strict increases: `5`
- Closed reversible system: `False`

strict monotone accounting is possible on the open forward branch, but this is not a closed reversible system

## What this improved

T110 generalizes T106 from one bounded-sink witness to a finite permutation obstruction. It identifies exactly which assumption must be broken before an H7 arrow can be physical: closed finite reversibility, scalar/antisymmetric monotone scoring, or inclusion of all memory and sink degrees of freedom.

## What this weakened

H7 is weakened as a thermodynamic-arrow claim. The finite constructor theorem survives only as a conditional order on admissible transformations or as open-system/coarse-grained resource accounting, not as a strict scalar monotone on closed bounded reversible dynamics.

## Falsification condition

T110 is falsified only by a finite closed reversible model with a strict D1-relevant scalar monotone on every transition edge and no excluded environment, erasure, fresh blank capacity, postselected branch, non-invertible quotient, or time-dependent scoring rule. Otherwise the model has left the theorem's assumptions.

## H7 update

Add T110 to H7: finite closed reversible dynamics cannot carry a strict scalar finality monotone. H7 must explicitly declare the open-system, coarse-graining, erasure, resource, or constructor restriction that supplies direction.

## Claim ledger update

H7 remains partially supported only as a conditional constructor or open-system resource-accounting claim. T110 proves the finite permutation obstruction: nondecreasing scalar finality on a closed reversible orbit is constant, so any strict increase on the forward branch requires omitted return degrees of freedom or a non-reversible/coarse-grained boundary.

## Open blocker

The project still lacks a physically grounded open-system H7 model that adds thermodynamic or coarse-grained direction without merely renaming standard entropy export.

## Recommended next

Either demote H7 to a constructor/resource-accounting lemma in claim-facing prose, or build an explicit open Markov/coarse-grained record model and compare its arrow to standard entropy production.
