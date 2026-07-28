# The ζ₁ Hypersurface-Orthogonality Gate: Does a Foliation Coupled to a Conserved Current Source the Countershaded Sector at All?

**Status:** one-page-calculation result (decidable question, decided), with
primary-source verification of every framework statement used. Executes
constructive next object 2 of
`explorations/foliation-sme-sourcing-map-2026-07-27.md` (the
"ζ₁-on-a-strict-foliation" question) — gate 2 of the wave-3 door relabel. The
gate decides whether the ζ₁ conserved-current sub-branch ((a-current) in the
sourcing map's §3) exists for foliations proper or only for generic vectors.
**Date:** 2026-07-28
**Outcome in one line:** the expected trivialization fires only in the
unnormalized-gradient corner; the khronometric (unit-normal) coupling survives
at **full countershaded strength with the model-dependent prefactor pinned,
α = 1/2**. The sub-branch exists for foliations proper. This is the opposite
of the trivialization the sourcing map's in-note wrinkle gestured at, and it is
reported prominently as such.
**Respects:** the dynamic-unity STOP on foliation existence testing. Everything
here is a Lagrangian identity plus a matching onto an already-published
framework (Kostelecký–Tasson), conditional on "if such a coupling existed."
**Primary sources verified this run** (ar5iv full texts fetched and converted
locally, quotes checked against the converted text):

- Kostelecký & Tasson, *Matter-gravity couplings and Lorentz violation*,
  arXiv:1006.4106, PRD 83, 016013 (2011) — "K-T" (full text, local grep).
- Blas, Pujolàs & Sibiryakov, *Models of non-relativistic quantum gravity: the
  good, the bad and the healthy*, arXiv:1007.3503, JHEP 04 (2011) 018
  (journal ref from INSPIRE metadata; full text fetched and grepped locally) —
  "BPS".
- Jacobson, *Einstein-aether gravity: a status report*, arXiv:0801.1547 —
  summary-level fetch only.
- K-T's PRL, arXiv:0810.1459 — summary-level fetch only.

---

## Verdict

1. **The gate does not close the sub-branch — and the calculation surprised in
   the open direction.** The wave-3 wrinkle ("a coupling to an exactly
   conserved current integrates toward a total derivative") is exactly right
   for a coupling to the **raw khronon gradient** ∂_μφ: that coupling is a
   redundant operator, removable off-shell, zero effect at any order in the
   metric (§2). It is exactly wrong for the coupling to the **unit normal**
   u_μ = N∂_μφ: the norm factor N is metric-dependent, the residue survives as
   F = ζ₁ dN∧dφ, and in a static field this reproduces the entire
   Kostelecký–Tasson countershaded phenomenology (§3).
2. **Hypersurface orthogonality plus unit norm does not suppress the
   countershaded signal — it fixes its prefactor.** Matching the exact
   khronometric response N = 1 − U onto K-T's fluctuation ansatz (their eq.
   (185)) pins their model-dependent constant at **α = 1/2** (leading
   post-Newtonian static order). The constraint structure does for the
   foliation what the nonminimal σ₁ coupling does in K-T's bumblebee. The
   feed's caveat "model-dependent α prefactor travels with the bound"
   *dissolves* for foliations proper: the foliation is the maximally
   predictive occupant of the countershaded channel.
3. **The construction fork decides branch membership, and it lands open.**
   "Foliation couples to a conserved current" has two constructions: through
   ∂_μφ (trivial) or through u_μ (open). Leaf-relabeling invariance
   (φ → f(φ)) forces any invariant coupling through u_μ — and any
   non-invariant gradient coupling ζ₁(φ)∂_μφ j^μ is itself exactly trivial by
   the chain rule. So foliations proper occupy the open case; the closed case
   is the measure-zero corner, not the theory (§2, §3).
4. **Detection non-diagnosticity is strengthened, not weakened.** At leading
   static order the WEP signal is *numerically identical* (α = 1/2) for the
   khronometric foliation and for any unit-norm aether on its aligned static
   solution — the locking is constraint kinematics, blind to the c_i and to
   HSO (§4). Wave 3's "a signal there would not by itself indicate a
   foliation" upgrades to: the leading countershaded signal cannot
   distinguish foliation from generic unit-norm aether *even in principle at
   that order*. What the channel gains instead is a **one-way structural
   falsifier**: for any HSO background the effective field strength is
   decomposable, a_eff∧F ≡ 0 and F∧F ≡ 0 (Frobenius, transplanted to the
   countershaded sector); a twist-type ("magnetic") countershaded signature
   would *exclude* a foliation (§4).
5. **Literature: components known, assembly not found.** The removability
   criterion ("constant or the total derivative of a scalar") is stated in
   K-T 2011 §II.3.1, citing Kostelecký PRD 69, 105009 (2004) — the khronon
   corner of this note is consolidation. The khronometric residual (α pinned,
   exact flat-space nullity, twist-null structure) was not found: K-T never
   treat gradient or HSO backgrounds (zero full-text occurrences of
   khronon/khronometric/Hořava/hypersurface/foliation), and BPS — on record
   with exactly the operator u_μψ̄γ^μψ — treat it as a generically
   dangerous dimension-3 term to be forbidden, with no conserved-current or
   countershading distinction. Flagged possibly-unremarked, with search
   bounds stated (§5).

---

## 1. The object, the fork, conventions

The coupling under audit is the sourcing map's (a-current) channel, K-T's eq.
(194) mechanism specialized to a foliation background:

> L ⊃ ζ₁ u_μ j^μ,  ∇_μ j^μ = 0,

with j^μ a conserved matter current (baryon number as the running example; per
K-T, ζ₁ "can vary with the particle species") and u_μ the foliation's timelike
covector. Signature (−,+,+,+); u_μu^μ = −1 in the normalized case; [ζ₁] = GeV.
In K-T's worldline form the same coupling reads L_u ⊃ (a_eff)_μ u^μ_worldline
with (a_eff)_μ = ζ₁B_μ (their eq. (194), verified); a body of charge q
(baryon number B) sees the worldline term q(a_eff)_μ ẋ^μ.

The construction fork (named per the repo's fork discipline):

- **(A) raw-gradient coupling:** the coupled object is ∂_μφ itself,
  u_μ := ∂_μφ, unnormalized. This is the natural coupling for a
  shift-symmetric scalar; it is *not* invariant under leaf relabeling
  φ → f(φ).
- **(B) unit-normal coupling (khronometric proper):** the coupled object is
  the geometric unit normal u_μ = N∂_μφ, N = (−g^{αβ}∂_αφ∂_βφ)^{−1/2} — the
  FDiff-covariant, reparametrization-invariant object. This is the coupling a
  foliation-as-geometry admits. (Orientation convention: (a_eff)_μ is quoted
  up to the overall sign fixed by the choice of future-directed normal —
  u₀ = ±N on φ = t slices; every observable below (α = 1/2, η, the twist
  criteria) is independent of that choice, and worked displays use the
  future-directed u₀ = −N where a sign is needed.)

Both sides are computed below; the fork resolves (B) as the construction
foliations proper occupy (verdict 3), and the two sides give opposite answers
— which is exactly why the fork had to be named rather than defaulted.

## 2. Case A: raw gradient — exactly trivial (the wrinkle, confirmed and bounded)

On-shell identity (one line):

> √(−g) ζ₁ ∂_μφ j^μ = ∂_μ(ζ₁ φ √(−g) j^μ) − ζ₁ φ √(−g) ∇_μ j^μ,

so for a conserved current the action term is a boundary term. Off-shell and
more strongly: for j^μ the Noether current of a global U(1) acting on ψ with
charge q, the local phase redefinition ψ → exp(iqζ₁φ(x))ψ cancels the coupling
*exactly* (for Dirac kinetic terms, with no O(ζ₁²) remainder), for any metric,
to all orders in h_μν. Equivalently: (a_eff)_μ = ζ₁∂_μφ has field strength
F = ζ₁ d(dφ) ≡ 0 — a pure-gauge configuration of the effective abelian field
that a conserved-current coupling defines. No force, no spectroscopy, no
gravitational-test signal. The channel is not suppressed; it is empty.

This is an instance of a published criterion, verified verbatim this run (K-T
§II.3.1, text following their eq. (16); "akgrav" = Kostelecký, PRD 69, 105009
(2004), bibliography entry verified):

> "the redefinition (16) with an appropriate f(x) can be used to move one
> component of the coefficient field a_μ into the other three, **unless a_μ is
> constant or the total derivative of a scalar** [akgrav]."

Validity audit of the trivialization (the gate's step-2 checklist):

- **ζ₁ constant:** not needed in the dangerous direction. Any khronon-dependent
  coupling ζ₁(φ)∂_μφ j^μ = ∂_μZ(φ) j^μ with Z′ = ζ₁ is *still* exactly
  trivial. Only a coupling varying with position or with *other* fields leaves
  a residue −φ j^μ∂_μζ₁ — and that residue is a position-dependent-coefficient
  scenario, outside the constant-ā countershaded question entirely.
- **Boundary terms:** for localized matter, the surface term evaluates to
  c-numbers of the form ζ₁·(φ at the temporal boundary)·(total charge Q) — a
  constant shift, no local physics. A chemical-potential reading of the
  flat-space term ζ₁j⁰ = ζ₁n confirms it: it shifts the Hamiltonian by
  ζ₁Q_total, invisible in any fixed-Q sector.
- **Global structure:** φ must be single-valued. A foliation of spacetime by
  Cauchy leaves has a global time function M → ℝ, so no Aharonov–Bohm-type
  holonomy ∮a·dx survives. (Compactified time would evade this; excluded by
  the foliation reading itself.)
- **Anomalies:** exact conservation must hold as an operator statement. Baryon
  number is anomalous under the electroweak SU(2); the redefinition then
  regenerates a ζ₁φ·(anomaly density) term — irrelevant in the lab, active
  exactly where B-violation is (early universe). This is the known
  spontaneous-baryogenesis structure (§5): the coupling is empty precisely
  when the current is exactly conserved, and only then.

**Case-A verdict: countershaded channel closed — unsourced, exactly.** Same
status as the no-matter-coupling branch (b) of the sourcing map.

## 3. Case B: khronometric proper — the ∂N residual is the whole countershaded signal, with α pinned

With u_μ = N∂_μφ the same integration by parts leaves (using ∇_μj^μ = 0):

> S_int = ζ₁∫d⁴x √(−g) N∂_μφ j^μ
>       = (boundary) − ζ₁∫d⁴x √(−g) φ j^μ ∂_μN.

Equivalently, ψ → exp(iqζ₁Nφ)ψ removes the gradient part ∂_μ(ζ₁Nφ) of
(a_eff)_μ = ζ₁N∂_μφ and leaves −ζ₁φ∂_μN. The gauge-invariant content is the
effective field strength

> **F_μν = ∂_μ(a_eff)_ν − ∂_ν(a_eff)_μ = ζ₁ (∂_μN ∂_νφ − ∂_νN ∂_μφ)
>  = ζ₁ (dN ∧ dφ)_μν,**

which vanishes iff N is constant on the leaves (N = N(φ)). Consequences,
each one line from this identity:

- **Flat spacetime: exact zero.** The flat khronon background has N ≡ 1, so
  F ≡ 0 identically — not "unobservable after a redefinition argument" but
  identically force-free. Countershading (flat-space invisibility,
  gravity-only visibility) is *automatic and exact* for the khronometric
  coupling; no single-flavor or species-alignment caveat is needed.
- **Static weak field: the full K-T signal.** With g₀₀ = −(1 − 2U) (U > 0 the
  Newtonian potential) the aligned static khronon solution is φ = t, and
  N = (−g⁰⁰)^{−1/2} = 1 − U. Then |F_j0| = ζ₁∂_jU. On a worldline of charge
  q: L ⊃ q(a_eff)₀ = −qζ₁N = −qζ₁(1 − U), i.e.

  > L = ½mv² + (m + qζ₁)U + const:

  inertial mass m, gravitational response m + qζ₁ — a composition-dependent
  free-fall anomaly δa/g = qζ₁/m per body, and an Eötvös parameter between
  bodies 1, 2:

  > **η₁₂ = |ζ₁| · |B₁/m₁ − B₂/m₂|.**

  Within fixed-q systems the level shift qζ₁N is state-independent, so
  standard clocks are blind at O(ζ₁): the channel is WEP-type, not
  redshift-type (in-note).
- **The α pin.** K-T's general O(1,1) fluctuation ansatz (their eq. (185),
  verified verbatim, harmonic coordinates):

  > (ã_eff)_μ^{(1,1)} = ½ α h_μν (ā_eff)^ν − ¼ α (ā_eff)_μ h^ν_ν + ∂_μΨ,

  with, verbatim, "the constant α is calculable but varies with the specifics
  of the theory, typically being determined in terms of the coupling constants
  that control the nonminimal couplings." Insert the K-T Newtonian-limit
  values h₀₀ = 2U, h_jk = 2Uδ_jk (their (0,1) solution, verified) and
  ā_eff = ζ₁ū: the ansatz gives ã₀ = 2αζ₁U; the exact khronometric response
  gives ζ₁ũ₀ = ζ₁U (from N = 1 − U); the spatial components vanish on both
  sides at this order. Hence

  > **α_khronometric = 1/2**  (leading PN static order; in-note matching),

  up to fractional corrections of order the khronometric gravity couplings
  (α_kh ≲ 10⁻⁵, β_kh ≲ 10⁻¹⁵, λ′ per the feed) and preferred-frame-velocity
  effects O(w). The K-T observable combination 2α(ā_eff) evaluates to
  ζ₁ exactly — consistent with the direct force derivation above.
- **Why this is not "suppressed."** The residual is proportional to ∂N ≈ ∂U —
  but the countershaded observable was *always* an O(coefficient × ∂U) effect:
  that is the definition of countershading (K-T's PRL mechanism: the
  coefficient fluctuation tied to the metric makes ā visible only through
  gravity). Relative to gravity itself the composition-dependent piece
  ζ₁q/m carries **no** ∂U or U suppression. The naive ζ₁ estimate for the
  countershaded signal survives at full strength; what is suppressed —
  totally — is every non-gravitational observable.
- **Contrast inside K-T's own model space (verified verbatim):** for their
  smooth-potential bumblebee, "observability of (ā_eff)_μ involves nonminimal
  couplings, so ... dominant effects from (ā_eff)_μ [are] proportional to the
  product ζ₁σ₁," and "minimal couplings cannot generate Lorentz violation of
  the (ā_eff)_μ type in the modified Einstein equation." The khronometric
  constraint (unit norm + HSO) plays the role of σ₁: it generates the locked
  fluctuation with α = 1/2 and *no* nonminimal coupling. The foliation is the
  countershaded channel's cleanest realization, not its trivialization.

**Parametric size (illustrative fold, not a claimed bound).** For the baryon
current, q = A and Δ(B/m) between MICROSCOPE's Ti and Pt test masses is
≈ 9.7×10⁻⁴ GeV⁻¹ (atomic masses, in-note arithmetic). Folding the recalled
MICROSCOPE final result |η(Ti,Pt)| ≲ 5×10⁻¹⁵ through η = |ζ₁|Δ(B/m) would put

> |ζ₁| ≲ 5×10⁻¹² GeV  (parametric; recalled η, no species decomposition),

within one to two decades of the feed's countershaded benchmark
α(ā_eff)_T ~ 10⁻¹³ GeV once α = 1/2 and the different species combinations
(ā^p, ā^n, ā^e) are folded. A real bound requires the K-T species machinery
and the published data-table methodology; none is claimed here.

**Residual dynamics (in-note, for completeness):** linearizing the residue in
flat space gives a derivative coupling of the khronon scalar mode to charge
density, of the schematic form −ζ₁ n χ̇. Static sources do not excite it, so
there is no static khronon-exchange fifth force at O(ζ₁²); the O(ζ₁) effects
are confined to dynamic/radiative environments, and the O(ζ₁ρ) stress-tensor
contribution back-reacts on the metric at the source side exactly as K-T's
source-body terms do. Back-reaction on the khronon profile shifts observables
only at O(ζ₁²).

**Case-B verdict: channel open and unsuppressed** — the foliation sources the
countershaded sector with a pinned prefactor and nothing else.

## 4. Case C: generic aether — same leading signal, plus the structure a foliation forbids

- **Static E-type signal: identical.** For *any* unit-norm timelike background
  aligned with the static Killing direction on-shell — Einstein-aether for any
  c_i, khronometric for any (α_kh, β_kh, λ′) — the unit constraint alone
  forces u₀ = −N = −(1 − U). The α = 1/2 locking is constraint kinematics.
  The leading countershaded WEP signal is therefore *the same number* for
  foliation and generic unit-norm aether: zero discrimination in this channel
  at this order.
- **Twist: the exact discriminator.** Generic aether: F = ζ₁du, and the
  Frobenius obstruction u∧du ≠ 0 (twist) maps ζ₁-linearly onto
  a_eff∧F ≠ 0. HSO backgrounds: F = ζ₁dN∧dφ is decomposable, so
  **a_eff∧F ≡ 0 and F∧F ≡ 0 identically** — in electromagnetic language the
  countershaded field strength of a foliation is purely electric-type
  (E_eff·B_eff = 0 in every frame). A generic aether in rotating or
  non-stationary environments can acquire twist (c_i-dependent), sourcing
  "magnetic-type" countershaded observables — spin-current couplings,
  gravitomagnetically correlated sidereal patterns — that a foliation forbids
  exactly. This is a one-way falsifier: a twist-type countershaded signature
  excludes a foliation; its absence confirms nothing. (In-note derivation;
  no twist-sensitive experiment is assessed here.)
- **Mode content:** the aether's transverse vector modes couple to j^μ at
  O(ζ₁) (extra radiative/dynamic channels); the khronon offers only the
  scalar mode through ṅ.
- **Unconstrained vectors are a different regime.** For K-T's smooth-potential
  bumblebee, the conserved-current limit (p^νj_ν = 0) of their fluctuation
  solution (213) collapses to B̃_μ = −ζ₁^S j_μ/p² (in-note reduction of their
  quoted equation) — a Maxwell-like response giving a *flat-space* Coulombic
  fifth force at O(ζ₁²) between charge densities. An in-note EFT estimate puts
  composition-dependent fifth-force reach parametrically far below the
  countershaded window for that model class (α̃_5th ~ (ζ₁M_Pl/m_N)²/4π against
  bounds ~10⁻⁹ would give ζ₁ ~ 10⁻²³ GeV; estimate only, recalled bound). For
  unit-*constrained* backgrounds (aether and khronometric alike) static charge
  density has no linear coupling to the propagating modes — u₀ is
  constraint-determined — so this channel is absent and the countershaded
  window is the leading one. The sourcing map's "generic bumblebee reaches the
  countershaded window untouched" is thus itself model-conditioned: it holds
  for constrained vectors; smooth-potential vectors may face much stronger
  flat-space exchange bounds first (in-note; not pursued).

| background | flat-space effect of ζ₁·(conserved j) | static WEP signal | twist sector a∧F | extra channels |
|---|---|---|---|---|
| khronon gradient ∂φ (case A) | zero, exactly | zero, exactly | ≡ 0 | none |
| khronometric u = N∂φ (case B) | zero, exactly | α = 1/2 pinned: η = ζ₁Δ(B/m) | ≡ 0 (HSO) | scalar mode via ṅ only |
| unit-norm aether (case C) | zero (constraint) | identical: α = 1/2 | ≠ 0 possible (c_i-dep.) | vector modes at O(ζ₁) |
| smooth-potential vector (K-T) | O(ζ₁²) Coulombic exchange | model-dep. (α ∝ ζ₁σ₁) | ≠ 0 possible | massless NG exchange |

## 5. Literature status (what is known, what was not found, and the bounds)

**Known — this note's case A is consolidation:**

- The removability criterion. K-T 2011 §II.3.1: flat-space constant a_μ
  removable by ψ → exp[if(x)]ψ, f = ā_μx^μ (their eq. (16) passage,
  verbatim); in curved spacetime removable "unless a_μ is constant or the
  total derivative of a scalar," citing Kostelecký PRD 69, 105009 (2004).
  Case A is a direct instance.
- The countershading mechanism and the α-ansatz. K-T 2011 eqs. (184)–(186)
  and their PRL (summary-level): fluctuation locked to h_μν with calculable,
  model-dependent α; observables enter as α(ā_eff)·(potential terms); K-T
  Table II amplitude structure confirms α(ā_eff) as the universal observable
  combination.
- The adjacent known anchor for case A: spontaneous baryogenesis. The operator
  ∂_μθ j_B^μ is inert for exactly conserved B and acts as a chemical potential
  only when B-violation is switched on — Cohen, "Spontaneous Baryogenesis,"
  Nucl.Phys.B 308 (1988) 913–928 (INSPIRE metadata fetched this run,
  first-author field only; Kaplan co-authorship recalled). The khronometric
  version would have μ_B = ζ₁ exactly constant; named as a next object only.

**Not found — the assembled case-B statement is flagged possibly-unremarked:**

- K-T 2011 contains **zero** full-text occurrences of khronon, khronometric,
  Hořava, hypersurface, or foliation (grep of the converted full text this
  session). Their bumblebee analysis is smooth-potential plus nonminimal σ₁;
  gradient or HSO vector backgrounds are never specialized to.
- BPS 1007.3503 §5.2 is on record with exactly the operator, and without the
  distinction. Verbatim: the "more 'dangerous'" class of direct u_μ couplings,
  first example u_μψ̄γ^μψ, "give rise to Lorentz-violating effects within the
  Standard Model as they couple matter fields to the VEV of u_μ"; dimension-3
  and 4 operators of this class "would lead to sizable effects even at low
  energies. On the other hand, the experimental constraints on these effects
  are extremely tight [9]" ([9] = Kostelecký–Russell data tables, bibliography
  verified); their proposed handling is suppression, e.g. "the first operator
  listed in (76) can be forbidden by requiring CPT invariance," with a
  footnote noting non-universality would violate WEP. No conserved-current
  integration by parts, no countershading, no gravitational-window statement
  appears; the paper's single "total derivatives" sentence concerns the
  projectable-lapse gravity Lagrangian, not matter. For the conserved-current
  contraction specifically, the flat-space part of their concern is empty by
  §3's exact nullity — the operator's entire content is the α = 1/2
  gravitational channel. (BPS's caution stands for the rest of their class
  (76), which includes genuinely flat-space-visible c-type operators.)
- Jacobson 0801.1547 (summary-level fetch): matter is assumed minimally
  metric-coupled on phenomenological grounds, "goes against the precepts of
  effective field theory" noted; no current-coupling analysis.
- Carried search bounds from the sourcing map §1f: INSPIRE
  khronometric ∩ "standard-model extension" = 0 records.

**Bounds on the negative claim:** two full texts and two summary-level fetches
this session; WebSearch unavailable (exhausted); no full-text database search
run. A statement of case B under different terminology (Hořava-phenomenology
reviews, SME reviews, technically-natural-LV literature) would evade these
checks. The claim is "not found within these bounds," not "absent from the
literature."

## 6. Consequence for the wave-3 door relabel

- **The ζ₁ conserved-current sub-branch exists for foliations proper.** The
  goal-1 classification's line "countershaded ā_eff [is reachable] only via
  the ζ₁ conserved-current sub-branch" keeps nonzero content for the
  substrate-internal row: a foliation that couples to matter *only* through a
  conserved current sources exactly the countershaded sector, at full
  countershaded strength, and nothing else — no flat-space leakage, no
  fifth-force channel, no c-type percolation from this operator at tree
  level. The sub-branch does not degenerate to generic-vector-only.
- **Non-diagnosticity in detection is sharpened to identity.** The leading
  static signal is α = 1/2 for the whole unit-norm class, foliation or not
  (§4). A countershaded detection would identify "a unit-norm timelike
  background with a current coupling," full stop. This is *even less*
  foliation-diagnostic than wave 3 recorded: not merely "would not by itself
  indicate a foliation" but "numerically identical to the non-foliation case
  at leading order."
- **But the door gains an internal polarity.** Within the countershaded
  channel, twist-type observables (a_eff∧F ≠ 0 signatures) are an exact
  foliation falsifier; E-type-only structure is consistent with (never
  evidence for) a foliation. Proposed amendment to the guardrail rewording
  owned by Swing 1/3 (proposal only, not enacted): door (2b) — countershaded
  ā_eff progress as a non-foliation-specific matter-gravity probe — should
  carry the clause *"twist-component signals in this sector would exclude
  hypersurface-orthogonal backgrounds; E-type signals cannot distinguish
  them."*
- **Consistency with the sourcing map's §3 evenness argument:** ζ₁u_μj^μ is
  odd under u → −u — it is precisely the direct odd coupling whose absence
  that argument requires for (ā_eff) = 0. Nothing here disturbs branch (b)
  (foliation-gravity-only sources nothing countershaded); this gate populates
  branch (a-current) with exact content.

## What This Does Not Claim

- **No experimental bound is derived or claimed.** The MICROSCOPE fold in §3
  is parametric sizing built on recalled numbers (final η, atomic masses) and
  a single-current toy decomposition; the published-methodology species
  analysis was not performed. ζ₁ remains a free parameter with no floor;
  nothing here predicts a nonzero signal.
- **No existence claim about foliations.** The dynamic-unity STOP is
  respected; every statement is conditional on a coupling that no chartered
  model here is asserted to possess.
- **The α = 1/2 pin is leading-PN, static-sector.** Velocity-dependent
  amplitude structure (K-T's V_L, V_⊕ modulations), khronometric-coupling
  corrections O(α_kh, β_kh, λ′), and back-reaction O(ζ₁²) are asserted
  qualitatively, not computed. Adversarial recomputation of the full K-T
  amplitude tables for u = N∂φ is named below, not done.
- **The twist falsifier is in-note analysis**, as are the exchange-force
  contrasts of §4 and every equation not explicitly attributed to a verified
  source. None of it has been adversarially reviewed.
- **The possibly-unremarked flag is search-bounded, not a novelty claim.**
  Components are published (K-T criterion; countershading; BPS operator
  inventory); the assembly may well be folklore among practitioners. Priority
  is claimed for nothing.
- **No claim movement, no charter or guardrail edit.** The door-relabel
  amendment in §6 is a proposal to the Swing 1/3 owners.

## Provenance and unverifiables (must travel with this note)

- **Verified verbatim from locally converted ar5iv full texts this run:**
  K-T 1006.4106 — §II.3.1 including eq. (16) passage and the
  constant-or-total-derivative criterion; eqs. (184)–(186) and the α
  definition sentence; §IV.2.3 WEP passage; §V eqs. (190)–(197) including
  (194), the ζ₁σ₁ sentence, eq. (203), the propagator and fluctuation
  solution (213), the energy-momentum statement (215) with the
  minimal-couplings-cannot-generate sentence; the (0,1) Newtonian-limit
  values; Table II amplitude structure. BPS 1007.3503 — §5.2 eqs. (75)–(79)
  with the dangerous-class passage, footnote 30, and the exchange amplitude
  (80); bibliography identifications ([9] = Kostelecký–Russell 0801.0287;
  akgrav = Kostelecký PRD 69, 105009 (2004)).
- **Extraction layer:** ar5iv HTML converted locally by tag-stripping with
  application/x-tex annotations retained; 15 unconverted math nodes in the
  K-T conversion (none inside quoted passages); the SME tilde-accent macros
  render as layout noise in conversion and were transliterated (ã, B̃) —
  symbol identity unambiguous in context.
- **Summary-level only (not full-text-verified):** Jacobson 0801.1547
  matter-coupling passage; K-T PRL 0810.1459 items (a fetched "α = −4ξ"
  statement was *not* relied on anywhere).
- **INSPIRE metadata:** Cohen, "SPONTANEOUS BARYOGENESIS," Nucl.Phys.B 308
  (1988) 913–928, from the literature API (first-author field only; Kaplan
  co-authorship recalled, not returned by the queried fields).
- **Recalled, unverified:** MICROSCOPE final η(Ti,Pt) ≈ (−1.5±2.3±1.5)×10⁻¹⁵;
  Ti-48/Pt-195 atomic masses (standard values); composition-dependent
  fifth-force reach ~10⁻⁹ of gravity; the electroweak anomaly of baryon
  number; the characterization of data-table a-type bounds as gravitational
  in origin.
- **In-note arithmetic and derivations:** both integration-by-parts
  identities; F = ζ₁dN∧dφ and its Frobenius corollaries; the N = 1 − U
  static solution and the α = 1/2 match; η = ζ₁Δ(B/m) and
  Δ(B/m)(Ti,Pt) ≈ 9.7×10⁻⁴ GeV⁻¹; the conserved-current reduction of K-T
  (213); the exchange-force estimates; the −ζ₁nχ̇ linearization. Each is
  recomputable from the quoted formulas in a few lines.
- **Negative-claim bounds:** greps run this session on the two converted full
  texts (terms: total derivative, conserved current, surface term, redundant,
  countershad-, khronon, khronometric, Horava, hypersurface, foliation);
  summary-level fetch of Jacobson; carried INSPIRE intersection results from
  the sourcing map. No full-text database search was available this session.

## Constructive next objects (named, not built)

1. **Adversarial α-pin check:** recompute the K-T amplitude tables (their
   Tables II–III structure) for u = N∂φ, verifying α = 1/2 propagates to the
   velocity-suppressed modulation amplitudes and locating any component where
   the khronometric background deviates from the one-parameter (185) form.
2. **Twist-falsifier phenomenology:** determine whether existing countershaded
   analyses (torsion-pendulum sidereal fits, MICROSCOPE harmonics) already
   separate E-type from twist-type components, i.e. whether the one-way
   foliation falsifier of §4 is testable in current data or requires a
   dedicated observable.
3. **The khronometric spontaneous-baryogenesis corner** (STOP-check first for
   cosmology scope): with μ_B = ζ₁ exactly constant during B-violating
   epochs, does the lab headroom ζ₁ ~ 10⁻¹² GeV intersect n_B/s ~ 10⁻¹⁰? A
   one-page estimate; would connect the countershaded window to an
   independent observable.
4. **Consolidation seam note** (mailbox proposal, not executed): the BPS
   dangerous-operator inventory and the K-T countershading criterion have an
   unmerged intersection at u_μj^μ for conserved currents; if the assembled
   statement stays unfound under wider search, a short literature comment is
   the natural artifact.
