# T244: Kappa Value-Gap Real-Threshold Absorber

**Verdict (top): conditional (finite_witness + poly_decider).**

**Builds on:** [T224](T224-typed-loss-transport-test.md),
[T229](T229-kappa-rank2-second-absorber.md),
[T234](T234-kappa-genre-crossing-third-absorber.md), and
[T239](T239-kappa-noncycle-genre-quorum-intersection.md). **Code:**
`models/kappa_value_gap_transport.py`;
`tests/test_kappa_value_gap_transport.py`;
`results/kappa-value-gap/T244-results.json`.

## Verdict

T244 is a positive finite witness for a fifth kappa absorber:

```text
kappa_A in {0,1,2,3}
  -> predicted target rank
  -> native finite real-threshold value-gap rank
  -> kappa_B via the same T224 compute_kappa
```

The target-side native witness is not a parity-product, tournament-cycle, or
quorum-intersection witness. It is a finite collection of decision cells whose
real value gap is compared against a fixed real floor, then counted by independent
blocks. The integer rank is load-bearing: the native witness separates 0, 1, 2,
and 3.

## Scope

This is **not** a genre-agnostic theorem and not a continuum/value-as-physics
claim. The earned statement is narrower:

```text
The T224 kappa rank predicts a finite real-threshold value-gap absorber on the
tested rungs, using the same source-side T39 kappa builders and a fresh
target-side value-gap witness.
```

The A-side intentionally reuses the T39 CSP source builders. The target-side
native value-gap witness does not call `compute_kappa` and does not import
`d1_restriction_system`, `cap_theorem_bridge`, or the quorum module.

## Honesty Guards

- Shared-block adversarial cells are valid and count once by independent block.
- Malformed inputs are rejected for duplicate names, non-real deltas, invalid
  block indices, and deltas outside the fixture regime where native value
  iteration and the `nu` encoding agree.
- The harness can report non-pass: a naive raw-cell counter mispredicts the
  at-floor boundary.
- No physics, continuum, hardness, or new-law language is promoted.

## Next Object

The next kappa object is either a stronger non-finite or non-threshold native
absorber, or an integrator decision that this line is best stated as a
multi-absorber finite rank law rather than as a genre-agnostic theorem.
