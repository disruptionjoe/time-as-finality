# T392: Fixed-SBS-Key Reversal Divergence Witness

## Route

Quantum measurement / classical records.

## Claim

A finite, exactly-simulable quantum model exists in which two preparations
agree exactly on (a) the full ordinary event-level monitored record and (b) the
repo's own SBS-importable closure key over the declared fragment family, yet
differ in reversal cost, so that an auxiliary channel tied to extra environment
structure gives positive, non-screened-off predeclared decision-risk lift for a
verdict `V = g(H)` whose independently typed axis `H` is reversal cost. If this
holds, the T146 live class `extra_environment_candidate` (T150:
`typed_extra_environment_candidate`) is non-empty **in this finite model**.
(Informal usage has called this "Q1C Class 1"; that label collides with T146's
own class numbering, where class 1 — `coarse_record_only` — is a null class,
which is why the named class is used.)

## Class

Subclaim of [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md);
constructive existence probe for the T146 `extra_environment_candidate` live
class. Also touches [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md).

## Status

Witness holds in this finite family. Q1C remains **dormant** (see
"What This Does Not Earn"). This is a finite existence proof, not a platform.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [T162: Q1A SBS Factorization Obstruction](T162-q1a-sbs-factorization-obstruction.md)
- [T146: Weak-Measurement Escape Architecture Gate](T146-weak-measurement-escape-architecture-gate.md)
- [T149: Weak-Measurement Conditional-Sufficiency Gate](T149-weak-measurement-conditional-sufficiency-gate.md)
- [T150: Weak-Measurement Verdict-Admissibility Gate](T150-weak-measurement-verdict-admissibility-gate.md)
- [T155: Weak-Measurement Blackwell Boundary](T155-weak-measurement-blackwell-boundary.md)

## Motivation

T162 turned the N10 SBS absorber into an executable obstruction: within the
current Q1A already-formed-record family, the D1 verdict factors through an
SBS-importable closure key, so fixing full SBS data cannot change the verdict.
T162 explicitly left one door: a witness that keeps the SBS closure key fixed
and supplies a genuinely new physical dimension that SBS cannot import for free.

T118 already tried reversal cost inside the *fixed-data* family and collapsed it,
but only because that family has no physical undo dynamics — its only reversal
proxy was the number of accessible record classes, which equals audited support.
This model gives the family what T118 lacked: actual, exact, reversible undo
dynamics on a statevector. The question is whether reversal cost, once it is a
real coherence-recovery cost rather than a class count, can split the verdict at
a fixed SBS closure key and a fixed full ordinary record.

## Setup

Statevector numerics, seven qubits, exact probabilities, no sampling.
`models/fixed_sbs_key_reversal_divergence.py`.

- System qubit `S` prepared in `|+>`.
- Ordinary instrument: meter qubit `M` weakly coupled to `S` by
  controlled-`Ry(theta)`, `theta = pi/3`; `M` read in `Z`. The **full ordinary
  event-level record** `R` is the joint `Z` distribution of `(M, S)`, computed
  exactly.
- Declared environment fragments `F1..F4`, each a perfect `Z`-copy of `S` via
  `CNOT (S -> Fi)`.
- **Preparation A** (shallow branching): exactly the above.
- **Preparation B** (deep branching): A plus `CNOT (F4 -> A0)`, one extra
  unmonitored ancilla `A0` copying `F4`'s record. `A0` is NOT a declared
  fragment and NOT accessible to the undo protocol.
- **Preparation B'** (null control): A0 copies nothing (product); identical
  to A.

Predeclared reversal-success threshold `v* = 0.9`, fixed before inspecting the
gap. The natural preparation-A analytic visibility is
`2 cos(theta/2) / (1 + cos(theta/2)^2) = 0.98974...`, comfortably above `0.9`,
so the round `0.9` is used unchanged.

### Verified exactly (assertions)

