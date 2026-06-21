# Technical Report: Weak-Measurement Escape Architecture Gate v0.1

## Claim Under Test

T143 sharpened Q1C to an architecture-level obstruction, but the repo still
needed a cleaner proposal filter:

```text
given a future auxiliary-channel proposal, what exact architecture class is it
in, and does that class remain live after T139 and T143?
```

T146 answers that question directly.

## Result

Only two live Q1C architecture classes remain:

1. an auxiliary channel tied to extra environment or detector structure whose
   verdict content survives conditioning on the full ordinary event log; or
2. an openly enlarged monitored instrument with a pre-declared preserved
   comparison target.

Everything else is now null or underdeclared.

## Executable Architecture Classes

| Class | Verdict | Reason |
| --- | --- | --- |
| `null_coarse_standard_record` | null | Fixes only a coarse standard record, so T139 already rejects it. |
| `null_screened_off_by_full_record` | null | Auxiliary content vanishes once the full ordinary transcript is fixed. |
| `null_proxy_or_postselection` | null | Uses schedule proxies or success-conditioned reversal rather than a calibrated independent meter. |
| `null_same_instrument_default` | null | Stays inside the same declared instrument and names no extra environment handle or explicit enlargement. |
| `candidate_extra_environment_escape` | live | The auxiliary channel is tied to extra environment structure that survives full-record conditioning and changes the verdict. |
| `candidate_enlarged_instrument_escape` | live | The proposal enlarges the monitored instrument and declares what fixed-standard comparison it still means to preserve. |

## Why The New Null Class Matters

The screened-off class from T137 and T139 was already necessary, but it was
not sufficient as a practical filter.

There is a softer failure mode:

```text
the proposal says the auxiliary hardware is physically distinct, but it still
stays inside the same declared instrument and never states what physically
extra structure makes the channel verdict-bearing.
```

T146 classifies that proposal as null by default. The burden now falls on the
proposal author to say one of two honest things:

- the auxiliary channel is tied to extra environment or detector structure not
  captured by the ordinary log; or
- the monitored instrument has been enlarged, and the preserved comparison
  target is declared in advance.

Without one of those admissions, "second meter" is only rhetoric.

## Strongest Current Q1C Form

The strongest safe version after T146 is:

```text
Weak measurement remains dormant unless a monitored-qubit proposal fits one of
two live architecture classes: an unscreened extra-environment auxiliary
channel, or an explicitly enlarged instrument with a pre-declared preserved
comparison target.
```

## What This Improved

T146 improves the route in three ways:

1. it separates same-instrument default null from already screened-off null;
2. it makes instrument enlargement honest rather than implicit; and
3. it tells future literature scans exactly what object is worth searching for.

That is better than another generic paper sweep because it exposes the minimum
physical burden any new proposal must carry.

## What This Weakened Or Falsified

T146 weakens a residual soft hope:

```text
if a second channel is physically distinct and not obviously derived from the
ordinary log, it probably still counts as progress.
```

No. Under the current audit posture, such a proposal is still null unless it
names extra environment structure or openly enlarges the instrument.

## Boundary Of The Result

T146 is not a theorem that extra-environment or enlarged-instrument routes
will succeed. It only states that these are the only remaining architecture
classes worth spending internal Q1C effort on.

The repo still has no concrete monitored-qubit platform in either class.

## Falsification Condition

T146 fails if a same-declared-instrument auxiliary channel with no extra
environment handle and no explicit instrument enlargement still yields a
pre-registered verdict-changing axis that survives the full-record gate.

That would show the architecture filter here is too strong.

## Open Blocker

No named monitored-qubit experiment in the repo currently instantiates either
live architecture class.

## Claim Ledger Update

Q1C remains `dormant`.

Add this sharpening:

```text
Filter future weak-measurement proposals by architecture first. Only two live
Q1C escape classes remain: extra-environment auxiliary channels not screened
off by the full ordinary log, or explicitly enlarged instruments with a
declared preserved comparison target.
```

## Recommended Next Move

Do not spend more internal time on generic second-meter searches.

Search only for one of:

1. a monitored-qubit platform with an auxiliary channel explicitly tied to
   extra environment or detector structure that survives full-record
   conditioning; or
2. an enlarged-instrument proposal that states, before analysis, the exact
   comparison target it still claims to preserve.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_escape_architecture_gate -v
python -m models.run_t146
```
