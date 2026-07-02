# T419 — Computational Arrow of Time (D2, temporal lift of T417) — Results v0.1

- **Artifact:** `T419-computational-arrow-of-time-v0.1`
- **Provisional T-number:** **T419** (TESTS.md and CLAIM-LEDGER.md **UNTOUCHED**;
  noted here only; registration + any promotion pause for Joe)
- **Problem:** [open-problems/computational-finality-arrow.md](../open-problems/computational-finality-arrow.md) (D2)
- **Taxonomy mode:** E2 — [technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md](../technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md)
- **Extends:** [results/T417-computational-finality-boundary-v0.1-results.md](T417-computational-finality-boundary-v0.1-results.md)
- **Spec (frozen first):** [tests/T419-computational-arrow-of-time.md](../tests/T419-computational-arrow-of-time.md)
- **Model:** [models/computational_arrow_of_time.py](../models/computational_arrow_of_time.py)
- **Test:** [tests/test_computational_arrow_of_time.py](../tests/test_computational_arrow_of_time.py)
- **Tags:** exploratory_D2_swing, E2_computational_arrow, rabin_bbs_squaring_permutation,
  entropy_neutral_bijection, hardness_by_reduction, QRA_conditional, closed_model,
  K4_FIRED, redesign, recorded_tier, no_claim_promotion

**Exploratory big-swing on the D2 open problem — a *computational arrow of time*.**
NOT a physics or crypto result beyond cited standard assumptions. Cross-domain
material (cryptography / number theory) is the **object of study**, never evidence
for physics or a sibling repo. Recorded-tier; **no CLAIM-LEDGER entry; no claim
promotion; ledger actions pause for Joe.** Single-process ceiling in force.
Hostile review **complete** — see verdict below.

---

## Verdict (house vocabulary) — **REDESIGN. A kill fired (K4).**

The construction is **numerically correct** and its thermodynamic (K1) and
stipulated-hardness (K3) guards **hold under hostile review**. But the originally
designated anti-relabel leg — **Leg 6, the K4 guard** — was **fabricated and false
on the exhibited orbit**, so the **static-relabel kill (K4) FIRED at confidence
0.90**. The committed model now records that failure directly.
The temporal object T419 actually exhibits is a **time-symmetric, reversible,
short-Poincaré-recurrent** dynamics, not a one-way arrow; the genuine one-way
asymmetry is present only as an **unexhibited appeal to cryptographic scale** that
the fixture itself flags as conditional. Two further kills landed partial hits
(**K2 Brown–Susskind, 0.62**; **K5 prior-art, 0.70**). **K1 (0.85), K3 (0.78), and
independent correctness (0.90) survive.**

The earlier v0.1 draft of this document asserted "no kill criterion fired." **That
claim is retracted here.** A negative result is a success of the method, and this is
reported plainly: **T419 does not clear the D2 novelty bar as built.** It is
**fixable in principle** (the break is in the *exhibition*, not proven fatal to the
*intended* construction), hence **REDESIGN, not ABANDON** — but the fix path is
narrow and, if executable exhibition cannot be restored, collapses to the spec's own
K4 consequence: **demote to T417.**

---

## Construction

Rabin / Blum–Blum–Shub squaring permutation on the quadratic residues of a **Blum
integer**. Reuse T417's `N = 77 = 7·11` (`7 ≡ 11 ≡ 3 mod 4`). Forward transition
`F(x) = x² mod N`. On `QR_77` (15 elements: `[1,4,9,15,16,23,25,36,37,53,58,60,64,
67,71]`) `F` is a **permutation** because `|QR_N| = φ(N)/4 = 15` is **odd** — so
nothing is erased and each state has a **unique predecessor**. From seed `x_0 = 4`,
the orbit is `[4,16,25,9,4,16,25,9,4]` (`T = 8` ticks, **period 4**) with emitted
BBS bit-record `b_t = lsb(x_t) = [0,0,1,1,0,0,1,1,0]` (also period 4). The **record**
is this tick-indexed trajectory + bit stream.

`F` on `QR_77` decomposes into cycles of length `[1,4,4,2,4]` (max 4); the seed-4
orbit is one of the 4-cycles. **This cycle structure is the crux of the K4 break**
(below): on a permutation of a finite set, `F⁻¹ = F^(L−1)` on any cycle of length
`L`, so a trapdoor-free agent recovers every recorded predecessor by iterating the
*forward* map — no factoring, no square root, no trapdoor.

