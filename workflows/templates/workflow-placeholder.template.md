---
document_type: workflow
primary_reader: automation
read_pattern: current_state
write_pattern: edit_in_place
authority: canonical
summarizable: false
---

# <Workflow Name>

**Family:** exploit | explore | govern
**Mode:** search | evaluation | both
**Status:** Phase 3 design — protocol level.

## Purpose
What this workflow is for (governance meaning).

## Authority boundaries
- **May:** ...
- **Must not:** ... (esp. actions reserved to other surfaces, e.g. lifecycle moves)
- **Scoring authority:** deterministic | hybrid | judgment-with-rationale
- **Write authority:** patch-first | direct (name which fields)

## Read surfaces
Registries, logs, repo artifacts, personas, and the Memory Pack load surface it
reads first.

## Write surfaces
What it writes or proposes (patch vs direct), and where.

## Memory interface (Phase 3.5; may be inert)
- Reads (load surface): ...
- Writes (learning-return): ...
- Does not depend on memory existing.

## Registry interactions
Which registries are read and/or written, and how.

## Outputs (shapes)
- Report: ...
- Patch: ...
- Docket / candidates: ...
Every run ends with the verdict block.

## Escalation triggers
What conditions route out, and to where.

## Failure modes
How this workflow can go wrong, and the guard for each.

## Success criteria
What a good run produces and how you would know it helped.

## Future automation decomposition notes
*Advisory; Phase 4 formalizes. Task atoms inherit this workflow's authority and
never exceed it (DEC-013).*

Likely execution atoms:
- <task atom 1>
- <task atom 2>

Likely cadence differences:
- <runs often> / <on events> / <periodic> / <after accumulated signals>

Likely context boundaries:
- <what each task loads> / <precompiled into a context pack> / <not loaded unless triggered>

Likely deterministic vs judgment split:
- Deterministic:
- Judgment-based:

Phase 4 coverage questions:
- Does every output have a downstream consumer?
- Does every registry write have an owning task?
- Does every escalation signal have a destination?
- Does every scheduled task have a bounded object?
- Is anything reviewed twice by competing tasks?
- Is any unit too large for one agent run?

## Verdict block
```text
Candidate best next move:
Reason:
Evidence:
Risks:
What would change this recommendation:
```
