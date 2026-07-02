# T409: Capability Restoration Frontier — Thermodynamic Forcing of Bounded-Agent Capability Loss

## Route

Quantum measurement / open-system collision models / bounded control
regions / capability objects. The named unbuilt card, executed at its
finite rung: T393's **Tier-2 (thermodynamic) forcing** — "bath dispersion;
undo cost scaling with bath contact" — which T393 named, T408 re-named
("the genuine open-system bound is T393's Tier-2, unbuilt"), and the
Direction-B checkpoint priced as the load-bearing gap ("real apparatuses
are bounded-region agents whose emitted records disperse beyond feasible
re-collection"). Direction C's first quantitative frontier; Direction B's
re-entry point.

**Hostile review is QUEUED for this artifact, not yet performed** — as for
T404 and T408 (per the 2026-07-02 stewardship postscript). Nothing below
has survived independent adversarial reproduction yet.

## Claim

In a finite open-system collision model — a record qubit `REC` holding the
which-way copy of system `S` (T392's measurement core: prepared phase
`phi`, weak meter `M` at `theta_meter = pi/3`, `CNOT` copy `S -> REC`),
interacting sequentially with a stream of fresh bath qubits `B1..B7` via
CNOT-type collisions of strength `theta` (controlled-Ry(theta), T393's
emission gate; `theta = pi` is the exact CNOT copy) — capability
restoration is governed by a **reach–work frontier**, three legs holding
jointly:

1. **Dispersion forces reach growth.** After `n` collisions, restoring
   `S`'s phase-locked visibility `>= v* = 0.9` (T392's threshold,
   unchanged) requires touching at least `r(n)` bath qubits, with `r(n)`
   monotonically growing — at `theta = pi` **exactly `r(n) = n` for every
   `n = 1..7`**, certified per `n` by the T393/T408 all-channel machinery
   (phi-independence certificate, worst `2.2e-16`; channel-independent
   trace-norm bound, worst `1.4e-16`) applied to insufficient-reach
   subsets: **exhaustively over every subset** (all `2^n`, every size) for
   `n <= 4` at two strengths, symmetry-pruned beyond — with the pruning
   itself asserted (permuted same-size reach subsets at `n = 7` have
   identical conditional states to `1.1e-16`; the collisions share the
   control `REC`, so they commute and the bath is permutation-symmetric).
   The record has an **escape velocity of one reach-unit per collision**
   beyond the onset delay: a reach frontier through the bath — not a light
   cone, but the same certified shape. Saturations are located exactly
   (see leg 3 and the contrast probes), as predeclared reportable
   findings.

2. **Work does not substitute for reach.** The certificates quantify over
   ALL CPTP maps on the reach, and both are **invariant under adjoining
   work registers**: any channel assisted by finitely many ancillas in any
   phi-independent state IS a channel on the reach (Stinespring), and
   adjoining a fixed state `sigma` sends the certificate operator `X` to
   `X (x) sigma` with `||A (x) sigma||_1 = ||A||_1` — asserted numerically
   (certificate on reach + work `2.2e-16`; bound ancilla-invariance diff
   `0.0`; every frontier bound at `n = 4` recomputed with work registers
   adjoined, max diff `4.9e-32`). Fresh work manufactures coherence but
   never phi-LOCKED coherence (T393's lemma, implemented: the
   |+>-injection exploit scores raw `1.0`, locked `6.9e-17`; the
   measure-and-feedback channel `0.0`; 15 seeded Haar unitaries on
   reach + work `2.1e-17`, illustrative). **Sharp form: the frontier is
   priced in reach, not work — reach-absolute at fixed reach.** Deletion
   is not definalization (T408's ledger, imported and recomputed here:
   blind reset pays the naive `5 ln 2` floor and restores `0.0`).

