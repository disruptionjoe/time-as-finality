# T413 — Legitimacy-as-Shapley Finality Probe — Results v0.1

- **Artifact:** `T413-legitimacy-shapley-finality-probe-v0.1`
- **Spec:** [tests/T413-legitimacy-shapley-finality-probe.md](../tests/T413-legitimacy-shapley-finality-probe.md)
- **Model:** [models/legitimacy_shapley_finality_probe.py](../models/legitimacy_shapley_finality_probe.py)
- **Test:** [tests/test_legitimacy_shapley_finality_probe.py](../tests/test_legitimacy_shapley_finality_probe.py)
- **Tags:** exploratory_homology_probe, governance_shapley_finality,
  region_indexed_capability, joint_record_completion_split,
  r1_constructed_classically, r2_declared, no_claim_promotion

**Exploratory big-swing probe of a candidate homology — NOT a discriminator
result.** Cross-domain material (cooperative game theory / governance) is the
**object of study**, never evidence for physics or any sibling repo. Registered
as T413 after normalizing the committed provisional numbering. No CLAIM-LEDGER entry. Ledger
actions pause for Joe. Predeclaration: spec frozen before the model existed;
every closed-form value below was hand-derived at spec-freeze.

## Verdict (house vocabulary)

**The governance-layering ↔ finality homology reproduces the finality wound
exactly, in a fully classical model class — and the Shapley/efficiency axiom
CONSTRUCTS a classical R1 object the quantum fixture (T411) could not.** All
eight predeclared legs hold; `10 passed in 0.15s`. Concretely:

- A cooperative game where an in-region player's **Shapley value** is its
  legitimate boundary-crossing capability reproduces the **T401 joint-record
  completion kill** (Pair 1) via a single **proper-subset** coalition query
  `{0,3}` — the exact structural analog of T411's single retained-Z measurement.
- The **efficiency axiom** builds Pair 2, where two games agree on **every**
  proper coalition yet differ in Shapley value; the datum lives only in the
  grand coalition `v(N)` = **the whole**, in no proper subset. Proper-subset
  joint-record completion **cannot absorb it** — this **satisfies R1**
  (relabel-proof separator) *classically and cleanly*, which is more than T411
  achieved.
- **But R2 (physical forcing) is not earned:** `v(N)` is a **declared** number.
  The honesty leg fires `boundary_physicality_reduces_to_declaration`, exactly as
  in T411. Physicality is handed to the non-atomic / infinite-layer
  (Aumann–Shapley) limit — the M1 "asymptotic gap" escape.

This is the persona pass's **R1/R2 split, re-derived in game theory**: R1 is the
*efficiency/symmetry* content (the legitimate share reflects the whole and is
automorphism-forced); R2 is the *non-atomic limit* content (uniqueness becomes
unconditional). **No claim promotion.**

## Leg-by-leg

**Leg 1 — Shapley cross-check + efficiency.** Dividend formula and the
120-permutation marginal average agree exactly. `φ_A=(2,2,2,0,0)`,
`φ_B=(3,2,2,1,0)`, `φ_C=(3,3,3,1,1)`; `v(N) = 6 / 8 / 11`; `Σφ_i = v(N)` exact
for all three (efficiency).

**Leg 2 — within-R equality (both pairs).** `v_A = v_B = v_C` on every coalition
`T ⊆ {0,1,2}`. The region cannot see the difference.

**Leg 3 — Shapley separation.** `φ_0` shifts by exactly `Δ = 1` in each pair
(`2/|{0,3}|` for Pair 1; `5/5` for Pair 2). The separating menu is
"compute your legitimate Shapley claim" — a boundary-crossing functional.

