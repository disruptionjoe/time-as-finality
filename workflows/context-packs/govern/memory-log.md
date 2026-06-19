---
document_type: operational_log
primary_reader: automation
read_pattern: newest_first
write_pattern: prepend
authority: guidance_only
summarizable: true
scope: govern
---

# Govern Family — Memory Log (raw, summarizer-only)

> **Summarizer-only.** Ordinary agents read `MEMORY.md`, never this file. Only the
> summarizer (owned by `govern/research-memory`) reads here and rolls accepted
> lessons up onto the load surface.

## How this log works

- **Prepend-only, newest-first.** New entries go at the **top**, below the marker.
- **Append after acceptance only.** A consuming workflow appends a single
  **learning-return** entry **after** its output is accepted — not during a run,
  not speculatively.
- **No destructive prune.** "Pruning" means the summarizer summarizes a lesson
  **out of the load surface** — it is **never** deleted from this log on disk.
  History here is permanent.
- **Evidence-grounded, short.** Each entry cites concrete work (`work_ref`,
  `round_ref`); any field may be left blank.
- **`last-summarized` marker.** The summarizer reads down to the marker, then
  drops a fresh marker at the new top. Below the marker is already rolled up.

<!-- last-summarized: (none yet — log is empty) -->

## Learning-return entry template

Copy this block to the top of the log (below the marker) after acceptance:

```yaml
learning_return:
  pack_ref:               # this pack, e.g. context-packs/govern
  work_ref:               # the run / artifact this lesson came from
  round_ref:              # round or pass identifier, if any
  guidance_used:          # which pack guidance was applied this run
  missing_guidance:       # guidance that would have helped but was absent
  confusion_or_conflict:  # any authority/registry conflict (logged, not resolved)
  observed_failure_mode:  # failure mode seen, if any
  output_quality_signal:  # signal on output quality (e.g. accepted/revised/rejected)
  suggested_summary_update: # proposed change to the Current Memory Summary
```

---

_No entries yet — initial build. The log is empty; the summarizer has nothing to
roll up._
