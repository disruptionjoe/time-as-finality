# T395: Record-Order Trade-off Probe

## Route

Quantum foundations / composition order / classical records. First executable
rung of Direction A (`audits/2026-07-01-high-gravity-research-directions.md`,
Direction A step 2 — "the CHSH move"), run as a kill-test.

## Claim

For the two-party quantum-switch-with-record family, the trade-off between
record-order distinguishability `D(gamma)` and switch interference visibility
`V(gamma)` is EXACTLY the interferometric which-path/visibility duality
transplanted (two-marker Greenberger–Yasin/Englert structure), with no residue
specific to composition order. The candidate record-order inequality therefore
carries no quantitative content beyond known duality in the two-order family.
Separation, if any, lives at k >= 3 partial-record structure, where a
class-coarse record produces a class-graded trade-off that no tested global
scalarization reduces to the binary duality form — a finite observation, not
a theorem.

This is a COLLAPSE verdict on the artifact's own kill-test, recorded as the
earned result — a forced collapse, made explicit: it prices what the
Direction-A inequality must contain (structure beyond two orders) before any
new bound can be claimed. Given the v0.1 definitions (D = marker
trace-distance, V = control coherence) and the pure two-branch family, the
duality relations are algebraic identities; the kill-test could not have
returned a residue in this family. Its earned content is the explicit
term-by-term mapping and the three-way pricing, not a contingent outcome.

## Class

New exploratory subclaim in the Direction-A lane, lineage C1/H1 via T49's
Anti-Scalar result (H1: temporal order reconstructed from records; T49: no
scalar replicates a partial order with incomparable elements). NOT registered
in CLAIM-LEDGER, deliberately: this is a probe, not a claim promotion.
Promotion to a ledger-registered claim would require, at minimum:

1. a genuine process-matrix causal-nonseparability witness (SDP random
   robustness or equivalent) replacing the visibility signature;
2. the k >= 3 class-graded trade-off stated and proved as a theorem in a
   declared family, not verified as a finite observation;
3. survival of the multipath-complementarity prior-art absorber (see
   Candidate Prior Art) — i.e., a demonstration that the k >= 3 structure is
   not itself transplanted multibeam duality;
4. the usual repo gates: runnable artifact, hostile review, and a pause for
   Joe before any external-facing step.

## Status

Implemented; verdict earned: **v0.1 record-order bound reduces to
interferometric duality in the two-order family; separation, if any, lives at
k >= 3 partial-record structure.** No claim promotion. This spec opens
process-composition-order ground in the repo (verified: no prior
process-matrix / quantum-switch content existed), so all physics literature
named here is candidate prior art from memory, flagged per the
no-fake-citations rule; nothing enters `literature/` unverified.

## Target Claims

- [H1: Record Reconstruction](../HYPOTHESES.md) (lineage; not upgraded)
- [C1: Experienced Time As Record Finality](../claims/C1-experienced-time-as-record-finality.md) (lineage; not upgraded)
- [T49: Reconstruction Without Background Time](T49-reconstruction-without-background-time.md) (the anti-scalar hook the k=3 probe exercises)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md) (guardrail)
- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md) (guardrail)

## Setup

Exact statevector numerics, numpy only, no sampling anywhere a verdict rests.
`models/record_order_tradeoff_probe.py`. Total Hilbert dimension <= 24
throughout (<= 6-qubit budget; the k-order control is a k-level system,
k <= 6, embeddable in 3 qubits).

**Two-order family, dims (c, r, t) = (2, 2, 2), subsystems INDEX-SORTED
(c = 0, r = 1, t = 2; every stored or printed tuple reads (c, r, t)):**

- Control `c` in `(|0> + e^{i phi}|1>)/sqrt(2)` selects composition order:
  branch `c = 0` applies A then B (target `B@A|psi>`), branch `c = 1` applies
  B then A (target `A@B|psi>`).
- Record qubit `r` coupled to the control by controlled-`Ry(gamma)`:
  `gamma = 0` no record, `gamma = pi` perfect record. The record is
  ACCESSIBLE (read in Z at readout) — the D1-style, finality-relevant
  difference from generic environment decoherence.
