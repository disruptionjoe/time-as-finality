# Technical Report: Measured Detector Policy Sensitivity v0.1

## Claim Under Test

T76 converted the detector branch into a measured-posterior audit, but it left
one open vulnerability: the signed positive verdict still depended on a chosen
acceptance policy. T77 asks whether that verdict survives stricter
pre-registered confidence and false-risk bounds.

## Artifact

T77 adds an executable policy-sensitivity audit over the T76 measured fixtures:

```text
deployment evidence
  -> posterior ranges
  -> policy corridor
  -> T74 Monte Carlo classifier
  -> Q1 verdict
```

The policy variable is separated from the measured deployment evidence. This
prevents a positive verdict from being attributed solely to instrumentation
quality when it may instead be produced by a permissive acceptance policy.

## Policies

- `strict`: confidence floor `0.90-0.95`, false-risk ceiling `0.05-0.10`;
- `baseline`: confidence floor `0.78-0.85`, false-risk ceiling `0.12-0.22`;
- `permissive`: confidence floor `0.65-0.75`, false-risk ceiling `0.25-0.35`.

## Controls

T77 reuses the T76 deployments:

- `measured_signed_time_tag_stack`;
- `timing_only_unsigned_control`;
- `signed_stack_incomplete_preregistration_control`.

These controls ask three distinct questions:

- does the signed result survive stricter policy?;
- does timing-only evidence stay insufficient even if the policy is relaxed?;
- does incomplete pre-registration remain a failure mode even if policy is
  relaxed?

## Current Strongest Claim

The signed measured fixture is robust across the tested policy family, but the
discriminator is not. Once policy becomes permissive enough, the timing-only
unsigned control starts to receive a small positive recovery rate.

## What This Improved

T77 makes the detector branch easier to falsify. The next lab-facing question
is no longer just "what evidence is needed?" but also "what pre-registered
acceptance corridor can that evidence actually sustain?"

## What This Weakened

T77 weakens any reading of T76 that would treat the signed measured fixture as
automatically sufficient. The main vulnerability is not that stricter policy
kills the signed positive result; it is that looser policy begins to admit
timing-only unsigned false positives.

## Falsification Condition

Demote the detector branch if no pre-registered policy corridor preserves all
three separations at once: signed measured recovery, unsigned timing-only
withhold, and incomplete-pre-registration failure.

## Claim Ledger Update

Q1 should remain `partially_supported`, but detector-level support narrows
again:

```text
Measured detector provenance is operational only inside an explicitly
pre-registered policy corridor that preserves control separation. The signed
positive result is robust here, but permissive policy already weakens the
unsigned control.
```

## Next Work

Compute the loosest policy corridor that still preserves:

- signed measured recovery;
- unsigned timing-only withhold;
- incomplete-pre-registration failure.

That corridor is the real experimental target for any future detector run.

## Reproduction

```bash
python -m unittest tests.test_measured_detector_policy_sensitivity -v
python -m models.run_t77
```
