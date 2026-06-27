# T251 Results: T249 Deletion Stability Screen

## Aggregate Checks

- Parent ordering fraction: 3/4 (0.750)
- Parent band passed: `False`
- Deletion cases: 9
- Deletions passing T126: 9
- Deletions passing ordering band: 0
- Deletion band pass rate: 0/1 (0.000)
- Verdict: `stable_over_ordering_under_single_deletion`

## Deletion Table

| Removed | T126 | Strict pairs | Ordering fraction | Band passed | Height | Width | Verdict |
| --- | --- | ---: | ---: | --- | ---: | ---: | --- |
| `p00` | `passes_filter_only` | 19 | 19/28 (0.679) | `False` | 4 | 3 | `t126_pass_but_ordering_fraction_fail` |
| `p01` | `passes_filter_only` | 21 | 3/4 (0.750) | `False` | 5 | 3 | `t126_pass_but_ordering_fraction_fail` |
| `p02` | `passes_filter_only` | 23 | 23/28 (0.821) | `False` | 5 | 2 | `t126_pass_but_ordering_fraction_fail` |
| `p10` | `passes_filter_only` | 21 | 3/4 (0.750) | `False` | 5 | 3 | `t126_pass_but_ordering_fraction_fail` |
| `p11` | `passes_filter_only` | 21 | 3/4 (0.750) | `False` | 5 | 2 | `t126_pass_but_ordering_fraction_fail` |
| `p12` | `passes_filter_only` | 21 | 3/4 (0.750) | `False` | 5 | 3 | `t126_pass_but_ordering_fraction_fail` |
| `p20` | `passes_filter_only` | 23 | 23/28 (0.821) | `False` | 5 | 2 | `t126_pass_but_ordering_fraction_fail` |
| `p21` | `passes_filter_only` | 21 | 3/4 (0.750) | `False` | 5 | 3 | `t126_pass_but_ordering_fraction_fail` |
| `p22` | `passes_filter_only` | 19 | 19/28 (0.679) | `False` | 4 | 3 | `t126_pass_but_ordering_fraction_fail` |

## Strongest Claim

The T249 grid's ordering-fraction failure is stable under every single-event deletion tested here: all nine deletions still clear T126, and none enter the declared flat 1+1 band.

## What This Improved

T251 distinguishes a fragile diagnostic failure from a structural one for the T249 witness. The over-ordering is not caused by one special grid event.

## What This Weakened Or Falsified

This further weakens T249 as an S1-facing candidate. The witness is useful as a T54/T126 construction control, but its mismatch with the declared 1+1 ordering band survives all single deletions.

## Falsification Condition

T251 fails if deletion suborders are not computed from the same T249 quotient-union relation, if T126 and T156 use different strict relations, or if this finite deletion result is treated as a general continuum or sprinkling theorem.

## S1 Update

S1 remains open_formal_target. T249 should be treated as a stable over-ordered finite control, not as spacetime-facing residue.

## Claim Ledger Update

Do not update the claim ledger from T251 alone. Safe future wording: T249's T156 failure is stable under all single-event deletions while T126 continues to pass.

## Open Blocker

No deletion-stable T54-native nine-event witness has been found inside the declared flat 1+1 ordering-fraction band.

## Suggested Next

Search beyond lattice-grid witnesses for T54-native candidates whose parent and deletion suborders both match the declared band, then apply locality and sprinkling comparisons.

## Not Claimed

T251 does not prove a continuum no-go, estimate dimension, validate or falsify random sprinkling in general, derive metric structure, or settle S1.
