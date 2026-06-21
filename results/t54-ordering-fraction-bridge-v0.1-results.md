# T157 Results: T54 Ordering-Fraction Bridge

## Target

- Name: `flat_1p1_interval_ordering_fraction`
- Ordering fraction: 1/2 (0.500)
- Tolerance: +/- 1/10 (0.100)
- Basis: In light-cone coordinates on a flat 1+1 causal diamond, two independent points are causally related exactly when their two coordinate orderings agree, giving ordering fraction 1/2. The 1/10 tolerance is a finite-audit band, not a continuum theorem.

## Aggregate Checks

- T54 flat candidate reaches T126 scale: True
- T54 flat candidate matches target band: True
- T54 product-grid control fails target band: True
- T54 chain control blocked before target: True
- Previous T156 open blocker removed: True

## Audit Table

| Candidate | T54 | T126 | T126 filter | Events | Strict pairs | Ordering fraction | Gap | Verdict |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `t157_flat_1p1_t54_colimit` | `canonical` | `passes_filter_only` | `True` | 6 | 7 | 7/15 (0.467) | 1/30 (0.033) | `t54_colimit_matches_ordering_fraction_control_only` |
| `t157_product_grid_2x3_t54_colimit` | `canonical` | `passes_filter_only` | `True` | 6 | 12 | 4/5 (0.800) | 3/10 (0.300) | `t54_colimit_fails_ordering_fraction_target` |
| `t157_chain_6_t54_colimit` | `canonical` | `rank_width_obstruction` | `False` | 6 | 15 | 1/1 (1.000) | 1/2 (0.500) | `blocked_at_t126` |

## t157_flat_1p1_t54_colimit

- T54 theorem applies: `True`
- Target verdict: `inside_declared_ordering_fraction_band`
- Reason: The T54-completed colimit reaches the T126 filter and its ordering fraction lies inside the declared finite 1+1 band.
- Required next: Apply stronger dimension, abundance, sprinkling, locality, and continuum diagnostics before any spacetime-facing claim.

## t157_product_grid_2x3_t54_colimit

- T54 theorem applies: `True`
- Target verdict: `outside_declared_ordering_fraction_band`
- Reason: The candidate survived T126's selected finite filter but is too highly ordered relative to the declared 1+1 flat-interval ordering-fraction target.
- Required next: Do not treat this T126 survivor as dimension evidence; either change the declared comparison target or build a less lattice-ordered finality colimit.

## t157_chain_6_t54_colimit

- T54 theorem applies: `True`
- Target verdict: `not_reached_t126_blocked`
- Reason: The rank/width profile is degenerate for the selected finite control class.
- Required next: Declare a different comparison class or supply a less degenerate candidate.

## Strongest Claim

A hand-built but genuine T54 canonical quotient-union datum can reach the T126 scale floor and land inside the declared flat 1+1 ordering-fraction band: the six-event T157 control has ordering fraction 7/15.

## What This Improved

T157 replaces the previous synthetic-only positive ordering-fraction control with a T54-completed colimit, while preserving negative T54 controls for the over-ordered product grid and the degenerate chain.

## What This Weakened Or Falsified

The narrow T156 blocker 'no actual T54 finality colimit reaches scale and matches the declared ordering-fraction band' is now false. This does not upgrade S1, because the survivor is a constructed finite control and has not faced interval-abundance, locality, sprinkling, covariance, or continuum diagnostics.

## Falsification Condition

T157 fails if the T54 completion does not reproduce the audited strict relation, if the same relation is not used by T126 and T156, if the product-grid and chain controls stop blocking the claimed interpretation, or if the positive finite control is described as spacetime evidence.

## S1 Update

S1 remains open_formal_target. The scale/order-fraction blocker has been cleared for one constructed T54 control, but the result is still only a pre-diagnostic finite colimit control.

## Claim Ledger Update

Add T157 to S1: a constructed six-event T54 canonical quotient-union colimit reaches T126 and matches the declared 1+1 ordering-fraction band, while T54 product-grid and chain controls remain rejected or demoted. This removes the immediate T156 scale/order-fraction blocker without upgrading S1.

## Open Blocker

No non-hand-built observer-local family, interval-abundance diagnostic, locality/sprinkling screen, embedding theorem, continuum-limit bridge, covariance result, or Lorentzian metric reconstruction exists for the T157 survivor.

## Suggested Next

Subject the T157 flat control and nearby T54-generated families to a stronger interval-abundance or locality diagnostic; require failure to demote the survivor back to a calibration artifact.

## Not Claimed

T157 does not estimate dimension, prove a faithful embedding, derive a Lorentzian metric, validate sprinkling behavior, or derive spacetime.
