# Roadmap

## Phase 1: Make The Claims Precise

- **Completed v0.1:** define [D1](claims/D1-physical-finality-definition.md)
  as a componentwise finality preorder.
- **Completed v0.1:** define the
  [D2](claims/D2-observer-as-record-bearing-system.md) observer capability
  taxonomy.
- Expand [N1](literature/N1-known-neighbors.md) with citations and prior-art positioning.

## Phase 2: Build Toy Models

- **Completed v0.1:** implement
  [T1](tests/T1-record-graph-temporal-reconstruction.md) as a finite causal
  record graph, including a minimal total-order counterexample.
- **Completed v0.1:** build the
  [Emergence Laboratory](tests/T9-emergence-laboratory.md) across all 256
  elementary rules and reversible second-order lifts.
- **Completed v0.1:** build
  [T10](tests/T10-proof-carrying-metastable-finality.md) to compare
  coarse-graining, ideal proof verification, Snowball confidence, Bayesian
  aggregation, and local metastability.
- Test spacelike-separated event ordering under [T3](tests/T3-spacelike-events-no-global-commit-order.md).
- Build a minimal quantum measurement record scenario for [T2](tests/T2-quantum-measurement-record-finality.md).

## Phase 3: Stress The Framework

- Try to break H1 by showing temporal order cannot be reconstructed without primitive time.
- Try to break Q1 by showing "under-finalization" adds no clarity beyond standard decoherence language.
- Try to break R1 by showing the distributed-systems analogy misleads about relativity.
- Try to break B1 by showing horizon language overstates causal record claims.

## Phase 4: Public Essay And Technical Note Split

- Keep [ESSAY.md](ESSAY.md) readable and claim-linked.
- **Completed v0.1:** publish the internal
  [technical note](TECHNICAL-NOTE-v0.1.md) after the first stable toy-model
  definition.
- Keep speculative extensions clearly separate from core claims.

## Best First Contributions

1. Build a persistent dynamical reconciler whose storage and access boundary
   arise inside the local-update model rather than being selected as a
   terminal observer window.
2. Replace T10's ideal proof functionality with one concrete proof relation,
   explicit proof costs, epoching, and stale-certificate revocation.
3. Implement [T2](tests/T2-quantum-measurement-record-finality.md) on a
   system-apparatus-environment model and compare D1 directly with
   quantum-Darwinism redundancy.
4. Test whether the D1 preorder composes under record-graph merge.
5. Replace the Landauer lower-bound calculation with an explicit stochastic
   bit-erasure protocol and simulated work distribution.
6. Run a relativity sanity check for
   [R1](claims/R1-relativity-no-global-commit-order.md).
7. Add a black-hole specialist critique of
   [B1](claims/B1-black-holes-finality-boundaries.md).
