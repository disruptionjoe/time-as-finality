# T442 — Interpretation and Connections (post-hostile-review)

> Exploration / synthesis note. Not a claim promotion. Reads the *surviving*
> content of T442 after the 2026-07-03 hostile review
> (`audits/2026-07-03-t442-hostile-review.md`) and traces its connections to the
> broader program. Cross-repo material below is **stress-test framing, not
> evidence**, carries the single-process-ceiling caveat, and makes **no identity
> claim** (per `Coordination - Tri-Repo Division of Labor.md`).

## What actually survived

After review, T442 does **not** give a new topological thermodynamic bound (the
`λ(G)` surcharge was refuted by a spanning-tree achievability construction). One
conceptual result and one relocated lead survive:

1. **Finality = the denied purifier.** T396 could drive the consensus cost to
   zero by *keeping the reconciliation transcript* (the Bennett reversible
   escape). T442's durable point: for a record to be **final and objective**, the
   transcript cannot be kept — a retained purifying copy is exactly an undo-handle,
   so keeping it means the record is *not* final. Therefore the fan-in erasure
   `H(X|V)` is genuinely paid precisely *because* the system is denied the
   external purifying reference that would make the erasure reversible.

2. **Redundancy's role in finality is feasibility, not cost.** The topological
   intuition, correctly located, is Dolev's fault-tolerance condition (robust
   consensus needs connectivity `≥ 2f+1`) — a *feasibility* requirement on
   whether robust finality is achievable at all, not a dissipation surcharge.

## Interpretation: this is the program's central motif, reached from a new angle

The program's recurring finding (scope theorem / Declarability Lemma;
`papers/drafts/finality-as-a-limit-phenomenon-synthesis-2026-07-02.md`) is that
**physical/sharp/final structure is not a finite-closed single-instance fact** —
in a closed system the discriminating datum is always co-present, and forcing a
genuine boundary requires *leaving* the closed single instance (openness, a
limit, an assumption, a symmetry no-go).

T442's surviving point is a fresh, independent instance of exactly that:

- In a closed system that *retains* the reconciliation transcript, the record is
  reversible — the "past" is not hard to undo, because the undo-information is
  co-present. This is the consensus-flavored twin of T110 (no strict finality
  monotone in a closed reversible system) and of the Declarability Lemma (the
  separating datum is always co-present in the closed model).
- Finality appears **only** when the purifier is *excluded* — i.e., only in the
  open regime, only relative to a denied exterior. Finality is a boundary
  phenomenon: it is defined by what is kept *outside* (absent), not by anything
  the interior contains.

So T442 re-derives, from distributed systems + Landauer, the same shape the
capability-boundary and canonicity routes reached: **finality/physicality lives
at the boundary between a system and an excluded exterior, never inside a
self-contained finite instance.** That is a third independent arrival at the
program's residue — which, under the single-process ceiling, is a *target* worth
noting, not corroboration.

## Connections to the lead line (A1, D1, H7)

- **A1 (distributed-systems finality analogy):** sharpened. The honest transfer
  from consensus is *not* a thermodynamic cost law; it is (a) the export/erasure
  distinction (finality forbids the retained purifier) and (b) Dolev feasibility
  (robustness needs connectivity). Both are about *whether* an objective record
  can exist, framed in the distributed idiom.
- **D1 holder-redundancy axis:** the review clarifies this axis is a
  *robustness/feasibility* dimension (survive `f` holder failures ⇒ connectivity
  `≥ 2f+1`), **not** a thermodynamic-cost dimension. Prior hand-waving that "more
  holders cost more" is wrong (already shown by T396's already-consensus zero);
  more holders buy fault-tolerance, not dissipation.
- **D1 reversal-cost axis:** T442 does not ground it thermodynamically (the
  topological floor failed). It leaves the axis where T142/T439 left it: reversal
  cost is real per-instance but is kinetic/resource accounting, not a new law.
- **H7 (finality-induced direction):** untouched and correctly avoided. T442 was
  framed as a resource/definalization statement, not a scalar arrow, so it never
  entered the H7 absorber field. The surviving "denied purifier" point is
  *consistent* with H7's weakened_conditional status (an arrow needs openness /
  an excluded environment) but adds no arrow evidence.

## The boundary residue, stated for cross-repo eyes (stress-test only)

The tri-repo residue: *"a bounded system, complete in itself, cannot supply one
specific thing from inside; the missing thing lives at its boundary; the honest
ledger for that boundary is what the region can do."* T442's surviving point adds
a **negative/withholding** version of that shape: finality requires the boundary
to *withhold* the purifier (an excluded exterior), whereas GU's boundary
*supplies* content (chirality/generation count) and TI's boundary is *crossed* by
novelty. Whether "withheld purifier," "supplied count," and "crossed novelty" are
the same boundary object, duals, or merely rhyming is an open stress-test
question — routed to the sibling mailboxes, with no identity claim and the
single-process caveat intact. See:

- `CapacityOS/mailboxes/gu-formalization/20260703-t442-finality-excluded-exterior-to-gu-formalization.md`
- `CapacityOS/mailboxes/temporal-issuance/20260703-t442-definalization-as-issuance-crossing-to-temporal-issuance.md`

## Honest bottom line

T442's exciting form is dead; its sober form is a clean, independent restatement
of the program's own central motif (finality is a boundary/openness phenomenon,
not a closed-instance fact) plus a correctly-located feasibility lead (Dolev).
That is modest but real, and it is exactly the kind of demotion-with-residue the
Method treats as progress.