- Canonical operations, documented sweep: candidates
  `(Ry(pi/2), Rz(pi/2))`, `(Ry(pi/2), Rz(pi))`, `(Rx(pi/2), Rz(pi/2))`,
  `(Ry(pi/2), Rz(pi/4))` on `psi = |0>`. Canonical choice
  `A = Ry(pi/2), B = Rz(pi/2)`: target order-branch overlap
  `|K| = 1/sqrt(2)` exactly — the balanced two-marker point. Disclosed: the
  literally maximal order-sensitivity candidate `(Ry(pi/2), Rz(pi))` has
  `|K| = 0`, which degenerates the visibility curve to `V == 0` and makes the
  trade-off invisible; it is documented in the sweep table and not chosen.
- `gamma` sweep: 21 values on `[0, pi]` (spec floor: >= 20), endpoints exact.
- Gate-built circuit and independent branch-sum construction asserted equal.

**k = 3 probe, dims (k, 2, 2):** three operations `A, B, C = Rx(pi/2)`;
uniform coherent superposition over a subset of the 3! = 6 orders. The record
has PARTIAL access: one qubit coupled by controlled-`Ry(gamma)` to the order
CLASS (a 2-class coarse-graining of the orders), not to the order itself.
Canonical 3-order subset `{ABC, BAC, CAB}` with class = "A before B"
(`{ABC, CAB}` vs `{BAC}`); full 6-order coherent sum with class = permutation
parity. Both were feasible within budget; the full 6-order sum runs at
Hilbert dimension 24.

## Definitions (what "record-fixed" operationalizes, and what it does not)

The three nested process classes probed:

1. **RECORD-FIXED**: order definite AND written into an accessible stabilized
   record `lambda` before readout (here: `gamma = pi`, record read in Z).
2. **CAUSALLY SEPARABLE**: order definite (possibly mixed) but not
   necessarily recorded/accessible (here: `gamma = pi`, record traced).
3. **NONSEPARABLE**: coherent superposition of orders (here: `gamma = 0`).

**D(gamma), order-distinguishability (the record-finality proxy):** the
trace-distance distinguishability of the two order-branch conditional record
states; equivalently, the optimal (Helstrom) equal-prior success of
postdicting which composition order the target underwent, given the record
alone, is `(1 + D)/2`. Why this is the right operationalization of "the order
is recorded": at `gamma = pi` the record is a perfect stabilized copy of the
order degree of freedom (`D = 1`); at `gamma = 0` no record exists (`D = 0`);
in between, `D` is exactly the best achievable postdiction advantage of an
agent whose access is the record. Defined honestly for the coherent case: no
"realized order" is asserted per run — `D` is branch-discrimination, not a
hidden variable (Q1D).

What `D` does NOT capture, disclosed in-model:

- (a) no per-run ontic order in the coherent case (no hidden-variable
  reading);
- (b) single-holder only — D1's distinct-holder redundancy, robustness, and
  reversal-cost axes are not modeled;
- (c) the physical readout basis is Z, and the Helstrom optimum generally
  needs a non-Z measurement; the accessible Z-readout advantage is computed
  separately and equals `D^2` exactly (disclosed sub-optimality — note the
  accessible form of the duality is then linear: `D_Z + (V/V0)^2 = 1`).

**V(gamma), switch interference visibility:** fringe visibility of the
control readout under a phase sweep, computed exactly as twice the control
coherence `2|rho_c[0,1]|` and cross-checked against an explicit 720-point
phase-grid fringe. NAMED LIMITATION (v0.1 honest scope): `V` is the standard
operational signature of order-coherence, NOT a causal-nonseparability
witness. A genuine process-matrix witness (random robustness) requires SDP
machinery, which is the named next rung; no closed-form witness was attempted
because none could be finitely verified here. All verdicts are scoped to the
visibility signature.

## The Trade-off (exact relations, all asserted at 1e-12)

With `V0 = |K| = |<t_0|t_1>|` (the target order-branch overlap) and
`Dt0 = sqrt(1 - V0^2)`:

