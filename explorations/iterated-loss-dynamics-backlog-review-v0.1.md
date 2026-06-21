# Iterated Loss Dynamics Backlog Review

## Context Read

This review inspected the active persona run queue, the general explorations
backlog, `open-problems/loss-kernel-formalization.md`, and the earned
LossKernel-adjacent artifacts around T69, T73, T63/T65, and the Pati-Salam
typed-forgetting witness.

The repo currently supports one-step or path-level loss claims, not iterated
orbit claims. T73's union law is the main null explanation any iterated proposal
must beat.

## Disposition Summary

| Goal | New relative to existing LossKernel work? | Finite executable test? | GU overclaim risk? | Neutral math-paper connection? | Expected value | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| A: Iterated Loss Dynamics | Yes: asks about `LossKernel(T^n)`, not only path composition | Yes | Low if no GU source needed | Strong if it extends T69/T73 | Potential algebra extension | Add to persona backlog and open problem |
| B: GU-Generated Bundle Loop Witnesses | Partly: source of finite loops, not a new theorem | Yes, if reduced to finite operators | High unless quarantined | Medium as example generator | Useful examples only | Add to persona backlog with GU guardrail |
| C: Latent Signatures of Iterated Loss | Yes as tooling, not as theory | Yes | Low | Medium if it finds families symbolic work missed | Example discovery | Add to persona backlog, not open problem by itself |
| D: Recurrence Classification Theorem | Premature | Eventually | Medium if examples come from GU | Strong only after A-C | Too early | Defer/block until examples exist |
| E: LossKernel Orbit Space | Yes: defines orbit equivalence | Yes | Low | Strong if orbit invariants survive | Candidate formal object | Add to persona backlog and open problem |

## Goals Added

- P73: Iterated Loss Dynamics Researcher.
- P74: GU-Generated Loop Witness Auditor.
- P75: Iterated Loss Signature Extractor.
- P76: LossKernel Orbit-Space Formalist.
- P77: Recurrence Classification Theorem Hunter, marked `blocked` until P73-P76
  produce nontrivial examples.
- `open-problems/iterated-loss-dynamics.md`.
- One iterated-orbit question and relationship row in
  `open-problems/loss-kernel-formalization.md`.

## Goals Rejected

No goal was rejected outright. The idea is not ready for main-line promotion,
but the executable finite-test path is clear enough to preserve.

## Goals Deferred

Goal D is deferred. A recurrence classification theorem would be attractive but
currently unearned. It should wait until examples show behavior not already
covered by finite powerset saturation or T73 union accumulation.

## Candidate Main-Line Promotions

None.

Iterated loss should be treated as a candidate extension of the LossKernel
formalization program, not as an independent main research line. Promotion would
require a witness where `LossKernel(T^n)` explains something the one-step
kernel and ordinary composition do not.

## Strategic Judgment

Current status is between B and C:

```text
B. useful example generator
C. possible legitimate extension of the LossKernel algebra
```

It is not yet D, a new main research line. It is also not merely A,
visualization trick, because finite orbit behavior can be tested directly and
connects to T69/T73/T63/T65.

## Recommended Next Concrete Test

Build T101: Iterated Loss Dynamics.

The minimal executable target should include four controls:

1. fixed-loss morphism, where `LossKernel(T^n)` is constant;
2. saturating-loss morphism, where new typed losses accumulate then stabilize;
3. period-2 loop, the finite Mobius-like case;
4. cycle-destroying degradation, linked back to T69.

The run should decide whether the observed trajectories are:

- already explained by T73 union accumulation;
- useful only as generated examples; or
- evidence for a finite LossKernel orbit object.
