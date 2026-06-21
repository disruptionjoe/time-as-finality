# T159: T54 Interval-Jackknife Screen

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T54: Finite Finality Descent Theorem](T54-finite-finality-descent-theorem.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T157: T54 Ordering-Fraction Bridge](T157-t54-ordering-fraction-bridge.md)

## Question

Does the T157 six-event T54 colimit remain credible as more than a calibration
control after a stricter interval-abundance and single-deletion robustness
screen?

## Motivation

T157 removed one narrow blocker: a genuine T54 canonical quotient-union colimit
can reach T126 scale and match the declared flat 1+1 ordering-fraction band.
That result is still easy to overread, because a single hand-built six-event
sample can match an aggregate ordering fraction while depending on a fragile
event configuration.

T159 adds a stricter finite screen before any robust S1 language is allowed.

## Setup

Pipeline:

```text
T54 ObserverDescentDatum
  -> T54 canonical quotient-union completion
  -> T126 causal-set screen
  -> T156 ordering-fraction target
  -> parent interval-support screen
  -> single-event deletion jackknife screen
```

Declared target:

```text
ordering fraction = 1/2 +/- 1/10
maximum parent Alexandrov-interval interior size = 1
required deletion pass rate = 1
```

The deletion screen is intentionally hostile. It is a finite fragility test,
not a continuum causal-set theorem.

## Cases

1. `t157_flat_1p1_t54_colimit`
   - Expected to pass T54, T126, T156, and parent interval support.
   - Expected to fail single-deletion stability if any deletion leaves the
     declared ordering-fraction band.
2. `t157_product_grid_2x3_t54_colimit`
   - Expected to fail before robust interpretation through ordering fraction
     and interval-support excess.
3. `t157_chain_6_t54_colimit`
   - Expected to block at T126 before interval interpretation.

## Success Criteria

- The flat T157 parent still passes the prior T126/T156 screens.
- The product-grid control remains demoted.
- The chain control remains blocked at T126.
- A deletion-instability in the flat control demotes it to calibration-only.
- S1 is not upgraded.

## Failure Criteria

T159 fails if:

- deletion suborders are computed from a different relation than the
  T54/T126/T156 relation;
- the product-grid or chain controls stop blocking the claimed interpretation;
- a jackknife failure is described as a continuum no-go theorem;
- a jackknife pass is described as spacetime evidence.

## Claim Impact

S1 remains `open_formal_target`.

T159 weakens the positive reading of T157:

```text
The T157 flat T54 control is calibration-only unless it also survives
interval-abundance and single-deletion robustness screens.
```

The expected result is a demotion rather than an upgrade. The T157 construction
can remain useful as a calibration fixture while failing as a robust finite
spacetime-reconstruction witness.

## Reproduction

```bash
python -m unittest tests.test_t54_interval_jackknife_screen -v
python -m models.run_t159
```
