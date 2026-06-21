---
document_type: exploration_report
workflow: workflows/explore/research-constellation-orchestrator.md
status: non_canonical_exploration
authority: report_only
timestamp: 2026-06-20T17:03:33-05:00
---

# Research Constellation Orchestrator - Maintenance Arrow Run

**Date:** 2026-06-20 17:03:33 America/Chicago
**Workflow:** `workflows/explore/research-constellation-orchestrator.md`
**Status:** Non-canonical exploration artifact
**Authority caveat:** This report proposes directions only. It does not update
claim status, `CLAIM-LEDGER.md`, `ROADMAP.md`, test status, line registries,
persona registries, automation schedules, workflow triggers, or canonical
research-line state.

## Run Parameters

```yaml
scope: focused constellation
room_count: 1
room_derivation_mode: user_provided
room_topics:
  - maintenance cost of structure as an alternative arrow-of-time direction
room_seed_text_visible_to_room: true
requested_output:
  - strongest version
  - weakest point
  - closest prior art
  - possible formalization
  - potential tests
  - reasons it may fail
  - reasons it may be important
```

## Room Seed Text

The room received the user's supplied research prompt before round 1. The
prompt asked whether the post-T110 arrow-of-time direction should shift from:

```text
Where does entropy increase come from?
```

to:

```text
What pays the cost of maintaining structure against collapse?
```

Core seed claims visible to the room:

```text
closed + bounded + reversible + finite systems do not appear capable of
generating a strict monotone arrow on their own.

The obvious next move is open systems, entropy production, Markov processes,
coarse-graining, and standard thermodynamic approaches.

Candidate alternative:
collapse is the default tendency; the interesting phenomenon is the existence
of structures that remain viable despite collapse pressure.

Examples: life, language, institutions, civilizations, scientific communities,
markets, observers, consciousness, record systems.

Working chain:
maintenance -> persistence -> emergence window -> higher-order structure
-> additional maintenance requirements

Or:
record maintenance -> viability -> finality -> emergence -> further structure
formation

Potential reinterpretations:
- reconstruction debt becomes maintenance obligation;
- lost structure becomes repair burden;
- finality becomes maintained viability;
- emergence becomes a partial solution to maintenance costs;
- collapse becomes underfunded maintenance.
```

The room was explicitly told not to assume the idea is correct and to test
whether it is distinct from thermodynamics, entropy production, open-system
physics, evolutionary dynamics, ecological resilience, commons governance,
cybernetics, control theory, active inference, free-energy principles,
thermodynamics, and information theory.

## Repository Context Read

- `workflows/explore/research-constellation-orchestrator.md`: current workflow
  authority, one-room default, three-round discussion requirement, report-only
  boundary.
- `agent-skills/time-as-finality-persona-panel/SKILL.md`: independent persona
  critique and conservative synthesis discipline.
- `claims/H7-finality-induced-direction.md`: H7 is now partially supported only
  as a conditional constructor theorem or open-system/resource-accounting
  claim.
- `TECHNICAL-REPORT-reversible-finality-nonmonotonicity-v0.1.md`: T80 shows
  reversible local dynamics do not automatically satisfy D1 monotonicity.
- `TECHNICAL-REPORT-bounded-sink-reversible-compression-v0.1.md`: T106 shows a
  bounded reversible sink gives only a forward-branch accounting curve; the
  closed cycle kills the monotone.
- `TECHNICAL-REPORT-finite-permutation-monotone-obstruction-v0.1.md`: T110
  proves the finite closed reversible scalar-monotone obstruction.
- `TECHNICAL-REPORT-viability-filter-v0.1.md` and `tests/T114-viability-filter.md`:
  maintenance, record-finality, and emergence-platform gates already exist as a
  finite North-Star schema with negative controls.
- `explorations/persona-goal-runs/2026-06-20-143930-p96-reconstruction-debt-spine-formalist.md`:
  reconstruction debt as unmet admissible witness obligations.
- `explorations/evolutionary-game-commons-rbt-evaluation-2026-06-20.md`:
  viability under maintenance cost, institutional finality, and finality as a
  public good.
- `explorations/persona-goal-runs/2026-06-20-164448-p08-quantum-information-operational-crosswalk.md`:
  reversal cost must be task-based and independently measured.
