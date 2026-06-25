# T226: Coefficient-Aware Čech-H1 Continuum-Obstruction Object

**Status:** implemented — finite computable object; pytest green (`20 passed`)
**Verdict:** **conditional** (finite_witness)
**Builds on:** [T222](T222-finite-to-infinite-boundary-theorem.md) (Contribution
Needed #i), [T59](T59-finite-to-infinite-boundary-audit.md) (Möbius template /
false-section trap), [T39](T39-csp-satisfiability-reframing.md) (signed-graph
parity engine, AC1–AC7 admissibility metadata)
**Code:** `models/coefficient_sheaf_h1.py` ·
`tests/test_coefficient_sheaf_h1.py` ·
`results/coefficient-sheaf-h1/T226-coefficient-sheaf-h1-v0.1.json`

---

## Verdict

**conditional.** A finite, computable coefficient-aware Čech-H1 object exists,
is constructed here, and does exactly what T222 demanded: on the same
Möbius/signed-graph witness it reports a nontrivial class (no global section)
exactly where the coefficient-blind scalar encoding falsely reported a section,
and its obstruction class agrees with PO1's AC6 restricted-obstruction flag iff
the AC5 transition data is retained. The verdict is **conditional**, not
**closed**, because this is a **finite_witness** that exhibits the
coefficient-aware-vs-blind distinction on finite nerves; it is **not** a general
continuum sheaf-cohomology theorem, and T222's continuum row stays conditional on
that theorem, which is not in scope here (honesty guard, binding).

## What was derived from the sources

