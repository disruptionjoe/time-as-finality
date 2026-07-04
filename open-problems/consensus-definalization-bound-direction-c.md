# Open Problem: The Consensus Definalization Bound (Direction C)

Status (updated 2026-07-03 after hostile review): **topological-surcharge form
REFUTED; downgraded to a conceptual correction of T396 plus one relocated lead.**
See `audits/2026-07-03-t442-hostile-review.md`. The theorem target below is kept
for the record with its refutation marked; do not rebuild the `λ(G)` cost claim.

## Post-review standing (read first)

- **Refuted:** the topological reversal floor `λ(G)`. A spanning-tree protocol
  reverses independent of `λ(G)` (`_local/t442_reversal_probe.py`), so it is not
  a lower bound. Direction C rung 1 does **not** yield a new topological
  thermodynamic law; it demotes to entropy bookkeeping (`H(X|V)`) + ordinary
  communication overhead — T396's predicted outcome.
- **Survives (conceptual):** T396's transcript-export escape is illegitimate for
  an objective *final* record (a retained transcript is an undo-handle ⇒ not
  final), so `H(X|V)` is genuinely paid. No new number.
- **Relocated lead (worth pursuing):** topology enters finality through
  **fault-tolerant feasibility** — Dolev (1982): robust consensus needs
  connectivity `≥ 2f+1`. This is a feasibility condition on the D1
  holder-redundancy axis, a candidate A1 result, and carries no heat cost. This
  is the only piece to carry forward, and not as thermodynamics.

## The target (kept for the record — topological cost form is refuted)

## The target

Fuse Landauer (erasure cost) with Lamport/FLP (consensus is communication-hard)
into a single lower bound on the cost of *finalizing and later definalizing* an
agreed record held redundantly by `k` separated observers.

Provisional statement (finite-witnessed in T442, not proven in general):

> For `k` holders on a connected communication graph `G` who acquire
> possibly-disagreeing observations and finalize a common record `V` as a
> **distributed objective record** — clean, robust local copies with the
> reconciliation garbage thermalised (no retained undo-handle) — the cost to
> reach and later definalize `V` is bounded below by
>
>   `W ≥ ( H(X|V) + λ(G) ) · kT ln 2`
>
> where `H(X|V)` is the fan-in erasure (now irreducible, because the T396
> transcript-export escape is incompatible with distributed local finality) and
> `λ(G)` is the edge connectivity of the communication graph (the topological
> reversal floor). The bound vanishes iff the record is pre-agreed, co-located
> (`k=1`), or garbage may be retained/exported — the broadcast / Darwinism limit.

## Why it is not yet a theorem

1. **Load-bearing exposure (unreviewed).** The claim that `λ(G)` is a genuine
   *reversal* cost rather than "ordinary forward communication overhead" (which
   T396 pre-labeled demotable) has not survived a hostile review. This is the
   first thing to attack.
2. **No achievability.** T442 computes a lower bound / cut invariant; no protocol
   is exhibited that meets `H(X|V) + λ(G)`. Tightness is open.
3. **(L2) is stipulated.** The thermodynamic reading is conditional on local
   thermalisation of reconciliation garbage. Without a substrate that *forces*
   L2, the bound is a resource statement, not an earned thermodynamic law — and
   a stipulated barrier would be absorbed by T152.

## Kill conditions

- If the reversal term collapses to a forward message count or to `k`-only
  scaling once achievability is modeled → demote to "entropy bookkeeping plus
  ordinary communication overhead" (T396's stated demotion), closing rung 1.
- If any construction expresses the bound as a scalar finality monotone → it
  collides with T110/T122 and must be reframed or dropped.
- If L2 can only be enforced by a finite kinetic barrier → T152 absorbs it.

## Path to earning it

1. Hostile review of exposure #1 (reversal vs forward communication).
2. Achievability companion protocol → toward internally-established tier.
3. A physical substrate forcing L2 → lifts thermodynamic reading; feeds
   Direction B's Tier-2 card and grounds T395's capability-relative boundary
   thermodynamically (per `audits/2026-07-01-high-gravity-research-directions.md`).
4. Translation into stochastic-thermodynamic language (finite-time / reliability)
   for an external register (PRL/PRX Quantum), per Direction C's ladder.

## Artifacts

- Spec: `tests/T442-consensus-definalization-bound.md`
- Model: `models/consensus_definalization_bound.py`
- Results: `results/T442-consensus-definalization-bound-v0.1-results.md`
- Prior gate this supersedes-with-geometry: `results/T396-consensus-cost-additivity-gate-v0.1-results.md`
- Boundary respected: `technical-reports/TECHNICAL-REPORT-finite-permutation-monotone-obstruction-v0.1.md` (T110)
