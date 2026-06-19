# Critique Log — govern/line-intake

Design process per DEC-019 autonomous run: draft v1 → pass A → revise → pass B →
revise → finalize.

## Pass A — gaps, ambiguity, authority leaks, dangling routes, edge cases

Findings and fixes:
1. **Maturity leak:** the draft let a "strong" candidate enter above seed. That
   would let intake grant maturity that must be earned (ROM §4-5). Fix: core
   invariant — every accepted candidate enters at exactly `stage: seed`,
   `status: active`; maturity is earned later via incubation + lifecycle-review.
   Reinforced in authority boundaries, the proposal shape, failure modes, and a
   Phase-4 coverage question ("Does intake ever assign maturity above seed? must be
   never").
2. **Overlap-resolution leak:** intake could "merge" a candidate into an existing
   line — that is portfolio-review's authority. Fix: intake *detects* overlap and
   *routes* it to portfolio-review; it never resolves it.
3. **Archived-line revival edge case:** a candidate that re-opens an archived line is
   not a new line — minting it would duplicate and would bypass the revival
   rationale required by lifecycle-review. Fix: dedupe checks archived lines + their
   information-portfolio entries; revivals route to lifecycle-review as a `revive`
   candidate.
4. **Off-North-Star candidate:** nothing initially stopped admitting a line that
   contradicts the program's top authority. Fix: alignment check; contradiction →
   reject with rationale (not added).
5. **Dangling route check:** routes to portfolio-review, lifecycle-review,
   decision-review — all exist. Upstream producers (explore/line-discovery,
   explore/cross-disciplinary-synthesis) are named in the README/skeleton, so they
   are valid route sources, not undefined-workflow flags. Phase-4 atom names are
   advisory only.

## Pass B — completeness, internal consistency, ROM + locked-workflow alignment

Findings and fixes:
1. **Registry-format fidelity:** the drafted ADD proposal must paste into the live
   line-registry entry format (title heading; Stage/Status/Mode-bias line;
   Why-this-stage; Artifacts; Maps-to authoritative; Relationships; Next candidate
   move). Confirmed against the current registry and stated explicitly so the accept
   step can apply it directly.
2. **DEC-007 status-drift guard:** the entry links out to CLAIM-LEDGER / ROADMAP /
   HYPOTHESES and never restates their status — consistent with line-registry's own
   status-authority rule and DEC-007.
3. **Two-axis fidelity:** seed/active uses the DEC-018/DEC-020 two-axis schema the
   registry now carries; no risk of proposing a field the registry lacks.
4. **Patch-first + acceptance owner:** consistent with the other govern workflows —
   ADD is a proposal applied by an accept step; the acceptance-owner question is the
   shared, non-lock-gating open item.
5. **Section parity:** verified the section set matches the locked exemplars
   (frontmatter through verdict block + open questions). Present and complete.
6. **Lock status:** no lock-gating blocker. Open items (intake bar, overlap-vs-new
   boundary, acceptance authority, seed-with-no-artifacts) are docketed to
   decision-review and covered by the seed-and-let-lifecycle-prune default (safe
   under ROM §1). Set to v1.0 LOCK-CANDIDATE.

## Net change v1 → final
Locked creation to seed/active as the core invariant; separated overlap *detection*
(intake) from overlap *resolution* (portfolio-review); added archived-line revival
routing and North Star alignment rejection; bound the ADD proposal to the live
registry format. No lock-gating blocker remains.
