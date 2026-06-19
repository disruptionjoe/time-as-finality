# Research Memory — Critique Log

## Draft → Pass A (adversarial)
- **Biggest risk: silently rewriting history.** Brief is explicit. Added hard
  Must-nots against overwriting/reordering logs, rewriting PROJECT-LOG entries,
  and modifying decision-history; made all writes append/prepend-per-contract and
  patch-first.
- **Summarizer scope creep.** Memory layer is plan-only (DEC-004). Marked the
  summarizer strictly interface/spec, inert until built, and reproduced the
  MEMORY-LAYER-PLAN summarizer contract verbatim in intent (read to marker, group,
  discard noise, rollup, never write policy).
- **Memory-as-policy hazard.** Authority order §11 puts pack second-lowest. Added
  the route-out rule: policy-class lessons → decision-review, never written onto
  the pack or a higher surface.

## Revise → Pass B (adversarial)
- **Does it touch registry content?** It must not (that belongs to line-review/
  lifecycle-review/etc.). Restricted its registry writes to Document Contracts +
  hygiene only; content drift routes to the owning workflow. Added a Phase-4
  coverage answer "this workflow writes NO registry content."
- **summarizable:false enforcement.** Added explicit guard against rolling a
  canonical surface onto a load surface.
- **Compaction-resilience test.** Tied success criteria directly to operating
  model §9's stated test (a fresh agent resuming from logs+registries), and made
  it an executable step (4) with a pass/fail + gap output.
- **Routing existence.** decision-review (planned this run), docket-triage (locked
  exemplar sink), owning govern workflows all exist; undefined sinks emit
  undefined-workflow-needed. Consistent.
- **Frontmatter.** output_authority: memory_maintenance_patch_proposal; patch-first;
  unit_of_review: one_memory_maintenance_pass. Matches brief + contract.

## Finalize
- Section set matches locked exemplars; added Governing decisions + a dedicated
  summarizer section under Memory interface (the owned role).
- Status: v1.0 LOCK-CANDIDATE — no lock-gating blocker (summarizer cadence and log
  rotation are deferred Phase-3.5/4 items, not blockers to the protocol).
