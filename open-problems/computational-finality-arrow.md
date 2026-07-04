# Computational Finality / A Computational Arrow of Time (frozen problem statement)

## Status

**Open problem - D2 first swing recorded as T419 v0.1 with REDESIGN verdict.**
This scopes the one direction the divergent persona pass (2026-07-02,
`papers/drafts/prior-art-verification-and-divergent-direction-pass-2026-07-02.md`)
flagged as the least-covered and most-plausibly-novel angle in the E2 mode of the
adopted taxonomy (`technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`).
The novelty bar and kill criteria below were fixed before the fixture. T419 does
not clear them: K4 fires on the exhibited toy orbit. No claim promotion; ledger
untouched; next redesign/abandon decision pauses for Joe.

## The question

Can a **finality / capability boundary** be forced by **computational hardness under
a standard cryptographic assumption** — such that the record is *information-
theoretically fully present and reversible in principle*, yet *computationally
locked* for any feasible agent — and is this a **distinct** kind of arrow from the
thermodynamic and complexity-growth arrows?

Slogan: **a cryptographic arrow of time** — finality that is real *relative to a
one-way-hardness assumption*, not to entropy growth or to complexity growth.

## Lineage (E2 mode)

- **T417** (`results/T417-computational-finality-boundary-v0.1-results.md`) already
  built the static object: a Goldwasser–Micali datum co-present in `(x,N)` but
  feasibly-hard to recover without the trapdoor; boundary physical conditional on
  QRA/factoring, family-level. D2 asks whether this yields a **temporal** statement
  — an *arrow* (past/future asymmetry of feasible recoverability), not just a
  static boundary.

## Prior art already checked (2026-07-02 pre-check) — the novelty bar

The broad "complexity and the arrow of time" space is **crowded**; D2 must
differentiate from all of these or it is not novel:

- **Brown–Susskind, "Second Law of Quantum Complexity" (arXiv:1701.01107).**
  Complexity grows — but *symmetrically* (toward past and future). D2 is **not** a
  complexity-growth statement; it is a *one-way feasible-recoverability asymmetry*.
- **Lesovik et al., reversal on IBM Q (arXiv:1712.10057).** Spontaneous reversal is
  exponentially *improbable* — a statistical/thermodynamic framing. D2 is **not**
  about probability of spontaneous reversal; it is about *conditional computational
  hardness under a named assumption*, with the information fully present.
- **Crutchfield–Ellison, "Time's Barbed Arrow" / crypticity.** Information hidden in
  a process's causal states (computational mechanics / ε-machines). D2 is **not**
  crypticity; it is *cryptographic* hardness (one-way functions), a different notion
  of "hidden."
- **Wolpert, stochastic thermodynamics of computation; Bennett.** Thermodynamic
  *cost* of computation — that is the **E1/thermodynamic** mode, not E2.

**Novelty survives only if** the claim is specifically: *an
information-theoretically-recoverable-but-computationally-locked finality/arrow,
conditional on a cryptographic hardness assumption, provably distinct from the
thermodynamic (E1) and complexity-growth (Brown–Susskind) arrows.* Anything broader
is already taken.

## Success criteria (a swing succeeds only if)

1. A finite/finite-family fixture where a record's forward direction is feasibly
   computable but its recovery ≡ inverting a one-way function / a standard hardness
   assumption (built on T417), **exhibiting a temporal asymmetry** (an arrow), not
   just a static boundary.
2. An explicit separation showing the boundary is **information-theoretically
   trivial** (the datum is present; reversal exists in principle) yet
   **computationally forced** — i.e. it is E2, not E1 and not E0.
3. A stated argument that this arrow is **distinct** from Brown–Susskind complexity
   growth (asymmetric feasible-recovery, not symmetric complexity) and from the
   thermodynamic arrow (no entropy/erasure needed).

## Kill / demotion criteria

- The construction reduces to a thermodynamic cost (E1) or to Landauer erasure →
  not a new arrow, just E1.
- The asymmetry is actually symmetric complexity growth (Brown–Susskind) → absorbed.
- The "hardness" is stipulated rather than a reduction to a standard assumption →
  E0 (declared) in disguise.
- The temporal content is only the static T417 boundary relabeled "past/future"
  with no dynamical asymmetry → no arrow, demote to T417.
- Prior art turns up a clean statement of exactly this (a cryptographic arrow of
  time with these properties) → cite and demote to synthesis.

## First swing boundary

