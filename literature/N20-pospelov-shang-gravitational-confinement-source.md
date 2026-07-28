# N20: Pospelov–Shang — the gravitational-confinement mechanism, and its own quadratic-divergence concession

## Status

Literature kill-source note. No Time as Finality claim, roadmap, canon, or
priority movement. This note exists so that the classification campaign's
load-bearing citations of this paper resolve inside the repository rather
than to chat-wave memory.

## Source

Maxim Pospelov & Yanwen Shang, *On Lorentz violation in Hořava-Lifshitz type
theories*, [arXiv:1010.5249](https://arxiv.org/abs/1010.5249), Phys. Rev. D
**85**, 105001 (2012), DOI 10.1103/PhysRevD.85.105001. Cited across the repo
as "P-S". arXiv history: v1 2010-10-25, v2 2010-12-02, v3 2011-11-14; the v3
comments field states the gauge-choice independence of the main conclusion
was proven in revision and "a new extension that could improve the original
model, which completely eliminates the need of fine-tuning, is proposed."

**Verification depth:** full ar5iv text fetched, converted, and
quote-verified in the swing-5 run — see the Provenance section of
[swing5-suppressed-percolation-adjudication-2026-07-28.md](../explorations/swing5-suppressed-percolation-adjudication-2026-07-28.md),
which lists P-S Eqs. (1)–(5), (30), (55), (57), (59) and the §4/§5/§6
passages as verified verbatim (two passages recovered from raw HTML alttext
after conversion truncation). This note's abs-page data (versions, abstract,
DOI) re-fetched 2026-07-28. Quotes below are reproduced from the swing-5
verified set, with locations.

## What the paper proposes (the mechanism the repo's leaking branch lived on)

The setup (Eq. (2)): a Lorentz-violating sector coupled to the Standard
Model only through power-suppressed operators. Generic outcome (Eq. (3)): a
power-divergent loop transfers O(1) LV into d = 4 matter operators. The
proposed stabilizer is Lifshitz scaling of the *gravity* propagator
(Eq. (4)), giving the mechanism sentence (§1):

> "If, however, a theory of this type is coupled to SM sector through
> power-suppressed interactions only, it is conceivable that the size of
> induced LV terms in SM is controlled by the ratio Λ_HL²/M² and can be made
> small, given a sufficiently large separation between Λ_HL and M. There
> would be no need of fine-tuning since radiative corrections become
> stabilized so that Λ_HL ≪ M alone would be sufficient."

Target scaling (Eq. (5)): Δc ∼ Λ_HL²/(π² M_pl²). Scale requirement (§6,
first Discussion bullet): "one would need to have Λ_HL ≲ 10¹⁰ GeV."
Their Option 1 (matter also Lifshitz) is rejected up front on fine-tuning
grounds (§1: non-universality "of the order of α_SM/π ∼ 10⁻³–10⁻², which has
to be tuned away at 1 part per 10²⁰"); Option 2 (gravity-only Lifshitz) is
the gravitational-confinement proposal — the name is LMS's
([N22](N22-liberati-maccione-sotiriou-crab-synchrotron-source.md)).

## The concession: Eq. (55) and §5, in the authors' own words

The one-loop physical speed difference (their Eq. (55)) contains, alongside
two controlled logs, an uncancelled term −Λ_UV²/(24π² M_pl²). Their §4:

> "The second term above is quadratically divergent, leading to a residual
> fine-tuning problem in this model as we discuss further below. This
> divergence is the direct consequence of the non-Lifshitz behavior of
> propagators for the spin-1 gravitons."

And §5, unhedged:

> "This poses serious problem since the model has essentially no natural
> protection against large Lorentz violation in the matter sector, and
> therefore tremendous amount of fine-tunning is required to keep the model
> consistent with observations. This quadratic divergence in
> δc²_photon − δc²_scalar means that our proposal based on a large scale
> separation Λ_HL/M_pl ≪ 1 to protect the Lorentz symmetry in the Standard
> Model does not work, and we must modify the theory in order to remove such
> remaining divergence." [spelling as printed]

The proposed repair (Eq. (57)) is the mixed-derivative term
ℒ′ = (2/Λ²)∇^i K_ij ∇_k K^kj, after which the divergences are logarithmic
(Eq. (59)); the paper itself flags residual risk in §1: "The model, on the
other hand, might still harbor additional problems associated with the new
terms we introduce." That is where CCGS 2016 later struck (fourth
scalar graviton, IR-unstable — see
[N21](N21-coates-melby-thompson-mukohyama-percolation-robustness-source.md)).

## What the repo uses this source for

- **Swing-5 row-1 kill:** the registered kill on gravitational confinement
  *as published* fires by P-S's own Eq. (55)/§5 — the unextended mechanism
  requires the d = 4 counterterm tuning it was invoked to avoid
  ([swing5 §1b, §5 row 1](../explorations/swing5-suppressed-percolation-adjudication-2026-07-28.md)).
- **The Λ²/M_Pl² suppression class** is the sole survivor class of the
  Hořava uniform-percolation window closure
  ([goal1 §5.1](../explorations/goal1-model-family-classification-2026-07-27.md));
  this paper defines that class.
- **The confinement ceiling:** evaluating their Eq. (55) log term against
  Δc ≤ 10⁻²⁰ gives Λ_HL ≲ 4×10⁸ GeV (swing-5 in-note arithmetic), an input
  to the review-window inconsistency finding (swing5 §3d).

## Scope and caveats

- The kill this source powers is scoped to the mechanism *as published*;
  P-S's own repair (Eq. (57)) moves the dispute to the CCGS/CMM literature
  and to the projectable branch, where the decisive calculation is
  unexecuted (see N21 and the standing monitorables note).
- P-S deferred induced d = 6 operators ("worth of a separate investigation,"
  §6); LMS's "expected to be the case for higher order operators as well"
  was an expectation, never a calculation (swing5 §2).
- Equation numbers are as rendered by ar5iv; the extraction layer and
  truncation-recovery flags of the swing-5 provenance section travel with
  every quote above.
