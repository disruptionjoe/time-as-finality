# T110: Finite-Permutation Monotone Obstruction

## Route

Thermodynamic arrow of time.

## Question

Can H7 support a strict finality arrow inside a finite closed reversible
state space once all memory, sink, and return degrees of freedom are included?

## Motivation

T106 showed a concrete bounded-sink reversible compression witness where the
forward accounting curve is monotone only until the reversible return path is
included. The highest-value follow-up is the general finite obstruction:
closed finite reversible dynamics are permutations, and permutation orbits are
cycles.

## Success Criteria

- Formalize the finite permutation-orbit obstruction.
- Apply it to the closed T106 accounted-support cycle.
- Include a plateau control where nondecreasing is possible only because the
  score is constant.
- Exhaustively enumerate small finite cycles to check that strict
  nondecreasing assignments do not exist.
- Include an open-branch control showing where strict accounting can appear
  only after the closed reversible assumption is dropped.

## Failure Criteria

- Count only the forward branch of a reversible cycle.
- Exclude sink, memory, or return-path degrees of freedom while calling the
  model closed.
- Treat a constant score as a strict arrow.
- Use erasure, fresh blank capacity, coarse graining, or a hidden environment
  without declaring that H7 has become an open-system/resource-accounting
  claim.

## Claim Impact

If T110 holds, H7 cannot be read as a strict scalar monotone generated inside a
finite closed reversible system. H7 survives only as a conditional constructor
theorem or as an explicitly open-system/coarse-grained resource-accounting
claim.

## Reproduction

```bash
python -m unittest tests.test_finite_permutation_monotone_obstruction -v
python -m models.run_t110
```
