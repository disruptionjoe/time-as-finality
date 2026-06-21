# T114 Results: Viability Filter

## Strongest claim

In this finite witness family, geometry is a possibility space, not a viability criterion. Structures become observer-experienced only after reachability, maintenance, and record-finality gates pass; emergence-platform status is a stricter downstream gate.

## Aggregate checks

- Geometry not sufficient: `True`
- Maintenance not sufficient: `True`
- Finality not platform: `True`
- Finality separates fixed standard state: `True`
- Observer-experienced cases: `['finalized_archive_not_platform', 'visible_protocol_platform']`
- Emergence-platform cases: `['visible_protocol_platform']`

## Candidate table

| Candidate | First failed gate | Observer-experienced | Platform | Interpretation |
| --- | --- | --- | --- | --- |
| `impossible_tiling` | `geometry` | `False` | `False` | Geometry rejects the candidate before viability is meaningful. |
| `geometric_but_unmaintained_seed` | `maintenance` | `False` | `False` | Geometrically admissible and reachable, but the preservation stack cannot maintain it long enough. |
| `maintained_but_unfinalized_wave` | `finality` | `False` | `False` | Maintenance succeeds, but bounded observers lack enough records to reconstruct it as a settled structure. |
| `finalized_archive_not_platform` | `emergence_platform` | `True` | `False` | The structure is stable and reconstructable, but it does not support enough downstream operations to be an emergence platform. |
| `visible_protocol_platform` | `None` | `True` | `True` | Same standard maintenance state as the archive case, but enough operation rights remain for recursive emergence. |
| `hidden_protocol_twin` | `finality` | `False` | `False` | A fixed-standard-state control: geometry, dynamics, maintenance, and platform operations match the positive protocol case, but record access is below threshold. |

## Gate traces

### impossible_tiling

- `geometry`: `False` - finite constraints are inconsistent
- `dynamics`: `False` - candidate is not reachable from allowed initial states
- `maintenance`: `False` - stability window 0 < required 1
- `finality`: `False` - accessible records 0 < threshold 1
- `emergence_platform`: `False` - structure is reconstructable but not a platform for further emergence

### geometric_but_unmaintained_seed

- `geometry`: `True` - finite constraints are mutually satisfiable
- `dynamics`: `True` - candidate is reachable under the declared transition rule
- `maintenance`: `False` - repair capacity 2 < load 4; entropy sink capacity 2 < required 3; stability window 5 < required 8
- `finality`: `False` - record threshold and reconstruction-debt budget both pass
- `emergence_platform`: `False` - structure supports enough downstream operations for platform status

### maintained_but_unfinalized_wave

- `geometry`: `True` - finite constraints are mutually satisfiable
- `dynamics`: `True` - candidate is reachable under the declared transition rule
- `maintenance`: `True` - repair, entropy export, and stability-window constraints all pass
- `finality`: `False` - accessible records 1 < threshold 3; reconstruction debt 3 > budget 1
- `emergence_platform`: `False` - structure supports enough downstream operations for platform status

### finalized_archive_not_platform

- `geometry`: `True` - finite constraints are mutually satisfiable
- `dynamics`: `True` - candidate is reachable under the declared transition rule
- `maintenance`: `True` - repair, entropy export, and stability-window constraints all pass
- `finality`: `True` - record threshold and reconstruction-debt budget both pass
- `emergence_platform`: `False` - structure is reconstructable but not a platform for further emergence

### visible_protocol_platform

- `geometry`: `True` - finite constraints are mutually satisfiable
- `dynamics`: `True` - candidate is reachable under the declared transition rule
- `maintenance`: `True` - repair, entropy export, and stability-window constraints all pass
- `finality`: `True` - record threshold and reconstruction-debt budget both pass
- `emergence_platform`: `True` - structure supports enough downstream operations for platform status

### hidden_protocol_twin

- `geometry`: `True` - finite constraints are mutually satisfiable
- `dynamics`: `True` - candidate is reachable under the declared transition rule
- `maintenance`: `True` - repair, entropy export, and stability-window constraints all pass
- `finality`: `False` - accessible records 2 < threshold 3
- `emergence_platform`: `False` - structure supports enough downstream operations for platform status

## What this improved

T114 turns the synthesis into a falsifiable filter with negative controls. It shows exactly where geometry, maintenance, finality, and emergence-platform capacity can separate without claiming a new law of physics.

## What this weakened

The artifact weakens any broad reading of the slogan. If all future positive cases are already fixed by standard maintenance and thermodynamic accounting, the viability filter is only bookkeeping. The only non-collapse signal here is the fixed-standard-state pair where record accessibility changes the observer-experienced verdict.

## Falsification condition

The viability-filter thesis loses independent content if every observer-experienced or platform verdict is determined by geometry, dynamics, and standard maintenance variables alone, with no pre-registered record-finality or operation-right separation.

## Open blocker

The current filter is a finite schema, not a derived theorem. It needs a real domain instantiation where the gates are measured or canonically derived rather than assigned.

## Recommended next

Instantiate the filter on one serious domain, preferably cellular automata or a D1RestrictionSystem transport case, and test whether the finality/emergence gates survive after matching standard stability and entropy variables.

## Claim ledger update

Add T114 as a North-Star/viability-filter artifact only: geometry can be treated as a finite possibility space, while maintenance, record-finality, and emergence-platform gates classify which candidates become observer-experienced. No core claim is upgraded.
