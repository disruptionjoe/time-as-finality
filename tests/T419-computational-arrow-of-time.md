# T419 — Computational Arrow of Time (spec, frozen)

**Status:** exploratory big-swing on the D2 open problem
(`open-problems/computational-finality-arrow.md`) — the *temporal lift* of T417's
static E2 computational-finality boundary into a genuine **arrow** (past/future
asymmetry of feasible recoverability). Mode **E2** of the adopted taxonomy
(`technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`).

Provisional T-number **T419** (**TESTS.md NOT edited**; CLAIM-LEDGER.md NOT
edited; noted here in the results header only; registration + any promotion pause
for Joe). No claim promotion; recorded-tier. Cross-domain material (cryptography /
number theory) is the **object of study**, never evidence for physics or any
sibling repo. Single-process ceiling in force. Spec frozen **before** the model
file. Hostile review to follow.

## The D2 question

Can a **finality / capability boundary** be forced by **computational hardness
under a standard cryptographic assumption** — such that the record is
*information-theoretically fully present and reversible in principle*, yet
*computationally locked* for any feasible agent — and is this a **distinct** kind
of arrow from the thermodynamic (E1) and complexity-growth (Brown–Susskind)
arrows? T417 built the static object; D2 asks for a **temporal** statement: an
arrow over an actual iterated dynamics, not a static `(x, N)` datum relabelled
past/future.

## Chosen construction (Rabin/BBS squaring permutation on QR_N of a Blum integer)

Reuse T417's `N = 77 = 7·11` (a **Blum integer**: `p ≡ q ≡ 3 mod 4`). Work on the
group of quadratic residues `QR_N`. The forward transition is one modular
squaring `F(x) = x² mod N`.

- **Permutation / entropy-neutral.** Because `|QR_N| = φ(N)/4` is **odd** for a
  Blum integer, `F` is a **bijection** of `QR_N` onto itself. Squaring is a genuine
  permutation ⇒ **zero Landauer erasure**, no reservoir, constant description
  length, **nothing grows**. `|QR_77| = 15`.
- **Orbit + emitted record.** From a seed `x_0 ∈ QR_77`, iterate
  `x_0 → x_1 → … → x_T` (`T = 8`) and emit a **BBS bit** `b_t = lsb(x_t)` at each
  tick. The *record* is the tick-indexed **trajectory plus the emitted bit
  stream**, NOT a static pair.
- **Forward-easy, FLAT.** A forward step is **1 modmul** using only `N`; cost is
  flat in `t` and polylog in `|N|`. Any reach agent extends both the orbit and the
  bit-record arbitrarily far forward with `N` alone.
- **Co-presence / reversal exists.** Each state has a **unique** predecessor; the
  trapdoor computes the **principal square root** via CRT (the unique root that is
  itself a QR), recovering the exact recorded `x_{t-1}` at every `t`. Datum
  present; reversal certain.
