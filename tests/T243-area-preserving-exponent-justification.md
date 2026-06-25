# T243: a WBE/BMR-native justification for the area-preserving n^{-1/2} condition that singles out the 3/4 exponent — MTI sub-object (1)

## Verdict: conditional

The area-preserving `n^{-1/2}` condition that yields the 3/4 exponent **is
singled out by a defensibly WBE/BMR-native structural premise** — a pulsatile
**impedance-matching (reflectionless) junction condition** — which is argued
**independently of the exponent it produces** and passes a **decisive
falsification control** and a five-point **circularity audit**. This resolves
T233 sub-object (1) — the second, untouched MTI blocker — in the **positive
direction**: the 3/4 exponent is not a hand-tuned input; it is the downstream
consequence of a junction-local conservation law (total daughter
cross-sectional area = parent cross-sectional area, `n·beta_r² = 1`) that has a
domain-native physical justification (no reflected pulse energy at branch
points) stated with **no reference to 3/4**.

This is `conditional`, **not** `closed`, for one explicitly named reason: the
WBE-nativeness rests on reading the large vessels as the **pulsatile /
impedance-matched regime** (the second physical regime West-Brown-Enquist
themselves invoke, and the Banavar-Maritan-Rinaldo cross-section-conservation
condition reached from the directed-transport side). That reading is defensible
and argued independently, but — exactly like T238's coverage premise — it is an
**interpretive WBE/BMR axiom, not a theorem** with a cited in-repo derivation.
A reviewer who insists the large-vessel regime is *also* governed only by steady
dissipation minimization can route back to T233's area-increasing `n^{-1/3}`
(a=1) horn.

This lane does **NOT** promote MTI. MTI moves past PARTIALLY_SUPPORTED only when
**both** this sub-object **and** the T238 coverage-axiom half (sub-object 2)
hold under domain-native inputs. With T243 the open MTI residue collapses from
two interpretive-premise gaps to **two parallel "elevate the premise to a cited
axiom" steps** — symmetric in shape, both interpretive, neither a theorem.

Recommendation to integrator: record that T233 sub-object (1) is now
**conditionally discharged** (the area-preserving premise is domain-native,
non-circular, and singles out 3/4 across n ∈ {4,8,16,27}); keep MTI
PARTIALLY_SUPPORTED; the two remaining MTI gaps (this reflectionless premise +
the T238 terminal-reachability premise) are now both **"premise → cited axiom"
upgrades**, not open computations. Ratification is the integrator's.

Tags: `finite_witness` (a finite self-similar branching-tree fixture + finite
grid scans over `beta_r`; NO continuum theorem) + `poly_decider` (closed-form
reflection functional + bounded finite-grid argmin with a finite feasibility
filter; NO hidden search, NO hardness / NP / scale claim).

## What Was Derived From Sources (IMPORT ONLY)

- From **T233** (`models/wbe_objective_selection.py`, IMPORT ONLY):
  `BranchingTree` (the WBE self-similar Poiseuille tree with
  `constrained_dissipation` = `Z·V²` and `metabolic_exponent`),
  `check_dissipation_optimum` (the Gate-1 baseline that lands on the
  area-INCREASING `n^{-1/3}`, a=1), `area_preserving_beta_r` (= `n^{-1/2}`),
  `area_increasing_beta_r` (= `n^{-1/3}`), `space_filling_gamma` (= `n^{-1/3}`),
  and `three_quarter_from_optimal_ratios`. Imported verbatim; the T233 file is
  **not modified** and its suite stays green (verified: 35 passed across
  `test_wbe_objective_selection.py` + `test_wbe_coverage_constrained.py`).
