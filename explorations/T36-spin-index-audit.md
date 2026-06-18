# T36 Spin Geometry / Index Theory Audit

## Verdict

PO1 is index-shaped, not an index theorem.

The Witten and Nielsen-Ninomiya bridges touch real index-theoretic terrain
because the source mathematics involves chirality, anomaly inflow, and no-go
constraints that are naturally expressed with Dirac, lattice, or K-theoretic
ideas. But current PO1 machinery tracks only finite local satisfiability,
global assignment failure, projection definability, and named forgotten
structure. It has no Dirac operator, symbol class, kernel/cokernel count,
spectral flow, eta invariant, K-theory class, or cobordism datum.

The safest verdict:

```text
PO1 can model the finite shadow of index-relevant structure loss,
but it does not preserve or compute an index.
```

## Closest Existing Mathematics

- Atiyah-Singer index theory: genuine index equals analytic
  kernel/cokernel data and topological characteristic-class data. PO1
  currently has neither side.
- APS and anomaly inflow: Witten and Nielsen-Ninomiya are closest to this
  because the richer systems add defect, boundary, bulk, or algebraic data.
- Lattice index, Ginsparg-Wilson, and overlap fermions: Nielsen-Ninomiya
  naturally belongs here.
- Cech cohomology and obstruction theory: PO1's finite gluing language is
  closer to Cech obstruction theory than to Fredholm index theory.
- Exact sequences of sheaves or presheaves: the cleanest mathematical upgrade
  would interpret forgotten structure as a kernel/cokernel and the restricted
  obstruction as a connecting obstruction.
- K-theory and bulk-boundary correspondence: a serious spin/index extension
  would need K-classes, pushforwards, boundary maps, and spectral flow.

## Clean Mappings

- **Witten:** The restricted smooth compact class has vanishing Dirac index or
  non-chiral spectrum in the source theorem. The finite model maps this to a
  restricted gluing obstruction, while a richer stratified/defect system has a
  global assignment because anomaly-inflow data is present.
- **Nielsen-Ninomiya:** The restricted on-site lattice assumptions force net
  chirality cancellation. The richer bulk-boundary/Ginsparg-Wilson-style setup
  restores chiral boundary content through anomaly inflow.
- **PO1 obstruction polarity:** AC6 plus AC7 encode a sharp polarity:
  restricted obstructed, richer unobstructed. That resembles an index defect
  only at the Boolean obstruction level.
- **Finite gluing analogy:** T33's finite gluing certificate is a legitimate
  local-to-global obstruction and a plausible stepping stone toward
  cohomological machinery.

## Failed or Weak Mappings

- The bridge morphisms explicitly do not preserve obstruction status, which is
  the opposite of index preservation.
- PO1 has no stable integer or K-theory-valued invariant.
- PO1 has no analytic operator, chiral grading, ellipticity, kernel, cokernel,
  or spectral flow.
- PO1 has no topological side: no characteristic classes, symbol classes,
  spin/spin-c structures, eta terms, or K-theory pairings.
- AC5 is metadata-dependent. Forgotten structure is named on
  `ProjectionCase`; it is not yet an intrinsic kernel, quotient, or
  obstruction class.
- T35 generic witnesses, such as `a=b, b=c, c=d, a!=d`, can be positive finite
  PO1 candidates with no natural spin/index content.
- Distler-Garibaldi fails AC3 because a richer site has no target in the
  single-E8 restricted system. That is a category-change boundary, not an
  index-preserving projection.

## Overclaims

Avoid saying:

- PO1 is an index theorem.
- Witten and Nielsen-Ninomiya bridges prove index preservation.
- Admissibility is already an index-like invariant.
- Finite gluing obstruction equals Cech cohomology equals Dirac index.
- Distler-Garibaldi is explained by PO1.
- T35 discovers index-theoretic theorems.

Defensible narrower claim:

```text
In Witten and Nielsen-Ninomiya, PO1 tracks finite shadows of structures
that are index-theoretically meaningful in the source mathematics.
```

## Underdeveloped Mathematics

- The category of `D1RestrictionSystem` objects is not developed enough:
  identities, composition, equivalence, refinement, and invariance are thin.
- AC5 needs to become first-class formal data, preferably as a kernel,
  quotient, or exact-sequence component.
- The finite gluing obstruction needs a refinement-invariant cohomological
  version.
- The bridge from finite binary constraints to real spin geometry is missing.
- The framework needs to distinguish "projection changes obstruction status"
  from "projection preserves an index class."
- Distler-Garibaldi needs representation-category machinery, not a forced
  finite-site map.

## Required Mathematics Before Serious Uptake

1. Define a category or bicategory of finite restriction systems and prove
   morphism composition laws.
2. Replace named forgotten structure with an intrinsic kernel/cokernel of
   projection.
3. Prove invariance of obstruction under isomorphism and cover refinement.
4. Build a sheaf/presheaf lift of PO1 with an exact sequence and connecting
   homomorphism.
5. For spin geometry, define actual spin/spin-c Dirac data, symbol classes,
   and K-theory pushforwards.
6. Map Witten and Nielsen-Ninomiya finite variables to source invariants such
   as chirality, index, anomaly inflow, spectral flow, or K-class.
7. Treat Distler-Garibaldi separately as representation-category obstruction.

## Recommended Next Theorem or Counterexample

Best next theorem:

**Projection Boundary Obstruction Theorem**

Given a short exact sequence of finite presheaves

```text
0 -> K -> Rich -> Restricted -> 0
```

a richer global assignment whose restricted image fails to glue determines a
nonzero connecting obstruction in `H1(K)`. PO1 admissibility holds exactly when
this obstruction is nonzero, the projection is total, and the forgotten kernel
is named.

After that, a spin/APS extension could test whether admissible projections of
spin-c Dirac data correspond to an APS or bulk-boundary index defect: the
restricted anomaly is cancelled by a forgotten bulk, defect, or boundary
contribution in the richer system.

Best counterexample to overclaim:

Use the T35 four-patch square obstruction as a fully finite PO1-style witness
with no Dirac operator or K-class. If it satisfies PO1 but has no index
interpretation, PO1 cannot be identified with index theory in general.

## Notes for Synthesis

Use "index-shaped obstruction bookkeeping," not "index theorem."

Witten and Nielsen-Ninomiya are the strongest spin/index-positive cases because
their source theorems already contain chirality/anomaly/index structure. PO1
did not discover that structure; it preserved a finite shadow of it.

Distler-Garibaldi should be synthesized as a boundary result: the framework
correctly refuses to pretend that a category-changing representation-theoretic
obstruction is a finite projection.
