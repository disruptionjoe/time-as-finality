# T410 Thermal Collision Work–Reach Frontier — Results v0.1

- **Artifact:** `T410-thermal-collision-work-reach-frontier-v0.1`
- **Spec:** [tests/T410-thermal-collision-work-reach-frontier.md](../tests/T410-thermal-collision-work-reach-frontier.md)
- **Model:** [models/thermal_collision_work_reach_frontier.py](../models/thermal_collision_work_reach_frontier.py)
- **Test:** [tests/test_thermal_collision_work_reach_frontier.py](../tests/test_thermal_collision_work_reach_frontier.py)
- **Numbers:** [T410-thermal-collision-work-reach-frontier-v0.1.json](T410-thermal-collision-work-reach-frontier-v0.1.json)
- **Tags:** thermal_collision_work_reach_frontier,
  hamiltonian_bath_finite_rung, departure_carried_boundary,
  temperature_blind_reach_frontier, restoration_work_refund_within_reach,
  entropy_locked_at_departure, ledger_bookkeeping_not_theorem,
  no_claim_promotion

**Hostile review is QUEUED for this artifact, not yet performed.**
Nothing below has survived independent adversarial reproduction. T409 is
cited throughout in its corrected, re-scoped standing (internally
established per `audits/2026-07-02-t409-hostile-review.md`); its
hostile-review corrections (degree-1 trig sentence, the "(necessarily
phi-independent)" qualifier, machine-floor reporting, EGY naming,
predeclaration-trail discipline) are adopted here from the start.

**T-number provisional:** T410 verified free at every file-creation step
(highest taken anywhere: T409; repo-wide grep for T410–T499 empty). Next
free T-numbers as of this write: **T411+**. Noted here only; TESTS.md
and CLAIM-LEDGER.md untouched per house rules.

**Predeclaration trail (auditable this time):** file-creation order was
spec → model → tests → results (this file last); the spec was
content-frozen before the model file existed and has not been edited
since — including one sentence that a predeclared cross-check later
revealed to be mis-scoped (disclosed below, Leg 1), left frozen in the
spec and reported here rather than back-edited. Constants imported
byte-identical from T392/T393/T142 are auditably prior; every
T410-specific sweep, threshold, tolerance, seed, and failure leg is in
the frozen spec.

## Verdict (house vocabulary)

**The thermal-collision work–reach frontier holds in this finite
repeated-interaction family — all nine legs.** The switched-Hamiltonian
Gibbs-ancilla collision stream reproduces T409's frontier exactly at its
zero-temperature free-off corner (zero translation loss, cross-module)
and extends it with a genuine work parameter, temperature, heat, and
entropy production — the content T393/T408/T409 named identically as
the unbuilt next rung. With free terms off the frontier is
**temperature-blind**: `f = |Tr[V_1 tau_beta V_0^dag]| = cos(theta/2)`
for every diagonal `tau_beta`, so departure at ANY temperature prices
the same reach — `r_feas = r_cert = n` at `theta = pi` at every swept
`beta` **including `beta = 0`, where every departed carrier holds
exactly zero locally readable record bits** (marginals exactly `I/2`,
branch blocks identical, escaped Holevo exactly `0`) and the record
lives only in joint coherences between retained and departed registers.
Both certificates transfer to mixed thermal states and are invariant
under work registers in any (necessarily phi-independent) state, pure
or Gibbs. Restoration within reach is a **work refund** (predeclared
branch B3, selected by the numbers): `W_rest = -n w_fwd - 3/7` with
round-trip work per retained contact exactly zero — the work/entropy
scaling with bath contact demanded by the named-unbuilt card is
computed, and it prices **contact and departure, not
restoration-within-reach**: forward contact costs `w_fwd(theta, beta)`
per collision and locks in entropy production `Sigma_i > 0` at
departure; the frontier's currency remains reach. The boundary is
physical GIVEN the repeated-interaction reservoir idealization, which
is **adopted, not derived** (T407's standing objection is NOT claimed
discharged unconditionally); the continuum/transport rung — work
literally BUYING reach — stays **named-unbuilt**. Bookkeeping,
exact-identity-backed at the computed states; finite-witness. **No
claim promotion; no CLAIM-LEDGER entry; ledger actions pause for Joe
per AGENTS.md.**

