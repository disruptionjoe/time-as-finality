# T442 — Consensus Definalization Bound (Landauer × Lamport) — v0.1 results

> **⚠️ SUPERSEDED IN PART BY HOSTILE REVIEW (2026-07-03).** The headline verdict
> below (`..._SURCHARGE_IRREDUCIBLE...`) **overstates the result and is
> retracted.** The topological reversal term `λ(G)` was **refuted** by an
> achievability construction (`audits/2026-07-03-t442-hostile-review.md`,
> `_local/t442_reversal_probe.py`): a spanning-tree protocol reverses at a cost
> independent of `λ(G)`, so `λ(G)` is not a floor. What survives is a conceptual
> point only — see "Hostile review outcome" at the end. The computed quantities
> (`λ(G)`, `H(X|V)`) remain arithmetically correct; only their interpretation as
> a *thermodynamic floor* is withdrawn. Read the results below with that caveat.
>
> Recorded-tier / computed finite-witness. `TESTS.md`, `ROADMAP.md`,
> `CLAIM-LEDGER.md`, and the North Star map are untouched. No H7 promotion, no
> thermodynamic-arrow derivation, no general theorem, no public posture.

- Spec (frozen first): `tests/T442-consensus-definalization-bound.md`
- Model: `models/consensus_definalization_bound.py`
- Tests: `tests/test_consensus_definalization_bound.py` (16 tests, all pass)
- Artifact JSON: `results/T442-consensus-definalization-bound-v0.1.json`
- Builds on: T396 (consensus-cost additivity gate), T110 (closed-reversible
  monotone obstruction), T142 (thermodynamic erasure calibration), A1, D1

## Overall verdict: `DISTRIBUTED_DEFINALIZATION_BOUND_COMPUTED_SURCHARGE_IRREDUCIBLE_UNDER_LOCAL_FINALITY_NO_H7_PROMOTION`

Direction C's rung 1 was absorbed by T396 into ordinary entropy bookkeeping,
because T396's single-system model always permits the Bennett escape (export the
transcript → zero cost). T442 supplies the ingredient T396's Next Gate named,
**communication geometry**, and shows that for a *distributed objective final
record* the escape is physically unavailable, exposing a positive consensus term
in two pieces:

1. the `H(X|V)` fan-in erasure becomes **irreducible** (cannot be exported away
   without destroying finality); and
2. **definalization** carries a **topological** reversal-cost floor `λ(G)` (edge
   connectivity) that T396's single-system ledger structurally could not
   represent.

The term vanishes in exactly the broadcast / Darwinism limits, which is the
model's own kill control and reproduces T396's zeros.

## T396 reproduction (single-system regime — the Bennett escape control)

| fixture | `H(X\|V)` bits | per-holder reset | export cost | matches T396 |
|---|---:|---:|---:|:--:|
| root_copy_k2…k6 | 1, 2, 3, 4, 5 | = k−1 | 0 | ✅ (`k−1` floor) |
| majority_k3 | 2.000000 | 2.433834 | 0 | ✅ (reset overcounts joint) |
| majority_k5 | 4.000000 | 4.480191 | 0 | ✅ |
| already_consensus_k5 | 0.000000 | 0.000000 | 0 | ✅ (holder count refuted) |
| single_error_k5 | 2.321928 | 3.609640 | 0 | ✅ |

Bit-for-bit agreement with the registered T396 numbers. The export control is
free everywhere, exactly as T396 found.

## New content — distributed objective final record (export closed by L1+L2)

Same k=5 majority task, same input distribution, same expected disagreement —
**only the communication graph changes**:

| fixture | graph | forced erasure (bits) | λ(G) | total floor (bits) | thermo floor (kT) | verdict |
|---|---|---:|---:|---:|---:|---|
| dist_majority_k5_line | line | 4.000 | 1 | 5.000 | 3.466 | surcharge irreducible |
| dist_majority_k5_star | star | 4.000 | 1 | 5.000 | 3.466 | surcharge irreducible |
| dist_majority_k5_ring | ring | 4.000 | 2 | 6.000 | 4.159 | surcharge irreducible |
| dist_majority_k5_complete | complete | 4.000 | 4 | 8.000 | 5.545 | surcharge irreducible |
| dist_majority_k3_complete | complete | 2.000 | 2 | 4.000 | 2.773 | surcharge irreducible |
| dist_single_error_k5_ring | ring | 2.322 | 2 | 4.322 | 2.996 | surcharge irreducible |

The reversal term orders strictly by topology at fixed k / task / disagreement:
`λ(line)=λ(star)=1 < λ(ring)=2 < λ(complete)=4`. That is a genuine
consensus-structure term — a function of the communication geometry, **not of k
alone** — which is precisely what a single-system entropy ledger cannot express.

## Kill controls (surcharge MUST vanish — Darwinism / broadcast limit)

