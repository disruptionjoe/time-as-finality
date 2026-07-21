---
title: "Involution-typing lemma for the GU/TaF boundary-law TIME face: does an involution alpha on the finality label have alpha-even maps EXACTLY the A*(R)-computable maps? Outcome T-REFUTE -- the coincidence holds IFF the excluded causal-future carries a single Z/2 witness (k=1); T19's fixture has k>=2 independent witnesses (e_E1,e_E2), so NO fixpoint-free involution reproduces the class. The exclusion engine is the causal-past RETRACTION (an idempotent forgetting the future up-set), strictly more general than a fixpoint-free flip on TWO independent axes: orbit-cardinality (block size 2^k > 2) and orientation (idempotent pi.pi=pi, non-invertible, vs order-2 automorphism alpha.alpha=id). The GU/TaF time-face unification is LEG-deep (shared first/third-person conclusion shape), not MECHANISM-deep. Planted controls separate: single-Z/2-witness toy registers T-EXHIBIT, multi-witness toy registers T-REFUTE."
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (cross-repo: boundary-law time-face involution lemma)"
extends:
  - "READ-ONLY gu-formalization: explorations/diagonal-boundary-unification-2026-07-20.md (Appendix A, Section 4)"
  - "READ-ONLY gu-formalization: explorations/l1-assembly-2026-07-20.md"
inputs:
  - CLAIM-LEDGER.md (rows T19/T92; 2026-06-19 T19 log block)
  - tests/T92-accessible-witness-gap-restriction.md
  - open-problems/first-person-finality-complexity-separation.md
  - open-problems/accessible-witness-gap-restriction-theorem.md
  - models/t19_phenomenal_bridge_separation.py
  - agent-runs/RUN-20260720-184304-t19-involution-typing-mailbox.md
runnable:
  - tests/involution_typing_probe.py
claim: none
canon: none
posture: none
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# Involution-typing lemma: does the T19 causal horizon hide a fixpoint-free flip?

GU's diagonal-boundary parent factors into a diagonal leg (L1) and an
involution leg (L2). Its TIME face is carried by TaF's T19/T92: the
composite conclusion `FIRST-PERSON-FINALITY(A*(R)) = NO` vs
`THIRD-PERSON-FINALITY(G) = YES` is exhibited on a finite record graph, and
a genuine self-encoding predicate (R's verdict about R's own finality) is
present. What is NOT present in TaF's receipts is an involution: T19's
exclusion mechanism is **causal witness placement**, and the ledger insists
the gap "is a causal-boundary obstruction, not a computational
undecidability." GU's own honest prior (its operator-lift) suspected the
causal boundary "looks STRICTLY MORE GENERAL than a fixpoint-free flip --
leg-deep not mechanism-deep." This swing resolves that suspicion.

The steward already gated exactly this question
(`RUN-20260720-184304-t19-involution-typing-mailbox.md`), requiring five
things before the lemma reopens: (1) an explicit finality-label object and
involution; (2) a proof or exhaustive finite check that the equivariant
maps are exactly the `A*(R)`-computable functionals; (3) fixpoint-freeness
+ an odd/even typing; (4) an external-cure and fixed-point dissolution
control; (5) a comparison showing whether causal witness placement is the
same obstruction or a distinct engine. This document supplies all five and
lands the outcome as a steward-ratifiable PROPOSAL. No claim, verdict, or
status moves.

Receipt: `tests/involution_typing_probe.py` -- deterministic (double-run
byte-identical), numpy for the seeded functional identity only, seed
20260720, exit 0 -- HEADLINE
`13 [E] + 11 [F] = 24 (setup [T] = 5 excluded) ALL PASS`.

## 1. Pre-declaration (before computing)

Three outcomes, both non-trivial ones successes:

- **T-EXHIBIT.** A fixpoint-free involution `alpha` on the finality label,
  built from TaF's own frozen apparatus, has `alpha`-even maps EXACTLY the
  `A*(R)`-computable maps. Then the time-face is a genuine parent instance:
  MECHANISM-deep. Must be machine-checked on a TaF fixture.
- **T-REFUTE.** No such involution exists; the causal-placement mechanism
  excludes strictly more than any fixpoint-free flip. A SUCCESS: it scopes
  the boundary law honestly (shared conclusion shape, distinct mechanism)
  and characterizes the more-general structure exactly.
