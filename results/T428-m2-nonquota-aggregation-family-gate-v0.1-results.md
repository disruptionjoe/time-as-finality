# T428 - M2 Nonquota Aggregation Family Gate - v0.1 results

> Recorded-tier exploratory guardrail. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the spec header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain social-choice / judgment-
> aggregation language is the OBJECT OF STUDY, never evidence for physics or a
> sibling repo. The only code imports are TaF-native M2/JRC machinery plus standard
> library modules.

- Spec (frozen first): `tests/T428-m2-nonquota-aggregation-family-gate.md`
- Model: `models/m2_nonquota_aggregation_family_gate.py`
- Tests: `tests/test_m2_nonquota_aggregation_family_gate.py` (6 passed)
- Artifact JSON: `results/T428-m2-nonquota-aggregation-family-gate-v0.1.json`
- Run: `python -m pytest tests/test_m2_nonquota_aggregation_family_gate.py -q`

## Overall verdict: REDESIGN_NONQUOTA_SELECTOR_COMPLETION

T427 left one M2 escape hatch: leave threshold rules and try a genuinely
different aggregation family. T428 tests a bounded, common nonquota family:
full-judgment selectors over `(p, q)` states, compared against the inherited
premise-based verdict.

The hatch does not repair M2 canonicity in the tested family.

Conservative plurality and minimax tie completion create n=4 positives, but no
tested selector has `SURVIVES-R1` positives at both n=4 and n=5. Every selector
separator is constant on full-support fibers over `(00, 01, 10, 11)`, so the
signal is selector/full-support completion rather than an independent finality
channel.

## Baseline control

Strict conclusion-majority aggregation reproduces the inherited M2 size pattern:

| n | SURVIVES-R1 | absorbed | no separation |
| ---: | ---: | ---: | ---: |
| 3 | 6 | 0 | 58 |
| 4 | 0 | 60 | 196 |
| 5 | 0 | 390 | 634 |

This is a regression control only. It is not counted as a nonquota selector.

## Selector family map

| selector family | tie completion | n=3 SURVIVES-R1 | n=4 SURVIVES-R1 | n=5 SURVIVES-R1 | reading |
| --- | --- | ---: | ---: | ---: | --- |
| plurality | reject | 6 | 24 | 0 | n=4 finite selector artifact |
| plurality | accept | 0 | 0 | 0 | all nonzero gaps absorbed |
| Kemeny/Hamming median | reject | 0 | 0 | 0 | collapses to premise completion |
| Kemeny/Hamming median | accept | 0 | 0 | 0 | all nonzero gaps absorbed |
| minimax Hamming | reject | 9 | 24 | 0 | n=4 finite selector artifact |
| minimax Hamming | accept | 3 | 0 | 0 | n=3-only artifact |

The two n=4 positive cells are:

| family | n | SURVIVES-R1 profiles | absorbed profiles | min-sep distribution |
| --- | ---: | ---: | ---: | --- |
| plurality_reject | 4 | 24 | 60 | none: 172, size 3: 60, size 4: 24 |
| minimax_reject | 4 | 24 | 66 | none: 166, size 3: 66, size 4: 24 |

Both vanish at n=5.

## Full-support completion control

For every selector family and every tested size, the separator is constant on full
support-count fibers:

```text
support counts = (#00, #01, #10, #11)
```

The mixed support-fiber count is `0` in all 18 selector cells. This means the
selector separator is recoverable from the same full support data the selector
itself reads. That is not a second independent canonicity channel.

Representative n=4 positives show the completion:

- plurality/reject sample support `(1, 1, 0, 2)` selects `(11)` uniquely; selector
  accepts while premise aggregation rejects, producing a grand gap `-1`.
- minimax/reject sample support `(0, 2, 1, 1)` also selects `(11)` uniquely;
  selector accepts while premise aggregation rejects, producing a grand gap `-1`.

These are real finite artifacts, but they are not stable M2 progress.

## What this says about M2

The nonquota selector branch is blocked in this bounded test:

- no tested family survives at both n=4 and n=5;
- conservative tie completion can create finite positives, but only locally;
- Kemeny/reject gives no gap at all because it matches the premise completion;
- liberal tie completion mostly turns gaps into proper-subset absorption;
- every separator is full-support determined.

Future M2 work should move to a genuinely different separator object, or
predeclare a stronger aggregation family with an explicit no-selector-leakage
control.

## What this earns / does not earn

Earns: a finite guardrail showing that common nonquota full-judgment selector
families do not by themselves reopen M2 canonicity after T427.

Does not earn: a universal no-go theorem, a canonical aggregation family, a
stable M2 rescue, any claim-ledger movement, any physics-facing claim, or any
cross-repo evidential use.
