# T425 - M2 Size-Sweep Absorption Gate - spec (frozen)

> Recorded-tier exploratory stress test. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the results header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain index language is the
> OBJECT OF STUDY, never evidence for physics or a sibling repo. The only code
> imports are TaF-native T413/T423 machinery plus standard library modules.

- Model: `models/m2_size_sweep_absorption_gate.py`
- Tests: `tests/test_m2_size_sweep_absorption_gate.py`
- Results: `results/T425-m2-size-sweep-absorption-gate-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_size_sweep_absorption_gate.py -q`

## The question this test settles

T424 left one honest Route-A escape hatch: the n=3 triangle is too small for
some bona fide index channels. A larger complex might provide a relabel-free
index that equals the finality separator.

This test checks the prior gate:

```text
Does the inherited T423/T424 SURVIVES-R1 finality separator still exist at n=4
or n=5 under the same AND doctrine and strict-majority / tie-reject rule?
```

If larger n has no SURVIVES-R1 separator, then a larger index channel has no
finality datum to compute. The Route-A rescue is blocked before index agreement.

## Object

For each `n in {3,4,5}`:

- enumerate all `4^n` profiles of judge premise pairs `(p_i, q_i)`;
- derive `r_i = p_i AND q_i`, so every individual judgment is consistent;
- compute `v_gap(S) = premise_verdict(S) - conclusion_verdict(S)` over every
  coalition `S`;
- run the inherited `joint_record_completion_verdict` against the zero game;
- record whether the separator is `SURVIVES-R1`, `ABSORBED`, or absent;
- group profiles by the full `v_gap` vector to confirm separator status is not
  mixed inside a fiber;
- record a compatibility-graph cycle-rank diagnostic to confirm larger profiles
  do contain index-looking cycle structure.

## Success / Kill Criteria

### REDESIGN

If n=4 and n=5 have zero `SURVIVES-R1` profiles and every nonzero gap is absorbed
by a 3-judge proper subset, then T424's direct larger-index-complex rescue is
blocked. Any future rescue must predeclare a different aggregation family,
threshold rule, or separator object.

### RECHECK

If n=4 or n=5 has a `SURVIVES-R1` profile, or if a nonzero gap is not absorbed by
a proper subset, inspect the candidate as a possible direct continuation of
Route A.

## Honest Ceiling

Finite enumeration only: n=3, n=4, n=5 under one inherited doctrine and one
inherited aggregation rule. This is not a universal theorem about judgment
aggregation, social choice, or index theory. It only says the direct T423/T424
AND/strict-majority Route-A continuation does not get a larger-n finality target
for free.