## Predeclarations (fixed before inspecting numbers)

- Imported unchanged and cited: `theta_meter = pi/3`, `v* = 0.9`,
  `PHI_CERT`, `PHI_LOCK_GRID` (8 uniform points), phase-locked
  conditional X-visibility figure of merit, `M = 0` conditioning,
  `vis_A = 4 sqrt(3)/7 = 0.989743`.
- Model constants: `hbar = omega = 1`; `H_REC = H_B = omega |1><1|`;
  `H_S = H_M = 0` (declared assignment, disclosed); `tau = 1.0`;
  `g = theta/(2 tau)`; `H_int = g |1><1|_REC (x) sigma_y`; Gibbs
  ancillas `tau_beta`, `beta = inf` the exact T409 corner.
- Sweeps: `beta in {inf, 2.0, 1.0, 0.5, 0.0}`,
  `theta in {0.25, 0.5, 1} pi`, free-term toggle {off, on}, `n = 1..5`;
  exhaustive retained subsets (all `2^n`) for `n <= 3` at every sweep
  point; symmetry pairs at `n = 4, 5` predeclared and asserted before
  canonical-prefix use.
- Tolerances: certificates/invariances `< 1e-12`; closed forms
  `< 1e-9`; identities (Sigma both ways, purification, balance,
  round-trip) `< 1e-10`; `Sigma >= -1e-10`; sub-`1e-13` values reported
  as machine floor, never as bolded run digits.
