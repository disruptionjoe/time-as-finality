# T431 - M2 Independent-Channel Admission Gate - spec (frozen)

> Recorded-tier exploratory admission artifact. `TESTS.md`, `ROADMAP.md`, and
> `CLAIM-LEDGER.md` are UNTOUCHED; the T-number lives only in this header / the
> results header. NO claim promotion; ledger actions pause for Joe. Cross-domain
> social-choice / index language is the OBJECT OF STUDY, never evidence for
> physics or a sibling repo.

- Model: `models/m2_independent_channel_admission_gate.py`
- Tests: `tests/test_m2_independent_channel_admission_gate.py`
- Results: `results/T431-m2-independent-channel-admission-gate-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_independent_channel_admission_gate.py -q`

## The question this test settles

T430 closed the bounded support-family M2 branch and named the next gate:

```text
A future M2 attempt must move off this support-family universe or predeclare an
independent measurement channel with no-completion controls.
```

T431 asks:

```text
Can a candidate M2 channel be admitted as independent only if it is not
recoverable from support counts, ambient size, quota step, selector/tie
completion, or proper-subset deletion-critical wording?
```

## Certificate inputs

T431 evaluates the current T424 Route-A channels over the AND-doctrine profile
universe:

- `finality_separator`;
- `I_chi`;
- `I_fr`;
- `I_sf`.

It also includes leaky negative controls and one guard-only positive control so
the admission detector proves it can both reject completion-derived signals and
see a deliberately independent label.

## Success / Kill Criteria

### Admission

A non-guard domain channel is admitted only if it:

- is non-null;
- is not recoverable from the old `v_gap` reference primitive;
- is not recoverable from support counts;
- is not recoverable from ambient size;
- is not recoverable from quota-step data;
- is not recoverable from selector/tie completion;
- is not recoverable from deletion-critical wording.

### REDESIGN / no current channel

If all current T424 domain candidates are null or completion-recoverable, record
that no current channel is admitted. Future M2 work must predeclare a new domain
channel before another swing.

### RECHECK

If any non-guard domain channel clears the gate, inspect it before using T431 as a
negative closure artifact.

## Honest Ceiling

Finite admission/control test only: T431 covers the current T424/T430 finite
AND-doctrine context. It is not a universal no-go theorem about judgment
aggregation, social choice, index theory, separator objects, finality, physics, or
cross-repo structure.

It does not move `TESTS.md`, `ROADMAP.md`, `CLAIM-LEDGER.md`, North Star, canon,
public posture, hard policy, or cross-repo truth.
