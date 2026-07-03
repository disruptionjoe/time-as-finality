# T427 - M2 Threshold-Index Leakage Gate - spec (frozen)

> Recorded-tier exploratory guardrail. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the results header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain social-choice / index
> language is the OBJECT OF STUDY, never evidence for physics or a sibling repo.
> The only code imports are TaF-native T426 machinery plus standard library
> modules.

- Model: `models/m2_threshold_index_leakage_gate.py`
- Tests: `tests/test_m2_threshold_index_leakage_gate.py`
- Results: `results/T427-m2-threshold-index-leakage-gate-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_threshold_index_leakage_gate.py -q`

## The question this test settles

T426 found that high fixed quota fractions can create larger-n SURVIVES-R1
targets only in size-matched cells:

```text
3/4 at n=4
4/5 at n=5
```

T426 therefore required threshold-tuning controls before any follow-up index
reading:

```text
Does any candidate index distinguish the high-quota target without merely reading
the size-matched quota step?
```

T427 runs that guardrail over the adjacent high-quota universe:

```text
3/4 at n=4, 3/4 at n=5, 4/5 at n=4, 4/5 at n=5
```

## Object

For each profile in the four-cell universe:

- reuse the T426 AND-doctrine and quota-rule machinery;
- compute whether the profile has a SURVIVES-R1 separator;
- inspect direct support/quota channels:
  - profile support counts over `(00, 01, 10, 11)`;
  - cell-local support `(rule, n, support_counts)`;
  - support plus quota step `(support_counts, grand_requirement,
    top_proper_requirement)`;
  - quota-margin signature `(p_margin, q_margin, r_margin, top_minus_grand)`;
- inspect candidate index-style channels that do not read the quota rule:
  - crossing-edge count;
  - compatibility-graph cycle rank;
  - complete signed-graph frustration index;
  - the triple of those three graph diagnostics.

The leakage test asks whether a channel perfectly predicts the separator and,
if so, whether it is merely direct support/quota information rather than an
independent index object.

## Success / Kill Criteria

### REDESIGN

If every perfect separator channel is a direct support/quota leak, and every
graph/frustration-style candidate index collides with nonseparator profiles, then
the T426 high-quota positives remain finite testbeds only. Future M2 work must
move to a genuinely new aggregation family or separator object, or define a
different predeclared index with an explicit no-leakage control.

### RECHECK

If a quota-independent graph/index channel perfectly predicts the separator over
the target/control universe, inspect it as a possible finite index target. That
would still not promote a claim; it would only justify a narrower follow-up.

## Honest Ceiling

Finite enumeration only: four high-quota cells over `n in {4,5}` under the T426
AND-doctrine fixture. This is not a universal theorem about judgment
aggregation, social choice, thresholds, signed graphs, or index theory. It only
tests whether the T426 positives already have a clean quota-independent index
reading in the predeclared diagnostic family.
