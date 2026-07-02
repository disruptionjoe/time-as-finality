# Direction A Swing Report — 2026-07-01

Scope: record of the first big swing at Direction A of `audits/2026-07-01-high-gravity-research-directions.md` (temporal-order inequality), plus lane-status notes for the whole program. Two artifacts built in parallel lanes, jointly hostile-reviewed, patched, re-verified. No claim promotion; no CLAIM-LEDGER edits.

Method: recon (T48/T49/T50/T54-family, Bell mappings T21/T131, guardrails R1/Q1D; confirmed zero prior process-matrix content in repo) → parallel builds → combined hostile review with independent from-scratch reproduction → patch cycle.

---

## T394 — Axis-Count Reconstruction Hierarchy (rung 1). Ruling: stands.

The Anti-Scalar Theorem (T49) is now the d = 1 case of a hierarchy: reconstruction of the record-dependency order by d monotone finality axes under componentwise comparison is exactly order dimension ≤ d. Verified exhaustively for all 405 poset classes up to n = 6, with the tie-collapse loophole (real axes permit ties; dimension is defined via linear extensions) closed by a proof-backed lemma the reviewer independently confirmed correct in general. The strict hierarchy is witnessed: dim(S_3) = 3, dim(S_4) = 4 (both brute-forced, independently reproduced unpruned), dim(S_5) = 5 by machine-checked certificate whose pigeonhole the reviewer verified proves dim(S_d) ≥ d for all d at the real-axis level. Realizability: every finite poset arises from T48's own containment rule with principal-downset record bases (405/405; the strict-downset variant fails outside antichains — documented edge case).

Consequence, stated conditionally: D1's four axes reconstruct exactly the event structures of order dimension ≤ 4; a concrete 10-event structure escapes any 4-axis reconstruction. Whether physical causal orders exceed dimension 4 is open, flagged as candidate prior-art territory.

Weight, priced in-spec: Theorems 1–3 are presumed re-derivations of classical dimension theory (Dushnik–Miller, from-memory, unverified). The repo-new content is the AM/axis-count ↔ dimension identification, the executable bridge to T48/PO1 objects, and the tie-collapse closure. 29 tests green.

## T395 — Record-Order Trade-off Probe (the hinge). Ruling: stands re-scoped.

The v0.1 hinge probe: quantum switch + accessible record qubit on the control, exact (D, V) trade-off, with a reduction audit against interferometric duality. Outcome, in the re-scoped honest form: **the collapse was definitionally forced, not contingent** — the switch+record state is term-by-term a Mach-Zehnder with which-path markers (diff 1.1e-16), D and V are Englert's quantities by definition, and every exact relation (D² + (V/V₀)² = 1, Englert saturation, three-way decomposition) is an algebraic identity of the branch form. The kill-test could not have returned a residue in the two-order family. Earned content: the explicit term-by-term pricing, and two located residues.

Residue 1 — k ≥ 3 partial-record structure: with a class-coarse (partial-access) record over 3 or 6 orders, binary duality holds exactly pairwise cross-class, is exactly absent within class, order postdiction is capped at (1/k)(1 + sin(γ/2)) (Helstrom-verified), and none of three tested global scalarizations keeps the binary form. Verified over all 60 + 31 configurations — though these too are identities of the branch form (disclosed post-review); the point is structural: the binary duality shape does not transplant to partial records over k ≥ 3 orders. This is where the T49 incomparability structure enters and where any Direction-A inequality must live, if one exists.

Residue 2 — the accessibility boundary: whether the record is read or ignored moves no process marginal (exactly 0). Any record-fixed vs causally-separable criterion is therefore capability-relative, not statistics-relative — a structural constraint on what Direction A's "device-independent criterion" can even mean, and a convergence with the capability-projection framing and the T392/T393 access-boundary results.

Named unbuilt rungs: a genuine causal witness (SDP random-robustness) instead of visibility; a multi-holder D that operationalizes record *finality* rather than record *existence*; the multipath-duality absorber audit (the known-physics candidate that could swallow the k ≥ 3 residue). 35 tests green.

## Direction A status after the swing

The hinge did not open at k = 2, and the v0.1 operationalization was shown to be incapable of opening it — that is the router result. The surviving hypothesis is sharper and harder: a record-order inequality, if it exists, lives at k ≥ 3 with partial-access records (incomparability structure) and must be phrased in capability terms, not marginal statistics. Rung 1 (T394) is solid ground; rung 2 now has a precise negative boundary instead of an open creative space. Direction A remains the lead lane; its next artifact must bring either the SDP causal witness or the multi-holder finality D — both named, both buildable.

## Lane status (per operating instruction: a lane pauses only if truly unbuildable)

- **Direction A (lead, big-swing lane):** ACTIVE. Next buildable: SDP causal-witness rung; multi-holder finality-D; multipath-duality absorber audit; k ≥ 3 incomparability instance using T394's dim-3 structures.
- **Direction B:** ACTIVE (not paused). Checkpoint passed (T392/T393). Human-expert read is queued but is NOT a blocker: buildable now — Tier-2 thermodynamic card (shared with C), partial-amplitude analytic boundary α*(v*), T166 packet sketch (drafting is buildable; sending pauses for Joe).
- **Direction C (background lane):** ACTIVE. Buildable now: positive complement of T110 (dissipation bound on k-observer record consensus), which is simultaneously B's Tier-2 re-entry and would ground T395's capability-relative boundary thermodynamically.
- **Hourly progressions:** literature diligence queue — Dushnik–Miller and dimension theory (T394), switch-control-decoherence and multipath duality (T395), quantum Darwinism vs irreversibility (T392/T393), Minkowski causal-order dimension (T394 consequence). Note: the hourly automation committed mid-session (home-path scrub + collision receipt, status blocked) and correctly backed off the active lane.
- **Nothing is human-blocked.** The human-expert read (T393 first) runs on Joe's clock in parallel; no lane waits on it.

## Housekeeping

Steward files (mount-truncation damage, pre-dating this swing) restored to committed state, then re-synced after the hourly scrub commit. Stale `.git/index.lock` cleared by the hourly lane. Session probe file archived (not deleted, per operating instruction) at `_local/archive/2026-07-01-session-artifacts/`. TESTS.md stdlib claim amended (T392/T393/T395 use numpy). T396 exists committed without spec/registration — belongs to another lane, flagged, untouched.

Cumulative artifact state, 2026-07-01: T392 (18), T393 (29), T394 (29), T395 (35) — 111 tests green, four hostile reviews survived (two with required patches, all applied).
