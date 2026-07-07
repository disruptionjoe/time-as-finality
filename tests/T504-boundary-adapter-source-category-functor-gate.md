# T504: Boundary-Adapter Source-Category Functor Gate

## Target Claims

- `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`
- T41 typed-transport category target (`D1Cat`)
- GU / TI / TaF reciprocal bridge contract Section 5, as sharpened by CT-1

## Setup

Build a finite, repo-local boundary-sector fixture with:

- three abstract source objects: carrier, W-minus mirror sector, and collective
  wall;
- six source morphisms: identities plus two restrictions and their composite;
- a target mapping into the T41 D1Cat fixture;
- hostile controls for no source category, object-only maps, constant
  functors, bad composition maps, wrong W-minus target, and sibling-repo truth
  shortcuts.

No sibling repository is inspected or treated as source truth.

## Success Criteria

- The synthetic source fixture satisfies identity, unit, composition-closure,
  and associativity checks.
- The admitted packet maps source objects and morphisms into D1Cat and
  satisfies `F(id) = id` and `F(g;f) = F(g);F(f)`.
- The admitted packet is non-constant and maps W-minus to the declared
  collective-complement target.
- Admission is review-only.

## Failure Criteria

- Object-only bridge language is rejected.
- Missing source morphisms are rejected.
- Constant functors are rejected even when they satisfy functor laws.
- Bad composite morphism maps are rejected.
- Wrong W-minus target maps are rejected.
- Cross-repo or sibling-truth shortcuts are blocked.

## Known Physics Constraints

This is not a physics or GU theorem. The finite fixture is an admission gate
for future bridge packets. It does not assert that GU has supplied a real
source category, that the mirror is the collective-capability boundary, or
that the two-adapter gate has been met.

## Contribution Needed

Future work must supply a source category from the owning repository or a
repo-local packet: objects, morphisms, composition, identities, object map,
morphism map, non-constant functoriality, hostile controls, and demotion path.