| control | result | reading |
|---|---|---|
| pre-agreed inputs (k=5, complete) | 0 | already objective; nothing to finalize |
| co-located single site (k=1) | 0 | no distribution ⇒ no consensus term |
| export available (all T396 fixtures) | 0 | Bennett escape ⇒ record not final |

All three vanish, reproducing T396 and matching Quantum Darwinism: redundant
*agreeing* records carry no surcharge; the surcharge is the price of finalizing
*disagreement* into an objective distributed record.

## Absorber checks passed (13/13)

- Reproduces T396 (5 checks) — root-copy `k−1`, majority-k3 joint/reset,
  single-error-k5, already-consensus zero, export free everywhere.
- Floor irreducible under local finality; reversal term topological and
  not-k-only; total floor ordered by topology; distributed strictly exceeds the
  single-system escape.
- Kill controls vanish (pre-agreed, co-located).
- Reversal bound independent of a dummy `barrier_height` field → **not** a T152
  kinetic/finite-barrier absorber. It is a graph cut invariant, not a
  T116 exported-history ledger, so it dodges the standing H7 arrow absorbers.

## What this earns / does not earn

**Earns (recorded tier, pending hostile review):** a computed finite-witness
separation showing that (i) T396's zero depended on an export assumption
incompatible with distributed objective finality, and (ii) consensus
definalization carries an irreducible, topological reversal-cost lower bound.
This is the first positive movement on Direction C past T396, and it gives the
D1 reversal-cost axis a concrete, graph-dependent number.

**Does not earn:** H7 promotion or any physical-arrow claim (framed strictly as a
resource / reversal-cost bound); a general theorem (finite witnesses + a
cut-argument sketch, no achievability/tightness proof); a proven thermodynamic
law (the `× kT ln 2` reading is conditional on (L2) local thermalisation, a
stated assumption); CLAIM-LEDGER / TESTS.md / ROADMAP / North Star movement.

## Honest exposure (what a hostile reviewer will attack first)

1. **"The reversal term is ordinary forward communication overhead."** T396
   pre-labeled communication overhead as demotable. The defense: `λ(G)` is a
   lower bound on *definalization* (reverse) that survives the export escape and
   is topological, not a forward message count — but this needs an adversarial
   pass. **This is the load-bearing claim; treat it as unproven until reviewed.**
2. **"Keep distributed garbage — global reversibility, zero heat."** True
   globally; the answer is that global-but-not-local reversibility means the
   record is not *locally* final. Whether "local finality" is the correct
   definition is a modeling choice (L2), stated explicitly, not proven.
3. **Achievability unproven.** The bound is a lower bound; no protocol is shown
   to meet `forced_erasure + λ(G)`.

## Recommended next

1. Run the hostile review on exposure #1 before any A1/D1 ledger movement.
2. Add an achievability companion (protocol meeting the bound) → would lift
   toward internally-established tier.
3. Build the (L2) substrate (forced local thermalisation) → lifts the
   thermodynamic reading from conditional to earned, and doubles as Direction B's
   Tier-2 re-entry.

## Reproduction

```bash
python -m unittest tests.test_consensus_definalization_bound -v
python -m models.consensus_definalization_bound --write-results
python -m json.tool results/T442-consensus-definalization-bound-v0.1.json
python _local/t442_reversal_probe.py   # the refutation probe
```

## Hostile review outcome (2026-07-03) — read this

Full review: `audits/2026-07-03-t442-hostile-review.md`.

- **Refuted:** the topological reversal surcharge `λ(G)`. A spanning-tree
  reversible protocol definalizes using only `k−1` edges for every connected
  graph, at a cost independent of `λ(G)`; the extra edges of ring/complete are
  never used, so they cannot be a floor. The `line < ring < complete` ordering
  was an artifact of picking edge-connectivity rather than a reachability
  quantity — not a physical cost. This is the demotion T396 predicted: entropy
  bookkeeping plus **ordinary** communication overhead.
- **Survives (reinterpreted, conceptual only):** T396's "export → 0" escape is
  illegitimate for a distributed *objective final* record, because a retained
  transcript is an undo-handle (⇒ not final). So `H(X|V)` is genuinely paid — but
  this is a reinterpretation of T396, yielding no new number or structure.
- **Relocated lead:** the topology intuition belongs to fault-tolerant
  *feasibility* (Dolev 1982: robust consensus needs connectivity `≥ 2f+1`), a
  known result on the D1 holder-redundancy axis — a feasibility condition, not a
  heat cost. This is the only piece worth carrying forward, and not as
  thermodynamics.
- **Net:** Direction C rung 1 does not deliver a new topological thermodynamic
  bound. Standing tier of the topological claim: **demoted / not earned.** The
  conceptual export-escape correction stands at recorded tier.
