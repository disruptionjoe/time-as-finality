# Time As Finality Steward Context

Status: active. Canonical steward load file adopted 2026-07-01 from the CapacityOS Repo Steward reference architecture. Original steward rollout: RUN-20260630-031.

Load this file when a Kernel directive, RCCM workflow, or direct repo-mounted run targets this repository. Do not load `steward/memory-log.md` by default unless doing stewardship or memory work, or this summary appears incomplete.

## North Star

Advance the Time as Finality program: search for the smallest set of formal principles whose shadows are physics, and let the executable mathematics decide which founding intuitions survive, while keeping the vision aggressive and the research program disciplined.

Change rule: do not change this North Star without very explicit conversation with Joe.

## Long-Term Objectives

- Maintain the aggressive vision in `Vision - North Star.md`.
- Follow the method in `Method - Research Program Guidelines.md`.
- Advance the lead technical line in `Lead Research Line - Time as Finality.md`.
- Keep roadmap, hypotheses, claim ledger, and complexity ledger mutually coherent, and not lagging the test registry (see the Ledger Reconciliation Trigger).

## Measures And Countermeasures

Measures:

- Claims are typed, projections/capabilities are declared, and absorber passes are run.
- Weak residue gets demoted rather than defended.
- Computational-status language is checked against `COMPLEXITY-LEDGER.md`.

Countermeasures / risks:

- No claim, physics, geometry, or novelty upgrade from synthesis alone.
- No promotion without a runnable artifact earning a narrow theorem, separation, or falsifying result.
- Preserve negative results and demotions as progress.

## What This Repo Owns

This repo owns its research truth: claim ledger, formalism, glossary, hypotheses, tests, audits, claims, models, results, governance/guardrails, essays, and explorations.

## What This Repo Must Not Absorb

- CapacityOS architecture, Kernel machinery, RCCM methodology, or JoeOps backlog state.
- Research truth from neighboring repos unless explicitly linked and marked.
- Historical North Star material as active canon without re-ratification.

## Operating Guardrails

- Load the current North Star map before repo work: `Vision - North Star.md`, `Method - Research Program Guidelines.md`, and `Lead Research Line - Time as Finality.md`.
- Contributions follow `CONTRIBUTING.md`.
- Preserve the split: vision can be aggressive; research program cannot.
- Claim-status changes, promotions/demotions, and Canon-Index tier moves are agent-owned once earned by a runnable artifact; a hard promotion (into `theorem_backed`, or asserting a top-line claim as proven/resolved) files an evidence-trail awareness note in `CapacityOS/mailboxes/joeops/` (template `templates/hard-promotion-joeops-notice.md`) — awareness, not approval. Publishing/external decisions and relicensing pause for Joe; nothing enters `papers/published/` before Joe publishes externally. Cross-repo results are proposed via the target surface's mailbox, not executed directly.
- Proposed T-numbers are placeholders until checked against `TESTS.md` and `tests/`.

## Ledger Reconciliation Trigger

The governance ledgers must not silently drift behind the test registry. Mutual
coherence alone does not catch this: the ledgers can be internally consistent while
collectively lagging `TESTS.md` by hundreds of tests, which lets earned or killed
results pile up un-triaged and makes the Canon Index answer as of a stale date.

A **reconciliation pass is due** whenever the highest test in `TESTS.md` exceeds the
highest test tracked in `CLAIM-LEDGER.md` or `COMPLEXITY-LEDGER.md` by more than
**25**. The pass has two separable parts; do the mechanical part unconditionally and
flag the judgment part:

1. **Mechanical (agent-owned, no tier judgment):** relocate any ledger cell over
   ~120 words into the `Test Histories` section (leave a compact disposition in the
   table, per the YAML-compact / narrative-to-body rule); re-stamp the Canon Index
   with the current highest-tracked T and today's date; and, if the frontier is still
   un-triaged, say so in the index rather than letting a stale date imply coverage.
2. **Ratification (agent-owned once earned, but consequential):** triage the new
   results into tiers. Negative results, demotions, and finite-witness moves need no
   note; a hard promotion into `theorem_backed` files the JoeOps awareness note
   (Operating Guardrails, above). Do not fabricate tier movements to close the lag —
   an honest "un-triaged frontier: T_x–T_y" is a valid ledger state.

The trigger fires on drift size, not a clock, consistent with registry-driven (not
arbitrary-cap) discipline.

## Routing

- Research truth stays in this repo.
- CapacityOS architecture questions route to `CapacityOS`.
- JoeOps coordination questions route to `CapacityOS\repos\private\joeops`.
- Durable artifacts belong in `library\repos\public\time-as-finality\`.
- Scratch belongs in `_local/`.

## Candidate Decisions

- Active open claims and tests remain candidate decisions until earned by runnable artifacts and ledger updates.

## Durable Decisions

- This repo is public and CC-BY 4.0.
- The current North Star map supersedes the archived historical `NORTH-STAR.md`.
- The real pause boundary is external publication (publishing/relicensing, and `papers/published/`), not promotion or internal drafting; a hard promotion proceeds under agent ownership but files a JoeOps evidence-trail notice.

## Principles

- Vision is allowed to be aggressive; method is not.
- Executable mathematics decides which founding intuitions survive.
- Negative results and demotions are first-class progress.

## Memory Log

Chronological memory lives at `steward/memory-log.md`. Append useful memory after sessions where this README is loaded.

Lightweight upward-learning pointer: method/workflow-module learnings go to `CapacityOS/mailboxes/rccm/`; kernel-primitive learnings go to `CapacityOS/mailboxes/kernel/`.

## Automation Hooks

Supports CapacityOS-orchestrated and direct repo-mounted runs. Automations are thin triggers; RCCM workflow plus this steward context supply the repo-local operation.

## Local Source References

- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `ROADMAP.md`
- `HYPOTHESES.md`
- `CLAIM-LEDGER.md`
- `COMPLEXITY-LEDGER.md`
- `CONTRIBUTING.md`
- `TESTS.md`
- `tests/`