- `NORTH-STAR.md`: viability filter refinement and guardrails against
  overclaiming.

## External Prior-Art Pointers Consulted

These were used only for orientation and prior-art pressure, not for claim
promotion:

- Free Energy Principle / active inference overview: https://pmc.ncbi.nlm.nih.gov/articles/PMC9141822/
- Friston free-energy brain theory review copy: https://www.uab.edu/medicine/cinl/images/KFriston_FreeEnergy_BrainTheory.pdf
- Ostrom, *Governing the Commons* accessible copy: https://www.actu-environnement.com/media/pdf/ostrom_1990.pdf
- Holling, "Resilience and Stability of Ecological Systems" copy: https://pure.iiasa.ac.at/id/eprint/26/1/RP-73-003.pdf
- Annual Reviews page for Holling 1973: https://www.annualreviews.org/content/journals/10.1146/annurev.es.04.110173.000245

## Room Framing

```yaml
room:
  name: Maintenance Cost And Observer-Viable Direction
  research_direction: >
    Determine whether "maintenance cost of structure" is a genuinely distinct
    post-T110 arrow-of-time research direction, or whether it collapses to
    standard entropy production, open-system thermodynamics, control theory,
    active inference, resilience, and commons governance.
  seed_text_visible_to_room: true
  why_this_direction_now: >
    T110 blocks strict scalar arrows inside finite closed reversible systems.
    T114 already frames maintenance and record-finality as viability gates.
    The open question is whether maintenance cost can sharpen H7 and
    reconstruction debt without becoming a synonym for dissipation or control
    cost.
  relevant_repo_context:
    - H7 post-T80/T106/T110 weakening
    - T114 viability filter
    - P96 reconstruction debt spine
    - evolutionary/game/commons maintenance evaluation
    - P08 task-based reversal-cost guardrail
```

## Persona Assignment

| Persona | Cluster or role | Why selected |
| --- | --- | --- |
| P01 Mathematical Physicist | physics/decoherence | Tests whether maintenance language adds anything beyond thermodynamics and open systems. |
| P08 Quantum Information Theorist | physics/decoherence | Pressures entropy, channels, erasure, recovery maps, and task-based reversal cost. |
| P16 Dynamical Systems Expert | simulation/dynamics | Grounds collapse, attractors, recurrence, stability, and basin structure. |
| P21 Complex Systems Scientist | simulation/complex systems | Evaluates emergence windows and platform effects in adaptive networks. |
| P22 Information Theorist | information/networking | Tests whether reconstruction debt is coding cost, rate-distortion, or side information. |
| P23 Resource Theory Researcher | math/formalism | Looks for maintenance monotones, convertibility, and resource accounting. |
| P24 Constructor Theory Researcher | math/formalism | Reframes maintenance as possible/impossible transformations and constructor reliability. |
| P25 Philosopher Of Physics | philosophy/testability | Separates explanatory reorientation from physical novelty. |
| P28 Evolutionary Biologist | biology/selection | Evaluates maintenance, reproduction, heredity, and future-structure capacity. |
| P35 Database Systems Architect | distributed-systems | Grounds record maintenance, compaction, audit, repair, and provenance debt. |
| P42 Poet / Literary Scholar | philosophy/metaphor pressure | Tests whether "collapse" and "maintenance" are metaphorically overextended. |
| P44 Ecologist | biology/resilience | Brings resilience, disturbance, adaptive cycles, and under-maintenance collapse. |
| P50 Scientific Skeptic | philosophy/testability | Demands falsification and prior-art separation. |
| P52 Mathematical Minimalist | math/formalism | Compresses the idea to the smallest object and rejects decorative terminology. |
| P54 Experimentalist | physics/test design | Forces finite executable tests and measurement boundaries. |

Persona exclusivity is satisfied because this run has one room.

## Round 1 - Divergence

**P01 Mathematical Physicist:** The T110 result is decisive in its finite
domain: closed bounded reversible dynamics cannot supply a strict scalar arrow.
The maintenance framing is not an alternative to thermodynamics if it means
"someone exports entropy." It becomes interesting only if it identifies which
subsystems can remain record-bearing under an explicitly paid resource budget.