- **From T222 (Contribution Needed #i):** the explicit task — build the
  coefficient-aware sheaf-H1 replacement for continuous orientation data and
  compare its verdict against PO1 admissibility metadata. T222's own engine
  (`models/finite_to_infinite_boundary_theorem.py`) only distinguished blind vs.
  aware on a **single index pair** `(U0, U1)` via a direct parity conflict
  (`same + different`). That is the gap this object fills.
- **From T59:** the discipline — a coefficient-blind scalar encoding gives a
  **false global section** despite monodromy −1; a continuum claim is admitted
  only after the transition/coefficient data are carried.
- **From T39:** the AC1–AC7 admissibility vocabulary. AC5 = "named forgotten
  structure"; AC6 = restricted system globally obstructed; AC7 = source globally
  satisfiable (locally orientable patches).

## The object

A finite Čech complex over a finite open cover (the nerve up to triple overlaps),
valued in the coefficient group **Z2** (≅ sign group {+1, −1}):

- **0-cochains** `C0: opens → Z2` — local frame/orientation choices.
- **1-cochains** `C1: overlaps → Z2` — the transition data `g`; `g(i,j)=0` =
  orientation preserved, `g(i,j)=1` = reversed (the sign-twist the blind encoding
  drops).
- **Coboundary** `(d0 f)(i,j) = f(j) − f(i)` in Z2.
- **Cocycle condition** on triple overlaps `g(i,j)+g(j,k)+g(i,k)=0` (real check;
  vacuous on the thin annular covers used as witnesses, validated to fire on a
  planted bad triple).
- **H1 = ker d1 / im d0.** `[g] = 0` (global section exists) **iff** `g` is a
  coboundary `d0 f`, found by exhaustive search over the `2^(#opens)` Z2 frames
  (small enumerated linear algebra; `finite_witness`, not a hardness claim).

Witnesses, all on faithful finite **annular (cyclic) covers** of a band:
`cylinder_annular_4` (zero reversals, loop sign +1) and `mobius_annular_4` (one
wrap reversal, loop sign −1).

## Strongest positive result

On the genuine annular nerves the coefficient-aware H1 separates exactly where
T222's blind encoding failed:

| Cover | loop sign | aware H1 `[g]` | global section (aware) | blind scalar section |
|---|---|---|---|---|
| `cylinder_annular_4` | +1 | trivial | **yes** | yes (agree) |
| `mobius_annular_4` | −1 | **nontrivial** | **no** | **yes — FALSE section** |

So the coefficient-aware H1 **closes the T59/T222 false-section trap**:
`closes_false_section_trap = True`. And the **AC comparison resolves**:

- AC5 **retained** (carry `g`): aware H1 obstructed = True = PO1 AC6 → **agrees**.
- AC5 **forgotten** (blind): H1 trivial = False while PO1 ground-truth AC6 still
  flags obstruction → **disagrees**. The T222 false-section trap is thereby
  **localized to AC5-forgetting**: the coefficient-blind move *is* the projection
  that discards AC5. AC7 (each patch locally orientable) holds throughout; the
  obstruction is purely in the gluing.

`aware_agrees_with_po1_when_ac5_retained = True`,
`blind_loses_obstruction_when_ac5_forgotten = True`.

## First exact obstruction / missing object (a real finding)

T222's blind-vs-aware comparison lived on a **single overlap** `(U0,U1)` and drew
its "obstruction" from a **direct parity conflict** (two edges, `same` + `different`,
on one index pair). That is a **CSP-unsatisfiability artifact, not a Čech-H1
class.** A single overlap is one 1-simplex with **no cover cycle**, and the
cohomology of an interval/tree nerve is trivial: `g(0,1)=1` is *always* the
coboundary of `f=(0,1)`, so `[g]=0` and a section exists even though the loop
sign is −1. The honest H1 therefore reports a **section** on the 2-set form
(`test_single_overlap_has_trivial_h1_no_cycle`). **The real Möbius obstruction
requires a genuine cover cycle (the annular wrap); single-overlap "monodromy −1"
is necessary but not sufficient.** This is the exact structural correction T226
contributes back to T222's encoding, and it is why the object had to be a true
nerve, not a single pair.

The **missing object** that keeps the verdict at conditional rather than closed:
a continuum statement requires a *limit / refinement* argument over arbitrarily
fine covers (Čech-to-derived comparison, or a colimit over the directed system of
finite covers) establishing that the finite-nerve class is the genuine continuum
H1 of the orientation sheaf. That limit theorem is **not** built here and is
**not** licensed from this finite witness (honesty guard).

## Constructive next object

Build the **directed colimit of the finite annular nerves** under cover
refinement and show the Z2 H1 class is **stable** across the refinement system
(the class survives subdivision), giving a finite-data certificate that the
continuum orientation class is what the finite nerve computes. This is the
honest bridge from `finite_witness` to a continuum statement, and it is distinct
from (and must not be conflated with) the D1Cat transfinite-colimit lane (a
different T222 contribution, a different object).

## Meaning for the relevant claim (CSP-PO1, T222 row)

T222 classified **CSP-PO1** as **conditional**: countable scale survives
unconditionally, continuum is conditional on carrying transition data. T226
**upgrades the conditional from a stated target to a built object**: the
coefficient-aware obstruction object now exists, computes the correct Möbius
class, and is verified to track AC5. The CSP-PO1 continuum row remains
**conditional** (no continuum theorem is claimed), but its conditionality is now
**concrete and instrumented** rather than a placeholder, and the precise extra
hypothesis is named (refinement-stability / cover colimit). No promotion of
CSP-PO1 to `proto_independent`-at-the-continuum is warranted from this finite
witness.

## Known constraints, success/failure criteria

**Known Physics Constraints:** None. This is a finite typed-machinery audit:
H1 is pure Z2 linear algebra on a finite cochain complex. No
physics/curvature/connection/holonomy/new-object language is promoted; "monodromy"
denotes only the loop sign-product, not a geometric claim.

**Success criteria (all met):** (1) aware H1 nontrivial on Möbius, trivial on
cylinder, with correct loop signs; (2) blind encoding exhibits the false section
on Möbius; (3) AC5-retained H1 agrees with PO1 AC6, AC5-forgotten disagrees;
(4) cocycle/coboundary machinery is a real computed check (validated to fire on a
bad triple, pass on a good one).

**Failure criteria (none triggered, two guards binding):** a general Čech/sheaf
continuum theorem stated from this finite witness → **forbidden**; any
physics/geometry promotion → **forbidden**; the single-overlap encoding treated
as a real H1 class → **explicitly rejected** (the finding above). Tag:
**finite_witness**.

## Next proof / computation step

Construct the cover-refinement colimit and prove (or executably exhibit)
refinement-stability of the Z2 class across at least one nontrivial subdivision of
the annular cover; that is the single remaining step to move CSP-PO1's continuum
row from `conditional` toward a stated continuum certificate — still short of, and
not to be confused with, a general continuum cohomology theorem.
