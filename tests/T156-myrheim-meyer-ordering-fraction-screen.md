# T156: Myrheim-Meyer Ordering-Fraction Screen

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T154: T54/T58-to-T126 Bridge](T154-t54-t58-t126-bridge.md)

## Question

If a scale-cleared finite finality colimit survives T126, does it also match a
declared causal-set ordering-fraction target, or is T126 only a
pre-diagnostic filter?

## Motivation

T126 created a finite causal-set/manifoldlikeness gate, and T154 connected the
actual T54/T58 canonical completions into that gate. T154 then found the
actual T51/T52 completions too small for dimension or manifoldlikeness
diagnostics.

The next risk is the opposite error: treating any larger T126 survivor as
spacetime-facing evidence merely because it passes the selected finite filter.
T156 blocks that. It adds one named causal-set comparison target:

```text
flat 1+1 interval Myrheim-Meyer ordering fraction = 1/2
```

The implementation uses a finite tolerance band. The band is an audit setting,
not a theorem about continuum convergence.

## Setup

Use the same strict relation audited by T126. For each candidate:

1. Run the T126 causal-set filter.
2. If T126 blocks the candidate, do not interpret the ordering fraction.
3. If T126 passes, compute

```text
ordering_fraction = strict comparable pairs / unordered event pairs
```

4. Compare it to the declared 1+1 target `1/2 +/- 1/10`.

## Cases

1. `flat_1p1_target_control`
   - Six deterministic light-cone-coordinate events.
   - Expected to pass T126 and lie inside the declared target band.
   - This is a calibration control, not a TaF derivation.

2. `t54_style_product_grid_2x3`
   - Six-event synthetic product-order finality colimit.
   - Expected to clear the T126 scale floor and selected filter.
   - Expected to fail the 1+1 ordering-fraction target as over-ordered.

3. `grid_filter_pass_control`
   - Existing T126 3x3 product-order survivor.
   - Expected to pass T126 but fail the 1+1 ordering-fraction target.

## Success Criteria

- The deterministic 1+1 target control passes the declared ordering-fraction
  band.
- The 2x3 and 3x3 product-grid controls pass T126 but fail the declared
  ordering-fraction band.
- S1 is not upgraded. The result must weaken T126-pass language.

## Failure Criteria

T156 fails if:

- the ordering fraction is not computed from the same strict relation used by
  T126;
- the target control is rejected by the declared band;
- product-grid survivors are promoted as 1+1 dimension evidence despite
  falling outside the declared band;
- the result is described as a dimension estimator, sprinkling theorem,
  embedding theorem, Lorentzian metric reconstruction, or spacetime
  derivation.

## Claim Impact

S1 remains `open_formal_target`.

T156 adds the following guardrail:

```text
T126 `passes_filter_only` is not even a Myrheim-Meyer ordering-fraction pass
unless the candidate also matches a declared causal-set comparison target.
```

In the implemented controls, T126 admits product-order grid survivors with
ordering fractions `4/5` and `3/4`, outside the declared 1+1 target band.
Those survivors are therefore pre-diagnostic controls only.

## Reproduction

```bash
python -m unittest tests.test_myrheim_meyer_ordering_fraction_screen -v
python -m models.run_t156
```
