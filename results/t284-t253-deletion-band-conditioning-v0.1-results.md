# T284 Results: T253 Deletion-Band Conditioning

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `t253` |
| `description` | `Hard conditioning on T253-style deletion-band stability.` |
| `total_weight` | `8339` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '10/8339', 'float': 0.001199184554502938}` |
| `parent_cap_probability` | `{'fraction': '10/8339', 'float': 0.001199184554502938}` |
| `selected_t252_probability` | `{'fraction': '1/8339', 'float': 0.0001199184554502938}` |
| `tail_lift_vs_uniform` | `{'fraction': '362880/8339', 'float': 43.51600911380262}` |
| `tautological` | `False` |

- Verdict: `deletion_band_conditioning_lifts_but_stays_broad`

## Strongest Claim

The `t253` measure gives the 10-case T252-style tail probability 10/8339.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T284 fails if the `t253` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T284 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
