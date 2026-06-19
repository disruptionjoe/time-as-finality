---
document_type: registry
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: canonical
summarizable: false
---

# Line Registry

The **portfolio / grouping layer** for the program. It answers five questions and
nothing else:

1. what research lines exist,
2. what lifecycle stage each is in,
3. what artifacts belong to it,
4. why it is primary / secondary / incubating / archived,
5. what the next candidate move is.

> **Status authority — read this.** This registry does **not** record claim,
> roadmap, or hypothesis status. Those live on their authoritative surfaces and
> are never restated here (to avoid drift):
> - **Claim status ->** `CLAIM-LEDGER.md`
> - **Roadmap / test-completion status ->** `ROADMAP.md`
> - **Hypothesis status ->** `HYPOTHESES.md`
> - **Tests / results / open problems ->** `tests/`, `results/`, `open-problems/`
>
> A research line is a *named grouping* of that work. The registry links out to
> it; the linked surfaces remain authoritative. If this file and an authoritative
> surface disagree on status, the authoritative surface wins and the discrepancy
> is logged (never silently reconciled).

> **Seed note.** Lifecycle stages below are an initial reading of current repo
> state, to be confirmed by the first `line-review` / `lifecycle-review` runs.
> "Research line" = a distinct line of inquiry; unrelated to git branches.

**Lifecycle:** `seed -> explored -> validated -> incubated -> secondary-exploit -> primary-exploit -> integrated / archived`

### Relationship fields (optional)

Each line may declare relationships to **other research lines** (not files), so
governance can eventually reason over a research *graph* instead of an isolated
list:

```yaml
depends_on:    # lines this line needs to be true/working
supports:      # lines this line strengthens
competes_with: # lines that contend for the same role (e.g. primary)
extends:       # lines this line generalizes or builds upon
imports:       # lines whose machinery this line reuses
```

Only non-empty relationships are listed per line. `lifecycle-review` and
`line-review` maintain these.

---

## RL-001 — Observer-relative temporal reconstruction via finite finality descent
- **Stage:** primary-exploit · **Mode bias:** evaluation
- **Why this stage:** current best formalization path; broad cross-cluster
  legitimacy; the live frontier (T47->T55).
- **Artifacts:** `tests/` T47-T55; `results/` finali-event-structure,
  multi-observer colimit, observer-colimit descent boundary, finite-finality
  descent theorem, conflict-finalievent descent; `models/` corresponding modules.
- **Maps to (authoritative):** claims C1, D1 -> `CLAIM-LEDGER.md`; phase entries ->
  `ROADMAP.md`; relevant Hx -> `HYPOTHESES.md`.
- **Relationships:** competes_with RL-002; depends_on RL-004.
- **Next candidate move:** *(set by line-review / advance-primary; not yet run.)*

## RL-002 — Projection-Obstruction schema (PO1)
- **Stage:** secondary-exploit · **Mode bias:** evaluation
- **Why this stage:** broad cross-domain support; PO1 has accumulated
  mathematical independence; candidate to challenge RL-001 for primary.
- **Artifacts:** `tests/` T29-T35; `results/` PO1 schema, admissibility
  conditions + derivation, foundational derivation, chained projection, discovery
  engine.
- **Maps to (authoritative):** claim PO1 -> `CLAIM-LEDGER.md`; -> `ROADMAP.md`,
  `HYPOTHESES.md` (H0-H5 matrix).
- **Relationships:** competes_with RL-001; supports RL-001.
- **Next candidate move:** *(pending challenge-primary / line-review.)*

## RL-003 — Distributed-systems / consensus finality crosswalk
- **Stage:** incubated · **Mode bias:** both
- **Why this stage:** strong specialist (distributed-systems cluster) support;
  tests theorem-transfer between consensus and physical record finality.
- **Artifacts:** `tests/` T17, T20, T28; `results/` consensus-finality crosswalk,
  consensus-record theorem transfer, CAP bridge.
- **Maps to (authoritative):** claims A1, S1 -> `CLAIM-LEDGER.md`; -> `ROADMAP.md`.
- **Relationships:** supports RL-001.
- **Next candidate move:** *(pending line-incubation / line-review.)*

## RL-004 — Typed transport & multiscale transport category
- **Stage:** incubated · **Mode bias:** evaluation
- **Why this stage:** categorical backbone connecting restriction systems; feeds
  RL-001/RL-002.
- **Artifacts:** `tests/` T37-T41; `results/` typed transport network, minimal
  multiscale transport, typed transport category.
- **Maps to (authoritative):** -> `CLAIM-LEDGER.md`, `ROADMAP.md`.
- **Relationships:** supports RL-001, RL-002.
- **Next candidate move:** *(pending line-review.)*

## RL-005 — Local persistence & mechanism identifiability
- **Stage:** explored · **Mode bias:** both
- **Why this stage:** separates local accumulation from record-access lag; H4 best
  supported so far.
- **Artifacts:** `tests/` T42-T45; `results/` local persistence reconciliation
  split, persistence mechanisms, mechanism identifiability.
- **Maps to (authoritative):** -> `HYPOTHESES.md` (H4), `CLAIM-LEDGER.md`.
- **Relationships:** supports RL-001.
- **Next candidate move:** *(pending line-incubation.)*

## RL-006 — Compression-finality crosswalk  *(archived)*
- **Stage:** archived · **Mode bias:** evaluation
- **Why this stage:** archived **with information gain** — compressibility is a
  downstream observable of stable records, not a D1 dimension (Rule 30 / Rule 0
  counterexamples across all 256 ECA rules). Information-gain entry recorded in
  `information-portfolio.md`.
- **Artifacts:** `tests/` T36; `results/` compression-finality crosswalk.
- **Maps to (authoritative):** -> `CLAIM-LEDGER.md` (negative result).
- **Relationships:** — (archived; informed RL-001 definitions).
- **Revival condition:** a compression measure that is not record-derivative.

---

## How this registry is maintained

- `explore/line-discovery`, `cross-disciplinary-synthesis` add seeds.
- `explore/line-incubation` advances early-lifecycle lines.
- `exploit/*` advances, challenges, integrates active lines.
- `govern/line-review` re-scores and reconciles standing; `govern/lifecycle-review`
  applies promotion/demotion/archival and adjudicates survival arguments.
- Status of individual claims/tests/hypotheses is **never** edited here — only on
  the authoritative surfaces named above.