A finite dynamical fixture was built: a forward-easy / backward-hard record
evolution keyed on a one-way construction, with the three success separations above
computed against the taxonomy's E0/E1 absorbers. Its recorded verdict is REDESIGN,
because the toy orbit is short-cycle reversible by public forward iteration and
therefore fails the anti-relabel guard.

No North Star, canon, public-posture, cross-repo, or ledger movement. GU/TI remain
stress-test input only.

---

## Swing outcome — 2026-07-02 (T419 v0.1, recorded-tier, REDESIGN)

The D2 swing was built and hostile-reviewed (provisional **T419**; TESTS.md and
CLAIM-LEDGER.md untouched; no promotion). Artifact and full leg/verdict record:
`results/T419-computational-arrow-of-time-v0.1-results.md`; spec
`tests/T419-computational-arrow-of-time.md`; model
`models/computational_arrow_of_time.py`.

**Construction built:** Rabin/BBS squaring permutation `F(x)=x² mod 77` on `QR_77`
(15 elements, bijection since `|QR_N|` odd), orbit from seed 4 with emitted BBS bit
record.

**Verdict: REDESIGN — a kill fired.** Six-probe adversarial panel:
- **K1 thermodynamic/E1** — DID NOT FIRE (survives, 0.85): verified zero Landauer
  erasure (bijection on `QR_77`); Bennett reversibility makes backward-hardness a
  time-complexity, not erasure, cost. Cleanest surviving separation (E2 vs E1/Wolpert).
- **K2 Brown–Susskind** — PARTIAL (0.62): the *exhibited* object is time-symmetric,
  reversible, short-Poincaré-recurrent; the intended one-way distinction survives only
  at unexhibited cryptographic scale.
- **K3 stipulated-hardness/E0** — DID NOT FIRE (survives, 0.78): Rabin (1979)
  sqrt≡factoring is a genuine reduction, not fiat; rigor defect noted (reduction
  omits an `r²==a` check, confounded at toy `N`).
- **K4 static-T417-relabel** — **FIRED (breaks, 0.90).** The original anti-relabel
  guard (Leg 6) was fabricated: `backward_feasible_without_trapdoor` was hardcoded
  `[]`, false on the period-4 orbit where `F⁻¹=F³` recovers every predecessor
  trapdoor-free. The committed T419 model now computes this failure directly.
  Evaluating the static
  square-root boundary along a time index is literally the relabel K4 forbids; the
  emitted bit-stream is also period-4, so cited BBS forward-security is vacuous here.
- **K5 prior-art** — PARTIAL (0.70): core concept largely pre-empted by reversible-CA
  public-key cryptosystems (Kari 1990 line) and Towell, "The Beautiful Deception"
  (arXiv:2510.12802, 2025), which states the trapdoor "arrow of time" idea directly;
  the fixture's full differentiated packaging is not cleanly published, so residual
  value is **synthesis/differentiation only**.
- **Correctness** — survives (0.90): every number independently re-derived; `12
  passed`; no numeric or logic error. The defect is the *mechanism story*, not the
  arithmetic.

**Consequence.** T419 as built does **not** clear the D2 novelty bar: it exhibits a
time-symmetric reversible-recurrent dynamics, not a distinct computational arrow. The
break is in the *exhibition* (toy `N`, short discoverable cycle, failed guard), not
proven fatal to the *intended* construction, so **REDESIGN** — the identified fix is
to relocate the hardness from point-square-root to **period-finding** (hard without
factoring at scale) and honestly concede the arrow is not executably exhibitable at
toy scale. **ABANDON fallback:** if a redesign cannot restore an executable per-step
asymmetry (likely impossible for a finite permutation on a toy), the K4 demotion
consequence governs — **demote to T417**, and per K5 treat any survivor as synthesis,
not a novel result. The v0.1 results doc's original "no kill fired" verdict is
retracted. No claim promotion; ledger and next-step decision pause for Joe.

---

## Guardrail outcome - 2026-07-02 (T420 v0.1)

T420 does **not** take the redesign/abandon decision. It formalizes the finite-cycle
anti-relabel gate created by T419's K4 failure:
`results/T420-finite-cycle-anti-relabel-gate-v0.1-results.md`; spec
`tests/T420-finite-cycle-anti-relabel-gate.md`; model
`models/finite_cycle_anti_relabel_gate.py`.

**Guardrail:** on a closed finite public permutation, if a state lies on a cycle of
length `L`, its predecessor is recovered by public forward iteration:

```text
predecessor(y) = F^(L-1)(y)
```

