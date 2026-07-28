# N24: Donadi et al. — the underground Diósi–Penrose bound, verified, with an arXiv-identifier correction

## Status

Literature source note for the classification's bin-1 rate family. No Time
as Finality claim, roadmap, canon, or priority movement. **Carries one
correction to the wave record:** the arXiv identifier circulating with this
citation (2011.04865) is wrong; the correct eprint is **arXiv:2111.13490**.

## Source

Sandro Donadi, Kristian Piscicchia, Catalina Curceanu, Lajos Diósi, Matthias
Laubenstein & Angelo Bassi, *Underground test of gravity-related wave
function collapse*, Nature Physics **17**, 74–78 (2021), DOI
10.1038/s41567-020-1008-4; [arXiv:2111.13490](https://arxiv.org/abs/2111.13490).
INSPIRE recid 1840699.

**Identifier divergence, resolved this run (2026-07-28):** arXiv:2011.04865
— the identifier attached to this citation in the wave record — resolves to
an unrelated cs.SI paper ("Scoring Popularity in GitHub," Al-Rubaye &
Sukthankar, 2020). The INSPIRE record for the exact title confirms
2111.13490 as the eprint of the Nature Physics paper. Any downstream file
carrying 2011.04865 for Donadi et al. should be corrected on next touch.

**Verification depth:** ar5iv full text of 2111.13490 fetched this run;
abstract and the bound-stating sentences verified verbatim; INSPIRE
publication record fetched this run. This is a this-run primary
verification, not a wave-attributed one.

## What the paper establishes (verified verbatim)

Setup: a coaxial p-type high-purity germanium detector (375 cm³ active
volume), heavily shielded, at the Gran Sasso underground laboratory (LNGS),
62 days of exposure. The Diósi–Penrose (DP) gravity-related collapse model
predicts spontaneous radiation emission from charged particles undergoing
collapse-driven diffusion; the paper computes the emission rate and compares
with the measured spectrum. Abstract, closing sentences:

> "Our result sets a lower bound on the effective size of the mass density
> of nuclei, which is about three orders of magnitude larger than previous
> bounds. This rules out the natural parameter-free version of the
> Diósi-Penrose model."

The quantitative bound, as stated in the text:

> "R₀ > 0.54×10⁻¹⁰ m with probability 0.95"

i.e. R₀ > 0.54 Å at 95% probability on the DP regularization length (the
effective size of the nuclear mass density), against the "natural"
parameter-free choice of R₀ at nuclear size (~10⁻¹⁵ m), which is excluded by
orders of magnitude. Conclusion sentence, verbatim:

> "Therefore, we conclude that Penrose's proposal for a gravity-related
> collapse of the wave function, in the present formulation, is ruled out."

**Scope note verified against the text:** the paper states *no* numerical
CSL/GRW parameter bounds. Its instrument class (underground low-background
γ/X-ray spectroscopy of collapse-induced spontaneous emission) is the same
class that bounds CSL-type rates, but those bounds live in companion
literature (the same group's X-ray emission analyses), not in this paper.

## What the repo uses this source for, and the goal1 §3 check

[goal1 §3.1](../explorations/goal1-model-family-classification-2026-07-27.md)
cites this paper as the worked example of a pinned collapse-rate parameter:
"Bounded by underground spontaneous X-ray emission: Donadi, Piscicchia,
Curceanu, Diósi, Laubenstein & Bassi, *Nature Physics* 17, 74 (2021) pinned
the Diósi–Penrose parameter this way." **Check result:** goal1 quotes no
numbers for this source, so there is no numeric divergence to flag in goal1;
the bibliographic citation (journal, volume, page, year, authors) is
correct. Two precision items are recorded here rather than there: (i) the
pinned parameter is the DP length R₀ (> 0.54 Å at 95%), with the
parameter-free version excluded; (ii) goal1's adjacent clause "the same
instrument class bounds GRW/CSL-type rates [feed]" is right about the
instrument class but should not be read as a claim of this paper, which
bounds DP only.

Downstream uses: the bin-1 universal-rate row of the classification table;
the rival map's GRW/CSL/DP entry
([rival-map-2026-07-28.md](../explorations/rival-map-2026-07-28.md)); the
rate-vs-tick axis guard (a pinned *rate* parameter is not evidence of a
foliation — the fourth-category guard, Tumulka rGRWf).

## Scope and caveats

- The DP exclusion is of the parameter-free version "in the present
  formulation" — the authors' own hedge; dissipative/regularized DP variants
  with larger R₀ survive by construction.
- The bound is model-mediated through the computed emission rate; the
  paper's own systematic discussion travels with it.
- Nothing here bears on foliations, preferred frames, or the update layer;
  this source lives entirely in the rate family (goal1 §1's rate-vs-tick
  axis).
