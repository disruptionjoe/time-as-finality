# T214: Capacity-Weighted Refinement Repair Audit

## Target Claims

- T205 continuum / refinement stability audit
- T203/T210 corrected finite `C_flow` model

## Origin

T205 killed unweighted path harmonic as a continuum-stable bridge object because
path multiplicity changed the value. T214 asks whether explicit capacity state
repairs the direction of travel.

## Formal Target

Compare two refinement regimes:

```text
unweighted path list refinement
capacity-aware flow refinement
```

## Setup / Fixtures

Use the T205 hostile pattern:

```text
{1,3} -> {1,1,3}
```

as an unweighted path-list refinement, and compare it against the T210/T213
rule that capacities and incidence must be part of the source object.

## Positive Control

Serial subdivision with total time/capacity preserved should not change the
source network's intended capability.

## Negative Control

Adding listed paths without capacity accounting still changes unweighted
harmonic by representation choice.

## Absorber Pass

Continuum network theory absorbs the repair route through measures,
conductances, capacities, or cross-section weights. The repo has not yet proved
a continuum limit theorem.

## Results

Capacity-aware state points toward a repair, but T214 does not promote a bridge.
It only narrows the refinement lesson:

```text
unweighted path counting is killed;
capacity-aware finite flow is the correct next object;
continuum convergence remains open.
```

## Verdict: narrowed

The refinement repair is narrowed to finite capacity-aware flow, not promoted
to continuum WBE support.

## Falsification Conditions

Promote only with a declared refinement functor, path/capacity measure, and
convergence theorem.

## Next Step

T215 searches for residue outside timing summaries: record/finality capability
at fixed native network state.
