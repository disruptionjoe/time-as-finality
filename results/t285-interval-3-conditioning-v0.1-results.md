# T285 Results: Interval-3 Conditioning

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `interval3` |
| `description` | `Hard conditioning on T126+band and parent largest interval <= 3.` |
| `total_weight` | `91350` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '1/9135', 'float': 0.00010946907498631637}` |
| `parent_cap_probability` | `{'fraction': '11/15225', 'float': 0.000722495894909688}` |
| `selected_t252_probability` | `{'fraction': '1/91350', 'float': 1.0946907498631636e-05}` |
| `tail_lift_vs_uniform` | `{'fraction': '576/145', 'float': 3.972413793103448}` |
| `tautological` | `False` |

- Verdict: `interval3_conditioning_stays_too_broad`

## Strongest Claim

The `interval3` measure gives the 10-case T252-style tail probability 1/9135.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T285 fails if the `interval3` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T285 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
