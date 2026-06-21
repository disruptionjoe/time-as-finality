---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: patch_proposal
authority: canonical_workflow
output_authority: compression_report_and_legibility_proposal
summarizable: false
unit_of_review: one_theory_slice
---

# Theory Compression Engine

**Family:** govern
**Mode:** both
**Status:** Phase 3 extension - v0.1 workflow proposal. Not yet mapped into the
Phase 4 automation scaffold.
**Consumes:** a large but bounded theory slice, line registry context, and recent
synthesis/challenge outputs.
**Emits:** compression candidates, shared-core analysis, decompression test
results, and legibility or refactoring proposals.

## Purpose

Reduce repo complexity without deleting insight. The workflow asks: what is the
smallest set of claims, definitions, or mechanisms that explains most of the
selected corpus?

It uses multiple compression pressures: mathematical, philosophical, and
intelligent-outsider compression. A decompression test then checks whether the
compressed theory can regenerate the same live research tasks. Compression is
useful only if it preserves generative structure.

This is a govern workflow because it improves project legibility, allocation,
and belief discipline. It does not decide which claims are true.

## Authority boundaries

- **May:** select a bounded corpus slice; produce multiple compressed versions;
  compare shared core; run a decompression test; propose documentation cleanup,
  glossary clarification, or line-portfolio restructuring; route candidates to
  owning workflows.
- **Must not:** delete artifacts; collapse research lines; replace the North
  Star; rewrite claim statuses; treat the shortest compression as best; hide
  minority interpretations; turn a compression into canon without acceptance.
- **Scoring authority:** hybrid. Deterministic for coverage counts and task
  regeneration overlap; judgment-based for explanatory adequacy and lost
  structure.
- **Write authority:** direct write for compression reports; patch-first for
  proposed documentation, registry, or glossary edits.

## Read surfaces

- Selected theory slice: one or more of `claims/`, `tests/`, `models/`,
  `technical-reports/`, `papers/`, `explorations/`, `open-problems/`.
- `CLAIM-LEDGER.md`, `HYPOTHESES.md`, `ROADMAP.md`, `TESTS.md`.
- `Vision - North Star.md`, `Method - Research Program Guidelines.md`,
  `Lead Research Line - Time as Finality.md`, `FORMALISM.md`, `GLOSSARY.md`.
- Workflow registries, recent synthesis logs, line registry, decision history.
- Govern Memory Pack load surface if present.

## Write surfaces

- Compression report under `workflows/logs/synthesis/` or `explorations/`.
- Candidate essence summary, explicitly non-canonical until accepted.
- Decompression test result.
- Patch proposals for docs/registry/glossary only when earned.
- Docket items for unresolved compression conflicts.

## Memory interface (Phase 3.5; may be inert)

- Reads: previous compression attempts, known lossy summaries, repeated
  outsider-confusion points, compression failures.
- Writes: `guidance_used`, `missing_guidance`, `confusion_or_conflict`,
  `observed_failure_mode`, `output_quality_signal`, `suggested_summary_update`.
- Does not depend on memory existing.

## Registry interactions

- **Reads:** line registry and scorecard to understand which lines the slice
  supports; information portfolio for information-gain preservation.
- **Writes:** no direct registry writes. Structural proposals route to
  `govern/portfolio-review`; line additions route to `explore/line-discovery` and
  `govern/line-intake`.

## Procedure

1. **Choose the theory slice.** State which corpus region is being compressed and
   why.
2. **Build three independent compressions.**
   - mathematical compression;
   - philosophical compression;
   - intelligent-outsider compression.
3. **Compare shared core.** Identify claims, mechanisms, and terms that appear in
   all three compressions.
4. **Identify lost structure.** Record what each compression drops and whether the
   loss matters for live work.
5. **Run decompression test.** A fresh pass receives only the compressed theory
   and generates research tasks. Compare generated tasks to existing live
   directions.
6. **Classify compression quality.**
   - `strong_compression`
   - `useful_but_lossy`
   - `legible_summary_only`
   - `overcompressed`
   - `failed`
7. **Route consequences.** Documentation edits, glossary candidates, line
   restructuring, or no-change outcomes route to owning workflows.

## Outputs

**Compression candidate:**

```yaml
compression_candidate:
  compression_lens: mathematical | philosophical | outsider
  compressed_theory:
  claims_preserved:
  mechanisms_preserved:
  tasks_regenerated:
  structure_lost:
  risk:
```

**Decompression test:**

```yaml
decompression_test:
  compressed_input:
  generated_tasks:
  overlap_with_live_directions:
  missing_live_directions:
  spurious_new_directions:
  compression_quality:
```

Every run ends with the verdict block.

## Escalation triggers

Route to `govern/portfolio-review` when compression implies merge/split/overlap;
to `govern/line-review` when it changes standing evidence; to
`explore/line-discovery` when decompression generates a novel line; to
`exploit/contradiction-hunter` when the compression exposes a claim that cannot
be preserved without circularity; to `govern/decision-review` when the repo needs
a new compression policy or canonical summary decision.

## Failure modes

- **Archive compression.** The workflow summarizes everything but explains
  nothing. Guard: require shared core and decompression test.
- **Insight loss.** Compression destroys the generative machinery. Guard:
  generated tasks must overlap live directions.
- **Majority erasure.** Minority research programs vanish from the compressed
  core. Guard: record lost structure and survival arguments.
- **Canonization by summary.** A convenient compression becomes truth. Guard:
  compression output is non-canonical until accepted.
- **Aesthetic minimalism.** Shortest summary wins. Guard: score by regenerative
  power, not brevity.

## Success criteria

A good run yields a compact theory statement that preserves most of the slice's
live tasks, clearly names what it loses, and produces actionable cleanup or
portfolio recommendations without rewriting authority surfaces.

Cheap auditability test: a reviewer can see what all compressions agree on, what
was lost, and whether the decompression test regenerates important work.

## Future automation decomposition notes

*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- `govern/compression-slice-select` - choose bounded corpus.
- `govern/compression-pass` - one compression lens.
- `govern/compression-core-compare` - shared core and loss analysis.
- `govern/compression-decompression-test` - regenerate tasks from compression.
- `govern/compression-route` - package recommendations.

Likely cadence differences:
- Periodic after major artifact accumulation.
- Event-triggered when the repo becomes hard to navigate or line overlap grows.

Likely context boundaries:
- Compression passes load the selected slice only.
- Decompression loads only the compressed theory.
- Routing loads workflow catalog and registry.

Likely deterministic vs judgment split:
- Deterministic: artifact list, overlap counts, route existence.
- Judgment-based: explanatory adequacy, lost-structure severity, core essence.

Phase 4 coverage questions:
- Does every compression state what it lost?
- Does every decompression test produce comparable tasks?
- Does every cleanup recommendation have an owner?
- Are minority programs preserved as minority programs when not in the core?

## Verdict block

```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```
