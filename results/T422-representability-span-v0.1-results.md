# T422 - Representability Span of the Forcing Modes (E1 / E2 / E3) - v0.1 results

> Recorded-tier exploratory big-swing. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the spec header (the
> numbering automation normalizes any collision later). NO claim promotion;
> ledger actions pause for Joe. Cross-domain material (Cech cohomology,
> computational complexity, CRT / quadratic residuosity) is the OBJECT OF STUDY,
> never evidence for physics or a sibling repo. One-way rule holds (GU adjacency
> only). Not committed.

- Spec (frozen first): `tests/T422-representability-span.md`
- Model: `models/representability_span.py`
- Tests: `tests/test_representability_span.py` (14 asserts, all pass, ~2.4 s)
- Artifact JSON: `results/T422-representability-span-v0.1.json`
- Run: `python -m pytest tests/test_representability_span.py -q`

## Predeclared claim (tested)

Physical forcing modes do NOT form a hierarchy / interconvertible lattice. E1
(asymptotic-limit) and E3 (structural-symmetry) share ONE local-to-global
representative (a Cech H^1 index); E2 (computational-hardness) admits NO such
functorial representative because hardness is presentation-dependent. Hence the
three forcings are NON-INTERCONVERTIBLE, with E2 the categorical obstruction.

## Verdict: GO (qualified) - finite-witness span holds; two scope corrections

The load-bearing thesis survives all four success legs AND six adversarial
attacks: **no kill fired** (no E2 invariant found; no E2<->E1/E3 conversion
found; the core is not circular; not fully pre-empted). The finite witness is
real at synthesis tier. It is a **qualified** GO, not a clean one - the
adversarial pass forced two honest scope corrections (see "Adversarial review"
and "Scope corrections"), which are recorded here rather than buried.

| leg | result |
| --- | --- |
| S1 common invariant (E1+E3) | PASS |
| S2 E2 non-representability, exhibited | PASS |
| S3 non-interconvertibility monotone | PASS (category-relative - see correction 2) |
| S4 falsifier stated, does not trigger | PASS |
| K1..K5 kills | none fired |

## S1 - the COMMON local-to-global invariant (with numbers)

ONE coefficient-generic engine `cech_h1` computes H^0/H^1 of the nerve of a
triangulated circle C_4. H^1(C_4; A) = A via the loop-sum (winding) map. E1 and
E3 call the IDENTICAL function; only the coefficient group changes.

- **E1 (A = Z, mod=0)**: transition 1-cochain with one unit twist on the wrap
  edge. Computed class: `h0 = 1`, `n_independent_cycles = 1`, **winding w = 1**,
  `h1_trivial = False`. Genuinely global: all **14 proper subcovers trivialize**
  (`some_proper_subset_witnesses_class = False`) - a global section with no local
  witness. Refinement-stable: n->2n gives `refined_winding = 1`. Iso-invariant
  under cyclic rotation.
- **E3 (A = Z/2, mod=2)**: SAME cover, sign-local-system transition. Computed
  class: `h0 = 1`, **monodromy = 1**, `h1_trivial = False`. All 14 proper
  subcovers trivialize; refinement-stable (`refined_winding = 1`).
- **T412 cross-check**: the E3 no-local-witness pattern reproduces T412's
  independently-measured Z/2 parity fact - `max_proper_subset_witness = 0.0`,
  `full_joint_separates = 1.0`, `matches_T412 = True`.

Same function, `winding = 1` in both; the ONLY difference is `mod = 0` (Z) vs
`mod = 2` (Z/2). This is the literal same-functor/different-coefficient object
that retro-predicts **T421's Z-vs-Z/2 bifurcation**. The common home is not
gerrymandered: it is one call to the same routine, H^1(C_n;A)=A is textbook, and
"no local witness" is checked exhaustively over every proper subcover. K2 does
not fire.

## S2 - E2 non-representability, EXHIBITED (not by fiat)