Applied to T419's `QR_77` squaring permutation, every cycle is publicly reversible
within at most three forward steps; the seed-4 orbit is `4 -> 16 -> 25 -> 9 -> 4`,
so the predecessor of `4` is `9` by `F^3` without trapdoor. A bounded long-cycle
control shows that failure inside a small search bound is not arrow evidence by
itself; it is only a pointer to the need for a declared family-level period-hardness
assumption or a different regime.

**Consequence for any later D2 redesign:** it cannot rely on a toy finite public
cycle. It must declare and defend family-level period hardness, change the agent's
public transition knowledge, leave the closed public-permutation regime, or demote
the temporal story to T417's static E2 boundary. No claim promotion; ledger and the
redesign/abandon decision still pause for Joe.

---

## Admission-gate outcome - 2026-07-03 (T438 v0.1)

T438 still does **not** take the redesign/abandon decision. It converts T420's
post-redesign rule into a reusable E2 packet classifier:
`results/T438-e2-period-hardness-admission-gate-v0.1-results.md`; spec
`tests/T438-e2-period-hardness-admission-gate.md`; model
`models/e2_period_hardness_admission_gate.py`.

**Gate:** future D2 work is admitted only as a predeclared family-level
period-hardness redesign packet. It must name the family, security parameter,
closed public-permutation regime, fixed public transition, period/reversal
problem, named hardness assumption or theorem target, and predeclared reduction
or proof obligation.

The gate rejects finite public cycles, bounded non-recovery without a family
assumption, point-inversion-only static relabels, single-instance hard-theorem
claims, thermodynamic/E1 packets, Brown-Susskind-style symmetric complexity growth
packets, and post-hoc or hidden-selector packets. Changed-public-transition and
open/nonpermutation ideas are routed to a separate spec rather than admitted as
closed-public-permutation D2.

**Consequence for any later D2 continuation:** first supply the admitted
period-hardness packet fields. If that packet cannot be supplied, demote the
temporal story to T417's static E2 boundary. No claim promotion; ledger and the
redesign/abandon decision still pause for Joe.

---

## Separate-regime gate outcome - 2026-07-04 (T444 v0.1)

T444 still does **not** take the redesign/abandon decision. It makes T438's
"separate spec required" route executable for changed-public-transition and
open/nonpermutation packets:
`results/T444-e2-changed-transition-regime-gate-v0.1-results.md`; spec
`tests/T444-e2-changed-transition-regime-gate.md`; model
`models/e2_changed_transition_regime_gate.py`.

**Gate:** changed-transition or open/nonpermutation packets are admitted only as
separate-regime review targets if they freeze a family, security parameter,
access boundary where applicable, transition evidence, update/dynamics law,
public audit trail, capability-vs-ignorance distinction, forcing burden, and
predeclared reduction or theorem target.

The gate rejects post-hoc or hidden transition policies, thermodynamic/E1
packets, Brown-Susskind symmetric-complexity packets, pure epistemic ignorance,
unfrozen transition evidence, open packets with no dynamics law, and ordinary
resource/environment completion. Closed public-permutation packets route back to
T438.

**Consequence for any later non-T438 D2 continuation:** first clear T444 as a
separate-regime packet. T444 admission is not D2 redesign, D2 success, claim
support, crypto theorem, physics evidence, or public posture. No claim promotion;
ledger and the redesign/abandon decision still pause for Joe.

---

## Packet-swing outcome - 2026-07-04 (T446 v0.1)

T446 still does **not** take the redesign/abandon decision. It runs the first
recorded-tier positive packet swing after T438/T444:
`results/T446-e2-family-open-regime-big-swing-v0.1-results.md`; spec
`tests/T446-e2-family-open-regime-big-swing.md`; model
`models/e2_family_open_regime_big_swing.py`.

**Packet:** an open Rabin-lift chain. Given `x_t in QR(N_t)`, compute
`r_t = x_t^2 mod N_t`, then lift `x_{t+1} = r_t^2` as an integer QR element in
`N_{t+1}`, with `N_{t+1} > N_t^2`. The public transition, domain tags, and lift
law are frozen; the claimed forcing burden is Rabin square-root/factoring
hardness at the current Blum modulus.

**Verdict:** `E2_OPEN_RABIN_LIFT_PACKET_SURVIVES_SCREEN_WITH_T417_CHAIN_RESIDUAL_NO_D2_DECISION`.
The packet clears T438/T444 routing and survives the literal absorber screen:
open/nonpermutation dynamics, information-theoretic reversal, named hardness, no
E1 cost basis, no symmetric complexity-growth basis, and no hidden transition
policy. The toy arithmetic remains crackable and is used only to check algebra.

