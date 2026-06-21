# T159 Results: T54 Interval-Jackknife Screen

## Target

- Name: `flat_1p1_interval_abundance_jackknife`
- Ordering target: `flat_1p1_interval_ordering_fraction`
- Ordering fraction: 1/2 (0.500)
- Tolerance: +/- 1/10 (0.100)
- Max parent interval size: `1`
- Required single-deletion pass rate: 1/1 (1.000)
- Basis: At the six-event T157 scale, the declared deterministic flat 1+1 target has Alexandrov intervals with at most one interior event. A candidate promoted beyond calibration-only must also keep every single-event deletion inside the same ordering-fraction band. This is a hostile finite robustness screen, not a continuum causal-set criterion.

## Aggregate Checks

- Flat parent interval support passes: True
- Flat jackknife stability fails: True
- Product-grid parent interval support fails: True
- Chain control blocked before interval screen: True
- T157 survivor demoted to calibration-only: True

## Audit Table

| Candidate | T126 | T156 | Events | Ordering fraction | Intervals | Deletion pass rate | Verdict |
| --- | --- | --- | ---: | ---: | --- | ---: | --- |
| `t157_flat_1p1_t54_colimit` | `passes_filter_only` | `passes_ordering_fraction_control_only` | 6 | 7/15 (0.467) | 0:5, 1:2 | 5/6 (0.833) | `calibration_only_fragile_jackknife` |
| `t157_product_grid_2x3_t54_colimit` | `passes_filter_only` | `t126_pass_but_ordering_fraction_fail` | 6 | 4/5 (0.800) | 0:7, 1:2, 2:2, 4:1 | 0/1 (0.000) | `blocked_at_ordering_fraction` |
| `t157_chain_6_t54_colimit` | `rank_width_obstruction` | `blocked_before_ordering_fraction_target` | 6 | 1/1 (1.000) | 0:5, 1:4, 2:3, 3:2, 4:1 | 0/1 (0.000) | `blocked_before_interval_jackknife` |

## t157_flat_1p1_t54_colimit

- Parent interval support: `True`
- Deletion stability: `False`
- Reason: The parent candidate passes the declared ordering and interval screens, but at least one single-event deletion leaves the target band, so the pass is fragile at this finite scale.
- Required next: Treat the candidate as calibration-only; search for a family or larger sample with stable suborders before S1 residue language.

| Removed event | Ordering fraction | Band | Intervals | Support |
| --- | ---: | --- | --- | --- |
| `p0` | 3/5 (0.600) | `True` | 0:4, 1:2 | `True` |
| `p1` | 1/2 (0.500) | `True` | 0:4, 1:1 | `True` |
| `p2` | 1/2 (0.500) | `True` | 0:4, 1:1 | `True` |
| `p3` | 1/2 (0.500) | `True` | 0:4, 1:1 | `True` |
| `p4` | 1/5 (0.200) | `False` | 0:2 | `True` |
| `p5` | 1/2 (0.500) | `True` | 0:4, 1:1 | `True` |

## t157_product_grid_2x3_t54_colimit

- Parent interval support: `False`
- Deletion stability: `False`
- Reason: The candidate survived T126's selected finite filter but is too highly ordered relative to the declared 1+1 flat-interval ordering-fraction target.
- Required next: Do not treat this T126 survivor as dimension evidence; either change the declared comparison target or build a less lattice-ordered finality colimit.

| Removed event | Ordering fraction | Band | Intervals | Support |
| --- | ---: | --- | --- | --- |
| `p0_0` | 7/10 (0.700) | `False` | 0:5, 1:1, 2:1 | `False` |
| `p0_1` | 4/5 (0.800) | `False` | 0:5, 1:2, 3:1 | `False` |
| `p0_2` | 9/10 (0.900) | `False` | 0:5, 1:2, 2:1, 3:1 | `False` |
| `p1_0` | 9/10 (0.900) | `False` | 0:5, 1:2, 2:1, 3:1 | `False` |
| `p1_1` | 4/5 (0.800) | `False` | 0:5, 1:2, 3:1 | `False` |
| `p1_2` | 7/10 (0.700) | `False` | 0:5, 1:1, 2:1 | `False` |

## t157_chain_6_t54_colimit

- Parent interval support: `False`
- Deletion stability: `False`
- Reason: The rank/width profile is degenerate for the selected finite control class.
- Required next: Declare a different comparison class or supply a less degenerate candidate.

| Removed event | Ordering fraction | Band | Intervals | Support |
| --- | ---: | --- | --- | --- |
| `c0` | 1/1 (1.000) | `False` | 0:4, 1:3, 2:2, 3:1 | `False` |
| `c1` | 1/1 (1.000) | `False` | 0:4, 1:3, 2:2, 3:1 | `False` |
| `c2` | 1/1 (1.000) | `False` | 0:4, 1:3, 2:2, 3:1 | `False` |
| `c3` | 1/1 (1.000) | `False` | 0:4, 1:3, 2:2, 3:1 | `False` |
| `c4` | 1/1 (1.000) | `False` | 0:4, 1:3, 2:2, 3:1 | `False` |
| `c5` | 1/1 (1.000) | `False` | 0:4, 1:3, 2:2, 3:1 | `False` |

## Strongest Claim

The T157 six-event T54 control still passes T126, T156, and the parent interval-support screen, but it is not deletion-stable: removing event p4 drops the ordering fraction to 1/5, outside the declared 1/2 +/- 1/10 band. It should be treated as a calibration artifact, not a robust S1 survivor.

## What This Improved

T159 adds a stronger post-T157 finite diagnostic that combines Alexandrov interval-size support with a jackknife stability check, making the S1 causal-set bridge harder to overread.

## What This Weakened Or Falsified

This weakens the positive reading of T157. The narrow claim that T54 can realize the ordering-fraction control survives, but the candidate fails the stricter robustness gate and therefore does not support spacetime-facing residue beyond calibration.

## Falsification Condition

T159 fails if deletion suborders are not computed from the same T54-completed relation, if parent interval sizes are read from a different causal relation than T126/T156, or if a finite jackknife failure is described as a continuum no-go theorem rather than a demotion of this small control.

## S1 Update

S1 remains open_formal_target. A finite T54 colimit must now clear T126, T156, interval-abundance, and robustness screens before it can be discussed as more than a calibration control.

## Claim Ledger Update

Add T159 to S1: the T157 flat T54 control passes parent interval support but fails the single-deletion ordering-fraction stability screen, so the current positive S1 boundary is calibration-only.

## Open Blocker

No non-hand-built T54 family, deletion-stable finite sample, sprinkling/locality diagnostic, faithful embedding theorem, continuum bridge, covariance result, or metric reconstruction exists for S1.

## Suggested Next

Search for a small non-hand-built T54 family with several deletion-stable members, or move to a proper random-sprinkling comparison with declared finite-size tolerances.

## Not Claimed

T159 does not estimate dimension, prove faithful embedding, validate a sprinkling process, derive a Lorentzian metric, or prove a continuum limit. The single-deletion screen is a finite fragility diagnostic only.
