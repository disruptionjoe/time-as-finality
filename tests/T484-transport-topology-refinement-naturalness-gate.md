# T484: Transport Topology Refinement Naturalness Gate

## Target Claims

- [RG Flow as a Multiscale-Transport Analogy](../open-problems/rg-flow-as-multiscale-transport-analogy.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)
- [T38: Minimal Multiscale Transport Formalization](T38-minimal-multiscale-transport.md)
- [T480: Scale-Label Operation Gate](T480-scale-label-operation-gate.md)
- [T481: Internal Scale Structure Admission Gate](T481-internal-scale-structure-admission-gate.md)
- [T482: Internal Scale Generator Invariance Probe](T482-internal-scale-generator-invariance-probe.md)
- [T483: Internal Scale Generator Independence Gate](T483-internal-scale-generator-independence-gate.md)

## Setup

T483 admitted one fixed-D1 transport-topology generator as a future review
target: classify observer sites by transport component relative to a declared
source and target. That admission was only review metadata and
transport-topology bookkeeping.

T484 tests the next burden. A topology generator must survive benign
transport-graph refinements before it can remain review-grade bookkeeping. The
gate subdivides each trust-preserving edge in the T24/T38 connected and
partitioned transport fixtures while preserving the D1 profile tuple for the
original observer sites.

The positive review packet uses only the source/target reachability role of
the original observer sites:

```text
source_target_component
source_side_component
target_side_component
other_component
```

Hostile packets try to treat component size, path length, relay count,
observer-label order, reachability finality, RG/conformal structure, or a
promotion shortcut as internal scale evidence.

## Success Criteria

- T483 remains passed and review-target-only.
- Original observer D1 vectors remain fixed across the connected, partitioned,
  and edge-subdivided fixtures.
- Reachability roles separate the connected and partitioned fixed-D1 pair.
- Reachability roles for original observers are invariant under edge
  subdivision.
- Reachability roles are invariant under observer-label relabeling.
- Component size changes under edge subdivision and is blocked as scale.
- Source-to-target shortest-path length changes under edge subdivision and is
  blocked as scale.
- Label-only, observer-order, hidden relay/time, duration/arrow, finality,
  RG/conformal, physics, and promotion shortcuts are blocked.
- The result earns no independent internal scale structure, record clock,
  duration, temporal arrow, record-finality change, scale-genesis theorem,
  physics claim, D1 promotion, RG/TaF equivalence theorem, claim-ledger
  movement, roadmap movement, North Star movement, public-posture movement, or
  cross-repo movement.

## Failure Criteria

- A refinement-sensitive component-size or path-length quantity is admitted as
  internal scale.
- Edge subdivision changes the reachability roles of original observers.
- Fixed-D1 controls are omitted.
- Observer ID order survives as a generator.
- Added relay count creates clock, duration, or arrow evidence.
- Reachability changes record-finality status.
- RG or conformal fixed-point machinery becomes a TaF topology generator.
- The result promotes D1, scale genesis, physics posture, public posture,
  claim status, or cross-repo truth.

## Known Physics Constraints

RG scale and conformal symmetry remain external analogy material. T484 does
not evaluate RG beta functions, conformal-gravity phenomenology, unitarity,
rotation curves, asymptotic freedom, or quantum gravity.

## Result

Implemented as T484 v0.1.

Expected verdict:

```text
TRANSPORT_TOPOLOGY_REFINEMENT_GATE_BUILT_REACHABILITY_BOOKKEEPING_ONLY
```

The gate admits source/target reachability roles only as refinement-stable
review bookkeeping. Component size and shortest-path length change under
benign edge subdivision, so they are blocked as internal-scale, clock,
duration, finality, or scale-genesis evidence.

## Reproduction

```bash
python -m pytest tests/test_transport_topology_refinement_naturalness_gate.py -q
python -m models.transport_topology_refinement_naturalness_gate --write-results
```

Artifacts:

- `models/transport_topology_refinement_naturalness_gate.py`
- `tests/test_transport_topology_refinement_naturalness_gate.py`
- `results/T484-transport-topology-refinement-naturalness-gate-v0.1.json`
- `results/T484-transport-topology-refinement-naturalness-gate-v0.1-results.md`

## Contribution Needed

Future topology packets must include transport-refinement controls before
using topology as a generator. Fixed-D1 transport reachability remains
bookkeeping unless a later theorem connects it to internal scale without
importing component size, path length, clocks, duration, finality,
RG/conformal mechanisms, physics posture, or claim promotion.
