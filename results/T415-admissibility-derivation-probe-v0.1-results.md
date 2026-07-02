# T415 — Admissibility-Derivation Probe — Results v0.1

- **Artifact:** `T415-admissibility-derivation-probe-v0.1`
- **Spec:** [tests/T415-admissibility-derivation-probe.md](../tests/T415-admissibility-derivation-probe.md)
- **Model:** [models/admissibility_derivation_probe.py](../models/admissibility_derivation_probe.py)
- **Test:** [tests/test_admissibility_derivation_probe.py](../tests/test_admissibility_derivation_probe.py)
- **Tags:** exploratory_bridge_probe, admissibility_derivation, governance_shapley_finality,
  bridge_obligation_2, P1_circular, P2_operational_automorphism, R2_conditional,
  no_claim_promotion

**Exploratory swing on bridge obligation #2** of the governance–Shapley–finality
homology, building on the registered **T412** separator gate and **T414**
certificate bridge. NOT a discriminator or physics result. Cross-domain material
is the **object of study**, never evidence. Provisional T-number (TESTS.md
untouched). No CLAIM-LEDGER entry. Ledger actions pause for Joe.

## Verdict (house vocabulary)

**Bridge obligation #2 is STRUCTURALLY bridged but NOT discharged to physicality.
The naive "the admissibility rule derives for free" hope is REFUTED as circular;
the principled port survives but bottoms out at R2.** `7 passed`. This is the
honest opposite of the clean result I set out to find — recorded as the method
working.

The game's derived admissibility rule (T414: the symmetry / Arrow-IIA axiom) has
**two** candidate ports to the quantum separator, and enumerating the full group
of reversible refactorizations `GL(3,2)` (168 elements) distinguishes them:

- **(P1) Equality-preservation** — *refuted as circular.* Because a relabel is
  unitary, the full-joint trace distance is invariant (= 1.0) under **every** one
  of the 168 refactorizations; "equality-preserving" therefore means only "keeps
  proper-subset TD = 0" = "keeps the separator a separator" — tautological. Worse,
  it is **strictly broader** than product-preservation: **18 entangling
  refactorizations preserve the equality** (the 24 global-parity-preserving maps
  minus the 6 qubit permutations). So (P1) admits operations a locally-restricted
  agent may not possess and cannot independently justify the admissibility rule.
- **(P2) Operational automorphism group** — *the correct port.* Admissible = the
  automorphisms of the operational structure (product / coupling-graph
  preserving = exactly T412's class), the true analog of the game's symmetry
  axiom (automorphisms of the game = player permutations). The separator survives
  it (T412). It is an **operational commitment** (which couplings the agent has),
  **not a free declaration** — but its **physicality is R2**: is the coupling
  graph / factorization physically forced, or stipulated?

## Leg-by-leg

**Leg 1 — baseline reproduces T412.** Parity pair: max proper-subset TD = 0.0,
full-joint TD = 1.0.

**Leg 2 — `equality_preserving ⇔ global_parity_preserving`.** The two
independently defined predicates induce the **same** partition over all 168
maps. Closed-form reason: a linear `A` sends the parity constraint to `⟨c, y⟩`
with `c = A⁻ᵀ1`; a proper subset distinguishes the images iff it contains
`support(c)`, which is impossible for a proper subset **iff** `c = 1` (weight 3)
**iff** `1ᵀA = 1ᵀ`.

**Leg 3 — counts.** `|GL(3,2)| = 168`; `equality_preserving = 24` (the stabilizer
of the parity functional, `168/7`); `product_preserving permutations = 6`.

**Leg 4 — the teeth: equality-preservation is strictly broader than product-
preservation.** `entangling_equality_preserving = 24 − 6 = 18 > 0`. Worked
example `A = CNOT(2→0)·CNOT(2→1)` (`y0=x0⊕x2, y1=x1⊕x2, y2=x2`): non-permutation
(entangling), global-parity-preserving, and **equality-preserving** (max
proper-subset TD = 0.0). The fan-in `y0=x0⊕x1⊕x2` is global-parity-**breaking**
and localizes the datum (factor-0 TD = 1.0). This single fact is what refutes
(P1) = product-preservation.

**Leg 5 — (P1) circularity.** Full-joint TD invariant (= 1.0) under all 168
relabels ⇒ equality-preservation is tautological.

**Leg 6 — (P2) is the port.** The principled admissible class is the operational
automorphism group (= T412's product/coupling-preserving class); the separator
survives it; it is an operational commitment, not a free declaration; physicality
reduces to R2.

## What this earns / does not earn

**Earns (exploration; method, not evidence):** a rigorous, group-complete
distinction between two ports of the game's admissibility rule, exposing the
circularity trap (P1) that a hand-picked example would have hidden, and
confirming the principled port (P2) — the operational automorphism group — is the
exact structural analog of the game's symmetry axiom. Bridge obligation #2's
invariance field is therefore **structurally bridged**: the game's symmetry
axiom and the quantum admissibility rule are the *same kind of object* (the
automorphism group of the operational structure). The homology's invariance field
(the one divergence in T414) is now **understood**, not merely open.

**Does not earn:** discharge of the physical question. (P2) is R2-conditional —
whether the operational automorphism group is *forced* (physical) or *declared*
depends on whether the coupling graph is physically forced, which is exactly R2 /
the transport rung / "why are agents bounded." The swing **relocates and pins**
the residual question; it does not close it. No physics/governance claim; no
cross-repo import; no promotion. **Single-process ceiling** in full force. Hostile
review not performed.

## Net for the homology

The governance–Shapley–finality homology now stands as: the finality wound (M1),
the R1/R2 split, and the escape-hatch structure port across model classes (T413);
the certificate signature matches on 5/6 fields (T414); and the one divergent
field — relabel-invariance — is now **structurally bridged** (both sides = the
operational automorphism group) with its physicality **pinned to R2** (T412/T415).
Every thread converges on the same single remaining question: **is the operational
structure (coupling graph / factorization / the value of the whole) physically
forced or declared?** — the program's central, still-open gap.

## Reproduction

```bash
python -m pytest tests/test_admissibility_derivation_probe.py -v   # 7 passed
python -m models.admissibility_derivation_probe
```

Deterministic; enumerates `GL(3,2)` exactly; reuses `models/separator_
refactorization_gate.py` (T412). No claim promotion; TESTS.md / CLAIM-LEDGER.md
untouched; pauses for Joe.