3. **The graded frontier + Landauer ledger.** With partial strength
   `theta`, the frontier surface is
   `r_feas(n, theta) = max(0, n - d(theta))`,
   `d(theta) = floor(ln(v*/vis_A) / ln cos(theta/2))` — an onset delay of
   `d` collisions, then slope-1 growth; computed exactly across
   `theta/pi in {0.1, 0.15, 0.2, 0.25, 0.5, 0.7, 0.75, 1}` and `n = 1..7`,
   with achieved `= vis_A cos(theta/2)^u` (`u` = unreached contacts) to
   `< 1e-9`. The certified frontier `r_cert` brackets it from below:
   **exact** (`r_cert = r_feas`) for `theta > 0.6995 pi` (the bite edge —
   the trace-norm bound computes to exactly `2x` achieved, the same
   factor-2 looseness measured in T393 and T408, now in a third artifact),
   width 2 at `theta = 0.5 pi` (`r_cert = max(0, n - 2)`), and **honestly
   vacuous** at weak coupling within this bath size (`u_min_cert in
   {10, 16, 29, 64} > 7` for `theta <= 0.25 pi`). The onset-delay
   threshold is T408's protocol-feasibility edge `0.27319 pi`, reappearing
   as frontier structure. **T142-convention ledger** (dimensionless
   `beta W >= bits ln 2`): restore-within-reach = correlated uncopy,
   `erased_bits = 0`, achieves `vis_A cos^u`; blind reset of the five
   in-reach holders pays naive `5 ln 2 = 3.4657` (joint record entropy
   `0.98523` bits at `M = 0`, `1.0` unconditioned, disclosed side by side)
   and restores `0.0`; beyond the frontier the feasible set is EMPTY
   (certified) and the min cost is an empty-set infimum **typed as
   access-not-work** (no work parameter exists in this closed unitary
   model to diverge). **The stated, computed correspondence:** capability
   deficit `1 - (achieved/vis_A)^2` EQUALS the squared branch
   distinguishability displaced into the unreached bath (complementarity
   residual `<= 9.8e-15` across both swept strengths), and the reach
   deficit `u = n - r` counts the **record-bearing bath contacts beyond
   reach**. Disclosure with teeth: at `theta = pi` the escaped Holevo
   content SATURATES at `h2(3/7) = 0.98523` bits for every `u >= 1` (one
   branch bit, redundantly broadcast — quantum-Darwinism structure) while
   the frontier keeps growing — the frontier is priced in **contacts, not
   bits**, just as leg 2 shows it is not priced in work. Scoped as
   finite-model bookkeeping; the continuum/asymptotic bath-dispersion
   theorem stays **named-unbuilt**.

**Dispersion-structure contrasts (computed):** (i) full-SWAP stream —
displacement without dispersion: the record moves to `B1` and later
collisions change NOTHING (state freeze diff exactly `0.0`); `r(n) = 1`
saturates and the frontier is subset-specific (every subset missing `B1`
certified at every size, exhaustive at `n = 3`) — frontier GROWTH is
sourced in broadcast (new record-bearing contact per collision), not in
motion of the record. (ii) Uncorrelated stream (`Ry(theta)` on each bath
qubit, no control) — real excitation (up to 3.5 quanta), no record:
`r(n) = 0` at every `n`; bath contact per se is free (T393's B' lineage).
(iii) Weak coupling `theta = 0.1 pi`: analytic onset `n = 8` exceeds the
bath size, so `r_feas = 0` throughout — saturation at zero within the
family, located exactly.

**What this earns if all legs pass (they do, as stated):** inside this
finite formalism the bounded-region premise becomes physical — **any
finite-reach agent in a dispersive (broadcasting) environment suffers
forced, work-insensitive, monotonically growing capability loss**. Tier-2
forcing at the collision-model rung, completing T393's Tier-1; Direction
C's first quantitative frontier; Direction B's re-entry. NOT earned: the
continuum limit, real bath thermodynamics, hardware (see What This Does
Not Earn).

## Class

