# T282 Results: Uniform Baseline

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `measure` | `uniform` |
| `description` | `Uniform ordinal ensemble over all 9! permutations.` |
| `total_weight` | `362880` |
| `tail_weight` | `10` |
| `tail_probability` | `{'fraction': '1/36288', 'float': 2.755731922398589e-05}` |
| `parent_cap_probability` | `{'fraction': '11/60480', 'float': 0.00018187830687830687}` |
| `selected_t252_probability` | `{'fraction': '1/362880', 'float': 2.7557319223985893e-06}` |
| `tail_lift_vs_uniform` | `{'fraction': '1/1', 'float': 1.0}` |
| `tautological` | `False` |

- Verdict: `uniform_tail_baseline_is_tiny`

## Strongest Claim

The `uniform` measure gives the 10-case T252-style tail probability 1/36288.

## What This Improved

This quantifies selection pressure as an exact finite weighted probability.

## What This Weakened Or Falsified

It weakens any qualitative claim about this measure unless the exact probability is high and non-tautological.

## Falsification Condition

T282 fails if the `uniform` weights are changed without renaming the measure.

## S1 Update

S1 is unchanged; this is a finite selection audit only.

## Claim Ledger Update

Do not update the claim ledger from T282 alone.

## Open Blocker

A finite weighting rule is not yet a physical finality-colimit measure.

## Suggested Next

Compare this measure against the hard-gate and soft-score rankings.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
