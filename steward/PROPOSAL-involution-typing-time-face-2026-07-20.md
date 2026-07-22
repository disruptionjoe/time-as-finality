---
artifact_type: steward_proposal
status: draft_for_ratification
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (cross-repo: boundary-law time-face involution lemma)"
subject: "T19 involution-typing lemma -- outcome T-REFUTE (fixture grade)"
gated_by: agent-runs/RUN-20260720-184304-t19-involution-typing-mailbox.md
sources:
  - explorations/involution-typing-lemma-2026-07-20.md
  - tests/involution_typing_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# PROPOSAL TO STEWARD -- T19 involution-typing lemma disposition

## Ask

Ratify the disposition of the gated TaF-local involution-typing lemma
(`RUN-20260720-184304-t19-involution-typing-mailbox.md`). This is a
new-file proposal only; no claim, verdict, or status has been moved. The
steward decides ratification.

## Outcome: T-REFUTE (a pre-declared success)

GU's diagonal-boundary parent needs, for its TIME face, an involution
`alpha` on the finality label whose `alpha`-even maps are EXACTLY the
`A*(R)`-computable maps. Built from TaF's frozen T19 apparatus and
machine-checked, the answer is: **no such involution exists for T19's
fixture.** The coincidence `alpha`-even `==` `A*(R)`-computable holds IFF
the excluded causal-future carries a single `Z/2` witness (`k = 1`). T19
has `k >= 2` independent witnesses (`e_E1`, `e_E2`), so the exclusion
engine is strictly more general than any fixpoint-free flip under the frozen
full-forget construction.

The more-general structure is named exactly: T19 excludes by the
**causal-past retraction** `pi` (restriction to R's accessible down-set) --
an IDEMPOTENT, non-invertible, oriented forgetting of the future up-set.
It differs from a fixpoint-free involution on two independent axes:

1. orbit-cardinality: `pi`'s indistinguishability class has size `2^k`;
   an involution's orbits have size `<= 2` (coincide only at `k = 1`);
2. orientation: `pi . pi = pi` (retraction) vs `alpha . alpha = id`
   (order-2 automorphism); the causal cut is antisymmetric/directed, a
   fixpoint-free flip is symmetric.

## The five gating requirements, discharged

1. explicit finality-label object + involution: the future-config space
   `X = 2^k` of `R_self_finality` witnesses; candidates `alpha_swap`
   (witness swap) and `alpha_flip` (finality-value flip). DONE.
2. exhaustive finite check of the full-forget coincidence: machine-verified that
   `alpha`-even `==` `A*(R)`-computable IFF `k <= 1` (brute-force
   involution enumeration for `n <= 8`; orbit-count fact for larger `k`).
   DONE.
3. fixpoint-freeness + odd/even typing: `alpha_swap` fails fixpoint-free
   (fixed configs `b_E1 = b_E2`); `alpha_flip` is fixpoint-free but its
   even-class is strictly larger than the `A*(R)` class. DONE.
4. external-cure + fixed-point dissolution control: the `k = 1` EXHIBIT
   toy (fixing the bit reads the odd datum; `alpha = id` dissolves the
   obstruction). DONE.
5. same-engine vs distinct-engine comparison for the frozen fixture: DISTINCT
   -- causal placement is the causal-past retraction `pi`, strictly more
   general under full forgetting. DONE.

## Recommendation

Ratify as **CLOSED-REFUTED at fixture grade.** The GU/TaF time-face
unification is LEG-deep (shared first-person NO / third-person YES
conclusion shape), not MECHANISM-deep. This CONFIRMS the ledger's
causal-boundary reading of T19 (richer than an involution, not secretly
one); it does not weaken T19 or T92. C1 stays `weakened`.

Reopener (single, named): an operator-grade lift in which `A*(R)` retains
partial coarse future information. The 2026-07-21 follow-up audit corrects
the former stability prediction: the lifted computable class equals the
involution-even class exactly when the retained-information fiber partition
equals the involution-orbit partition. An aligned lift can therefore restore
coincidence; its information map must be fixed independently to avoid a
circular construction.

## Receipts

- `explorations/involution-typing-lemma-2026-07-20.md` (construction,
  outcome, coincidence check, five-lens council, boundary).
- `tests/involution_typing_probe.py` -- HEADLINE
  `13 [E] + 11 [F] = 24 (setup [T] = 5; scope [P] = 4 excluded) ALL PASS`, exit 0,
  deterministic, seed 20260720.
- `explorations/partial-future-information-involution-audit-2026-07-21.md`
  -- exact orbit-alignment criterion with aligned and misaligned controls.

## Cross-repo courtesy note (awareness only; no GU claim movement requested)

GU's Appendix-A lemma target (does the T19 causal horizon hide a
fixpoint-free flip?) resolves NO at fixture grade. GU's realizable
single-`Z/2` label object (L1 assembly) is exactly the `k = 1` case, which
here registers T-EXHIBIT -- so GU's structure and TaF's coincide only on
that degenerate fiber. GU may record, at its discretion, that the
time-face is leg-deep, not mechanism-deep. No TaF claim moves; the one-way
rule is respected.
