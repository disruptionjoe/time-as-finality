# T428 - M2 Nonquota Aggregation Family Gate - spec (frozen)

> Recorded-tier exploratory guardrail. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the results header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain social-choice / judgment-
> aggregation language is the OBJECT OF STUDY, never evidence for physics or a
> sibling repo. The only code imports are TaF-native M2/JRC machinery plus standard
> library modules.

- Model: `models/m2_nonquota_aggregation_family_gate.py`
- Tests: `tests/test_m2_nonquota_aggregation_family_gate.py`
- Results: `results/T428-m2-nonquota-aggregation-family-gate-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_nonquota_aggregation_family_gate.py -q`

## The question this test settles

T427 blocked the threshold-index reading and left two honest M2 escape hatches:

```text
genuinely different aggregation family or separator object
```

T428 tests the first hatch. It replaces issue-wise quota aggregation with
predeclared full-judgment selector families:

- plurality over the full judgment state `(p, q)`;
- Kemeny / Hamming median over full judgment states;
- minimax Hamming selector over full judgment states.

Each selector is tested with two explicit tie completions:

- `reject`: accept `r` only when the unique selected full state is `(1, 1)`;
- `accept`: accept `r` when `(1, 1)` is among the selected states.

The selector conclusion is compared against the inherited premise-based verdict.
The gate asks whether any nonquota selector creates a larger-size
`SURVIVES-R1` finality target that survives after selector/tie/full-support
completion is admitted.

## Controls

Baseline strict-conclusion aggregation is included only as a regression control
for the inherited M2 lane:

```text
n=3 has 6 SURVIVES-R1 profiles
n=4 and n=5 have no SURVIVES-R1 profiles
```

Every nonquota selector must also report whether the separator is fully
determined by full support counts over `(00, 01, 10, 11)`. If the separator is
support-determined, it is not an independent canonicity channel; it is a
selector-completion artifact.

## Success / Kill Criteria

### RECHECK

If a nonquota selector creates `SURVIVES-R1` targets at both n=4 and n=5 and the
target is not determined by full support counts or tie completion, inspect it as a
possible M2 redesign lead. This would still not promote a claim.

### REDESIGN

If all nonquota selector positives are size-local, tie-completion artifacts, or
fully determined by full support counts, then this aggregation-family hatch does
not repair M2 canonicity. Future M2 work should move to a genuinely different
separator object or make a stronger predeclared aggregation rule with a
no-selector-leakage control.

## Honest Ceiling

Finite enumeration only: AND-doctrine profiles over `n in {3, 4, 5}`. This is not
a universal theorem about judgment aggregation, Kemeny aggregation, plurality,
minimax rules, social choice, or index theory. It tests whether this common
nonquota-selector family gives the existing M2 redesign lane a clean next finite
target.
