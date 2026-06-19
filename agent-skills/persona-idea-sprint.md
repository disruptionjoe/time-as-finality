# Persona Idea Sprint — Reusable Method

## What It Does

Runs the 43-lens sprint selection from `personas/INDEX.md` against the current repo state.
Each persona generates three ideas at increasing ambition tiers. A cross-disciplinary voting
pass then surfaces what's most novel, profound, publishable, and intriguing — with special
attention to where independent disciplines converge on the same structural claim without
coordinating.

## Why It Works

Disciplinary anchoring effects are the main failure mode of single-perspective idea generation.
By running lenses in isolated parallel groups — each group unaware of the others' output —
the method surfaces genuine independent convergences rather than one discipline's idea
dressed up in five vocabularies.

## Method Steps

### 1. Enumerate Lenses

Read `personas/INDEX.md`. The registry is organized into 7 families; the workflow voices 43 selected lenses from these families:

| family | count | source |
|---|---|---|
| Local TaF Lenses | 12 | `## Local Time As Finality Lenses` |
| TaF Crosswalk Lenses | 10 | `### Time As Finality Crosswalk Lenses` |
| Foundational Math Lenses | 10 | `### Foundational Math Lenses` |
| Substrate-Loophole Lenses | 5 | `### Substrate-Loophole Lenses` |
| Computation-Substrate Lenses | 5 | `### Computation-Substrate Lenses` |
| Heterodox Problem-Shape Lenses | 10 | `### Heterodox Problem-Shape Math Lenses` |
| Distributed-Systems Lenses | 6 | `### Distributed-Systems Lenses` |

### 2. Assign to Disciplinary Groups

Split into 5 parallel groups to prevent anchoring:

| group | families included |
|---|---|
| **A – Quantum / Measurement** | Local TaF quantum lenses + Crosswalk quantum lenses + Substrate-Loophole quantum lenses |
| **B – Relativity / Geometry** | Local TaF relativity + Crosswalk relativity + Foundational Math geometry half |
| **C – Math / Formal** | Foundational Math formal half + Heterodox Problem-Shape lenses |
| **D – Computation / Distributed** | Computation-Substrate lenses + Distributed-Systems lenses |
| **E – Conceptual / Critical** | Local TaF analogy + Critical lenses + Crosswalk critical/strategic lenses |

### 3. Idea Generation — Parallel

Each group agent:

1. Reads `personas/INDEX.md` and extracts its assigned lenses with descriptions.
2. Reads the current state of the theory: `ESSAY.md`, `HYPOTHESES.md`, `ROADMAP.md`, `CLAIM-LEDGER.md`, `TESTS.md`.
3. For each persona in its group, voices that lens and generates three ideas:
   - **Useful** — implementable next step the theory clearly needs
   - **Big** — significant leap that would advance the claim class
   - **Wild Swing** — ambitious idea the persona doesn't see anything fundamentally wrong with

Output format per idea:
```
[PERSONA] [TIER]
Title: <5-10 word name>
Claim: <one sentence — what this idea asserts or tests>
Why not wrong: <why this persona doesn't reject it outright>
Deliverable: <most concrete next step to make progress>
```

Groups run fully in parallel. No group sees another group's ideas during generation.

### 4. Synthesis / Voting — Single Agent

One synthesis agent receives all ideas from all groups (full output). It does not know group
assignments. It votes:

- **Most Novel** (top 3) — ideas that don't appear anywhere in the existing repo
- **Most Profound** (top 3) — ideas whose success would most reshape the theory
- **Highest Publishable Potential** (top 3) — ideas closest to a CS or physics venue paper
- **Most Intriguing / Worth a Bet** (top 5) — ideas the synthesis agent would personally investigate

Then it produces a **Cross-Persona Convergence Map**: groups of ideas where independent disciplines,
using different vocabulary and formalisms, arrived at structurally the same claim. These convergences
are the primary output signal — they indicate the theory has a natural attractor in that direction.

### 5. Output Routing

After synthesis, route outputs:

| destination | what goes there |
|---|---|
| `explorations/all-persona-idea-sprint-<DATE>.md` | Full sprint: all 129+ ideas + voting results + convergence map |
| `tests/T<N>-<name>.md` | New test specs for ideas that are implementable as bounded toy models |
| `open-problems/<name>.md` | New open problem specs for ideas that require formal derivation |
| `ROADMAP.md` | Phase entry for any new phase spawned by convergence signals |
| `HYPOTHESES.md` | New Hx entries for any ideas that crystallize into a formal hypothesis |

## How to Invoke as a Workflow

The workflow script is at `agent-skills/persona-idea-sprint.js`.

```bash
# Run against current repo state
Workflow({ scriptPath: 'agent-skills/persona-idea-sprint.js', args: { date: '2026-06-16' } })

# Run with a focus area
Workflow({ scriptPath: 'agent-skills/persona-idea-sprint.js', args: { date: '2026-06-17', focus: 'T13 sheaf cohomology implications' } })
```

## Output Quality Signals

A sprint ran well if:

- At least 2 convergence clusters appear independently across groups
- At least one "Wild Swing" survives the synthesis vote without modification
- The synthesis agent identifies at least one idea it cannot refute from first principles
- No two ideas in the convergence map use identical vocabulary (same words = coordination, not convergence)

A sprint ran poorly if:

- All top-voted ideas were already in ROADMAP.md before the sprint
- Convergence clusters only appear within a single disciplinary group
- The synthesis agent names existing tests as most novel

## History of Runs

| date | trigger | key findings | output file |
|---|---|---|---|
| 2026-06-16 | Initial sprint — full 42-persona pass | 4 convergence clusters: spacetime-from-finality (5 formalisms), phenomenal bridge as incompleteness (5), temporal direction from impossible transformations (6), distributed consensus = physical record formation (8+) | `explorations/all-persona-idea-sprint-2026-06-16.md` |
| 2026-06-16 v2 | Re-run after T13/T16 Cech cohomology + T18 + 6 open problems added | 7 convergence clusters: H1-sheaf underexploited (7 personas, 4 traditions), native impossibility needed (6 personas), phenomenal bridge = complexity separation (7 personas, → T19), D1 reduction maps missing (6 personas), H1-Bell test mapping (5 quantum lenses), distinguishing-predictions table as top documentation gap (6 critical lenses), observer self-reference needs fixed-point treatment (6 personas) | `explorations/all-persona-idea-sprint-2026-06-16-v2.md` |
