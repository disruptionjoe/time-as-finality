# Technical Report: Typed Transport Network — v0.1

## What This Tests

T37 formalizes the TypedTransportNetwork as the next mathematical object above
D1RestrictionSystem. The central question: can PO1 admissibility depend on
which path is taken through a network, even when source and target systems are
identical?

## Answer

**Yes.** Path-dependent admissibility is real and executable. Two simple paths
between the same source and target layer yield different PO1 verdicts when they
accumulate different forgotten_structure along the path.

## The New Object

A TypedTransportNetwork is a finite directed graph where:

- **Nodes** are NetworkLayer objects, each wrapping a D1RestrictionSystem.
- **Edges** are NetworkTransport objects, each wrapping a D1RestrictionMorphism
  plus explicit `forgotten_structure` and `preserved_structure` declarations.

The key operations:

```
_compose_morphisms(f, g):
  site_map = {a -> g(f(a)) for a in source}
  preserved_dims = intersection(f.preserved_dims, g.preserved_dims)

_path_accumulated_forgotten(path):
  union of forgotten_structure across all transports in the path

check_path_admissibility(network, path):
  endpoint_case = ProjectionCase(source, target, composed_morphism, accumulated_forgotten)
  return check_admissibility(endpoint_case)  # AC1-AC7
```

## Why AC5 Is the Locus of Path-Dependence

Of the seven admissibility conditions, AC5 is the only one that depends on
path-specific information:

| Condition | Depends on |
| --- | --- |
| AC1 | richer system (endpoint) |
| AC2 | restricted system (endpoint) |
| AC3 | composed morphism's site_map_total |
| AC4 | restricted system's patches |
| **AC5** | **accumulated forgotten_structure + local_profiles_preserved** |
| AC6 | restricted system's obstruction status |
| AC7 | richer system's obstruction status |

When two paths accumulate different forgotten_structure, AC5 is the only
condition that can differ between them. The other six are determined by the
endpoint systems alone.

## The Two Test Networks

### Spectre Network (emergent obstruction)

```
SRC --[type_guarantee forgotten]--> MID --[nothing]--> TGT
```

| Path | PO1? | Why |
| --- | --- | --- |
| SRC -> MID -> TGT | Yes | all AC pass; AC5: forgotten non-empty, profiles differ |
| SRC -> MID (partial) | No | AC6 fails: MID has no obstruction |

Emergent obstruction: the PO1 property appears only at the full chain endpoint,
not at any partial prefix. This reproduces T34's pattern within the network
formalism. T34 consistency: **True**.

### Diamond Network (path-dependent admissibility)

```
SRC --[type_guarantee forgotten, 4 dims]--> L_A --[nothing, 4 dims]--> TGT
SRC --[nothing, 3 dims]-----------------> L_B --[nothing, 3 dims]--> TGT
```

| Path | PO1? | AC5 | Accumulated forgotten |
| --- | --- | --- | --- |
| SRC -> L_A -> TGT | Yes | True | ("type_guarantee",) |
| SRC -> L_B -> TGT | No | False | () |

Path via L_A: forgets ("type_guarantee",); composed morphism declares all 4
dimensions; source accessible_support=2, target accessible_support=1 →
local_profiles_preserved=False → AC5=True → PO1.

Path via L_B: forgets nothing; composed morphism declares only 3 dimensions
(excluding accessible_support); all declared dims match between source and
target → local_profiles_preserved=True; but forgotten_structure=() → AC5=False
→ not PO1.

Same source, same target. Different path, different verdict.

## The Theorem

**Path-Dependent Admissibility Theorem:**

> In a TypedTransportNetwork, two simple paths between the same source and
> target layer can yield different PO1 admissibility verdicts when they
> accumulate different forgotten_structure. Specifically, if path P1 accumulates
> non-empty forgotten_structure and path P2 accumulates empty
> forgotten_structure, then AC5 holds for P1 and fails for P2, even though both
> paths connect the same endpoint systems.
>
> AC1, AC2, AC3, AC6, AC7 are endpoint-determined and path-invariant. Only AC5
> (structure_forgotten) can vary when paths accumulate genuinely different
> forgotten_structure.

## What This Does Not Claim

**Composition associativity:** The intersection-of-preserved-dimensions
composition rule has not been proven associative. Identity morphisms have not
been constructed. The TypedTransportNetwork is not yet a formal category.

**Path-dependence via other conditions:** Only AC5 has been shown to vary by
path. It is an open question whether AC1-AC4 or AC6-AC7 could vary if the
network is constructed differently.

**Canonical forgotten structure:** There is no current claim about a canonical
minimal forgotten_structure for a (source, target) pair.

**Hostile domain testing:** The network formalism has not yet been applied to
non-physics hostile domains.

## Relationship to Prior Tests

| Prior test | Relationship |
| --- | --- |
| T26 (D1RestrictionSystem) | NetworkLayer wraps a D1RestrictionSystem |
| T31 (admissibility checklist) | check_path_admissibility uses AC1-AC7 |
| T34 (chained projection) | Spectre network reproduces T34's emergent obstruction pattern |
| T33 (IPT/RMT derivation) | Path-dependence localizes to AC5 (P5: informative forgetting) |

## Alignment with the Research Stack

The TypedTransportNetwork is a new primitive, not a new physical claim. Its
position in the research stack:

| Level | Current occupant |
| --- | --- |
| Primitive objects | D1RestrictionSystem, TypedTransportNetwork (new) |
| Operations | global_section, check_admissibility, analyze_network (new) |
| Theorem | Path-Dependent Admissibility (new) |
| Hostile domain testing | pending |
| Discovery engine | pending (T35 extension) |

The mathematics is not trying to prove the North Star. This result is one small
piece: typed multiscale transport structure is now an executable formal object,
and path-dependence within that structure is a theorem, not a metaphor.

## Evidence Record

- `models/transport_network.py` — TypedTransportNetwork, operations, test networks
- `models/run_t37.py` — runner, writes `results/transport-network-v0.1.json`
- `tests/test_transport_network.py` — 57 tests, all passing
- `results/transport-network-v0.1-results.md` — full evidence table
- `results/transport-network-v0.1.json` — machine-readable output
