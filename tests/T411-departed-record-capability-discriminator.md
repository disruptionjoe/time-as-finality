# T411: Departed-Record Capability Discriminator — the Big-Swing Fixture on the Thermal Departure Boundary

## Route

Quantum measurement / repeated-interaction (collision) open systems /
bounded control regions / capability objects. This artifact builds the
program's primary open problem
(`open-problems/region-indexed-capability-discriminator.md`) on top of
T410's departure-carried boundary: **two capability states that are
exactly equal under ALL R-supported statistics — observational AND
under every R-supported intervention — yet separated by one fixed
boundary-crossing task menu**, where the completing datum (dispersal
depth) is not merely undeclared but physically departed (traced-out
thermal carriers), so that every prior absorber's completion move
(T399 enlarged state, T400 hidden datum, T401 joint record, T402
causal domain, T403 finality flag, T405 latch substrate, T406
transition system) is answered by a named, computed control rather
than by prose.

Lineage and standing of the load-bearing neighbors:

- **T409** is cited in its corrected, **internally-established
  re-scoped standing** (hostile review 2026-07-02,
  `audits/2026-07-02-t409-hostile-review.md`,
  survives-with-corrections): a repo-internal calibration of the
  certificate toolkit on a quantum-Darwinism-type collision family.
- **T410** (the thermal collision work–reach frontier, whose model this
  artifact imports as machinery) is **recorded tier only — its hostile
  review is QUEUED, not performed**. Every T410-derived fact used here
  is re-asserted inside this artifact's own suite; nothing is taken on
  T410's authority.

**Hostile review is QUEUED for this artifact, not yet performed.**
Nothing below has survived independent adversarial reproduction.

**Predeclaration trail:** this spec is content-frozen BEFORE
`models/departed_record_capability_discriminator.py` exists. Outcomes
are recorded in the results file and never back-edited here; the
file-creation order (spec -> model -> tests -> results) is recorded in
the results file. Constants imported byte-identical from committed
T392/T393 code and from T410 (working tree, hash recorded in the
results file) are listed below; every T411-specific sweep, threshold,
tolerance, scenario, seed, and failure leg is fixed in this file before
the model file is created. All numeric values quoted in this spec are
**hand-derived closed forms and their corner evaluations**, not run
outputs (no run exists at spec-freeze time).

**T-number:** T411, provisional. Verified free at spec-creation time
(highest taken across `tests/`, `results/`, `TESTS.md`: T410; the only
repo hits for "T411" are T410's own next-free note and a steward run
recommending "a T411-style absorber audit" with numbering explicitly
provisional — no files reserve it). Re-verified at each file creation;
recorded as provisional in the results file per the T397/T404–T408
collision precedent.

## Claim

On T410's switched-Hamiltonian collision substrate — T392's measurement
core (system `S` at prepared phase `phi`; weak meter `M` at
`theta_meter = pi/3`, measured, all verdicts conditional on `M = 0`,
the dominant branch, `P(M = 0) = 7/8` phi-independent; `CNOT S -> REC`
which-way copy), then `m <= 3` broadcast collisions
`REC -> E1_1..E1_m` at `theta = pi` (T410's free-off collision =
exactly `controlled-Ry(pi)`) into fresh Gibbs(`beta`) tier-1 carriers —
two preparations are compared:

- **Capability state A (shallow dispersal):** stop after the
  broadcasts. Tier-1 carriers retained; they hold the which-way
  correlations.
