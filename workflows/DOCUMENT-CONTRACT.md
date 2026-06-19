---
document_type: specification
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: canonical
summarizable: false
---

# Document Contract

A Document Contract is a short front-matter block at the top of a significant
file that tells an agent **how to use the file** — who reads it, in what order,
how it is written, how much authority it carries — instead of forcing the agent
to infer all of that.

It operationalizes the governance guideline (operating model §12): *optimize a
document's layout for its dominant consumption pattern, not its write pattern.*

## The three document classes

```text
Current State
    ↳ edit in place        (read to know what is true now)

Historical Record
    ↳ append chronologically   (searched by item; stable references matter)

Operational Log
    ↳ prepend newest first     (read recent-first; readers stop after recent entries)
```

The class determines the default `read_pattern` and `write_pattern`, but the
contract states them explicitly so exceptions are legible.

## Front-matter schema

Place at the very top of the file, as YAML front-matter:

```yaml
document_type:   # e.g. operational_log | historical_record | registry | specification | workflow | memory_pack
primary_reader:  # automation | governance | human | mixed
read_pattern:    # newest_first | chronological | current_state
write_pattern:   # prepend | append | edit_in_place
authority:       # canonical | historical_only | guidance_only | none
summarizable:    # true | false   (may a summarizer roll this up?)
```

### Field vocabulary

- **document_type** — what kind of artifact this is. The three layout classes map
  to: operational_log, historical_record, and the current-state types
  (`registry`, `specification`, `workflow`, `memory_pack`, …).
- **primary_reader** — who the layout should be optimized for. `automation` (an
  agent reading at run time), `governance` (govern workflows), `human` (Joe), or
  `mixed`.
- **read_pattern** — `newest_first` (operational logs), `chronological`
  (historical records), `current_state` (registries/specs read as a whole).
- **write_pattern** — `prepend`, `append`, or `edit_in_place`.
- **authority** — where the file sits in the authority order (operating model
  §11): `canonical` (a real authority surface), `historical_only` (records, no
  forward authority), `guidance_only` (memory packs), `none`.
- **summarizable** — whether a summarizer (memory layer, Phase 3.5) may roll its
  contents up onto a load surface. Operational logs are typically `true`;
  canonical surfaces are typically `false`.

## Examples

Operational log (e.g. a memory log):

```yaml
document_type: operational_log
primary_reader: automation
read_pattern: newest_first
write_pattern: prepend
authority: historical_only
summarizable: true
```

Registry (current state):

```yaml
document_type: registry
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: canonical
summarizable: false
```

Historical record (e.g. decision history):

```yaml
document_type: historical_record
primary_reader: mixed
read_pattern: chronological
write_pattern: append
authority: historical_only
summarizable: false
```

## Rollout

This is a guideline, not a gate. Contracts are added incrementally — exemplars
first (this file, the decision history, the line registry, the project log),
then the rest as a `govern/research-memory` housekeeping task. A file without a
contract is not broken; it simply hasn't declared its pattern yet.

## Relationship to authority

A Document Contract describes *how to read/write* a file; it does **not** grant
authority. Authority is fixed by operating model §11. A file may declare
`authority: canonical` only if it genuinely is a canonical surface there.
