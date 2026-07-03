# T441: E1 Family-Limit Packet Gate

## Target Claims

- E1 asymptotic/limit mode in the adopted capability-boundary taxonomy.
- H7 physical-deletion / thermodynamic-arrow reinstatement guardrails.
- T440 follow-up route for family-level ideal-limit packets.

## Setup

T440 routes an ideal-limit packet to future E1 review only when it is a family,
not a single instance, with finite approximants, a predeclared limit invariant,
and diverging recovery cost or nonlocality.

T441 turns that route into a stricter admission gate. It does not prove any
E1 theorem. It checks whether a proposed E1 packet has enough frozen structure
to be worth future review:

- declared family and security/scale/size parameter;
- finite approximants and an approximant-to-limit map;
- stable task, operation class, observer boundary, and resource accounting;
- predeclared limit invariant visible on finite approximants;
- finite error, convergence, and negative-control plan;
- diverging recovery cost or nonlocality across the family.

## Success Criteria

- Reject single-instance infinite barriers, finite barriers, and finite positive
  gaps as E1 evidence.
- Reject post-hoc limit selectors, family drift, changed task or operation
  class, hidden resource or boundary changes, and missing finite controls.
- Reject packets that lack a declared family, parameter, finite approximants,
  approximant map, predeclared invariant, convergence/error controls, or a
  diverging family quantity.
- Route E2 hardness and E3 exact no-go packets to their own gates rather than
  admitting them as E1.
- Admit only a synthetic full packet as a future E1 review target, with no H7
  promotion, theorem claim, public posture, or claim-ledger movement.

## Failure Criteria

The artifact fails if it:

- treats a single-instance ideal lock as E1;
- treats high but finite cost as asymptotic forcing;
- allows the task, observer boundary, resource accounting, or operation class
  to change across the family;
- allows a post-hoc invariant or selector;
- treats E2 or E3 material as E1;
- claims an E1 theorem, H7 evidence, physics result, public posture, or claim
  promotion;
- edits the claim ledger, North Star, roadmap, or hard policy.

## Known Physics Constraints

This is a finite admission classifier and synthetic positive-control shape. It
does not prove a Kadanoff-style limit theorem, thermodynamic-arrow theorem,
stochastic-thermodynamic theorem, catalytic resource theorem, or physical arrow
of time.

## Contribution Needed

A future positive E1 packet must bring a named family, finite approximants,
predeclared limit invariant, convergence/error controls, fixed absorber
accounting, and an independently justified divergent recovery-cost or
nonlocality claim. Admission by T441 only means the packet is structured enough
for later review.

## Reproduction

```bash
python -m pytest tests/test_e1_family_limit_packet_gate.py -q
python -m models.e1_family_limit_packet_gate --write-results
```
