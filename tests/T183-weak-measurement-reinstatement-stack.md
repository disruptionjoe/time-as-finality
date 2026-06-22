# T183: Weak-Measurement Reinstatement Stack

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [T166: Weak-Measurement Platform-Packet Gate](T166-weak-measurement-platform-packet-gate.md)
- [T149: Weak-Measurement Conditional-Sufficiency Gate](T149-weak-measurement-conditional-sufficiency-gate.md)
- [T150: Weak-Measurement Verdict-Admissibility Gate](T150-weak-measurement-verdict-admissibility-gate.md)
- [T158: Weak-Measurement Preserved-Target Gate](T158-weak-measurement-preserved-target-gate.md)
- [T182: Weak-Measurement Platform Family Screen](T182-weak-measurement-platform-family-screen.md)

## Question

Can Q1C reinstatement be treated as a single executable stack rather than a
sequence of prose gates?

## Motivation

After T182, no currently named platform family is live. The remaining risk is
procedural: a future proposal could clear one local gate and be described as
"close" to Q1C while still failing another required burden.

T183 removes that ambiguity. It composes packet intake, architecture
consistency, typed verdict lift, and enlarged-instrument preserved-target
honesty into one proposal-level screen.

## Setup

Audit stack proposals over:

1. a T166 platform packet;
2. a T149/T150 event-level verdict input;
3. a T158 preserved-target input when the packet declares an enlarged
   instrument.

Admit two positive controls:

1. an extra-environment packet with typed verdict lift;
2. an enlarged-instrument packet with typed verdict lift and honest
   eventwise preservation of the full ordinary standard record.

Reject null controls:

1. packet-only promises with no event-level verdict data;
2. zero-lift packets;
3. auxiliary-defined verdicts;
4. enlarged instruments whose preserved target drifts;
5. coarse-record packets;
6. the current same-instrument frontier.

## Success Criteria

- Both stack-positive controls are admitted.
- Every null control is rejected by a specific lower-level gate.
- The current Q1C frontier remains closed.
- No local positive control is promoted into reinstatement without clearing
  the whole stack.

## Failure Criteria

- A packet-only proposal counts as live.
- A positive decision-lift proposal counts despite an auxiliary-defined verdict.
- An enlarged-instrument proposal counts despite target drift.
- The composed stack rejects a proposal that satisfies all lower-level
  assumptions.

## Claim Impact

Q1C remains `dormant`.

The sharper statement is:

```text
Q1C is reinstated only by a stack-positive proposal: T166 packet intake,
architecture consistency, T149/T150 typed verdict lift, and T158 preserved-
target honesty for enlarged instruments.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_reinstatement_stack -v
python -m models.run_t183
```