**P08 Quantum Information Theorist:** Maintenance must be task-indexed. A record
is not maintained in the abstract; a channel, code, memory, or witness is
maintained for a recovery, discrimination, or verification task. If the model
does not specify a recovery map and an independent resource meter, it will
collapse to the same reversal-cost placeholder that P08 already rejected.

**P16 Dynamical Systems Expert:** "Collapse" is too broad. Systems do not
necessarily collapse; they recur, drift, enter attractors, fragment basins, or
move between metastable states. The clean formal candidate is not collapse
pressure but viability under perturbation: which states remain inside a
constraint set under allowed controls and disturbances?

**P21 Complex Systems Scientist:** The idea is strongest in its platform form.
Many structures matter because they lower the cost of future structure: a
language, institution, genome, archive, or market is a scaffold that changes
the next search space. Maintenance cost is not only survival cost; it is the
cost of keeping an emergence platform operational.

**P22 Information Theorist:** Reconstruction debt sounds like missing side
information. Maintenance obligation sounds like repeatedly paying to preserve
side information or tolerate its loss. This is probably close to coding theory,
rate-distortion, channel capacity, and refresh costs. The repo needs a case
where equal entropy or code length has unequal finality because of observer
access or admissibility.

**P23 Resource Theory Researcher:** A useful direction would define a resource:
maintainable structure under allowed operations. The monotone would not be
entropy itself; it could be minimum maintenance resource needed to keep a
structure in a viability set for horizon `h`. But this must be compared against
standard nonequilibrium free energy and thermodynamic resource theories.

**P24 Constructor Theory Researcher:** Maintenance is a constructor problem.
Which transformations remain possible after repeated use? A structure is
viable if a constructor can keep producing the transformation it is supposed to
produce, despite degradation. That matches the seed's "structure capable of
producing future structure."

**P25 Philosopher Of Physics:** The question "what pays the cost?" is
explanatorily valuable even if it is not physically fundamental. It shifts
attention from global entropy increase to the conditions of persistence for
observers and records. But calling it a better arrow of time would be too
strong unless it yields new constraints or predictions.

**P28 Evolutionary Biologist:** Life is not merely maintained; it reproduces
maintenance capacity. The chain should include inheritance and selection:
maintenance -> persistence -> reproduction of maintenance protocol ->
evolvability. Structures that beget future structure are lineages and niches,
not just stable objects.

**P35 Database Systems Architect:** The record-system analogue is concrete:
logs rot, indexes drift, schemas migrate, backups need verification, and
audits cost money. Finality is never free; it is a maintained service-level
property. But this is standard operations engineering unless the repo shows a
new observer-relative separation.

**P42 Poet / Literary Scholar:** "Collapse is the default tendency" is powerful
but dangerous. It risks becoming a universal metaphor: everything is falling
apart unless maintained. The phrase should be replaced with explicit failure
modes: decay, drift, corruption, loss of witness, loss of authority, loss of
interpretability.

**P44 Ecologist:** Ecological resilience is the nearest home. Systems persist
by absorbing disturbance, reorganizing, and keeping functions inside bounds.
The repo should not treat maintenance as holding a state fixed. Often the
maintained object is function, not configuration.

**P50 Scientific Skeptic:** The idea is probably not distinct from known
frameworks unless it finds a residual after matching entropy export, stability,
control effort, free-energy minimization, and resilience variables. T114 already
states that failure condition. Use it.

**P52 Mathematical Minimalist:** Strip the prose to:

```text
Given a finite transition system with disturbance, repair action, budget, and
target task, compute whether a record-bearing structure stays in a viability
set and whether it supports downstream tasks.
```

Everything else is commentary until this object separates cases.

**P54 Experimentalist:** The smallest test should be finite and adversarial:
two systems with matched entropy production and matched persistence time, but
different record-maintenance/access protocols. If finality or downstream
emergence differs, there is a TaF-relevant residue.

## Round 2 - Convergence

**P01 Mathematical Physicist:** P54's matched-standard-variable demand is the
right guardrail. Maintenance is allowed as a research direction only if the
model first declares the ordinary thermodynamic variables it is matching or
using.

**P08 Quantum Information Theorist:** P22 and P54 imply the same packet shape:
state, channel, task, recovery operation, side information, and resource meter.
If "record maintenance" is real, it must change recovery or discrimination
success under a fixed channel summary.