- **Capability state B (deep dispersal):** each `E1_i` additionally
  undergoes one cascade collision with a fresh Gibbs(`beta`) tier-2
  carrier `E2_i`, which then DEPARTS (partial trace — T410's boundary).
  Primary cascade: resonant full SWAP (the record MOVES to tier 2;
  post-cascade the retained state is exactly
  `rho_R (x) tau_beta^{(x) m}`). Contrast cascade (robustness probe):
  `controlled-Ry(pi)` with `E1_i` as control (the record is COPIED
  deeper; the induced channel on `E1_i` is exact Z-dephasing because
  `Tr[Ry(pi) tau] = 0` for every diagonal `tau`).

Declared region `R` = apparatus core `{S, M, REC}` (after the meter is
measured and `M = 0` selected, `M` is pure `|0>` and factorized and is
removed from the density matrix — T410 convention, disclosed; an
intervention on a pure factorized register cannot alter any other
statistic, and the pre-removal `M` state being exactly `|0><0|` is part
of the construction). Boundary-crossing reach `R+` = `R` plus tier-1
`{E1_1..E1_m}`; positive-control reach `R++` = `R+` plus tier-2 (a run
in which tier-2 is retained instead of departing; for state A the
`R++` run appends `m` fresh, never-collided Gibbs carriers so the
register sets match). **Reach = what is physically retained in that
run** (T410's departure convention); the menu at every reach is ALL
CPTP channels supported on the reach with unlimited work ancillas in
any (necessarily phi-independent) state, pure or Gibbs — no menu line
ever forbids touching a co-present register. Task: restore phase-locked
conditional X-visibility `>= v* = 0.9`.

The open problem's own success criterion, quoted:

> No functional of R-supported statistics, including statistics under
> all declared R-supported interventions, separates the two capability
> states; but a boundary-crossing task menu separates them.

The following legs hold jointly (each a predeclared reportable verdict,
pass or fail):

1. **Equality — observational.** `rho_R^A = rho_R^B` exactly:
   post-broadcast operations supported on the environment factors
   cannot move the `R` marginal. Asserted entrywise `< 1e-12` across
   `PHI_CERT` and `PHI_LOCK_GRID`, every `beta` in the sweep, every
   `m`, BOTH cascade variants. (Hand derivation: at `theta = pi` the
   broadcast multiplies the `S`–`REC` coherence block of `rho_R` by
   `f^m = cos(pi/2)^m = 0`, so `rho_R = diag(4/7, 3/7)` on
   `{|00>, |11>}` — phi-independent exactly, identical for A and B.)

2. **Equality — interventional (the bar the T399-era attempts
   missed).** Carried by the **environment-side channel lemma**, stated
   here: B's global retained state is `(id_R (x) Lambda_E)(A's)`, with
   `Lambda_E` acting only on the tier-1 factors (`Lambda_E` =
   per-carrier replacement `Y -> Tr[Y] tau_beta` for the SWAP cascade;
   per-carrier Z-dephasing `Y -> P0 Y P0 + P1 Y P1` for the broadcast
   cascade). For EVERY finite sequence of R-supported CPTP maps,
   instruments, and readouts (with unlimited work ancillas),
   `Lambda_E` commutes with the sequence (disjoint tensor factors) and
   is trace-preserving, so all outcome statistics — including
   per-branch post-measurement continuations — are identical between A
   and B. **The lemma carries the ALL quantifier; the numerics assert
   it on a predeclared family** (and the sampling rows are
   illustrative, never load-bearing):
   - operator-level: `Lambda_E` applied to A's retained `R+` state via
     its abstract Kraus operators (no tier-2 register ever appended —
     an independent construction path) reproduces B's retained `R+`
     state entrywise `< 1e-12`, both variants;
   - 12 predeclared unitary interventions on `R`
     (`X, Y, Z, H` on `S`; `X, Y, Z, H` on `REC`; `CNOT S->REC` — the
     R-supported piece of the un-write attempt; `CNOT REC->S`;
     `CZ(S, REC)`; `SWAP(S, REC)`): post-intervention `R` marginals
     equal `< 1e-12`;
   - 2 predeclared measure-then-act instruments (I1: measure `REC` in
     Z, on outcome 1 apply `X_S`; I2: measure `S` in X, on outcome 1
     apply `Z_REC`): per-branch probabilities and per-branch
     post-instrument `R` marginals equal `< 1e-12`;
   - one predeclared sequential composition (I1, then the first Haar
     unitary, then I2): joint 2x2 outcome distribution and final `R`
     marginals equal `< 1e-12`;
   - 15 seeded Haar unitaries on `(S, REC)` + one work register in
     `|0><0|` (seed `20260704`; illustrative);
   - commutation asserted in action for representative members
     (`X_S`, `CNOT S->REC`, I1 branches):
     `Lambda_E(Phi_R(A)) = Phi_R(Lambda_E(A))` `< 1e-12`;
   - subsequent-readout sufficiency, stated: a later R-statistic
     depends on a conditioned joint state only through its `R`
     marginal (`Tr_E[(Phi (x) id) sigma] = Phi(Tr_E sigma)`), so
     per-branch `R`-marginal equality covers arbitrary continuations.
   Intervention phases `phi in {0, 1.0, 2 pi/3}` (equality is per-phi;
   three phases suffice for the family because every compared object
   is degree-1 trigonometric in `phi`, and the lemma is
   phase-uniform).

3. **Forcing at `R` (the reason boundary crossing is not optional).**
   BOTH states at reach `R` are `final-relative-to-R`, certified
   against ALL channels with unlimited work: the phi-independence
   certificate fires (`< 1e-12`; `rho_R` exactly phi-independent since
   `f = 0`) and the trace-norm bound is `< 1e-12` (the locked mean `X`
   vanishes for a phi-constant family), both invariant under adjoined
   work registers (pure and Gibbs, asserted). The restoration task
   cannot be re-posed inside `R` at any work expenditure — for EITHER
   state — so an agent tasked with restoration must operate beyond
   `R`, and `R -> R+` is exactly where the two states split.
   (Disclosed: T400's compulsion clause — an agent FORCED to attempt —
   is not modeled; forcing here is task-relative and certificate-
   carried.)

4. **Separation at `R+` — one functional, one fixed menu, opposite
   verdicts.** At reach `R+` (everything retained in the B run):
   - **A is `restorable-at-R+`:** the un-write protocol
     (`controlled-Ry(-pi) REC -> E1_i` per carrier, then
     `CNOT S -> REC`) is an exact unitary undo for arbitrary diagonal
     carrier initial states; achieved `= vis_A = 4 sqrt(3)/7 =
     0.989743 >= v*` at every `beta` and `m` (`< 1e-9`).
   - **B is `final-relative-to-R+`:** for the SWAP cascade the
     retained state is exactly `rho_R (x) tau_beta^{(x) m}` (asserted
     `< 1e-12`), hence exactly phi-independent — the STRONG
     certificate: NO channel on `R+`, with unlimited work ancillas
     pure or Gibbs, produces phi-locked output (certificate
     `< 1e-12`; dilation invariance asserted). The same un-write that
     restores A returns locked visibility `< 1e-12` on B.
   - **Contrast cascade (broadcast):** hand derivation predicts the
     retained coherence block is `diag(Ry(pi) tau_blk) = 0`, so the
     phi-independence certificate fires (`< 1e-12`) at every `beta`
     here too. Predeclared fallback if the derivation is wrong: if
     `cert >= 1e-12`, the verdict falls to the trace-norm bound
     (`final-relative-to-R+` iff bound `< v*`); if the bound is also
     `>= v*`, the cell is reported `undetermined_by_bound` — reported,
     not narrated around (that fires `separation_not_certified_B` for
     the contrast row only).
   - A's record trace at `R+` is REQUIRED by T408's menu-support
     obstruction lemma (a capability gap needs a statistical trace
     within the separating menu's support): A's `R+` phi-certificate
     is predeclared `> 0.05` (hand value: entrywise coherence
     magnitude `>= ab/2^m = 0.0619` at `beta = 0, m = 3`, times the
     max grid phase separation `sqrt(3)` gives `~ 0.107`). The flat
     surface (`R`) is exactly the complement of the separating menu's
     support.

5. **Physical boundary + positive control, priced.** The completing
   datum (dispersal depth) lives in DEPARTED tier-2 carriers; at fixed
   `R+` its B-side trace is exactly zero (leg 4's product state).
   Positive control: at `R++` (tier-2 retained in that run), B is
   `restorable-at-R++` — un-SWAP (or inverse cascade) then un-write,
   achieved `= vis_A` (`< 1e-9`) at every `beta` and `m`; A remains
   restorable at `R++` (fresh uncollided tier-2 appended so register
   sets match). Region enlargement restores capability — the open
   problem's demanded positive control — and the relocation is PRICED
   in the T410 ledger conventions (omega-units, nats; bookkeeping, not
   a theorem):
   - cascade switching work `W_casc = 0` exactly for the resonant
     SWAP (`< 1e-12`; SWAP commutes with `H_E1 + H_E2` at resonance);
   - cascade heat into the departing tier
     `Q_casc = (3/7) tanh(beta/2)` per carrier (`< 1e-9`; `3/7` at
     `beta = inf`, `0` at `beta = 0`);
   - cascade entropy production `Sigma_casc = Delta S_complex +
     beta Q`, asserted against the exact identity
     `I(complex : E2)_after + D(rho_E2' || tau_beta)` both ways
     `< 1e-10` at finite `beta`, `>= -1e-10` everywhere, typed `inf`
     at `beta = inf` with `Q > 0` (extended-real bookkeeping,
     disclosed, not asserted);
   - **the `beta = 0` corner, predeclared as expected and NOT spun as
     entropy pricing:** `W_casc = 0`, `Q_casc = 0`, yet
     `Sigma_casc(total, m = 1) = H(3/7) = 0.682908` nats — exactly
     the mutual information `I(R : E1)` carried away by the departing
     tier (the identity's `I` term with `D = 0`): the ledger books
     the record's departure as entropy production even with zero work
     and zero heat flow;
   - restoration work at `R++`: un-SWAP work `= 0` (`< 1e-12`);
     un-write work `= -m w_fwd(pi, beta) - 3/7` — T410's refund law,
     asserted cross-module against `w_rest_analytic` (`< 1e-9`).
   Honest scope, conceded up front: departure-by-trace is the standard
   reservoir idealization — **adopted, not derived** — so boundary
   physicality is conditional on the model class (T410's concession,
   inherited verbatim); the unconditional version (spatial transport,
   work literally buying reach) stays **named-unbuilt**.

6. **`beta = 0` marginal blindness (the sharpest tooth).** At
   `beta = 0`: EVERY proper-subset marginal of the retained `R+`
   register set is identical between A and B (`< 1e-12`, all
   `2^(2+m) - 2` proper subsets enumerated for every `m <= 3`) — every
   single register, every pair, every subset short of the full joint;
   "which registers hold the discriminating datum" has no answer short
   of everything — while the FULL joint states differ by trace
   distance exactly `vis_A / 2 = 0.494872` (`< 1e-9`, every `m`; hand
   derivation: `A - B` decomposes into `2^m` disjoint rank-2
   off-diagonal blocks of trace norm `2 ab / 2^m` each). At
   `beta = inf` the single-carrier marginals DO distinguish A from B —
   entrywise difference exactly `(3/7) tanh(beta/2) = 3/7` (`< 1e-9`;
   general-`beta` closed form asserted across the sweep) — and the
   full-joint trace distance is `(3 + sqrt(57))/14 = 0.753560`
   (`< 1e-9`, every `m`): the LOCAL trace of dispersal depth fades to
   exactly zero as `beta -> 0` while both capability verdicts and both
   equality certificates are `beta`-blind. Also predeclared: at
   `beta = 0` the two cascade variants produce IDENTICAL retained
   states (`< 1e-12`; both `rho_R (x) (I/2)^{(x) m}`). Mutual
   information closed forms (bits, `< 1e-9`): `I_A(R : E1-block) =
   2 h2(3/7) = 1.970457` at `beta = inf` and `= h2(3/7) = 0.985228`
   at `beta = 0` (every `m`); `I_B = 0` exactly (SWAP cascade, every
   `beta`); `I_B = h2(3/7)` at `beta = inf` and `0` at `beta = 0`
   (broadcast cascade — the classical which-way record is RETAINED
   there, and the capability verdict is final anyway; see leg 7).

7. **Absorber-control battery (named, computed controls — the
   T397–T406 graveyard answered leg by leg).**
   - **T399 (enlarged-state completion):** the positive control IS the
     leg — enlargement restores, and it is priced (leg 5). The claim
     is never "the reviewer cannot compute"; it is that at FIXED `R+`
     — full access to everything retained in the run — the split is
     sourced in dispersal depth whose B-side trace is exactly zero.
     Against boundary relocation: B is final relative to EVERYTHING
     retained in its run; there is no larger retained reach to
     relocate to (the `R++` run is a different, counterfactual
     retention, run as the priced positive control).
   - **T400 (hidden datum / stipulated label):** contrast control —
     two copies of the SAME physical preparation carrying different
     stipulated classical flags produce bit-identical states
     (asserted `== 0.0`) and hence identical capability verdicts: a
     stipulated label alone moves nothing here, while in T411 every
     declared field is matched and the capability still splits. The
     task functional (locked visibility `>= v*`) reads no label. The
     compulsion clause of T400's gate is disclosed as not modeled.
   - **T401 (joint-record completion):** granting the COMPLETE
     retained joint state at `R+` gives, for B (SWAP), a product state
     — mutual information exactly 0; the completion is exhausted and
     returns nothing; completing further requires the departed tier,
     i.e. the open-system premise itself. Sharper, via the broadcast
     contrast: there the joint-record completion DOES return the
     which-way datum (classical correlations, `h2(3/7)` bits at
     `beta = inf`) and the capability verdict is STILL
     final-relative-to-`R+`, certified — the record datum and the
     capability are transverse; joint-record completion cannot absorb
     the split.
   - **T402/T403/T405/T406 (causal-domain / finality-flag / latch /
     transition-system completion):** matched-declared-fields control:
     registers per reach, Hamiltonians, gate set, menu, task,
     threshold, phase grids, conditioning, collision window, and
     carrier initial states are asserted EQUAL between A and B as
     declared data; the ONLY differing item is the physical cascade
     history, which carries an energy/entropy ledger entry (leg 5),
     not a bookkeeping entry. Operation unavailability (restoration
     infeasibility) is DERIVED by one verdict functional applied to
     the physical retained state — same code path for A and B, no
     per-state flag, latch field, or transition relation consulted;
     swapping the input states swaps the verdicts (asserted).
   - **T398/T404 (resource projection):** run the projection on
     itself — the per-reach capability profiles
     `C(A) = (final@R, restorable@R+)` and
     `C(B) = (final@R, final@R+, restorable@R++)` are admitted as
     resource objects, and their order content absorbs exactly as
     T398 showed (ordinary non-total convertibility; conceded). The
     claimed residues sit at the frame's interface, inheriting T404's
     standing AND its predeclared conditional demotion clause,
     disclosed verbatim: (a) causal indexing — work, the athermality
     frame's own currency, is certified unable to purchase what reach
     purchases (dilation-invariant certificates with pure and Gibbs
     work registers; candidate absorbers: dynamical resource theories
     / superchannels — named, from memory, unverified); (b) the
     `beta = 0` locally-hidden sharpening (leg 6; candidate absorber:
     Blackwell comparison of experiments — named, from memory,
     unverified). If either candidate verifies as absorbing, the
     corresponding residue demotes per T404's clause.
   - **T397 (class-marker algebra) / SBS closure key:** no class
     markers and no closure key exist in the fixture — the task is a
     threshold on a computed functional of the post-protocol state,
     not a readout of any label; stated, with the T400 flag control
     as the numeric witness.
   - **Lieb-Robinson:** no geometry exists (all-to-one contact
     graph); the boundary is a departure boundary, **not a light
     cone** (Lieb-Robinson named as an absorber risk, from memory,
     unverified).

8. **Guardrails.** Q1D asserted numerically: declared `(S, M)` record
   (unconditioned Z-distribution) invariant across `beta`, `m`,
   variant, and cascade (`< 1e-12`; broadcasts and cascades never
   touch `S` or `M`); every R-supported intervention in the leg-2
   family moves every tier-1 marginal by `< 1e-12` (no signalling out
   of `R`); the counterfactual `R+` un-write moves the tier-1
   marginals by exactly `(3/7) tanh(beta/2)` (`< 1e-9`; `3/7` at
   `beta = inf`, `0` at `beta = 0`, where the tooth is instead the
   restored-visibility jump `0 -> vis_A` — leg 6's marginal blindness,
   disclosed). **R1 untouched**: no claim about global temporal order
   or spacetime.

## Class

**Exploratory, capability-object lineage; the primary open problem's
big-swing fixture, built at its finite thermal-collision form.** NOT
registered in CLAIM-LEDGER. Lineage: T392 (measurement core, `v*`,
gameability lemma), T393 (certificates), T408 (operator-level flatness
discipline; menu-support obstruction lemma), T409 (frontier object;
re-scoped internally-established standing), T410 (departure boundary,
thermal substrate, ledger — recorded tier, hostile review queued),
T397–T406 (the absorber ladder this fixture must answer). Whether this
artifact discharges or advances the open problem is a promotion
decision that pauses for Joe per AGENTS.md. Hostile review QUEUED for
this artifact.

## Status

Predeclared. This spec is frozen before the model file exists; the
model, tests, and results follow it. Outcomes (including any fired
failure leg) are recorded in the results file, not back-edited here.

## Target Claims

- [Open problem: Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
  (the success criterion is quoted in-claim; each demanded fixture
  ingredient is mapped to a leg by number in the results file)
- [T410: Thermal Collision Work–Reach Frontier](T410-thermal-collision-work-reach-frontier.md)
  (substrate and machinery — imported, and re-asserted here; recorded
  tier)
- [T409: Capability Restoration Frontier](T409-capability-restoration-frontier.md)
  (frontier object; re-scoped standing)
- [T408: Basis-Free Flat Pair and the Physical Capability Boundary](T408-basis-free-capability-boundary.md)
  (menu-support obstruction lemma, used as a consistency requirement in
  leg 4)
- [T393: Causal Forcing of the Access Asymmetry](T393-causal-forcing-of-access-asymmetry.md)
  (both certificates)
- [T392: Fixed-SBS-Key Reversal Divergence Witness](T392-fixed-sbs-key-reversal-divergence-witness.md)
  (measurement core, `v*`, locked figure of merit — imported unchanged)
- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md) (guardrail, asserted numerically)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md) (guardrail; untouched)

## Definitions (fixture, reaches, menu, task)

**Registers and preparation.** T392 core on `(S, M, REC)`; `M`
measured, `M = 0` selected (`P(M = 0) = 7/8`, phi-independent), `M`
removed (pure, factorized). Broadcasts: `m <= 3` collisions
`REC -> E1_i` using T410's `collision_u(pi, free_off)` = exactly
`controlled-Ry(pi)`; fresh carriers in `tau_beta` (T410's
`tau_gibbs`). State A stops. State B cascades each `E1_i` with a fresh
`E2_i` (SWAP primary / `controlled-Ry(pi)` with `E1_i` control as
contrast), then `E2_i` departs unless the run is `R++`. Retained
register order: `S, REC, E1_1..E1_m` (`R+`/`R` runs) or
`S, REC, E1_1..E1_m, E2_1..E2_m` (`R++` runs). Exact density-matrix
evolution throughout (T410 machinery; no Trotter error).

**Reaches (departure convention).** `R` run: all tiers depart after
their last collision; retained = `(S, REC)`. `R+` run: tier-1
retained, tier-2 departs; retained = `(S, REC, E1_*)`. `R++` run:
nothing departs (A appends `m` fresh uncollided carriers so the
declared register sets match). Reach IS the retained set; declared
once, identical across preparations, variants, and phases.

**Menu.** ALL CPTP channels supported on the reach, with unlimited
work ancillas in any (necessarily phi-independent) state — pure or
Gibbs; dilation lemma asserted numerically for both. Identical menu
object at every reach; no menu line references the A/B identity.

**Task and figure of merit.** Restore phase-locked conditional
X-visibility `|mean_phi e^{i phi} 2 rho_S[0,1]|` over `PHI_LOCK_GRID`
to `>= v* = 0.9` (T392, imported unchanged; the uniform grid exactly
nulls manufactured phi-independent coherence). Zero-loss restorable
value `vis_A = 4 sqrt(3)/7 = 0.989743`.

**Verdict functional (one code path, both states).** Given a retained
family `{rho(phi)}` and the reach's declared protocol (un-write at
`R+`; inverse-cascade-then-un-write at `R++`; identity at `R`):
`restorable-at-<reach>` iff achieved `>= v*`;
else `final-relative-to-<reach>` iff the phi-independence certificate
`< 1e-12` OR the trace-norm bound `< v*`;
else `undetermined_by_bound` (reported).

**Capability states.** The compared objects are the two preparations
A and B as capability states in the open problem's sense: the pair
(reach-indexed retained state family, fixed menu, fixed task). The
discriminator claim is region-relative to the declared `R`.

## Setup

`models/departed_record_capability_discriminator.py`; imports T410's
machinery by name (`collision_u`, `tau_gibbs`, `core_conditioned`,
`core_full_dm`, `dm_apply`, `dm_kraus`, `dm_ptrace`, `dm_append`,
`dm_expect`, `embed_unitary`, entropy/trace-distance helpers,
`w_fwd_analytic`, `w_rest_analytic`, tolerances, `VIS_A_ANALYTIC`,
`BRANCH1_WEIGHT`, `H2_3_7`, `_json_safe`), T392's `THETA` (meter) and
`V_STAR` and `_HADAMARD`, T393's `PHI_CERT`, `PHI_LOCK_GRID`,
`_trace_norm`, `haar_unitary`. numpy + scipy stack unchanged;
deterministic; the only sampling (Haar, 15 samples, seed `20260704`)
is illustrative and never carries an impossibility or equality
verdict. Peak retained dimension `2^8 = 256` (`R++` run at `m = 3`).
pytest from repo root; neighbor suites (T392, T393, T408, T409, T410,
T142) re-run green alongside, combined counts reported.

## Predeclared constants, sweeps, tolerances (fixed here, before the model)

- Imported unchanged and cited: `theta_meter = pi/3`, `v* = 0.9`,
  `PHI_CERT = (0, 1.0, sqrt(2), pi/3, 2 pi/3, pi/7)`, `PHI_LOCK_GRID`
  = 8 uniform points, `vis_A = 4 sqrt(3)/7`, `M = 0` conditioning,
  `FLATNESS_TOL = 1e-12`, `ANALYTIC_TOL = 1e-9`,
  `IDENTITY_TOL = 1e-10`, T410 collision/ledger machinery. Changing
  any of these after seeing numbers is a listed failure criterion.
- Fixture constants: `m in {1, 2, 3}`; `beta in {inf, 1.0, 0.0}`
  (subset of T410's sweep; both corners exact); broadcast
  `theta = pi` fixed; cascade primary = resonant full SWAP, contrast
  = `controlled-Ry(pi)` (E1 control); reaches `R`, `R+`, `R++` as
  defined, declared once.
- Intervention family (leg 2): the 12 unitaries, 2 instruments, 1
  sequential composition, and 15 Haar samples listed in-claim, at
  `phi in {0, 1.0, 2 pi/3}`; Haar seed `20260704`, work register
  `|0><0|`; the LEMMA carries the ALL quantifier, sampling never does.
- Proper-subset enumeration (leg 6): all `2^(2+m) - 2` proper subsets
  of the retained `R+` register set, every `m <= 3`, `beta = 0`, both
  variants ("exhaustive" is used for these literal enumerations only).
- Ledger scenarios (leg 5): cascade ledger at every
  `(m, beta)` in the sweep, SWAP variant closed-form-gated, broadcast
  variant identity-gated only (its `W, Q` reported as computed);
  restoration work at `R++` for both variants.
- Tolerances: certificates/equalities/invariances `< 1e-12`
  (`FLATNESS_TOL`); closed forms and predeclared corner values
  `< 1e-9` (`ANALYTIC_TOL`); Sigma identity both ways and balance
  `< 1e-10` (`IDENTITY_TOL`); `Sigma >= -1e-10`; A's `R+` record
  trace `> 0.05`; values at or below `1e-13` reported as "< 1e-13
  (machine floor)", never as bolded run digits.
- Runtime budgets, predeclared: model run `< 300 s`, T411 test suite
  `< 300 s` (report actuals against budgets). If busted: fall back to
  `m <= 2` and report the reduction — never silently.

## Verified exactly (assertions the suite makes)

1. Construction anchors: A's `R+` state == T410's
   `prepare_retained(n = m, all retained, theta = pi, free off)`
   cross-module `< 1e-12`; A's `R` state == T410's zero-retention
   state `< 1e-12`; B(SWAP)'s `R+` state == `rho_R (x) tau^(x) m`
   `< 1e-12`; B(broadcast) == B(SWAP) at `beta = 0` `< 1e-12`;
   `P(M = 0) = 7/8` phi-independent `< 1e-12`.
2. Leg 1: worst `rho_R^A - rho_R^B` entrywise diff `< 1e-12` over
   {both variants} x {m} x {beta} x {PHI_CERT + PHI_LOCK_GRID}.
3. Leg 2: abstract-Kraus lemma reproduction `< 1e-12` (both
   variants); all 12 unitary interventions `< 1e-12`; both
   instruments per-branch `< 1e-12` (probabilities and states); the
   sequential composition `< 1e-12`; 15 Haar rows `< 1e-12`
   (illustrative); commutation-in-action rows `< 1e-12`.
4. Leg 3: `R`-level phi certificate and trace-norm bound `< 1e-12`
   for both states; work-dilation invariance (pure + Gibbs)
   `< 1e-12`.
5. Leg 4: A achieved `= vis_A` `< 1e-9` (every `beta`, `m`);
   B(SWAP) cert `< 1e-12`, un-write on B `< 1e-12`, dilation
   invariance `< 1e-12`; B(broadcast) cert `< 1e-12` (or the
   predeclared fallback path, reported); A's `R+` cert `> 0.05`;
   verdicts `restorable-at-R+` / `final-relative-to-R+` from the one
   shared functional.
6. Leg 5: B `R++` achieved `= vis_A` `< 1e-9` (both variants);
   `W_casc(SWAP)` `< 1e-12`; `Q_casc = (3/7) tanh(beta/2)` `< 1e-9`;
   Sigma identity both ways `< 1e-10` (finite beta),
   `Sigma >= -1e-10`, typed `inf` at `beta = inf`;
   `Sigma_casc(total, m = 1, beta = 0) = 0.682908` nats `< 1e-9` and
   equal to the departed `I(R : E1)` `< 1e-10`; un-SWAP work
   `< 1e-12`; un-write work vs `w_rest_analytic` `< 1e-9`.
7. Leg 6: all proper-subset marginals at `beta = 0` `< 1e-12`; full
   joint TD `= vis_A/2 = 0.494872` `< 1e-9` (every `m`); TD at
   `beta = inf` `= (3 + sqrt(57))/14 = 0.753560` `< 1e-9`; carrier
   marginal diff `= (3/7) tanh(beta/2)` `< 1e-9`; `I_A`, `I_B` closed
   forms `< 1e-9`; `I_B(SWAP) < 1e-12`.
8. Leg 7: flag-control states bit-identical (`== 0.0`) with identical
   verdict outputs; matched-declared-fields dicts equal; verdict
   functional swaps with its input; resource-projection profiles as
   stated with both residue disclosures present; Lieb-Robinson /
   not-a-light-cone strings present.
9. Leg 8 (Q1D): record invariance `< 1e-12`; no-signal-out `< 1e-12`
   (max over the full leg-2 family); teeth `= (3/7) tanh(beta/2)`
   `< 1e-9`; `beta = 0` tooth carried by the visibility jump; R1 note
   contains "not a light cone" and "Lieb-Robinson".
10. Discipline: determinism (bit-identical repeat); register layout;
    verdict tags tuple ends `no_claim_promotion`; verdict language
    contains "pause for Joe", "no claim promotion", "named-unbuilt",
    "adopted, not derived"; the open problem's success-criterion
    sentence present in the model's report.

## Success Criteria

- All eight legs hold as predeclared; every equality and every
  impossibility verdict is carried by an exact operator-level fact or
  an all-channel certificate (never by sampling); the two capability
  states realize the open problem's success criterion at the declared
  `R`, with the boundary-crossing menu `R -> R+` separating them and
  the forcing certificate closing the `R`-interior.
- The positive control restores at `R++` and its price is tabulated in
  the T410 ledger conventions.
- Every absorber control in leg 7 reports its named outcome, including
  the two conceded absorptions (T398-style order content; T399-style
  enlargement) and the two conditional residues with their demotion
  clauses.

## Failure Criteria (predeclared reportable verdicts — findings, not patches)

- **`equality_fails`** (HALTING): any leg-1/leg-2 comparison
  `>= 1e-12` — the fixture's equality clause is dead; report exactly
  which certificate failed and stop; NO discriminator claim.
- **`separation_fails_A`**: A's un-write at `R+` restores `< v*`.
  Fires -> reported; the fixture exhibits equality without
  separation (an absorption-grade negative result).
- **`separation_not_certified_B`**: B's `R+` family fails the
  phi-independence certificate (`>= 1e-12`) AND the trace-norm bound
  (`>= v*`). The cell is reported `undetermined_by_bound`; no
  final-relative-to-`R+` verdict is claimed for that variant; if this
  happens for the PRIMARY (SWAP) cascade the discriminator claim is
  withdrawn and the artifact reports the obstruction.
- **`positive_control_fails`** (HALTING): B not restorable at `R++`
  (`< v*`) — a construction defect (the cascade inverse exists by
  construction); halt and report.
- **`marginal_blindness_fails`**: any `beta = 0` proper-subset
  marginal distinguishes A from B (`>= 1e-12`). Fires -> leg 6
  reported failed; the "no answer short of everything" sharpening is
  withdrawn (the discriminator's other legs stand or fall on their
  own numbers).
- **`separator_factors_through_declared_field`**: the matched
  declared-fields dicts differ anywhere other than the disclosed
  physical cascade history, OR the flag control shows a stipulated
  label moving the capability functional. Fires -> the fixture is
  absorbed T403/T405/T406-style; reported as the finding.
- **`boundary_physicality_reduces_to_declaration`** (the honest
  leg): fires if any separation or forcing verdict fails to be
  carried by an all-channel certificate computed on the physically
  retained state — i.e. if a verdict would need a declared menu
  restriction on a co-present register or a protocol-failure-only
  argument. Fires -> "separation exists but boundary physicality
  reduces to declaration — absorbed" is the reported verdict.
  Independently of firing: the CONDITIONALITY of departure-by-trace
  (reservoir idealization adopted, not derived) is conceded in the
  verdict language in all outcomes; this leg polices the stronger,
  in-model failure mode.
- Any tuning of `v*`, the phase grids, the sweeps, the intervention
  family, seeds, or tolerances after inspecting values; any recovery
  measured by raw visibility (the T392 exploit; the locked grid is
  load-bearing); departed carriers quietly re-appended to any
  admissible protocol; reach adjusted per preparation or per phase.
- **Re-scope clause (verbatim, predeclared):** if the assembled object
  is standard (environment-assisted recovery / quantum Darwinism /
  data processing on a dilation), the artifact re-scopes to a
  repo-internal calibration of the certificate toolkit.

## Neighbors / Prior Art

In-repo: the absorber ladder T397–T406 (each answered by a named leg-7
control); T407 (C(R) lineage; its declared-vs-physical standing
objection is inherited through T410's conditional answer and NOT
claimed discharged unconditionally); T408 (menu-support obstruction
lemma — used as a consistency REQUIREMENT here: the capability gap at
`R+` must and does leave a statistical trace at `R+`); T409 (re-scoped
standing); T410 (substrate; recorded tier).

Candidate prior art (ALL from memory — flagged, unverified, per the
no-fake-citations rule; named as absorber risks for the queued hostile
review):

- **Environment-assisted recovery (Gregoratti–Werner lineage)** — that
  a unitarily dilated channel is correctable given the environment is
  presumed standard; A's restorability at `R+` and B's at `R++` are
  instances, not claims.
- **Quantum Darwinism, incl. mixed/hazy environments
  (Zurek; Zwolak–Quan–Zurek)** — record proliferation and
  finite-temperature record suppression are their territory.
- **Petz / approximate recovery maps** — the sufficiency side of
  recovery is worked territory; no Petz result is used or claimed.
- **No-hiding-theorem lineage (Braunstein–Pati)** — the `beta = 0`
  corner (the datum in no proper subsystem) is presumed adjacent in
  mechanism; flagged, not cited as support.
- **Blackwell comparison of experiments; dynamical resource theories /
  superchannels** — the two T404-interface residues' named candidate
  absorbers, inherited with T404's conditional demotion clause.
- **Lieb-Robinson bounds** — no geometry, no locality bound; a
  departure boundary, not a light cone.

The claimed residue, if the legs hold: the ASSEMBLED object — exact
observational AND interventional `R`-equality (lemma-carried, all
channels, all work), opposite certified capability verdicts under one
fixed boundary-crossing menu, forcing closed inside `R`, the departed
completing datum with zero retained trace (product state), the priced
positive control, and the `beta = 0` no-proper-subset sharpening —
under the T397–T406 control battery. If verification shows even the
assembly is standard, the re-scope clause fires.

## Honest Reviewer Attack Surface

- **"This is T399 again: equal marginals, joint separator."** The
  differences are predeclared as legs: (i) equality here is
  interventional, lemma-carried against ALL R-supported sequences,
  not just observational marginals; (ii) crossing is FORCED (the task
  is certified impossible inside `R` for both states, all channels,
  unlimited work — not an optional readout); (iii) at the fixed
  crossing reach `R+`, BOTH runs grant full access to everything
  retained — the split is carried by what departed, and B's retained
  state is an exact product (nothing to complete with); (iv) the
  positive control is priced. If a reviewer judges these insufficient,
  the demotion criteria of the open problem apply as written.
- **"Departure is declared bookkeeping too — you chose to trace."**
  Inherited from T410 and conceded identically: the reservoir
  idealization is ADOPTED, not derived; the claim is conditional on
  the model class, the verdict language says so, and the
  unconditional version (transport; work buying reach) is
  named-unbuilt. What the fixture adds over a declaration: within the
  model class the inaccessibility is carried by the state space
  itself, the completing datum has exactly zero retained trace, and
  the honest failure leg above polices any regression to
  menu-restriction reasoning.
- **"The two states differ at R+ — so statistics DO separate them."**
  Yes, at `R+` — that is the separation, and T408's obstruction lemma
  REQUIRES it (a capability gap with no statistical trace inside the
  separating menu's support is impossible). The equality claim is
  indexed to `R`, exactly as the open problem demands.
- **"A and B have different preparation circuits — the completion is
  the circuit description."** The circuit difference is physical
  (cascade collisions with real carriers, a real ledger entry) and
  its retained trace at `R+` is exactly zero for the SWAP cascade;
  granting the full retained quantum state — the strongest
  completion available at the boundary — returns a product. The
  reviewer who grants the DEPARTED registers has granted `R++`,
  which is the priced positive control, not a refutation.
- **"The broadcast contrast retains a classical record — surely that
  can be completed into the separator."** It can be completed into
  the RECORD; it cannot be completed into the CAPABILITY — the
  verdict is final-relative-to-`R+`, certified all-channel. That
  transversality is the point of the contrast row.
- **"Three intervention phases are too few."** Every compared object
  is degree-1 trigonometric in `phi` (single phase gate), the same
  structure T409/T410 assert; and the lemma is phase-uniform. The
  equality numerics are a check on an operator identity, not a
  statistical sample.

## Known Physics Constraints

- No-cloning respected; the meter statistics are phi-independent, so
  conditioning introduces no phase information.
- The impossibility side quantifies over all CPTP maps on the reach
  via the phi-independence certificate (degree-1 structure) and the
  trace-norm bound; work ancillas covered by the dilation lemma in
  any (necessarily phi-independent) state, asserted for pure and
  Gibbs sigma.
- The equality side quantifies over all R-supported intervention
  sequences via the environment-side channel lemma (disjoint tensor
  factors + trace preservation); the numerics assert the lemma's
  operator-level content and a predeclared operational family.
- Exact density-matrix evolution; entropy-production nonnegativity is
  structural for fresh Gibbs carriers (asserted as computed); at
  `beta = inf` the divergence is typed, not asserted.

## What This Does Not Earn

- **No unconditional physical-boundary claim**: departure-by-trace is
  the standard reservoir idealization, adopted, not derived (T407's
  standing objection remains open at the unconditional level); the
  transport/continuum rung stays **named-unbuilt**.
- **No resolution of the open problem by itself**: whether this
  fixture discharges the discriminator burden is a review + promotion
  decision that pauses for Joe; the T398-style order-content
  absorption and T399-style enlargement absorption are CONCEDED in
  leg 7, and two residues carry conditional demotion clauses.
- **No thermodynamic theorem** (the leg-5 ledger is
  exact-identity-backed bookkeeping at the computed states;
  finite-witness per COMPLEXITY-LEDGER vocabulary).
- **No new mathematics or new physics**: every assembled physical fact
  is presumed standard (flagged above, from memory, unverified); the
  claimed residue is the assembled, certificate-disciplined object.
- **No hardware, platform, or experimental claim.**
- **No claim promotion, no CLAIM-LEDGER entry**; ledger actions pause
  for Joe per AGENTS.md. Hostile review is QUEUED, not survived.

## Reproduction

```bash
python -m pytest tests/test_departed_record_capability_discriminator.py -v
python -m models.departed_record_capability_discriminator
```

Deterministic; predeclared budgets `< 300 s` each (actuals reported in
the results file).

## Contribution Needed

- The transport rung (carriers that MOVE; reach with geometry; work
  literally buying reach) — the unconditional physical boundary,
  still unbuilt.
- Verification of the flagged prior art (environment-assisted
  recovery; hazy-environment Darwinism; no-hiding; Blackwell;
  dynamical resource theories) before anything external-facing;
  hostile review first — including the two conditional-demotion
  residues.
- A forced-task COMPULSION gate (T400's remaining clause): an agent
  model that must attempt restoration, so "forced" is carried by the
  agent dynamics rather than by task-relative certificates.
- The continuum/weak-coupling analogue of both certificates (exact
  phi-independence will not survive discretization removal).
