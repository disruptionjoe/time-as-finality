# T231: Cover-Refinement-Stability of the Coefficient-Aware Z2 Čech-H1

**Verdict (top): conditional (finite_witness).**

**Builds on:** [T226](T226-coefficient-aware-sheaf-h1-continuum.md) (the finite
coefficient-aware Čech-H1 object, `models/coefficient_sheaf_h1.py`),
[T222](T222-finite-to-infinite-boundary-theorem.md) (CSP-PO1 continuum row;
Contribution Needed #i). **Code:** `models/sheaf_h1_refinement.py` ·
`tests/test_sheaf_h1_refinement.py` (37 passed with T226's suite; 17 new) ·
`results/sheaf-h1-refinement/T231-sheaf-h1-refinement-v0.1.json`.

**Tag:** `finite_witness` (executable fixture; NO continuum cohomology theorem
asserted). The class decider is a `poly_decider` (linear wrap-cycle parity,
cross-validated against T226's exhaustive 2^n search). This is the **continuum
coefficient-sheaf bridge** and is **explicitly distinct from** the discrete
category-level D1FilteredMorphism object (T232) — T226 and T228 both flag these
must not be conflated; they index different colimit systems and this file touches
only the coefficient-sheaf side.

---

## Verdict

**conditional.** The named bridge T226 left open — "build the directed colimit of
the finite annular nerves under cover refinement and show the Z2 H1 class is
stable across the refinement system" — is built and executably exhibited. A
genuine subdivision `annular_n → annular_2n` with an explicit simplicial
refinement map and cochain pullback is iterated into a directed chain
`annular_4 → annular_8 → annular_16 → annular_32`. The **nontrivial Möbius class**
(`[g] ≠ 0`, loop sign −1, no global section) and the **trivial cylinder class**
(`[g] = 0`, loop sign +1, global section) are **preserved at every refinement
step**. The verdict is **conditional**, not **closed**, because this is a
`finite_witness` refinement-stability *certificate* over an explicit cofinal
annular chain; it is **not** a general continuum sheaf-cohomology theorem and
does not license one (binding honesty guard).

## What was derived from the sources

- **From T226 (Constructive next object / Next proof step, verbatim target):** the
  exact object — the directed colimit of finite annular nerves under cover
  refinement, with the demand that the Z2 H1 class survive subdivision, "giving a
  finite-data certificate that the continuum orientation class is what the finite
  nerve computes." T226 supplied the witnesses (`annular_cover`,
  `mobius_annular_4`, `cylinder_annular_4`), the Z2 cochain machinery
  (`coboundary_d0`, `is_cocycle`, `transition_is_coboundary`, `monodromy_sign`),
  and the honesty guards. This module reuses all of them unchanged (import only;
  `coefficient_sheaf_h1.py` is not modified).
- **From T222:** the CSP-PO1 continuum row is `conditional` on carrying transition
  data and on a refinement/colimit argument over arbitrarily fine covers. T231
  supplies the refinement-stability half of that named extra hypothesis as a
  finite, instrumented certificate — without claiming the full continuum theorem
  T222 reserves.

## The object

A subdivision + refinement map + pullback, on the orientation (sign) sheaf with
constant stalk Z2:

- **Subdivision** `subdivide_annular(n, reversed_edges)`: each coarse patch
  `V_i` splits into two fine patches `U_{2i}, U_{2i+1}` (left/right halves),
  giving `annular_2n`. Patch count and edge count both double (non-vacuous
  refinement, asserted in `test_subdivision_doubles_the_cover`).
- **Refinement map** `pi`: `pi(2i)=pi(2i+1)=i` (containment `U_a ⊆ V_{pi(a)}`).
  Fine edges are **INTRA** (both ends in one coarse patch — the split seam,
  transition 0, image `None`) or **INTER** (crossing two coarse patches,
  inheriting the coarse edge's transition). A real simplicial-map check
  (`vertex_map_respects_containment`) verifies `pi` carries 1-simplices to real
  coarse 1-simplices or collapses them inside a 0-simplex.
- **Pullback** `pi^* g`: the fine transition cochain equals the pullback of the
  coarse transition cochain (`pullback_is_consistent`). Exactly one INTER edge
  carries the Möbius reversal at every scale, so the loop sign-product is
  transported faithfully (`test_inter_edges_inherit_coarse_transition`).
- **Class decider** `annular_class_obstructed` (`poly_decider`): for a
  single-cycle annular nerve, `[g] ≠ 0` iff the Z2 sum (wrap-cycle parity) of the
  transition cochain is 1. This is the spanning-forest / cycle-space computation
  specialized to one cycle. It replaces T226's exhaustive `2^(#opens)` frame
  search (which would be `2^32` on `annular_32`) and is **cross-validated against
  that exhaustive search** on `annular_{4,8,16}`
  (`test_poly_decider_matches_exhaustive_search`).

## Strongest positive result

Across the directed chain `annular_4 → annular_8 → annular_16 → annular_32`,
every per-step stability check passes for both witnesses:

| Chain | loop sign (every scale) | `[g] ≠ 0` (every scale) | class verdict preserved | pullback / simplicial / cocycle |
|---|---|---|---|---|
| Möbius  | −1 | **True** (no global section) | **True** | all True |
| Cylinder | +1 | **False** (global section)   | **True** | all True |

So the coefficient-aware H1 verdict and the loop sign-product are **invariant
under subdivision through the refinement system**: the obstruction is not an
artifact of one cover granularity. `mobius_class_refinement_stable = True`,
`cylinder_class_refinement_stable = True`, `mobius_loop_sign_invariant = True`,
`cylinder_loop_sign_invariant = True`, `all_steps_stable = True`. The poly_decider
returns the same verdict as T226's exhaustive H1 wherever both are tractable,
so the certificate inherits T226's coefficient-aware-vs-blind correctness.

## First exact obstruction / missing object (a real finding)

The certificate is exhibited over an **explicit cofinal chain of *uniform*
annular subdivisions**, each halving patch diameter. What is **not** established,
and is the exact gap keeping the verdict at `conditional`:

1. **No arbitrary-refinement statement.** Stability is shown for the canonical
   bisection chain, not for *every* refinement of an annular cover, and not for
   non-annular covers (covers whose nerve has more than one independent cycle, or
   nontrivial triple overlaps). The single-cycle structure is load-bearing: the
   `poly_decider` is the *one-cycle* specialization, and the cylinder/Möbius
   classes live in a 1-dimensional H1. A genuine cofinality argument over the
   *whole* directed system of covers is not built here.
2. **No colimit-equals-derived-cohomology theorem.** Refinement-stability of the
   finite class is necessary but not sufficient for the statement "the colimit
   over all covers equals the sheaf/derived cohomology of an orientation sheaf on
   a continuum band." That Čech-to-derived comparison is **not** built and is
   **not** licensed from this finite witness (binding honesty guard).

**Missing object:** a cofinality + colimit-stability theorem over the full
directed poset of covers (not just the bisection chain), plus the Čech→derived
comparison identifying the stable finite class with continuum H1. That is the
single remaining step from this certificate to a continuum statement.

## What the certificate DOES and DOES NOT license (binding)

- **DOES:** certify that the finite-nerve Z2 class is **refinement-stable** — the
  `[g]`-verdict and loop sign survive subdivision through the directed chain — so
  the finite nerve's class is not a granularity artifact. The honest bridge
  *from* `finite_witness` *toward* a continuum statement.
- **DOES NOT:** assert a general continuum sheaf-cohomology theorem; assert
  stability over arbitrary (non-annular / multi-cycle) covers; promote any
  physics / curvature / connection / holonomy / new-object language. "monodromy"
  = loop sign-product only; "H1" = finite Z2 cycle-space rank of the specific
  finite annular cover.

## Constructive next object

The **cofinal colimit stability theorem**: extend from the bisection chain to the
full directed poset of finite covers of the band, proving cofinality of the
annular bisection system and stability of the Z2 class along *every* refinement,
then the Čech→derived comparison identifying the stable class with the
orientation sheaf's continuum H1. Named, not built. (Distinct object from the
D1FilteredMorphism category-level colimit lane.)

## Meaning for the relevant claim (CSP-PO1, T222 continuum row)

T222 holds CSP-PO1 at `conditional`: continuum reach is conditional on carrying
transition data **and** a refinement/colimit argument. T226 built the
coefficient-aware object (carries the data). T231 now supplies the
**refinement-stability** half of the remaining condition as a finite, instrumented
certificate: the class the finite nerve computes is stable under subdivision. The
CSP-PO1 continuum row **remains `conditional`** — no continuum theorem is claimed —
but its conditionality is now narrowed to the single named gap (cofinality +
Čech→derived comparison over the *full* cover poset), with the uniform-bisection
stability already discharged. No promotion of CSP-PO1 to a continuum
`proto_independent` is warranted from this finite witness.

## Known Physics Constraints

None. Pure finite Z2 linear algebra on a finite cochain complex plus a linear
cycle-parity decider. No hardness/scale claim (the decider is a `poly_decider`,
explicitly NOT a hidden search per COMPLEXITY-LEDGER discipline; the exhaustive
2^n route is retained only as a small-cover cross-check). No physics / geometry /
curvature / connection / holonomy / new-object language is promoted.

## Success / failure criteria

**Success (all met):** (1) the subdivision is a genuine non-identity refinement
(patch + edge count double); (2) the refinement map is a valid simplicial map and
the fine transition is the pullback `pi^*` of the coarse transition; (3) loop sign
and `[g]`-verdict are invariant across `annular_4 → 8 → 16 → 32` for both Möbius
(nontrivial) and cylinder (trivial); (4) the `poly_decider` matches T226's
exhaustive H1 on `annular_{4,8,16}`.

**Failure (none triggered; two guards binding):** stating a general continuum
Čech/sheaf-cohomology theorem from this finite witness → **forbidden**; claiming
stability over arbitrary non-annular covers from the bisection chain →
**forbidden**; any physics/geometry promotion → **forbidden**; conflation with the
D1FilteredMorphism category colimit lane → **explicitly disclaimed**.

## Next proof / computation step

Prove cofinality of the annular bisection system inside the full directed poset of
band covers and stability of the Z2 class along every refinement, then the
Čech→derived comparison — the single remaining step to move CSP-PO1's continuum
row from `conditional` toward a stated continuum certificate, still short of, and
not to be confused with, a general continuum cohomology theorem.

## Reproduction

```
cd "<repo root: .../time-as-finality>"
python -m pytest tests/test_sheaf_h1_refinement.py -q        # 17 passed
python -m pytest tests/test_sheaf_h1_refinement.py tests/test_coefficient_sheaf_h1.py -q  # 37 passed
python -c "from models.sheaf_h1_refinement import run_t231_analysis, t231_result_to_dict; import json; print(json.dumps(t231_result_to_dict(run_t231_analysis(depth=3)), indent=2))"
```

Results snapshot: `results/sheaf-h1-refinement/T231-sheaf-h1-refinement-v0.1.json`.
