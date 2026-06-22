---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: bridge_memo_and_test_proposal
summarizable: false
unit_of_review: one_bridge_question
---

# Cross-Repo Bridge Builder

**Family:** explore
**Mode:** search
**Status:** Phase 3 extension - v0.1 workflow proposal. Not yet mapped into the
Phase 4 automation scaffold.
**Consumes:** Time as Finality plus one or more neighboring repo/context packets.
**Emits:** bridge memo with shared structure, false analogy, and a bridge test.

## Purpose

Compare Time as Finality, Architecture of Legitimacy, GU Formalization, and other
neighboring ecosystems by operations rather than vocabulary. The workflow asks:
where are these projects independently solving the same abstract problem?

It does not merge projects, import authority, or declare one mega-theory. Its
output is a bridge memo that separates genuine shared structure from tempting
false analogy and proposes one artifact that would test the bridge.

## Authority boundaries

- **May:** read explicitly provided neighboring repo context; extract core
  operations from each ecosystem; compare operation-level structures; write a
  bridge memo; propose one bridge experiment or artifact; route new research
  lines to `explore/line-discovery`.
- **Must not:** merge repo roadmaps; import claim status from another repo; edit
  external repos unless explicitly asked; treat similar vocabulary as evidence;
  collapse project identities; use a bridge as physics or legitimacy evidence.
- **Scoring authority:** judgment-with-rationale over operation equivalence,
  analogy risk, and testability.
- **Write authority:** direct write for bridge memos; patch-first for any proposed
  repo-facing doc updates.

## Read surfaces

- TaF core: North Star, Method, Lead Research Line, claim/test/model surfaces,
  workflow registry and recent synthesis logs.
- Neighboring context supplied by the user or available locally, usually:
  Architecture of Legitimacy, GU Formalization, or an exported context memo.
- `GLOSSARY.md`, `FORMALISM.md`, and relevant technical reports.
- Explore Memory Pack load surface if present.

## Write surfaces

- Bridge memo under `explorations/` or `workflows/logs/synthesis/`.
- Candidate bridge experiment routed to the owning workflow.
- Candidate research line routed to `explore/line-discovery`.
- False-analogy guardrail notes routed to `govern/decision-review` only if they
  need policy.

## Memory interface (Phase 3.5; may be inert)

- Reads: prior bridge attempts, false analogy records, successful operation-level
  correspondences, external-context caveats.
- Writes: `guidance_used`, `missing_guidance`, `confusion_or_conflict`,
  `observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** line registry for TaF ownership and overlap; decision history for
  authority constraints.
- **Writes:** none directly. Bridge-born candidates route through discovery and
  intake.

## Procedure

1. **Declare bridge question.** Name the repos/ecosystems and the suspected shared
   problem.
2. **Extract operations independently.** For each ecosystem, produce a list of
   core operations without importing the other projects' vocabulary.
3. **Compare operations, not words.** Identify possible matches such as record
   finality, valid settlement, audit trails, transport, symmetry, invariance,
   reconstruction, or admissibility.
4. **Separate bridge classes.**
   - `genuine_shared_structure`
   - `tempting_false_analogy`
   - `unclear_requires_test`
5. **Design one bridge test.** The test should produce an artifact, not a slogan:
   a crosswalk table, finite fixture, obstruction, theorem sketch, or negative
   control.
6. **Route consequences and emit memo.**

## Outputs

**Bridge memo:**

```markdown
# Cross-Repo Bridge Memo
## Question
## Ecosystems Compared
## Core Operations By Ecosystem
## Genuine Shared Structure
## Tempting But False Analogy
## Unclear Bridge Requiring Test
## One Bridge Experiment Or Artifact
## Routes And Owners
```

**Bridge candidate:**

```yaml
bridge_candidate:
  shared_operation:
  taf_expression:
  neighbor_expression:
  equivalence_basis:
  false_analogy_risk:
  bridge_test:
  owner_workflow:
```

Every run ends with the verdict block.

## Escalation triggers

Route to `explore/cross-disciplinary-synthesis` when the bridge is really a
multi-discipline convergence; to `explore/line-discovery` for new research lines;
to `govern/portfolio-review` if a bridge implies line merge/split/overlap; to
`exploit/contradiction-hunter` if the bridge exposes an overclaim; to
`govern/decision-review` if cross-repo authority rules are unclear.

## Failure modes

- **Vocabulary bridge.** Similar terms are treated as shared structure. Guard:
  extract operations independently.
- **Mega-theory collapse.** Projects are merged into one vague frame. Guard:
  bridge memo must include false analogies.
- **Authority import.** Another repo's confidence becomes TaF evidence. Guard:
  bridge outputs are exploratory only.
- **No test.** The memo ends as a conceptual comparison. Guard: require one
  experiment or artifact.
- **External context drift.** Neighboring repo context is stale or incomplete.
  Guard: state source and date of external context.

## Success criteria

A good run produces a bridge memo where a reviewer can tell what is genuinely
shared, what is only tempting, and what one artifact would decide whether the
bridge is useful.

Cheap auditability test: every proposed bridge names operations on both sides,
not just vocabulary, and includes a negative-control analogy.

## Governance review gate

This workflow remains valid only if each run passes all five checks:

- **Stopping condition:** stop after one declared bridge question has operation
  tables, false-analogy analysis, and exactly one proposed bridge test.
- **Bounded artifact:** emit one bridge memo plus one bridge candidate or test
  artifact proposal.
- **Success vs noise:** success is an operation-level correspondence with a
  negative control; noise is shared vocabulary, prestige transfer, or a broad
  megatheory frame.
- **Overclaim protection:** bridges are exploratory and must not import claim
  status, physics evidence, legitimacy evidence, or roadmap authority from
  another repo.
- **Claim-weakening ability:** every bridge must include a false-analogy or
  demotion path stating when the comparison collapses to metaphor.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `explore/bridge-context-load` - load TaF and supplied neighbor context.
- `explore/bridge-operation-extract` - one ecosystem -> operation list.
- `explore/bridge-compare` - operation match and false analogy classification.
- `explore/bridge-test-design` - one artifact/test proposal.
- `explore/bridge-route` - package memo and route outputs.

Likely cadence differences:
- Event-triggered when Joe supplies a neighboring repo/context.
- Slow periodic run for known adjacent ecosystems.

Likely context boundaries:
- Operation extraction agents each load only one ecosystem.
- Comparison loads only extracted operation tables.

Likely deterministic vs judgment split:
- Deterministic: context provenance, route-target existence, memo packaging.
- Judgment-based: operation equivalence, analogy risk, bridge-test design.

Phase 4 coverage questions:
- Is external context fresh enough?
- Does every bridge include false-analogy analysis?
- Does every bridge have exactly one proposed test artifact?
- Are external repo authority boundaries preserved?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```