- **T-OBSTRUCT.** The coincidence is not decidable on TaF's current
  fixtures; name what is needed.

Planted control, to prove the test has teeth in both directions: a toy
where the excluded future is a single Z/2 witness MUST register T-EXHIBIT;
a toy where placement is strictly more general MUST register T-REFUTE. A
test that cannot separate them proves nothing.

## 2. The construction, from TaF's frozen T19 structure

The apparatus is `models/t19_phenomenal_bridge_separation.py`, unchanged.
Its finite T1 graph is a causal diamond:

```
CORE (R's world):  e_src -> e_R_recv -> e_R_rec1 -> e_R_final
EXTERNAL:           e_R_final -> e_E1 -> e_meta
                    e_R_final -> e_E2 -> e_meta
```

`R_self_finality` records exist ONLY at `{e_E1, e_E2, e_meta}` -- the strict
causal FUTURE up-set `U = future(e_R_final)`. `A*(R)` is R's accessible
DOWN-set (the causal past of `e_R_final`, the fixed point of R's bounded
D1 iteration). The decisive structural facts, read verbatim from the model:

1. An `A*(R)`-computable functional of the finality content is exactly one
   that is INVARIANT under any change to the future up-set `U`. (The model
   makes this literal: `is_finalized` on any external node raises
   `ValueError` -- the future is structurally absent from `A*(R)`.)
2. Equivalently, an `A*(R)`-computable map factors through the causal-past
   **retraction** `pi`: restriction to the down-set `A*(R)`. `pi` forgets
   the entire future up-set. It is IDEMPOTENT: `pi . pi = pi`.
3. The `A*(R)`-indistinguishability relation on future-configurations is
   therefore the SINGLE all-of-`X` block: two full assignments agreeing on
   the past are `A*(R)`-indistinguishable regardless of their future. Its
   invariant functions are the constants.

The candidate involution has to be built on the finality label from THIS.
Two candidates are natural in TaF's vocabulary, and I test both:

- `alpha_swap` = swap the two witnesses `e_E1 <-> e_E2` (the graph's own
  automorphism);