- `D(gamma) = sin(gamma/2)` (max residual `1.1e-16`)
- `V(gamma) = V0 cos(gamma/2)` (max residual `1.1e-16`)
- `D^2 + (V/V0)^2 = 1` — normalized binary duality, exact (`4.4e-16`)
- `D_joint^2 + V^2 = 1` — Englert saturation with the joint
  (record x target) marker, exact (`8.9e-16`)
- `D^2 + V^2 + (1 - D^2) Dt0^2 = 1` — three-way decomposition, exact
  (`2.2e-16`): the candidate bound `D^2 + V^2 <= 1` holds with slack exactly
  equal to the unread target-marker term. The target is itself a second,
  fixed-strength order marker; the record and the target compose as
  independent markers (branch overlaps multiply).
- `D` strictly increasing, `V` strictly decreasing on the sweep; endpoints
  exact: `D(0) = 0, D(pi) = 1, V(0) = V0, V(pi) = 0`.

**Accessibility result (the (1)/(2) boundary), elementary but load-bearing:**
the reduced process on (control, target) is EXACTLY identical whether the
record is traced out or measured-and-forgotten (asserted to machine
precision; it is an identity of partial trace). At fixed `gamma`, record
ACCESSIBILITY moves no process marginal at all — the record-fixed vs
causally-separable boundary is capability-relative (what the record holder
can postdict), not marginal-statistics-relative. Any future record-order
criterion must be stated at the capability level (T392's "same data,
different capability" pattern), not at the level of process statistics.

## The Reduction Audit (the kill-test — verdict: collapse)

Explicit Mach-Zehnder-with-which-path-marker mapping, implemented in code:

| switch object | MZ object |
| --- | --- |
| control `c` | path degree of freedom (which arm) |
| order branch `c=0` / `c=1` | path 0 / path 1 |
| record `r`, controlled-`Ry(gamma)` | which-path marker, same coupling |
| target `t` (branch states `B@A psi`, `A@B psi`) | internal dof: a second, fixed-strength marker with branch overlap `K` |
| `D(gamma)` | Englert which-path distinguishability |
| `V(gamma)` | Englert fringe visibility |

Three exact checks, all passing at 1e-12 across the full sweep (and three
control phases for the statevector check):

1. **Statevector identity**: the mapped MZ state (internal dof loaded with
   the order-branch targets) equals the gate-built switch state — max
   difference `1.1e-16`. The switch+record state IS an
   MZ-with-two-markers state, term by term.
2. **Plain-MZ curve coincidence**: `(D_switch, V_switch/V0)` equals
   `(D_MZ, V_MZ)` pointwise — max differences `0.0` and `1.1e-16`.
3. **Englert saturation** with the joint marker (above).

**Verdict (predeclared vocabulary, asserted verbatim in the test suite):**
collapse — the v0.1 record-order trade-off reduces exactly to interferometric
which-path duality in the two-order family. The residue is interpretational
only (reading interferometer arms as composition orders), not quantitative.
The record-order inequality needs structure beyond two orders.

Given the v0.1 definitions (D = marker trace-distance, V = control
coherence) and the pure two-branch family, the duality relations are
algebraic identities; the kill-test could not have returned a residue in
this family. Its earned content is the explicit term-by-term mapping and the
three-way pricing, not a contingent outcome.

## The k = 3 Probe (partial record; where binary duality has no analog)

The record writes only the order-CLASS (partial access). Order postdiction
becomes a k-class discrimination; the finality-side order knowledge is a
partition with ties — the T49 anti-scalar structure — where binary duality
is a single scalar pair. Findings, all exact where stated:

- **Binary duality SURVIVES pairwise on cross-class pairs**: every
  cross-class normalized pairwise coherence scales exactly as `cos(gamma/2)`
  and satisfies `sin^2(gamma/2) + (V_ij/V_ij(0))^2 = 1` (max residual
  `5.6e-16` canonical; exact across the exhaustive sweep).
- **Binary duality is ABSENT within class**: within-class coherences are
  exactly gamma-flat (max deviation `0.0`) — a perfect class record destroys
  no within-class order-coherence.
- **Order-postdiction ceiling**: optimal record-only postdiction is
  `P(gamma) = (1/k)(1 + sin(gamma/2))` (derived via the identical-in-class
  reduction to binary Helstrom; achievability confirmed on a 2000-point
  projective-measurement grid). At `gamma = pi`: `2/3` for the 3-order
  subset, `1/3` for the 6-order sum — the record ceiling. Class postdiction
  reaches 1 at `gamma = pi` (the class IS recorded).
- **No tested global scalarization keeps the binary form**: with
  `D_glob = (P - 1/k)/(1 - 1/k)` and visibility scalarized as mean/min/max of
  normalized pairwise coherences, the circle residual `D^2 + V^2 - 1` at
  `gamma = pi` is `-0.639` (mean), `-0.750` (min), `+0.250` (max, exactly
  `sin^2(gamma/2)/4` above the circle). The (D, V) point detaches from the
  duality circle in both directions depending on scalarization — the
  trade-off is irreducibly class-graded. Disclosed: `D_glob` and `V_max`
  aggregate different structure levels; this is an exhibit that no scalar
  pair reproduces the binary form, not a physics violation.
- **Exhaustively verified in the declared finite family**: all C(6,3) = 20
  three-order subsets x 3 bipartitions (60 configs) and the full 6-order sum
  x all 31 bipartitions, full 21-point gamma sweep each: within-class
  flatness, cross-class cos-scaling/duality, and the `2/k` ceiling hold in
  every configuration (degenerate zero-baseline pairs skipped for the
  normalized form and counted: they satisfy the cos-scaling check
  trivially). Within this family the pattern is exhaustive, not sampled;
  beyond it, nothing is claimed.
- **Full-resolution contrast**: a k-level record register at `gamma = pi`
  achieves postdiction 1 and kills all pairwise coherence (the binary-duality
  corner). The ceiling is a consequence of class-coarse ACCESS, not of k.

Honest framing: the k = 3 structure is a candidate instance of known
multipath-complementarity territory (see prior art); what is repo-relevant is
the exact class-graded form — "record-fixed at class resolution" is NOT
"order definite," and the record's knowledge is a partial structure no scalar
captures. Whatever pattern appears here is a finite observation in the
declared family, not a theorem.

## Candidate Prior Art (ALL from memory — flagged, unverified, none cited as fact)

Per the no-fake-citations rule: the repo has no process-matrix/quantum-switch
content and no verified literature for this lane; every item below is a
from-memory candidate that MUST be verified before entering `literature/` or
any external-facing artifact.

- Distinguishability–visibility duality: Wootters–Zurek (1979);
  Greenberger–Yasin (1988, `P^2 + V^2 <= 1`); Englert (1996,
  `D^2 + V^2 <= 1`). The two-order result here should be exactly this with
  two composed markers.
- Multipath/multibeam duality (the k >= 3 absorber candidate): Dürr (~2001,
  multibeam visibility measures); Englert et al. (~2008, multi-path duality
  concepts); entropic complementarity treatments (Coles et al.). If the
  class-graded k = 3 structure is a special case of these, the k >= 3
  residue also collapses — this is the named absorber for any promotion.
- Quantum switch and indefinite causal order: Chiribella–D'Ariano–Perinotti–
  Valiron (switch definition); Oreshkov–Costa–Brukner (process matrices);
  Araújo et al. (~2015, SDP causal witnesses / random robustness);
  Procopio et al. (2015) and Rubino et al. (2017) (photonic experiments);
  Zych–Costa–Pikovski–Brukner ("Bell's theorem for temporal order").
- Decohering the switch control (directly adjacent to the record coupling
  here): Brukner-group and related work on switch visibility under control
  decoherence — from-memory; the two-order collapse result is very likely
  implicit or explicit in this literature.
- The "is the photonic switch just an interferometer?" debate (adjacent to
  the reduction audit's interpretational residue): Oreshkov (time-delocalized
  subsystems, ~2019); Vilasini–Renner; Paunković–Vojinović; MacLean et al.
  (quantum-coherent mixtures of causal relations).

## Guardrails

- **Q1D (no-signalling), asserted numerically**: the joint (control, record)
  Z-readout marginal is exactly independent of both parties' operation
  settings (four setting combinations, five gammas, two control phases; max
  difference `1.7e-16`), and the record marginal is exactly independent of
  the control phase. Teeth check: the same settings move the target marginal
  by >= 0.16, so the invariance is not vacuous. Disclosed honestly: a single
  target traverses both operations, so Bell-style spacelike marginal
  independence is not the applicable constraint here; what is asserted is
  that order/record readout cannot be steered by local operation choices.
- **R1**: no claim about global temporal order, simultaneity, or spacetime.
  The artifact is about process composition order only; "order" always means
  composition order of operations.
- Verdict vocabulary predeclared as module constants and asserted verbatim.

## Failure Conditions

- Any tuning of the gamma sweep, tolerances, or the canonical pair to make a
  relation look exact; the sweep, tolerances, and pair-selection criterion
  are predeclared, and the degenerate maximal-sensitivity pair is disclosed
  rather than hidden.
- Claiming a residue in the two-order family after the statevector identity
  holds (the mapping is exact; there is nothing left to differ).
- Claiming the k = 3 pattern as a theorem, an inequality, or a bound beyond
  the exhaustively-verified finite family.
- Treating `V` as a causal witness, or the collapse verdict as a statement
  about genuine process-matrix causal nonseparability (SDP rung not built).
- Any hidden-variable reading of `D` in the coherent regime, any signalling
  reading of the record coupling, or any spacetime claim (Q1D / R1).

## Known Physics Constraints

- The model is a standard coherently-controlled order superposition (the
  qubit quantum switch) plus a which-order marker; no exotic dynamics.
- No-cloning respected: the record copies the control's Z (order) basis via
  a rotation coupling, not an unknown state.
- The k-order control is a k-level system; unused levels carry exactly zero
  amplitude by construction (branch-sum equals gate-built circuit, asserted).
- All quantities are exact statevector functionals; the only grids (fringe
  phase, measurement achievability) cross-check quantities whose exact
  values are computed independently, and carry no verdict.

## What This Does Not Earn

- No new inequality, bound, or theorem. The headline result is a collapse
  verdict plus an exhaustively-verified finite-family observation.
- No causal-nonseparability content: the SDP witness rung is not built; all
  statements are scoped to the visibility signature.
- No upgrade to C1, H1, T49, or any ledger claim; no CLAIM-LEDGER entry.
- No statement about physical platforms or experiments; no external-facing
  artifact. Any move toward the process-matrix community's formalism pauses
  for Joe per AGENTS.md.
- The k = 3 "anti-scalar enters here" reading is a structural observation
  tied to T49's vocabulary, not a derivation of T49's partial order from
  quantum structure.
- Candidate prior art is flagged from memory and verified nowhere; the
  multipath-duality absorber may absorb the k >= 3 residue too.

## Reproduction

```bash
python -m pytest tests/test_record_order_tradeoff_probe.py -v
python -m models.record_order_tradeoff_probe
```

## Contribution Needed

- The SDP rung: a genuine random-robustness causal witness for the reduced
  switch+record process as a function of `gamma`, to replace the visibility
  signature (named v0.1 limitation).
- The multipath-duality absorber run: map the k = 3 class-coarse-record model
  onto multibeam-interferometer duality measures (Dürr-style, once verified)
  and test whether the class-graded structure is transplanted there too. This
  is the k >= 3 analog of this artifact's own kill-test and gates any
  promotion.
- A theorem-form statement of the class-graded trade-off (partition-indexed
  duality: which functionals of (postdiction, coherence structure) are
  exactly conserved) for arbitrary k and arbitrary class partitions, with the
  record register generalized beyond one qubit (nested/partial partitions —
  where genuine T49-style incomparability, not just ties, would enter).
- Multi-holder records: D1's distinct-holder redundancy axis (several record
  qubits, different access sets) — where record-FINALITY, as opposed to
  record-existence, would first become visible in this lane.
