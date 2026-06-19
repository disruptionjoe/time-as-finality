# Repo Hygiene Review — redundancies & conflicts from the workflows layer

**Date:** 2026-06-19. **Scope:** redundancies and conflicts the new `workflows/`
operating layer introduces (or exposes) in the Time as Finality repo, with
recommendations. Quick triage, prioritized. Nothing here has been changed yet —
these are proposals for a future `govern/persona-governance` /
`govern/research-memory` pass.

## High priority

**H1 — Persona system fragmentation. ✅ RESOLVED (Session 5).** Canonical source
is now `personas/EXPERT-PANEL.md` (1–62); the panel script and skill read it; the
in-skill copy is a mirror pointer; INDEX and persona-clusters reference it.
There are two near-canonical persona sources — `personas/INDEX.md` (review
*lenses*) and `agent-skills/time-as-finality-persona-panel/references/personas.md`
(56 numbered *experts*) — and the new `workflows/registries/persona-clusters.md`
adds a third. They overlap heavily: e.g. Hashgraph (lens *and* persona #55),
Avalanche (lens + #56), ZK/crypto (lens + #13), distributed systems (lens + #9).
The six new lenses (57–62) were added to `INDEX.md`, but the matching numbered
personas don't exist yet.
*Recommendation:* make one source canonical under `personas/` (the numbered
experts), have `persona-clusters.md` and the lens registry *reference* it, add
numbered personas 57–62, and record the lens↔persona mapping. Treat the in-skill
`references/personas.md` as a generated/mirrored copy, not a second source of
truth. Owned by `govern/persona-governance`.

**H2 — Parallel status tracking. ✅ RESOLVED (Session 5).** The line registry is
now a portfolio/grouping layer that links out to the authoritative surfaces and
restates no status; conflicts resolve in favor of the authoritative surface and
are logged.
`line-registry.md` introduced lifecycle states over work whose status is already
tracked in `CLAIM-LEDGER.md` (per-claim), `ROADMAP.md` ("Completed v0.1"), and
`HYPOTHESES.md` (H-status). Without a defined relationship these will drift.
*Recommendation:* declare the line registry the *portfolio/grouping* layer — a
research line is a named set of claims/tests — that **links to** but never
duplicates claim/test status. Add a "maps to" column (claims/tests) and make
`govern/line-review` responsible for reconciling, not re-recording.

## Medium priority

**M1 — `persona-idea-sprint` counts are now stale.**
`agent-skills/persona-idea-sprint.md` hard-codes "7 families / 43 lenses" and
fixed group assignments (A–E). Adding the Simulation/MMO/Game-Mechanism family
makes that 8 families, and the new lenses aren't routed to any group.
*Recommendation:* update the family table and assign the new family to a group
(natural fit: the Computation/Distributed group, or a new Simulation group).

**M2 — `governance/` vs `workflows/govern/` naming overlap.**
The repo already has `governance/` (a review packet); now there's
`workflows/govern/` (governance workflows). Two "governance" homes invite
confusion.
*Recommendation:* keep both but state the split explicitly — `governance/` holds
governance *artifacts/packets*; `workflows/govern/` holds the *workflows* that
produce them — and cross-link. `governance/` becomes a route target for govern
runs.

**M3 — `agent-skills/` vs `workflows/` overlap.**
`persona-idea-sprint` and the persona panel are, functionally, Explore/Govern
workflows that live outside `workflows/`. `explore/line-discovery` already
*references* the sprint, which is the right call.
*Recommendation:* keep referencing (don't duplicate); long-term, register these
skills as the canonical *implementations* of the relevant workflows rather than
re-implementing them.

**M4 — Root `README.md` doesn't list the new layer.**
The root "Repository Map" omits `workflows/` (and also `audits/`, `governance/`,
`papers/`, `agent-skills/`).
*Recommendation:* add `workflows/` to the map (and ideally the other missing
dirs) so the operating layer is discoverable.

## Low priority

**L1 — Two transitional docs in `workflows/`.**
`RESEARCH-POSTURE.md` (redirect stub, kept per your call) and
`WORKFLOW-SKELETON-PROPOSAL.md` (a plan now executed) are both transitional.
*Recommendation:* add an "executed — see README" banner to the proposal; retire
both into `logs/` once the model has proven stable.

**L2 — Lock the term "research line" in `GLOSSARY.md`.**
We deliberately reserved "branch" for git. One glossary line prevents future
drift.
*Recommendation:* add "research line" (and note it ≠ git branch) to
`GLOSSARY.md`.

**L3 — Pre-existing clutter (not created by this project).**
`.claude/worktrees/wf_115d3e7f-439-2/` contains a full duplicate copy of many
repo files — an apparently stale git worktree.
*Recommendation:* if abandoned, prune with `git worktree remove`. Flagged only
because it showed up while mapping the repo; unrelated to `workflows/`.

## Suggested order

H1 and H2 are the only two that will cause real drift if left; do them before
Phase 3 wires workflow behavior to these registries. M1–M4 are quick coherence
fixes. L1–L3 are cleanup whenever convenient.
