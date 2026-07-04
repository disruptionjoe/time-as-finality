# T444: E2 Changed-Transition Regime Gate

## Route

D2 computational finality / computational arrow of time, after T438 routed
changed-public-transition and open/nonpermutation packets to a separate spec.

## Question

Can the T438 separate-spec route be made executable without deciding whether D2
should be redesigned or abandoned?

## Motivation

T438 admits only closed public-permutation period-hardness packets as future D2
targets. That leaves two possible loopholes:

- make the public transition unavailable, changing, or access-relative;
- leave the closed permutation regime through open or nonpermutation dynamics.

Both may be worth reviewing later, but neither should sneak past the T438 gate as
a computational arrow. T444 classifies those packets before any future D2 attempt
uses them.

## Success Criteria

- Route ordinary closed public-permutation packets back to T438.
- Reject post-hoc transition policies, pair-specific policies, hidden selectors,
  and private transition oracles.
- Reject thermodynamic/E1 and Brown-Susskind symmetric-complexity packets.
- Reject pure epistemic ignorance of a transition as not yet a capability
  boundary.
- Require frozen transition evidence, a predeclared update/dynamics law, a public
  audit trail, and a declared agent/access boundary where applicable.
- Admit predeclared changed-transition and open/nonpermutation packets only as
  separate-regime review targets, not as D2 success.

## Failure Criteria

- Treat unknown transition state as finality.
- Treat an open dynamics fixture as E2 when ordinary resource/environment
  completion absorbs the separator.
- Claim D2 is redesigned, abandoned, discharged, promoted, or public-ready.
- Treat cryptographic or transition-regime material as physics evidence.
- Edit the claim ledger, North Star, public posture, hard policy, or T442 lane.

## Claim Impact

No claim movement. T444 only operationalizes the T438 separate-spec route. It does
not upgrade T417/T419/T420/T438 and does not choose D2 redesign or abandonment.

## Reproduction

```bash
python -m pytest tests/test_e2_changed_transition_regime_gate.py -q
python -m models.e2_changed_transition_regime_gate
```