---

## Predeclared legs — honest outcomes

| Leg | Predeclared claim | Held? |
| --- | --- | --- |
| **1 PERMUTATION / entropy-neutral** | `sorted(F over QR_77) == QR_77`; `|QR_77|=15` odd; zero erasure | **HOLDS** (verified independently) |
| **2 CO-PRESENCE** | unique QR-predecessor each tick; trapdoor CRT principal-sqrt recovers exact `x_{t-1}` | **HOLDS** |
| **3 FORWARD-EASY-FLAT** | 1 modmul/step using only `N`; ops `[1,1,1,1,1,1,1,1]` | **HOLDS** |
| **4 BACKWARD-HARD-BY-REDUCTION** | Rabin sqrt≡factoring exhibited: oracle `w=2 → root 9`, `gcd(9−2,77)=7` | **HOLDS as a *generic-point* statement** (see K3/K4 caveats) |
| **5 TRAPDOOR-RESYMMETRIZES** | with `(p,q)` backward polylog; without, ≥ factoring | **HOLDS at generic points; false on-orbit** (cycle-iteration reverses trapdoor-free) |
| **6 TEMPORAL-ASYMMETRY-OVER-ORBIT (anti-relabel, the K4 guard)** | `backward_feasible_without_trapdoor = []` on the orbit | **FAILS — fabricated in the original draft.** The corrected T419 model computes the true set as non-empty and cheap (`F³` recovers each predecessor) |
| **7 COST-GROWTH-FAMILY** | forward flat; `backward_without_trapdoor` strictly increasing `[2,6,10,22,42,82]` | **NUMBERS CORRECT but MIS-BILLED** — the curve is `trial_division_steps(N)` (a *factoring* proxy that grows in `N`), not the trapdoor-free reversal cost. The true trapdoor-free reversal cost is the cycle length `[2,4,12,20,84,40]` (grows in `N`, **not monotone**, **not in `t`**) |
| **8 KILLER-PREMORTEM table** | four dodges, none fire | **FALSE as originally scored** — K4 fires; K2/K5 partial |

Legs 1–4 are sound. Legs 5–8 rest on the same defect: the fixture conflates
**generic-point** square-root hardness (which *is* T417's static boundary) with
**hardness along the exhibited dynamics** (which is trivially easy because the orbit
is a short known cycle). That conflation is exactly what K4 hunts.

---

## Adversarial review — six verdicts

Hostile panel run to completion. Each kill criterion and whether it **FIRED**:

### K1 — Thermodynamic / E1 reduction (Landauer erasure). **DID NOT FIRE. Survives (0.85).**
`F` is a verified bijection on the actual state space `QR_77` (every element has
exactly one QR-preimage; `sorted(images) == QR_77`), so there is **zero Landauer
erasure** — no `kT ln2` to bill. No step erases or resets; the emitted bit is a
reversible copy of a retained state, not a partial trace. The strongest reframing —
that physically factoring `N` to invert dissipates heat — is defeated by **Bennett's
reversible-computation theorem**: factoring can run with arbitrarily small
dissipation, so backward-hardness is an irreducible **time-complexity** cost, not an
erasure cost. The E1 guard is structurally sound.
*Honest caveat (different lane):* the fixture's own honest bounding (family-level,
asymptotic, single-`N` crackable) does expose it to the taxonomy's **asymptotic-E1
(limit-gap)** absorber — but that is the limit-gap sense, not Landauer erasure, and
the docs loosely conflate "E1 = thermodynamic" with "E1 = asymptotic."
Probe: `_local/thermodynamic_probe.py`.

### K2 — Brown–Susskind (symmetric complexity growth / reversible recurrence). **PARTIAL (0.62).**
Real hit on the demonstration. Every **concrete** object the fixture exhibits is
**time-symmetric reversible-recurrent**: reversal = traverse the cycle, same cost
either way; the seed-4 orbit is a 4-cycle; there is **no one-way function present**
(squaring is inverted by iterating squaring). This falsifies Leg 6's emptiness claim
and shows Leg 7 bills the wrong cost (size-monotone in `N`, not a `t`-monotone
mechanism). **Not a full break:** the *intended* arrow (single state, no record,
huge cycle: squaring = P vs principal-sqrt = assumed-factoring) is a difference in
computational **kind** that survives at cryptographic scale and is distinct from
symmetric linear complexity growth; `forward_step_ops` stays flat in `t` and no
two-sided complexity monotone is tracked, so the *literal* K2 trigger is dodged.
Probes: `_local/brown-susskind-probe.py`, `_local/brown-susskind-scaling.py`.

