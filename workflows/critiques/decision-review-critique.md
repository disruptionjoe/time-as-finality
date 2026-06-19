# Critique Log — govern/decision-review

Design process per DEC-019 autonomous run: draft v1 → pass A → revise → pass B →
revise → finalize.

## Pass A — gaps, ambiguity, authority leaks, dangling routes, edge cases

Findings and fixes:
1. **Self-canonization (the central risk):** the workforce that *proposes* DEC-NNN
   could too easily *write* DEC-NNN. That would invert ROM §11 (only an explicit
   user/authority acceptance canonizes). Fix: made "proposes; never canonizes" the
   core invariant; output is a patch-first, inert proposal with an explicit
   accept/reject/amend gate; the only atom touching canonical Decision History
   (`decision-acceptance`) requires explicit authority and never auto-runs.
2. **docket-triage ambiguity (required reconciliation):** line-review,
   lifecycle-review, and portfolio-review all route to "docket-triage," which was
   never defined. Decided per the brief's recommendation: docket-triage is a
   lightweight Phase-4 intake/triage **atom of decision-review**, not a separate
   workflow. Justified via ROM §13 (it is bounded, mostly-deterministic intake work
   = a task) and DEC-013 (a task atom inherits authority and may not exceed it — so
   it may cluster/route but never propose a DEC-NNN). Documented in a dedicated
   "Relationship to docket-triage (RESOLVED)" section and as a candidate DEC.
3. **Premature decisions:** a single docket item could mint a rule. Fix: a
   decision-worthiness test (recurrence/durability/scope/reversibility/evidence) and
   a `hold_for_recurrence` default that prefers waiting over a premature rule
   (ROM §1, anti-lock-in).
4. **Editing/deleting prior decisions:** supersession could be read as "rewrite."
   Fix: Decision History is append-only (DEC-010); supersession is *proposed* and
   applied by the accept step; entries are never deleted.
5. **Authority inversion via memory:** a Memory Pack lesson could become policy by
   living in the pack. Fix: explicit guard — policy-class lessons arrive here as
   proposals and still face the acceptance gate (ROM §11).

## Pass B — completeness, internal consistency, ROM + locked-workflow alignment

Findings and fixes:
1. **Docket-item shape parity:** confirmed the consumed `governance_docket_item`
   shape matches the one emitted by line-review, lifecycle-review, portfolio-review,
   and line-intake (same fields, only the `why_<source>_cannot_resolve` key varies).
   Intake normalizes `signal_type` → `decision_candidate_type`.
2. **Route closure:** decision-review routes non-decision items back to line-review /
   lifecycle-review / portfolio-review / line-intake — all of which exist. No
   dangling route. The lone genuine gap (the *acceptance authority* step) is
   docketed and held, not improvised.
3. **DEC schema fidelity:** the drafted DEC-NNN proposal uses the exact
   decision-history entry schema (Date/Status/Decision/Reason/Applies to/Supersedes/
   Superseded by/Evidence/Notes) plus a proposal wrapper, marked inert. An accept
   step can paste it in directly.
4. **Closes carried open items:** this design resolves DEC-017's "reconcile
   decision-review with docket-triage" and lifecycle-review Open Question #8. Both
   are now answered in-file; canonization of the resolution is itself offered as a
   candidate DEC (not self-appended).
5. **Lock status:** no lock-gating blocker. Open items (acceptance authority,
   recurrence threshold, docket file location, the docket-triage-record DEC) are
   docketed and covered by the inert/propose-only invariant. Set to v1.0
   LOCK-CANDIDATE.

## Net change v1 → final
Hardened the propose-never-canonize invariant with an explicit acceptance gate and a
single authority-gated acceptance atom; fully reconciled docket-triage as an
inherited-authority intake atom (option a); added the decision-worthiness test and
hold-for-recurrence default; made supersession append-only. No lock-gating blocker.