- From **T227** (`models/mti_wbe_continuum.py`, via T233's re-exports): the
  Alpha/Beta network fixtures and `total_dissipation_of_flow` are available but
  **not needed** here — this sub-object is about the branching-ratio selection,
  not the delivery-objective. T227's suite stays green (5 passed).
- **No new physics** beyond (a) the canonical Poiseuille impedance already in
  `BranchingTree`, and (b) the standard linear pulse-wave **junction reflection
  coefficient** `R = ((Y₀ − n·Y₁)/(Y₀ + n·Y₁))²` with area-proportional
  admittance `Y ~ A = π r²` (the rigid-walled long-wavelength / BMR limit). No
  Womersley re-derivation, no GR/QFT/spacetime/curvature, no new law.

## Strongest Positive Result

**A WBE/BMR-native condition — stated as junction physics, not a number — under
which T233's Gate-1 optimum becomes the area-preserving `n^{-1/2}` (a=3/4),
with a decisive falsification control and a five-point circularity audit, across
n ∈ {4,8,16,27}.**

The premise (PART 1): in the pulsatile (periodically driven) large-vessel
regime the network loses energy to waves **reflected** back up the tree at every
impedance-**mismatched** junction. The reflected power at a symmetric n-way
junction is `R(n, beta_r) = ((Y₀ − n·Y₁)/(Y₀ + n·Y₁))²`, `Y₁/Y₀ = beta_r²`. Its
**unique zero** is `n·beta_r² = 1 ⟺ beta_r = n^{-1/2}` — the area-preserving
ratio. Minimizing reflected energy is a physical objective with **no metabolic
exponent in it**. PART 1 confirms the reflection optimum is `n^{-1/2}` to ~1e-8
and the exponent there is 3/4 for every n:

```
n    reflection-argmin beta_r   area-pres n^-1/2   R@argmin   a@argmin   is_area_preserving
 4         0.5000                  0.5000          2.3e-09     0.7500        True
 8         0.3536                  0.3536          6.0e-09     0.7500        True
16         0.2500                  0.2500          3.9e-08     0.7501        True
27         0.1924                  0.1925          6.8e-09     0.7500        True
```

The **load-bearing Gate-1 re-run** (PART 2b): impose `R=0` as a **HARD
feasibility constraint** (lexicographic regime separation: the large vessels ARE
the reflectionless regime) and minimize T233's steady dissipation **within** the
feasible set, on T233's identical scan window/grid. The feasible set of `R=0` is
the single point `n^{-1/2}`, so the constrained dissipation optimum is
`n^{-1/2}`, a=3/4:

```
n    constrained argmin beta_r   area-pres   a@argmin   selects_area_preserving   recovers_3/4
 4        0.5050                   0.5000      0.7582           True                  True
 8        0.3571                   0.3536      0.7554           True                  True
16        0.2525                   0.2500      0.7540           True                  True
27        0.1944                   0.1925      0.7534           True                  True
```

**Hard-constraint limit (the no-free-coefficient proof, PART 2b-conv):** `R=0`
is a single *point*, not a band; on a finite grid a loose tolerance admits a
thin band and steady dissipation pulls the argmin to its fat edge (over-reporting
a > 3/4). As `refl_tol → 0` the argmin converges **monotonically** to `n^{-1/2}`
and the exponent to **3/4** — confirming there is **no free coefficient**, only
a grid concession:

```
n=8  refl_tol  5e-3   1e-3    1e-4    1e-5
     argmin   0.3795 0.3649  0.3571  0.3547   -> n^-1/2 = 0.35355
     a        0.7904 0.7675  0.7554  0.7517   -> 0.75
```

**Decisive falsification control (PART 3):** drop the reflectionless premise and
the optimum reverts to T233's area-INCREASING `n^{-1/3}` (a=1) for every n
(`decisive=True` all n). The constraint is separable and load-bearing; the 3/4
is not smuggled in.

**Rejected encoding, made explicit (PART 2a):** an *additive weighted blend*
`J = (Z·V²) + λ·R` is the tempting-but-circular route. Built and **REJECTED**:
the argmin slides continuously from `n^{-1/3}` toward `n^{-1/2}` as λ grows but
**never lands** at any finite λ (`slides_continuously=True`,
`lands_at_finite_lam=False` all n) — λ would be an **exponent dial**, exactly
the hand-tuning the honesty guard forbids. The honest encoding is the hard
constraint, which has no tunable weight.

**Circularity audit (PART 4), five guards, all green all n:** (1) `R=0` is
exactly the area-preserving condition `n·beta_r²=1`; (2) the reflection
functional contains no exponent and rises on both sides of `n^{-1/2}`; (3) the
3/4 is computed downstream from the selected ratio via T233's
`metabolic_exponent`, never fed in; (4) the additive blend is rejected as a
dial; (5) the falsification control is decisive. `NOT_CIRCULAR = True` for all n.

## First Exact Obstruction / Missing Object

The result is positive, so the obstruction is the **named boundary of the
conditional**, not a failure inside it:

> **The pulsatile reflectionless / area-preserving premise is an interpretive
> WBE/BMR axiom, not a theorem.** "The large-vessel regime minimizes pulsatile
> reflection energy, hence is impedance-matched, hence area-preserving" is a
> defensible reading of the West-Brown-Enquist large-vessel regime and is the
> Banavar-Maritan-Rinaldo cross-section-conservation condition. It is argued
> here independently of 3/4 and does real, falsifiable work. But the repo
> contains **no formal object asserting it as a WBE/BMR axiom**. A hostile
> reviewer who holds that the large vessels are *also* governed only by steady
> dissipation minimization (no separate pulsatile regime) can route back to the
> T233 `n^{-1/3}` (a=1) horn and demote. The missing object is a **cited
> WBE/BMR axiom certificate** that the large-vessel branching is
> impedance-matched / area-preserving (reflection-minimizing) as a
> *constitutive* condition, not an optional add-on.

This is structurally the **same shape** as T238's open obstruction (its
terminal-reachability premise is also a defensible-but-uncited WBE axiom). MTI's
two open gaps are now symmetric "premise → cited axiom" upgrades.

