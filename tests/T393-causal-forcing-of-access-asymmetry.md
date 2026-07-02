# T393: Causal Forcing of the Access Asymmetry

## Route

Quantum measurement / classical records / causal structure.

## Claim

The T392 access asymmetry is **forced, not engineered**, when the
record-carrying degree of freedom is an emitted mode that propagates out of
the apparatus's causal control region. T392's stipulated access triple for the
extra-environment structure — (i) outside the declared fragment family,
(ii) outside the coherent undo set, (iii) readable by the auxiliary channel —
then becomes a consequence of light-cone geometry: (i) the declared fragment
family is principled (records inside the control region); (ii) the undo set is
principled (**all** operations supported on the control region, not a protocol
restriction); (iii) readability is principled (a downstream detector
intersects the escaped mode's forward cone). If this holds, the T392 existence
result is upgraded from Tier 3 (engineered) to Tier 1 (causal), **conditional
on emission occurring**.

## Class

Subclaim of [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md);
forcing upgrade for the T392 witness of the T146 live class
`extra_environment_candidate` (T150: `typed_extra_environment_candidate`).
Also touches [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md).

## Status

Forcing holds at the causal tier in this finite family. Q1C remains
**dormant** (see "What This Does Not Earn"); packet/status decisions pause for
Joe per AGENTS.md. This is a finite forcing result, not a platform.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [T392: Fixed-SBS-Key Reversal Divergence Witness](T392-fixed-sbs-key-reversal-divergence-witness.md)
- [T162: Q1A SBS Factorization Obstruction](T162-q1a-sbs-factorization-obstruction.md)
- [T146: Weak-Measurement Escape Architecture Gate](T146-weak-measurement-escape-architecture-gate.md)
- [T149: Weak-Measurement Conditional-Sufficiency Gate](T149-weak-measurement-conditional-sufficiency-gate.md)
- [T150: Weak-Measurement Verdict-Admissibility Gate](T150-weak-measurement-verdict-admissibility-gate.md)
- [T155: Weak-Measurement Blackwell Boundary](T155-weak-measurement-blackwell-boundary.md)

## Motivation

T392 established that at a fixed full ordinary event-level record and a fixed
T162 SBS closure key over declared fragments `F1..F4`, an extra-environment
ancilla `A0` splits the reversal-cost axis (visibility `0.9897` vs `0.0`,
`H = 4` vs `inf`) with `0.25` decision-risk lift and `0.5` bits CMI. The
hostile-review ruling was: **stands, but the access boundary is stipulated** —
nothing forces the triple (i)-(iii). That objection is exactly what T392's
"Contribution Needed" asked for: a physical argument that some accessible
environment forces `A0`-like structure rather than it being engineered in.

This artifact supplies the causal version of that argument in an exactly
simulable model: replace the by-hand ancilla with an emitted mode on a
discrete lightcone. Emission of record-carrying modes is ubiquitous physics —
spontaneous emission during measurement, photon loss from a cavity while a
meter latches — not a contrived ancilla. The claim tested is **not** that all
measurements emit records; it is that WHEN they do, the T392 structure follows
from causal geometry with no residual protocol choices.

## Setup

Statevector numerics, nine qubits, exact probabilities; nothing that carries
the verdict is sampled. `models/causal_forcing_access_asymmetry.py`, reusing
T392's primitives and certificate machinery by import.

- Same measurement core as T392: system `S` in `|+>` (parameterizable phase
  `phi`), weak meter `M` via controlled-`Ry(theta)`, `theta = pi/3`, `M`
  measured; declared fragments `F1..F4` as `CNOT` Z-copies of `S`. Full
  ordinary event-level record `R` = joint `Z` distribution of `(S, M)`.
- **Propagation line**: a chain of `L = 3` qubit sites `C0, C1, C2` leading
  out of the control region. Discrete time steps; content placed on site 0
  SWAPs outward one site per step (nearest-neighbor SWAP circuit = discrete
  lightcone; the repo's own discrete-propagation device, cf. T377/T379, with
  the region framing of T153's causal diamonds).
- **Control region** (fixed once, for every preparation): `S, M, F1..F4` and
  chain sites `0..r` with `r = 1`. Region membership of the emitted mode is
  **time-indexed by the causal structure**: site `t` at step `t`, so the mode
  exits the region at step 2 (`ESCAPE_STEP`).
- **Preparation A** (no record escapes): the outgoing mode carries `|0>`
  (vacuum); the chain runs the identical SWAP circuit.
- **Preparation B** (record escapes): `CNOT (F4 -> C0)` writes a Z-copy of
  the record onto chain site 0 BEFORE propagation; the copy then propagates
  out of the region.
- **Preparation B'** (emission null control): `X` on chain site 0 — a real
  excitation, UNCORRELATED with the record (no CNOT from `F4`) — then the
  same propagation.

Predeclared reversal-success threshold `v* = 0.9` (T392's, unchanged). The
preparation-A analytic visibility is `4 sqrt(3) / 7 = 0.98974...`.

**Record-labeling convention** (T392 review lesson, stated explicitly): every
outcome tuple stored or printed is in index-sorted qubit order. The ordinary
record tuples read `(S, M)` with `S` = qubit 0 < `M` = qubit 1, so `(1, 0)`
is `P(S=1, M=0)`.

## The Forcing Theorem

**Statement.** Let the undo class be ALL channels (CPTP maps, not just inverse
couplings or unitaries) supported on the control region at final time, and let
recovery mean restoring phase-locked conditional X-visibility of the prepared
phase `phi` above `v*`. Then in preparation B no admissible channel achieves
any recovery at all, while in preparation A the in-region inverse-coupling
undo achieves `0.98974 >= v*`.

**Certificate (the proof).** The reduced state of the control region
conditional on the meter outcome, `rho_region|M` — the ONLY object any
admissible channel can act on — is **exactly independent of `phi`** in
preparation B: max pairwise difference across the sweep
`phi in {0, 1.0, sqrt(2), pi/3, 2pi/3, pi/7}` (including values
incommensurate with `pi`) is asserted `< 1e-12` and computes to `2.2e-16`.
Since every channel output is a function of `rho_region|M`, no in-region
channel output — and hence no recovered visibility — can depend on `phi`.
In preparation A the same object is genuinely `phi`-dependent (max pairwise
difference `0.857`).

**Spot-check (illustrative only).** 50 Haar-random unitaries on the in-region
qubits, none restoring phase-locked visibility above `0.05` (measured max:
`1.6e-17`), plus one representative non-unitary channel (measure `C0`, feed
back on `S`): `0.0`. This sampling is belt-and-suspenders; **the
phi-independence certificate, not the sampling, carries the result.**

**Why phase-locked visibility.** T392's own lemma disclosed that raw
visibility is gameable: manufactured coherence (`CNOT (F1 -> S)` then `H` on
`S`) achieves raw visibility `1.0` in preparation B while carrying zero
information about the prepared phase. The recovery figure of merit is
therefore the phase-locked visibility `|mean_phi e^{i phi} 2 rho_S[0,1]|`
over a uniform phase grid, which equals raw visibility for a genuine undo
(`0.98974` in A) and exactly nulls manufactured coherence (`7.5e-17` for the
exploit; asserted `<= 1e-12`). This is implemented, not just argued: the
manufactured-coherence control is a test.

### Verified exactly (assertions)

1. **Ordinary-record equality.** `R` identical for A and B (max diff exactly
   `0.0`).
2. **SBS-key and full-signature equality.** The T162 closure key AND the full
   SBS signature over `F1..F4` (per-fragment conditional trace distances plus
   the full event-level `Z` distribution over the declared register) identical
   for A and B (max diff exactly `0.0`); both keys D1-finalized, computed with
   the repo's own `_class_count_for` and pointer/objectivity vocabulary.
3. **The forcing theorem** as stated above (certificate + spot-check + A-side
   recovery to the T392 value `4 sqrt(3) / 7`).
4. **Typed axis.** `H(A) = 4` (finite; all four fragments needed),
   `H(B) = inf`, where the infinity is grounded in the causal certificate
   (no in-region channel, full stop), not in a protocol restriction. Verdict
   map `V = g(H)`: `recoverable-in-control-region` vs
   `final-relative-to-control-region`; both classes populated.
5. **Auxiliary channel** = `Z` readout at the far end of the chain (`C2`,
   outside the region, inside the escaped mode's forward cone): decision-risk
   lift `0.25` on all three T155 losses, `I(V ; C2 | R) = 0.5` bits `> 0`.
   T137 null control (downstream transform `S XOR M` of the ordinary record):
   exactly zero lift and zero CMI.
6. **B' emission null.** Preparation B' is bitwise identical to A on every
   verdict-relevant quantity (record, full SBS signature, region conditional
   state at every swept `phi`, undo visibility, `H`, verdict) while the
   emission itself is real (global statevector difference `0.707`; chain
   excitation `1.0` vs B's `0.5` vs A's `0.0`). Emission per se, and its
   energy signature, are not doing the work.
7. **Region-boundary sanity.** (a) Recovery window: the same in-region undo
   recovers `0.98974` at steps 0 and 1 (mode still inside the region) and
   `0.0` at step 2 (mode escaped) — same circuit, same region, only time
   differs. (b) Counterfactual enlargement: including the escaped site `C2`
   in the undo support restores B's recovery to exactly the A value
   (difference `0.0`), and the enlarged conditional state is `phi`-dependent
   again. The asymmetry tracks the light-cone, not a declaration.
8. **Boundary-location sweep (v0.1.1 hardening, post-hostile-review).** The
   forcing certificate re-run for a smaller (`r = 0`) and an enlarged
   (`r = 2`) control region, each fixed once for every preparation: with
   `r = 0` the mode is already outside at step 1 and the certificate fires
   there (max pairwise diff `2.2e-16`), while at step 0 (mode still inside)
   the region state stays `phi`-dependent (`0.857`); with `r = 2` (whole
   chain in-region) the region state stays `phi`-dependent at step 2
   (`0.857`). Every tested boundary placement yields the corresponding
   verdict in both directions; the residual premise is only that the
   apparatus has SOME bounded control region — not where its boundary sits.

### Thresholded forcing robustness (v0.1.1 hardening)

Earned (staged v0.2 content, brought forward after hostile review): the
exact-zero forcing is not a knife-edge of the perfect CNOT copy. With
emission via `controlled-Ry(alpha)` (`F4 -> C0`, emission probability
`sin^2(alpha/2)`; `alpha = pi` reproduces the CNOT statevector exactly since
the chain target starts in `|0>`), two exact facts are asserted per `alpha`
in the sweep `{0.75 pi, 0.9 pi, 0.98 pi, pi}`:

- the fragment-undo locked recovery in prep `B_alpha` equals
  `cos(alpha/2) * (4 sqrt(3) / 7)` to numerical precision (`0.378758`,
  `0.154830`, `0.031089`, `0.0` across the sweep);
- a channel-INDEPENDENT upper bound on ANY in-region channel's locked
  visibility — `2 (||Re X||_1 + ||Im X||_1)` with
  `X = mean_phi e^{i phi} rho_region|M(phi)`, by Hoelder plus CPTP
  trace-norm contractivity, so it covers every channel supported on the
  control region at once, with no channel enumeration — is below the
  predeclared `v* = 0.9` for all `alpha >= 0.75 pi`: `0.7575`, `0.3097`,
  `0.0622`, `~0` across the sweep (sanity: prep A's own bound `1.9795`
  respects its achievable `0.98974`; the exact-CNOT bound is numerically
  zero).

Forcing at threshold `v* = 0.9` is therefore certified for
`alpha >~ 0.75 pi`: no channel supported on the control region reaches
threshold recovery anywhere in that range. The exact-zero form of the main
theorem is the `alpha = pi` idealization of this robust fact. The analytic
`alpha*(v*)` threshold boundary stays on the open card.

## Success Criteria

- Ordinary-record and full-SBS-signature equalities hold exactly (max diff
  `0.0`, not merely below tolerance).
- The forcing certificate holds: exact `phi`-independence (`< 1e-12`) of the
  B region conditional state across a sweep of at least 5 phases including
  incommensurate ones, with genuine `phi`-dependence (`> 0.1`) in A.
- Prep A in-region undo reaches `v*`; prep B phase-locked recovery is `0` for
  the protocol family, the Haar sample, and the representative non-unitary
  channel.
- `H` finite for A, infinite for B; verdict split with both classes populated.
- Far-end detector lift strictly positive across the whole T155 loss family
  with `I(V ; C2 | R) > 0`; T137 null exactly zero.
- B' identical to A on all verdict-relevant quantities.
- Recovery window closes exactly at the escape step; boundary enlargement
  restores recovery exactly.

## Failure Criteria

- Any weakening of the exact equalities (1)-(2) to make the gap appear; the
  honesty rule for this artifact was: fix the construction, never the
  assertions, and if no placement of the emission coupling satisfies both
  equalities with a nonzero forcing gap, report "forcing fails at Tier 1 in
  this family" and demote Direction B.
- The forcing claimed from the Haar sampling rather than the certificate.
- Recovery measured by raw visibility (gameable by manufactured coherence).
- Region membership adjusted per preparation, or the escaped site quietly
  included in the undo support.
- The result described as unconditional (it is conditional on emission), as a
  Q1C reinstatement, or as a physical no-go / platform.

## Gates Addressed

- **T137 (postprocessed second-meter null).** Directly implemented: the
  downstream-of-`R` channel `S XOR M` has exactly zero lift and zero CMI.
  The live channel (`Z` at `C2`) is not a downstream transform of `R`
  because `R` is prep-invariant while `C2`'s correlation with `S` differs
  across preparations; `I(V ; C2 | R) = 0.5` bits is the formal certificate.
- **T139 (full-record sufficiency).** `R` is the full event-level joint
  `(S, M)` distribution; equality is asserted on the full distribution, and
  the signature equality extends this to the full declared-register
  event-level `Z` distribution.
- **T146 (escape architecture).** The class exercised is
  `extra_environment_candidate`, now with the extra structure FORCED into
  extra-environment status by the lightcone rather than declared into it:
  the escaped mode is outside the declared family and outside every
  in-region channel's support as a consequence of geometry.
- **T149 (conditional-sufficiency).** Positive predeclared decision-risk lift
  at fixed full ordinary record, computed exactly; the lift source is typed
  as the escaped mode.
- **T150 (verdict-admissibility).** `V = g(H)` is a fixed map from the
  independently typed reversal-cost axis, declared before the decision
  problem; both classes carry `0.5` prior mass.
- **T155 (Blackwell boundary).** Lift verified across the same finite
  three-loss family as T392 (relabeled onto the T393 verdict vocabulary);
  the null channel is null across the same family. Disclosed boundary: in
  the uniform three-preparation mixture `{A, B, B'}` the 0-1 and
  false-final-costly lifts degenerate to exactly zero at that symmetric
  prior while CMI (`0.2516` bits) and the false-recover-costly lift
  (`0.333`) remain positive; the lift claim is scoped to the declared A/B
  family, matching T392.
- **T158 / T166.** As in T392: the enlarged-instrument route is not taken
  (no preserved-target claim needed), and no platform packet is frozen; the
  T166 intake is explicitly not cleared.

## Forcing Hierarchy (typed)

- **Tier 1 — causal (this artifact).** The record-carrying mode escapes the
  future control cone. Conditions (i)-(iii) are consequences of light-cone
  geometry. Earned here, in this finite family, conditional on emission.
- **Tier 2 — thermodynamic (open card, Direction-C-facing; NOT built here).**
  Bath dispersion: the record disperses into many bath modes that remain
  causally accessible in principle, and the undo cost scales with the bath
  contact (number of modes that must be coherently re-collected). Here
  finality is not absolute within the cone but priced, and the natural
  currency is the same dissipation accounting that Direction C's
  record-consensus bound trades in: a Tier-2 artifact would connect the
  reversal-cost axis to a dissipation signature (work or entropy scaling of
  coherent recovery with bath size), which is exactly where the T144/T145
  H7 discipline about deletion accounting would start to bind. This is the
  named open follow-up; nothing about it is claimed here.
- **Tier 3 — engineered (T392).** The access triple stipulated by hand.
  Remains what it was: a finite existence result.

T393 upgrades T392 from Tier 3 to Tier 1 **conditional on emission
occurring**. The residual choice is "a record-carrying mode was emitted",
which is standard physics (spontaneous emission during measurement, photon
loss while a detector latches), and the B' control shows emission alone is
innocuous.

## Neighbors / Prior Art

Prior-art sweep: `grep` over `tests/` and `models/` for emission /
propagation / lightcone / undo content (T144/T145, T151/T153, T377-T386,
T392, s6-g9).

- **T392 (fixed-SBS-key reversal divergence witness)** — the artifact this
  upgrades. Same measurement core, same key machinery (imported), same
  decision-theoretic certificate; differs exactly at the reviewed weak point:
  the extra environment is no longer an ancilla with stipulated access but an
  emitted mode whose access status is fixed by causal geometry, and the undo
  class is enlarged from inverse couplings to all in-region channels.
- **T377 / T379 (relativistic record rendering; Lorentz pattern from
  propagation)** — the repo's discrete-propagation fixtures: lightlike
  rank/signal structure and invariant-speed compatibility channels. T393
  borrows the discrete-lightcone device (one site per step) but uses it for
  a quantum record-escape argument, not coordinate rendering; no Lorentz
  content is claimed.
- **T153 (Lorentzian causal-diamond screen)** — the absorber that classifies
  access-diamond splits as standard causal structure, not TaF residue. T393
  is deliberately on the right side of T153: the A/B split is NOT a changed
  access diamond (region and circuit are identical across preparations; only
  what was written to the emitted mode differs), so the residue here is the
  fixed-access, fixed-record reversal split, which T153 does not absorb.
  T153's discipline is also why the region is time-indexed rather than
  declared per preparation.
- **T151 (causal-access screen)** — same discipline as T153 at the graph
  level; same differentiation.
- **T144 / T145 (definalization reverse-edge taxonomy / physical deletion
  screen)** — the undo here is a reversible uncompute (a T144 non-arrow
  reverse class), not physical deletion; no H7 arrow claim. The Tier-2 card
  is where their fixed-accounting discipline would engage.
- **T118 / T162** — as in T392: the fixed-data family collapse and the SBS
  factorization obstruction; T393 lives in the same reopening door T162
  named, now with the access boundary forced rather than chosen.
- **s6-g9 (same-final-record capability pair)** — formal presheaf neighbor;
  no quantum dynamics, no causal structure.

Differentiation summary: no existing artifact combines a fixed ordinary
record, a fixed full SBS signature, exact undo dynamics, a causally
time-indexed access region, an all-channels undo class with an exact
impossibility certificate, and a non-screened-off downstream detector. The
propagation fixtures are classical/coordinate-facing; the causal screens are
absorbers that this artifact is built to respect, not to fight.

## Honest Reviewer Attack Surface

The strongest remaining line: **"you chose to correlate the mode"** — the
CNOT from `F4` to the chain is still a modeling decision, so the forcing is
conditional, not absolute. Answer, in-spec: correct, and the claim is scoped
accordingly. T393 does not claim that all measurements emit records; it
claims that WHEN a record-carrying mode is emitted — which is generic in real
detectors (spontaneous emission, photon loss during readout) — conditions
(i)-(iii) are no longer free parameters: they follow from the lightcone. The
class is physically populated, not engineered; what T392 needed stipulated,
T393 derives from geometry given emission. The B' control closes the flanking
move ("emission itself, or its energy, does the work"): B' emits MORE energy
than B and splits nothing. What would remain for a reviewer is the physical
realism of the toy lightcone (three sites, perfect SWAPs; the perfect-copy
knife-edge is closed at threshold by the v0.1.1 partial-amplitude sweep),
which is disclosed as the finite-family scope, and the Tier-2 thermodynamic
question, which is explicitly the open card.

A second line: "the region is still declared." The region is declared ONCE,
uniformly across preparations, and the verdict split tracks the mode's
causal position relative to WHICHEVER boundary is declared — earned as
tests by the v0.1.1 boundary-location sweep, in both directions at every
tested placement: `r = 0` forces at its own escape step (step 1, cert diff
`2.2e-16`) and does not force while the mode is inside (step 0, `0.857`);
`r = 1` forces at step 2 and not before (recovery window closes exactly at
the escape step; counterfactual enlargement restores recovery exactly);
`r = 2` never forces within the chain (step 2, `0.857`). The residual
premise is only that the apparatus has SOME bounded control region, not
where its boundary sits. What is NOT declared per preparation is exactly
what T392 had to stipulate per preparation: whether the extra structure is
accessible.

## Known Physics Constraints

- No-cloning respected: the chain copies only the `Z` (pointer) basis of an
  already-branched record.
- The SWAP-chain propagation is a unitary discrete lightcone; no continuum
  or Lorentz claim is made (cf. T379's own caveats).
- The `S`-`M` coupling is not reversed (the meter is measured); verdicts are
  stated conditional on the `M` outcome, on the dominant branch, as in T392.
- The A-side undo and the B-side impossibility use the same figure of merit
  (phase-locked visibility), so the split is not an artifact of asymmetric
  metrics.

## What This Does Not Earn

- It does **not** reinstate Q1C. No T166 platform packet is frozen; the T183
  reinstatement stack is not cleared; Q1C stays dormant and any packet or
  status decision pauses for Joe per AGENTS.md.
- It does **not** show that measurements must emit records. The upgrade is
  conditional on emission; a preparation that emits nothing (A) stays
  recoverable.
- It does **not** build Tier 2 (thermodynamic forcing); that is the named
  open card.
- It does **not** upgrade D1, H7, or any physical-arrow claim; the undo is a
  reversible uncompute.
- The result is scoped to this nine-qubit finite family with a three-site
  chain. Partial emission amplitude is earned at threshold (v0.1.1,
  `alpha >= 0.75 pi` at `v* = 0.9`) and the boundary placement is swept
  (`r = 0, 1, 2`); robustness to imperfect fragment copies and longer
  chains is future work, staged through T166 if it is ever platform-facing.

## Reproduction

```bash
python -m pytest tests/test_causal_forcing_access_asymmetry.py -v
python -m models.causal_forcing_access_asymmetry
```

## Contribution Needed

- The Tier-2 thermodynamic forcing artifact: bath dispersion with undo cost
  scaling in bath contact, connected to Direction C's dissipation accounting.
- The analytic `alpha*(v*)` threshold boundary for the partial-amplitude
  forcing (the numeric sweep is earned in v0.1.1; the closed-form boundary
  is not).
- Robustness sweeps still open: imperfect fragment copies and chain-length
  scaling.
- A physical-platform mapping (cavity photon loss during dispersive readout)
  IF Joe ever elects to press toward the T166 packet gate.