**P16 Dynamical Systems Expert:** P44 corrected the collapse language. The
formal model should not assume every unattended system goes to disorder. It
should define disturbances and viability constraints. Collapse then means exit
from the task-relevant viability set.

**P21 Complex Systems Scientist:** P28's lineage point improves the platform
idea. The higher-order structure is not merely a structure that survives; it is
a structure that maintains or reproduces the process by which future structures
become possible.

**P22 Information Theorist:** The clean distinction from entropy could be
observer-indexed side information. Two encodings can have the same information
quantity but differ in who can verify, refresh, or use them under admissibility
constraints.

**P23 Resource Theory Researcher:** The resource-theory version should name
free operations: unattended evolution, bounded repair, copying, audit, erasure,
fresh-capacity import, and authority validation. Maintenance cost becomes the
least non-free resource needed to keep a task available for horizon `h`.

**P24 Constructor Theory Researcher:** The room is converging on "viable
constructor capacity." A maintained record is one that keeps a future
transformation possible. This naturally connects finality to emergence:
finalized records become constructors or inputs for further constructors.

**P25 Philosopher Of Physics:** The strongest philosophical version is not
"maintenance is more fundamental than entropy." It is "entropy production is
not the whole explanatory object for observers, because observer-relevant
structure is selected by maintainability, accessibility, and task use."

**P28 Evolutionary Biologist:** The model needs a reproduction or recurrence
axis. A single maintained object is not life-like. A platform has to affect the
production of successor platforms, otherwise the "structure begets structure"
claim is under-modeled.

**P35 Database Systems Architect:** P23's free operations map cleanly onto
database operations: compaction, backup, checksums, migration, access control,
audit, conflict resolution. The finite model can be a record store with
disturbance and repair policies.

**P42 Poet / Literary Scholar:** "Underfunded maintenance" is a good phrase for
social systems but not for all physics. Keep it for institutions and record
systems; use neutral "unpaid repair obligation" or "insufficient repair budget"
in mathematical contexts.

**P44 Ecologist:** The room should preserve the idea that too much finality can
be maladaptive. Maintenance can create rigidity. An emergence platform that
cannot reorganize may be brittle.

**P50 Scientific Skeptic:** The failure criteria are now obvious: if every
positive case is selected by standard entropy/free-energy/control/resilience
quantities, the direction is a rephrasing. If the only residual is post hoc
"observer importance," demote it.

**P52 Mathematical Minimalist:** The smallest object is a finite controlled
Markov/transition system with two scores:

```text
standard_score = entropy/export/stability/control variables
taf_score = accessible record-finality + downstream operation rights
```

The test is whether matched `standard_score` can split `taf_score`.

**P54 Experimentalist:** The test should include negative controls:
maintenance without finality, finality without platform capacity, platform
capacity without observer access, and high entropy export without record
maintenance.

## Round 3 - Reflection And Judgment

**P01 Mathematical Physicist:** Most important: do not present this as a
replacement for entropy production. Present it as a post-T110 open-system
resource-accounting route that may expose observer-relevant distinctions.

**P08 Quantum Information Theorist:** The next model must make reversal cost and
maintenance cost task-based. Otherwise the quantum/information-theory critique
will absorb it immediately.

**P16 Dynamical Systems Expert:** Define collapse as exit from a viability set,
not as entropy increase. That makes the idea mathematically testable.

**P21 Complex Systems Scientist:** The promising concept is platform viability:
structures are important when their maintained operation widens or stabilizes
future structure formation.

**P22 Information Theorist:** The likely novelty, if any, is not information
quantity. It is admissible access to side information needed for future tasks.

**P23 Resource Theory Researcher:** Maintenance cost can be a useful resource
monotone candidate, but only after free operations and non-free resources are
declared.

**P24 Constructor Theory Researcher:** Formalize structures as constructors or
constructor-supporting substrates. A structure persists if its transformation
role remains possible under degradation and repair.

**P25 Philosopher Of Physics:** The idea is distinct as explanatory framing,
not yet as physics. It may help reinterpret finality and observer persistence
without claiming a new thermodynamic arrow.

