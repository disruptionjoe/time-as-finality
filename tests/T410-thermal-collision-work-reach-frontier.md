# T410: Thermal Collision Work–Reach Frontier — the Hamiltonian-Bath Rung of the Restoration Frontier

## Route

Quantum measurement / repeated-interaction (collision) open systems /
bounded control regions / capability objects. This artifact builds the
rung that T393 named, T408 re-named, and T409 left as its explicit
next step: **the genuine open-system bound — a Hamiltonian bath, a real
work parameter, temperature, and entropy production, so that
"restoration cost" acquires computable work/entropy scaling with bath
contact.** T409's hostile review (2026-07-02,
`audits/2026-07-02-t409-hostile-review.md`; aggregate verdict
survives-with-corrections; T409 now **internally established in its
re-scoped standing** — a repo-internal calibration of the certificate
toolkit on a quantum-Darwinism-type collision family, with the
"Tier-2 forcing earned" and "boundary made physical" framing withdrawn)
identified exactly two gaps this artifact addresses head-on:

1. T409's reach was a **declared, graded bookkeeping boundary** —
   nothing dynamical prevented access to the "unreached" bath qubits.
   Here the boundary is **departure**: each bath ancilla is a fresh
   Gibbs-state carrier that collides once and then leaves the model
   (partial trace) unless it is physically retained. Reach IS the
   retained register set. No menu line ever forbids touching a
   co-present register. (Conceded up front: departure-by-trace is the
   standard reservoir idealization — ancillas never return — which is
   **adopted, not derived**; see Honest Reviewer Attack Surface.)
2. T409's "work does not substitute for reach" failure leg was
   **mathematically unfireable** (predeclaration theater, per the
   review). Here work is a genuine, computed, omega-unit quantity with
   a temperature axis, and the work-substitution failure leg is
   **fireable in the predeclared undetermined-band cells** (and only
   there — in certified cells it remains excluded by the bound, which
   is disclosed rather than dressed up as an open experiment).

**Hostile review is QUEUED for this artifact, not yet performed.**
Nothing below has survived independent adversarial reproduction.
T409 is cited throughout in its corrected, re-scoped standing only.

**Predeclaration trail:** this spec is content-frozen BEFORE
`models/thermal_collision_work_reach_frontier.py` exists. Outcomes are
recorded in the results file and never back-edited here; the
file-creation order (spec -> model -> tests -> results) is recorded in
the results file. Constants imported byte-identical from committed
T392/T393/T142 code are auditably prior; every T410-specific sweep,
threshold, tolerance, scenario, seed, and failure leg is fixed in this
file before the model file is created. All numeric values quoted in
this spec are **hand-derived closed forms and their corner
evaluations**, not run outputs (no run exists at spec-freeze time).

**T-number:** T410, provisional. Verified free at spec-creation time
(highest taken across `tests/`, `results/`, `TESTS.md`: T409; repo-wide
grep for T410–T499: no hits). Re-verified at file creation; recorded as
provisional in the results file per the T397/T404–T408 collision
precedent.

## Claim

In a finite repeated-interaction model — T392's measurement core
(system `S` at prepared phase `phi`, weak meter `M` at
`theta_meter = pi/3`, measured, all verdicts conditional on `M = 0`,
the dominant branch; `CNOT S -> REC` which-way copy), followed by
`n <= 5` switched-Hamiltonian collisions of the record qubit `REC` with
fresh Gibbs(`beta`) bath ancillas, each ancilla **departing** (traced
out) after its collision unless retained — the capability-restoration
frontier of T409 acquires genuine thermodynamic bookkeeping, and the
following legs hold jointly (each a predeclared reportable verdict,
pass or fail):

1. **First law + entropy production (exact-identity-backed at the
   computed states).** Per collision, with the switching work
   convention (interaction on/off at window endpoints),
   `W_i = Delta<H_REC> + Delta<H_Bi>` and the interior evolution is
   autonomous (`Tr[H_window (U rho U^dag - rho)] = 0` to `< 1e-12`;
   equivalently `W_i = -Delta<H_int>` — the two conventions coincide
   because H_int is off at both endpoints, reported side by side).
   Entropy production `Sigma_i = Delta S_complex + beta Q_i` (nats,
   `Q_i = Delta<H_Bi>`) equals `I(complex : B_i)_after +
   D(rho_Bi' || tau_beta)` — the exact repeated-interaction identity
   (flagged prior art, from memory, unverified: Esposito–Lindenberg–
   Van den Broeck 2010) — asserted BOTH ways `< 1e-10` at every finite
   `beta` in the sweep, `Sigma_i >= -1e-10` everywhere, cumulative
   `Sigma` non-decreasing in contact count. At `beta = inf` with
   `Q_i > 0`, `Sigma_i` is typed `inf` (zero-temperature limit;
   `D(rho' || pure)` divergent) — extended-real bookkeeping, disclosed,
   not numerically asserted. Global energy balance over core + stream +
   restoration, counting appended and departed carrier energies at
   their boundary values, telescopes to `< 1e-10`.

