# P33 Run - Cognitive Scientist

- timestamp: 2026-06-21T18:05:15.6142458-05:00
- goal_id: P33
- selected_persona: Cognitive Scientist
- selected_goal: Add salience and abstraction filters to observer access and test whether apparent finality changes while event finality stays fixed.
- bounded_question: Can the repo formalize cognitive observer boundaries as pre-reconstruction filters on accessible records without reviving the renderer/consciousness lane or changing event-finality claims?
- posture: bounded exploratory run only; no claim-status update, roadmap change, or ledger edit.

## Repo Context Read

- `explorations/persona-future-run-goals-2026-06-20.md`
- `personas/EXPERT-PANEL.md`
- `explorations/apparent-vs-event-finality-v0.1.md`
- `tests/T51-multi-observer-apparent-finality-colimit.md`
- `explorations/access-as-record-restriction-invariant-v0.1.md`
- `explorations/cognitive-social-renderer-layer-split.md`
- `tests/T8-observer-renderer-toy-model.md`
- `audits/2026-06-10-repo-audit-and-research-map.md`
- `explorations/persona-goal-runs/2026-06-21-150428-p30-neuroscientist-operational-boundary.md`
- `explorations/research-constellation-orchestrator-2026-06-20.md`

## Bounded Run

I treated the cognitive-science persona as an observer-modeling discipline, not
as a license to reopen consciousness claims.

The useful repo-side pressure is narrower:

```text
physical accessibility is not yet usable observership
```

The current apparent/event split already handles bounded causal access:

- apparent finality depends on accessible records;
- event finality depends on the full finality trace.

P33 asks whether an observer can have the same physically accessible records but
still reconstruct a different apparent-finality order because some records are
ignored, grouped, or treated as below-threshold.

That answer is yes, but only on the apparent side.

## Smallest Honest Formal Object

The clean extension is a filter stack layered on top of the existing access
boundary, not a new ontology.

```text
R_phys(O)          = physically accessible records for observer O
S_{O,T}(R_phys)    = salience filter for observer O and task family T
A_{O,T}(S)         = abstraction / coarse-graining map on the salient records
R_cog(O,T)         = A_{O,T}(S_{O,T}(R_phys(O)))
AF_{O,T}           = apparent finality reconstructed from R_cog(O,T)
EF                 = event finality reconstructed from the full finality trace
```

Interpretation:

- `R_phys(O)` is the existing access-boundary object.
- `S_{O,T}` models attention, relevance, thresholding, or task-gated uptake.
- `A_{O,T}` models abstraction: multiple record distinctions may be collapsed
  into one category before reconstruction.

This keeps the cognitive import typed:

```text
cognitive boundary = pre-reconstruction projection on accessible records
```

not:

```text
mind creates the underlying finality structure
```

## Hostile Witness Shape

Use a fixed T51-style event trace and hold event finality fixed.

Let the observer physically access records witnessing:

- local lock on `e1`;
- local lock on `e2`;
- later composite or revision evidence `e3`;
- one witness that distinguishes "stable local lock" from "still revisable in a
  broader context."

Now compare two cognitive filters on the same `R_phys(O)`:

### Filter F1: fine-grained / witness-preserving

- keeps the revision-sensitive witness salient;
- preserves the distinction between local lock and broader composite support.

Result:

```text
AF_{O,T}(F1) withholds finality or preserves the incomparability
```

### Filter F2: coarse / abstraction-heavy

- discards the revision-sensitive witness as irrelevant or low salience;
- collapses multiple support states into one macro-label such as "already settled."

Result:

```text
AF_{O,T}(F2) upgrades apparent finality
while EF remains unchanged
```

This gives the desired bounded separation:

```text
same event-finality trace
+ same physical access boundary
+ different salience / abstraction filters
-> different apparent finality
```

## Negative Control

To stop this from becoming a free-form psychology story, require one invariance
control:

```text
If S_{O,T} and A_{O,T} preserve all witness-critical record classes and
provenance distinctions needed for the finality verdict, then AF_{O,T} is
unchanged.
```

That is the important discipline rule. The filter only matters when it removes
or collapses verdict-relevant witness structure.

## Relation To Existing Repo Structure

1. This is naturally an apparent-finality refinement, not an event-finality
   revision.
2. It matches the P30 boundary: measurable imports are acceptable only when
   they change reportable observer-side variables rather than metaphysics.
3. It connects to `LossKernel` cleanly:

```text
salience filtering = witness loss by suppression
abstraction filtering = witness loss by quotient / coarse-graining
```

4. It avoids reviving the quarantined renderer language as a core theorem lane.

## Absorber / Demotion Pressure

The neighboring absorber is ordinary cognitive science:

- attention gating;
- relevance filtering;
- category abstraction;
- predictive processing / world-model compression.

So the repo should not claim a new cognitive theory here.

The only potentially useful repo-specific residue is:

```text
these filters can be expressed as typed observer-side projections on the same
record/finality objects already used elsewhere in TaF
```

That is a formal integration result, not a psychology result.

## Result

### Main Verdict

P33 succeeds as a bounded formal refinement:

```text
apparent finality can change under salience and abstraction filters even when
event finality and physical access stay fixed
```

The change belongs to observer-side reconstruction, not to the underlying event
structure.

### Strongest Safe Formulation

```text
Salience and abstraction are typed pre-reconstruction filters on accessible
records. They can change observer-relative apparent finality only by removing
or quotienting verdict-relevant witness structure.
```

### What Does Not Follow

- No consciousness theory is earned.
- No claim that cognition changes event finality is earned.
- No return to "renderer" language in theorem-facing surfaces is recommended.
- No claim-status update is justified from this run alone.

## Smallest Useful Next Step

If Joe wants a follow-on later, the clean next move is a tiny T51 sidecar:

1. hold the event trace and physical access boundary fixed;
2. implement two explicit observer filters `F1` and `F2`;
3. show `AF(F1) != AF(F2)` while `EF` is unchanged; and
4. include the invariance control where witness-preserving filters leave
   apparent finality unchanged.

That would keep the cognitive lane formal, bounded, and falsifiable.

## Claim-Status Posture

- No claim-status changes recommended.
- No roadmap, `TESTS.md`, or `CLAIM-LEDGER.md` changes recommended.
- Positive narrow statement: cognitive observer boundaries can be modeled as
  typed salience and abstraction filters on accessible records.
- Negative narrow statement: current evidence supports only an observer-side
  apparent-finality refinement, not a mind-first or consciousness-facing theory.
