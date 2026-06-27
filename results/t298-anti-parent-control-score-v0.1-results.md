# T298 Results: Anti-Parent Control Score

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `anti_parent` |
| `description` | `Control score 2^(band + not-interval3 + not-lowcover).` |
| `total_weight` | `1659252` |
| `tail_weight` | `20` |
| `tail_probability` | `{'fraction': '5/414813', 'float': 1.2053624163177143e-05}` |
| `parent_cap_probability` | `{'fraction': '11/138271', 'float': 7.955391947696913e-05}` |
| `selected_t252_probability` | `{'fraction': '1/829626', 'float': 1.2053624163177142e-06}` |
| `tail_lift_vs_uniform` | `{'fraction': '8640/19753', 'float': 0.43740191363337216}` |
| `tautological` | `False` |

- Verdict: `anti_parent_control_suppresses_tail`

## Strongest Claim

The `anti_parent` measure gives the 10-case T252-style tail probability 5/414813.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T298 fails if the `anti_parent` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T298 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
