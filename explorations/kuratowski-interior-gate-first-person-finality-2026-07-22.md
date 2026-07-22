---
title: "Kuratowski interior-operator gate for the first-person-finality paper: does the T19 causal-past retraction pi satisfy the four interior axioms? Outcome PASS -- pi's faithful knowledge-modality interior (open sets = the pi-saturated / A*(R)-accessible subsets) satisfies int(X)=X, int A subset A, int int A = int A, and int(A cap B) = int A cap int B on the frozen T19 fixture. Therefore an S4-interior-operator title is LICENSED for the paper. The raw set-image readings of pi are NOT interior operators (direct image fails top-preservation K1 and meet-preservation K4; preimage fails contractivity K2), which gives the gate teeth: the FAIL branch was reachable. The interior on the EXCLUDED future subspace is the DEGENERATE (indiscrete) S4 modality; the non-degenerate S4 content lives on the full causal order. The broad 'certify your own present is final' headline stays EMBARGOED -- it needs an all-finite-graphs quantifier not established here."
status: active_research
doc_type: exploration
created: 2026-07-22
directed_by: "Joe direct chat, 2026-07-22 (directed-wake run, Wave-1 triple-diamond prep steering, TaF-3 paper-routing gate)"
extends:
  - "explorations/involution-typing-lemma-2026-07-20.md (the causal-past retraction pi and the frozen T19 fixture)"
  - "explorations/partial-future-information-involution-audit-2026-07-21.md (operator-grade retained-information scope)"
  - "explorations/2026-07-22-wave1-triple-diamond-prep-steering.md (TaF-3 wake directive)"
inputs:
  - explorations/2026-07-22-wave1-triple-diamond-prep-steering.md (TaF-3 section)
  - explorations/involution-typing-lemma-2026-07-20.md
  - models/t19_phenomenal_bridge_separation.py (the frozen causal diamond)
  - steward/PROPOSAL-involution-typing-time-face-2026-07-20.md
  - steward/research-portfolio.json (CAPABILITY-TO-TEMPORAL-ORDER, Lane 1)
runnable:
  - tests/involution_typing_probe.py (kuratowski_interior_checks section, [K] tag)
claim: none
canon: none
posture: none
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
track: "Track-2 (paper lane), subordinate to the Track-1 North Star. Reports up; changes no posture."
---

# Kuratowski interior-operator gate: is first-person finality an S4 interior modality?

This is the single deterministic probe that routes the first-person-finality
paper (Wave-1 steering, TaF-3). The involution-typing lemma
(`involution-typing-lemma-2026-07-20.md`) named T19's exclusion engine exactly:
the causal-past **retraction** `pi`, an idempotent, non-invertible, oriented
forgetting of the causal future up-set. `pi` is what the A*(R)-computable
finality maps factor through. The downstream paper question is not whether `pi`
is an involution (it is not; that is settled) but whether `pi` gives rise to an
**S4 interior operator**: a genuine knowledge/necessity modality on record
predicates. If yes, the paper is licensed to call first-person finality an
S4-interior operator; if no, the paper routes instead to a retraction-algebra
framing carrying a publishable sub-S4 negative.

This document records the probe extension, the verdict, and a steward PROPOSAL
for the paper route. It is subordinate Track-2 (paper lane) work: it moves no
claim, no canon, no verdict, and it does not assert the embargoed headline.

Receipt: `tests/involution_typing_probe.py` (new `kuratowski_interior_checks`
section, `[K]` tag) -- deterministic (double-run byte-identical), exit 0.
HEADLINE
`13 [E] + 11 [F] = 24  |  [K] Kuratowski gate = 17 PASS  (setup [T] = 5; scope [P] = 4 excluded) ALL PASS`.

## 1. Pre-declaration (before computing)

The gate is a single deterministic disjunction, both branches publishable:

- **PASS.** `pi` induces an interior operator satisfying all four Kuratowski
  interior axioms (int(X)=X; int A subset A; int int A = int A;
  int(A cap B) = int A cap int B). Then first-person finality is an S4-interior
  (necessity) modality and the S4-interior-operator title is LICENSED.
- **FAIL.** The induced operator breaks at least one axiom (the diagnostic one
  is K4, meet-preservation: a monotone modality that is not normal). Then the
  paper routes to a **retraction-algebra** framing and reports a publishable
  **sub-S4 NEGATIVE** (first-person finality is a weaker-than-S4 modality).

