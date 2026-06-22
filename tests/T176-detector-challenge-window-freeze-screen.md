# T176: Detector Challenge-Window Freeze Screen

## Route

Quantum measurement / classical records, detector evidence infrastructure only.

## Target Claims

- [Q1B: Detector Provenance Admissibility](../claims/Q1B-detector-provenance-admissibility.md)
- [T171: Detector Row-Review Substitution Screen](T171-detector-row-review-substitution-screen.md)
- [T173: Detector Claim-Review Authority Bound](T173-detector-claim-review-authority-bound.md)
- [T175: Detector Threshold-Root Quorum Screen](T175-detector-threshold-root-quorum-screen.md)

## Question

Is a T175-valid static guardian quorum map enough for the surviving Q1B route,
or is the route still null whenever guardian identity or critical challenge-
window rules can be changed after data collection begins?

## Motivation

T175 kills optional guardians inside a published quorum map. A realistic group
can still answer that the map is only the starting state, with break-glass
override, temporary trust suspension, or guardian replacement available during
dispute handling.

That loophole matters. If the challenge-window rights are mutable, then the
pre-data guardian map does not actually determine who controls row review,
revocation, or audit once the run becomes contentious.

T176 turns that loophole into a finite screen.

## Setup

Start from a T175-valid static quorum policy and audit whether the following
remain mutable during the challenge window:

- release quorums;
- revocation quorums;
- audit quorums; or
- guardian identity itself.

Include positive and negative fixtures:

1. `fully_frozen_challenge_window_policy`
2. `governance_break_glass_release_override`
3. `midwindow_escrow_replacement`
4. `trust_suspension_before_revocation`
5. `postdispute_guardian_addition`

## Success Criteria

- Exactly one fixture survives: the one where the T175-valid guardian and
  policy map is frozen until challenge-window expiry.
- Break-glass release override is null.
- Mid-window guardian replacement is null.
- Temporary trust suspension or post-dispute guardian insertion is null.
- The result stays at detector governance/admissibility level, not detector
  physics or Q1 empirical support.

## Failure Criteria

- A workflow still counts for Q1B even though guardian identity or critical
  challenge-window rights can be changed after data collection.
- The screen treats a good initial quorum map as sufficient when later policy
  mutation can bypass it.
- The result is described as detector evidence rather than a governance burden.

## Boundary Note

T176 does not claim that real collaborations can never have emergency, legal,
or safety procedures. It only says that an unmodeled post-data procedure that
can rewrite guardian identity or critical challenge-window rights is null for
the current Q1B claim-review route. A predeclared exception or successor
policy would need its own T175/T176-style audit showing that archive custody,
escrow, and trust cannot be bypassed during the review window.

## Claim Impact

Q1B remains `externally_blocked`.

Add this sharpening:

```text
A T175-valid static quorum map is scaffold-only unless the guardian roster and
critical challenge-window release, revocation, and audit policies are frozen
until challenge-window expiry.
```

## Reproduction

```bash
python -m unittest tests.test_detector_challenge_window_freeze_screen -v
python -m models.run_t176
```
