# T58: Gap-Phantom Equivalence Audit

## Target Claims

- T56 open question Q1: whether H0(G), with `G(U) = A(U) - F(U)`, is exactly the set of phantom incomparability witnesses from T51 and T52.
- C1 and D1-Field only inside the finite observer-colimit witness class already built by T51 and T52.

## Setup

Reuse the executable T51 and T52 analyses.

For each observer view:

```text
A(U) = non-reflexive event-finality/colimit order
F(U) = non-reflexive apparent observer order
G(U) = A(U) - F(U)
```

Compare `G(U)` with the model's independently reported phantom incomparability pairs:

```text
observer says: incomparable
colimit says: ordered
```

## Success Criteria

- T51 Observer A has empty `G(U)` and no phantom pair.
- T51 Observer B has exactly one gap pair, `(e1_A_locking, e3_composite_locking)`, matching its phantom pair.
- T52 Observer A has exactly one gap pair, `(e1_alpha_locking, e4_delta_locking)`, matching its phantom pair.
- T52 Observer B has exactly one gap pair, `(e1_alpha_locking, e3_gamma_locking)`, matching its phantom pair.
- All T51/T52 apparent orders are suborders of their ambient colimit orders.

## Failure Criteria

- Any T51/T52 `G(U)` contains a pair not independently classified as phantom.
- Any T51/T52 phantom pair is absent from `G(U)`.
- Any T51/T52 observer has a local apparent order pair absent from the ambient colimit order.

## Boundary / Control

The audit includes a hostile local-reversal control:

```text
A(U) = {a <= b}
F(U) = {b <= a}
```

The gap contains `(a,b)`, but this is not a phantom incomparability because the local observer did not see `a` and `b` as incomparable. The case is classified as an invalid extension boundary.

## Expected Result

`H0(G)` matches phantom incomparability witnesses for the tested T51/T52 well-formed extension cases, but the result is not promoted to an arbitrary-observer theorem. The equivalence requires `F(U) <= A(U)` as a suborder condition.

## Run Command

```bash
python -m pytest tests/test_gap_phantom_equivalence.py -v
python -m models.run_t58
```

## Dependencies

- T51 multi-observer apparent finality colimit
- T52 symmetric colimit theorem
- T56 gap-presheaf question

## Non-Claims

- Does not prove that `H0(G)` is complete for every possible observer assignment.
- Does not resolve T56 Q2 sheafification, T56 Q3 nerve cohomology, or T56 Q4 arrow-direction circularity.
- Does not promote T58 into a general sheaf theorem beyond the finite T51/T52 witness class.