1. **Ordinary-record equality.** `R` identical for A and B (max diff `0.0`).
2. **SBS-key equality.** The closure key over `F1..F4` — pointer observable,
   objectivity status, pointer value, partition visibility, and the
   independence-corrected support count `R_delta` — identical for A and B, and
   both keys are D1-finalized under the repo's `D1_INDEPENDENT_SUPPORT_THRESHOLD`.
   The key is computed with the repo's own `_class_count_for` and pointer /
   objectivity vocabulary imported from
   `models/q1a_sbs_factorization_obstruction.py`.
3. **Reversal divergence.** Undo protocol `U_K` = inverse of the `S->Fi`
   couplings on the accessible set `K = {F1..F4}`, conditioned on each `M`
   outcome (the `S`-`M` coupling is not reversed; `M` is already measured).
   X-basis visibility of `S` after undo: A restores `0.98974`, B stays `0.0`.
4. **Typed axis H.** Reversal cost = minimal `k` (accessible undo-set size)
   achieving visibility `>= v*`. `H(A) = 4` (all four fragments needed),
   `H(B) = inf` (unattainable in the accessible family). Verdict map
   `V = g(H)`: `recoverable-at-access-K` vs `final-relative-to-K`. Both classes
   populated.
5. **Screening-off failure certificate.** Auxiliary channel = `Z` on `A0`.
   Bayes decision risk for predicting `V` from `R` alone vs `(R, A0)`, under
   three loss functions (symmetric 0-1, false-recover-costly, false-final-costly):
   lift `0.25` on all three. Conditional mutual information `I(V ; A0 | R) = 0.5`
   bits `> 0`.
6. **Null controls.** (a) An auxiliary channel that is a downstream transform
   of `R` (`M XOR S`) shows zero lift and zero CMI (T137 null class).
   (b) Preparation B' shows zero divergence from A on every metric.

## Success Criteria

- Ordinary-record equality and SBS-key equality both hold to numerical
  precision.
- The reversal visibility gap is substantive (`> 0.5`) at fixed keys.
- `H` is finite for A, infinite for B; the verdict map splits with both classes
  populated (T150 support floor met by construction).
- The auxiliary lift is strictly positive across the whole finite loss family
  (T155) and `I(V ; A0 | R) > 0`.
- The T137 downstream-transform null control and the B' product-state null
  control both show zero effect.

## Failure Criteria

- Any tuning of `v*`, `theta`, or the assertion tolerances to force a positive
  verdict. `v*` is predeclared; `theta` is a fixed weak angle; equalities are
  exact.
- Ordinary-record or SBS-key equality weakened to make the gap appear.
- The lift claimed from a single loss rule or a single chosen verdict map.
- The witness described as reinstating Q1C or as a physical no-go / platform.

## Gates Addressed

- **T137 (postprocessed second-meter null).** Directly implemented as a null
  control: the downstream-of-`R` auxiliary channel `M XOR S` has zero lift and
  zero CMI. The live channel `Z` on `A0` is NOT a downstream transform of `R`
  because `R` is prep-invariant (`P(R|A) = P(R|B)`) while `A0`'s correlation
  with `S` differs across preparations; the positive `I(V ; A0 | R)` is the
  formal certificate that it survives full-record conditioning.
- **T139 (full-record sufficiency).** `R` is the full event-level joint `(M, S)`
  distribution, not a coarse or thresholded summary; equality is asserted on the
  full distribution.
- **T146 (escape architecture).** The live class exercised is
  `extra_environment_candidate`: `A0` is extra environment structure outside the
  declared instrument and outside the declared fragment family, not a
  same-instrument channel and not an instrument enlargement.
- **T149 (conditional-sufficiency).** Positive predeclared decision-risk lift
  at fixed full ordinary record, with the lift source typed as extra
  environment structure (`A0`), is computed exactly, not asserted.
- **T150 (verdict-admissibility).** `V = g(H)` is a fixed map from the
  independently typed axis `H` (reversal cost), declared before the decision
  problem; both verdict classes carry `0.5` prior mass, so the lift is not an
  auxiliary-echo label, a rare-target partition, or a post hoc target.
- **T155 (Blackwell boundary).** Lift is verified across a finite family of
  three loss tables, not one scoring rule; the null channel is verified null
  across the same family.
