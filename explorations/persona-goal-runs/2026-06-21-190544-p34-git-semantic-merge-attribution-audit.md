# P34 Run - Git Version Control Expert

- timestamp: 2026-06-21T19:05:44-05:00
- goal_id: P34
- selected_persona: Git Version Control Expert
- selected_goal: Build a semantic-merge obstruction where two histories share endpoints and naive loss but differ in attribution, then compare it to LossKernel.
- bounded_question: Does Git supply a concrete same-endpoint path-dependence witness for typed obstruction attribution, or does it collapse under the repo's stricter same-neighbor-data gate?
- posture: bounded exploratory run only; no claim-status update, roadmap change, or ledger edit.

## Repo Context Read

- `explorations/persona-future-run-goals-2026-06-20.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `tests/T30-cross-domain-projection-obstruction-validation.md`
- `tests/T31-po1-admissibility-conditions.md`
- `models/cross_domain_projection_obstruction_validation.py`
- `tests/T99-losskernel-quotient-separation.md`
- `models/losskernel_quotient_separation.py`
- `tests/T127-same-neighbor-data-losskernel-audit.md`
- `models/same_neighbor_data_losskernel_audit.py`
- `claims/TF1-typed-forgetting-attribution.md`

## Work Performed

1. Read the existing Git positive case in `T30/T31` to recover the repo's
   current semantic-merge witness: rename-aware merge succeeds in the richer
   system, while a path-only projection creates a local-to-global obstruction.
2. Read the stricter `T99` and `T127` LossKernel gates to separate three
   questions that are easy to blur:

```text
PO1 positive?
typed attribution witness?
same-neighbor-data separation witness?
```

3. Rebuilt the Git case as a bounded history-attribution audit rather than as a
   claim-promotion exercise.

## Finite Git Witness

Use one base commit `B` and two branches:

- left branch `L`: rename `old_path/report.txt -> new_path/report.txt`;
- right branch `R`: edit the file contents in the pre-rename location;
- merge target `M`.

### Richer history

The merge machinery retains:

- merge-base ancestry;
- rename map `old_path -> new_path`;
- source-line/content correspondence showing that the right-branch edit should
  be applied to the renamed file.

Then the merge has a clean source-side resolution:

```text
apply R's content edit to L's renamed path
```

### Projected history

Forget the rename witness and keep only path-level endpoint data:

- branch endpoints;
- visible file paths at each side;
- naive statement "some rename metadata was lost."

At that projection level, the target sees an ambiguity:

```text
right edit mentions old_path/report.txt
left branch removed old_path/report.txt
target lacks the witness that old_path and new_path are the same file history
```

So Git remains a clean PO1-style example:

```text
richer system: global section exists
projected path-only system: merge obstruction appears
```

## Attribution Split

To make the persona goal hostile, compare two projected histories that share:

- same visible branch endpoints;
- same path-level merge proposition;
- same naive loss description: "rename-related structure not exported to the
  target merge view."

### Case A: attribution-relevant loss

Lost structure includes a source-anchored witness:

- a concrete rename map;
- merge-base identity needed to transport the right-side edit onto the renamed
  file;
- enough lift data to resolve the target obstruction.

Here attribution is legitimate:

```text
the obstruction exists because the projection forgot the witness that
identifies the edited file across the rename
```

### Case B: decorative or non-resolving loss

Keep the same projected endpoint behavior and the same naive "rename metadata"
story, but let the omitted side-data be only decorative or non-resolving, for
example:

- branch color/label metadata;
- author trailer metadata;
- a path tag that does not identify the preimage needed to transport the edit.

Here attribution is not legitimate:

```text
the target obstruction is unchanged, but the omitted data does not resolve it
```

This gives the desired Git-shaped path dependence:

```text
same endpoints
+ same naive loss language
+ different source-side witness content
-> different attribution verdict
```

## Comparison To LossKernel

The comparison is now fairly sharp.

### What survives

`LossKernel` is useful if it names source-anchored witness obligations, not
just labels.

In Git language, the minimally useful typed entry is not:

```text
{"rename_metadata"}
```

but something closer to:

```text
{"rename_map(old_path,new_path)", "merge_base_transport_witness"}
```

because those are the forgotten structures that actually discharge the target
merge ambiguity.

### What collapses

This does **not** currently give a strict same-neighbor-data separation result
for `LossKernel`.

Reason:

- once the richer lift table / rename witness is exposed, mature neighboring
  accounts already distinguish the cases;
- Git provenance, ancestry, and merge-plumbing data are already exactly the
  kind of source-side witness packages that T127 allows neighbors to see.

So the Git case supports the same narrow moral as `T99`, not a stronger one:

```text
label-only loss is too weak;
witness-carrying loss can matter;
but the surviving content still looks like disciplined provenance / witness
 bookkeeping unless a stricter separation theorem is earned
```

## Result

### Main Verdict

P34 succeeds as a bounded hostile audit, but the result is narrower than the
goal's optimistic reading.

Git does provide a familiar, concrete path-dependent attribution witness:

- path-only projection can create a merge obstruction;
- source-anchored rename/merge-base witnesses can legitimately explain it;
- decorative omitted metadata cannot.

But Git does **not** currently rescue `LossKernel` past the repo's stronger
same-neighbor-data gate.

### Strongest Safe Formulation

```text
Semantic merge is a good finite witness that obstruction attribution depends on
which forgotten source-side witness was lost, not merely on endpoint behavior
or naive loss labels. In the current repo posture, this supports witness-aware
audit notation, not prior-art-separated novelty.
```

## Blocker

The blocker is canonical derivation.

The Git witness is easy to state informally, but the attribution-relevant
object is still described at the level of "the rename witness that resolves the
merge." The repo has not yet derived that witness obligation mechanically from
the morphism and the richer/restricted finite systems.

## Proposed Next Action

If Joe wants a follow-on later, the clean next move is a tiny executable Git
sidecar in the `T99` style:

1. encode two Git-path cases with identical projected endpoints and identical
   naive loss labels;
2. represent one with a real source-anchored rename/transport witness and one
   with decorative metadata only;
3. show that label-only attribution collapses while witness-carrying
   attribution distinguishes them; and
4. explicitly test whether any same-neighbor-data quotient survives after the
   rename lift table is exposed.

That would make the Git lesson executable without overpromoting it.

## Claim-Status Posture

- No claim-status changes recommended.
- No roadmap, `TESTS.md`, or `CLAIM-LEDGER.md` changes recommended.
- Positive narrow result: Git semantic merge is a concrete witness for
  path-dependent, source-anchored obstruction attribution.
- Negative narrow result: the witness currently supports provenance-style
  bookkeeping discipline more than a separated `LossKernel` theorem.
