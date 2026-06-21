# T157: T54 Ordering-Fraction Bridge

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T54: Finite Finality Descent Theorem](T54-finite-finality-descent-theorem.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)

## Question

Can a genuine T54 canonical quotient-union colimit, rather than a synthetic
T126/T156 control, reach the T126 scale floor and match the declared flat 1+1
ordering-fraction band?

## Motivation

T156 left a precise blocker:

```text
No actual T54/T58 finality colimit both reaches T126 scale and matches a
named causal-set diagnostic.
```

T157 attacks only the scale/order-fraction part of that blocker. It constructs
T54 descent datums, completes them with the T54 quotient-union algorithm, and
then applies the existing T126 and T156 gates. It does not import an order
directly into the causal-set screen.

## Setup

Pipeline:

```text
T54 ObserverDescentDatum
  -> T54 canonical quotient-union completion
  -> T126 FinalityColimitCausetDatum
  -> T156 flat 1+1 ordering-fraction target
```

Cases:

1. `t157_flat_1p1_t54_colimit`
   - Six-event, two-observer T54 datum.
   - Record dependencies encode the same strict order as the T156 flat 1+1
     deterministic control.
   - Expected to pass T126 and land at ordering fraction `7/15`.

2. `t157_product_grid_2x3_t54_colimit`
   - T54 version of the T156 over-ordered product-grid control.
   - Expected to pass T126 but fail the flat 1+1 ordering-fraction band.

3. `t157_chain_6_t54_colimit`
   - T54 canonical six-event chain.
   - Expected to be rejected by T126 before target interpretation.

## Success Criteria

- The flat candidate is a T54 canonical completion.
- The completed relation exactly matches the audited T156 flat control.
- The flat candidate reaches T126 and lands inside `1/2 +/- 1/10`.
- The product-grid control remains over-ordered after T54 completion.
- The chain control blocks at T126.
- S1 is not upgraded.

## Failure Criteria

T157 fails if:

- the T54 completion does not reproduce the strict relation sent to T126/T156;
- the flat candidate is synthetic rather than a T54 descent completion;
- the product-grid or chain controls stop blocking the claimed interpretation;
- the result is described as dimension evidence, sprinkling evidence, a
  faithful embedding, a Lorentzian metric reconstruction, or a spacetime
  derivation.

## Claim Impact

S1 remains `open_formal_target`.

T157 removes the immediate scale/order-fraction blocker left by T156:

```text
A constructed six-event T54 canonical quotient-union colimit can reach T126
and match the declared flat 1+1 ordering-fraction band.
```

This is still only a finite control. The live blocker moves to stronger
diagnostics: interval abundance, locality, sprinkling behavior, faithful
embedding, covariance, continuum limit, and Lorentzian metric reconstruction.

## Reproduction

```bash
python -m unittest tests.test_t54_ordering_fraction_bridge -v
python -m models.run_t157
```