**P28 Evolutionary Biologist:** Include reproduction of maintenance protocols
or niche construction. Otherwise "life" and "civilization" examples are being
used without their central mechanism.

**P35 Database Systems Architect:** The database/record-store toy model is
probably the fastest executable path: logs, audits, corruption, repair budget,
and downstream query rights.

**P42 Poet / Literary Scholar:** The room improved the language. Avoid
"collapse" as a universal metaphysical default; name failure modes.

**P44 Ecologist:** Preserve adaptive reorganization. Maintenance is not always
state preservation; it can be function preservation through structural change.

**P50 Scientific Skeptic:** This is useful only if it generates a finite test
that could fail. T114 already supplies the failure condition: collapse into
standard variables.

**P52 Mathematical Minimalist:** Candidate theorem shape:

```text
If two finite systems are matched on standard persistence and entropy/export
variables but differ in accessible witness maintenance, then observer-finality
or platform status may split.
```

That is not a theorem yet, but it is the smallest useful target.

**P54 Experimentalist:** Immediate next action: instantiate T114 on a finite
record-maintenance model with matched entropy/control variables and explicit
negative controls.

## Room Synthesis

```yaml
room_synthesis:
  strongest_insight: >
    The candidate is strongest when stated as observer- and task-indexed
    maintenance of record-bearing structure under disturbance, not as a
    replacement for entropy production.
  most_novel_insight: >
    "Structure that begets structure" can be formalized as maintained platform
    capacity: a structure matters if it preserves or enlarges downstream
    operation rights for future structure formation.
  most_profound_implication: >
    Finality may be interpretable as an affordable-maintenance verdict:
    a record is final for an observer/task when the remaining reconstruction
    and repair obligations are bounded enough for future use.
  most_actionable_next_direction: >
    Build a finite record-maintenance viability model that matches ordinary
    entropy/export/stability/control variables while varying accessible
    record-maintenance and downstream operation rights.
  additional_promising_directions:
    - viability kernel for record maintenance
    - resource theory of maintenance obligations
    - constructor-capacity view of emergence platforms
    - commons-governance model of record finality as public good
    - evolutionary model of maintenance-protocol reproduction
  major_disagreements:
    - whether "collapse pressure" is a good primitive or misleading metaphor
    - whether maintenance cost is ever more fundamental than entropy production
    - whether social/institutional examples are analogies or core cases
  areas_of_uncertainty:
    - whether any finite witness can survive T114's prior-art collapse condition
    - how to measure maintenance cost without choosing it post hoc
    - whether observer access adds an independent split after standard variables are matched
  confidence_assessments:
    direction_as_exploration_lens: 0.78
    direction_as_new_physics: 0.12
    finite_model_value: 0.72
    prior_art_separation: 0.31
  minority_viewpoints_to_preserve:
    - Too much finality can reduce adaptability.
    - Maintenance may preserve function, not state.
    - Social "underfunded maintenance" language should not be exported into physics unchanged.
    - The direction may be entirely absorbed by free energy, control, and resilience theory.
```

## Orchestrator Contextual Judgment

This was a one-room run, so the synthesis is compared against current repo
context rather than against other rooms.

### What Changed After Discussion

Before the room, the idea could be read as:

```text
entropy increase is not the key; maintenance against collapse is the key.
```

After the room, the safer and stronger version is:

```text
After T110, H7's remaining physical route must be open-system/resource
accounting. Maintenance cost is a candidate observer/task-indexed resource
that may explain which record-bearing structures remain viable and become
platforms for future structure, but only if it separates from standard entropy,
free-energy, control, and resilience variables.
```

That is a narrower claim and a better executable target.

### Strongest Version

The strongest version is not:

```text
maintenance cost is more fundamental than entropy production.
```

The strongest version is:

```text
For observer-bearing systems, the relevant directional structure is the
ongoing resource expenditure required to keep records, witnesses, and
constructors inside a viability set long enough to support future operations.
Entropy production is one physical accounting layer; maintenance cost is the
task- and observer-indexed accounting layer that decides which structures
remain usable, final, and platform-forming.
```

### Weakest Point

The weakest point is prior-art absorption. Standard frameworks already cover
large parts of the idea:

- nonequilibrium thermodynamics and stochastic thermodynamics cover entropy
  export and dissipation;
