# Valid Coarse-Graining as Finality Admissibility

Open-problem stub, opened 2026-06-30 from the Wolfram Observer Theory reading-set council pass
([explorations/wolfram-observer-theory-reading-set-2026-06-30.md](../explorations/wolfram-observer-theory-reading-set-2026-06-30.md)).
External provocation, not evidence. **Projection != finality** and guardrails **G1/G3** held.

## Problem

Wolfram's Observer Theory makes equivalencing/coarse-graining the fundamental observer operation, then leaves
*open* the question that actually carries the content: **which coarse-grainings are valid?** Wolfram notes
some equivalencings are "computationally ornate" (it would take enormous computation to even recognize two
states as equivalent), and that you can coarse-grain so finely you "become synonymous with the system." He
does not give a criterion for the admissible ones. TaF appears to already have that criterion: a coarse-grain
is admissible iff a **causally bounded observer can actually form and certify the corresponding finalized
record** under D1 (bounded accessible records, bounded reversal cost), passing the T10/T29 selection. Question:
**is TaF's finality-admissibility filter exactly the criterion for a valid coarse-graining that Observer Theory
leaves open?**

## Working Claim (to attack)

The valid coarse-grainings (Wolfram's open slot) are precisely the **bounded-observer-certifiable** ones, and
TaF's D1 + T10/T29 machinery is the criterion. A coarse-graining whose equivalence relation is not computable
within the observer's record/causal budget is *not* a finality the observer can hold; one fine enough to track
microstates is no coarse-graining at all. Finality lives in the admissible band between.

## Why It Might Help

- Converts a vague "we do equivalencing" into a falsifiable criterion: enumerate candidate coarse-grainings on
  a finite model, mark which are bounded-observer-certifiable under D1, and check that exactly those are the
  "valid" ones a bounded observer would use.
- Supplies a concrete distinguishing prediction vs Observer Theory: TaF predicts the *cost/certifiability
  boundary* of valid coarse-grainings; Observer Theory currently does not specify it.

## How It Could Mislead

- "Computationally ornate" (Wolfram) is a computation-cost notion; D1 reversal-cost is "formal only, not
  thermodynamic work by default." Mapping them risks importing a cost model TaF has not committed to. State
  the cost model explicitly before claiming the identification.
- An observer choosing a coarse-graining is not the same as a record finalizing; do not let "valid
  coarse-graining" smuggle in observer-creates-reality (G3). The filter is about what can be *certified*, not
  what is *made true*.

## Connection to Existing Claims and Tests

- [T10: Finality Superselection Rule](../tests/T10-finality-superselection-rule.md)
- [T29: Projection Obstruction Schema](../tests/T29-projection-obstruction-schema.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [unitarity-as-finality-precondition](unitarity-as-finality-precondition.md) (sibling external-provocation note)

## Contribution Needed

On a finite record-graph model, enumerate candidate equivalence relations (coarse-grainings), compute for each
whether it is bounded-observer-certifiable under D1, and test whether that set coincides with the
intuitively-valid coarse-grainings. A clean coincidence is the constructive version of the claim; a mismatch
bounds what TaF's filter actually characterizes. Keep cost-model assumptions explicit.
