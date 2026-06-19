# challenge-primary — critique log

## Self-critique A
- Adversarial posture present? Yes — hostile/skeptic cluster (philosophy/
  testability/skepticism: 50, 27, 51) as REVIEW POSTURE, not authority/evidence
  (ROM §6). Failure mode "persona-as-evidence" guards it. PASS.
- Successful challenge routes a lifecycle (demote/challenge) candidate to
  lifecycle-review AND a re-score to line-review? Yes — step 7, outcome classes,
  escalation, core invariant. Does NOT execute the demotion. PASS.
- Survival-argument rule (ROM §5) applied before demotion? Yes — mandatory step 5
  check; `challenged_survives_via_survival_argument` outcome; Failure mode
  "bypassing the survival argument". PASS.
- Three attack modes (counterexample / hidden-assumption / overclaim) per spec?
  Yes — challenge taxonomy + step 4 branches. PASS.
- Failed challenge as positive outcome (ROM §3)? Yes — survived = strengthened
  primary, recorded + info-gain. PASS.
- Truth-verdict leak? No — weakening patch is patch-first/accept-gated; falsity
  is the authority surface's call. PASS.

## Revision after A
- Added explicit `challenged_survives_via_survival_argument` outcome class and
  wired it through escalation + report (the survival-argument case was implied but
  needed its own labeled outcome to be auditable).
- Tied the demote candidate's `why_source_workflow_cannot_decide` text to the
  canonical lifecycle_candidate shape so it docks cleanly into lifecycle-review's
  intake.

## Self-critique B
- Section parity with locked exemplars: full set incl. Consumes/Emits, Core
  invariant, Challenge taxonomy, Outcome classes, Docket shape, cheap test. PASS.
- Route targets exist/locked or docketed: lifecycle-review (locked, consumes
  lifecycle_candidate), line-review (locked, consumes re-score), info-portfolio,
  docket. challenge-worthiness inbound from advance-secondary is consistent. PASS.
- Open Q2 (demote vs a distinct challenge candidate type) correctly flagged as a
  lifecycle-review/decision-review schema question rather than invented here —
  honors "do not invent policy". PASS.
- LOCK-CANDIDATE: open questions non-gating (survival adjudicator, candidate-type
  schema, cadence, acceptance owner), all docketed. → v1.0 LOCK-CANDIDATE.

## Revision after B
- None structural; verified deep-panel only loads on trigger (matches line-review
  exemplar), keeping the default context bounded to the skeptic cluster.
