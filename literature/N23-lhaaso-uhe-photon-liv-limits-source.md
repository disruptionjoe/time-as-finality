# N23: LHAASO UHE-photon LIV limits — Table 1 as printed, and the citation target

## Status

Literature kill-source note. No Time as Finality claim, roadmap, canon, or
priority movement. **Citation discipline for this source:** cite the PRL as
published; an arXiv revision dated 2026-01-10 exists and has *not* been
collated against the PRL here (see below).

## Source

LHAASO Collaboration (Zhen Cao et al., 274 authors), *Exploring Lorentz
Invariance Violation from Ultrahigh-Energy γ Rays Observed by LHAASO*,
Phys. Rev. Lett. **128**, 051102 (2022), DOI 10.1103/PhysRevLett.128.051102;
[arXiv:2106.12350](https://arxiv.org/abs/2106.12350). INSPIRE recid 1869962.
arXiv history: v1 2021-06-23; **v2 2026-01-10**. The PRL (2022) precedes v2.

**Verification depth, per item:**

- **Re-verified 2026-07-28 (this run):** Table 1 in full via the ar5iv
  render — whose generation stamp (2024-03-12) predates v2, so it
  necessarily converts v1, the version the PRL publication tracks; the CLs
  sentence; the γ→3γ attribution sentence; the abstract; the INSPIRE
  publication record; the existence and date of v2.
- **PRL-body-verified in a prior wave (V1 arm, wave-attributed):** the
  per-mechanism attribution of the Table 1 columns and the body-level
  mechanism discussion beyond the sentences quoted here.
- **Not done anywhere yet:** a v2-vs-PRL diff. Until executed, v2-specific
  numbers must not be quoted as this source.

## Table 1 as printed (v1/ar5iv, verified this run)

| Source | L (kpc) | E_max (PeV) | E_cut^95% (PeV) | E_LIV^(1) (×10³² eV) | E_LIV^(2) (×10²³ eV) | E_LIV^(2) 3γ (×10²⁵ eV) |
|---|---|---|---|---|---|---|
| J0534+2202 (Crab) | 2.0 | 0.88 | 0.75 ± 0.043 | 4.04 (+0.73/−0.65) | 5.5 (+0.65/−0.61) | 1.04 (+0.12/−0.11) |
| J2032+4102 | 1.4 | 1.42 | 1.14 ± 0.06 | 14.2 (+2.32/−2.10) | 12.7 (+1.36/−1.29) | 2.21 (+0.22/−0.21) |

In GeV, the second-order (quadratic) 95% CL lower limits:

- **photon decay** (γ → e⁺e⁻): Crab 5.5×10¹⁴ GeV; J2032 1.27×10¹⁵ GeV;
- **photon splitting** (γ → 3γ): Crab **1.04×10¹⁶ GeV**; J2032
  **2.21×10¹⁶ GeV**.

Method sentence, verbatim: "Hence, we adopt the CLs method [Read (2002)] to
derive the 95% CL limit of E_cut." Attribution sentence, verbatim: "The
second-order LIV energy scale reaches 10⁻³ times of the Planck scale, as
derived from the γ→3γ process." Abstract scope sentence: the LIV effect
probed "results in decay of high-energy gamma rays in the superluminal
scenario and hence a sharp cutoff of the energy spectrum" — these are
**superluminal-only** limits.

## What the repo uses this source for

- **The superluminal-uniform half of the Hořava window kill** (in-house
  application; the subluminal half is
  [N22](N22-liberati-maccione-sotiriou-crab-synchrotron-source.md)'s, in
  print 2012):
  [goal1 §5.1 and corrections item 3](../explorations/goal1-model-family-classification-2026-07-27.md).
- **The margin artifact:** the splitting limits against the window's 10¹⁵
  GeV ceiling give the 10–22× closure margin —
  [lhaaso-splitting-margin-verification-2026-07-28.md](../explorations/lhaaso-splitting-margin-verification-2026-07-28.md),
  including why splitting's photon-only external legs moot the
  electron-coefficient escapes.
- **Degeneration condition 1** of the classification's guardrails
  (substantially fired 2026-07-27; goal1 §7).

## Scope and caveats

- Limits are per-source and assume the spectral-cutoff logic of the paper
  (no intrinsic cutoff conspiring at exactly the LIV energy); E_cut^95% is a
  CLs limit on the spectrum, from which the E_LIV rows derive.
- The limits constrain the *photon* sector at linear and quadratic order,
  superluminal sign only; they say nothing about subluminal parameter space
  (that is N22's side) or about matter-sector CPT-odd structure.
- The repo's use composes these numbers with the window's own percolation
  assumption (uniform, unsuppressed transmission to matter); under
  suppressed percolation the composition changes — that branch is
  adjudicated in
  [swing5-suppressed-percolation-adjudication-2026-07-28.md](../explorations/swing5-suppressed-percolation-adjudication-2026-07-28.md).
- The 2026-01-10 v2 exists (abs-page source sizes: v1 36 KB, v2 32 KB;
  contents not examined here). Any future note that needs v2 must diff it
  against the PRL first; nothing in the repo currently rests on v2.
