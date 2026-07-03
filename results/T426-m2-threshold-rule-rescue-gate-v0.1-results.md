# T426 - M2 Threshold-Rule Rescue Gate - v0.1 results

> Recorded-tier exploratory stress test. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the spec header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain social-choice / index
> language is the OBJECT OF STUDY, never evidence for physics or a sibling repo.
> The only code imports are TaF-native T423/T425 machinery plus standard library
> modules.

- Spec (frozen first): `tests/T426-m2-threshold-rule-rescue-gate.md`
- Model: `models/m2_threshold_rule_rescue_gate.py`
- Tests: `tests/test_m2_threshold_rule_rescue_gate.py` (5 passed)
- Artifact JSON: `results/T426-m2-threshold-rule-rescue-gate-v0.1.json`
- Run: `python -m pytest tests/test_m2_threshold_rule_rescue_gate.py -q`

## Overall verdict: RECHECK_SIZE_MATCHED_THRESHOLD_ONLY

T425 said the direct larger-index rescue is blocked under the inherited AND /
strict-majority rule, and any rescue must predeclare a new aggregation family,
threshold rule, or separator object.

T426 tests the threshold-rule branch. The result is not a clean negative:

```text
Fixed high quota fractions can create larger-n SURVIVES-R1 targets.
```

But it is also not a stable threshold rescue:

```text
The targets appear only in size-matched cells: 3/4 at n=4 and 4/5 at n=5.
No single fixed quota survives both n=4 and n=5.
```

So the high-quota targets are real finite testbeds, but they are not yet M2
canonicity progress. A follow-up index/fiber probe would need threshold-tuning
controls before claiming anything stronger.

## Quota sweep

| rule | n=3 verdict | n=4 verdict | n=5 verdict | reading |
| --- | ---: | ---: | ---: | --- |
| strict majority / tie reject | 6 SURVIVES | 60 ABSORBED | 390 ABSORBED | T425 regression reproduced |
| 1/2 quota | 18 ABSORBED | 110 ABSORBED | 570 ABSORBED | weak thresholds expose pairwise proper-subset gaps |
| 2/3 quota | 6 SURVIVES | 60 ABSORBED | 390 ABSORBED | same pattern as strict majority over n=3..5 |
| 3/4 quota | 0 | 12 SURVIVES | 140 ABSORBED | size-matched n=4 target only |
| 4/5 quota | 0 | 0 | 20 SURVIVES | size-matched n=5 target only |
| unanimity | 0 | 0 | 0 | no premise/conclusion gap appears |

## What the size-matched cells are doing

The positive cells are not arbitrary profile accidents. They share the same quota
shape:

```text
grand coalition accepts at n-1 of n,
but every top proper coalition requires unanimity.
```

For `3/4` at `n=4`, the coalition-size requirements are:

```text
1 -> 1, 2 -> 2, 3 -> 3, 4 -> 3
```

For `4/5` at `n=5`, they are:

```text
1 -> 1, 2 -> 2, 3 -> 3, 4 -> 4, 5 -> 4
```

This creates a clean whole-only gap: the grand coalition can accept both
premises with one dissenter per premise, while every large proper subset must be
unanimous and therefore cannot already carry the same datum.

The same fixed quota loses this shape when moved to the next size:

- `3/4` at `n=5` has 140 nonzero gaps, all ABSORBED at size 4.
- `4/5` at `n=4` has no nonzero gaps.

That is the threshold-tuning risk. The rule can produce a target, but the target
tracks the size/quota step rather than an obviously stable finality object.

## What this says about M2

The threshold-rule rescue is open only in a narrowed sense:

- There are real larger-n SURVIVES-R1 targets under predeclared high quotas.
- They are not inherited from T423/T424 strict majority.
- They are not stable under a single fixed quota across `n=4` and `n=5`.
- They therefore should be treated as finite testbeds, not as a canonicity lift.

If this lane continues, the next gate should not merely compute an index on the
positive cells. It must first guard against threshold tuning:

```text
Does any candidate index distinguish the high-quota target without merely reading
the size-matched quota step?
```

## What this earns / does not earn

Earns: a bounded finite map of the threshold-rule rescue class for the M2
AND-doctrine fixture over `n in {3,4,5}` and quotas
`1/2, 2/3, 3/4, 4/5, 1`, including exact positive cells for `3/4@4` and `4/5@5`.

Does not earn: a stable threshold rescue, a canonical index, a universal theorem
about judgment aggregation or social choice, any claim-ledger movement, any
physics-facing claim, or any cross-repo evidential use.
