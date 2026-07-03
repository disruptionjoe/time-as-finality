# T438: E2 Period-Hardness Admission Gate

## Route

D2 computational finality / computational arrow of time, after T419 REDESIGN and
T420 finite-cycle anti-relabel guardrail.

## Question

Can the post-T420 redesign rule be made into an executable admission gate for any
future E2 computational-finality attempt, without deciding whether D2 should be
redesigned or abandoned?

## Motivation

T419 failed because the exhibited finite public squaring orbit was a short cycle.
T420 generalized the failure: on a closed finite public permutation, predecessor
recovery is public once the cycle is traversable. A future D2 attempt therefore
cannot pass by naming point-inversion hardness or by showing bounded non-recovery
inside a toy cycle.

T438 turns that rule into a packet classifier. It admits only a narrow kind of
future target: a family-level period-hardness redesign packet that is explicit
about the security parameter, the public transition, the feasible-agent bound, the
period/reversal problem, and the named hardness assumption. Admission is not a
D2 success.

## Success Criteria

- Reject T419-style finite public cycles when public forward iteration recovers
  predecessors inside the declared bound.
- Reject bounded non-recovery when no family-level period-hardness assumption is
  declared.
- Reject point-square-root or point-inversion hardness alone as a static T417
  relabel rather than a temporal arrow.
- Reject thermodynamic-cost, symmetric complexity-growth, post-hoc, hidden-label,
  and single-instance packets.
- Route changed-public-transition or open-regime packets to a separate spec rather
  than admitting them as closed-public-permutation D2.
- Admit a predeclared family-level period-hardness packet only as a future E2
  redesign target, with no claim promotion and no D2 decision.

## Failure Criteria

- Treat a finite toy cycle as evidence for a computational arrow.
- Treat bounded search failure as arrow evidence.
- Claim D2 is redesigned, abandoned, discharged, promoted, or public-ready.
- Treat cryptographic material as physics evidence.
- Use sibling-repo material as support.
- Edit the claim ledger, North Star, public posture, or hard policy.

## Claim Impact

No claim movement. If T438 holds, it only operationalizes the admission burden for
future D2 work. It does not choose redesign or abandon, and it does not upgrade
T417/T419/T420.

## Reproduction

```bash
python -m pytest tests/test_e2_period_hardness_admission_gate.py -q
python -m models.e2_period_hardness_admission_gate
```
