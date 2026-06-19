# Persona Governance — Critique Log

## Draft → Pass A (adversarial)
- **Risk: authority creep into persona conclusions.** Original draft let it "tune
  weighting" without explicitly forbidding changing votes. Added explicit
  Must-not: change scoring conclusions or any persona's vote.
- **Risk: it could author personas, colliding with explore/persona-expansion.**
  Added a hard STOP/route at intake (step 1) and a Phase-4 coverage question
  ("expansion authors, governance clusters") to prevent double ownership.
- **Risk: deciding the coverage gap unilaterally.** Brief says own the decision
  but route it. Clarified: owns *surfacing*, routes the *policy choice* to
  decision-review, proposes only a provisional best-fit patch-first so scoring is
  not blocked.
- **Mirror sync hazard.** Made mirror patches explicitly
  apply-after-canonical-acceptance, matching DEC-006 (canonical = source).

## Revise → Pass B (adversarial)
- **Routing target existence.** decision-review and persona-expansion both exist
  (planned this run / skeleton). docket-triage matches the locked line-review/
  lifecycle-review sink. deep-panel-review left as undefined-workflow-needed,
  consistent with the locked exemplars (which also defer it).
- **unit_of_review scoping.** Tightened intake to split bundled requests so the
  one_persona_or_cluster_change unit is honored and atoms stay right-sized.
- **Frontmatter.** output_authority set to persona_registry_patch_proposal (fit);
  patch-first; summarizable:false — matches contract + exemplars.
- **Two-axis / terminology.** No lifecycle vocabulary used here; "research line"
  terminology only where lines are referenced. Consistent.

## Finalize
- Section set matches locked exemplars (added Governing decisions, Coverage-gap
  handling as workflow-specific sections, consistent with line-review's
  "Governing decisions" block).
- Status: v1.0 LOCK-CANDIDATE — no lock-gating blocker (coverage-gap is a
  pre-existing open question already docketed, not a blocker to this protocol).