- `alpha_flip` = flip the `R_self_finality` value at every witness (the
  finality-label value flip, the closest analog of GU's grading swap).

The coincidence question reduces EXACTLY to a partition-comparison, and this
is the load-bearing reduction:

> `alpha`-even maps `== A*(R)`-computable maps
>   `<=>`  orbit-partition(`alpha`) `==` the `A*(R)` indistinguishability
>          partition `== { all of X }`.

An involution has orbits of size `<= 2`. The `A*(R)` block has size
`|X| = 2^k`, where `k` = number of independent future witnesses. So the two
partitions coincide **iff `2^k <= 2`, i.e. `k <= 1`.**

## 3. Which outcome fired: T-REFUTE (and the exact characterization)

`k` for T19 is at least 2 (the model has TWO independent witnesses,
`e_E1` and `e_E2`, each an accessible holder of `R_self_finality`; the
external support is 2, threshold 1; a third, `e_meta`, makes `k = 3` at
config level). Since `k >= 2`:

- **No fixpoint-free involution reproduces the class.** The probe enumerates
  EVERY involution of the 4-element future-config set (the `k=2` fixture)
  and finds none whose orbit-partition is the single `A*(R)` block
  (`[F] k=2: NO fixpoint-free involution's even-class == A*(R)-class`). The
  `k=3` fixture registers T-REFUTE by the same structural fact.
- **`alpha_swap` fails C2 (not fixpoint-free):** every config with
  `b_E1 = b_E2` is a FIXED point of the witness-swap. Placement excludes
  those too, so no fixpoint-freeness.
- **`alpha_flip` fails the coincidence (even-class too big):** it IS
  fixpoint-free, but its even-class has `2^(k-1)` orbits (`= 2` at `k=2`),
  strictly larger than the single `A*(R)` block. It collapses only
  antipodal PAIRS; placement collapses the WHOLE future.

**The more-general structure, exactly.** The `A*(R)`-computable maps are the
invariants of the causal-past retraction `pi`. Two independent facts make
`pi` strictly more general than any fixpoint-free involution `alpha`:

1. **Orbit-cardinality.** `pi`'s indistinguishability classes have size
   `2^k`; `alpha`'s orbits have size `<= 2`. For `k >= 2` an order-2
   automorphism can never collapse a `>2`-element excluded set to the
   single-orbit (constant) invariant class that causal forgetting produces.
   The involution mechanism is precisely the `k=1` fiber.
2. **Orientation.** `pi` is an IDEMPOTENT retraction (`pi.pi = pi`,
   non-invertible -- it forgets the future), whereas every involution is an
   order-2 BIJECTION (`alpha.alpha = id`). The causal cut is ANTISYMMETRIC
   and oriented (past accessible, future not -- a strict order), while a
   fixpoint-free flip is symmetric and has no preferred direction. No
   involution equals `pi` (the probe checks this on the 4-config fixture).
   This is the deeper reason the "orientation datum" of the GU parent is
   external: TaF's exclusion is not a symmetric swap whose orientation you
   must pick, it is a directed forgetting whose forgotten content you cannot
   reach.

So T19's exclusion engine is: **invariance under the causal-past retraction
`pi` = invariance under the full symmetric group on the future-record set**
(order `>= (2^k)!`), of which a fixpoint-free `Z/2` is the degenerate
`|future| = one orbit` special case. Causal placement is strictly more
general on both the cardinality axis and the invertibility/orientation axis.

## 4. The coincidence check and the controls (machine)

The probe (`tests/involution_typing_probe.py`) separates the two planted
controls, which is the whole point of teeth:

- **Control k=1 (single Z/2 witness) -> T-EXHIBIT.** Future `X = {0,1}`;
  `alpha = swap` is fixpoint-free; `orbit-partition(alpha) == { {0,1} } ==`
  the `A*(R)` block; the finality datum (`id: {0,1} -> {0,1}`) is
  `alpha`-ODD; the external cure (fixing the bit) breaks the symmetry and
  reads it; the dissolution control (`alpha = id`, a fixed point) removes
  the exclusion -- exactly the parent's fixed-point dial. `[E] PLANTED
  CONTROL k=1 registers T-EXHIBIT`. This is the `Z/2`-witness case GU's L1
  found realizable, and it correctly registers EXHIBIT.
- **Control k>=2 (multi-witness) -> T-REFUTE.** `[F] PLANTED CONTROL k=2
  registers T-REFUTE (not EXHIBIT)`; `[F] teeth: exhibit and refute are
  SEPARATED by the fixture (k=1 vs k>=2)`.
- **The `exactly` clause is verified as an identity, not asserted.** A
  seeded sweep of 2000 random functionals (numpy seed 20260720) confirms:
  a functional reads the future `<=>` it separates two same-past configs
  (`2000/2000`). So "excluded class = `A*(R)`-computable class" is the exact
  statement "factors through `pi`," per the retraction characterization.

The exact theorem the probe stamps: **exhibit fires IFF `k == 1`** (checked
`k = 1` yes; `k = 2, 3, 4` no; brute-force for `n <= 8`, the fixpoint-free
orbit-count fact `2^(k-1)` blocks for larger `k`).

## 5. What this means for the boundary law's time-face

MECHANISM-deep is FALSE for the time-face at fixture grade; it is
LEG-deep. The GU/TaF unification is real at the level of the shared
CONCLUSION (`first-person NO / third-person YES`, class-relative to
`A*(R)`-access, external witness exists, self-encoding predicate present) --
exactly the parent's composite conclusion shape. But the EXCLUSION ENGINE
differs in kind: GU's leg (b) excludes by `alpha`-evenness under a
fixpoint-free flip (a symmetric order-2 automorphism); TaF excludes by the
causal-past retraction (an oriented, non-invertible idempotent). The two
engines coincide ONLY on the degenerate single-`Z/2`-witness fiber, which
T19 is not.

This is the honest scoping GU's operator-lift anticipated, now made exact:
the parent has two genuinely distinct exclusion engines on its time-face,
and the diagonal-boundary law unifies the time-face at the conclusion level,
not the mechanism level. It does not oversell the unification, and it does
not weaken T19: the causal-boundary reading in the ledger is confirmed as
the RIGHT reading -- richer than an involution, not secretly one.

## 6. Council pass (inline, five lenses)

- **Categorical logician (attack the reduction and the partition claim):**
  the reduction `even-class == A*(R)-class <=> orbit-partition == A*(R)
  partition` is the standard fact that a function is constant on the fibers
  of a quotient iff it factors through it; here the quotient by `alpha` (an
  order-2 group action) versus the quotient by `pi` (an idempotent
  retraction). The content is that these two quotients coincide iff every
  fiber has size `<= 2`, which for a single all-of-`X` fiber means
  `|X| <= 2`. That is exact, not hand-waved. One genuine subtlety flagged:
  I modeled `A*(R)`-computability of the finality datum as invariance under
  ALL future changes (the whole up-set is forgotten). This is faithful to
  the T19 model (`ValueError` on every external node), but a future
  operator-grade lift where `A*(R)` retains PARTIAL, coarse future
  information would enlarge the surviving invariant class; the coincidence
  could then only get HARDER, never easier, so the refute is stable under
  that generalization. Recorded as the honest residue, not a hole.
- **TaF-native finality theorist (T19/T92 fidelity):** the extraction is
  faithful and moves nothing. `A*(R)` is the fixed-point access down-set;
  the finality label is `R_self_finality`; the mechanism is causal
  placement; "stronger than undecidability" and "not a computational
  undecidability" are quoted and respected -- indeed the refute CONFIRMS
  them (a retraction is not a computability bound and not a flip). T92's
  restriction-closure result is untouched: it concerns the gap presheaf
  `G(U) = A(U) - F(U)`, a different object; nothing here proposes it is an
  involution-even class either. C1 stays `weakened`; no row moves.
- **Krein / involution analyst (the flip identification, borrowed from GU's
  L1):** GU's L1 assembly found its `alpha` is a genuine fixpoint-free swap
  whose antilinear dress is Kramers-type, living on a label object of size
  2 (`{+K_S, -K_S}`). That is precisely the `k=1` fiber -- which is why the
  Z/2-witness control registers EXHIBIT and matches GU's realizable case.
  The refute is not a failure to find GU's structure; it is the finding that
  T19's excluded object is NOT a two-element label but a `2^k`-element
  future cube, on which no order-2 flip has the right orbit structure. The
  Krein flip and the causal retraction are cousins only at `|B| = 2`.
- **Causal-set theorist (is `pi` really the right invariant?):** yes -- the
  T19 exclusion is a causal cut of a partial order into a down-set (`A*(R)`)
  and its complementary up-set (`future(e_R_final)`). Invariance under
  forgetting an up-set is the invariant of a causal-past restriction, which
  is the causal-set analog of a filtration/retraction, intrinsically
  ANTISYMMETRIC. An involution has no antisymmetry to encode a "before/after"
  cut; that is the orientation obstruction, stated causally. The multiplicity
  `k` is just the width of the excluded future antichain (`{e_E1, e_E2}` is a
  2-antichain), and any width `>= 2` kills the involution typing.
- **Adversarial referee (answered in writing):** (i) Charge: you defined
  `A*(R)`-computable as "forget the whole future," which trivially can't be
  an involution-even class -- you built in the refute. Answer: the
  definition is the T19 model's, not mine (external nodes are structurally
  absent from `A*(R)`); and the test is NOT rigged, because the SAME
  machinery registers T-EXHIBIT on the `k=1` control -- the refute is a fact
  about `k >= 2`, exhibited by the separation, not an artifact of the
  definition. (ii) Charge: maybe a cleverer involution on a LARGER label
  object works. Answer: the coincidence is a partition identity; enlarging
  the label object only enlarges `|X|`, and `2^k <= 2` fails harder, not
  easier -- the categorical-logician residue covers the partial-info case
  too. (iii) Charge: this is a negative result dressed as a success. Answer:
  it is the success the mission pre-declared -- it correctly SCOPES the
  boundary law (leg-deep, exact more-general structure named) instead of
  overselling a mechanism identity; and it discharges all five of the
  steward's gating requirements with a machine check. (iv) Charge:
  cross-repo claim movement by the back door. Answer: no TaF row moves; this
  is a new exploration + probe + a PROPOSAL flagged for the steward, in
  TaF's own vocabulary; GU was read-only.

## 7. Receipts

- Probe: `tests/involution_typing_probe.py` -- HEADLINE
  `13 [E] + 11 [F] = 24 (setup [T] = 5 excluded) ALL PASS`, exit 0,
  deterministic (double-run byte-identical), numpy for the seeded identity
  only, seed 20260720. `[T]` reconstructs the T19 mechanism (internal NO /
  external YES; A*(R) partition = one block). `[E]` the k=1 EXHIBIT control
  (fixpoint-free swap; even-class == A*(R)-class; odd datum; external cure;
  dissolution), the retraction `pi` idempotent/non-bijective, the exactly
  identity (2000/2000 seeded). `[F]` the k>=2 REFUTE (exhaustive involution
  enumeration at k=2; k=3 T19 fixture; both TaF-native candidates fail for
  the two distinct reasons; orientation obstruction; teeth/separation).
- TaF receipts (read): CLAIM-LEDGER T19 block (FIRST-PERSON = NO /
  THIRD-PERSON = YES, O(|G|), causal-boundary, "stronger than
  undecidability"); `models/t19_phenomenal_bridge_separation.py` (the
  frozen diamond and the ValueError-on-future mechanism);
  `tests/T92-accessible-witness-gap-restriction.md`;
  `open-problems/first-person-finality-complexity-separation.md`;
  `agent-runs/RUN-20260720-184304-t19-involution-typing-mailbox.md` (the
  five gating requirements, all discharged here).
- GU receipts (read-only): `diagonal-boundary-unification-2026-07-20.md`
  Section 4 + Appendix A (the ANALOGOUS-toward-DERIVABLE grade and the
  exact lemma target); `l1-assembly-2026-07-20.md` (the realizable
  single-Z/2 label object = the k=1 EXHIBIT control's match).

## 8. Boundary

Exploration tier; claim/canon/posture: none; no external actions; no
commits or pushes; no edits to any existing file -- new files only
(`explorations/involution-typing-lemma-2026-07-20.md`,
`tests/involution_typing_probe.py`, and the steward proposal note). GU and
temporal-issuance touched read-only; nothing written outside
time-as-finality. Fixture grade throughout: finite Z/2-sets, exhaustive
involution enumeration for `n <= 8`, the fixpoint-free orbit-count fact for
larger `k`. Named residues: (i) the operator-grade lift where `A*(R)`
retains partial coarse future information (the refute is stable under it,
per the categorical-logician note, but is not machine-checked there);
(ii) T92's gap presheaf is a distinct object, not addressed as an
involution class here; (iii) the VALUE of the finality bit remains what
T19 says it is -- nothing here posits or moves it. Nothing here moves C1,
T19, T92, the Complexity Ledger, or public posture.

## 9. PROPOSAL TO STEWARD (for ratification; no claim movement requested)

Outcome for the gated T19 involution-typing lemma
(`RUN-20260720-184304-t19-involution-typing-mailbox.md`): **T-REFUTE.**

All five gating requirements are discharged: (1) explicit finality-label
object (the future-config space `X = 2^k` of `R_self_finality` witnesses)
and two candidate involutions (`alpha_swap`, `alpha_flip`); (2) exhaustive
finite check that `alpha`-even maps `==` `A*(R)`-computable maps IFF the
excluded future is a single `Z/2` orbit (`k <= 1`) -- machine-verified;
(3) fixpoint-freeness and odd/even typing checked per candidate; (4)
external-cure and fixed-point dissolution controls (the `k=1` EXHIBIT toy);
(5) the comparison: causal witness placement is the causal-past retraction
`pi` (idempotent, non-invertible, oriented) -- a DISTINCT engine, strictly
more general than a fixpoint-free flip on two axes (orbit-cardinality
`2^k > 2`, and orientation `pi.pi = pi` vs `alpha.alpha = id`).

**Recommendation:** ratify the lemma as **CLOSED-REFUTED at fixture grade**
-- the GU and TaF exclusion mechanisms are structurally distinct; the
GU/TaF time-face unification is confirmed LEG-deep (shared first/third-person
conclusion shape), not MECHANISM-deep. This CONFIRMS, and does not weaken,
the ledger's causal-boundary reading of T19. No C1, T19, T92, Complexity
Ledger, Canon Index, public posture, or external action moves. If a future
operator-grade lift gives `A*(R)` partial future information, the refute is
predicted stable (coincidence only gets harder); that lift is the one open
reopener.