**Residual:** the strongest absorber is still that the hard part may be only
chained T417/Rabin static inversion. The next useful D2 move is to prove or kill
whether coupled open iteration adds any theorem beyond per-step Rabin inversion.
No claim promotion; ledger and the redesign/abandon decision still pause for Joe.

---

## Residual-audit outcome - 2026-07-04 (T448 v0.1)

T448 resolves the T446 residual for the current open Rabin-lift packet:
`results/T448-e2-chain-residual-factorization-v0.1-results.md`; spec
`tests/T448-e2-chain-residual-factorization.md`; model
`models/e2_chain_residual_factorization.py`.

**Verdict:** `T446_CHAIN_RESIDUAL_FACTORS_THROUGH_PER_STEP_RABIN_NO_NEW_D2_THEOREM`.
Full-chain recovery factors through public integer-square lift unwraps plus one
independent Rabin square-root inversion for each current modulus. A length-one
T446 chain already embeds the ordinary T417/Rabin inversion problem, and changing
the next lift domain while preserving lift room does not change predecessor
recovery.

**Consequence:** the current T446 open Rabin-lift chain is absorbed as chained
T417/Rabin inversion. This closes that positive route without abandoning D2. A
future D2 continuation must either return to T438's true family-level
period-hardness path or supply a different packet whose chain inversion is not
product-decomposable into public unwraps plus independent step inversions. No
claim promotion; ledger and the broader redesign/abandon decision still pause for
Joe.

---

## Period-hardness packet outcome - 2026-07-04 (T449 v0.1)

T449 returns to T438's closed public-permutation path after T448 closed the
open-chain route:
`results/T449-e2-period-hardness-packet-audit-v0.1-results.md`; spec
`tests/T449-e2-period-hardness-packet-audit.md`; model
`models/e2_period_hardness_packet_audit.py`.

**Verdict:** `E2_PERIOD_HARDNESS_PACKET_SHARPENED_TO_HIDDEN_ORDER_THEOREM_TARGET_NO_D2_DECISION`.
For BBS-style public squaring on `QR_N`, `F_N^t(x) = x^(2^t)`, and if
`d = ord_N(x)`, the orbit period is `L = ord_d(2)`. Once `L` is known,
predecessor recovery is public forward iteration `F_N^(L-1)`. In the toy family,
the formula matches public cycle discovery and known period recovers the
predecessor. Granting `|QR_N|` is trapdoor completion: with semiprime `N=p*q`,
`N` and `|QR_N|` recover `p,q`.

**Consequence:** the best remaining D2 route is now sharply typed as a
hidden-order / cycle-length theorem target with seed-distribution controls.
Small-period seeds collapse the route, and finite toy period discovery is not
hardness evidence. A future D2 continuation should not build another finite toy
unless it changes the theorem obligation; it should either formulate the exact
hidden-order cycle-length assumption/reduction/lower-bound burden or demote the
temporal route back to T417's static E2 boundary. No claim promotion; ledger and
the broader redesign/abandon decision still pause for Joe.

---

## Period-oracle trapdoor outcome - 2026-07-04 (T450 v0.1)

T450 stress-tests whether the T449 hidden-order period target is independent of
the T417/Rabin trapdoor:
`results/T450-e2-period-oracle-trapdoor-equivalence-v0.1-results.md`; spec
`tests/T450-e2-period-oracle-trapdoor-equivalence.md`; model
`models/e2_period_oracle_trapdoor_equivalence.py`.

**Verdict:** `PERIOD_ORACLE_COLLAPSES_TO_RABIN_TRAPDOOR_NO_INDEPENDENT_D2_ROUTE`.
For the current closed public-squaring route, an all-target period oracle is
trapdoor-strength. A target period gives the unique predecessor by public forward
iteration, and that predecessor oracle is the principal square-root oracle.
Rabin's square-root oracle reduction then factors `N`. Conversely,
group-order/factorization completion computes periods.

**Consequence:** the current closed public-squaring period route has no
independent finite-witness residue beyond the standard Rabin/factoring boundary.
D2 should continue only if a nonstandard period assumption is specified with
scope that avoids both single-seed weakness and all-target trapdoor equivalence.
Otherwise the temporal D2 route should be demoted to T417's static E2 boundary in
a separate governed decision packet. No claim promotion; ledger and the broader
redesign/abandon decision still pause for Joe.
