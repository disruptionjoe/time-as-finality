# Physics from a Finite Observer, and the Observer/System Split as a Bounded Gauge

Framing note (North-Star-level), 2026-07-07 (Joe, chat). **Posture / organizing frame, not a derivation. No
claim moves in any repo. From-memory physics flagged inline.** This states the principle the tri-repo
capability program has been circling, positions the program against GR and QM, and names the one gauge freedom
that both explains the cross-repo resonance and bounds what any of it can claim. Cross-links the candidate
North Star (`Candidate North Star/`), the finality-as-computation note, T12', the two boundary adapters, and
the category-theoretic corrective CT-3.

## The principle: drop the omniscient observer

Traditional models assume an observer who is infinitely removed, unconstrained, exempt from the laws of the
systems it observes, and able to measure without disturbing. **Take the observer to be a finite physical
system instead, and physics falls out of its limitations.** GR and QM are the two classic
observer-finitude theorems; the capability/finality program is a candidate third.

| the observer cannot... | forced structure | honest status |
|---|---|---|
| **outrun a signal** (finite invariant speed) | disagreement on simultaneity of spacelike-separated events -> relativity of simultaneity -> **Special Relativity**; stacked with **can't locally distinguish gravity from free-fall** (equivalence principle) -> general covariance + curvature -> **General Relativity** | GR is TWO stacked limitations, not one; the value of `c` and the field equations are extra inputs. Observer-finitude gives the kinematic frame, not the full dynamics. [from memory] |
| **read without interacting** (same laws as the system) | measurement requires interaction -> a disturbance floor -> the flavor of **Quantum Mechanics** | the disturbance story is the Heisenberg-microscope HEURISTIC. Real uncertainty is kinematic (non-commuting observables / Fourier structure of states) and holds with no measurement; the Hilbert space, complex amplitudes, and Born rule are extra structure. Observer-finitude motivates QM; it does not derive it. [from memory] |
| **individually access, or recompute, all the content** (bounded records; irreducible past) | **finality + the individual<->collective capability wall** | the program's THESIS, not a proven theorem. T12' and TI's F2 are FORCED sub-results (zero-trace capability walls); whether they add up to a finality theorem is the open question below. |

The honest cap on the whole table: **observer-finitude is a powerful organizing principle and a genuine
PARTIAL derivation, not a complete derivation of any of the three from observer-limits alone.** It organizes
and motivates; the specific physical constants and structures are additional inputs.

## The observer/system split is a gauge -- and it is bounded

