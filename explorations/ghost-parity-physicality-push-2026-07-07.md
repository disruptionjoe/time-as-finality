# Pushing the Ghost-Parity Physicality Bet (the finality record reading, on trial)

Push note, 2026-07-07. **Analysis is method, not evidence. No claim moves. From-memory physics flagged.**
Continues the finality line: the records-vs-redundancy discriminator
(`finality_records_vs_redundancy_discriminator.py`) isolated the entire finality residual to ONE bet -- is
physicality defined by POSITIVITY (standard -> the ghost is gauge REDUNDANCY) or by the full KREIN structure
(ghost-parity / Krein quantization -> the ghost is a RECORD)? This note pushes that bet, and the honest result
is that it leaned AGAINST the home team.

## The literature the bet lives in (from-memory, flagged)

The record reading is not fringe: it is the Bender-Mannheim PT-symmetric-QM / Turok-Bateman Krein-quantization
program -- theories with negative-norm "ghost" sectors can be consistently quantized (unitary, positive
probabilities) by choosing a positive-definite inner product (a C / CPT operator) on the full space instead of
gauge-quotienting the ghost away. So "the ghost is physical, not redundancy" is a real, active claim.

## The push (`models/ghost_parity_physicality_probe.py`, exit 0) -- and it refuted the easy version

The record reading needs the mirror to be BOTH physical AND hidden ("a hidden collective record"). The probe
tested whether "physical-and-hidden" is even coherent, and found it is **normalization-contingent**, which is
worse for the record reading than expected:

- A positive-definite inner product on the full space EXISTS (Krein quantization is kinematically available):
  the mirror state has norm +1 under it, -1 under the Krein form. So "physicalize the ghost" is on the table.
- **But if you physicalize it, the honest FULL-space Born rule LEAKS it.** Two states sharing their W+ part
  but differing in W- have different total norms, so a W+-restricted observer's *normalized* statistics differ
  (O_a diff 9e-2, O_b diff 7e-3) -- the ghost becomes partially VISIBLE, not a hidden record.
- The mirror is hidden ONLY under the **self-normalized / projector-Born convention** (normalize by the
  physical component's own norm `||P+ psi||^2` -- exactly what T12' used): then the W+ observer sees nothing
  (diff 0). So "hidden" is a property of the observer's normalization, not of the physics alone.

**Net of the push: the record reading got MORE contingent, not less.** It survives only in the corner
`{Krein-retention quantization AND self-normalized observer}`. The default corner
`{BRST-quotient AND full-space Born rule}` gives **REDUNDANCY**. Two compounding special assumptions, each
non-default, are required for "records"; the standard reading is redundancy.

## What the push DID buy (a smaller gate, honestly named)

Pushing was not wasted -- it shrank the quantization leg of the bet to a specific, named object:
**is the mirror (ghost) sector BRST-exact (a first-class-constraint gauge artifact -> quotient -> REDUNDANCY)
or BRST-cohomology-nontrivial (a genuine physical dof -> retain -> candidate RECORD)?** That is fixed by the
CONSTRAINT / gauge structure -- a named piece of the dynamics -- NOT the full stabilized-twisted source action.
So the finality bet is reduced from "build the source action" to "is the ghost a first-class-constraint
artifact?", plus the separate normalization-convention question the probe exposed.

## Honest verdict

The sharpest live thread, pushed, leaned **against** the home team: the finite-observer record reading of the
mirror requires two compounding non-default choices (Krein-retention *and* self-normalized observer), and the
standard reading of a negative-norm sector is gauge redundancy. This is consistent with the best-explanation
swing (the records reading was a promissory note) and with the discipline installed this session: the push was
run to test the home team's hope, and it honestly did not confirm it -- it made the burden clearer and the gate
smaller. The record reading is not dead (the corner is coherent under its two assumptions, and the BRST-exactness
question is genuinely open), but it is now precisely priced: two special bets, default is redundancy.

Cross-links: `finality-records-vs-redundancy` discriminator (the dichotomy this pushes),
`finality-best-explanation-swing-2026-07-07.md` (records = promissory note), the ghost-parity/Krein synthesis
in `gu-formalization/canon/ghost-parity-krein-synthesis.md`. No claim moves in any repo.

## Governed artifact pointer: T507

T507 (`tests/T507-finality-record-redundancy-double-gate.md`) now records this push as a repo-native double gate.
The result is deliberately priced: the standard positivity/BRST plus full-Born corner is redundancy; full-Krein
plus full-Born is visible rather than hidden; the hidden-record reading survives only as review material in the
Krein-retention plus self-normalized/projector Born corner. T507 does not decide BRST exactness, accept
Krein-retention quantization, prove a hidden mirror record, move claims, or move cross-repo truth.

## Governed artifact pointer: T508

T508 (`tests/T508-brst-cohomology-record-admission-gate.md`) now carries the
repo-native admission gate for the BRST/exactness burden named above. A future
packet must predeclare a nilpotent constraint operator `Q`, prove the mirror is
Q-closed, decide exactness by membership in `im(Q)`, declare the cohomology or
physical-state quotient and Q-closed observables, include exact/nontrivial
controls, and still pay T507's operation and normalization gates. T508 admits a
nontrivial mirror class only as review material and does not decide real BRST
status, Krein quantization, hidden-record physics, source-action truth, claim
status, public posture, or cross-repo truth.

## Governed artifact pointer: T509

T509 (`tests/T509-brst-observable-compatibility-gate.md`) makes the Q-closed
observable/readout burden executable. The T507-style full-Krein recovery is
blocked in the finite BRST fixture because it does not descend through the
quotient, and W+ representative leakage is blocked because ordinary W+ readout
is not exact-invariant. A direct cohomology observable is admitted only as a
review target, not hidden-record or physics evidence. This further narrows the
record reading without moving claim status, public posture, or cross-repo truth.
