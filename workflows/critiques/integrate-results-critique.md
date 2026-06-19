# integrate-results — critique log

## Self-critique A
- Does it canonize? No — every durable-surface edit (claims/, CLAIM-LEDGER,
  ROADMAP, GLOSSARY) is a patch-first, accept-gated proposal; core invariant +
  Failure mode "canonizing by integrating". PASS.
- Stage -> integrated owned by lifecycle-review (DEC-018, high-scrutiny)? Yes —
  emitted as an `integrate` lifecycle_candidate; Purpose, core invariant, step 6,
  Failure mode "self-promoting the stage" all enforce. PASS.
- Integration != proof? Yes — readiness gate requires survived_challenge +
  sufficient evidence, not certainty; Failure mode "integration as proof". PASS.
- Independence-audit handled correctly (point, don't rewrite verdict)? Yes —
  "Must not" + Failure mode + escalation. PASS.
- DEC-007 (registry never restates status): registry patch limited to evidence
  pointers / next move. PASS.
- Consistency check covers glossary collision, ledger inconsistency, dependency
  cycle, guardrail/North-Star conflict. PASS.

## Revision after A
- Added explicit `integration_readiness` gate block (six fields) + a
  `not_integration_ready` outcome that routes a challenge-worthiness signal when a
  challenge is owed — closes the "premature integration" hole and links integrate
  back to challenge-primary (so the exploit arc advance->challenge->integrate is
  fully wired).
- Added `integration_proposed_with_conflicts` outcome so a flagged consistency
  result is auditable rather than blocking silently.

## Self-critique B
- Section parity with locked exemplars: full set incl. Consumes/Emits, Core
  invariant, readiness gate, Outcome classes, two patch shapes, Docket shape,
  cheap test. PASS.
- Bundle atomicity: success criterion + decomposition note both require the
  proposal be accept/rejectable as ONE bundle (a reviewer-legibility win). PASS.
- Route targets exist/locked or docketed: lifecycle-review (consumes integrate
  candidate), line-review (re-score), portfolio-review (structure/cycles, a known
  referenced sink), challenge-primary, info-portfolio, docket. PASS.
- LOCK-CANDIDATE: open questions (acceptance owner, accept-ordering, audit
  coupling, readiness calibration) all non-gating + docketed. → v1.0 LOCK-CANDIDATE.

## Revision after B
- None structural; confirmed claims/ new files are "proposed as patch content,
  created on acceptance" rather than written as authoritative directly.

## Cross-cutting (all four exploit workflows)
- Shared discipline consistent across the family: evaluation mode stated;
  patch-first + accept-gated for all authority surfaces; one bounded unit per run;
  lifecycle moves always routed to lifecycle-review; re-score always to
  line-review; failures/survivals preserved with info-gain (ROM §3); identical
  verdict block (ROM §10); DEC-013 inheritance note in every decomposition
  section; shared docket signal_type `patch-acceptance-owner-needed`.
- The four compose a clean arc: advance-primary (develop) / advance-secondary
  (develop minority, guard budget) / challenge-primary (red-team) / integrate-
  results (fold in). advance-secondary -> challenge-primary (challenge-worthiness)
  -> lifecycle-review (demote) and ... -> integrate-results (integrate) all route
  through the locked govern workflows without any exploit workflow exceeding its
  authority.
