# T408: Basis-Free Flat Pair and the Physical Capability Boundary

## Route

Quantum foundations / bounded control regions / capability objects. The
priced v0.2 card of T407 (region-indexed capability no-go), executed:
physicalization of the capability boundary, answering T407's standing
hostile-review objection that its statistics-flatness leg was relative to
the declared readout convention.

## Claim

In a finite, exactly-simulable ten-qubit family (T392/T393's measurement
core plus an annex record holder and T393's discrete SWAP-chain lightcone),
three parts hold jointly:

1. **Basis-free flat pair.** Two preparations A and B have EXACTLY identical
   full region states `rho_R` on the record region `R = {S, M, F1..F4}` —
   operator equality, asserted `< 1e-12`, computed `1.1e-16`, at every
   certificate phase, every lightcone step, and every leak amplitude. Trace
   distance `7.4e-17` certifies that every POVM on R **in every basis**, and
   every channel-then-readout composition supported on R, yields exactly
   equal statistics (CPTP contractivity) — not just the declared Z readout.
   Yet under ONE fixed intervention menu (all channels supported on the
   accessible zone `Z = R + {AX, C0, C1}`; the menu never touches the
   escaped tail `C2`), capability splits: A's extended undo restores
   phase-locked visibility `4 sqrt(3) / 7 = 0.98974 >= v* = 0.9`, while B's
   recovery is impossible for ALL channels supported on Z (phi-independence
   certificate `2.2e-16`; channel-independent trace-norm bound `1.4e-16`).
   The split is sourced in one physical fact: whether the annex record
   carrier leaked onto the outgoing mode and propagated past the causal
   boundary (T393's forced escape, conditional on emission).

2. **Graded curve.** With T393's partial-amplitude machinery
   (controlled-Ry(alpha) leak), the WHOLE sweep sits on one basis-free flat
   family (`rho_R` identical at every alpha, operator level). The capability
   boundary is a graded physical curve, not a knife-edge: achieved recovery
   `cos(alpha/2) * 0.98974` exactly, escaped-holder branch
   distinguishability `sin(alpha/2)`, exact complementarity (residual
   `<= 4.4e-16`), with the channel-independent bound certifying the
   no-recovery side for every swept `alpha >= 0.7 pi` and an honestly
   disclosed undetermined band where the bound does not bite.

3. **Dissipation bookkeeping (Direction-C entry; NOT a theorem).** Under
   T142's erasure-calibration conventions, restoring capability in A is a
   correlated uncopy: zero Landauer floor, all five handles in-zone. Blind
   reset erases the record at a finite floor (naive `5 ln 2`;
   correlation-aware joint entropy `0.98523` bits at `M = 0`) but restores
   ZERO capability — deletion is not definalization, computed. In B the
   in-zone restoration cost is `+inf` by the empty-feasible-set convention,
   typed precisely: the limiting resource is ACCESS to the escaped holder,
   not work — no work parameter exists in this closed unitary model to
   diverge.

**The obstruction lemma (the residual boundary, stated and witnessed).**
Capability under a menu supported on Z is a functional of the phi-indexed
conditional state family on Z, so a pair operator-flat on the FULL menu
support cannot have a capability gap. Both directions are delivered:
flat-on-R with a certified gap (the construction), and flat-on-Z forcing
zero gap (tail-unitary witness pairs, computed identity to `4.4e-16`). The
flat surface is therefore MAXIMAL at the complement of the menu support: a
capability gap requires a statistical trace within the menu's reach — here
located entirely in zone coherences (zone trace distance `0.49487`) that
are invisible to every measurement on R AND to the full joint Z-basis
readout on the whole zone (diff exactly `0.0`).

## Class

**Exploratory, capability-object lineage; T407's v0.2 card.** NOT registered
in CLAIM-LEDGER. Lineage: T392 (same data / different capability), T393
(causal forcing; certificates; alpha machinery — imported), T407 (the
declared-readout flat class this upgrades), T142 (erasure-calibration
conventions — imported), T144/T145 (deletion vs definalization discipline).
Any promotion pauses for Joe per AGENTS.md.

## Status

Implemented; all three parts hold as stated. 35 tests green; T392/T393/
T407/T142 suites re-run green alongside (87 passed). No claim promotion.

**Numbering collision -- resolved 2026-07-01, authorized by Joe:** while
this artifact was being built, a sibling lane landed a complete quartet
also numbered T404 (`tests/T404-resource-theory-absorber-audit.md` --
T407's named resource-theory absorber audit, whose TESTS.md row registered
before this one). Distinct slugs; both quartets intact. Resolution (per the
T397/T407 precedent, stewardship pass under Joe's direct authorization):
the absorber audit registered first and keeps T404; this artifact is
renumbered T404 -> T408. Substantively the two artifacts compose: the
absorber audit LOCATES T407's residue at the causal-indexing frame and the
declared-record interface, and this artifact CONSTRUCTS exactly that
residue -- a causally indexed capability split with zero record-region
statistical trace at the operator level.

## Target Claims

- [T407: Region-Indexed Capability No-Go](T407-region-capability-no-go.md)
  (the standing objection answered; its Leg-3 flatness upgraded from
  declared-readout-relative to operator-level)
- [T393: Causal Forcing of the Access Asymmetry](T393-causal-forcing-of-access-asymmetry.md)
  (escape construction, certificates, partial-amplitude machinery — imported)
- [T392: Fixed-SBS-Key Reversal Divergence Witness](T392-fixed-sbs-key-reversal-divergence-witness.md)
  (measurement core, statevector primitives, v* — imported unchanged)
- [T142: Thermodynamic Erasure Calibration](T142-thermodynamic-erasure-calibration.md)
  (Landauer bookkeeping conventions — imported)
- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md) (guardrail, asserted numerically)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md) (guardrail; untouched)

## Definitions (R, Z, menu, preparations)

Registers, index-sorted: `S, M, F1, F2, F3, F4, AX, C0, C1, C2` (10 qubits,
Hilbert dimension 1024, exact statevector).

**Record region R** = `{S, M, F1..F4}`: where basis-free flatness is
asserted. **Accessible zone Z** = `R + {AX, C0, C1}`: the ONE fixed menu
support (T393's `r = 1` convention: chain sites 0..1 in reach). **Escaped**:
`C2` (the mode reaches it after `N_STEPS = 2` lightcone steps). All three
declared once, identical for every preparation.

**Shared core (identical couplings in every preparation):** S in
`(|0> + e^{i phi}|1>)/sqrt(2)`; controlled-Ry(theta) S -> M with
`theta = pi/3` (T392's, unchanged); CNOT Z-copies S -> F1..F4; annex copy
CNOT F4 -> AX. The annex copy is the same physical record-copy event in A
and B.

- **A** (carrier retained): nothing emitted; the propagation SWAPs run
  identically on the vacuum chain.
- **B** (carrier escapes): controlled-Ry(alpha) AX -> C0 (default
  `alpha = pi`, the exact Z-copy), then the identical propagation
  SWAP(C0,C1), SWAP(C1,C2).
- **B'** (emission null): X on C0 — a real excitation uncorrelated with the
  record — then the identical propagation.
- **A_tail / B_tail** (obstruction witnesses): A / B followed by a unitary
  on the escaped tail C2 only.

Because the leak and everything downstream of it are supported on the
complement of R, `rho_R(A) = rho_R(B)` is an **operator identity by
construction** (states differing by a unitary on `R`'s complement have equal
reduced states on R) — and it is asserted numerically anyway, since the
construction, not the assertion, is what a hostile review would probe.

**Menu**: all channels supported on Z. The achieving protocol (extended
undo: CNOT F4 -> AX, then the four fragment uncopies) is exhibited; the
impossibility side quantifies over ALL CPTP maps on Z via T393's
certificates. Figure of merit: phase-locked conditional X-visibility over
the uniform 8-point grid (T392's gameability lemma; the manufactured-
coherence exploit scores raw `1.0`, locked `6.9e-17`). Threshold `v* = 0.9`
imported unchanged.

## Setup

`models/basis_free_capability_boundary.py`; exact statevector, numpy,
deterministic (the Haar spot check and the random-basis check are seeded and
illustrative; certificates carry every verdict). Imports by name: T392's
`THETA`, `V_STAR`, `_HADAMARD`, `reduced_density_matrix`, `z_distribution`,
`zero_state`; T393's `PHI_CERT` (incommensurate phases included),
`PHI_LOCK_GRID`, `apply_on_qubits`, `haar_unitary`, `_trace_norm`; T142's
`landauer_bound_bits`, `LANDAUER_NAT_PER_BIT`. T392's `project_qubit` is
imported for provenance and replaced by a numerically identical
reshape-based projector (the dense-matrix version is prohibitive at
`n = 10`); the replacement is asserted equivalent in the suite's neighbor
re-runs.

## Verified exactly (assertions)

1. **Operator flatness of `rho_R`** across A/B/B' and the whole alpha sweep,
   at all six certificate phases: max entrywise diff `1.1e-16`, max trace
   distance `7.4e-17` (asserted `< 1e-12`); per lightcone step: `0.0`;
   M-conditioned on the active record region: `0.0`.
2. **Basis-free consequences**: 20 seeded Haar-random bases on R, max
   probability diff `0.0` (illustrative; the operator equality is the
   proof); declared Z-readout diff `0.0` (a fortiori). Disclosure: `rho_R`
   is also phi-independent WITHIN each preparation (`1.7e-16`) — the annex
   copy fully dephases the record region; the phase lives in annex/chain
   correlations.
3. **Capability split under the fixed zone menu**: A `0.98974 >= v*`
   (equals `4 sqrt(3)/7` to `1e-12`; H(A) = 5, every 4-holder subset scores
   `0.0`); B `6.1e-17` with the all-channel certificates (zone
   phi-independence `2.2e-16`; trace-norm bound `1.4e-16 < v*`; 15 seeded
   Haar zone unitaries max `1.6e-17`, illustrative); H(B) = inf; verdicts
   `recoverable-in-access-zone` vs `final-relative-to-access-zone`.
4. **R-only menu null**: on R alone BOTH preparations are certified
   unrecoverable (cert `2.2e-16`, bound `1.2e-16` each) — A's capability
   genuinely requires the annex; the flat surface is not the recovery
   surface.
5. **B' emission null**: capability identical to A (diff `0.0`), region
   state identical (`0.0`), while the emission is real (chain excitation
   `1.0` vs A's `0.0`; B's is `0.5`).
6. **Recovery window**: in-zone undo of B recovers `0.98974` at steps 0 and
   1 (mode in reach; zone state phi-dependent, `0.857`) and `6.1e-17` at
   step 2 (zone cert fires: `2.2e-16`); counterfactual enlargement across
   the boundary restores `0.98974` exactly (diff `0.0`) and the enlarged
   state is phi-dependent again (`0.857`).
7. **Obstruction lemma witnessed**: tail-unitary pairs have zone-family diff
   `1.1e-16` and capability-column diffs `<= 4.4e-16` (visibility, bound, H)
   — flat-on-menu-support forces no gap. Trace location: zone trace
   distance A vs B `0.49487` (real), zone joint Z-basis readout diff `0.0`,
   zone single-qubit marginal diff `0.0` — the trace is pure zone coherence.
8. **Graded curve** (`alpha/pi` in {0, .25, .5, .7, .75, .9, .98, 1}):
   `rho_R` flat at every alpha (`<= 1.1e-16`); achieved = analytic
   `cos(alpha/2) * 0.98974` to `< 1e-9`; bound below `v*` for all
   `alpha >= 0.7 pi` (`0.8987, 0.7575, 0.3097, 0.0622, 0.0`), protocol
   feasibility for `alpha <= 0.25 pi` (analytic feasibility edge
   `alpha = 0.27319 pi`), `0.5 pi` honestly undetermined (bound `1.3997`,
   achieved `0.6999`); complementarity `(ach/vis_A)^2 + sin^2(alpha/2) = 1`
   to `4.4e-16`; escaped Holevo content rises `0 -> 0.98523` bits
   (= `h2(3/7)` at `M = 0`), conditional states pure (`< 1e-15`).
   Disclosure: in this family the bound computes to exactly twice the
   achieved value, so its bite threshold (`~0.6994 pi`) is not tight
   against the feasibility edge; the analytic `alpha*(v*)` boundary stays
   on T393's open card.
9. **Dissipation ledger (T142 conventions)**: restore-A = correlated
   uncopy, `erased_bits = 0`, `beta W >= 0`, achieves `0.98974`; blind
   reset of the five in-reach holders = naive floor `5 ln 2 = 3.4657` nats
   (joint record entropy `0.98523` bits at `M = 0`, `1.0` unconditioned,
   disclosed side by side), capability after reset `0.0`, residual record
   `0.0` — deletion is not definalization; restore-B in-zone: feasible set
   EMPTY (certified), min cost `inf` as an empty-set infimum, limiting
   resource typed as access-not-work; counterfactual enlargement: 6-holder
   uncopy at zero floor restores `0.98974` exactly (blind-reset disclosure
   `6 ln 2`).
10. **Q1D asserted numerically**: declared R readout invariant across
    preparations, phases, and leak amplitudes (`1.1e-16`); in-zone undo
    cannot move the escaped marginal (`0.0`) while the counterfactual
    enlarged undo moves it by `0.42857 = 3/7` (teeth); zone trace-distance
    teeth `0.49487`. **R1 untouched** (discrete lightcone carries
    T393/T379's caveats).

## Success Criteria

- Operator flatness of `rho_R` `< 1e-12` at every phase/step/alpha AND a
  capability gap `> 0.9` with the zero side certified against all zone
  channels; failure of either would have been the reportable verdict.
- The A-side protocol reaches `v*`; the B-side impossibility comes from the
  certificates, never from protocol sampling.
- The obstruction lemma witnessed in both directions (tail pairs identical;
  zone trace real and located).
- Graded sweep: flatness at every alpha; achieved matches the analytic
  factor; three bands (feasible / undetermined / certified) all realized
  and consistent with the analytic feasibility edge.
- Ledger entries computed, typed with T142 vocabulary, and scoped as
  bookkeeping.

## Failure Criteria

- Any weakening of the operator-equality assertions to make the gap appear
  (the honesty rule: fix the construction, never the assertions). If NO
  construction had satisfied exact `rho_R` equality with a certified gap,
  the reportable verdict was predeclared: "capability difference requires
  an in-region statistical trace" — the T407-noted obstruction extended to
  the record region, connecting to T392's converse pair. (Did not occur;
  the obstruction instead localizes exactly at the menu support.)
- Region, zone, or menu adjusted per preparation; the escaped site quietly
  included in any admissible protocol.
- Recovery measured by raw visibility (gameable; the manufactured-coherence
  control is implemented).
- Part 3 stated as a thermodynamic result, or the B-side infinity read as a
  divergent work requirement.
- Claiming this clears T400's boundary-forced-task gate (it does not and
  does not try).

## Neighbors / Prior Art

In-repo:

- **T407 (region-indexed capability no-go)** — the artifact this upgrades.
  T407's 16-member flat class had configurations differing INSIDE R as
  operators (phase-basis writes), equal only in the declared Z readout; its
  spec priced exactly this objection and named the v0.2 card. Here the flat
  pair is operator-equal on R, so no readout convention, in any basis, can
  split it — the flatness is physical (sourced in causal escape), not
  bookkeeping. T407's other legs (profile poset, anti-scalar) are not
  re-litigated.
- **T393 (causal forcing)** — supplies the escape construction, both
  impossibility certificates, the alpha machinery, and the Tier-1 forcing
  argument (conditional on emission) that makes the zone boundary
  non-conventional. T393's own A/B pair was NOT operator-flat on its
  declared register (coherence diff `0.433`, disclosed there); this
  artifact's pair is — the flatness upgrade is the new content.
- **T392** — the "same data, different capability" pattern; core imported.
  Its converse-pair lesson (neither typing refines the other) reappears
  here as the obstruction lemma's two directions.
- **T398 (resource-profile absorber)** — demanded "equality under all
  R-supported intervention statistics, separated only by a boundary-crossing
  menu." This artifact delivers the first half exactly (operator equality
  on R implies all R-intervention statistics equal); the separator is NOT a
  boundary-crossing menu between compared objects — the menu is fixed and
  identical; the preparations differ by a physical escape event outside R.
- **T399 (boundary-crossing intervention screen)** — the nearest-looking
  neighbor, differentiated sharply: T399's Bell pair separates only when
  the menu is RELOCATED (region-only vs admitted joint access), which is
  why it absorbed as ordinary enlarged-state access. Here nothing is
  admitted differentially: one menu, both preparations, and the zero side
  is all-channel certified on the full menu support. What T399 varied (the
  access) is held fixed; what T399 held fixed (the physical escape status)
  varies.
- **T400/T401/T402/T403 (forced-task lane)** — orthogonal continuation of
  T399; those artifacts hunt a task whose boundary-crossing is forced by
  the task declaration. This artifact does NOT clear T400's gate and does
  not claim to: its task is the house reversal task, and the boundary
  enters through the certified impossibility, not the task declaration.
- **T142 / T144 / T145** — the erasure-calibration conventions and the
  deletion-vs-definalization discipline, here computed inside one quantum
  family: the blind reset pays the Landauer floor and restores nothing.
- **T151 / T153** — causal-access screens; as in T393, the A/B split is not
  a changed access diamond (identical region, zone, and circuit skeleton;
  only what was written to the outgoing port differs).
- **s6-g9** — same-final-record capability pair, formal side; no dynamics.
- **open-problems/region-indexed-capability-discriminator.md** — the card's
  stronger fixture shape ("equality under all in-region interventions,
  separation only via boundary-crossing menu") is here shown to be
  IMPOSSIBLE in its naive form by the obstruction lemma when "separation"
  means a capability gap under the same menu — and the deliverable form
  (flat up to the menu boundary, gap sourced beyond it) is constructed.

Candidate prior art (ALL from memory — flagged, unverified, per the
no-fake-citations rule): **purification freedom / Schroedinger-HJW** — that
states differing by an isometry on the complement have equal reduced states
is textbook quantum information; the flat pair's EXISTENCE is therefore
standard and is not the claimed content. The claimed residue is the
assembled object: exact flatness on a declared record region JOINTLY with a
fixed-menu all-channel-certified capability gap, causal sourcing of the
difference (T393), the maximality lemma at the menu support, the graded
flat family, and the T142-typed ledger. **Environment-assisted recovery /
Petz recoverability** and **quantum steering** are adjacent frames for the
annex-side recovery; no result from either is claimed or used. If
verification shows even the assembled object is standard, the artifact
re-scopes to a repo-internal calibration.

## Honest Reviewer Attack Surface

- **"Flatness is trivial — you built the difference outside R."** Correct,
  and by design: the operator identity is the point, not a gotcha. T407's
  objection was that its flat class was flat only in a declared readout;
  the honest fix is a pair whose in-region flatness is EXACT and basis-free,
  which requires sourcing the difference outside R. The non-trivial content
  is that a certified capability gap SURVIVES this total in-region
  flatness under a menu that reaches beyond R; that A's recovery genuinely
  needs the annex (R-only null: both preparations certified final relative
  to R); and that the obstruction lemma makes this the maximal flat
  surface.
- **"You moved the convention from the readout basis to the R/Z split."**
  The R/Z split is fixed once, identically, for both preparations — nothing
  about it does differential work. The differential fact is the leak and
  its causal escape, which is T393's Tier-1-forced boundary (conditional on
  emission), cited not re-derived. What remains declared is that the
  apparatus has SOME bounded zone — T393's residual premise, unchanged.
- **"This is T399 with extra qubits."** See Neighbors: T399 compared menus
  at a fixed pair; this compares preparations at a fixed menu. T399's
  absorber verdict (admitted joint access) has no purchase here because no
  access is admitted differentially; the counterfactual enlargement is
  labeled counterfactual and never admissible.
- **"The annex is T392's A0 renamed."** A0's access triple was stipulated
  per preparation; AX's access status is identical in both preparations.
  The stipulation T392 needed is exactly what this construction does not
  have.
- **"The bound is loose (exactly 2x achieved), so the graded certification
  band is weak."** Disclosed in the spec and the results: the bound bites
  at `~0.70 pi` while feasibility ends at `0.273 pi`; the mid-band is
  reported as undetermined, and the analytic threshold stays on T393's
  open card.
- **"Part 3 dresses bookkeeping as thermodynamics."** Scoped against this
  reading everywhere it appears: no bath, no temperature, no work
  parameter; the infinity is an empty-set infimum typed as an access
  obstruction; the genuine open-system bound is the named, unbuilt Tier-2
  card.

## Known Physics Constraints

- No-cloning respected: all copies (fragments, annex, leak) are Z-basis
  copies of an already-branched record.
- The impossibility side quantifies over all CPTP maps on the zone via the
  trace-norm bound; no channel enumeration carries a verdict.
- Exact statevector throughout; the only randomness (Haar and random-basis
  spot checks) is seeded and illustrative.
- Perfect couplings at `alpha = pi` are the idealization of the graded
  family built in Part 2 (the same disclosure T393 v0.1.1 earned).

## What This Does Not Earn

- **No thermodynamic theorem.** Part 3 is bookkeeping in a finite closed
  unitary model. The genuine bound (bath dispersion; work/entropy scaling
  with bath contact) is T393's Tier-2 card: named, unbuilt, Direction-C-
  facing.
- **No claim promotion, no CLAIM-LEDGER entry**; ledger actions pause for
  Joe per AGENTS.md.
- **No clearing of T400's forced-task gate** — the task here is the house
  reversal task; the domain-native forced-task burden stays open.
- **No new mathematics**: the flat pair's existence is presumed textbook
  (purification freedom, flagged from memory); the obstruction lemma is an
  elementary functional-dependence fact stated as discipline.
- **No hardware, platform, or experimental claim**; not TI's Ext_S surplus
  (out of scope by construction, as in T407).
- The 2x-loose bound leaves the mid-alpha band undetermined; the analytic
  `alpha*(v*)` boundary is not earned here.

## Reproduction

```bash
python -m pytest tests/test_basis_free_capability_boundary.py -v
python -m models.basis_free_capability_boundary
```

Deterministic; ~2 s and ~8 s respectively.

## Contribution Needed

- The Tier-2 thermodynamic artifact: replace the three-site chain with a
  many-mode bath and test whether the in-zone restoration ledger acquires a
  genuine work/entropy scaling with bath contact (Direction C's dissipation
  accounting; the T144/T145 fixed-accounting discipline binds there).
- The analytic `alpha*(v*)` threshold and a tighter channel bound (the
  factor-2 looseness is now measured in two artifacts).
- A T407-bridge: rebuild T407's full profile family (readout tasks
  included) on top of an operator-flat substrate like this one, to see how
  much of the 3 x 4 capability grid survives exact flatness.
- Verify the flagged prior art (purification freedom, Petz/steering
  adjacency) before anything external-facing.
