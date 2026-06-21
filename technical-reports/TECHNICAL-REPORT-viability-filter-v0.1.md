# Technical Report: Viability Filter v0.1

## Claim Under Test

The motivating synthesis is:

```text
Geometry may supply the space of possibilities, while finality, maintenance,
and emergence determine which structures remain viable long enough to become
the world experienced by observers.
```

T114 asks whether this can be stated as a falsifiable finite object. The point
is not to defend the slogan. The point is to expose what would have to be true
for it to add anything beyond ordinary geometry, dynamics, thermodynamic
stability, and coarse-graining.

## Artifact

The executable artifact defines:

```text
candidate structure
  -> geometry gate
  -> dynamics gate
  -> maintenance gate
  -> record-finality gate
  -> emergence-platform gate
```

The finality gate determines whether a structure is observer-experienced in
this finite model. The emergence-platform gate is stricter: it asks whether the
finalized structure supports enough downstream operation rights to participate
in further structure formation.

The canonical witness family contains:

- an inconsistent geometry control;
- a geometry-and-dynamics positive case that fails maintenance;
- a maintained case that fails record finality;
- a finalized archive that is not an emergence platform;
- a visible protocol platform that passes all gates;
- a hidden protocol twin matching the visible protocol's geometry, dynamics,
  maintenance, and platform variables, but failing record access.

## Result

The finite filter reaches four separations:

```text
geometry is not sufficient
maintenance is not sufficient
finality is not platform status
record finality can separate a fixed standard-state pair
```

The strongest positive signal is narrow. The visible protocol platform and
hidden protocol twin match on geometry, reachability, repair capacity,
perturbation load, entropy sink capacity, entropy export requirement, stability
window, and platform operation count. They split only because accessible record
support differs across the pre-registered finality threshold.

That is the TaF-specific residue in this toy model. Everything else is ordinary
filtering by consistency, reachability, maintenance, or operation capacity.

## Current Strongest Claim

In this finite witness family, geometry is a possibility space, not a
viability criterion. Structures become observer-experienced only after
reachability, maintenance, and record-finality gates pass; emergence-platform
status is a stricter downstream gate.

## What This Improved

T114 turns the synthesis into a falsifiable filter with negative controls. It
shows exactly where geometry, maintenance, finality, and emergence-platform
capacity can separate without claiming a new law of physics.

It also prevents a common overreach: "geometrically possible" does not mean
"world-experienced," and "record-final" does not mean "emergence platform."

## What This Weakened Or Falsified

This weakens any broad reading of the slogan. The artifact does not show that
geometry, maintenance, finality, and emergence are a new foundation for
physics. It supplies only a finite classification schema.

If future positive cases are already determined by standard maintenance and
thermodynamic accounting, the viability filter is bookkeeping. The current
non-collapse signal is only the fixed-standard-state pair where record access
changes the observer-experienced verdict.

## Falsification Condition

The viability-filter thesis loses independent content if every
observer-experienced or platform verdict is determined by geometry, dynamics,
and standard maintenance variables alone, with no pre-registered record-finality
or operation-right separation.

## Claim Ledger Update

Add T114 only as a North-Star/viability-filter artifact:

```text
Geometry can be treated as a finite possibility space, while maintenance,
record-finality, and emergence-platform gates classify which candidates become
observer-experienced. No core claim is upgraded.
```

## Open Blocker

The current filter is a finite schema, not a derived theorem. It needs a real
domain instantiation where the gates are measured or canonically derived rather
than assigned.

## Next Work

Instantiate the filter on one serious domain, preferably cellular automata or a
D1RestrictionSystem transport case, and test whether the finality/emergence
gates survive after matching standard stability and entropy variables.

## Reproduction

```bash
python -m unittest tests.test_viability_filter -v
python -m models.run_t114
```