**Leg 4 — joint-record completion (the SPLIT).**
| Pair | min separating coalition | in proper subset? | verdict |
| --- | --- | --- | --- |
| **1** (boundary dividend `{0,3}`) | `{0,3}`, size 2 | **yes** | **ABSORBED** |
| **2** (efficiency-only, grand dividend) | `{0,1,2,3,4}`, size 5 = whole | **no** | **SURVIVES-R1** |
Exhaustive certificate: all `2^5−1` proper subsets give identical restricted
games for Pair 2; only the grand coalition differs.

**Leg 5 — relabel / declared re-weighting vs axioms.** A "boundary-blind"
random-order value (drop orderings where a boundary player precedes `0`) moves
`φ_0` from `3` to `3/5` — i.e. it *localizes / declares the boundary away* — but
it is **illegitimate: it breaks the symmetry axiom** (interchangeable players in
`u_N` receive unequal shares; `boundary_blind_symmetric = False`), while Shapley
is symmetric and efficient. **Symmetry = automorphism-invariance = the persona
pass's exact criterion for "physical, not declared."** The localizing relabel is
forbidden by the constitution (the axioms). Pair 2's global datum is
**relabel-proof relative to the axioms.**

**Leg 6 — R2 honesty.** Pair 2's datum is `v(N)`, a declared number
(`6 → 11`). R1 is satisfied; R2 is not. `boundary_physicality_reduces_to_
declaration = True` — the classical game reproduces the wound; it does not heal
it. Physicality requires the infinite-layer limit.

**Leg 7 — Nash multiplicity vs Shapley uniqueness (the Joe bridge).** The
imputation set of `v_C` is a **positive-dimensional polytope** (dimension
`|N|−1 = 4`, slack `11`): many declared, legitimate-*looking* allocations at
finite scale. The four axioms single out **one** point (Shapley). The
Aumann–Shapley-flavored trend: the grand-coalition datum's grip on a single
share falls with `N` — `φ_0/v(N) = 1/3 → 13/44 → 3/11` for `N = 3,4,5` — the
finite gesture toward non-atomic dilution (out of house style, flagged). *Nash
at finite scale = declared multiplicity; Shapley at the infinite layers =
axiom-forced legitimate uniqueness.*

**Leg 8 — quantum-residue negative (the sharp boundary on the homology).**
Executable: two games equal on **every** coalition have identical Shapley values,
and every `φ` difference has a coalition-value witness — because Shapley is
**linear in `v`**. So a **no-marginal separator** (information in *no* coalition,
the genuine T411 β=0 residue) **cannot exist in a finite classical game.** Pair
2's R1 object is the *weaker* whole-coalition kind (datum in `v(N)`), not the
no-marginal kind. **The T411 surviving object is intrinsically quantum and does
not port.**

## What this earns / does not earn

**Earns (as exploration, method not evidence):** a faithful, executable
re-derivation of the finality wound (M1) and the R1/R2 repair in a classical,
established-mathematics model class (Shapley / cooperative games), independent of
the quantum machinery; a *clean classical construction of an R1 object* via the
efficiency axiom; and a precise identification of the two escape hatches with two
named game-theoretic structures (symmetry axiom ↔ automorphism-forcing;
Aumann–Shapley non-atomic limit ↔ asymptotic gap). Strengthens the reading that
M1 is a **structural theorem**, not a physics artifact, because it recurs in a
completely different model class.

**Does not earn:** any physical-boundary claim (R2 declared, Leg 6); any
governance claim (governance is the object, not a result); any cross-repo import;
any promotion. The **single-process ceiling** applies with full force: this model
was built by the same process that produced the pass and holds Joe's hint — its
agreement with the pass is a *target*, never corroboration. The infinite-limit
leg is a finite gesture, not a non-atomic proof. Hostile review not performed.

## Reproduction

```bash
python -m pytest tests/test_legitimacy_shapley_finality_probe.py -v   # 10 passed
python -m models.legitimacy_shapley_finality_probe
```

Deterministic, exact rational arithmetic; `N=5` (120 orderings) enumerated in
full. No claim promotion; TESTS.md / CLAIM-LEDGER.md untouched; pauses for Joe.
