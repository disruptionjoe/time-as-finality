# T283 Results: T126 Plus T156 Conditioning

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `band` |
| `description` | `Hard conditioning on T126 plus the declared T156 ordering band.` |
| `total_weight` | `143435` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '2/28687', 'float': 6.971799072750723e-05}` |
| `parent_cap_probability` | `{'fraction': '66/143435', 'float': 0.00046013873880154774}` |
| `selected_t252_probability` | `{'fraction': '1/143435', 'float': 6.9717990727507235e-06}` |
| `tail_lift_vs_uniform` | `{'fraction': '72576/28687', 'float': 2.5299264475197827}` |
| `tautological` | `False` |

- Verdict: `band_conditioning_barely_lifts_tail`

## Strongest Claim

The `band` measure gives the 10-case T252-style tail probability 2/28687.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T283 fails if the `band` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T283 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