Object (unchanged T417 Goldwasser-Micali construction): units mod N=77=7*11 with
the QR 2-coloring; x_A = 58 (QR), x_B = 24 (non-QR, Jacobi +1). Two presentations
related by the CANONICAL CRT ring iso phi(x) = (x mod 7, x mod 11).

**Circularity guard A - phi is a genuine ring iso** (verified elementwise over
all of Z/77 and 3600 unit pairs): bijective, preserves +, preserves *, preserves
QR-ness on units. `is_genuine_ring_iso = True`.

**Circularity guard B - STEP-1 positive control** (the load-bearing anti-K3
device): run the Cech routine on the QR-coloring cover under BOTH presentations.
Both return **H^0 = 2** (two color classes), **H^1 = 0**. `cech_invariants_equal
= True`. The object HAS presentation-independent Cech invariants - it is NOT
pathological. What then fails to be an invariant is specifically the HARDNESS
verdict.

**The flip** (across the verified iso, on the demonstrably well-behaved object):

| presentation | feasible local predicate | on x_A / x_B | verdict |
| --- | --- | --- | --- |
| P1 (N-coords) | Jacobi(x, 77) | +1 / +1 (identical) | **FORCED** |
| P2 (CRT-coords) | per-factor Legendre (x/7),(x/11) | (+1,+1) / (-1,-1) | **DECLARED** |

`verdict_flips_across_iso = True`. Because the flip is across the object's OWN
canonical ring iso - under which every genuine Cech invariant is preserved - the
presentation-dependence is exhibited, not stipulated. It is textbook QRA content
(hard mod N, easy mod the factors), so K3 does not fire.

**Deformation scan** (no index conservation): forcing indicator over N in
{77, 79, 91, 143, 899} = {1, 0, 1, 1, 1}. It jumps to 0 at the prime N=79 with no
compensating ker/coker exchange - forcing is discontinuous, unlike a conserved
index.

**Two-horn dilemma** (closes the "you smuggled the trapdoor into the easy
presentation" objection): either CRT is a free morphism (then a functorial
invariant must be CRT-invariant, but hardness is not) or CRT is declared
not-a-morphism (then hardness is admitted to depend on presentation). Both horns
are the conclusion.

## S3 - the non-interconvertibility monotone

delta(toy) = 0 iff the toy's natural boundary-quantity is unchanged under BOTH
cover refinement AND object isomorphism, else 1.

- **delta(E1) = 0**, **delta(E3) = 0** (winding invariant under refinement and
  rotation), **delta(E2) = 1** (forcing verdict flips under CRT and is
  discontinuous under N-deformation). `separates_E2_from_E1E3 = True`.
- **Argument**: delta is preserved by the free operations (cover refinement,
  object isomorphism) by the Cech-colimit definition - any quantity that IS a
  Cech class has delta=0. E1/E3 are Cech-representable (delta=0); E2 hardness is
  not (delta=1). Free ops preserve delta, so no free operation crosses the line.
  E2 is the categorical obstruction. The T110 orbit lemma (a scalar nondecreasing
  on every orbit edge is constant on the orbit) holds (`t110_orbit_lemma_holds =
  True`) as the independent reason indices descend and E2 cost does not.
- **Matched-battery positive control** (anti-rig): the same iso battery returns
  delta=0 on E1/E3, and T412 independently shows **48/48** product-structure-
  preserving relabels preserve the Z/2 separator (`survives = True`). If the
  battery were rigged to eject E2 it would eject E3 too; it does not. K4 does not
  fire.

## S4 - the falsifier (stated; does not trigger)

**Falsifier**: exhibit a single quantity computed from (x, N) that is BOTH
CRT/refinement-invariant AND tracks the QRA hardness gap (FORCED != DECLARED).
Such a quantity would be a functorial / homotopy representative for E2 - the span
collapses (K1).

Pre-registered candidate enumeration - each is invariant-but-blind OR
tracking-but-discontinuous, none is both:

| candidate | phi-invariant | tracks hardness |
| --- | --- | --- |
| spectral gap of the C_n cover operator | yes | no |
| minimal-circuit-size proxy for QR | no | yes |
| family cost-growth index (trial-division steps) | no | yes |
| description-length proxy (bit-length of N) | yes | no |
| Cech winding of the coloring cover | yes (H^1=0, positive control) | no |

`candidate_that_is_both = []`, `falsifier_triggers = False`. A test
(`test_s4_falsifier_would_fire_if_a_both_candidate_existed`) guards the guard: if
any candidate were both, the search MUST report firing.

## Honest scoping (binding ceiling; steering-risk callouts)

- **NOT a universal theorem.** This is a finite-witness demonstration + a
  colimit-invariance argument-sketch + a stated falsifier. "No functorial
  invariant exists for E2 in general" is NOT proven and was not attempted.
- **E1 forcing is asymptotic.** The finite winding w=1 is an explicit PROXY for
  the no-local-witness STRUCTURE (refinement-stability is the finite E1-flavor
  signature), not the divergence itself. Stated, not hidden.
- **Weakest surface - the falsifier candidate table.** Three of the five
  candidate booleans are an argued (pre-registered) enumeration rather than a
  fully computed measure; two are grounded in computation (the Cech-winding row
  via the STEP-1 positive control; the trial-division cost-growth via T417). This
  is inside the honest ceiling (argument-sketch), but it is the place a
  determined reviewer should push first.
- **Category caveat.** The separation lives in the cost-blind category
  (isomorphisms / refinements). A reviewer insisting on the poly-time-reduction
  category declines the claim's category rather than refuting it - and there the
  E1/E3 indices are not preserved either. Shared by the whole construction; a
  scope statement, not a defense.
- **Steering risk (self-audit).** The claim was framed by the orchestrating
  persona, so "build the toys to confirm by construction" was the live risk. The
  two structural guards that make this non-circular are NOT under the toy's
  control: (i) the STEP-1 positive control could have returned unequal Cech
  invariants (K3) and did not - it returned (2,0)=(2,0) because phi genuinely
  preserves the coloring; (ii) the winding is textbook H^1(C_n;A)=A checked over
  all 14 proper subcovers, not a bespoke scalar. The flip is textbook QRA, not a
  toy artifact. The residual by-fiat surface is the falsifier table (flagged
  above).

## K5 prior-art concession (up front)

The general no-go component is essentially known: complexity / circuit-size is
not a homotopy / functorial invariant (Immerman-Vardi logic-for-P
order-dependence; Goldwasser-Micali computational indistinguishability). Those
are cited, not claimed. The novelty here is confined to the cross-application to
FINALITY / forcing-modes - the E1=E3 common-coefficient realization and the
E2-as-categorical-obstruction framing - which is **synthesis-tier**, not a novel
general theorem.

## Adversarial review (six attacks; did the kill FIRE?)

Six independent adversarial passes. "Kill fired" = the attack met its own
break-criterion (would force ABANDON). None did; three landed genuine partial
dents that are converted to scope corrections below.

