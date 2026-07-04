# T442: Consensus Definalization Bound (Landauer × Lamport)

> Recorded-tier / computed finite-witness. Hostile review queued. This is the
> first **positive** swing on Direction C's rung 1 (the positive complement of
> T110) that clears the T396 absorption. It targets A1 and the D1 reversal-cost /
> holder-redundancy axes. It does **not** claim H7, a general theorem, or a new
> physical law, and does not move CLAIM-LEDGER / TESTS.md / ROADMAP / North Star.

## Target Claims

- **A1** (distributed-systems finality analogy) — supplies a quantitative,
  topological reversal-cost lower bound rather than a bounded impossibility
  witness.
- **D1 reversal-cost axis** — the audit's named "most hand-waved axis"; this
  gives it a computed lower bound tied to communication geometry.
- **D1 holder-redundancy axis** — shows redundancy alone is not a cost (T396),
  but redundancy under *distributed local finality* is.
- Positive complement of **T110** (finite closed-reversible monotone
  obstruction): the object T110 forbids in a closed reversible system reappears
  in the open/distributed regime as an irreducible resource lower bound, not a
  scalar monotone.

## Setup

T396 established that in a single-system framing the minimal consensus cost is
ordinary entropy reduction `H(X) − H(V) = H(X|V)`, that a holder-count-only floor
is refuted by already-consensus inputs, and that **a full-transcript export
control has zero closed-reversible cost in every fixture** (the Bennett escape).
T396's Next Gate asked for the missing ingredient: *communication geometry*.

T442 adds it. A **distributed objective final record** is `k` holders at separate
sites, each carrying a clean, robust copy of the outcome (Quantum-Darwinism
sense). This carries two properties absent from T396's single-system model:

- **(L1) locality** — no global site holds "the transcript"; finality requires
  the value present at `k` separated sites.
- **(L2) no-undo-handle** — a record co-present with the reconciliation garbage
  that could reverse it is, by definition, not final. Finality = the garbage is
  thermalised, not retained.

Under (L1)+(L2) the export escape is unavailable, and the model scores, for each
finite fixture, declared **before** scoring (per T439 discipline):

- `single_system_floor_bits = H(X|V)` (reproduces T396);
- `export_escape_cost_bits = 0` (reproduces T396's Bennett control);
- `forced_erasure_bits` — equal to `H(X|V)` but now **irreducible** because
  export is closed under (L1)+(L2);
- `edge_connectivity λ(G)` — the topological reversal floor: minimum
  re-communication to isolate a value-holder so it cannot re-broadcast;
- `total_definalization_floor_bits = forced_erasure + λ(G)`, and its
  thermodynamic reading `× kT ln 2` (conditional on (L2)).

Fixtures: T396 reproductions (root-copy, majority-k3/k5, already-consensus,
single-error); the same k=5 majority task across `line / star / ring / complete`
graphs to isolate topology at fixed k and disagreement; and kill controls
(pre-agreed, co-located k=1).

## Success Criteria

- Reproduce T396 exactly: root-copy floor `= k−1`; majority-k3 joint floor `2.0`
  with per-holder reset `≈ 2.433834` (overcount); single-error-k5 `≈ 2.321928`;
  already-consensus `= 0`; every export-regime fixture `= 0`.
- Under distributed local finality, the `H(X|V)` floor is positive and marked
  irreducible for genuine-disagreement, connected, `k ≥ 2` fixtures.
- The reversal term is **topological**: at fixed k=5 / task / disagreement,
  `λ(line)=λ(star)=1 < λ(ring)=2 < λ(complete)=4`, so the total definalization
  floor is strictly ordered by graph structure — a consensus-structure term that
  is not a function of `k` alone (the thing T396 could not see).
- The surcharge **vanishes** in exactly the broadcast/Darwinism limits:
  pre-agreed inputs, co-located `k=1`, or export-available.
- The reversal bound is independent of a dummy kinetic `barrier_height` field
  (it is a graph invariant) → not a T152 finite-barrier absorber.

## Failure Criteria (demotion to "entropy bookkeeping plus overhead")

The artifact demotes Direction C's rung 1 if:

- the distributed floor collapses to `H(X|V)` with no term beyond it once
  communication is admitted (i.e., the reversal term is zero or `k`-only);
- the surcharge fails to vanish in the pre-agreed / co-located / export limits
  (would mean it is an artifact, not a consensus term);
- the reversal term tracks a kinetic/barrier parameter (T152 absorber) or an
  exported-history ledger (T116 absorber) rather than graph topology;
- it can only be stated as a scalar finality monotone (would collide with T110 /
  T122) rather than a resource lower bound.

## Known Physics Constraints

Every mechanism is standard: Landauer `kT ln 2` per erased bit; Bennett
reversible computing (kept garbage ⇒ zero heat); graph edge-connectivity /
min-cut; Lamport/FLP message-complexity of consensus; Zurek Quantum Darwinism
(redundant objective records). The thermodynamic reading is **conditional** on
(L2) local thermalisation — it is a stated modeling assumption, not a proven
theorem. This is not a derivation of an arrow of time (that is H7, deliberately
untouched) and not a general theorem (finite witnesses + a cut-argument sketch).
The repo-specific content is the identification of the assumption that closes
T396's export escape, and the topological reversal-cost term it exposes.

## Contribution Needed

- **Hostile review** (queued): steelman "the reversal term is ordinary forward
  communication overhead, not a reversal cost." The intended defense is that it
  is an export-proof lower bound on *definalization*, but this needs an
  adversarial pass before any A1/D1 ledger movement.
- An **achievability** companion: is `forced_erasure + λ(G)` tight, i.e., a
  protocol that meets it? Current result is a lower-bound / cut computation only.
- A **substrate** for (L2): a physical model where local thermalisation of
  reconciliation garbage is forced (not stipulated), which would lift the
  thermodynamic reading from conditional to earned — and would feed Direction B's
  Tier-2 card.

## Reproduction

```bash
python -m unittest tests.test_consensus_definalization_bound -v
python -m models.consensus_definalization_bound --write-results
```

Artifact: `results/T442-consensus-definalization-bound-v0.1.json`