- **T158 (preserved-target honesty).** Does not apply: this is the
  extra-environment route, not the enlarged-instrument route. The ordinary
  instrument is not enlarged; `A0` sits outside it. No preserved-target
  back-projection is claimed or needed.
- **T166 (platform-packet intake).** Not applicable and explicitly not cleared:
  this is a finite model, not an external platform. No `R, A, H, V, L` packet is
  frozen for a real device, so Q1C reopening is not triggered.

## Neighbors / Prior Art

- **T162 (Q1A SBS Factorization Obstruction)** — the obstruction this probes.
  T162 shows the D1 verdict factors through the SBS closure key in the
  fixed-*data* family. This model keeps that exact key fixed (reusing T162's own
  `_class_count_for` and vocabulary) and adds a dimension T162's family did not
  contain: physical reversible undo dynamics. It occupies T162's explicitly
  named reopening door, not a contradiction of it.
- **T118 (Q1A reversal-cost collapse)** — collapsed reversal cost *inside the
  fixed-data family*, where the only reversal proxy was a class count equal to
  audited support. This model differs precisely where T118 said the family was
  blind: it supplies actual undo dynamics and a coherence-recovery cost, so the
  reversal cost is no longer a relabeling of support. It does not reopen the
  Q1A `bookkeeping_only` verdict; it is a Q1C-directed existence probe.
- **s6-g9 (same-final-record capability pair)** — the closest conceptual
  neighbor: same associated final record, different presheaf capability, with
  the capability lost in the final record. That result is purely formal
  (presheaf descent), with no quantum statevector, no SBS key, no reversal
  dynamics, and no decision-theoretic lift. This model is the quantum,
  decision-theoretic instance of the same "same final data, different residual
  capability" pattern, aimed at the Q1C access boundary rather than at descent
  non-factorization.
- **T144 / T145 (definalization reverse-edge taxonomy / physical deletion
  screen)** — classify reverse edges and screen physical-record-deletion under
  fixed thermodynamic accounting for H7. This model's undo is a *reversible
  uncompute* (a T144 non-arrow reverse class), not physical deletion, and makes
  no H7 arrow claim.
- **T183 (reinstatement stack)** — the composed Q1C reopening burden. This model
  clears the internal architecture / verdict / lift checks for the
  extra-environment route but deliberately does not attempt the packet-intake or
  platform legs, so it does not clear the T183 stack.
- **dual_record_opportunity_fixture** — an adjacent-possible opportunity-edge
  comparator; unrelated mechanism (search traces, not measurement records).

Differentiation summary: no existing artifact combines a fixed SBS closure key,
a fixed full ordinary record, exact reversal dynamics, and a non-screened-off
decision-theoretic auxiliary lift. The nearest neighbors are either formal-only
(s6-g9), inside a family with no undo dynamics (T118/T162), or aimed at a
different claim (T144/T145 H7).

## Honest Reviewer Attack Surface

A hostile reviewer's strongest line: "In preparation B, `A0` is a perfect
`Z`-copy of `S`, so the auxiliary channel is just a second pointer record — a
downstream copy, hence T137-null." Response, stated candidly: within a single
preparation `A0` *is* screened off by `S`, but the decision problem is over the
prep mixture, and `R = (M, S)` is prep-invariant, so `R` alone carries zero
information about the verdict `V` (which tracks prep identity via reversibility).
The auxiliary channel's lift comes from its *differential correlation with `S`
across preparations*, which `R` cannot resolve. The exact `I(V ; A0 | R) = 0.5`
bits `> 0`, against the exact `I = 0` for the genuine downstream-of-`R` channel,
is the formal separation. A reviewer may still argue the extra environment here
is engineered rather than physically forced; that is true, and is exactly why
this earns only a finite existence result, not a platform (see below).

## Mixture Legitimacy (why the A/B family is not smuggled)

A related objection: "the lift is merely preparation identification — the A/B
mixture is an artifact of posing a two-preparation problem." Three answers, in
decreasing order of dependence on the mixture reading:

