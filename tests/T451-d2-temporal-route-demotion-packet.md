# T451: D2 Temporal Route Demotion Packet

## Target Claims

- D2 computational-finality temporal route, as scoped in
  `open-problems/computational-finality-arrow.md`.
- T417 static E2 computational-finality boundary.
- Prior D2 route gates and audits: T438, T444, T446, T448, T449, T450.

## Setup

T419 first tried to turn T417's static E2 boundary into a temporal
computational-arrow route. T420 and T438 blocked finite public cycles and
bounded non-recovery. T444 admitted changed-transition/open packets only as a
separate regime. T446 built one such open Rabin-lift packet, but T448 showed
that the chain factors through public unwraps plus independent per-step Rabin
inversions. T449 sharpened the remaining closed public-squaring route to a
hidden-order period target; T450 then showed that the useful all-target period
oracle is trapdoor-strength and collapses to Rabin/factoring equivalence.

T451 executes the separate governed decision packet recommended by T450.

## Success Criteria

- Import the current D2 route evidence from T438, T444, T448, T449, and T450.
- Classify the current finite-cycle, open-chain, and closed-period routes as
  absorbed.
- Preserve a future exception for genuinely changed assumptions or scope.
- Record that the current temporal route demotes to T417's static E2 boundary.
- Leave `CLAIM-LEDGER.md`, `ROADMAP.md`, `TESTS.md`, README, North Star files,
  public posture, hard policy, and cross-repo truth untouched.

## Failure Criteria

- If any current route still contains independent temporal residue not already
  routed as a future exception, do not demote.
- If the packet would require claim-ledger movement or public posture, stop and
  record the blocker.
- If a nonstandard period assumption has already been specified in repo context
  and clears T438/T450, route to that packet instead of demoting.

## Known Constraints

This is a route-level decision, not a cryptographic theorem. It does not prove
factoring hardness, refute factoring hardness, prove a computational arrow, make
a physics claim, or move public posture. T417 remains a static E2 boundary.

## Contribution Needed

Future D2 work must change the assumption or scope: for example, a nonstandard
period assumption avoiding both single-seed weakness and all-target trapdoor
equivalence, or a separate changed-transition/open-regime packet that clears
T438/T444 without factoring through T448/T450.