| # | attack | verdict | kill fired? | what it establishes |
| --- | --- | --- | --- | --- |
| 1 | **e2-invariant-exists** (build a functorial/homotopy invariant that is phi-invariant AND reproduces FORCED/DECLARED) | survives | **NO** (K1) | Structural failure to find one: any iso-invariant quantity is single-valued on the iso class, but the verdict *flips* across it (`verdict_flips_across_iso=True`). Pseudosquare count (=15) and QR-ness are genuine phi-invariants but identical on both presentations - they vindicate the claim (invariant residue preserved; hardness is the non-invariant leftover). Conf 0.85. |
| 2 | **e1e3-index-engineered** (show the common home is fake / not local-to-global) | partial | **NO** (K2) | The invariant TYPE is genuinely shared and genuinely local-to-global (all 14 proper subcovers trivialize; refinement-stable) - that leg holds. BUT the *sharing* is near-tautological: E1/E3 use the LITERALLY identical nerve + cochain, differing only mod 0 vs mod 2; `H^1(C_n;A)=A` holds for *any* A (checked mod {0,2,3,5,7,13}, winding=1 in all), so nothing structurally *selects* Z/2 for E3. -> **Correction 1.** Conf 0.70. |
| 3 | **free-conversion search** (find a free op crossing any edge) | partial | **NO** | E2 boundary is uncrossable (the load-bearing leg): no free op carries E2 forcing to an index; E2's genuine Cech invariant is trivial and tracks no forcing. BUT a real one-way free conversion E1->E3 DOES exist (coefficient reduction Z->Z/2 carries winding 1 -> monodromy 1), because the toy builds both from the identical nerve. Dents the *blanket* "all three non-interconvertible." -> **Correction 1.** Conf 0.62. |
| 4 | **circular-toy** (is the separation an artifact of construction?) | partial | **NO** | S1 (shared H^1 index) and the S2 *local* fact (hardness flips across verified CRT iso) are genuinely non-circular. BUT the *decisive* delta monotone is a category equivocation: E1/E3 get a cost-BLIND quantity (winding, delta=0), E2 gets a cost-SENSITIVE quantity (feasibility, delta=1). `is_qr_mod_N` is itself a phi-invariant that separates x_A/x_B in the *same* cost-blind category - so E2's obstruction is *feasibility*, not *invariance*. No single category makes E1/E3 representable while E2 is not. -> **Correction 2.** Conf 0.68. |
| 5 | **prior-art** | partial | **NO** (K5, conceded up front) | Core pre-empted on both prongs: "complexity is not a homotopy invariant" (Immerman-Vardi, Goldwasser-Micali; arXiv:1112.0812) and "resource theory separating computational from thermodynamic forcing" (Gour-Spekkens; Coecke-Fritz-Spekkens categorical resource theories; arXiv:2501.15950 Thermodynamic-Complexity Duality, which advances the *opposite* embedding thesis). Un-pre-empted: only the FINALITY cross-application (E1/E2/E3 forcing labels, the E1=E3 common-coefficient realization, the T419/T421 retro-prediction). Conf 0.80. |
| 6 | **correctness** (independent re-run with sympy) | survives | **NO** | 14/14 pass; every computed quantity exactly re-derived independently (H^1(C_4;A)=A; N=77=7*11; x_A=58 QR, x_B=24 non-QR both Jacobi +1; deformation scan {77:1,79:0,91:1,143:1,899:1} matches `factorint`). Only by-fiat surface is the falsifier candidate table (a soundness matter, not an arithmetic error). Conf 0.90. |

**Net:** the load-bearing claim - **E2 is the categorical obstruction; no free
operation converts E2 forcing into an E1/E3 index; E1/E3 share a genuine
no-local-witness H^1 home** - survives all six. Attacks 2, 3, 4 land real dents
on the *supporting* apparatus, not the core, and are converted to corrections.

## Scope corrections (forced by the adversarial pass; binding)