**Exploratory, capability-object lineage; T393's named Tier-2 card at its
finite rung.** NOT registered in CLAIM-LEDGER. Lineage: T392 (measurement
core, v*, gameability lemma), T393 (certificates, emission gate, forcing
hierarchy — this artifact is its Tier-2 entry), T407/T408 (capability
boundary; operator-level flatness discipline; graded-band honesty), T142
(erasure-calibration conventions), T144/T145 (deletion vs definalization
discipline). Any promotion pauses for Joe per AGENTS.md. Hostile review
QUEUED.

## Status

Implemented; all three legs hold as stated. 36 tests green;
T392/T393/T408/T142 suites re-run green alongside (124 passed). No claim
promotion. Hostile review queued, not performed.

## Target Claims

- [T393: Causal Forcing of the Access Asymmetry](T393-causal-forcing-of-access-asymmetry.md)
  (the Tier-2 card built here at its finite rung; certificates and the
  partial-strength gate imported)
- [T408: Basis-Free Flat Pair and the Physical Capability Boundary](T408-basis-free-capability-boundary.md)
  (the capability-boundary object this extends from one escape event to a
  dispersive stream; ledger discipline imported)
- [T407: Region-Indexed Capability No-Go](T407-region-capability-no-go.md)
  (C(R) lineage; the reach parameter is a graded region index)
- [T392: Fixed-SBS-Key Reversal Divergence Witness](T392-fixed-sbs-key-reversal-divergence-witness.md)
  (measurement core, statevector primitives, v* — imported unchanged)
- [T142: Thermodynamic Erasure Calibration](T142-thermodynamic-erasure-calibration.md)
  (Landauer bookkeeping conventions — imported)
- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md) (guardrail, asserted numerically)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md) (guardrail; untouched)

## Definitions (registers, reach, menu, frontier)

Registers, index-sorted: `S, M, REC, B1..B7` (10 qubits, Hilbert dimension
1024, exact statevector). Collision order = bath index order.

**Shared core (identical in every preparation):** `S` in
`(|0> + e^{i phi}|1>)/sqrt(2)`; controlled-Ry(`theta_meter = pi/3`)
`S -> M` (T392's weak meter, measured; verdicts conditional on `M = 0`,
the dominant branch); `CNOT S -> REC` (the which-way record copy).
`vis_A = 4 sqrt(3)/7 = 0.98974` (the zero-collision restorable value,
asserted).

**Collision families:** `cnot` — controlled-Ry(theta) `REC -> B_i`, a
strength-theta partial Z-copy per fresh bath qubit (broadcast; the primary
certified family); `swap` — full `SWAP(REC, B_i)` (displacement contrast
probe); `uncorrelated` — `Ry(theta)` on `B_i`, no control (record-free
null).

**Reach**: the apparatus core `{S, M, REC}` plus `r` bath qubits (active
support `{S, REC}` + reached bath; `M` is measured). Declared once,
identical for every family. **Menu**: ALL channels supported on the reach,
with unlimited work ancillas (leg 2 makes the ancilla-invariance explicit
rather than implicit). Figure of merit: phase-locked conditional
X-visibility over the uniform 8-point grid (T392's gameability lemma;
manufactured coherence exactly nulled). Threshold `v* = 0.9` imported
unchanged.

**Frontier**: `r_feas(n, theta)` = least reach size whose achieving
protocol (un-write reached copies via controlled-Ry(-theta), then uncopy
`REC`; all gates reach-supported) restores `>= v*`; `r_cert(n, theta)` =
greatest reach size such that every smaller reach is trace-norm-certified
infeasible (`bound < v*`) for all channels. `r_cert <= r_true <= r_feas`;
where they coincide the frontier is exact.

## Setup

`models/capability_restoration_frontier.py`; exact statevector, numpy,
deterministic (the only sampling — Haar spot check, 15 samples, seed
`20260702` — is illustrative; certificates carry every verdict). Imports
by name: T392's `THETA` (meter), `V_STAR`, `_HADAMARD`,
`reduced_density_matrix`, `z_distribution`, `zero_state`; T393's
`PHI_CERT` (incommensurate phases included), `PHI_LOCK_GRID`,
`apply_on_qubits`, `haar_unitary`, `_trace_norm`; T142's
`landauer_bound_bits`, `LANDAUER_NAT_PER_BIT`. The reshape-based
`project_qubit` is T408's (numerically identical to T392's dense version;
neighbor suites re-run green alongside). Runtime: model `~3 s`, suite
`~4 s` (predeclared budget `< 90 s`).

