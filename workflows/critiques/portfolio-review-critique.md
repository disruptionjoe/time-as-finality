# Critique Log — govern/portfolio-review

Design process per DEC-019 autonomous run: draft v1 → adversarial self-critique
pass A → revise → self-critique pass B → revise → finalize. Summary below.

## Pass A — gaps, ambiguity, authority leaks, dangling routes, edge cases

Findings and fixes:
1. **Authority leak (most serious):** the first framing let portfolio-review
   "execute" merges/splits. That collides with lifecycle-review's ownership of
   `stage`/`status` and with the patch-first constraint. Fix: portfolio-review
   proposes *structure* only; every per-line stage/status consequence (a merge's
   retire, a split child's promote) is routed to lifecycle-review as a
   `lifecycle_candidate`. Added the "never both reconcile the same axis" rule and a
   dedicated "Routed Lifecycle Candidates" output section.
2. **Balance as hidden promotion:** a `balance` run could "rebalance" by quietly
   promoting/demoting lines — a lifecycle move in disguise. Fix: balance *diagnoses
   and routes* lifecycle candidates; it never moves stages. Added as an explicit
   failure-mode guard and an escalation trigger.
3. **Merge erasing information gain:** merging two lines could lose a line's
   recorded information-gain entry (violates ROM §3 / archive-never-delete). Fix:
   added information-portfolio as a read surface, made gain-preservation mandatory on
   every merge/retire-by-merge, and added a report section + verdict line for it.
4. **Dangling route risk:** decision-review and the docket consumer must exist. They
   do (decision-review designed in the same family). docket-triage is reconciled as
   decision-review's intake atom, so portfolio-review addresses docket items to
   decision-review. No undefined-workflow flag needed.
5. **Status-drift edge case:** a relationship/why-state patch could accidentally
   restate claim/roadmap/hypothesis status (violates DEC-007). Fix: explicit guard
   that the patch links out and never edits those surfaces.

## Pass B — completeness, internal consistency, ROM + locked-workflow alignment

Findings and fixes:
1. **Consumes alignment:** confirmed line-review routes "portfolio implication →
   portfolio-review" and lifecycle-review routes split/merge here by default.
   Consumes line and taxonomy now match both locked upstreams' emitted shapes; added
   a legacy-alias normalizer so routed flags map cleanly.
2. **Structure parity with exemplars:** verified the section set matches the locked
   line-review/lifecycle-review (frontmatter; title; Family/Mode/Status; Purpose;
   core invariant; conservative default; relationship section; taxonomy; canonical
   encoding; authority boundaries; read/write surfaces; memory interface; registry
   interactions; procedure; outputs; escalation; failure modes; success criteria
   with cheap test; future automation notes; verdict block; open questions). Present.
3. **Patch-first + acceptance owner:** consistent with both locked files — all
   structural changes are patch proposals applied by an accept step, never by the
   workflow. The acceptance-owner open question is shared and non-lock-gating.
4. **Dependency-graph on the proposed graph:** added the guard that cycle/dangling
   validation runs on the *proposed* graph, not just the current one — an edge fix
   must not introduce a new cycle.
5. **Lock status:** no unresolved lock-gating blocker. The four open questions
   (merge/split policy, balance policy, dependency-schema, docket location) are all
   docketed to decision-review and covered by the conservative default
   (propose-never-execute). Set to v1.0 LOCK-CANDIDATE.

## Net change v1 → final
Recast from "executes structure" to "proposes structure, routes lifecycle
consequences"; added information-gain preservation throughout; added the
proposed-graph validation guard; added balance-as-diagnosis rule; aligned the
consumes/taxonomy with both locked upstreams. No lock-gating blocker remains.
