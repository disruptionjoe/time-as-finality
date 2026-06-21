# Technical Report: Accessible-Witness Gap Restriction v0.1

## Claim Under Test

T89 identified T19 as a unary accessible-witness gap instance sharing H0
failure shape with the T58 order-pair phantom-gap instance. The missing theorem
target was whether the T19 proposition-domain gap object actually restricts
like the T57 gap object.

## Result

T92 supports the restriction theorem with explicit boundaries.

For finite typed proposition-domain accessible-witness systems:

```text
G(U) = A(U) - F(U)
```

restricts contravariantly when:

1. ambient truth restricts;
2. auditability is monotone under patch inclusion;
3. proposition types are stable under restriction.

The T19 unary witness and a non-chain joint-witness control both satisfy these
conditions. Semantic relabeling and audit-monotonicity violation both break
gap restriction closure.

## Current Strongest Claim

The first-person/third-person finality gap has a finite degree-0
accessible-witness form with restriction closure for typed proposition-domain
witness systems.

This is a conditional theorem audit, not a consciousness claim and not a
general Cech/cohomology theorem.

## What This Improved

T92 prevents the T19/T58 bridge from staying vague. It shows that T19 can join
the T56-T58 H0 gap program under explicit hypotheses, while preserving the
distinction between section objects:

- T19 sections are unary propositions;
- T58 sections are order pairs.

The shared content is H0 failure shape plus restriction closure, not identity
of mathematical objects.

## What This Weakened Or Falsified

T92 weakens any broad phenomenal-bridge reading. The result fails if
`R_self_finality` can be semantically relabeled into `R_obs`, or if smaller
patches can audit propositions not auditable at larger patches.

The theorem therefore depends on typed propositions and monotone witness
availability. Without those, the accessible-witness gap is not licensed as a
gap-presheaf-style object.

## Falsification Condition

T92 fails if a well-typed nested proposition-domain witness satisfies ambient
restriction and audit monotonicity but has a larger-patch gap whose restriction
is not a smaller-patch gap.

## Claim Ledger Update

C1 should not be upgraded. It may be sharpened:

```text
The T19 first-person/third-person finality gap has a finite degree-0
accessible-witness form with restriction closure for typed proposition-domain
witness systems; it remains distinct from T58 order-pair phantom gaps.
```

## Open Blocker

T92 does not place `FIRST-PERSON-FINALITY` in a complexity class. It does not
show that T19 proposition gaps and T58 order-pair gaps are instances of one
identical presheaf. It only establishes a conditional finite restriction
theorem audit.

## Next Work

Generalize the proof sketch into a short formal lemma, then test whether T19
proposition gaps and T58 order-pair gaps share a common typed gap category or
only the same H0 failure shape.

## Reproduction

```bash
python -m unittest tests.test_accessible_witness_gap_restriction -v
python -m models.run_t92
```