2. **T409 regression corner — zero translation loss.** At
   `(beta = inf, free terms off, theta = pi)` the collision unitary is
   EXACTLY `controlled-Ry(theta)` (`< 1e-12`) and the model reproduces
   T409's frontier block for `n <= 5`: `r_feas = r_cert = n`, every
   insufficient retained reach with phi-independence certificate
   `< 1e-12` and channel bound `< 1e-12`, full reach restoring
   `vis_A = 4 sqrt(3)/7 = 0.989743` to `< 1e-9`; cross-module
   comparison against T409's own `frontier_row` at the predeclared
   cells (`n in {1, 3, 5}`, all reach sizes, `theta in {0.5 pi, pi}`):
   achieved and bound agree `< 1e-9`.

3. **Temperature-blind frontier (free terms off).** The branch-overlap
   law: tracing a departed carrier multiplies the record coherence by
   `f = |Tr[V_1 tau_beta V_0^dag]|` (V_j = the REC-conditional block
   unitaries of the collision). With free terms off, `V_0 = I`,
   `V_1 = Ry(theta)`, and `f = cos(theta/2)` **for every diagonal
   tau_beta** — the frontier is EXACTLY temperature-blind:
   `achieved(u) = vis_A cos(theta/2)^u` (`u` = departed contacts),
   `r_feas(n) = max(0, n - d)`, `d = floor(ln(v*/vis_A)/ln cos(theta/2))`
   with `d = (1, 0, 0)` at `theta = (0.25, 0.5, 1) pi`, identical at
   every `beta` in the sweep including `beta = 0` (asserted: same-value
   spread across `beta` `< 1e-10`, integer tables identical, closed
   form `< 1e-9`). Departure at ANY temperature prices the same reach.

4. **Certificate transfer to mixed thermal states + bands.** T393's two
   all-channel certificates run unchanged on the retained density
   matrices: (a) phi-independence certificate (max pairwise entrywise
   diff across `PHI_CERT`, `< 1e-12` fires) — exactness carried by the
   degree-1 trigonometric structure `rho(phi) = A + e^{i phi} B +
   e^{-i phi} B^dag` (single phase gate; `P(M = 0) = 7/8`
   phi-independent), so flatness at >= 3 phases forces flatness at ALL
   phi; the 3-phase reconstruction is itself asserted (`< 1e-12` at
   held-out phases); (b) trace-norm bound `L <= 2(||Re X||_1 +
   ||Im X||_1)`, `X = mean_phi e^{i phi} rho_retained|M=0(phi)` over
   the 8-point lock grid (Hoelder + CPTP contractivity; rigorous for
   any CPTP map on the retained registers, mixed states included). In
   this family the bound computes to exactly `2x` achieved
   (block-off-diagonal `X`; `||V_0 tau V_1^dag||_1 = 1`) — the same
   factor-2 looseness measured in T393/T408/T409, now at finite
   temperature (`< 1e-9` asserted). Bands per cell:
   `feasible_zero_cost` / `certified_infeasible` /
   `undetermined_by_bound`, with `u_min_cert = floor(ln(v*/(2 vis_A))/
   ln f) + 1`: free-off `(10, 3, 1)` at `theta = (0.25, 0.5, 1) pi` —
   vacuous within `n <= 5` at `0.25 pi`, reported as undetermined, not
   narrated around. Free terms ON at `theta = pi`: `f <= |A_blk|` with
   `A_blk = cos(Omega tau) + i sin(Omega tau)/(2 Omega)`,
   `Omega = sqrt(1/4 + g^2)` — at `tau = 1`, `g = pi/2`:
   `|A_blk| = 0.312194`, so `bound(u >= 1) <= 2 vis_A |A_blk| =
   0.617983 < v*` at EVERY beta (convexity in `(p0, p1)`):
   `r_cert = n` survives the free Hamiltonians. **Work invariance:**
   both certificates and every frontier bound are invariant under
   adjoining work registers in any (necessarily phi-independent) state
   — asserted numerically for BOTH `|0><0|` and Gibbs `tau_beta`
   ancillas (Stinespring dilation + `||A (x) sigma||_1 = ||A||_1`);
   the unlimited-work claim is carried by the lemma, the numerics
   assert two registers (disclosed). Attack battery: manufactured
   `|+>`-injection (raw `> 0.99`, locked `< 1e-12`),
   measure-and-feedback (`< 1e-12`), 15 seeded Haar channels on
   retained + work (seed `20260703`, illustrative — sampling never
   carries an impossibility verdict).

