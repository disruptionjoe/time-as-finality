# T287 Results: T252 Parent-Cap Conditioning

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `parentcap` |
| `description` | `Hard conditioning on the T252-style parent interval and cover cap.` |
| `total_weight` | `66` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '5/33', 'float': 0.15151515151515152}` |
| `parent_cap_probability` | `{'fraction': '1/1', 'float': 1.0}` |
| `selected_t252_probability` | `{'fraction': '1/66', 'float': 0.015151515151515152}` |
| `tail_lift_vs_uniform` | `{'fraction': '60480/11', 'float': 5498.181818181818}` |
| `tautological` | `False` |

- Verdict: `parent_cap_concentrates_but_does_not_isolate_tail`

## Strongest Claim

The `parentcap` measure gives the 10-case T252-style tail probability 5/33.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T287 fails if the `parentcap` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T287 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