## Verified exactly (assertions)

1. **Leg-1 headline frontier** (`theta = pi`): `r_feas = r_cert = n` for
   `n = 1..7`; every insufficient reach cell has phi-certificate
   `< 1e-12` (worst `2.2e-16`) and bound `< 1e-12` (worst `1.4e-16`);
   full reach restores `0.98974` (= `4 sqrt(3)/7` to `1e-12`).
2. **Exhaustive certification**: all `2^n` subsets for `n <= 4` at
   `theta in {0.5 pi, pi}` — same-size value spread `0.0`; exhaustive
   frontier equals canonical; at `theta = pi` every proper size certified.
3. **Symmetry pruning asserted**: permuted same-size subsets at `n = 7`,
   sizes {1, 3, 6}, two strengths, two phases: max state diff `1.1e-16`.
4. **Monotonicity + escape velocity**: `r_feas`, `r_cert` non-decreasing
   in `n` at every swept `theta`; slope exactly 1 beyond onset.
5. **Work invariance (leg 2)**: certificate on reach + work `2.2e-16`;
   bound ancilla diff `0.0`; frontier-with-work max diff `4.9e-32`;
   manufactured raw/locked `1.0 / 6.9e-17`; feedback channel `0.0`; Haar
   `2.1e-17 < 0.05`.
6. **Graded surface**: `r_feas(n, theta) = max(0, n - d)` with
   `d = {7, 3, 1, 1, 0, 0, 0, 0}` across the sweep; `r_cert` exact above
   the bite edge, `max(0, n - 2)` at `0.5 pi`, vacuous (`0`) at
   `theta <= 0.25 pi` with `u_min_cert > 7` — three bands all realized on
   the `theta = 0.5 pi, n = 7` column; bound `= 2x` achieved to `1e-9`
   (disclosed looseness).
7. **Ledger + correspondence**: complementarity residual `<= 9.8e-15` at
   all 16 correspondence rows; escaped Holevo monotone in `u`, saturating
   at `h2(3/7) = 0.985228` bits for every `u >= 1` at `theta = pi`;
   restore-within-reach `erased_bits = 0`; blind reset naive floor
   `5 ln 2`, capability after `0.0`, residual record `0.0`; beyond
   frontier `inf` (empty-set infimum), typed access-not-work.
8. **Contrast probes**: swap freeze diff exactly `0.0`, `r = 1` saturated,
   subsets missing `B1` certified at every size; uncorrelated null
   `r = 0` with real excitation (teeth); `theta = 0.1 pi` saturation at
   zero located (onset `n = 8`).
