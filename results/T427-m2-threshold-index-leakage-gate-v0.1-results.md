# T427 - M2 Threshold-Index Leakage Gate - v0.1 results

> Recorded-tier exploratory guardrail. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the spec header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain social-choice / index
> language is the OBJECT OF STUDY, never evidence for physics or a sibling repo.
> The only code imports are TaF-native T426 machinery plus standard library
> modules.

- Spec (frozen first): `tests/T427-m2-threshold-index-leakage-gate.md`
- Model: `models/m2_threshold_index_leakage_gate.py`
- Tests: `tests/test_m2_threshold_index_leakage_gate.py` (5 passed)
- Artifact JSON: `results/T427-m2-threshold-index-leakage-gate-v0.1.json`
- Run: `python -m pytest tests/test_m2_threshold_index_leakage_gate.py -q`

## Overall verdict: REDESIGN_THRESHOLD_INDEX_LEAKAGE

T426 left a narrow opening: high fixed quota fractions create larger-n
SURVIVES-R1 targets, but only in size-matched cells. T427 tests whether those
positive cells already have a clean index reading.

They do not.

Across the four-cell high-quota universe:

```text
3/4 at n=4
3/4 at n=5
4/5 at n=4
4/5 at n=5
```

there are 2,560 profiles and 32 SURVIVES-R1 targets. The only channels that
perfectly identify those 32 targets read quota/support data directly:

- cell-local support;
- support plus quota step;
- the quota-margin signature `(0, 0, -1, 0)`.

Every graph/frustration-style candidate index collides with nonseparator
profiles.

## Cell map

| rule | n | grand req | top-proper req | separator profiles | reading |
| --- | ---: | ---: | ---: | ---: | --- |
| 3/4 | 4 | 3 | 3 | 12 | target cell |
| 3/4 | 5 | 4 | 3 | 0 | same support shape absorbs into size-4 proper subsets |
| 4/5 | 4 | 4 | 3 | 0 | no nonzero target |
| 4/5 | 5 | 4 | 4 | 20 | target cell |

## Leakage controls

Support alone is not stable across adjacent quota controls:

| support counts `(00,01,10,11)` | separator=0 | separator=1 | reading |
| --- | ---: | ---: | --- |
| `(0,1,1,2)` | 12 | 12 | 3/4@n=4 survives; 4/5@n=4 control does not |
| `(0,1,1,3)` | 20 | 20 | 4/5@n=5 survives; 3/4@n=5 absorbs |

Adding the quota step makes the separator perfect, but that is exactly the
leakage T427 was built to block:

```text
p margin = 0
q margin = 0
r margin = -1
top-proper quota minus grand quota = 0
```

This signature says only that the premises exactly meet the grand quota, the
conclusion misses it by one, and top proper coalitions have the same requirement
as the grand coalition. That is T426's size-matched threshold mechanism, not an
independent index.

## Candidate index channels

| channel | collision values | separator collision | reading |
| --- | ---: | --- | --- |
| crossing-edge count | 1 | value `1`: 224 nonseparators / 32 separators | fails separator |
| compatibility cycle rank | 2 | values `2` and `5` collide | fails separator |
| signed-graph frustration index | 1 | value `1`: 736 nonseparators / 32 separators | fails separator |
| graph diagnostic triple | 2 | `(1,2,1)` and `(1,5,1)` collide | fails separator |

The graph channels are not useless as diagnostics; they show the positive cells
have structure. But they do not distinguish the finality target from nearby
nonseparator profiles. The clean separator is still carried only by quota/support
bookkeeping.

## What this says about M2

The threshold-index follow-up is blocked in the tested family:

- T426's high-quota positives remain real finite testbeds.
- They are not a stable M2 canonicity lift.
- The tested quota-independent graph/frustration channels do not separate them.
- The perfect channels are exactly the threshold-tuning/support leaks the guard
  was meant to catch.

Future M2 work should move to a genuinely different aggregation family or
separator object, or predeclare a new index with a stronger no-leakage control
than support/quota-step recovery.

## What this earns / does not earn

Earns: a bounded finite guardrail showing that the T426 high-quota targets do
not already carry a clean quota-independent index in the tested diagnostic
family.

Does not earn: a universal no-go theorem, a stable threshold rescue, a canonical
index, any claim-ledger movement, any physics-facing claim, or any cross-repo
evidential use.
