# T296 Results: Parent Soft Score

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `parent_soft` |
| `description` | `Soft integer score 2^(band + interval3 + lowcover).` |
| `total_weight` | `689517` |
| `tail_weight` | `80` |
| `tail_probability` | `{'fraction': '80/689517', 'float': 0.00011602324525718728}` |
| `parent_cap_probability` | `{'fraction': '176/229839', 'float': 0.0007657534186974361}` |
| `selected_t252_probability` | `{'fraction': '8/689517', 'float': 1.1602324525718728e-05}` |
| `tail_lift_vs_uniform` | `{'fraction': '322560/76613', 'float': 4.210251523892812}` |
| `tautological` | `False` |

- Verdict: `parent_soft_score_lifts_tail_weakly`

## Strongest Claim

The `parent_soft` measure gives the 10-case T252-style tail probability 80/689517.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T296 fails if the `parent_soft` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T296 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
