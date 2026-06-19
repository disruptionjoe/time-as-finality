# advance-primary — critique log

Process: draft → self-critique A → revise → self-critique B → revise → finalize.

## Self-critique A
- Authority leak check: Does any step write claim/roadmap/hypothesis status
  directly? No — step 6/7 propose patches only; core invariant + Failure mode
  #1 guard it. PASS.
- Does it write to `claims/`? No — that durable folding is integrate-results'
  job; advance-primary writes results/tests/models only. Kept the boundary in
  "Must not" (integration → integrate-results). PASS.
- DEC-007 (registry never restates claim/roadmap/hyp status): honored — all
  status lives on the authority surfaces; registry patch is limited to next-move
  + evidence pointers. PASS.
- DEC-013 (task atoms inherit authority): decomposition notes state it. PASS.
- Single-object discipline (ROM §13): "one bounded move per run" enforced in
  scope, step 3, Failure mode "scope creep". PASS.
- Mode (evaluation) stated explicitly (Purpose + Failure mode "mode bleed"). PASS.
- Edge case: zero/multiple primary lines — handled (step 1, outcome
  blocked_ambiguous_primary, docket). PASS.
- Edge case: no defensible move — handled (no_move_available + re-score). PASS.
- Failure preservation (ROM §3): negative-result outcome + info-gain. PASS.

## Revision after A
- Added overclaim_check field to status_patch_proposal and an explicit overclaim
  gate before strengthening patches.
- Clarified that the artifact is a direct write (new record) vs status = patch.

## Self-critique B
- Exemplar section parity vs line-review/lifecycle-review: frontmatter, title,
  Family/Mode/Status, Consumes/Emits, Purpose, Core invariant, Authority
  boundaries, Read/Write surfaces, Memory interface, Registry interactions,
  Procedure, Outcome classes, Outputs, Escalation, Docket shape, Failure modes,
  Success criteria + cheap test, Future automation decomposition notes, Verdict
  block, Open questions. PARITY OK.
- Route targets all exist or are docketed-as-undefined: line-review (locked),
  lifecycle-review (locked), integrate-results (this family), information-
  portfolio (govern), docket-triage (referenced sink). PASS.
- LOCK-CANDIDATE: no lock-gating blocker; open questions are non-gating
  (acceptance owner, rigor threshold, budget, calibration) and shared/docketed.
  → v1.0 LOCK-CANDIDATE.

## Revision after B
- No structural change needed; confirmed verdict block matches ROM §10 currency.