9. **Q1D asserted numerically**: declared `(S, M)` record invariant across
   families, counts, strengths (`1.1e-16`); reach protocol moves unreached
   marginals by `0.0`; counterfactual enlarged protocol moves them by
   `3/7 = 0.42857` (teeth — T408's number). **R1 untouched.**

## Success Criteria

- The frontier exists and grows: `r_feas` and `r_cert` monotone
  non-decreasing at every swept strength, with the `theta = pi` frontier
  exact (`r_cert = r_feas = n`) and every insufficient reach certified
  against all channels — never from protocol sampling.
- Exhaustive subset coverage at small `n`; symmetry pruning asserted, not
  assumed, before any canonical-subset shortcut is used.
- Work invariance of both certificates AND of the frontier itself,
  numerically; the manufactured-coherence and feedback attacks nulled.
- Graded surface matches the predeclared closed forms; the certified
  bracket and its honest gaps (undetermined band; vacuous-at-weak-coupling)
  reported as computed.
- Ledger entries computed and typed with T142 vocabulary; the
  contacts-not-bits disclosure stated with the saturating Holevo numbers.

## Failure Criteria

- **Predeclared reportable verdicts (failure legs are findings, not
  patches):** if `r(n)` saturates or is non-monotone anywhere, report
  exactly where — that is a real finding about dispersion structure (this
  occurred, by design, in the contrast probes: swap saturation at
  `r = 1`, weak-coupling saturation at `r = 0`, both located and typed;
  the broadcast family itself is monotone). If any insufficient-reach
  subset admits a certified restoration, leg 1 fails and the frontier is
  protocol-relative only — report as "frontier not channel-forced".
  If any certificate or the frontier moves under work adjoining, leg 2
  fails — report as "frontier is work-priced after all" (would have been
  the headline). If a correspondence row breaks complementarity, leg 3's
  ledger claim fails and is reported, not repaired.
- Any tuning of `v*`, the phase grids, the theta sweep, or the subset
  family after inspecting values (all fixed before frontier computation;
  `v*` and grids imported unchanged).
- Recovery measured by raw visibility (gameable; the exploit is
  implemented as a null control).
- Leg 3 stated as a thermodynamic theorem, the infinity read as divergent
  work, or the Holevo saturation hidden to make "bits" the currency.
- The escaped/unreached bath quietly included in any admissible protocol;
  reach adjusted per preparation or per family.

## Neighbors / Prior Art

In-repo:

- **T393** — supplies both certificates, the emission gate, and the tier
  vocabulary; this artifact is its named Tier-2 card at the finite rung.
  T393's chain was a propagation line (one escaping mode); here the
  environment is a broadcast stream (one new record-bearing contact per
  step) — that difference IS the frontier's growth, isolated by the swap
  contrast (a T393-style moving mode saturates at `r = 1`).
- **T408** — the operator-level capability boundary at one escape event;
  its ledger (deletion vs definalization; access-not-work typing; the
  `2x`-loose bound; `h2(3/7)`; the `3/7` teeth) recurs here computed on a
  family. T409 adds the reach axis and the growth theorem-shape.
- **T407 / T404 / T398** — the C(R) lineage; reach is a graded region
  index, and the frontier is a one-parameter capability curve per
  `(n, theta)`. The resource-frame caveats located by T404 carry over
  unexamined (the audit is not re-run here).
- **T142 / T144 / T145** — the ledger conventions and the
  deletion-is-not-definalization discipline, recomputed in this family.
- **T400** — NOT cleared and not attempted: the task here is the house
  reversal task; the boundary enters through certified impossibility, not
  task declaration.

Candidate prior art (ALL from memory — flagged, unverified, per the
no-fake-citations rule; **named as absorber risks** for the queued
hostile review):

- **Collision models / repeated-interaction systems** (Ziman–Bužek-style
  homogenization; Ciccarello-review lineage) — sequential fresh-ancilla
  collisions are a standard open-system device; the MODEL is presumed
  standard and is not the claimed content.
- **Quantum Darwinism bath models** (Zurek; Riedel–Zurek photon
  environments) — redundant record broadcast into environment fragments
  is exactly the `theta = pi` structure, and the Holevo-saturation
  disclosure is its signature. The claimed residue is the assembled
  frontier object: per-`n` all-channel certified reach lower bounds, the
  work-invariance lemma, the graded `r(n, theta)` surface with honest
  bands, and the T142-typed ledger — not the broadcast structure itself.
- **Lieb-Robinson bounds** — the frontier is a reach frontier through an
  interaction sequence, not a spatial light cone; no locality bound is
  claimed or used. Named so a reviewer does not have to ask.
- **Environment-assisted recovery / Petz recoverability** — adjacent
  frame for the sufficient-reach side; no result from either is claimed
  or used.

If verification shows even the assembled object is standard, the artifact
re-scopes to a repo-internal calibration (same clause as T408).

## Honest Reviewer Attack Surface

- **"r(n) = n is trivial for perfect copies."** The value is not the
  arithmetic but the certification form: every insufficient subset
  all-channel certified (exhaustive at small `n`, asserted symmetry
  beyond), the work-invariance made explicit, and the graded surface with
  its bracket honestly split into exact/width-2/vacuous regimes. The
  trivial-looking headline is the anchor of a computed surface.
- **"The frontier is protocol-relative below the bite edge."** Correct
  and reported: for `theta <= 0.25 pi` the certified frontier is vacuous
  within this bath size — `r_feas` there is an upper bracket only. The
  factor-2 bound looseness is now measured in three artifacts; tightening
  it is a named open card (T393's `alpha*(v*)`).
- **"Work-invariance is a one-line lemma."** Yes — stated as discipline
  and asserted numerically because the Tier-2 claim ("work does not
  substitute for reach") is exactly the sharp form of that lemma; the
  point is that the frontier's currency is proven to be reach, not that
  the lemma is deep.
- **"No thermodynamics here."** Agreed in the strict sense and scoped
  everywhere it appears: no bath Hamiltonian, no temperature, no work
  parameter; the ledger is T142-convention bookkeeping. "Thermodynamic
  forcing" names T393's tier, whose finite rung this is; the continuum
  statement stays named-unbuilt. If the reviewer prefers "dispersive
  forcing" for this rung, nothing substantive changes.
- **"The collision stream is engineered."** The stream is the standard
  collision-model device (flagged prior art); the B'-style uncorrelated
  null shows contact alone does nothing, and the swap probe shows motion
  alone does nothing — what forces the frontier is record-bearing
  broadcast, which is the physics being modeled, not smuggled.

## Known Physics Constraints

- No-cloning respected: all collisions copy (partially or fully) the Z
  basis of an already-branched record.
- The impossibility side quantifies over all CPTP maps on the reach via
  the trace-norm bound and the phi-independence certificate; no channel
  enumeration carries a verdict; work ancillas covered by the dilation
  lemma, asserted numerically.
- Exact statevector throughout; the only randomness (Haar spot check) is
  seeded and illustrative.
- Perfect collisions at `theta = pi` are the idealization anchoring the
  graded family (T393 v0.1.1's disclosure pattern).

## What This Does Not Earn

- **No continuum or asymptotic bath-dispersion theorem** — the named
  card at the next rung stays unbuilt: work/entropy scaling in a genuine
  open-system bath (Hamiltonian bath, temperature, weak-coupling limit).
- **No real bath thermodynamics**: leg 3 is bookkeeping in a finite
  closed unitary model; the infinity is an access obstruction in
  extended-real convention, never a work divergence.
- **No hardware, platform, or experimental claim**; no T166 packet.
- **No claim promotion, no CLAIM-LEDGER entry**; ledger actions pause for
  Joe per AGENTS.md.
- **No new mathematics**: the dilation/trace-norm lemma is elementary;
  the broadcast structure is presumed standard (quantum Darwinism,
  collision models — flagged from memory, unverified).
- Hostile review is QUEUED, not survived; nothing here should be cited as
  reviewed.

## Reproduction

```bash
python -m pytest tests/test_capability_restoration_frontier.py -v
python -m models.capability_restoration_frontier
```

Deterministic; ~4 s and ~3 s respectively (budget < 90 s).

## Contribution Needed

- The next rung of the Tier-2 card: a Hamiltonian bath (or
  weak-coupling collision limit) where restoration cost acquires a
  genuine work/entropy scaling with bath contact — the
  continuum/asymptotic bath-dispersion theorem, still named-unbuilt.
- A tighter channel bound (the factor-2 looseness is now measured in
  three artifacts); the certified frontier at weak coupling is currently
  vacuous within `n <= 7`.
- The partial-SWAP stream at intermediate strength: subset-INequivalent
  geometric dispersion (leading contacts carry more record), where the
  frontier becomes subset-shaped rather than size-shaped — named open
  probe beyond the full-SWAP contrast built here.
- The agent-side reading: connect `r(n)` growth to a reach-budgeted agent
  model (CapacityOS-facing; TI-side twin) — pauses for Joe.
- Verify the flagged prior art (collision models, quantum Darwinism,
  Lieb-Robinson adjacency) before anything external-facing; hostile
  review first.
