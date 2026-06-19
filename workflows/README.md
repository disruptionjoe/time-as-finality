# Workflows

The agentic research operating layer for Time as Finality. Read
[`RESEARCH-OPERATING-MODEL.md`](RESEARCH-OPERATING-MODEL.md) first — it defines
how the program thinks. This README is the structural index.

> **Phase status:** Phase 2 (skeleton). Workflow files are lightweight
> placeholders; behavior is designed in Phase 3 and automated in Phase 4. See
> [`PROJECT-LOG.md`](PROJECT-LOG.md) and
> [`WORKFLOW-SKELETON-PROPOSAL.md`](WORKFLOW-SKELETON-PROPOSAL.md).

## Three families

- **exploit/** — develop the strongest active research lines
  (`advance-primary`, `advance-secondary`, `challenge-primary`, `integrate-results`).
- **explore/** — expand and search the idea landscape
  (`line-discovery`, `line-incubation`, `foundation-ingestion`,
  `cross-disciplinary-synthesis`, `landscape-reassessment`, `persona-expansion`).
- **govern/** — improve the quality, fairness, memory, and allocation of the
  program (`line-review`, `persona-governance`, `research-memory`,
  `lifecycle-review`, `information-portfolio`).

## Registries (current state — source of truth)

- `registries/line-registry.md` — research lines + lifecycle states.
- `registries/persona-clusters.md` — personas mapped into seven discipline clusters.
- `registries/foundation-queue.md` — inbound reading/concept queue.
- `registries/information-portfolio.md` — information-gain ledger.
- `registries/decision-history.md` — constitutional record of major decisions (DEC-NNN).
- `registries/research-line-scorecard.md` — per-line portfolio health signal (governance).

## Logs (history — append-only)

- `logs/runs/` — one record per workflow run.
- `logs/synthesis/` — cross-run synthesis notes.
- `logs/best-next-move/` — the verdict block from each run.

## Conventions

- **Document layout:** files declare a contract (`DOCUMENT-CONTRACT.md`) — Current
  State (edit in place), Historical Record (append), or Operational Log (prepend
  newest-first). Optimize layout for the dominant read pattern.
- **Decisions:** major architectural decisions are recorded in
  `registries/decision-history.md` (DEC-NNN).
- **Authority order:** `RESEARCH-OPERATING-MODEL.md` §11.

## How to run a workflow (Phase 2)

A workflow is markdown-prompt-only for now. An agent: (1) opens the workflow
file, (2) reads the inputs it names (registries + recent logs first), (3) acts,
(4) appends durable outputs and a run log, ending with the verdict block. No
automation or scheduled triggers exist yet (Phase 4).

## Templates

See `templates/` for the workflow placeholder, run log, line card, scorecard,
and best-next-move formats.
