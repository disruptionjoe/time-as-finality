# T392 Direction-B Orchestration Report — 2026-07-01

Scope: record of a single orchestrated run attacking Direction B of `audits/2026-07-01-high-gravity-research-directions.md` (physical criterion for measurement irreversibility). One new artifact quartet was produced, adversarially reviewed, patched, and registered. No claim promotion occurred; Q1C remains `dormant`.

Method: four phases — recon of earned state, design, implementation by a build agent, independent hostile review by a second agent with from-scratch numerical reproduction — followed by five review-mandated patches and re-verification.

---

## What was attacked

The recon established that the Q1A collapse sequence (T104 → T105 → T109 → T118 → T162) closed every escape hatch *within the fixed accessible-fragment-data family*, and that Q1C's executable gates (T146/T149/T150/T155/T158) leave exactly two live proposal classes. The swing targeted the boundary T162 did not close: reversal cost at a **fixed SBS closure key** under an **honest access boundary** — the T146 live class `extra_environment_candidate`.

## The artifact

T392 — Fixed-SBS-Key Reversal Divergence Witness:

- `tests/T392-fixed-sbs-key-reversal-divergence-witness.md`
- `models/fixed_sbs_key_reversal_divergence.py`
- `tests/test_fixed_sbs_key_reversal_divergence.py` (18 tests)
- `results/T392-fixed-sbs-key-reversal-divergence-v0.1-results.md` + `.json`

Finite exact-statevector model: system S, weak meter M (ordinary record = full event-level (S, M) joint), four declared fragments F1..F4 (perfect Z-copies), and in the deep-branching preparation one unmonitored ancilla A0 copying F4, outside the declared family and the undo set.

## Verdict: witness holds in this finite family

- Ordinary-record equality across preparations: exact (max diff 0.0).
- SBS closure key over F1..F4 (computed with the repo's own T162 machinery): identical; both preparations D1-finalized at R_delta = 4.
- Reversal divergence under the predeclared undo protocol: visibility 0.989743 (= 4√3/7) vs 0.0 exactly; typed axis H = 4 vs ∞.
- Auxiliary channel on A0: decision-risk lift 0.25 across a three-member loss family; I(V; A0 | R) = 0.5 bits; T137 downstream-transform null control shows exactly zero lift and zero CMI.
- φ-independence lemma (added at review): the accessible conditional state in the deep preparation is exactly independent of S's initial phase, so H(B) = ∞ is protocol-independent, not an artifact of restricting to inverse-coupling undo.

Earned content, stated in the repo's own factorization language: the D1-relative-to-access verdict does not factor through (full ordinary record, T162 SBS key) in this family. Reversal cost is the residue axis, exactly where T22 left it formal-only and T5 showed it is not thermodynamic work.

## Hostile review

Independent agent, all headline numbers reproduced from scratch (`_local/t392_hostile_check.py`). Six attacks: prep-mixture crux, T137 downstream, SBS-key fidelity, physics re-derivation, T150 gerrymander via H = ∞, verdict-language audit. Ruling: **stands, with five required patches** — all applied and re-verified (mixture-legitimacy section; (S, M) labeling bug fix; class-name collision fix to `extra_environment_candidate` / `typed_extra_environment_candidate`; φ-independence lemma earned as an 18th test; TESTS.md registration with T391 noted unassigned). Strongest surviving objection, priced in the spec: the access boundary is stipulated — A0 engineered, not physically forced. That bounds the claim to an existence result; it does not kill it.

## What this does not earn

- No Q1C status change. Reinstatement requires the T166 platform packet stack and pauses for Joe per AGENTS.md.
- No hardware platform. The witness converts the live class from a logical possibility into a constructive design target: deep vs shallow branching at fixed visible redundancy, with a detect-but-not-recapture auxiliary channel.
- No claim promotion; CLAIM-LEDGER untouched.

## Next moves (in priority order)

1. **Forcing argument** (the reviewer's residual objection): is there a physical setting where the A0 asymmetry — outside the declared family, outside the undo set, yet readable — is forced rather than engineered? Candidates: photon loss to an outgoing mode, phonon emission into a monitored bath. This is Direction B's real open problem now.
2. **Platform packet sketch** against T166 intake for one concrete architecture — decision pauses for Joe.
3. Consider whether T392's non-factorization result changes the strongest-form wording of Q1A's `bookkeeping_only` status (scoped to fixed-data family) — wording review only, pauses for Joe.

Note: pre-existing uncommitted edits to `steward/README.md` and `steward/memory-log.md` were present before this run and were not touched.
