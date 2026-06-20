# T88: Pati-Salam Typed Forgetting Crosswalk

## Route

Mathematical machinery / adoption elsewhere.

## Question

Does the verified GU Pati-Salam chain give TaF a clean typed-forgetting witness:
full Pati-Salam structure reconstructs the Standard-Model one-generation
hypercharge table, while the `B-L`-only projection fails because it forgets
`T3R`?

## Motivation

The GU verification establishes, within group-theory scope, that the standard
`SO(10) -> Pati-Salam -> SM` branching reproduces the 16-state one-generation
table. It also reports an ambiguity probe: using the `SU(4)` `U(1)` term alone
does not reproduce the paper's `n = 6Y` values. This is exactly the kind of
named-structure-loss boundary TaF's `LossKernel` and `TF1` track.

## Construction

- Build the Spin(10) chiral spinor weights `(+-1/2)^5` with even minus parity.
- Compute `B-L`, `T3L`, and `T3R`.
- Compare two maps:
  - full Pati-Salam: `Y = T3R + (B-L)/2`;
  - naive projection: `Y' = (B-L)/2`.
- Collapse each result to `(SU3, SU2_L dimension, n=6Y, dimension)` multiplets.
- Classify the lost structure as a `LossKernel` only if the full map succeeds
  and the projected map fails in the predicted way.

## Success Criteria

- The full Pati-Salam map exactly reproduces the six-row one-generation table.
- The `B-L`-only projection preserves total dimension `16` but does not match
  the table.
- The projected `n` set is `{-3, -1, 1, 3}` rather than
  `{-4, -3, 0, 1, 2, 6}`.
- The right-singlet rows are merged by the projection.
- The result is classified as a typed-forgetting witness, not a PO1 instance
  and not support for GU or TaF physics.

## Failure Criteria

- `B-L` alone reproduces the table.
- The full Pati-Salam map fails to reproduce the table.
- The failure can be repaired without restoring `T3R` or an equivalent
  right-isospin term.
- The report uses the result to upgrade Q1, H1, H7, spacetime reconstruction,
  GU physics, or TaF physics.

## Claim Impact

T88 can strengthen TF1 only narrowly: it supplies an external finite math
witness where named forgotten structure is necessary for preserving a
downstream invariant. It does not prove a TaF physics claim.

## Reproduction

```bash
python -m unittest tests.test_pati_salam_typed_forgetting_crosswalk -v
python -m models.run_t88
```