To collapse the full multiway system (the ruliad) to one coherent thread of experience, an observer must make
equivalences between paths (coarse-graining; the Knuth-Bendix completion of Gorard's model). That observer's
sophistication can be arbitrarily high. So there is a **conserved total with a free split**:

> (computation done by the SYSTEM) + (computation done by the OBSERVER) = the observed behavior,
> and only the TOTAL is observable. **The split is gauge.**

Trivial-observer/all-system and trivial-system/all-observer are the two gauge extremes; the whole interstitial
range is unobservably free. (Gorard's argument.)

- **This is the empiricist/rationalist debate, dissolved.** Empiricism (Locke, Hume) puts the computation in
  the SYSTEM (the world is structured; the mind reads). Rationalism (Descartes, Berkeley) puts it in the
  OBSERVER (the mind structures raw input). Kant answered "both"; the computational version is sharper -- a
  **continuous gauge with no privileged point**, so the debate was never decidable because it was a
  gauge choice all along. Kin to underdetermination-of-theory-by-data and theory-ladenness-of-observation,
  now with a mechanism. [philosophy from memory]
- **But the gauge is bounded, and bounding it is this program's real job.** An arbitrarily sophisticated
  observer can carry all the burden; a FINITE observer cannot. A bounded observer provably cannot perform
  arbitrarily sophisticated equivalencing (the `C(R)` capability bound; the state-space / complexity lower
  bounds from `explorations/finality-as-computation-state-vs-attention-2026-07-07.md`). So the split is free
  **only up to the observer's capability.** The capability framework does not RESOLVE the observer/system
  gauge; it **fences** it. Empiricist and rationalist may trade burden freely, but neither may hand the
  observer more computation than a finite observer can run.

## What this fixes and what it costs us

- **Finality is gauge; the records are the invariant.** Is the past fixed because the SYSTEM finalized it or
  because the OBSERVER coarse-grained it into a fixed record? Observationally indistinguishable. So finality
  lives in the observer/system gauge, and the **gauge-invariant** content is the record/capability structure.
  This is exactly why TaF has always said finality is *observer-relative* while the records are *real*
  (guardrails G1/G3): those are the statements that finality is gauge-dependent and the records are gauge-
  invariant. The frame grounds the posture instead of merely asserting it.
- **Correction to the open theorem.** The question posed earlier -- "does bounded-observer record-finitude
  FORCE finality?" -- is sharpened by the gauge: it can force finality only **up to gauge**. What would be
  forced and real is the record/capability structure (the invariant); which side you attribute the finalizing
  to is free. **Open theorem:** does bounded-observer record-finitude force the gauge-invariant record
  structure that TaF calls finality? T12' and F2 are forced fragments of it; the theorem is unproven.
- **The realism correction (Deutsch's dinosaur) -- corrects an over-hasty CT-3 deflation.** An earlier draft
  of this note slid from "the observer/system split is not directly perceivable" to "therefore it is a gauge
  CHOICE, not a fact -- the capability framework is not 'the truth.'" **That is the verificationist mistake.**
  No one has seen or will see a dinosaur; the fossils are explained by a model that logically IMPLIES
  dinosaurs, and that implication IS the evidence (Deutsch). Unobservability of a distinction does not demote
  it to a choice -- most of science is unobservable-but-real by inference to the best explanation. The correct
  criterion: **a distinction is real if the BEST explanation requires it**, where "best" = **hard to vary**
  (unifying, no ad-hoc dials), not merely empirically adequate.
  - *Rescues the program from self-deflation.* The capability framework is a candidate EXPLANATION, real to the
    degree it is the hardest-to-vary account of the invariant records -- the realism that makes paleontology
    knowledge, not geology. If unobservability demoted it to "choice," the framework would be self-undermining.
  - *Corrects the use of CT-3.* CT-3 ("equivalent presentations -> the invariant cannot move") is legitimate
    ONLY when the equivalence is PROVEN (all consequences identical -- e.g. the genuine Quillen equivalence in
    the substrate-thesis case, where the count-obstruction really cannot move). The observer/system split is
    NOT proven-equivalent; it is UNDERDETERMINED by current data -- a live question decided by best
    explanation, not a gauge. Reading "gauge" off "no observed difference" is the dinosaur mistake. (See the
    CT-3 dinosaur guard added to the methodology registry.)
  - *The genuinely-gauge category still exists* (PROVEN symmetries: coordinate choice, a real categorical
    equivalence) and there there is no fact of the matter -- but membership is decided by explanatory
    difference, NOT by perceivability. The non-triumphalism survives in its correct form: do not mistake a
    proven-equivalent presentation for a fact; but do not mistake an unobservable-yet-explanatorily-required
    structure for a mere choice either.

## The operational payoff (folded into the adapter work)

The observer/system gauge is the **manufactured-convergence knob**. In the two-adapter build one could
attribute the individual<->collective boundary to the system (GU's Krein structure) or to the observer (the
capability reading) and tune the split to make the adapters agree. So **"de-correlation" of the two adapters
means, concretely, fixing the observer/system gauge INDEPENDENTLY on each side**: `F` fixes it via GU physics
(T12'), `S` via TI source-logic (F2); if those independently-set splits coincide the agreement is real, if
they share one tunable knob it is gauge (manufactured). This is folded into
`open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`.

## Discipline (the anchor)

The **split** is free; the **total** (observed behavior, records) is invariant; the **capability bound**
fences the split. That triple is what keeps this from collapsing into "it is all gauge, nothing is real."
The gauge is also the manufactured-convergence risk itself -- and the test is **explanatory, not perceptual**:
manufactured convergence is a BAD explanation (EASY to vary -- the split/encoding was dialed until the pieces
agreed), real convergence is HARD to vary (each side forced independently, no free dial). So any cross-repo
agreement is judged by whether it is hard-to-vary under independently-fixed gauges, NOT by whether the
difference is perceivable (the verificationist trap). Single-process caution: this frame and the programs it
organizes are one research process; it is an organizing lens, not evidence.
