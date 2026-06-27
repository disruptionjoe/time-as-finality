# T299 Results: Selected Shape Soft Score

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `shape_soft` |
| `description` | `Soft score for T252-like parent shape labels without using the tail label.` |
| `total_weight` | `987721` |
| `tail_weight` | `640` |
| `tail_probability` | `{'fraction': '640/987721', 'float': 0.0006479562548533443}` |
| `parent_cap_probability` | `{'fraction': '2208/987721', 'float': 0.0022354490792440376}` |
| `selected_t252_probability` | `{'fraction': '128/987721', 'float': 0.00012959125097066883}` |
| `tail_lift_vs_uniform` | `{'fraction': '3317760/141103', 'float': 23.513036576118154}` |
| `tautological` | `False` |

- Verdict: `shape_soft_score_enriches_selected_tail_but_stays_broad`

## Strongest Claim

The `shape_soft` measure gives the 10-case T252-style tail probability 640/987721.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T299 fails if the `shape_soft` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T299 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
