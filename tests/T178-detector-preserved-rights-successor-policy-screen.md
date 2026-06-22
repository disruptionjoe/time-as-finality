# T178: Detector Preserved-Rights Successor Policy Screen

## Route

Quantum measurement / classical records, detector evidence infrastructure only.

## Target Claims

- [Q1B: Detector Provenance Admissibility](../claims/Q1B-detector-provenance-admissibility.md)
- [T175: Detector Threshold-Root Quorum Screen](T175-detector-threshold-root-quorum-screen.md)
- [T176: Detector Challenge-Window Freeze Screen](T176-detector-challenge-window-freeze-screen.md)

## Question

T176 says mutable challenge-window rights are null by default. Does that force
literal immutability, or can a predeclared legal, safety, or emergency
successor policy preserve the surviving Q1B review rights?

## Motivation

If the repo insists on absolute freeze with no exception class, Q1B risks
becoming operationally unrealistic for the wrong reason. If it accepts generic
successor language, it reopens the same loophole T176 was written to close.

T178 tests the only useful middle position:

```text
predeclared successor policy that preserves rights
```

## Setup

Start from a T175-valid, T176-frozen challenge-window policy and audit whether
any successor path:

- is frozen pre-data;
- has explicit trigger conditions;
- preserves the same mandatory archive, escrow, and trust guardians on every
  critical action;
- preserves already-granted full row-review access during the challenge
  window;
- preserves guardian identity; and
- emits immutable transition logs.

Include positive and negative fixtures:

1. `fully_frozen_no_successor_policy`
2. `predeclared_preserved_rights_legal_hold_successor`
3. `undeclared_break_glass_successor`
4. `predeclared_release_pause_pending_governance_clearance`
5. `predeclared_escrow_rotation_successor`
6. `predeclared_revocation_override_successor`

## Success Criteria

- The fully frozen policy survives.
- A predeclared successor survives only when it preserves guardians, access,
  identity, and immutable logs.
- Undeclared break-glass override is null.
- Review-pausing, guardian-rotating, or revocation-bypassing successors are
  null.
- The result stays at detector governance/admissibility level, not detector
  physics or Q1 empirical support.

## Failure Criteria

- A successor policy still counts for Q1B even though it was not frozen
  pre-data.
- A successor counts while reducing outside row-review access.
- A successor counts while changing guardian identity or letting critical
  actions bypass archive, escrow, or trust.

## Boundary Note

T178 does not claim that real collaborations can never have legal, safety, or
emergency procedures. It claims only that the current Q1B route can admit such
procedures, if at all, only as preserved-rights successor policies that are
typed and frozen before data collection.

## Claim Impact

Q1B remains `externally_blocked`.

Add this sharpening:

```text
A challenge-window exception policy counts only if it is predeclared and
preserves the same mandatory guardians, guardian identity, full row-review
access, and immutable transition logging throughout the review window.
```

## Reproduction

```bash
python -m unittest tests.test_detector_preserved_rights_successor_policy_screen -v
python -m models.run_t178
```
