# T286 Results: Low-Cover Conditioning

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `lowcover` |
| `description` | `Hard conditioning on T126+band and parent cover hub <= 2/7.` |
| `total_weight` | `185` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '2/37', 'float': 0.05405405405405406}` |
| `parent_cap_probability` | `{'fraction': '66/185', 'float': 0.3567567567567568}` |
| `selected_t252_probability` | `{'fraction': '1/185', 'float': 0.005405405405405406}` |
| `tail_lift_vs_uniform` | `{'fraction': '72576/37', 'float': 1961.5135135135135}` |
| `tautological` | `False` |

- Verdict: `low_cover_is_best_single_hard_gate`

## Strongest Claim

The `lowcover` measure gives the 10-case T252-style tail probability 2/37.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T286 fails if the `lowcover` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T286 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