- control theory covers maintaining a state or function under disturbance;
- viability theory covers staying inside constraint sets;
- free-energy / active inference covers self-maintaining adaptive systems that
  resist disorder by acting to maintain expected states;
- ecological resilience covers persistence of function under disturbance;
- cybernetics covers regulation and feedback;
- information theory covers side information, coding cost, error correction,
  and refresh;
- commons governance covers monitoring, sanctioning, repair, and institutional
  maintenance costs.

The idea fails as independent content if it cannot produce a matched-standard
variable split where record-finality or platform capacity differs.

### Closest Prior Art

| Framework | Relation | Absorption risk |
| --- | --- | --- |
| Nonequilibrium / stochastic thermodynamics | Physical cost of maintaining nonequilibrium structure | Very high |
| Thermodynamic resource theories | Free operations, work, heat, nonequilibrium resources | High |
| Control theory / cybernetics | Feedback and regulation under disturbance | High |
| Viability theory | Constraint sets, controls, disturbances, viability kernels | High |
| Active inference / Free Energy Principle | Adaptive systems maintain expected states by minimizing variational free energy | High |
| Autopoiesis | Living systems as self-producing/self-maintaining organization | Medium-high |
| Ecological resilience / panarchy | Persistence, adaptation, reorganization, disturbance response | High for ecology cases |
| Evolutionary dynamics | Maintenance, reproduction, inheritance, fitness, evolvability | High for life cases |
| Commons governance / Ostrom | Monitoring, repair, sanctions, shared-resource maintenance | High for institutional cases |
| Information theory / coding | Error correction, side information, refresh, rate-distortion | High for record cases |
| Databases / distributed systems | Logs, repair, replication, consistency, audit | High for engineered record systems |

The possible TaF delta is not "maintenance exists." It is:

```text
maintenance cost of accessible record-finality and downstream operation rights,
after ordinary stability and thermodynamic variables are matched.
```

### Possible Formalization

Start with a finite object:

```text
MaintenanceViabilityCase =
  states
  transition_rule
  disturbance_rule
  repair_actions
  repair_budget
  entropy_or_cost_meter
  record_access_map
  witness_requirements
  reconstruction_debt_budget
  downstream_operation_rights
  viability_set
  horizon
```

Derived quantities:

```text
standard_cost = entropy_export + control_effort + stability_window
maintenance_cost = minimum repair/audit/refresh resource to keep task viable
record_finality = accessible witnesses discharge reconstruction debt
platform_status = downstream operation rights above threshold
collapse = exit from viability_set, not generic disorder
```

Minimal theorem target:

```text
Matched-standard split:
There exist finite systems A and B with equal standard_cost and equal
state-persistence window, but different record_finality or platform_status
because accessible witness maintenance differs.
```

Minimal negative theorem target:

```text
If record_access_map and downstream_operation_rights are functions only of
standard_cost and viability_set membership, then maintenance-finality adds no
independent classification.
```

### Potential Tests

1. **Finite record-store model.** Records decay or corrupt; repair actions cost
   budget; audit logs can be maintained or allowed to rot; downstream queries
   require admissible witnesses. Compare cases matched on entropy/control
   proxy but split by accessible witness maintenance.
2. **Matched platform twins.** Two structures have the same geometry,
   reachability, repair capacity, perturbation load, entropy sink, and
   stability window. One maintains accessible records needed for downstream
   operation rights; the other does not.
3. **Maintenance without finality negative control.** A system is energetically
   maintained but cannot discharge reconstruction debt for an observer/task.
4. **Finality without platform negative control.** A record is stable and
   accessible but supports too few downstream operations to count as a platform.
5. **High entropy export without useful maintenance.** A system spends energy
   but fails the task-relevant viability set.
6. **Adaptive reorganization case.** A system changes state representation but
   preserves function and record-finality under disturbance.

### Reasons It May Fail

- Maintenance cost is fully captured by free energy, control effort, or entropy
  export.
- Reconstruction debt reduces to ordinary side-information or coding cost.
- "Finality as maintained viability" becomes a post hoc label for stable states.
- The model assigns platform status after seeing the desired conclusion.
- Observer access does not split any matched-standard-state pair.
- Social and cognitive examples remain analogies and do not transfer back to
  physical H7.