1. **The blanket "all three forcings are non-interconvertible" is too strong.**
   E1 and E3 admit a genuine *one-way* free conversion: change-of-coefficients
   Z -> Z/2 (reduction mod 2) carries E1's winding class (=1) onto E3's monodromy
   class (=1). There is no natural Z/2 -> Z inverse, so it is lossy/one-directional
   (which is exactly why T421's iso-disanalogy stands). This does NOT falsify the
   thesis - it lies *inside* the E1/E3 pair the claim already unifies as sharing a
   "common representative," and it corroborates E1~E3. **Corrected statement:**
   *E2 is non-interconvertible with E1/E3 (the load-bearing separation); E1 and
   E3 are cohomologically cognate and admit a one-way coefficient reduction
   E1 -> E3.* Relatedly, nothing in the toy structurally *selects* Z/2 for E3
   over any other coefficient group - the "Z-vs-Z/2 bifurcation" that
   retro-predicts T421 is a *label/coefficient choice*, not an independently
   forced structural fork. Honestly downgraded from "structural fork" to
   "coefficient-realization consistent with T421."

2. **The delta separation is category-relative, not category-free.** The
   monotone assigns E1/E3 a cost-blind quantity and E2 a cost-sensitive one. In
   the *cost-blind* category, E2 also has a phi-invariant representative
   (`is_qr_mod_N` separates x_A/x_B) - so E2's non-representability is a statement
   about *feasibility/efficient computability*, not about invariance per se. In
   the *poly-time-reduction* (cost-sensitive) category where E2 genuinely fails,
   E1/E3's indices are *also* not preserved. **There is no single category in
   which E1/E3 are representable and E2 is not.** The separation is therefore
   real but *category-indexed*: E1/E3 are representable-and-cheap; E2 is
   representable-but-expensive / cheap-but-non-invariant. This is the honest
   residue of confirm-by-construction and it caps the result at **finite-witness
   synthesis tier**, not theorem. (Half-conceded already in the Category caveat;
   promoted here to a binding correction.)

## Prior-art outcome

The general machinery is **pre-empted** (partial, not a break): the
invariant-vs-cost-of-computing-invariant distinction and the resource-theoretic
non-interconvertibility apparatus (free ops / interconvertibility order /
separating monotones, including the "categorical obstruction" framing) are both
published. A live *counter-thesis* exists (arXiv:2501.15950 embeds computational
hardness AS a thermodynamic coordinate - the opposite of non-interconvertibility).
**Un-pre-empted and genuinely novel:** only the narrow cross-application to
finality - the E1/E2/E3 forcing-mode labeling, the E1=E3 common-coefficient
Cech-H^1 realization, and the T419/T421 retro-prediction. The build does not
oversell this (K5 conceded up front). Novelty is real but **synthesis-tier and
domain-local**, not a new general theorem.

## Recommendation: GO (qualified, finite-witness / synthesis tier)

**GO**, with the two scope corrections binding. Rationale, weighed against the
ABANDON triggers:

- *E2 invariant found?* No (attack 1 survives). -> not ABANDON.
- *Conversion exists?* Only the E1 -> E3 one-way coefficient reduction, which is
  *inside* the already-unified pair and corroborates it; no E2<->E1/E3
  conversion (attack 3). -> not ABANDON.
- *Circular?* The core (S1 + S2-local) is non-circular; only the decisive
  monotone is category-relative (attack 4). -> correction, not ABANDON.
- *Fully pre-empted?* No - the finality cross-application is un-pre-empted
  (attack 5). -> not ABANDON.
- *Kill fired?* None (K1-K5). -> not REDESIGN.

The finite-witness span holds *as corrected*: E1 and E3 share a genuine
local-to-global (no-local-witness, refinement-stable) H^1 home; E2 is genuinely
non-representable *by any phi-invariant that also tracks the hardness gap*, with
the FORCED/DECLARED flip surviving an independently-verified CRT iso and an
independent sympy re-derivation; E2 is the categorical obstruction to
unification and no free operation carries its forcing to an index. The
un-pre-empted meta-object (a representability-stratified resource theory of
*forcing itself*, applied to finality) is real at finite-witness tier and
retro-predicts the arc's two honest negatives (T419, T421).

What a GO does NOT license: promotion to "E2 admits no functorial invariant in
general" (a universal theorem, not attempted), any claim-ledger movement, or the
blanket non-interconvertibility phrasing (corrected). The honest weakest surface
remains the S4 falsifier candidate table (argued, not fully computed) and the
category-relativity of the separation (correction 2). Pauses for Joe.

## What this does and does not license

- Licensed (recorded, synthesis-tier): a finite witness that E1/E3 carry a
  common Cech-H^1 index while E2 hardness carries none, and a monotone delta that
  separates them - a concrete, falsifiable articulation of the
  representability-span picture, consistent with the honest negatives T419 and
  T421.
- NOT licensed: any claim-ledger movement, any promotion of "E2 has no functorial
  invariant" to a theorem, any cross-repo evidential use. Pauses for Joe.