## Constructive Next Object

A **WBE/BMR area-preserving axiom certificate**: locate (in West-Brown-Enquist
1997 and the Banavar-Maritan-Rinaldo directed-transport literature already in
the repo's MTI line) the statement that the large-vessel branching is
impedance-matched / cross-section-conserving (reflection-minimizing) as a
constitutive condition, and cite it against the constraint this module already
implements (`is_reflectionless` / `junction_reflection` / `area_mismatch`). With
that citation the `conditional` on this half upgrades to `closed`, leaving only
the T238 coverage-axiom certificate between MTI and promotion.

(Independent, NOT in this lane: the T238 coverage-axiom certificate — MTI
sub-object (2). MTI promotes only when both land.)

## Meaning For The Claim

- **MTI sub-object (1) is conditionally discharged.** The area-preserving
  `n^{-1/2}` condition that singles out 3/4 has a domain-native,
  independently-argued, non-circular justification (pulsatile impedance matching
  / BMR cross-section conservation), verified across n ∈ {4,8,16,27} with a
  decisive falsification control. This is strictly stronger than T233 left it:
  T233 showed dissipation-min FAILS Gate 1 (lands on `n^{-1/3}`, a=1) and left
  the area-preserving input unexplained; T243 supplies the explanation as a
  separable, falsifiable premise — without re-tuning any exponent.
- **MTI stays PARTIALLY_SUPPORTED.** This lane does not promote it. The two
  remaining MTI gaps — this reflectionless premise (T233 sub-object 1) and the
  terminal-reachability premise (T238 / sub-object 2) — are now **both**
  interpretive "premise → cited axiom" upgrades. Promotion requires both
  citations.
- **Absorbers named.** Steady-dissipation minimization (T233's `Z·V²`) still
  absorbs the *unconstrained* branching-ratio selection (it owns `n^{-1/3}`,
  a=1). The pulsatile reflection functional is a **second, disjoint** physical
  regime that owns the area-preserving `n^{-1/2}` (a=3/4); it is the WBE model's
  own large-vessel physics, not an imported optimizer. No mature neighbor
  absorbs the reflectionless-constrained residue without itself being the
  WBE/BMR area-preserving axiom.
- **No physics promotion.** A finite typed audit of a branching-network
  optimization. Every quantity (`0.7500`, the `n^{-1/2}` ratios, the
  monotone-converging exponents) is a finite computed value of a specific finite
  fixture; **no exponent-as-physical-law claim**, no continuum theorem, no
  hardness/scale claim, no new law (`finite_witness` + `poly_decider`). The 3/4
  is a computed value, not a promoted constant.

## Known Physics Constraints

Physics in scope but bounded: (a) the canonical Poiseuille tube impedance
`Z = 8μl/(πr⁴)` already in T233's `BranchingTree`, and (b) the standard linear
pulse-wave junction reflection coefficient `R = ((Y₀ − n·Y₁)/(Y₀ + n·Y₁))²` in
the area-proportional admittance limit `Y ~ A`. The reflectionless premise is
the West-Brown-Enquist large-vessel (pulsatile / impedance-matched) regime,
equivalently Banavar-Maritan-Rinaldo cross-section conservation, stated
physically (no reflected pulse energy at branch points), **not** promoted to a
universal law. No GR/QFT/spacetime/curvature/gravity language. No
exponent-as-physical-law claim: 3/4 is the computed metabolic exponent of the
selected finite fixture.

## Failure / Falsification Conditions

- **Demote this result to T233's `n^{-1/3}` horn** if "the large-vessel
  branching is impedance-matched / area-preserving (reflection-minimizing)" is
  rejected as WBE/BMR-native — i.e. if the large vessels are held to be governed
  only by steady dissipation minimization with no separate pulsatile regime.
  Then the optimum reverts to area-increasing `n^{-1/3}` (a=1) and the 3/4
  demotes.
- **Invalidate T243** if any of: (a) the reflection functional's zero is NOT the
  area-preserving condition (it is, to 1e-12); (b) the additive blend *lands* on
  `n^{-1/2}` at some finite λ — which would mean a tunable weight could be
  defended (it does NOT: it slides without landing for all tested n/λ); (c) the
  hard-constraint argmin does NOT converge to `n^{-1/2}` / a→3/4 as `refl_tol→0`
  (it does, monotonically); (d) the falsification control is non-decisive — i.e.
  dropping the constraint does NOT revert to `n^{-1/3}` (it reverts to a=1.000
  for all n); or (e) any circularity guard fails (none do).
- **Promote MTI** (separate, integrator-only) only when BOTH this area-preserving
  axiom certificate AND the T238 coverage-axiom certificate are cited under
  domain-native inputs.

## Artifacts

- `models/mti_area_preserving_exponent.py` — the pulsatile junction-reflection
  functional (`junction_reflection`, `area_mismatch`, `is_reflectionless`); the
  reflection optimum (`check_reflection_optimum`, singles out `n^{-1/2}`); the
  **rejected** additive blend (`additive_blend_objective`,
  `additive_blend_is_an_exponent_dial`); the **load-bearing** hard reflectionless
  constraint re-running T233's Gate 1 (`check_constrained_optimum`) plus its
  no-free-coefficient limit (`reflectionless_convergence`); the decisive
  falsification control (`falsification_remove_constraint`); the five-guard
  `circularity_audit`; and the headline `rerun_gate1`. IMPORTS T233/T227 models
  verbatim; touches NO kappa / sheaf-h1 / attribution / d1cat / functor files.
- `tests/test_mti_area_preserving_exponent.py` — 13 real checks (green):
  reflection zero ⟺ area-preserving; reflection positive at `n^{-1/3}`; reflection
  rises both sides of `n^{-1/2}`; reflection optimum is `n^{-1/2}`/3-4; **T233
  baseline unchanged** (dissipation → `n^{-1/3}`, a=1); additive blend rejected
  as exponent dial; hard constraint selects area-preserving; convergence to 3/4
  as tol→0; falsification control decisive; circularity audit all-pass; Gate-1
  re-run singles out 3/4; input validation.
- `results/mti-area-preserving/T243-results.json` — per-n executable numbers and
  all-True summary booleans.

## Next Proof / Computation Step

1. Obtain the **WBE/BMR area-preserving axiom certificate**: a citation
   (West-Brown-Enquist 1997 large-vessel pulsatile regime; Banavar-Maritan-
   Rinaldo cross-section conservation) that impedance-matched / area-preserving
   branching is constitutive of the large-vessel network, not optional. This
   upgrades this half from `conditional` to `closed`.
2. Independently (T238 / sub-object 2): the terminal-reachability coverage-axiom
   certificate.
3. MTI promotes past PARTIALLY_SUPPORTED only when BOTH (1) and (2) hold under
   domain-native inputs; this lane delivers the area-preserving / 3/4 half.

## Registered Status

T243 RUN as of 2026-06-25. Implementation, results, and 13 green checks under
the worker's slug namespace (`models/mti_area_preserving_exponent.py`,
`tests/test_mti_area_preserving_exponent.py`,
`results/mti-area-preserving/T243-results.json`). Imports T227/T233 models
verbatim (their suites verified green: 35 + 5 passed); does NOT edit kappa,
sheaf-H1, attribution, functor, or d1cat-colimit files; does NOT edit
CLAIM-LEDGER.md, ROADMAP.md, MATHEMATICAL-INDEPENDENCE-AUDIT.md, or TESTS.md.
Report at test level; MTI promotion deferred to integrator.