1. **The gates structurally require a family.** T137's null condition is
   defined over a joint distribution with a latent branch-relevant variable,
   and T150's support floor requires both verdict classes to carry mass, which
   forces `H` to vary across runs. A single frozen preparation can satisfy
   neither; an A/B family is required by the gates this artifact clears, not
   smuggled in to manufacture lift.

2. **The mixture is physically a single frozen architecture.** The 50/50 A/B
   mixture is physically equivalent to one fixed 8-qubit circuit with a single
   extra unmonitored coin qubit `C` prepared in `|+>` and controlling the
   `F4 -> A0` coupling. Cross terms between the two branches carry `|0><1|_C`
   and vanish under partial trace for every observable excluding `C`; the
   branch overlap `<psi_A|psi_B> = 1/2` never becomes visible to any such
   observable. Nothing in the family requires switching circuits between runs.

3. **The earned content survives without the mixture reading.** Independently
   of how the mixture is interpreted, the artifact establishes verdict
   non-factorization: identical `R` and identical T162 keys, yet different
   D1-relative-to-access verdicts. The verdict does not factor through
   `(R, key)` in this family, and that statement makes no reference to a prior
   over preparations.

## The Phi-Independence Lemma (what `H(B) = inf` rests on)

Disclosure first: the visibility metric alone is gameable under unrestricted
accessible unitaries. Raw visibility `1.0` is achievable in preparation B by
manufactured coherence — e.g. `CNOT (F1 -> S)` followed by `H` on `S` — so the
inverse-coupling protocol restriction is NOT what `H(B) = inf` rests on.
Manufactured coherence carries no information about the prepared state and
would trivialize A equally.

What `H(B) = inf` does rest on is a protocol-independent lemma, verified
exactly in the test suite: parameterize the initial `S` state as
`(|0> + e^{i phi}|1>)/sqrt(2)`. Then the full accessible conditional state
`rho_{S,F1..F4 | M=0}` in preparation B is EXACTLY independent of `phi`
(max difference `0.0` to machine precision, asserted `< 1e-12`, across the
sweep `phi in {0, pi/7, pi/3, 2pi/3, pi}`), while in preparation A it is
genuinely `phi`-dependent (max difference `0.9897`, asserted `> 0.1`). In B,
no operation confined to the accessible register — inverse-coupling or
otherwise — can recover the prepared phase, because the accessible conditional
state carries no `phi` information at all. That, and not the protocol
restriction, is the ground for `H(B) = inf`.

## Known Physics Constraints

- No-cloning is respected: fragments and `A0` copy only in the `Z` (pointer)
  basis of an already-branched record, which is permitted.
- The undo is a genuine unitary uncompute of the declared couplings; it is not
  a measurement-outcome erasure and claims no thermodynamic arrow.
- The `S`-`M` coupling is not reversed (the meter is measured); the verdict is
  stated conditional on the `M` outcome, on the dominant branch.

## What This Does Not Earn

- It does **not** reinstate Q1C. Q1C reopening requires the T166 platform-packet
  intake and pauses for Joe per AGENTS.md. This is a finite model, not a device.
- It does **not** name or endorse any hardware platform, and clears neither the
  T166 packet gate nor the composed T183 reinstatement stack.
- It does **not** upgrade D1, H7, or any physical-arrow claim. The undo is a
  reversible uncompute (a T144 non-arrow reverse class).
- It does **not** overturn T162: T162's factorization holds in the fixed-*data*
  family; this model lives in a richer family (with undo dynamics) that T162
  itself named as the reopening door.
- The result is scoped to this seven-qubit family. It shows the
  `extra_environment_candidate` class is non-empty as a mathematical
  possibility, not that any accessible physical system realizes it.

## Reproduction

```bash
python -m pytest tests/test_fixed_sbs_key_reversal_divergence.py -v
python -m models.fixed_sbs_key_reversal_divergence
```

## Contribution Needed

- A physical argument that some accessible environment forces `A0`-like extra
  structure rather than it being engineered in, which is what a real Q1C
  platform would have to supply.
- A check of robustness to imperfect fragment copies and finite `theta` ranges,
  and whether the lift survives partial `A0` accessibility.