Teeth requirement, predeclared: the gate must be able to REGISTER a failure.
A test that cannot fail proves nothing. The probe therefore also feeds `pi`'s
raw set-image readings (which are not interior operators) through the same four
axioms and confirms they fail specific ones. The desired title does not dispose;
the axiom computation does.

## 2. Construction fork (identify, name, do not default)

Per the repo's standing construction-fork discipline (`AGENTS.md`): `pi` is a
POINT map (idempotent `pi.pi = pi`, non-invertible, oriented), not a set
operator, so "the interior operator of `pi`" has more than one construction.
Naming the fork is mandatory; defaulting silently to either side is the error.

- **Faithful reading (used for the verdict): the accessible-knowledge
  interior.** In epistemic logic a knowledge modality is the interior of the
  indistinguishability relation. Here two configurations are
  A*(R)-indistinguishable exactly when they share a causal past, i.e. when they
  have the same `pi`-image. The OPEN sets are therefore the `pi`-saturated
  subsets (unions of `pi`-fibers = the A*(R)-accessible predicates), and the
  interior is `int(A) = union of the pi-fibers contained in A`. This is THE
  standard construction for "what R can certify from within A*(R)."
- **Orientation-faithful variant: the `pi`-stable interior.** Built directly
  from `pi` as an oriented idempotent, without symmetrizing to an equivalence:
  `int(A) = A cap pi^{-1}(A)`, whose opens are the `pi`-stable subsets
  (`x in A => pi(x) in A`). This keeps `pi`'s orientation explicit.
- **Not interior operators (the FAIL-reachable readings): raw set-images of
  `pi`.** The direct image `A -> pi(A)` and the preimage `A -> pi^{-1}(A)` are
  the literal set-actions of the point map. Neither is an interior operator, and
  the probe shows exactly which axioms each breaks. This is a category mismatch
  (`pi` is a point map), NOT a modal sub-S4 result -- but it is what gives the
  gate teeth, and (see the proposal) the direct-image reading is itself a
  publishable companion negative on the retraction algebra.

The verdict below is reported for the faithful knowledge-modality reading and
cross-checked on the orientation-faithful variant.

## 3. Which branch fired: PASS (all four axioms, on three principled interiors)

All checks run on the frozen T19 configuration space (past bit `p`, future bit
`u`; four configs), exhaustively over the full powerset (all subsets, all pairs).

- **Faithful A*(R)-accessible interior (full config space).** The kernel of
  `pi` partitions the four configs by the past bit into TWO blocks
  `{(0,0),(0,1)}` and `{(1,0),(1,1)}`. The induced interior satisfies all four
  axioms and is NON-DEGENERATE (a proper open block exists). PASS.
