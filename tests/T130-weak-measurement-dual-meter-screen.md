# T130: Weak-Measurement Dual-Meter Screen

## Route

Experimental discriminator.

## Question

Does any concrete weak-measurement platform now provide a real dual-meter route
that could clear Q1C's independent-axis gate?

## Motivation

T91 and T93 demoted the existing superconducting homodyne, uncollapse, and
quantum-jump reversal families because their candidate TaF axes collapsed to
the same monitored record, control bookkeeping, or postselected reversal
success. The most plausible remaining rescue is a dual-meter platform that
tracks the standard weak-measurement record while also exposing an independent
physical meter, for example a calorimetric or thermal record.

## Platform Family Under Audit

1. continuous superconducting weak measurement with homodyne or no-click
   monitoring;
2. nanocalorimetric or thermal-detector measurement chains for superconducting
   circuits;
3. combined "dual-meter" proposals where the second meter records absorbed
   energy rather than the same microwave I/Q stream.

## Success Criteria

- A named platform supplies two simultaneous pre-registered records:
  the standard monitored trajectory record and a second physical meter.
- The second meter is not reconstructible from the first record plus declared
  control schedule.
- Two cases can hold the standard monitored statistics fixed while the second
  meter changes the TaF verdict.

## Failure Criteria

- The second meter replaces the standard monitored record instead of being an
  independent simultaneous axis.
- The second meter is only a noisy downstream transform of the same readout
  chain.
- No fixed-statistics witness is named where the second meter alone changes the
  TaF verdict.

## Claim Impact

Q1C remains dormant unless a real dual-meter witness exists. If the best
calorimetric or thermal-detector candidates still fail the fixed-statistics
gate, weak measurement should remain a reinstatement-only route rather than an
active experimental frontier.