- "Collapse" stays too metaphorical unless failure modes are explicitly named.

### Reasons It May Be Important

- It offers a disciplined post-T110 direction without pretending closed
  reversible systems generate arrows.
- It connects H7, T114, reconstruction debt, commons governance, and observer
  persistence through one finite audit object.
- It may explain why record-bearing structures matter: they are maintained
  platforms for future operations, not merely low-entropy configurations.
- It turns "debt" into a future cost or repair obligation, which is more
  operational than "lost information."
- It sharpens emergence: emergence is not just macro-pattern formation; it is
  platform capacity under maintenance constraints.
- It gives consciousness-stack questions a safer form: memory, attention,
  self-model, and social reconciliation are maintenance protocols, not
  metaphysical primitives.

## Route Consequences

```yaml
candidate_route:
  primary: explore/line-discovery
  secondary: exploit/advance-secondary
  reason: >
    The idea is a candidate research direction with a clear finite-probe shape,
    but it should not update H7 or D1 until a model separates from standard
    thermodynamics/control/resilience variables.
suggested_artifact:
  type: executable finite audit
  tentative_name: T### Maintenance-Cost Viability Split
  related_existing_anchor: T114 viability filter
canonical_updates: none
```

## Proposed Next Concrete Artifact

Build:

```text
T###: Maintenance-Cost Viability Split
```

Minimum model:

```text
CandidateStructure:
  id
  state_sequence
  disturbance_sequence
  repair_policy
  repair_budget
  entropy_export_proxy
  control_effort_proxy
  stability_window
  record_access_support
  required_witnesses
  maintained_witnesses
  reconstruction_debt
  downstream_operation_rights
```

Required cases:

| Case | Purpose |
| --- | --- |
| standard_positive | ordinary maintained structure passes standard stability and finality |
| no_maintenance | geometry/dynamics pass but maintenance fails |
| maintenance_no_finality | maintenance passes but required witnesses are inaccessible |
| finality_no_platform | finality passes but downstream operation rights fail |
| matched_standard_split | standard variables match, record maintenance splits observer-finality/platform verdict |
| entropy_export_decoy | high cost/entropy export without useful record maintenance |
| adaptive_reorganization | state changes but function and record-finality remain viable |

Pass condition:

```text
At least one matched-standard pair must split only on accessible witness
maintenance or downstream operation rights, and all negative controls must
block overbroad "maintenance explains everything" readings.
```

Fail condition:

```text
If all verdicts are determined by entropy_export_proxy, control_effort_proxy,
stability_window, and ordinary viability_set membership, demote the direction
to a T114 explanatory lens over standard frameworks.
```

## Explicit Non-Actions

- No claim status updated.
- No `CLAIM-LEDGER.md`, `ROADMAP.md`, `TESTS.md`, registry, schedule, trigger,
  or workflow file updated.
- No H7 promotion.
- No assertion that maintenance cost replaces entropy production.
- No claim that consciousness, institutions, or life prove a physical arrow.

## Verdict Block

```text
Candidate best next move:
Build a finite Maintenance-Cost Viability Split audit as a T114-adjacent
executable model.

Reason:
T110 blocks strict scalar arrows in finite closed reversible systems, while T114
already provides the gate structure needed to test maintenance, record-finality,
and emergence-platform separations. The maintenance-arrow idea is promising
only if it can split matched standard thermodynamic/control/resilience cases.

Evidence:
T80/T106/T110 force H7 toward open-system/resource accounting. P96 frames
reconstruction debt as unmet witness obligations. The commons/evolutionary run
identified under-modeled maintenance, repair, monitoring, and incentive costs.
T114 already states the relevant failure condition and supplies a finite schema.

Risks:
The direction may collapse completely into entropy production, free-energy
minimization, control theory, viability theory, resilience, coding theory, or
commons governance. "Collapse" and "maintenance" can become metaphors unless
the finite model names failure modes and cost meters.

What would change this recommendation:
If the next finite model cannot produce a matched-standard-variable split, keep
maintenance cost as a North-Star/T114 vocabulary only. If it does produce a
split, route the result to `exploit/advance-secondary` for a stricter prior-art
comparison against thermodynamics, control, active inference, and resilience.
```
