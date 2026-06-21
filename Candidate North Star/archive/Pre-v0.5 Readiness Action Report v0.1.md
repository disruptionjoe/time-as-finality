# Pre-v0.5 Readiness Action Report v0.1

## Status

Fresh readiness review of `Candidate North Star v0.4.md` against:

```text
Candidate North Star Next Version Update Queue v0.5.md
Pre-v0.5 Review Report v0.1.md
the low-hanging formal/editorial/physics patch reports
the math, physics, database, and prior-art companion reports
```

Reviewer:

```text
Codex GPT-5, 2026-06-20
```

This is not canon.
It does not draft v0.5.
It is an action report on what should be done before the next version.

## Bottom Line

`Candidate North Star v0.4.md` is structurally sound enough to be treated as
the v0.5 baseline. The next version should be a tight patch release, not a
restructure.

Before drafting v0.5, the queue should absorb:

1. five small main-note patches;
2. three companion-report or appendix tasks;
3. two navigation/posture checks;
4. one source-hygiene pass for raw deep-research reports.

The core formal spine is already in good shape:

```text
projection sufficiency for typed capability objects
factorization through X / ~=_X
declared capability equivalence ~=_K
fiber-constancy
minimal capability-preserving quotient
trivial enrichment control
absorber-first residue discipline
known physics -> induced Cap -> projection sufficiency audit
```

Do not expand v0.5 back toward v0.3. Patch the sharp edges and keep the main
note compact.

## Sound Enough To Leave Alone

These areas do not need main-note expansion before v0.5:

- Quotient formalism: v0.4 correctly factors through `X / ~=_X` and carries
  the `~=_K` equivalence caveat.
- Prior-art posture: the opening already says the bare idea is old and frames
  the project as an audit surface.
- Failure labels: the current labels are distinguishable enough in normal
  review use; no distinction table is needed unless future reviews produce
  real confusion.
- Residue ladder: the canonical/formal/translation/heuristic/demoted ladder is
  adequate. A one-word cleanup from "immediate" to "tested" in the formal
  residue paragraph would reduce ambiguity but is not structurally important.
- Physics direction: v0.4 correctly uses the no-free-physics posture. Physics
  examples should remain induced-capability audits, not claims that Capability
  Projection derives physics.

## Main-Note Patches Before v0.5

### M1. Add the default-equality guardrail

Issue:

```text
same payload
same current value
```

can still be read as acceptable default equality unless the note says otherwise
plainly.

Smallest patch:

```text
The default equality relation is not "same payload" or "same current value."
Equality must be declared by the audit context.
```

Placement:

```text
Formal Core, immediately after ~=_X is introduced.
```

Source support:

```text
Queue Q10
Pre-v0.5 Review Report v0.1
Database Absorption Test
```

### M2. Add approximate-equivalence to the reviewer checklist

Issue:

Approximate retrieval, vector search, probabilistic systems, time-series
rollups, and workload-sensitive systems often have the wrong bar if exact
equality is the only visible checklist option.

Smallest patch:

```text
if approximate: epsilon/probabilistic/top-k/recall@k/latency-recall/workload
equivalence declared?
```

Placement:

```text
Reviewer Checklist.
```

Source support:

```text
Queue Q7
Database Absorption Test
20 Mathematics Perspectives Report
```

### M3. Replace the flat appendix map with a burden table

Issue:

The document strategy depends on companion reports, but the current appendix
map is a filename list. A fresh reviewer cannot tell which report carries which
burden.

Smallest patch:

```text
Report | Burden carried
```

with rows for:

- schema/audit template;
- database absorption;
- broad prior-art absorption;
- mathematical strengthening;
- 20 math perspectives;
- 20 physics perspectives;
- low-hanging dispatch synthesis;
- fresh-eye review;
- pre-v0.5 review reports.

Placement:

```text
Appendix Map.
```

Source support:

```text
Queue Q3
Pre-v0.5 Review Report v0.1
```

### M4. Add a domain-calibration gate sentence

Issue:

The domain calibration section is correct but can still be misread as domain
examples confirming novelty. It should say explicitly that domain sections are
pressure tests.

Smallest patch:

```text
Domain sections are calibration gates, not novelty evidence. Strong absorption
is expected; the question is whether any formal or canonical residue survives
after the domain's native state, equivalence, and absorber theory are allowed.
```

Placement:

```text
Start of Domain Calibration.
```

Source support:

```text
Queue Q4
Database Expert Lens Review
Prior-Art Audit
```

### M5. Add a per-witness falsifiability line

Issue:

