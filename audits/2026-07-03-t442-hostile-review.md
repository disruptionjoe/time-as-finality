# Hostile Review — T442 Consensus Definalization Bound (2026-07-03)

> Adversarial pass on the load-bearing claim behind T442, requested after the
> v0.1 build. Verdict up front: the flashy part is **refuted**; a narrower
> conceptual point **survives**. This is a demotion, recorded as first-class
> progress per the Method guidelines. No CLAIM-LEDGER / TESTS.md / ROADMAP /
> North Star movement.

## What was on trial

T442 v0.1 reported that, for a *distributed objective final record*,
definalization carries two costs:

1. **forced erasure** `H(X|V)` — the fan-in collapse, made irreducible because
   the T396 transcript-export escape is illegitimate for a final record; and
2. **a topological reversal floor** `λ(G)` (edge connectivity), added to (1), so
   that at fixed k the total "definalization floor" orders by graph:
   `line = star = 5 < ring = 6 < complete = 8` bits.

Claim (2) — "network shape sets an irreducible cost" — was the headline and the
declared load-bearing exposure. This review attacks it.

## The attack (achievability construction)

A lower bound must hold for **every** protocol. Exhibit one protocol that beats
`λ(G)` and the floor falls.

**Spanning-tree reversible protocol.** Run consensus so it is reversible along a
BFS spanning tree from a root: each non-root node keeps an O(1) provenance stub
(its parent + its own pre-merge bit). To definalize, walk the tree backward,
uncompute each merge from its stub (Bennett-reversible, zero heat), then erase
the `k−1` stubs. Probe: `_local/t442_reversal_probe.py`.

Result (k=5, majority):

| graph | λ(G) | T442 claimed floor (forced+λ) | tree edges used | achievable (topology-independent) |
|---|---:|---:|---:|---:|
| line | 1 | 5.0 | 4 | 8.0 |
| star | 1 | 5.0 | 4 | 8.0 |
| ring | 2 | 6.0 | 4 | 8.0 |
| complete | 4 | 8.0 | 4 | 8.0 |

The achievable protocol uses a spanning tree — `k−1` edges — for **every**
connected graph. The extra edges that make the ring and complete graph denser
(`λ = 2, 4`) are **never used**. A cost you can avoid is not a floor.

## Verdict

**REFUTED — the topological surcharge (claim 2).** `λ(G)` is the wrong invariant.
It was imported from an intuition about *disconnecting* a graph (min-cut /
robustness), but consensus and its reversal only ever traverse a spanning tree,
whose size (`k−1`) is topology-independent for connected graphs. T442 v0.1
conflated "the graph *has* more edges" with "you must *pay* for more edges." The
`line < ring < complete` ordering is an artifact of choosing edge-connectivity
rather than a reachability quantity; it is not a physical cost.

This is precisely the demotion T396 predicted for this rung: *"entropy
bookkeeping plus ordinary communication overhead."* Communication is ordinary and
additive (`~k−1`), not a new topological law.

**SURVIVES (reinterpreted) — the export-escape point (claim 1, conceptual only).**
The one durable gain: T396's "export the transcript → cost 0" control keeps
information that can reverse the record, which by this program's own definition
of finality ("the past is what has become hard to undo") means the record is
**not final**. So for a genuinely *final, objective* record the `H(X|V)` fan-in
erasure must actually be paid — it cannot be exported to zero. This is a correct
sharpening of T396's boundary, but it yields **no new number** beyond `H(X|V)`
and **no structure**. It is a reinterpretation, not a bound.

## Where the topological intuition legitimately lives

The instinct that "network structure matters for finality" is not wrong — it was
mis-located. Its correct home is **fault-tolerant feasibility**, not heat cost:
Dolev's theorem (1982) says robust consensus against `f` faulty holders requires
graph connectivity `≥ 2f+1`. That is a *feasibility* condition (can robust
finality be achieved at all), a known distributed-systems result, and carries no
thermodynamic surcharge. If topology is to re-enter Direction C, it enters here —
as a redundancy/robustness requirement on the D1 holder-redundancy axis — not as
a Landauer-style cost.

## Net effect on Direction C rung 1

- The positive complement of T110 does **not** yield a new topological
  thermodynamic bound. Rung 1, as a bid for new physics, is **demoted** to
  entropy bookkeeping (`H(X|V)`) plus ordinary communication overhead — matching
  T396's stated demotion condition.
- What is banked: (a) a clean conceptual correction to T396 (the export escape is
  illegitimate for objective/final records, so `H(X|V)` is genuinely paid); and
  (b) a correctly-located open lead — topology → fault-tolerant feasibility
  (Dolev), a candidate D1 holder-redundancy result, distinct from any heat cost.
- Tier: the T442 v0.1 headline verdict string (`..._SURCHARGE_IRREDUCIBLE...`)
  **overstates and is superseded by this review.** The computed quantities in the
  model and tests remain arithmetically correct (λ(G), H(X|V) are what they are);
  only the *interpretation* of `forced + λ` as a thermodynamic floor is retracted.

## Recommended next (if Direction C continues)

1. Do **not** rebuild the topological-cost claim. Drop `λ(G)` as a cost term.
2. If pursuing thermodynamics: the only honest object left is finite-time /
   reliability excess-work on a real substrate (stochastic thermodynamics), which
   T439 already gates hard — likely absorbed as kinetic/resource overhead (T152).
   Low expected yield; say so before spending on it.
3. If pursuing topology: pivot to the Dolev feasibility lead as a D1
   holder-redundancy / A1 result — a *feasibility* theorem, not a cost. Higher
   integrity, cleanly framed, no thermodynamic overclaim.
4. Overall: Direction C's near-term "always-on credibility engine" value is lower
   than the 2026-07-01 audit hoped once the topological surcharge is gone. The
   honest read is that this rung mostly reproduces known results; escalate only
   the Dolev-feasibility reframe, and keep Direction A as the lead lane.

## Artifacts

- Probe: `_local/t442_reversal_probe.py` (confirms refutation).
- Under review: `results/T442-consensus-definalization-bound-v0.1-results.md`,
  `models/consensus_definalization_bound.py`,
  `open-problems/consensus-definalization-bound-direction-c.md`.
- Prior: `results/T396-consensus-cost-additivity-gate-v0.1-results.md` (predicted
  this demotion), `technical-reports/TECHNICAL-REPORT-finite-permutation-monotone-obstruction-v0.1.md` (T110).