- **Excluded future subspace (the object T19's separation is about).** On the
  future-config space the A*(R)-indistinguishability partition is the SINGLE
  all-of-X block, so the interior is the INDISCRETE one:
  `int(A) = X` if `A = X`, else `int(A) = empty`. It satisfies all four axioms
  (the indiscrete topology is a genuine topology), but it is the DEGENERATE S4
  modality: R can necessitate only tautologies about its own finality future.
  This is exactly the content of T19 -- R certifies nothing contingent about
  its future from within A*(R) -- and it is honest to state that the S4
  structure on the excluded subspace is trivial. PASS (degenerate).
- **Orientation-faithful `pi`-stable interior.** `int(A) = A cap pi^{-1}(A)`
  satisfies all four axioms as well (idempotent because `pi.pi = pi`;
  meet-preserving because `pi^{-1}` preserves intersections; contractive by
  construction). PASS.

Because all three principled interior constructions satisfy all four Kuratowski
axioms, the ROUTING VERDICT is **PASS -> S4-interior-operator title LICENSED**.

### Teeth (the FAIL branch was reachable)

The same four axioms, applied to `pi`'s raw set-images, FAIL as predicted:

- **Direct image** `A -> pi(A)` fails **K1** (`pi(X) = image(pi) != X`) and
  fails **K4** meet-preservation on the witness `A = {(0,0),(1,1)}`,
  `B = {(0,1),(1,0)}`: `pi(A cap B) = pi(empty) = empty`, but
  `pi(A) cap pi(B) = {(0,0),(1,0)}`, a strict inclusion. This is the exact
  shape of a NON-normal (sub-S4) modality -- the material a FAIL branch would
  have published.
- **Preimage** `A -> pi^{-1}(A)` fails **K2** contractivity (e.g.
  `pi^{-1}({(0,0)}) = {(0,0),(0,1)}` is not a subset of `{(0,0)}`).

So the gate can and does register interior-axiom failures. PASS is therefore a
computed result about the faithful construction, not a rubber stamp.

## 4. What PASS means, stated precisely (and what it does not)

- **Licensed:** the paper may call first-person finality (the A*(R)-accessible
  knowledge operator induced by the causal-past retraction) an **S4 interior
  operator**. It satisfies the four Kuratowski axioms; its open sets are the
  A*(R)-accessible predicates; `pi`'s idempotency is exactly the S4 axiom
  `int int A = int A`.
- **Non-degenerate content is on the full causal order, not the excluded
  future.** On the future subspace the operator is the indiscrete (trivial) S4
  modality. The paper must locate the substantive S4 content on the full
  config/causal-order space (two open blocks), and state plainly that the
  excluded-future interior is degenerate. Overselling the future subspace as
  carrying rich S4 structure would be false.
- **S4, not automatically S5.** The kernel-partition reading is symmetric and
  would be S5; the orientation-faithful `pi`-stable reading keeps `pi`'s
  antisymmetry and is properly S4. The paper should adopt the oriented
  construction to preserve the causal before/after datum the lemma prized (the
  orientation obstruction that made `pi` not an involution).

## 5. Embargo (unchanged, restated)

The broad headline "an observer can certify that its own present is final" (or
"certify your own present") remains **EMBARGOED**. That headline needs an
all-finite-graphs quantifier: that the S4-interior structure holds for every
finite record graph, not only the frozen T19 fixture. The present result is
fixture-grade on T19. Nothing here establishes the universal quantifier, and
nothing here asserts the broad headline. The licensed title is the narrower,
honest one: first-person finality is an S4-interior operator on the T19-grade
construction, with the universal claim left open.

## 6. Council pass (inline, five lenses)

- **Category, sheaf, and obstruction lens (attack the interior claim).** The
  Kuratowski axioms are exactly the definition of an interior operator, i.e. an
  S4 necessity modality, and every finite topology / Alexandrov preorder induces
  one. The load-bearing move is the construction fork: the axioms hold for the
  interior whose opens are the `pi`-saturated sets, and independently for the
  `pi`-stable interior. The honest residue, flagged: on the EXCLUDED future
  subspace the interior is indiscrete (degenerate). That is not a defect of the
  test, it is a true fact about T19; the paper must not launder it into rich
  structure.
- **TaF-native finality theorist (T19 fidelity).** The extraction is faithful
  and moves nothing. `pi` is the A*(R) causal-past retraction from the frozen
  lemma; the accessible predicates are its saturated sets; the degenerate
  future interior restates "R cannot certify its own finality from within
  A*(R)" (the T19 separation). C1 stays `weakened`; no T19/T92 row moves.
- **Complexity and cryptography lens (block the relabel).** PASS is a modal-
  logic typing result (S4), not a temporal or hardness claim. It does not assert
  any complexity separation beyond what T19 already records, and it does not
  license a public-cycle or "certify your present" relabel. The embargo holds
  precisely because the universal quantifier is a separate, unmet burden.
- **Philosopher of science (what could kill it, where is it protected).** The
  FAIL branch was genuinely reachable (the direct-image reading fails K1 and
  K4), so PASS is exposed, not protected. The one place the result could be
  oversold is the future subspace; the doc pre-empts that by naming the
  degeneracy. The kill for the S4 title would be an axiom failure on a faithful
  interior; none occurred.
- **Adversarial referee (answered in writing).** (i) Charge: you chose the
  construction that passes. Answer: the fork is named, both faithful
  constructions pass, and the passing constructions are the STANDARD epistemic
  interior and its oriented variant, not ad hoc choices; the non-interior
  set-image readings are computed and shown to fail. (ii) Charge: PASS is
  trivial because any partition gives an interior. Answer: correct that the
  positive is structurally unsurprising, which is exactly why the informative
  content is the fork plus the degeneracy on the excluded future plus the S4
  (not S5) orientation choice; the paper's honesty burden is there, not in
  claiming novelty for the axioms. (iii) Charge: this smuggles the embargoed
  headline. Answer: no; the licensed title is fixture-grade S4-interior, the
  all-finite-graphs quantifier is explicitly left open, and the broad headline
  is not asserted anywhere.

## 7. Receipts

- Probe: `tests/involution_typing_probe.py`, `kuratowski_interior_checks`
  section (`[K]` tag), 17 checks, HEADLINE
  `13 [E] + 11 [F] = 24  |  [K] Kuratowski gate = 17 PASS  (setup [T] = 5; scope [P] = 4 excluded) ALL PASS`,
  exit 0, deterministic (double-run byte-identical), seed 20260720 (for the
  pre-existing seeded identity only; the Kuratowski checks are exhaustive, not
  sampled).
- Frozen fixture: `models/t19_phenomenal_bridge_separation.py` (the causal
  diamond and the ValueError-on-future mechanism).
- Upstream: `explorations/involution-typing-lemma-2026-07-20.md` (the
  retraction `pi`, T-REFUTE, orientation obstruction),
  `explorations/partial-future-information-involution-audit-2026-07-21.md`.
- Steering: `explorations/2026-07-22-wave1-triple-diamond-prep-steering.md`
  (TaF-3 wake directive).

## 8. Boundary

Exploration tier; Track-2 (paper lane), subordinate. claim/canon/posture:
none; no claim/verdict/status movement; no external action; no publication.
New files only: this exploration, the probe extension (a new section in the
existing `tests/involution_typing_probe.py`), and a companion steward proposal
`steward/PROPOSAL-kuratowski-interior-paper-route-2026-07-22.md`. Fixture grade
throughout (the four configs of the frozen T19 diamond; exhaustive powerset
checks). Named residues: (i) the all-finite-graphs quantifier for the broad
headline remains UNMET and the headline stays embargoed; (ii) the excluded-
future interior is the degenerate indiscrete S4 modality, so the paper's
substantive S4 content must be located on the full causal order; (iii) the
S4-vs-S5 choice is a paper decision, resolved here in favor of the oriented
(S4, antisymmetry-preserving) `pi`-stable construction to keep the causal
orientation datum. Nothing here moves C1, T19, T92, the Complexity Ledger, the
Canon Index, or public posture.

## 9. PROPOSAL TO STEWARD (for ratification; no claim movement requested)

Outcome of the TaF-3 paper-routing gate (Wave-1 steering): **Kuratowski PASS.**

The causal-past retraction `pi`, read as its faithful accessible-knowledge
interior (open sets = the `pi`-saturated / A*(R)-accessible subsets), satisfies
all four Kuratowski interior axioms on the frozen T19 fixture; the
orientation-faithful `pi`-stable interior does too. The raw set-image readings
of `pi` are not interior operators and fail specific axioms (teeth).

**Recommendation:** route the first-person-finality paper to an **S4-interior-
operator framing** and license an S4-interior title at FIXTURE GRADE, with three
mandatory honesty conditions written into the paper:

1. adopt the ORIENTED (S4, not S5) `pi`-stable construction so the causal
   before/after datum is preserved;
2. locate the substantive S4 content on the FULL causal order and state
   explicitly that the excluded-future interior is the DEGENERATE (indiscrete)
   modality;
3. keep the broad "certify your own present is final" headline EMBARGOED until
   the all-finite-graphs quantifier is established; the licensed title is the
   fixture-grade S4-interior claim only.

**Companion negative (secondary, publishable):** the retraction-algebra framing
survives as secondary material -- the raw direct-image action of `pi` is a
non-normal (sub-S4) monotone operator that fails K1 and K4. This is the result
the FAIL branch would have led with; it can appear as a contrast that sharpens
why the SATURATED interior (not the raw retraction) is the right knowledge
modality.

No C1, T19, T92, Complexity Ledger, Canon Index, public posture, or external
action moves. This is a paper-lane (Track-2) disposition reported up to the
steward; it does not touch the Track-1 North Star posture (Lane 1 still waits
for a physical source packet or an independently specified operator-grade lift).
