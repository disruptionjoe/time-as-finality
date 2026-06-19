---
document_type: historical_record
primary_reader: mixed
read_pattern: chronological
write_pattern: append
authority: historical_only
summarizable: false
---

# QA Report — Phases 3 / 3.5 / 4

**Date:** 2026-06-19 (Session 18). **Method:** deterministic structural scan
(orchestrator) + fresh-eyes semantic review (independent subagent; drafter ≠
critic, DEC-021). **Scope:** the 18 workflow protocols, the Phase-3.5 memory layer
(`context-packs/`), the Phase-4 automation scaffold (`automation/`), and supporting
registries / decision-history against `RESEARCH-OPERATING-MODEL.md`.

## Verdict

**Sound. Zero blockers.** Phase 3/3.5/4 is internally consistent and ready: the
16 lock-candidates may be flipped to LOCKED, and the system is safe to move toward
arming (arming itself stays human-gated; every canonical write is patch-first /
accept-gated; all 65 triggers are NOT-ARMED). Findings were documentation-
consistency, not authority or logic flaws.

## Structural scan (orchestrator)

77 checks passed; 5 issues surfaced, triaged below. Confirmed: 18 workflows + 6
memory-pack files + 4 automation files present; frontmatter on every in-scope file
(after fixes); required sections + verdict block per workflow; 18/18 workflows in
the coverage matrix; 0 armed triggers; DEC numbering contiguous 1..24; five pieces
in each MEMORY.md; `archived` used only as a status in the line registry.

## Semantic review (fresh-eyes subagent) — findings & dispositions

| id | sev | finding | disposition |
|---|---|---|---|
| (struct) | — | 3 registries (foundation-queue, information-portfolio, persona-clusters) lacked document-contract frontmatter | **FIXED** — contracts added |
| M1 | major | `README.md` still framed as "Phase 2 / placeholders" — and it is the route-target catalog workflows trust | **FIXED** — banner + how-to updated to Phase 3/3.5/4 state |
| M2 | major | `COVERAGE-MATRIX.md` said "Memory layer not yet built", contradicting DEC-023 | **FIXED** — now "built (DEC-023) but not yet wired/validated" |
| m4 | minor | line-registry said lifecycle-review "applies" promotion/demotion (it is patch-first/propose-only) | **FIXED** — reworded to "proposes (patch-first) … an accept step applies them" |
| m1 | minor | locked line-review/lifecycle-review still call `docket-triage` a "separate workflow" | **ACCEPTED** — superseded by DEC-022; locked files left unedited by design; add a pointer on next post-lock errata |
| m2 | minor | several explore workflows route test candidates to `tests/` (a directory, not a workflow/owner) | **DEFERRED** — clarify `tests/` proposals as inert artifacts (picked up by exploit/*) or define an owner; closes the last routing-closure soft gap |
| m3 | minor | `evidence-review` referenced as possibly-existing | **OK** — handled conditionally with `undefined-workflow-needed` fallback; keep deep-panel-review + evidence-review on the allowed-undefined list |
| m5 | minor | ROM §3 gain-type prose vs information-portfolio `gain_type` enum lexical mismatch | **DEFERRED** — align tokens or add a one-line crosswalk |
| (cosmetic) | cosmetic | RL-006 "Why this stage: archived" reads oddly now that stage=validated/status=archived; foundation-queue seed note mentions routing persona flags to persona-clusters (workflow routes to persona-expansion) | **DEFERRED** — tidy wording on next pass |

## No authority/logic defects found

The reviewer confirmed: the propose-vs-canonize split holds everywhere; no
workflow self-canonizes or seizes another's authority; only lifecycle-review moves
stage/status, only portfolio-review does cross-line structure, only decision-review
proposes DEC-NNN; the two-axis lifecycle is applied correctly throughout; memory
packs are strictly guidance (rank 6) and inert; all 65 triggers honestly
NOT-ARMED with truthful coverage answers.

## Arming prerequisites (unchanged; honestly disclosed in SCHEDULE-SPEC §5)

1. Patch-acceptance owner decided (the most-referenced open item).
2. Cadences / thresholds / per-run budget caps set.
3. Memory layer wired + shadow-run validated.
4. deep-panel-review: standalone workflow vs inline atom.
5. 0–3 standing calibration anchors.

## Recommendation

Flip the 16 lock-candidates to LOCKED; action the deferred minors (m2, m5,
cosmetics) opportunistically; resolve arming prerequisites before any trigger is
armed.