- Restoration-work headline branches B1 (positive slope) / B2 (flat) /
  B3 (refund — the spec's hand-derived prediction) predeclared with
  their sentences; post-hoc headline selection a listed failure
  criterion.
- Failure legs as reportable verdicts:
  `work_substitutes_for_reach_at_finite_temperature` (fireable ONLY in
  the six predeclared undetermined-band cells — disclosed pre-run, the
  T409 predeclaration-theater lesson), `restoration_work_flat`,
  `restoration_work_positive_slope`, `thermal_frontier_collapse`,
  `entropy_production_violation` (halting),
  `t409_regression_failure` (halting); the re-scope clause verbatim in
  the spec. No assertion weakening.
- Haar 15 samples, seed `20260703`, illustrative; runtime budgets
  `< 300 s` (model) and `< 300 s` (suite).

## Leg 1 — first law + entropy production (exact-identity-backed)

Scenario `n = 4`, full sweep (3 theta x 5 beta x 2 toggles, full and
partial retention):

| Identity | Worst residual over sweep |
| --- | --- |
| interior autonomy `Tr[H_window Delta rho] = 0` | machine floor (< 1e-13; tol 1e-12) |
| switching work `W = -Delta<H_int>` (free ON) | machine floor (< 1e-13; tol 1e-12) |
| `Sigma_i` two-way identity `Delta S + beta Q = I + D` (finite beta) | machine floor (< 1e-13; tol 1e-10) |
| min `Sigma_i` over sweep | **0.0** (>= -1e-10) |
| global energy balance (appended/departed counted) | machine floor (< 1e-13; tol 1e-10) |
| `W, Q` uniform across collisions; ledger phi-blind | machine floor (< 1e-13) |

Per-collision work/heat and entropy production at `theta = pi`, free
off, full retention (`W_i = Q_i = w_fwd`; nats):

| `beta` | `W_i = Q_i` (omega-units) | `Sigma_i` (nats) |
| --- | --- | --- |
| inf | **0.428571** (= 3/7) | inf (typed: zero-temperature limit, `D(rho'||pure)` divergent — disclosed, not asserted) |
| 2.0 | 0.326397 | 1.335703 |
| 1.0 | 0.198050 | 0.880958 |
| 0.5 | 0.104965 | 0.735391 |
| 0.0 | 0.0 | 0.682908 (`= Delta S_complex`; identity still exact at `beta = 0`) |

**Fired finding (spec-wording defect, disclosed — not repaired):** the
frozen spec's leg-1 parenthetical "equivalently `W_i = -Delta<H_int>`"
is true only with free terms ON (where `H_int` is the only switched
term). With free terms OFF the window generator is `H_int` alone:
interior conservation gives `Delta<H_int> = 0` (asserted, same machine
floor), the switched object is the entire window generator, and
`W = Delta E_free` by definition — the free-off deviation
`|W - (-Delta<H_int>)|` equals `w_fwd` per collision (max over sweep
`0.428571 = 3/7`), which is what revealed the mis-scoping. No computed
quantity, closed form, or leg verdict is affected. The spec file is
left frozen; the defect lives here and in the model/JSON
(`first_law.spec_wording_defect`).

## Leg 2 — T409 regression corner (zero translation loss)

At `(beta = inf, free off)` the collision unitary equals
`controlled-Ry(theta)` to machine floor, and:

| n | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| `r_feas(n)` at `theta = pi` | 1 | 2 | 3 | 4 | 5 |
| `r_cert(n)` at `theta = pi` | 1 | 2 | 3 | 4 | 5 |

- Every insufficient retained reach: phi-independence certificate and
  trace-norm bound at machine floor (< 1e-13; tol 1e-12); full reach
  restores **0.989743** (`= 4 sqrt(3)/7`, < 1e-9).
- **Cross-module comparison against T409's own `frontier_row`**
  (`n in {1, 3, 5}`, all reach sizes, `theta in {0.5 pi, pi}` — 22
  cells): worst achieved/bound difference at machine floor
  (< 1e-13; tol 1e-9). The departure boundary (partial trace)
  reproduces T409's declared-reach reduced states exactly — the
  translation is lossless; what changes is what CARRIES the boundary.

## Leg 3 — temperature-blind frontier (free terms off)

`f = |Tr[V_1 tau_beta V_0^dag]| = cos(theta/2)` for every diagonal
`tau_beta` — asserted at every sweep point; achieved spread across the
full beta sweep at machine floor; closed form
`achieved(u) = vis_A cos(theta/2)^u` to < 1e-9; frontier integer tables
IDENTICAL at every beta including `beta = 0`:

| `theta/pi` | d | `u_min_cert` | `r_feas(1..5)` | `r_cert(1..5)` | bracket |
| --- | --- | --- | --- | --- | --- |
| 0.25 | 1 | 10 | 0 1 2 3 4 | 0 0 0 0 0 | cert honestly vacuous within `n <= 5` |
| 0.50 | 0 | 3 | 1 2 3 4 5 | 0 0 1 2 3 | width 2 (bound = 2x achieved) |
| 1.00 | 0 | 1 | 1 2 3 4 5 | 1 2 3 4 5 | **exact** |

`d` and `u_min_cert` match the predeclared closed-form values
`(1, 0, 0)` and `(10, 3, 1)`; onset and bite edges are T408/T409's
constants, now shown beta-independent. `thermal_frontier_collapse` did
not fire.

## Leg 4 — certificate transfer, bands, dilation, and the fireable leg

- **phi-independence on mixed thermal states:** at `theta = pi` free
  off, every insufficient reach at every beta certified — worst
  certificate at machine floor (< 1e-13; tol 1e-12). Exactness carried
  by the degree-1 trigonometric structure (single phase gate;
  `P(M = 0) = 7/8` phi-independent, asserted): the 3-phase
  reconstruction predicts all six `PHI_CERT` states to machine floor.
- **Bound = 2x achieved** at every checked cell, both toggles, all
  temperatures (worst deviation < 1e-9 as predeclared; actual machine
  floor): the factor-2 looseness of T393/T408/T409, measured in a
  **fourth artifact**, now at finite temperature.
- **Free terms ON at `theta = pi`** (the certificate that survives real
  Hamiltonians): `f` becomes beta-dependent but stays under the
  analytic ceiling `|A_blk| = 0.312194`, so `bound(u = 1) <= 0.617983
  < v*` at every beta — `r_cert = n` survives:

  | `beta` | inf | 2.0 | 1.0 | 0.5 | 0.0 |
  | --- | --- | --- | --- | --- | --- |
  | `f` (free on) | 0.312193 | 0.242931 | 0.159574 | 0.106793 | 0.076896 |
  | bound at `u = 1` | 0.617982 | 0.480878 | 0.315876 | 0.211395 | 0.152214 |
  | band | certified | certified | certified | certified | certified |

- **Dilation (work invariance):** certificates and every frontier bound
  invariant under adjoining work registers in `|0><0|` AND in Gibbs
  `tau_beta` (both asserted; all diffs at machine floor). The
  unlimited-work claim is carried by the lemma (Stinespring +
  `||A (x) sigma||_1 = ||A||_1`, valid for any — necessarily
  phi-independent — sigma); the numerics assert two registers, one
  pure, one Gibbs (disclosed).
- **The fireable failure leg — did not fire.** Six predeclared
  undetermined-band cells (`theta = 0.5 pi`, off,
  `beta in {inf, 1.0, 0}`, `n = 4`, reach `{2, 3}`; bounds
  0.989743 / 1.399657 >= v*): manufactured `|+>`-injection raw
  1.000000 / locked machine floor; measure-and-feedback machine floor;
  15 seeded Haar channels on retained + two work registers per cell,
  max locked visibility **0.0817** (< `v* = 0.9`; illustrative — the
  cells REMAIN `undetermined_by_bound`, which is the honest verdict:
  no certificate excludes a cleverer channel there, and no sampled
  channel found one).
  `work_substitutes_for_reach_at_finite_temperature: fired = False`.

## Leg 5 — restoration work: branch B3 (refund) selected by the numbers

Predeclared law confirmed at every sweep point (both toggles):
`W_rest(r, theta, beta) = -r w_fwd(theta, beta) - 3/7`, residual
< 1e-9 (actual machine floor); free-off closed form
`w_fwd = (3/7) sin^2(theta/2) tanh(beta/2)` exact; **round-trip work
per retained contact = 0** to < 1e-10 (actual machine floor).

`W_rest` by `n` at (`theta = pi`, `beta = 1.0`, off) — linear, slope
`-w_fwd = -0.198050`:

| n | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| `W_rest` | -0.6266 | -0.8247 | -1.0227 | -1.2208 | -1.4188 |

At the T409 corner `w_fwd(pi, inf) = 3/7 = 0.428571` exactly; at
`beta = 0`, `w_fwd = 0` (writing into an infinite-temperature bath
costs no switching work) and `W_rest = -3/7` exactly (the uncopy
refund). **Headline (B3, predeclared):** restoration within reach
REFUNDS the forward switching work exactly (unitary undo); the genuine
work/entropy scaling with bath contact lives in the forward writing
cost (linear in `n`, slope `w_fwd(theta, beta)`) and in the
per-departed-contact entropy production locked in at departure; the
frontier's currency remains reach. B1 and B2 did not fire.

## Leg 6 — zero-bit contacts: the `beta = 0` corner

Escaped Holevo (bits) of the departed block at `theta = pi`, free off,
`n = 4`, by departed count `u`:

| `beta` | u=1 | u=2 | u=3 | u=4 |
| --- | --- | --- | --- | --- |
| inf | **0.985228** | 0.985228 | 0.985228 | 0.985228 |
| 2.0 | 0.464379 | 0.676485 | 0.804162 | 0.874676 |
| 1.0 | 0.156912 | 0.281774 | 0.384813 | 0.470667 |
| 0.5 | 0.042830 | 0.083162 | 0.121258 | 0.157322 |
| 0.0 | **0.0** | 0.0 | 0.0 | 0.0 |

- `beta = inf` row = T409's plateau `h2(3/7)` (regression); closed form
  `chi_1(beta) = h2(4/7 p0 + 3/7 p1) - h2(p0)` exact (< 1e-9).
- At `beta = 0`: every single-carrier marginal exactly `I/2` (diff
  0.0), branch-conditional departed blocks identical (diff 0.0), Holevo
  exactly 0 — **and the frontier does not move:**
  `r_feas = r_cert = (1, 2, 3, 4, 5)`, identical to `beta = inf`.
- **T409's "contacts, not bits," sharpened:** the escaped bits fall
  monotonically with temperature (asserted per `u`) all the way to
  exactly zero, while the reach frontier is temperature-blind. At
  `beta = 0` "which register holds the record bits" has no answer —
  the record is entirely in joint coherences spanning the departure
  boundary. (Flagged, from memory, unverified: hazy-environment
  quantum Darwinism, Zwolak–Quan–Zurek; discord-type locally-hidden
  correlations.)

## Leg 7 — thermal complementarity

- `D_1(theta, beta) = sin(theta/2) tanh(beta/2)` exact (< 1e-9).
- `deficit - D_u^2 >= 0` at every cell (min gap 0 at machine floor);
  equality at `beta = inf` (< 1e-9) — the Englert–Greenberger–Yasin
  duality corner (named per the T409 review; from memory, unverified).
- Sample rows (`theta = 0.5 pi`, `beta = 1.0`, `n = 4`):

| u | achieved | deficit | displaced `D_u` | gap `deficit - D_u^2` |
| --- | --- | --- | --- | --- |
| 0 | 0.989743 | 0.0 | 0.0 | 0.0 |
| 1 | 0.699854 | 0.500000 | 0.326766 | 0.393224 |
| 2 | 0.494872 | 0.750000 | 0.343769 | 0.631823 |
| 4 | 0.247436 | 0.937500 | 0.493506 | 0.693952 |

The strictly positive thermal gap is leg 6 in trace-distance form: the
capability deficit is temperature-blind; the locally readable record
is not.

## Leg 8 — Landauer ledger (T142 conventions at real beta; bookkeeping)

Scenario `n = 4`, `theta = pi`, holders = `REC + B1..B4`:

| `beta` | uncopy: erased bits / `W_rest` / restores | blind reset: naive floor / restores / residual | joint record bits (M=0) | heat per collision |
| --- | --- | --- | --- | --- |
| inf | 0 / -2.142857 / **0.989743** | `5 ln 2 = 3.4657` nats / 0.0 / 0.0 | **0.985228** (= h2(3/7), T409's number) | 0.428571 |
| 1.0 | 0 / -1.220772 / 0.989743 | 3.4657 nats / 0.0 / 0.0 | 4.344994 | 0.198050 |
| 0.0 | 0 / -0.428571 / 0.989743 | 3.4657 nats / 0.0 / 0.0 | 4.985228 | 0.0 |

- Correlated uncopy erases nothing and REFUNDS work (consistent with a
  Landauer floor of zero); deletion-is-not-definalization re-asserted
  at every temperature (reset restores 0.0, residual 0.0).
- At finite temperature the joint holder entropy is thermal-noise
  dominated (4.34 bits at `beta = 1` vs 0.985 record bits at
  `beta = inf`) — reported side by side; bookkeeping, not a theorem.
- **Beyond the frontier** (`n = 4`, reach 2, `theta = pi`): feasible
  set EMPTY (certificates at machine floor), min cost `inf` — an
  empty-set infimum typed **access-not-work**, with the sharper
  finite-temperature statement: a work parameter now EXISTS in this
  model and is computed to be unable to substitute (leg 4); the
  infinity is still not a work divergence — departed carriers are
  outside the support of every retained-reach channel.

## Guardrails

- **Q1D (with teeth):** declared `(S, M)` record (unconditioned
  Z-distribution) invariant across all beta, theta, toggle, and `n`
  (machine floor); retained-reach protocols move outside-reach carrier
  marginals by 0.0 on the pre-trace joint state; the counterfactual
  enlarged protocol moves them by exactly `(3/7) tanh(beta/2)`:
  **0.428571** at `beta = inf` (T408/T409's tooth), 0.198050 at
  `beta = 1`, 0.0 at `beta = 0` — where the tooth is instead the
  restored-visibility jump (reach 3 of 4: 0.0; reach 4 of 4:
  0.989743), the leg-6 marginal blindness made explicit.
- **R1:** untouched. A reach frontier through an interaction sequence,
  not a light cone (Lieb-Robinson named as an absorber risk, from
  memory, unverified).

## Tests

`tests/test_thermal_collision_work_reach_frontier.py`: **48 passed**
(~15 s). Neighbor suites re-run green alongside in one invocation:
T409 (36), T408 (35), T393 (29), T392 (18), T142 (6) — **172 passed**
total, 46 s wall. Model run ~14–18 s. Predeclared budgets < 300 s each:
met with wide margin; no fallback needed. Deterministic; exact
density-matrix evolution cross-pinned to a thermofield statevector
purification (machine floor at the predeclared configuration); the only
sampling (Haar, seed `20260703`) is illustrative. Exhaustive retained
subsets: all `2^n` for `n <= 3` at all 30 sweep points (420 subset
cells); symmetry pruning at `n = 4, 5` asserted on 48 predeclared
pair-comparisons before any canonical-prefix use. First use of scipy in
`models/` (`scipy.linalg.expm`), disclosed in the spec and asserted
against the analytic block construction (machine floor).
Reproduction:

```bash
python -m pytest tests/test_thermal_collision_work_reach_frontier.py -v
python -m models.thermal_collision_work_reach_frontier
```

## What this does not earn

No continuum, weak-coupling, or transport theorem — the asymptotic
bath-dispersion statement, work BUYING reach (the physically
interesting substitution, which this model's certified and
undetermined bands still exclude or leave open respectively), and
spatial re-collection stay **named-unbuilt**. No thermodynamic theorem:
legs 1/5/8 are exact-identity-backed bookkeeping at the computed states
of a finite model (finite-witness; "exhaustive" used only for the
literal all-`2^n` blocks at `n <= 3`). No unconditional discharge of
T407's declared-vs-physical objection: departure-by-trace is the
standard reservoir idealization, adopted, not derived — a hostile
reviewer may still relocate the boundary by rejecting the model class,
and the verdict language concedes this. No new mathematics or physics:
every assembled fact is presumed standard (collision-model
thermodynamics, Esposito–Lindenberg–Van den Broeck identity,
hazy-environment Darwinism, EGY duality — all flagged from memory,
unverified); the claimed residue is the assembled,
certificate-disciplined object, and the spec's re-scope clause stands
ready if verification shows even the assembly is standard. No hardware
or platform. No CLAIM-LEDGER movement; TESTS.md untouched (new
T-number availability noted in the header of this file only). Hostile
review QUEUED, not survived. All promotion decisions pause for Joe.

---

## Addendum (2026-07-02): adapter-test gauntlet reached this rung

The four-absorber adapter gauntlet run against the T411 discriminator
built on this model also named T410's load-bearing objects directly. Run
record: `steward/runs/2026-07-02-physical-boundary-swing.md`; T411
addendum in
`results/T411-departed-record-capability-discriminator-v0.1-results.md`.
This addendum relabels; the original text above is preserved unedited.

The **decoherence-bookkeeping absorber (verdict: absorbed)** reduces this
rung's load-bearing objects to standard open-system accounting: the
per-copy visibility `f = cos(theta/2)` is the textbook mixed-state
decoherence factor; the leg-1 identity `Sigma = dS + beta Q = I + D` is
the Esposito-Lindenberg-Van den Broeck identity (worst `|Sigma - (I+D)|`
7.8e-16 on the finite-`beta` sweep); the switched Hamiltonian buys
standard collision-model thermo bookkeeping, not a dynamically-forced
boundary. Critically, the departure mechanism — `prepare_retained` traces
a carrier iff `i not in retained` — is a partial trace keyed on a
STIPULATED retained set: the reservoir idealization, **declared, not
dynamically forced.** At the model-class level this **fires the
`boundary_physicality_reduces_to_declaration` failure leg**: the
T409 -> T410 "physical rather than declared" ambition is not achieved
here. This is consistent with, and sharpens, this file's own conditional
"adopted, not derived" language; T407's declared-vs-physical objection is
not discharged at this rung either.

No computed quantity, leg verdict, or threshold is affected — the
finite-witness content (the two-way entropy identity, the temperature-blind
integer frontier, the refund ledger, the certificate transfer) reproduces
exactly as recorded. What is relabeled is the standing: this rung is a
repo-internal calibration of the certificate/ledger toolkit on a standard
thermal quantum-Darwinism collision family, not a physically-forced
boundary. The transport rung (work literally buying reach) stays
named-unbuilt. No claim promotion; no CLAIM-LEDGER / TESTS.md edits;
ledger actions pause for Joe.
