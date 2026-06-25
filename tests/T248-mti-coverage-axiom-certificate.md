# T248: an in-repo WBE/Moses CITATION CERTIFICATE for the terminal-reachability (space-filling SERVICE / coverage) constraint — MTI sub-object (2)

## Verdict: conditional

The terminal-reachability / coverage constraint that T238 implements **is an
in-repo cited West-Brown-Enquist / Moses space-filling SERVICE condition** — a
*constitutive* feasibility constraint of the WBE optimization, quoted verbatim from
the repo's own canonical Moses-framework writeup, stated **independently of** the
metric-vs-causal separation it licenses, and shown **load-bearing** by a decisive
falsification control. This resolves T233 sub-object (2) — the T238 half — in the
**positive direction**: T238's "every terminal must be reached" is no longer an
*uncited interpretive premise* but a **cited WBE/Moses coverage axiom** with a real
in-repo source. It is structurally analogous to T243's area-preserving /
reflectionless certificate (MTI sub-object 1) but **disjoint** from it; this lane
touches only the delivery / coverage half and does not close T243's citation gap.

This is `conditional`, **not** `closed`, for one explicitly named reason, and it
does **NOT** promote MTI:

1. **The upgrade is premise→cited-axiom, not premise→theorem.** The cited
   condition is a real, constitutive WBE/Moses statement in the repo's MTI line
   (it sits in the `subject to:` clause of the WBE optimization, and the repo
   itself equates space-filling with "all sites accessible"). That elevates the
   delivery half from *uncited premise* to *cited axiom*. It is not a derivation
   of coverage from a deeper TaF object; a reviewer who rejects the WBE/Moses
   service-hierarchy reading entirely can still decline the axiom. So the
   `conditional` collapses to a citation acceptance, not an open computation —
   the same kind of boundary T243 reports, but for the coverage half only.
2. **MTI promotes only when BOTH halves land.** This lane delivers the coverage
   / delivery-objective half (sub-object 2). The area-preserving 3/4 half
   (sub-object 1, T243) is the disjoint other half. MTI stays
   PARTIALLY_SUPPORTED; promotion is the integrator's call, not this lane's.

Recommendation to integrator: record that T233 sub-object (2) is now
**conditionally discharged** (T238's terminal-reachability constraint is the
in-repo cited WBE/Moses space-filling SERVICE axiom, non-circular, load-bearing,
and structurally analogous to T243); keep MTI PARTIALLY_SUPPORTED. T243's
area-preserving / reflectionless premise still needs its own citation-acceptance
or citation-certificate step before any joint MTI promotion.

Tags: `finite_witness` (the finite Alpha/Beta fixtures + finite D-sweep imported
from T238; NO continuum theorem) + `poly_decider` (re-uses T238's finite
floored-simplex scan; the certificate itself is a finite citation/structure
audit — NO hidden search, NO hardness / NP / scale claim).

## What Was Derived From Sources (IMPORT ONLY)

