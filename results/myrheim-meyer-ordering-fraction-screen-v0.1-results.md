# T156 Results: Myrheim-Meyer Ordering-Fraction Screen

## Target

- Name: `flat_1p1_interval_ordering_fraction`
- Ordering fraction: 1/2 (0.500)
- Tolerance: +/- 1/10 (0.100)
- Basis: In light-cone coordinates on a flat 1+1 causal diamond, two independent points are causally related exactly when their two coordinate orderings agree, giving ordering fraction 1/2. The 1/10 tolerance is a finite-audit band, not a continuum theorem.

## Aggregate Checks

- Positive target control passes: True
- T126 pass can fail ordering-fraction target: True
- Product-grid T126 survivors fail target: True

## Audit Table

| Candidate | T126 | T126 filter | Events | Strict pairs | Ordering fraction | Gap | Verdict |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `flat_1p1_target_control` | `passes_filter_only` | `True` | 6 | 7 | 7/15 (0.467) | 1/30 (0.033) | `passes_ordering_fraction_control_only` |
| `t54_style_product_grid_2x3` | `passes_filter_only` | `True` | 6 | 12 | 4/5 (0.800) | 3/10 (0.300) | `t126_pass_but_ordering_fraction_fail` |
| `grid_filter_pass_control` | `passes_filter_only` | `True` | 9 | 27 | 3/4 (0.750) | 1/4 (0.250) | `t126_pass_but_ordering_fraction_fail` |

## flat_1p1_target_control

- Target verdict: `inside_declared_ordering_fraction_band`
- Source: deterministic light-cone coordinate control, not a TaF derivation
- Reason: The candidate's ordering fraction lies inside the declared finite 1+1 target band. This is only a calibration/control pass.
- Required next: Apply stronger dimension, abundance, sprinkling, locality, and continuum diagnostics before any spacetime-facing claim.

## t54_style_product_grid_2x3

- Target verdict: `outside_declared_ordering_fraction_band`
- Source: synthetic T54-style canonical product-order finality colimit; not an actual T54 quotient-union output
- Reason: The candidate survived T126's selected finite filter but is too highly ordered relative to the declared 1+1 flat-interval ordering-fraction target.
- Required next: Do not treat this T126 survivor as dimension evidence; either change the declared comparison target or build a less lattice-ordered finality colimit.

## grid_filter_pass_control

- Target verdict: `outside_declared_ordering_fraction_band`
- Source: small 3x3 product-order control that passes this filter only
- Reason: The candidate survived T126's selected finite filter but is too highly ordered relative to the declared 1+1 flat-interval ordering-fraction target.
- Required next: Do not treat this T126 survivor as dimension evidence; either change the declared comparison target or build a less lattice-ordered finality colimit.

## Strongest Claim

A T126 `passes_filter_only` result is not even a 1+1 Myrheim-Meyer ordering-fraction pass. The 2x3 and 3x3 product-order finality-colimit controls clear T126 but fail the declared flat 1+1 ordering-fraction band.

## What This Improved

T156 connects the finite finality-colimit bridge to a named causal-set diagnostic and supplies a deterministic positive target control, making the S1 scale-up path more reviewable.

## What This Weakened

This weakens the current S1 positive boundary: T126 survivors can be too lattice-ordered to resemble the declared 1+1 flat causal interval, so T126 passing is only a pre-diagnostic filter.

## Falsification Condition

T156 fails if the ordering-fraction calculation is not computed from the same strict relation used by T126, if the deterministic target control is rejected by the declared band, or if product grid survivors are promoted as 1+1 dimension evidence despite falling outside that band.

## S1 Update

S1 remains open_formal_target. A future spacetime-colimit witness must clear T126 and then match a declared causal-set diagnostic; T126 alone is insufficient.

## Claim Ledger Update

Add T156 to S1: scale-cleared T126 product-grid survivors can fail a declared Myrheim-Meyer 1+1 ordering-fraction target. This turns the T126 pass into a stricter pre-diagnostic gate rather than dimension or manifoldlikeness evidence.

## Open Blocker

No actual T54/T58 finality colimit both reaches T126 scale and matches a named causal-set dimension, sprinkling, locality, or continuum diagnostic.

## Suggested Next

Generate a genuine T54 quotient-union family with at least six events whose ordering fraction falls inside the declared target band, then test whether stronger interval and locality diagnostics still reject it.

## Not Claimed

T156 does not estimate continuum dimension, prove faithful embedding, derive a Lorentzian metric, or validate spacetime reconstruction.
