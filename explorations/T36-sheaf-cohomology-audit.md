# T36 Sheaf / Cohomology / Local-to-Global Audit

## Verdict

`D1RestrictionSystem` is not currently a presheaf or sheaf. It is a finite
graph-indexed patch-constraint system with D1 profile labels, transport
metadata, and a global satisfiability checker. That is weaker than a presheaf
because there is no base category, no contravariant restriction functor, and no
restriction maps for all inclusions or subcontexts.

PO1 obstructions are not currently cohomological. They are finite
local-to-global satisfiability obstructions: every patch is locally
satisfiable, but the combined constraint set has no global assignment. Some
binary `same`/`different` cases are close to `Z2` parity cohomology on a signed
graph, but the repo has not yet proved or implemented that realization.

`global_section` is the right future abstraction, but current T26 usage should
be read as `global_assignment` or `joint_solution`. Calling it a sheaf global
section is premature unless a presheaf/sheaf realization theorem is added.

## Closest Existing Mathematics

- Finite CSP / SAT: local constraints satisfiable, global constraint set
  unsatisfiable.
- Sheaf-theoretic contextuality: local sections over contexts with no global
  hidden-variable assignment.
- Signed graph parity / `Z2` cohomology: `same=0`, `different=1`; obstruction
  is odd parity around a cycle.
- Relational database consistency: local relations whose global join is empty.
- Cech cohomology as a plausible later upgrade, not yet a proved current
  semantics.

## Clean Mappings

- D1 sites map cleanly to finite indices, vertices, or measurement contexts.
- `RestrictionPatch` maps cleanly to a local relation over finite variables.
- `local_witness_count == patch_count` means every local relation is nonempty.
- `global_assignment_exists=False` means the global join or CSP solution set is
  empty.
- AC6 is exactly "locally satisfiable but globally unsatisfiable."
- AC7 is exactly "the richer system has a global solution."
- T21's CHSH example cleanly supports local sections without global
  assignment.
- PO1 cleanly captures definable projection plus richer satisfiable plus
  restricted unsatisfiable plus named forgotten structure.

## Failed or Weak Mappings

- Transport edges are not sheaf restriction maps.
- A single local D1 profile per site is not a stalk, section set, or local
  section space.
- Patches are constraints, not open sets; the cover/category is implicit.
- There is no locality or gluing axiom check for `D1RestrictionSystem`.
- T13's integer-score Cech machinery is not integrated with T26/PO1.
- No global assignment is not automatically nonzero H1.
- PO1 projections are not yet functorial; composition is tested operationally
  in T34 but not proved categorically.
- AC5 depends on external `ProjectionCase` metadata, not intrinsic
  restriction-system structure.

## Overclaims

- "D1RestrictionSystem is sheaf-like" is acceptable informally; "is a sheaf"
  is false.
- `H1_cohomological` and `H1_finite_gluing` are overnamed in T33. Use "finite
  gluing obstruction" unless a cohomology theorem is proved.
- T13's "H1 is now executable" claim should be downgraded until a nontrivial
  H1 witness actually passes.
- T21 proves a contextuality-style no-global-assignment certificate, not Cech
  cohomology.
- T33's claim that RMT derives AC5-measurable is too strong: a resource drop
  can be built with identical local profiles and changed patches.
- "Theorem" language around IPT/RMT should be softened to "framework,"
  "principle," or "audit check" until formal statements and proofs exist.

## Implementation Audit Notes

Two concrete local checks support the caution above:

1. The executable T13 scenario currently reports:

```text
is_cocycle True
is_coboundary True
h1_is_nontrivial False
```

The tests also assert `h1_is_nontrivial` is false. So the current executable
does not provide a nontrivial H1 witness.

2. The current PO1 machinery has strong finite gluing evidence, but this is a
CSP/joint-assignment result until a cochain complex and quotient are defined.

## Underdeveloped Mathematics

- Define the base category: sites, patches, contexts, subcontexts, covers.
- Define the section object: proposition assignments, D1 profiles, or
  D1-labeled assignments.
- Separate the ambient assignment sheaf from the constrained support
  subpresheaf.
- Define restriction maps by projection to subcontexts.
- Prove equivalence between current `global_section()` and sheaf/global-section
  language.
- Choose coefficients for cohomology; binary parity suggests `Z2`.
- Prove soundness/completeness for when cohomology detects the obstruction.
- Extend beyond binary `same`/`different` constraints.
- Make forgotten structure first-class, not just metadata.

## Required Mathematics Before Serious Uptake

1. A finite context category for every `D1RestrictionSystem`.
2. A presheaf `F : C^op -> Set` of local assignments.
3. A constrained support object `E` whose local sections satisfy patches.
4. A theorem: T26 global assignment exists iff `E` has a global section.
5. A theorem identifying AC6 with local nonemptiness plus empty global section.
6. A `Z2` cohomology theorem for the equality/difference fragment.
7. A projection/functor theorem showing how PO1 maps richer to restricted
   systems.
8. A corrected T13 nontrivial H1 witness, or a retraction of that claim.

## Recommended Next Theorem or Counterexample

Prove the **Binary Parity Obstruction Theorem**:

Given a finite graph of variables with edge labels in `Z2`, where `0 = same`
and `1 = different`, a global `+/-1` assignment exists iff the edge-label
1-cochain is a coboundary. Equivalently, every cycle has even total parity.

The T27/T28/T35 patterns

```text
a = b
b = c
a != c
```

and

```text
a = b
b = c
c = d
a != d
```

would then become genuine `Z2` cohomology obstructions.

Also preserve the T32 `remove_ac5` style witness as a counterexample: strict
global satisfiability loss does not imply local D1 profile loss or named
forgotten structure.

## Notes for Synthesis

Recommended renames:

- `global_section()` -> `global_assignment()` or `joint_solution()`.
- `H1_cohomological` -> `finite_gluing_obstruction`.
- `H1_finite_gluing` -> `locally_satisfiable_globally_unsat`.
- `D1RestrictionSystem` in prose -> `finite D1 patch-constraint system` until
  restriction maps exist.
- `Resource-Monotonicity Theorem` -> `global-satisfiability resource
  principle`.
- `Invariant-Preservation Theorem` -> `invariant-preservation framework`.

Synthesis should say: PO1 is strongest as a finite projection-created
satisfiability-loss schema. Its sheaf/cohomology upgrade is promising,
especially through `Z2` parity contextuality, but not yet earned.