- From **T238** (`models/wbe_coverage_constrained.py`, IMPORT ONLY):
  `all_terminals_reachable`, `coverage_constrained_delivery`, `coverage_quantum`
  (the network-fixed floor `q = demand/K^2`), `decide_objective_invariance`, and
  `feasible_bound` (the network-fixed `D_min = max free time`). Imported
  verbatim; the T238 file is **not modified** and its suite stays green
  (asserted by a subprocess check in this lane's test).
- From **T227** (`models/mti_wbe_continuum.py`, IMPORT ONLY): the Alpha/Beta
  fixtures and the *unconstrained* `solve_total_cost` / `solve_minimax` screens —
  used to reconstruct the **objective-DEPENDENT** baseline (T227's horn) that the
  coverage axiom escapes. Not re-tuned, no new physics.
- From the repo's canonical **Moses-framework writeup**
  (`explorations/explorer-metabolic-scaling-energy-time-transport-networks-2026-06-22.md`,
  cited by `claims/MTI-metabolic-temporal-irreducibility.md`): the real,
  in-repo constitutive coverage condition this certificate stands on (quoted
  below). The test **re-reads this file** and asserts each cited line is
  literally present — the binding honesty guard that the axiom is *cited*, not
  fabricated.
- **No new physics.** Only the canonical M/M/1 congestion delay already in
  T238/`mti_cflow_solver.py` enters, via import. No Poiseuille re-derivation, no
  exponent claim (out of scope here — that is the disjoint T243 half), no
  GR/QFT/spacetime/curvature/new-law language.

## Strongest Positive Result

**A real, in-repo WBE/Moses constitutive coverage condition — quoted verbatim,
stated as a CONSTRAINT not a conclusion — that is exactly the T238
terminal-reachability constraint, with a decisive falsification control proving
it is load-bearing.**

The cited axiom (`COV-AXIOM`): *the WBE/Moses transport network is a
constrained optimization whose feasibility clause requires it to space-fill the
serviced volume, i.e. to make every terminal/site reachable — coverage of every
terminal is constitutive, not an optional add-on to the dissipation objective.*

Its four load-bearing source quotes (all verified literally present in the
source file):

```
"subject to: network fills volume V; terminal units have fixed size"   (the optimization's CONSTRAINT clause — coverage is not the objective)
"distributed from central supply to distributed demand"                (the network's reason to exist: deliver to every demand site)
"Coverage requirement (all sites accessible)"                          (the repo's OWN equation of WBE space-filling with terminal coverage)
"Moses derives 3/4 from 3D space-filling branching with fixed terminal size"   (the WBE result itself is derived UNDER coverage)
```

The certificate verdict (run captured in `results/mti-coverage-axiom/T248-results.json`):

```
citation: all 4 quotes present in source         True
PART A  axiom stated independently of separation  True
PART B  cited axiom IS the T238 constraint        True   (full-coverage reachable=True; abandoning a terminal violates=True)
PART C  falsification control decisive            True
        WITH axiom : minimax sep=True  total-cost sep=True  invariant=True
        WITHOUT    : total-cost sep=True  minimax sep=False  objective-DEPENDENT=True
PART D  same shape as T243                         True
PART E  non-vacuity (harness can report NOT-EARNED) True
PART F  feasibility / quantum->0 guards            True
CERTIFICATE HOLDS                                  True
```

**Mechanism (the decisive falsification control, PART C):** with the cited
coverage axiom **present** (T238's regime, by import), the metric-vs-causal
separation is **objective-INVARIANT** — minimax *and* total-cost both separate.
**Drop** the cited coverage axiom and the separation **reverts to T227's
objective-DEPENDENT horn**: total-cost still separates, but minimax does **not**
(it zeroes the slow terminal, hiding the metric label). So the cited coverage
axiom is the *only* thing that flips minimax from non-separating to separating —
it does real, separable work and is not a renamed result. This is the exact
analogue of T243's "drop reflectionless → revert to `n^{-1/3}`" control.

**Non-circularity (PART A):** the axiom statement mentions none of
{separation, minimax, total-cost, objective-invariant, beta, 0.75, 3/4,
exponent}. It is a pure statement about what the WBE network must *do* (service
every terminal it fills), so it cannot be question-begging.

**Same structural audit shape as T243 (PART D):** this lane has the same pattern
T243 used — an independently stated constitutive premise plus a decisive
drop-the-premise falsification control. T248 certifies the coverage citation only;
it does not certify T243's area-preserving citation gap.

**Non-vacuity (PART E):** the harness catches (1) a *fabricated* axiom whose
"quote" is absent from the source file, and (2) a *circular* axiom phrased via
the separation. Both are rejected — the certificate CAN report the negative
verdict, so its PASS is meaningful. A dedicated test also forces
`quotes_present_in_source=False` and confirms the certificate then does **not**
hold (the citation is load-bearing, not cosmetic).

**Feasibility / quantum→0 (PART F, inherited from T238):** the coverage quantum
is positive and shrinks with the service fraction (the verdict is not carried by
a large floor); the delivery bound reports infeasibility below the network-fixed
threshold `D_min` and feasibility above it (a real physical bound, not a fiat
number).

## First Exact Obstruction / Missing Object

The result is positive, so the obstruction is the **named boundary of the
conditional**, not a failure inside it:

> **The cited condition is a constitutive WBE/Moses axiom, accepted by citation,
> not a TaF theorem.** "The WBE network must service every terminal it
> space-fills" is quoted from the repo's own canonical Moses-framework writeup
> (it lives in the `subject to:` clause of the optimization, and the repo
> equates space-filling with "all sites accessible"). It is argued independently
> of the separation and does real, falsifiable work. But it is a **cited domain
> axiom**, not derived from a deeper TaF object. A reviewer who rejects the
> WBE/Moses service-hierarchy reading wholesale (holding the WBE optimization to
> be unconstrained dissipation minimization with *optional* coverage) can still
> decline the axiom and route to the T227 minimax horn. The missing object — were
> one to push past `conditional` to `closed` — is a *derivation* of the coverage
> requirement from the underlying transport object, not merely its citation.

This is structurally similar to T243's open obstruction, but it is not the same
completion status: T243's reflectionless premise remains a defensible interpretive
premise awaiting its own citation certificate or citation-acceptance step.

## Constructive Next Object

With coverage now elevated from uncited premise to **in-repo cited WBE/Moses
axiom**, the constructive next object is T243-side citation acceptance: obtain or
reject the area-preserving / reflectionless axiom certificate before any joint
promotion decision. If either citation is contested, the corresponding half
demotes to its T227/T233 horn. Beyond citation, the single remaining mathematical
object that would move
either half from `conditional` to `closed` is a **derivation** (not a citation)
of the constitutive condition from the typed transport object — for coverage,
a proof that terminal-reachability is forced by the D1 transport graph's own
service structure rather than imported from the WBE service-hierarchy reading.

## Meaning For The Claim

- **MTI sub-object (2) is conditionally discharged.** T238's
  terminal-reachability constraint is an in-repo cited WBE/Moses space-filling SERVICE
  axiom — non-circular, load-bearing (decisive falsification control), and the
  same structural audit pattern as T243's area-preserving certificate. This is strictly
  stronger than T238 left it: T238 had the constraint as an *uncited
  interpretive premise*; T248 supplies the real in-repo citation and proves the
  cited axiom matches T238's finite constraint, with the harness able to report the
  negative.
- **MTI stays PARTIALLY_SUPPORTED.** This lane does not promote it. The remaining
  MTI gap on this branch is T243's reflectionless premise (sub-object 1),
  which still needs its own citation acceptance/certificate. Promotion requires both
  halves and is the integrator's call.
- **Absorbers named.** The *unconstrained* minimax/equal-load convex
  optimization (T201/T227) still absorbs the *unconstrained* separation (it
  zeroes the slow terminal). The West total-cost objective preserves it. The
  **coverage-constrained** problem is preserved by **both** objectives — and the
  residue that survives every objective is now the separation itself, owned by
  no mature neighbor: the cited space-filling SERVICE condition is the WBE
  model's *own* constitutive constraint, not an imported scheduling add-on.
- **No physics promotion.** A finite citation/structure audit over T238's finite
  congestion-flow fixture. Every quantity is a finite computed value or a
  literal source quote; no continuum theorem, no hardness/scale claim, **no
  coverage-as-physical-law and no exponent-as-law promotion** (`finite_witness` +
  `poly_decider`). The 3/4 exponent is explicitly OUT OF SCOPE (the disjoint
  T243 half).

## Known Physics Constraints

Physics in scope but bounded: only the canonical M/M/1 congestion delay
`delay(load) = tau/(1 - load/capacity)` already in T238 / `mti_cflow_solver.py`,
entering by import. The coverage / terminal-reachability condition is the
West-Brown-Enquist / Moses space-filling SERVICE
constraint, cited verbatim from the repo and stated physically (every terminal
perfused within a finite delivery bound), **not** promoted to a universal law.
No GR/QFT/spacetime/curvature/gravity language; no exponent claim is made in this
lane.

## Failure / Falsification Conditions

- **Demote this result to T227's horn** if the cited WBE/Moses space-filling
  SERVICE condition is rejected as constitutive — i.e. if the WBE optimization is
  held to be unconstrained dissipation minimization with *optional* coverage.
  Then the separation reverts to objective-DEPENDENT (minimax kills it) and MTI's
  metric content demotes per T233's falsification clause.
- **Invalidate T248** if any of: (a) a cited quote is **not** literally present
  in the source file (it is — all 4 verified by file read); (b) the axiom
  statement mentions the separation / objective / exponent it licenses (it does
  not); (c) the cited axiom is **not** the T238 constraint on the fixture (it is:
  full coverage reachable, abandoning a terminal violates); (d) the falsification
  control is **non-decisive** — i.e. dropping coverage does NOT revert minimax to
  non-separating (it does: `without_axiom_minimax_separates=False`); (e) the
  non-vacuity injector fails to catch a fabricated or circular axiom (it catches
  both); or (f) the imported T238/T243/T233 suites are not green (they are —
  subprocess-verified).
- **Promote MTI** (separate, integrator-only) only after this coverage-axiom
  certificate is accepted and T243's area-preserving / reflectionless premise gets
  its own citation acceptance or citation certificate under domain-native inputs.

## Artifacts

- `models/mti_coverage_axiom_certificate.py` — the cited `CoverageAxiom`
  (`CITATION_SOURCE`, `CITED_QUOTES`); the independence guard
  (`axiom_stated_independently_of_separation`); the binding identification
  (`axiom_matches_t238_constraint`); the decisive falsification control
  (`falsification_drop_coverage`); the same-shape-as-T243 audit
  (`same_shape_as_t243_audit`); the non-vacuity injector (`non_vacuity_injector`);
  the feasibility / quantum→0 guards (`feasibility_guards`); and the combined
  `build_certificate`. IMPORTS T238 / T227 models verbatim; touches NO kappa /
  sheaf-H1 / attribution / d1cat / functor files.
- `tests/test_mti_coverage_axiom_certificate.py` — 15 real checks (green): cited
  quotes literally present in source (file read); the `subject to:` constraint
  clause + "all sites accessible" present; axiom stated independently; circular
  axiom rejected; cited axiom is the T238 constraint; falsification control
  decisive; dropping coverage reverts to the T227 minimax horn; same shape as
  T243; non-vacuity injector catches fabricated + circular axioms; fabricated
  quote really absent; certificate fails when quotes absent; feasibility guards;
  combined verdict holds; **imported T238/T243/T233 suites stay green
  (subprocess)**.
- `results/mti-coverage-axiom/T248-results.json` — recorded verdict + all booleans.

## Next Proof / Computation Step

1. Integrator: keep MTI PARTIALLY_SUPPORTED until T243's area-preserving /
   reflectionless premise gets its own citation acceptance or citation certificate;
   then decide joint promotion only if both halves are accepted.
2. Independently (to move either half from `conditional` to `closed`): derive the
   constitutive condition from the typed transport object rather than citing it —
   for this half, prove terminal-reachability is forced by the D1 transport
   graph's own service structure.
3. MTI promotes past PARTIALLY_SUPPORTED only when the coverage citation and the
   T243-side area-preserving / reflectionless citation are both accepted under
   domain-native inputs; this lane delivers only the coverage / delivery-objective
   half.

## Registered Status

T248 RUN as of 2026-06-25. Implementation, results, and 15 green checks under
the worker's slug namespace (`models/mti_coverage_axiom_certificate.py`,
`tests/test_mti_coverage_axiom_certificate.py`,
`results/mti-coverage-axiom/T248-results.json`). Imports T238 / T227 models
verbatim (their suites verified green: T238 + T243 + T233 = 48 passed); does NOT
edit kappa, sheaf-H1, attribution, functor, or d1cat-colimit files; does NOT
edit CLAIM-LEDGER.md, ROADMAP.md, or MATHEMATICAL-INDEPENDENCE-AUDIT.md. Registered
in TESTS.md by the integration pass. Report at test level; MTI promotion deferred
to integrator.
