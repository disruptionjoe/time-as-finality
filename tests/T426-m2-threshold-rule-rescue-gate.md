# T426 - M2 Threshold-Rule Rescue Gate - spec (frozen)

> Recorded-tier exploratory stress test. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the results header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain social-choice / index
> language is the OBJECT OF STUDY, never evidence for physics or a sibling repo.
> The only code imports are TaF-native T423/T425 machinery plus standard library
> modules.

- Model: `models/m2_threshold_rule_rescue_gate.py`
- Tests: `tests/test_m2_threshold_rule_rescue_gate.py`
- Results: `results/T426-m2-threshold-rule-rescue-gate-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_threshold_rule_rescue_gate.py -q`

## The question this test settles

T425 closed the direct larger-index rescue under the inherited AND doctrine and
strict-majority / tie-reject rule:

```text
n=4 and n=5 have no inherited SURVIVES-R1 finality target.
```

It left only a new object class:

```text
predeclare a different aggregation family, threshold rule, or separator object.
```

This test checks the threshold-rule version before any new index channel is
allowed:

```text
Can a fixed quota threshold rule create a non-atomic n=4 or n=5 SURVIVES-R1
target under the same AND doctrine?
```

## Object

For each `n in {3,4,5}` and each quota fraction

```text
1/2, 2/3, 3/4, 4/5, 1
```

where the quota for a coalition `S` is `ceil(q * |S|)` and the empty coalition
rejects:

- enumerate all `4^n` profiles of judge premise pairs `(p_i, q_i)`;
- derive `r_i = p_i AND q_i`, so every individual judgment is consistent;
- compute premise verdict by applying AND to the quota verdicts of `p` and `q`;
- compute conclusion verdict by the same quota rule on `r`;
- compute `v_gap(S) = premise_verdict(S) - conclusion_verdict(S)` over every
  coalition `S`;
- run the inherited `joint_record_completion_verdict` against the zero game;
- record whether the separator is `SURVIVES-R1`, `ABSORBED`, or absent;
- record the minimum separating coalition size and quota support pattern;
- compare each quota to the inherited strict-majority baseline.

The quotas are predeclared as rule-level candidates, not chosen after seeing a
profile.

## Success / Kill Criteria

### REDESIGN

If no predeclared quota produces a stable non-atomic n=4 or n=5 SURVIVES-R1
target, or if every candidate larger-n target exists only under a threshold that
also creates many small/proper-coalition targets and therefore reads as
threshold-tuned residue, then the threshold-rule rescue is blocked. Future M2
work must move to a genuinely different aggregation family or separator object.

### RECHECK

If a predeclared quota produces n=4 or n=5 SURVIVES-R1 profiles whose minimum
separating coalition is the full grand coalition, and the same rule has
nontrivial controls rather than arbitrary threshold tuning, inspect it as a
possible index target.

## Honest Ceiling

Finite enumeration only: `n in {3,4,5}` under one doctrine (AND) and four
predeclared quota rules. This is not a universal theorem about judgment
aggregation, social choice, thresholds, or index theory. It only blocks or opens
the threshold-rule rescue route for this finite M2 fixture.