### K3 — Stipulated-hardness / E0-in-disguise. **DID NOT FIRE. Survives (0.78).**
The backward step is the principal square root mod `N`, which **Rabin (1979)** — a
real, correctly-cited theorem — makes poly-time equivalent to factoring. Factoring
and **QRA (Goldwasser–Micali 1982)** are named **standard** assumptions, not author
fiat. `rabin_reduction(n, oracle)` is genuinely trapdoor-free (references neither
`P/Q` nor `principal_sqrt`; uses only `n` and the black-box oracle); a **non-trapdoor**
brute-force sqrt oracle also drives the reduction to a nontrivial factor on every
family member. Hardness is **reduced**, not stipulated.
*Real defect (rigor, not fiat):* the shipped `rabin_reduction` never checks
`r*r % n == a`, so at the toy `N=77` a garbage oracle also "factors" `N` via
coincidental nontrivial idempotents — the executable exhibition backing
`sqrt_oracle_yields_factor_of_N` is **confounded at small `N`** and does not, by
itself, isolate the sqrt capability as the cause. Fix: verify `r² == a`.
Probes: `_local/probe_stipulated_hardness.py`, `_local/probe_stipulated_hardness2.py`.

### K4 — Static-T417-relabel. **FIRED. Breaks (0.90).** *(This is the decisive verdict.)*
The original anti-relabel leg (Leg 6, the *designated* K4 guard) was
**fabricated**. The quantity `backward_feasible_without_trapdoor` was hardcoded to
`[]` rather than computed. The committed T419 model now computes it and records the
failure. The exhibited orbit has **period 4**; on a
period-`p` cycle `F⁻¹ = F^(p−1)`, so the recorded predecessor of every orbit state
is recoverable by **3 forward squarings mod `N` using `N` alone** — no trapdoor, no
factoring, cost flat and cheap. The probe (`_local/static_relabel_probe.py`) confirms
period 4 is discoverable by forward iteration and all predecessors recovered
trapdoor-free by `F³`. **Along the actual iterated dynamics there is NO
forward/backward feasibility asymmetry** (forward 1 modmul, backward 3 modmuls, both
trapdoor-free); the claimed empty backward set is **inserted by fiat**. The only real
hardness left (Leg 4's Rabin sqrt≡factoring) is a statement about inverting `F` at a
**generic** point — i.e. exactly T417's static QR/square-root boundary. On-orbit
points are non-generic, so evaluating that static boundary at `t = 2,4,6` is
**literally relabeling `(x,N)` along a time index** — precisely the K4 failure mode.
Corroboration: the emitted bit-stream is also period 4, so the cited BBS
forward-security (past-bit unpredictability) is **vacuous** — past/future bits
readable by inspection. The v0.1 draft's assertion that the per-step invertibility
asymmetry "still holds at every tick" is **incorrect**; it does not.

### K5 — Prior-art / novelty. **PARTIAL (0.70).**
The **core concept is not novel**; strongly adjacent prior art exists. (1)
**Reversible-CA public-key cryptosystems** (Kari 1990 line) are structurally
identical: unique-predecessor (no information loss), forward-easy, backward-infeasible
without the key — the exact entropy-neutral-bijection + hardness-keyed-asymmetry
object, minus the arrow label. (2) **Towell, "The Beautiful Deception"
(arXiv:2510.12802, 2025)** explicitly states "an artificial arrow of time through
trapdoor functions... easily compute future indices but cannot determine what came
before without the seed" — a paper-level statement of the cryptographic-arrow idea.
(3) **BBS forward-security** ("cannot reconstruct previous states") is textbook
folklore and is the fixture's own spine. **However**, no single clean paper carries
the fixture's *full differentiated packaging together* — entropy-neutral bijection +
hardness-**by-reduction** (Rabin sqrt≡factoring, not stipulated) + explicit provable
separation from **both** E1 thermodynamic **and** Brown–Susskind complexity-growth
arrows. So K5 as literally worded ("a clean published cryptographic arrow of time
with *these exact* properties") does **not strictly fire** — but the broader novelty
bar ("anything broader is already taken") is **largely consumed**. Residual value is
**synthesis / differentiation only**, matching the program's taxonomy note ("at most
a synthesis/perspective, not a novel result").

### Correctness — independent re-derivation. **Survives (0.90).**
Suite re-run (`12 passed`), model re-run (clean JSON). Every number independently
re-derived without reusing model functions (from-scratch principal sqrt, sympy
`jacobi_symbol`, brute-force QR-predecessor): all match. Blum `7≡11≡3 mod4`;
`|QR_77|=15=φ/4` odd ⇒ bijection; orbit `[4,16,25,9,…]` period 4, bits
`[0,0,1,1,…]`; unique QR-predecessor each tick `== x_{t-1}`; Rabin reduction
genuinely exhibited (`w=2, a=4 → root 9, gcd(9−2,77)=7` splits `N`, real because
`2∉QR_77`); Jacobi over orbit all `+1`; family `[21,77,209,713,2537,8549]` all Blum,
trial-division backward `[2,6,10,22,42,82]` strictly increasing, trapdoor
`[10,14,18,20,24,28]`. **No numeric error, no logic bug.** The one framing point
(Leg 6 `[]` while brute-force does recover) is disclosed in the honesty notes, not a
hidden overclaim — but see K4: disclosure does not rescue it, because the whole
temporal claim rests on that leg.

**Scoreboard:** K1 survives · K2 partial · K3 survives · **K4 FIRED** · K5 partial ·
correctness survives.

---

## Novelty-differentiation outcome (success-criterion-3)

The differentiation *arguments* remain individually reasonable, but K4/K2 hollow out
the object they are meant to distinguish, and K5 shows the concept is largely
pre-empted. Honest scoring:

- **vs Brown–Susskind (arXiv:1701.01107)** — **weakest point.** The *exhibited*
  object is precisely a Brown–Susskind finite-system regime: reversible,
  short-Poincaré-recurrent, time-symmetric, with the cycle/recurrence length as the
  binding "backward cost." The claimed distinction (asymmetric feasible-invertibility
  vs symmetric complexity growth) is **true only of the unexhibited cryptographic-scale
  object**, not of anything T419 actually runs.
- **vs Lesovik (arXiv:1712.10057)** — distinction holds *in principle* (reversal
  exists with probability 1 via unique predecessor, not statistical improbability),
  but is not the mechanism that fails; unaffected by the kills.
- **vs Crutchfield–Ellison (crypticity / ε-machines)** — distinction holds (state
  fully observed; the intended lock is cryptographic one-wayness, not causal-state
  hiding); unaffected.
- **vs Wolpert / Bennett (stochastic thermodynamics of computation)** — distinction
  holds and is *strengthened* by the K1 survival (Bennett reversibility confirms the
  seal is time-complexity, not `kT ln2`). This is the cleanest surviving separation.

Net: the E2-vs-E1 separation (K1, vs Wolpert/Bennett) is genuinely defended; the
**E2-vs-Brown–Susskind separation — the load-bearing novelty claim for D2 — is the
one the fixture fails to exhibit.** And K5 shows even a corrected version would be
**synthesis/differentiation**, not a first-of-kind result.

---

## What fired, why, and the fix path

**Root cause (single defect, several symptoms).** The fixture was built at a **toy
`N = 77` whose seed-4 orbit is a period-4 cycle**. On any finite permutation, a short
*discoverable* cycle makes trapdoor-free reversal trivial (`F⁻¹ = F^(p−1)`). The
one-way arrow the spec wanted exists **only** where the cycle length is
super-polynomial *and the period is itself hard to find* — a regime that cannot be
exhibited executably on a toy. The original draft hardcoded the emptiness claim and
mis-billed the backward cost (Leg 7) with a factoring proxy that happens to grow in
`N`; the committed model now encodes the K4 failure. K2 still fires partially on
the recurrence; the numbers are all correct but the *mechanism story* is wrong.

**Why REDESIGN and not ABANDON.** The break is in the **exhibition**, not proven
fatal to the **intended** construction. K1, K3, and correctness survive; the
E2-vs-E1/Wolpert separation is clean. A redesign has an identifiable path:
1. **Delete the hardcode.** Actually compute `backward_feasible_without_trapdoor`,
   which will (honestly) show trapdoor-free recovery via cycle iteration at toy scale.
2. **Relocate the arrow to where cycle-reversal is infeasible.** At cryptographic
   scale the trapdoor-free agent cannot *find the period* cheaply (period-finding for
   BBS relates to the order of 2 mod λ(N), hard without factoring). Add a leg that
   makes **period-hardness**, not just point-sqrt-hardness, the basis of the arrow —
   this is the piece that actually separates the dynamics from the static T417 datum.
3. **Fix the Rabin exhibition confound** (verify `r² == a`; note toy idempotent
   artifacts) — K3's rigor defect.
4. **Re-bill Leg 7** in the true trapdoor-free reversal cost (period/recurrence), and
   present the factoring curve separately as the *conditional* basis.

**The narrow-path caveat / ABANDON fallback.** If the redesign cannot restore an
**executable per-step asymmetry** — and for finite permutations exhibited on a toy it
provably cannot — then the arrow lives only as an **asymptotic, unexhibited appeal**,
which is precisely the spec's K4 demotion consequence: **no arrow, demote to T417.**
Combined with K5 (novelty largely pre-empted by reversible-CA cryptography and
Towell's trapdoor-arrow paper), a corrected T419 is at best a **synthesis/perspective
lift of T417**, not a novel distinct arrow. The honest expected ceiling of the
redesign is "T417 + a defensible temporal framing conditional on period-hardness,"
recorded-tier.

---

## Honesty notes (retained and corrected)

- **The v0.1 "no kill fired" verdict is retracted.** K4 fired (0.90). The period-4
  orbit is not a benign detail: it is the mechanism by which the anti-relabel guard
  fails.
- **`backward_feasible_without_trapdoor = []` was not merely "the conditional QRA
  claim."** In the original draft it was **hardcoded and false on the exhibited
  orbit**; the corrected model records that trapdoor-free cycle-iteration recovers
  every predecessor. The concede-co-presence / deny-feasible
  move from T417 does **not** transfer, because at toy scale the recovery is *feasible*
  (cheap forward iteration), not just co-present.
- **Leg 7's backward curve is a factoring proxy, not the reversal cost.** It grows in
  `N` (size), never in `t`; it does not evidence a per-tick arrow.
- **The E2-vs-Brown–Susskind separation is unexhibited.** Everything T419 runs is
  reversible-recurrent. The distinction is real only at cryptographic scale, which the
  fixture asserts but does not demonstrate.
- **Boundary remains conditional and asymptotic.** Even a corrected fixture rests on
  factoring/QRA (unproven) and is family/asymptotic-level; any single fixed `N` is
  finite-work crackable. **D2 is not discharged.**

## Reproduction

```bash
python -m pytest tests/test_computational_arrow_of_time.py -q   # 12 passed
python -m models.computational_arrow_of_time                    # emits leg JSON
# adversarial probes (gitignored _local/):
python _local/static_relabel_probe.py        # K4 — period 4, F^3 reverses trapdoor-free
python _local/brown-susskind-probe.py         # K2 — reversible-recurrent cycle structure
python _local/thermodynamic_probe.py          # K1 — zero erasure, Bennett reversibility
python _local/probe_stipulated_hardness.py    # K3 — trapdoor-free Rabin reduction
```

Deterministic, exact integer arithmetic; closed model (no reservoir, no partial
trace, no randomness). Hardness cited (Rabin 1979 sqrt≡factoring; Goldwasser–Micali
1982 QRA; Blum–Blum–Shub 1986 forward-security), **not** proven. Recorded-tier; no
claim promotion; TESTS.md / CLAIM-LEDGER.md untouched; pauses for Joe.

---

## Overall recommendation — **REDESIGN**

A kill (K4, static-relabel) fired at 0.90 and a second (K2, Brown–Susskind) landed a
partial hit at 0.62, both traced to a single defect: the arrow is exhibited on a
short reversible cycle; the original anti-relabel guard was hardcoded rather than
computed, and the committed model now computes the failure.
**T419 as built does not clear the D2 novelty bar — it exhibits a time-symmetric,
reversible-recurrent dynamics, not a distinct computational arrow.** The
thermodynamic (K1), stipulated-hardness (K3), and correctness guards survive, and the
E2-vs-E1 separation is clean, so the angle is **not dead** — but the fix requires
relocating the hardness from *point-square-root* to *period-finding* and honestly
conceding that the arrow is not executably exhibitable at toy scale. If that redesign
cannot restore an executable per-step asymmetry (it likely cannot for a finite
permutation on a toy), the spec's own K4 consequence governs: **demote to T417**, and
— given K5's largely-consumed novelty — treat any survivor as **synthesis, not a
novel result.** No promotion; ledger and next steps pause for Joe.