5. **Restoration work — the fireable ledger leg.** The restoration
   protocol at full retained reach (apply `U_i^dag` per retained
   carrier — supported on the reach, commuting, exact — then
   `CNOT S -> REC`) has computed switching work
   `W_rest(n, theta, beta) = -n w_fwd(theta, beta) - (3/7) omega`,
   where `w_fwd = (3/7)(Tr[H_B V_1 tau V_1^dag] - Tr[H_B tau])` is the
   per-contact forward writing work (free-off closed form:
   `w_fwd = (3/7) sin^2(theta/2) tanh(beta/2)`; at
   `theta = pi, beta = inf`: `3/7 = 0.428571`). Three headline branches
   predeclared here, before any code exists:
   - **B1 `restoration_work_positive_slope`**: `W_rest` linear with
     positive slope — "restoration cost acquires genuine work scaling
     with bath contact."
   - **B2 `restoration_work_flat`**: `W_rest = 0` identically —
     "reach-only pricing sharpened; work strictly orthogonal to reach."
   - **B3 `restoration_work_refund`** (the analytic prediction, derived
     in this spec pre-run): restoration within reach REFUNDS the
     forward switching work exactly (unitary undo returns each retained
     carrier's diagonal blocks, so per-contact un-write work
     `= -w_fwd` exactly and the final uncopy extracts the `3/7`-weighted
     record-carrier excitation); net round-trip work per retained
     contact exactly `0`; the genuine work/entropy scaling with bath
     contact demanded by the named-unbuilt card lives in the FORWARD
     writing cost (linear in `n`, temperature-dependent slope
     `w_fwd(theta, beta)`) and in the per-departed-contact entropy
     production `Sigma_i > 0` locked in at departure; the frontier's
     currency remains reach.
   Whichever branch the numbers select is the reported verdict;
   selecting a different headline post hoc is a listed failure
   criterion. (Deviation from the workflow plan's two-branch P9,
   stated: the closed form is hand-derivable before any code runs and
   falls outside both planned branches; B1/B2 are retained as fireable
   verdicts should the derivation be wrong.)

