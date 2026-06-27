# T297 Results: Deletion Soft Score

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `deletion_soft` |
| `description` | `Soft integer score 2^(band + interval3 + lowcover + t253 + relaxed deletion interval3).` |
| `total_weight` | `790437` |
| `tail_weight` | `320` |
| `tail_probability` | `{'fraction': '320/790437', 'float': 0.0004048393483604639}` |
| `parent_cap_probability` | `{'fraction': '256/263479', 'float': 0.0009716144360651134}` |
| `selected_t252_probability` | `{'fraction': '32/790437', 'float': 4.048393483604639e-05}` |
| `tail_lift_vs_uniform` | `{'fraction': '3870720/263479', 'float': 14.690810273304514}` |
| `tautological` | `False` |

- Verdict: `deletion_soft_score_lifts_tail_more_but_not_enough`

## Strongest Claim

The `deletion_soft` measure gives the 10-case T252-style tail probability 320/790437.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T297 fails if the `deletion_soft` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T297 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