- **Backward-hard = FACTORING (a reduction, not a stipulation).** A backward step
  is a principal square root mod `N`, which by **Rabin (1979)** is polynomial-time
  **equivalent to factoring `N`** — exhibited executably: a sqrt-oracle yields a
  nontrivial factor of `N` (pick `w`, compare `sqrt(w²)` to `±w`, `gcd`). The
  decision-flavor wall is the **Quadratic Residuosity Assumption** (Goldwasser–
  Micali 1982) on the emitted bits — T417 Leg 2 lifted onto the time axis — with
  **Blum–Blum–Shub (1986)** forward-security ("cannot compute previous
  states/bits"). Cited, **not** proven.
- **Trapdoor resymmetrizes (E2, purely computational).** With `(p,q)` the agent
  computes backward in polylog at every step ⇒ **symmetric** cone. Without `(p,q)`
  ⇒ **asymmetric** cone. The arrow is **agent-relative to trapdoor possession** —
  a computational wall, not thermodynamic and not intrinsic.

The RSW/VDF **sequentiality** route (candidate 3) is **deliberately declined** as
the spine (it cannot be reduced to factoring — a fresh conjecture, the exact
E0-in-disguise smell the kill criteria hunt) and noted only as an optional future
extension. The RSA framing (candidate 1) is declined (RSA is not a reduction to
factoring, and a "monotone-growing infeasible past" invites the Brown–Susskind
kill). The arrow is stated purely as the consistently-oriented, forward-**FLAT**
per-step invertibility asymmetry — with **no growing monotone**.

## Fixed constants (predeclared)

`N = 77 = 7·11`; Blum (`7 ≡ 11 ≡ 3 mod 4`). `|QR_77| = 15`. Seed `x_0 = 4 ∈ QR_77`;
`T = 8` ticks. Cost-growth family of Blum semiprimes
`[21, 77, 209, 713, 2537, 8549]` from pairs
`(3,7),(7,11),(11,19),(23,31),(43,59),(83,103)` (all `≡ 3 mod 4`).

## Predeclared SUCCESS legs (verdicts fixed before running)

1. **PERMUTATION / entropy-neutral.** `F(x)=x² mod N` is a bijection on `QR_N` for
   the Blum integer (`|QR_N|` odd); `sorted(F over QR_N) == sorted(QR_N)`.
   Establishes zero erasure and success-criterion-2 (reversal exists in principle).
2. **CO-PRESENCE.** Along `x_0..x_T` every state has a unique predecessor; the
   trapdoor CRT principal-sqrt recovers the exact recorded `x_{t-1}` at every `t`.
3. **FORWARD-EASY-FLAT.** Forward step = 1 modmul using only `N`; `forward_reach`
   is `O(k)`; cost flat in `t` and polylog in `|N|`; the emitted BBS bit-record is
   extendable forward by any reach agent.
4. **BACKWARD-HARD-BY-REDUCTION.** Backward step = principal sqrt mod `N`; the
   **Rabin reduction is exhibited executably** (a sqrt oracle yields a nontrivial
   factor of `N`), so backward ⇒ factoring (not stipulated); the trapdoor-free
   past-bit predicate = Jacobi (`+1`, uninformative), Legendre-with-`(p,q)`
   recovers it (QRA) — T417 Leg 2 on the time axis.
5. **TRAPDOOR-RESYMMETRIZES.** With `(p,q)` backward is polylog at every step
   (symmetric cone); without it, asymmetric cone. The wall is E2/computational and
   agent-relative, not intrinsic or thermodynamic.
6. **TEMPORAL-ASYMMETRY-OVER-ORBIT (anti-relabel).** At several `t` on the SAME
   iterated orbit, the forward-reachable set is poly-enumerable while the
   backward-feasible set is empty without the trapdoor; the record extends forward
   for anyone but reconstructs backward only with the trapdoor. Asymmetry is a
   per-step property of the transition map; forward cost FLAT; **no growing
   monotone**.
7. **COST-GROWTH-FAMILY.** Blum semiprimes of increasing bit-length;
   `forward_step_ops` flat, `backward_without_trapdoor_ops` strictly increasing
   (mirrors T417's `[2,6,10,28,58]` shape), `backward_with_trapdoor_ops` polylog;
   honest note that trial division is illustrative and the basis is factoring/QRA.
8. **KILLER-PREMORTEM table.** The four kills each answered with its executable
   dodge, mirroring T417 Leg-4.

## Predeclared KILL / demotion legs (reportable verdicts)

- **K1 THERMO/E1.** TRUE and demote if any step erases/overwrites information
  irrecoverably, uses a reservoir/partial-trace, or backward cost is billed in
  `kT ln2` rather than arithmetic operations. *Guard:* the permutation leg ⇒ zero
  erasure.
- **K2 BROWN–SUSSKIND.** TRUE and demote if the claimed arrow is actually a
  symmetric growth of a state-complexity quantity toward both directions, OR if
  the fixture RELIES on any monotone-growing quantity. *Guard:* constant
  description length; nothing grows; asymmetry is per-step forward-vs-inverse cost
  with forward FLAT.
- **K3 STIPULATED-HARDNESS/E0.** TRUE and demote if backward-hardness is declared
  by fiat, or the past is recoverable by any admissible enlargement short of the
  genuinely-absent trapdoor `(p,q)`, or the hardness is NOT reduced to a named
  standard assumption. *Guard:* Rabin sqrt≡factoring THEOREM exhibited executably +
  QRA; only `(p,q)` crosses.
- **K4 STATIC-T417-RELABEL.** TRUE and demote to T417 if the temporal content is
  only the static `(x,N)` datum relabelled past/future with no per-step dynamical
  asymmetry over an actual iterated orbit. *Guard:* real orbit with time index,
  emitted BBS record stream, per-step transition-map cost asymmetry at multiple `t`.
- **K5 PRIOR-ART.** TRUE and demote to synthesis if a clean published
  "cryptographic arrow of time" with these exact properties surfaces on
  adversarial search.

## Hardness assumption (named, standard — a reduction, not a stipulation)

Integer-factorization hardness of Blum integers, entered in two named forms:
(a) **Rabin (1979)** — extracting principal square roots mod `N` is polynomial-time
equivalent to factoring `N`, so one backward step is provably as hard as factoring
(the E0-dodge, exhibited executably by a sqrt-oracle → factor extraction on the toy
`N`); (b) the **Quadratic Residuosity Assumption** (Goldwasser–Micali 1982)
governing unpredictability of the emitted BBS bits (the decision-flavor wall,
continuous with T417 Leg 2), with **Blum–Blum–Shub (1986)** forward-security.
Cited, **NOT** proven. Honest posture inherited from T417: any single fixed `N` is
finite-work crackable, so the boundary is **asymptotic / family-level and
conditional**. Candidate 3's RSW/VDF sequentiality is deliberately NOT the basis
(it cannot be reduced to factoring).

## Differentiation (argued, not asserted) — success-criterion-3

- **vs Brown–Susskind:** constant-complexity bijection, forward cost FLAT,
  asymmetric feasible-INVERTIBILITY not symmetric complexity growth — nothing grows.
- **vs Lesovik:** reversal EXISTS with probability 1 (unique predecessor),
  computationally sealed — hardness is not statistical improbability, no ensemble.
- **vs Crutchfield:** state fully observed, nothing hidden in causal states — the
  lock is cryptographic one-wayness with an explicit factoring reduction.
- **vs Wolpert/Bennett:** entropy-neutral, zero thermodynamic cost — the seal is
  algebraic (missing factorization), isolating the E2 wall from E1.
- **vs T417:** real iterated dynamics + time index + emitted record stream +
  per-transition cost asymmetry, not a static `(x,N)` datum.

## Success / honesty criteria

Succeeds as exploration if it exhibits, executably: (a) an actual iterated orbit
with a time index and an emitted bit-record; (b) an information-theoretically
trivial boundary (datum present, reversal exists) that is nonetheless
computationally forced (E2), with backward-hardness **reduced** to Rabin/QRA (not
stipulated); (c) a per-step forward/backward asymmetry over the SAME orbit (not a
relabel) with forward cost FLAT and no growing monotone; (d) the four-kill dodge
table; (e) honest bounding: conditional on factoring/QRA, family-level, any single
fixed `N` crackable. A negative result (any kill firing) is a success of the
method and must be reported plainly. No physics/crypto claim beyond cited standard
assumptions; no promotion; no cross-repo import; pauses for Joe.
