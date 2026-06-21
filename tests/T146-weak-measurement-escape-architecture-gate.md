# T146: Weak-Measurement Escape Architecture Gate

## Route

Quantum measurement / classical records.

## Question

After T139 and T143, what exact auxiliary-channel architectures could still
reopen Q1C, and which proposal shapes should now be rejected immediately as
null or underdeclared?

## Motivation

T143 sharpened the obstruction to an architecture-level statement: once the
full pre-registered ordinary event log is treated as the ordinary instrument's
conditional transcript, same-instrument auxiliary channels are null by default
unless they capture genuinely extra environment structure or explicitly
enlarge the monitored instrument.

What remained missing was an executable gate that turns that prose into a
durable proposal filter.

## Setup

T146 audits six proposal classes:

1. `coarse_record_only`
   The proposal fixes only a coarse standard record rather than the full
   event-level transcript.
2. `screened_off_by_full_record`
   The auxiliary channel is determined once the full ordinary record is fixed.
3. `proxy_or_postselected`
   The auxiliary axis is a control-schedule proxy or success-conditioned
   reversal variable.
4. `same_instrument_default_null`
   The proposal stays inside the same declared instrument and names no extra
   environment structure or explicit instrument enlargement.
5. `extra_environment_candidate`
   The auxiliary channel is tied to extra environment or detector structure
   that survives full-record conditioning and changes the verdict.
6. `enlarged_instrument_candidate`
   The proposal openly enlarges the monitored instrument and pre-declares the
   preserved comparison target.

## Success Criteria

- The artifact distinguishes "screened off" from the stronger T143 default
  null: same-instrument proposals with no extra environment handle are
  rejected even before a concrete unscreened witness is shown.
- The live escape classes are minimal and costly: extra environment structure
  or explicit instrument enlargement with an honest comparison target.
- The current frontier classifies as dormant/null.

## Failure Criteria

- Any physically distinct same-instrument hardware is treated as a live route
  without extra environment structure.
- Instrument enlargement is allowed to count without naming the preserved
  fixed-standard comparison.
- Coarse-record or postselected loopholes are allowed back in.

## Claim Impact

Q1C remains dormant.

Add this sharpening:

```text
Future weak-measurement proposals should be filtered first by architecture.
Only two live Q1C escape classes remain: an auxiliary channel tied to extra
environment structure not screened off by the full ordinary log, or an openly
enlarged instrument with a pre-declared preserved comparison target.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_escape_architecture_gate -v
python -m models.run_t146
```