6. **Zero-bit contacts (`beta = 0` corner — the sharpest tooth).** At
   `theta = pi`, free off, `beta = 0`: every departed carrier's
   marginal is exactly `I/2` (identical across branches and phases),
   the branch-conditional states of the departed block are identical,
   and the escaped Holevo content is exactly `0` bits for every `u` —
   yet the frontier persists in full: `r_feas = r_cert = n`
   (`f = |Tr[Ry(pi) tau]| = 0` for every diagonal tau, so the
   phi-independence certificate fires at every insufficient reach).
   The record lives ONLY in joint coherences between retained and
   departed registers; "which register holds the record bits" has no
   answer. Closed form for the one-carrier Holevo at `theta = pi`,
   free off: `chi_1(beta) = h2(4/7 p0 + 3/7 p1) - h2(p0)` bits —
   `h2(3/7) = 0.985228` at `beta = inf` (T409's plateau), `0` at
   `beta = 0`; `chi_u` monotone in `u`, bounded by `h2(3/7)`, computed
   for `u <= 4`. T409's "contacts, not bits" sharpened: at finite
   temperature the escaped bits go DOWN while the frontier does not
   move. (Flagged, from memory, unverified: mixed/hazy-environment
   quantum Darwinism, Zwolak–Quan–Zurek lineage; discord-type
   locally-hidden correlations.)

7. **Thermal complementarity.** One-carrier displaced branch
   distinguishability `D_1(theta, beta) = sin(theta/2) tanh(beta/2)`
   (free off, `< 1e-9`); the capability deficit obeys
   `1 - (achieved/vis_A)^2 >= D_u^2` with equality iff `beta = inf`
   (asserted: `deficit - D_u^2 >= -1e-10` everywhere; equality
   `< 1e-9` at `beta = inf` — the Englert–Greenberger–Yasin duality
   corner, named per the T409 hostile-review prior-art completion,
   from memory, unverified). The thermal gap `deficit - D_u^2 > 0` at
   finite beta is the leg-6 phenomenon in trace-distance form: the
   capability deficit is temperature-blind, the locally readable
   record is not.

8. **Landauer leg (T142 conventions generalized to real beta —
   bookkeeping, not a theorem).** Scenario `n = 4, theta = pi`,
   holders = `REC + B1..B4` all retained, `beta in {inf, 1.0, 0.0}`:
   correlated uncopy erases `0` bits at Landauer floor `0` and restores
   `vis_A` with computed work `W_rest` (leg 5 — a refund is consistent
   with a floor of zero: nothing is erased); blind reset (measure-Z +
   reset each holder, no uncopy) pays the naive per-holder floor
   `5 ln 2` nats, restores `< 1e-12`, residual branch
   distinguishability of the reset holders `< 1e-12`
   (deletion-is-not-definalization, re-asserted at finite temperature);
   actual thermal record entropies reported side by side (per-holder
   marginal and joint, bits; at `beta = inf` the joint is
   `h2(3/7) = 0.985228` bits at `M = 0`, T409's number). Restore beyond
   the frontier: feasible set EMPTY (certified), min cost `inf` — an
   empty-set infimum typed as ACCESS-not-work: a work parameter now
   EXISTS in this model and is computed to be unable to substitute
   (leg 4); the infinity is still not a work divergence — departed
   carriers are outside the support of every retained-reach channel.

9. **Guardrails.** Q1D asserted numerically: declared `(S, M)` record
   (unconditioned Z-distribution) invariant across all `beta`,
   `theta`, toggle, and `n` (`< 1e-12`; collisions never touch `S` or
   `M`); retained-reach protocols move not-yet-departed outside-reach
   ancilla marginals by `< 1e-12` on the pre-trace joint state (no
   signalling out of reach); the counterfactual enlarged protocol
   moves them by exactly `(3/7) tanh(beta/2)` (`< 1e-9`) — `3/7` at
   `beta = inf` (T409's tooth), vanishing at `beta = 0` where the tooth
   is instead carried by the restored-visibility jump `0 -> vis_A`
   (the beta = 0 marginal blindness of leg 6, disclosed). **R1
   untouched**: a reach frontier through an interaction sequence, not
   a light cone (Lieb-Robinson named as an absorber risk, from memory,
   unverified).

## Class

**Exploratory, capability-object lineage; the named-unbuilt
Hamiltonian-bath rung of T393's Tier-2 card, built at its finite
repeated-interaction form.** NOT registered in CLAIM-LEDGER. Lineage:
T392 (measurement core, `v*`, gameability lemma), T393 (certificates,
tier vocabulary), T408 (operator-level flatness discipline, ledger
typing), T409 (frontier object; cited in its re-scoped,
internally-established standing only), T142 (erasure-calibration
conventions). Whether this artifact discharges the Tier-2 card is a
promotion decision that pauses for Joe per AGENTS.md. Hostile review
QUEUED for this artifact.

## Status

Predeclared. This spec is frozen before the model file exists; the
model, tests, and results follow it. Outcomes (including any fired
failure leg) are recorded in the results file, not back-edited here.

## Target Claims

- [T409: Capability Restoration Frontier](T409-capability-restoration-frontier.md)
  (the frontier object; its named-unbuilt next rung is built here; its
  hostile-review corrections are incorporated, not repeated)
- [T393: Causal Forcing of the Access Asymmetry](T393-causal-forcing-of-access-asymmetry.md)
  (both certificates; the Tier-2 card)
- [T408: Basis-Free Flat Pair and the Physical Capability Boundary](T408-basis-free-capability-boundary.md)
  (ledger typing; access-not-work convention)
- [T392: Fixed-SBS-Key Reversal Divergence Witness](T392-fixed-sbs-key-reversal-divergence-witness.md)
  (measurement core, `v*`, locked figure of merit — imported unchanged)
- [T142: Thermodynamic Erasure Calibration](T142-thermodynamic-erasure-calibration.md)
  (Landauer bookkeeping conventions — generalized here to real beta)
- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md) (guardrail, asserted numerically)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md) (guardrail; untouched)

## Definitions (registers, Hamiltonians, departure, reach, menu)

**Registers.** `S, M, REC` (apparatus core, fixed), plus up to
`n <= 5` bath ancillas `B1..B5`, one appended fresh per collision in
the Gibbs state `tau_beta`. After the meter is measured and the `M = 0`
branch selected, `M` is in a pure product state and is removed from the
density matrix (disclosed; nothing later touches it). Exact density-
matrix evolution throughout (no Trotter error); a thermofield-double
statevector purification cross-checks the DM path at the predeclared
`n = 2` configuration.

**Hamiltonians (declared assignment; hbar = omega = 1).**
`H_REC = omega |1><1|_REC`, `H_Bi = omega |1><1|_Bi`
(ground `|0>`, gap omega, resonant); `H_S = H_M = 0` (the phase-bearing
system and the measured meter are treated as work-free logical
registers — a declared modeling choice, part of the bookkeeping, not
derived). Gibbs ancilla: `tau_beta = diag(p0, p1)`,
`p0 = 1/(1 + e^{-beta})`, `p1 = e^{-beta}/(1 + e^{-beta})`;
`beta = inf` gives `|0><0|` exactly (the T409 corner), `beta = 0`
gives `I/2` exactly.

**Collision.** Window length `tau = 1.0` (omega-units), coupling
`g = theta/(2 tau)`, interaction
`H_int,i = g |1><1|_REC (x) sigma_y^(Bi)`, switched on at window start
and off at window end. Collision unitary
`U_i = expm(-i tau (f H_REC + f H_Bi + H_int,i))` with the free-term
toggle `f in {0 (off), 1 (on)}`. Free-off corner:
`U_i = controlled-Ry(theta)` EXACTLY (`Ry(2 g tau)`; `theta = 2 g tau`)
— T409's gate, zero translation loss. REC-conditional block form
(independent construction, asserted against `expm` `< 1e-12`):
`U_i = |0><0|_REC (x) V_0 + |1><1|_REC (x) e^{-i tau f} V_1`,
`V_0 = expm(-i tau f H_B)`, `V_1 = expm(-i tau (f H_B + g sigma_y))`.
Windows are back-to-back; no idle evolution is modeled (REC's free
phase during windows is inside `U_i`; the residual per-branch phases
are constant in `phi` and cannot move the locked figure of merit).

**Departure (the boundary).** Immediately after its collision, ancilla
`B_i` departs — it is traced out of the model — unless `i` is in the
retained set `R_set`, declared once per scenario and identical across
preparations and phases. **Reach = apparatus core `{S, REC}` + the
retained ancillas.** There is no declared menu restriction on
co-present registers: what the agent cannot touch is what is gone.

**Menu.** ALL CPTP channels supported on the reach, with unlimited work
ancillas in any (necessarily phi-independent) state — pure or Gibbs;
dilation lemma asserted numerically for both.

**Figure of merit.** Phase-locked conditional X-visibility
`|mean_phi e^{i phi} 2 rho_S[0,1]|` over the uniform 8-point grid
`PHI_LOCK_GRID` (T392's gameability lemma: the grid exactly nulls
manufactured phi-independent coherence). Threshold `v* = 0.9`,
imported unchanged. Zero-collision restorable value
`vis_A = 4 sqrt(3)/7 = 0.989743`.

**Frontier.** `r_feas(n, theta, beta, toggle)` = least retained-reach
size whose restoration protocol restores `>= v*`;
`r_cert` = greatest reach size such that every smaller reach has
trace-norm bound `< v*` (all channels). `r_cert <= r_true <= r_feas`.

**Ledger conventions.** All work/heat in omega-units on the
`M = 0`-conditioned trajectory (the branch the agent inhabits;
disclosed); entropies in nats except record/Holevo entropies flagged in
bits (T409 continuity). Work under the switching convention
(`W = Delta E_free` across each gate/window) with the autonomous
interior (`Delta<H_window> = 0` while coupled) reported side by side —
the two coincide because `H_int` is off at endpoints. The
work/heat/entropy stream is phi-independent (asserted `< 1e-12`): the
thermodynamic ledger carries no record of the phase.

## Setup

`models/thermal_collision_work_reach_frontier.py`; exact density-matrix
simulation, numpy + `scipy.linalg.expm` (first scipy use in `models/`;
disclosed — the expm construction is asserted against the analytic
REC-block form `< 1e-12`), deterministic; the only sampling (Haar spot
check, 15 samples, seed `20260703`) is illustrative and never carries
an impossibility verdict. Imports by name: T392's `THETA` (meter),
`V_STAR`, `_HADAMARD`, `zero_state`, `reduced_density_matrix`,
`z_distribution`; T393's `PHI_CERT`, `PHI_LOCK_GRID`, `apply_on_qubits`
(purification cross-check), `haar_unitary`, `_trace_norm`; T142's
`landauer_bound_bits`, `LANDAUER_NAT_PER_BIT`; T409's `frontier_row`
(regression comparison only). Peak retained dimension `2^7 = 128`
(`S, REC` + 5 ancillas) plus transient appended carrier.

## Predeclared constants, sweeps, tolerances (fixed here, before the model)

- Imported unchanged and cited: `theta_meter = pi/3`, `v* = 0.9`,
  `PHI_CERT = (0, 1.0, sqrt(2), pi/3, 2 pi/3, pi/7)`, `PHI_LOCK_GRID`
  = 8 uniform points, `vis_A = 4 sqrt(3)/7`, `M = 0` conditioning.
  Changing any of these after seeing numbers is a listed failure
  criterion.
- `TAU = 1.0`; `BETA_SWEEP = (inf, 2.0, 1.0, 0.5, 0.0)`;
  `THETA_SWEEP = (0.25 pi, 0.5 pi, pi)`; free-term toggle
  `(off, on)`; `n = 1..5` (`N_ANC_MAX = 5`).
- Exhaustive retained-subset blocks: ALL `2^n` subsets for `n <= 3` at
  every sweep point. Symmetry pruning at `n = 4, 5` asserted BEFORE any
  canonical-prefix shortcut is used, via explicit permuted-subset
  retained-state comparisons at the predeclared pairs — `n = 5`: sizes
  1 (`{B1}` vs `{B3}` vs `{B5}`), 2 (`{B1,B2}` vs `{B2,B4}` vs
  `{B3,B5}`), 4 (`{B1..B4}` vs `{B2..B5}`); `n = 4`: size 2
  (`{B1,B2}` vs `{B2,B4}`) — each at
  `(theta, beta, toggle) in {(0.5 pi, 1.0, off), (0.5 pi, 1.0, on),
  (pi, 0.5, off), (0.25 pi, inf, on)}`, `phi in {1.0, pi/3}`,
  max entrywise diff `< 1e-12`.
- Tolerances: `FLATNESS_TOL = 1e-12` (certificates, invariances,
  exact-zero assertions); `ANALYTIC_TOL = 1e-9` (closed-form matches,
  regression values); identity/cross-check tolerance `1e-10`
  (Sigma both-ways, purification, global balance, round-trip work);
  `Sigma >= -1e-10`; same-size subset spread `< 1e-10`. Values at or
  below `1e-13` are reported as "< 1e-13 (machine floor)", never as
  bolded run digits (T409 hostile-review correction, adopted).
- Purification cross-check configuration: `n = 2`, retain `{B2}`
  (B1 departed), `beta = 1.0`, `theta = 0.5 pi`, both toggles,
  `phi in {1.0, pi/3}`: retained DM from the thermofield statevector
  path agrees with the density-matrix path `< 1e-10`.
- Work-substitution attack cells (the fireable region):
  `(theta = 0.5 pi, off)`, `beta in {inf, 1.0, 0.0}`, `n = 4`,
  retained prefixes `r in {2, 3}` (`u in {2, 1}`; free-off bounds
  `2 vis_A cos(pi/4)^u = {0.989743, 1.399657}` — both `>= v*`, hence
  undetermined-by-bound, hence genuinely open pre-run). Attacks per
  cell: the un-write baseline; manufactured `|+>`-injection;
  measure-and-feedback; 15 seeded Haar channels on retained + two work
  registers (one `|0>`, one Gibbs(beta)). The leg fires iff any attack
  reaches `>= v*` below `r_feas`.
- Ledger scenarios: leg-1/leg-5 stream bookkeeping at
  `(theta, beta, toggle)` across the full sweep, `n = 4`; Sigma
  identity asserted at `beta in {2.0, 1.0, 0.5, 0.0}`; leg-8 holders
  scenario `n = 4, theta = pi, off, beta in {inf, 1.0, 0.0}`; leg-6/7
  tables at `theta in {0.5 pi, pi}`, free off, `n = 4`, `u = 0..4`,
  full beta sweep, Holevo blocks `u <= 4`.
- Runtime budgets, predeclared: model run `< 300 s`, test suite
  `< 300 s` (report actual against budget). If busted: fall back to
  `n <= 4` and report the reduction — never silently.
- Haar seed `20260703`, 15 samples, ceiling `0.05` for the
  illustrative-attack row at certified cells; labeled "illustrative;
  the certificates carry the verdict".

## Verified exactly (assertions the suite makes)

1. Construction: `expm` unitary = REC-block construction `< 1e-12`;
   free-off `U = controlled-Ry(theta)` `< 1e-12`; `tau_inf = |0><0|`,
   `tau_0 = I/2` exact; `P(M=0) = 7/8` phi-independent `< 1e-12`.
2. Leg 1: interior conservation `< 1e-12`; `W = -Delta<H_int>`
   agreement `< 1e-12`; Sigma both-ways identity `< 1e-10` (finite
   beta), `Sigma >= -1e-10`, cumulative monotone; per-collision
   `W, Q` identical across `i` `< 1e-12`; ledger phi-independence
   `< 1e-12`; global balance `< 1e-10`.
3. Leg 2: regression integers equal; achieved/bound vs T409
   `frontier_row` `< 1e-9`; certs `< 1e-12` both modules; `vis_A`
   restored `< 1e-9`.
4. Leg 3: free-off achieved spread across beta `< 1e-10`; closed form
   `< 1e-9`; frontier integer tables beta-identical; `d` and
   `u_min_cert` match `(1, 0, 0)` and `(10, 3, 1)`.
5. Leg 4: phi-cert `< 1e-12` where `f = 0` (theta = pi, off, all
   beta); degree-1 reconstruction `< 1e-12`; bound `= 2x` achieved
   `< 1e-9`; free-on theta = pi bound(u=1) `<= 0.617983 + 1e-9` and
   `< v*` at every beta; dilation invariance `< 1e-12` for `|0><0|`
   AND Gibbs sigma; attacks nulled as predeclared; band
   classifications match the closed-form `u_min_cert`.
6. Leg 5: `W_rest = -n w_fwd - 3/7` `< 1e-9`; free-off
   `w_fwd = (3/7) sin^2(theta/2) tanh(beta/2)` `< 1e-9`; round-trip
   work per retained contact `< 1e-10`; branch B1/B2/B3 selection
   consistent with the computed numbers.
7. Leg 6: beta = 0 marginals `I/2` `< 1e-12`; branch-block equality
   `< 1e-12`; `chi_u(0) < 1e-12`; `chi_1(beta)` closed form `< 1e-9`;
   `chi_u(inf) = h2(3/7)` `< 1e-9` for `u >= 1`; frontier at beta = 0
   equals the beta = inf frontier (integers).
8. Leg 7: `D_1 = sin(theta/2) tanh(beta/2)` `< 1e-9`;
   `deficit - D_u^2 >= -1e-10`; equality at `beta = inf` `< 1e-9`.
9. Leg 8: uncopy `erased_bits = 0`, restores `>= v*`; blind reset
   restores `< 1e-12`, residual `< 1e-12`, naive floor
   `= landauer_bound_bits(5)`; joint record bits at `beta = inf,
   M = 0` `= h2(3/7)` `< 1e-9`; beyond-frontier `inf` typed
   access-not-work.
10. Leg 9 (Q1D): record invariance `< 1e-12`; no-signal-out
    `< 1e-12`; teeth `= (3/7) tanh(beta/2)` `< 1e-9` (`= 3/7` at
    `beta = inf`); beta = 0 tooth carried by the visibility jump;
    R1 note contains "not a light cone" and "Lieb-Robinson".
11. Discipline: exhaustive subsets counted (`2^n` for `n <= 3`);
    same-size spread `< 1e-10`; symmetry pairs `< 1e-12`; determinism
    (bit-identical repeat); register layout; verdict tags tuple ends
    `no_claim_promotion`; verdict language contains "pause for Joe",
    "no claim promotion", "named-unbuilt".

## Success Criteria

- All nine legs hold as predeclared, with every impossibility verdict
  carried by a certificate (never by sampling), the T409 regression
  corner exact, and the ledger identities closing at the stated
  tolerances.
- The restoration-work branch (B1/B2/B3) selected BY THE NUMBERS and
  reported under its predeclared headline sentence.
- Bands reported as computed, including the vacuous
  weak-coupling certification band (undetermined, not narrated
  around); the factor-2 bound looseness disclosed, fourth artifact.

## Failure Criteria (predeclared reportable verdicts — findings, not patches)

- **`work_substitutes_for_reach_at_finite_temperature`**: any attack
  in the predeclared undetermined-band cells restores `>= v*` below
  `r_feas`. Fires -> becomes the headline (the physically interesting
  substitution T409's review asked for). Honest scope: fireable ONLY
  in the undetermined band; in certified cells it is excluded by the
  bound (disclosed here, pre-run, to avoid predeclaration theater).
- **`restoration_work_positive_slope` (B1) / `restoration_work_flat`
  (B2)**: the leg-5 numbers contradict the B3 derivation. Fires ->
  reported with the failed algebra located; headline switches to the
  fired branch.
- **`thermal_frontier_collapse`**: the free-off frontier moves with
  temperature (contradicting the `f = cos(theta/2)` law). Fires ->
  reported; leg 3 fails as stated.
- **`entropy_production_violation`**: any `Sigma_i < -1e-10` — a
  bookkeeping defect, not physics. HALT and report; no results
  claimed.
- **`t409_regression_failure`**: the regression corner does not
  reproduce T409's block. HALT and report; translation loss located.
- Any tuning of `v*`, the phase grids, the sweeps, the subset family,
  seeds, or tolerances after inspecting values; any headline selected
  against the predeclared branch table; recovery measured by raw
  visibility (the exploit is a null control); the departed carriers
  quietly re-appended to any admissible protocol; reach adjusted per
  preparation.
- The leg-1/5/8 ledger stated as a thermodynamic THEOREM (it is
  exact-identity-backed bookkeeping at the computed states); the
  beyond-frontier `inf` read as divergent work.
- **Re-scope clause (verbatim, predeclared):** if the assembled object
  is standard repeated-interaction thermodynamics with no
  discriminator content beyond data processing, the artifact re-scopes
  to a repo-internal calibration of the certificate toolkit at finite
  temperature.

## Neighbors / Prior Art

In-repo: T393 (certificates, tier card), T408 (ledger typing), T409
(frontier; internally established in re-scoped standing; its
hostile-review corrections — degree-1 trig sentence, the
"(necessarily phi-independent)" qualifier, machine-floor reporting,
EGY naming — are adopted here from the start), T142/T144/T145 (erasure
conventions), T407 (C(R) lineage; its standing objection — declared vs
physical boundary — is addressed here by departure, conditionally on
the reservoir idealization, and NOT claimed discharged).

Candidate prior art (ALL from memory — flagged, unverified, per the
no-fake-citations rule; named as absorber risks for the queued hostile
review):

- **Repeated-interaction / collision-model thermodynamics**
  (Barra 2015; Strasberg–Schaller–Brandes–Esposito 2017; De Chiara et
  al.; Landi–Paternostro-lineage reviews) — switched-coupling work,
  per-collision first law, and the entropy-production identity are
  presumed STANDARD; the model class is not the claimed content.
- **Esposito–Lindenberg–Van den Broeck 2010** — the leg-1 identity
  `Sigma = I + D` is presumed to be exactly their result; it is used
  as a cross-check, not claimed.
- **Quantum Darwinism, incl. mixed/hazy environments**
  (Zurek; Zwolak–Quan–Zurek) — finite-temperature suppression of
  redundant records is their territory; leg 6's Holevo suppression is
  presumed adjacent or identical in mechanism.
- **Englert–Greenberger–Yasin duality** — leg 7's `beta = inf` corner
  (named per the T409 review; the thermal-gap version computed here is
  not claimed new, only computed).
- **Environment-assisted recovery / Petz recovery**
  (Gregoratti–Werner; half-environment recovery) — the
  sufficient-reach side is worked territory; no result claimed or
  used.
- **Lieb-Robinson bounds** — no geometry, no locality bound; the
  frontier is a reach frontier, not a light cone.

The claimed residue, if the legs hold: the ASSEMBLED object — the
T409 frontier surface with a genuine `(beta, work, entropy)` axis
attached, departure as the boundary carrier, the temperature-blind
free-off frontier law, the refund/lock-in split of the work ledger,
and the zero-bit-contacts corner — under the same certificate
discipline. If verification shows even the assembly is standard, the
re-scope clause above fires.

## Honest Reviewer Attack Surface

- **"Departure is declared bookkeeping too — you chose to trace."**
  Conceded in part, pre-run: the repeated-interaction reservoir
  idealization (fresh ancillas, never returning) is ADOPTED, not
  derived. The claim is conditional on that model class, and the
  verdict language says so. What changes vs T409: within the model
  class the inaccessibility is carried by the state space itself
  (the carrier is not in the model after departure), not by a menu
  line forbidding a co-present register. The unconditional version —
  transport, spatial dispersion, work literally buying reach — is
  named-unbuilt.
- **"The interesting substitution is still not live: in certified
  cells work cannot fire."** Correct and disclosed: the fireable
  region is exactly the undetermined band. That band is nonempty and
  predeclared (six cells), which is more than T409's leg 2 had; a
  tighter-than-2x bound would shrink it and is a named open card.
- **"W_rest is a refund — so there is no thermodynamic price of
  restoration at all."** If B3 holds, the price structure is: forward
  contact costs work and locks in entropy production at departure;
  restoration-within-reach refunds the work precisely BECAUSE the
  reach still contains the carriers. The thermodynamic price of the
  CAPABILITY loss is booked at departure, which is the artifact's
  point; saying "restoration is free within reach" without the
  departure ledger would be the dishonest reading.
- **"H_S = H_M = 0 is a convenient assignment."** Yes — declared,
  disclosed, and inert: S carries the phase (its Hamiltonian would
  add a deterministic, locked-metric-invisible phase), M is measured
  and removed. The ledger's load-bearing terms live on REC and the
  carriers.
- **"Six phases again."** The degree-1 trigonometric argument is
  stated in-claim this time (T409 correction adopted) and the 3-phase
  reconstruction is itself asserted.

## Known Physics Constraints

- No-cloning respected (partial Z-copies of an already-branched
  record); the meter statistics are phi-independent, so conditioning
  introduces no phase information.
- The impossibility side quantifies over all CPTP maps on the reach
  via the trace-norm bound and the phi-independence certificate
  (degree-1 structure); work ancillas covered by the dilation lemma
  in any (necessarily phi-independent) state, asserted for pure and
  Gibbs sigma.
- Exact density-matrix evolution; the purification cross-check pins
  the DM path to a statevector path; the only randomness is the
  seeded, illustrative Haar battery.
- Entropy production nonnegativity is asserted as computed (the
  exact identity makes it structural for fresh Gibbs ancillas); at
  `beta = inf` the divergence is typed, not asserted.

## What This Does Not Earn

- **No continuum, weak-coupling, or transport theorem** — the
  asymptotic bath-dispersion statement, work BUYING reach, and
  spatial re-collection stay **named-unbuilt** (the next rung).
- **No thermodynamic theorem**: legs 1/5/8 are exact-identity-backed
  bookkeeping at the computed states of a finite model
  (finite-witness per COMPLEXITY-LEDGER vocabulary).
- **No discharge of T407's standing objection** is claimed
  unconditionally: the boundary is physical GIVEN the reservoir
  idealization; the idealization is adopted.
- **No hardware, platform, or experimental claim.**
- **No new mathematics or new physics**: every assembled physical fact
  is presumed standard (flagged above, from memory, unverified); the
  claimed residue is the assembled, certificate-disciplined object.
- **No claim promotion, no CLAIM-LEDGER entry**; ledger actions pause
  for Joe per AGENTS.md. Hostile review is QUEUED, not survived.

## Reproduction

```bash
python -m pytest tests/test_thermal_collision_work_reach_frontier.py -v
python -m models.thermal_collision_work_reach_frontier
```

Deterministic; predeclared budgets `< 300 s` each (actuals reported in
the results file).

## Contribution Needed

- The transport rung: carriers that MOVE (chain / field), where reach
  has geometry, re-collection costs work that scales with distance,
  and "work buys reach" becomes a live positive channel — the
  physically interesting substitution, still unbuilt.
- The weak-coupling / continuum limit (Lindblad or SLH), where the
  certificates need continuum analogues (exact phi-independence will
  not survive discretization removal).
- A tighter-than-2x channel bound (fourth artifact measuring the same
  looseness; the undetermined band it leaves is now the fireable
  region, so tightening it has teeth).
- Verification of the flagged prior art (collision-model
  thermodynamics; EGY; hazy-environment Darwinism) before anything
  external-facing; hostile review first.