v0.4 has program-level failure criteria, but individual witnesses need a
quick fail condition.

Smallest patch:

```text
A proposed witness fails if a mature absorber supplies a natural sufficient
enrichment or quotient under the declared audit context.
```

Placement:

```text
Reviewer Checklist, Residue Ladder preamble, or Failure Criteria.
```

Source support:

```text
Queue Q12
Pre-v0.5 Review Report v0.1
Prior-Art Audit
```

## Companion Or Appendix Work Before Drafting

### C1. Add one worked demotion example outside the main note

The main note probably does need one example somewhere in the v0.5 bundle, but
not in the main body.

Best candidate:

```text
database/event-log, database/vector retrieval, or detector provenance
```

Required shape:

- fill the audit fields;
- show the same-visible-state claim;
- run the fiber/spread test;
- name the native absorber;
- apply enrichment;
- demote honestly to translation or heuristic residue.

Purpose:

```text
show the audit preventing overclaim
```

not:

```text
promote a flagship novelty witness
```

### C2. Add one filled physics witness template outside the main note

The no-free-physics template is already present. A filled example would help
reviewers see how a physics witness works without turning v0.5 into a physics
essay.

Best candidates:

```text
GR causal accessibility
quantum resource theory under explicit access
detector/instrumentation provenance
EFT/RG preservation control
```

The example must end with an absorber and residue verdict. It should not claim
physics-bearing novelty.

### C3. Put the database equality checklist in a companion report or appendix

The main note should keep `same-visible-state context fixed?` as the compact
gate. The expanded database checklist belongs in support material:

```text
schema
constraints
view/query language
transaction/isolation context
snapshot/log position
provenance or lineage regime
index/materialization context
access policy
consistency model
approximation tolerance
workload
budget
```

This is especially important if the worked example uses a database or retrieval
case.

## Navigation And Posture Tasks

### N1. Clarify the root `Candidate North Star.md`

The folder contains both:

```text
Candidate North Star.md
Candidate North Star v0.4.md
```

The root file reads like an older physics-forward draft. Before v0.5, add a
short status note or update the folder `Readme.md` so fresh reviewers know:

```text
v0.4 is the current baseline;
Candidate North Star.md is historical / superseded / pre-v0.4 unless named
otherwise.
```

This is navigation hygiene, not a content demotion.

### N2. Posture-check the physics companion reports

Some physics companion material predates the locked v0.4 stance. Before v0.5,
scan:

```text
Candidate North Star 20 Physics Perspectives Report v0.1.md
Strongman for physics sections.md
Prior Art And Physics Grounding For Capability Projection - Deep Research.md
```

Add a header note if any section can be read as:

```text
Cap -> known physics
dark matter/dark energy as more than heuristic
local observer credited with inaccessible global capability
```

The goal is not to rewrite the reports. It is to prevent a companion artifact
from weakening the main note's no-free-physics posture.

## Source-Hygiene Pass

The deep-research reports are useful but not clean appendix material yet. They
contain citation placeholders and encoding artifacts such as mojibake in
mathematical symbols and punctuation.

Before the appendix map asks those reports to carry major burden, do one of:

1. clean citations and encoding in the linked reports;
2. add a header note marking them as raw research memos with citation cleanup
   pending.

This should not block a narrow v0.5 draft if the main note remains clean. It
does matter before presenting the companion bundle as polished review material.

## Recommended Execution Order

1. Apply M1-M5 to `Candidate North Star v0.4.md`.
2. Add or designate the C1/C2 companion examples and C3 database checklist.
3. Add explicit queue entries for N1, N2, and source hygiene if the queue is
   meant to track every pre-v0.5 task.
4. Do one final fresh-eye pass focused only on overclaim, appendix navigation,
   and whether the five patches stayed compact.
5. Draft v0.5 as a patch release.

## Do Not Do Before v0.5

- Do not expand the main note into a long absorber inventory.
- Do not add a new flagship physics claim.
- Do not promote dark matter or dark energy beyond typed tests or heuristic
  analogies.
- Do not call finite non-factorization pairs canonical residue.
- Do not replace TaF's current North Star posture.
- Do not treat companion reports with raw citation artifacts as polished
  appendices without a warning or cleanup.

## Readiness Verdict

```text
Main note: ready for small v0.5 patch after M1-M5.
Companion bundle: needs C1-C3 plus N1-N2 before it is easy for fresh reviewers.
Source bundle: usable internally, but needs citation/encoding cleanup or header
warnings before it should be treated as polished support.
Overall: proceed with a compact v0.5 patch, not a restructure.
```
