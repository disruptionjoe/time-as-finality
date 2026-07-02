# Finite-Closed Capability-Boundary Scope Theorem (candidate)

## Status

Theorem-candidate / open problem. **No claim promotion; no CLAIM-LEDGER entry;
no TESTS.md edit; promotion pauses for Joe.** This document formalizes **M1** —
the strongest convergence of the 2026-07-02 physical-boundary persona pass
(`explorations/physical-boundary-hegelian-persona-pass-2026-07-02.md`) — and
marshals three independent executable witnesses (T411, T413, T417) plus a general
argument. Part 1 (the Declarability Lemma) is proven at the finite-witness /
elementary-argument level; Part 2 (Physicality-Requires-a-Gap) is a
theorem-**candidate** with a stated exhaustiveness gap. **Single-process ceiling
in full force:** the three witnesses were produced by one process; their
agreement motivates the theorem and supplies instances, but the *argument*, not
the convergence, is what carries it. Cross-domain witnesses (cooperative game
theory, cryptography) are the **object of study**, never evidence for physics.

## Informal statement

> In any **finite closed** model, a capability boundary between two
> R-statistically-identical configurations is **informationally declared** — the
> separating datum is always co-present in the complement of R. Making the
> boundary **physically forced** (not a removable access-restriction) requires
> leaving the finite-closed **single-instance** regime, via exactly one of an
> **asymptotic/limit gap** or a **forcing assumption**. No finite closed model
> exhibits an unconditionally physical single-instance capability boundary.

This is the scope no-go the program has been circling: it explains *why* every
physical-boundary attempt was absorbed, and it says precisely what a genuine
physical boundary would have to buy from outside the finite-closed-single-instance
regime.

## Definitions

- **Finite closed model.** A finite configuration space with deterministic
  endomorphism or finite-dimensional unitary dynamics; *closed* = no external
  reservoir, the full configuration is retained. Two configurations `c_A, c_B`.
- **Region `R` with menu `M_R`.** A sub-structure (subsystem / subset of tensor
  factors / subset of feasibly-queryable data) together with the operations and
  queries supported within it (observational and interventional-within-`R`).
- **`R`-statistical equivalence.** `c_A` and `c_B` yield identical outcomes under
  every `M_R`-supported query.
- **Capability boundary.** A boundary-crossing menu `M⁺ ⊋ M_R` and an `M⁺`-query
  that separates `c_A` from `c_B` (they differ in an enactable / recoverable
  transformation).
- **Declared vs physical.** The boundary is **declared** if the separating datum
  is a function of co-present complement data that `M_R` is merely *not permitted*
  to query (a restriction removable by enlarging access within the model's own
  resources). It is **physical / forced** if no enlargement of `R`-supported
  operations *within the model's own resources* recovers the datum — the inability
  is a consequence of the dynamics/structure, not a stipulated access-restriction.

## Part 1 — Informational Declarability Lemma (proven)

**Lemma.** In a finite closed model, if `c_A` and `c_B` are `R`-statistically
equivalent but some capability boundary separates them, then the separating datum
is a function of the complement of `R` in the full (co-present) configuration.

**Proof.** The full configuration determines the outcome of every query
(closedness + finiteness). `R`-statistical equivalence says the separating datum
is *not* a function of `R`-supported data alone. Since the model is closed, the
full configuration is `R`-data together with its co-present complement; a function
of the whole that is not a function of the `R`-part is a nonconstant function of
the complement. Hence the datum is a function of the co-present complement. ∎

**Corollary (informational boundary is declared).** The information required to
cross is *always co-present*; the informational boundary is therefore a declared
access-restriction, not a physical absence. This is exactly the **joint-record
completion** kill (the T401 move) in general form — and it is why "exclude the
retained registers from `R`" was pure declaration in every thermal attempt.

## Part 2 — Physicality-Requires-a-Gap (candidate)

By the Lemma the datum is co-present, so a physical boundary cannot be an
*informational* absence; it can only be an **extraction-resource** barrier. Let
`cost_R(c_A, c_B)` be the resources (energy, computation, or model-size) an
`M_R`-agent must spend to extract the co-present separating datum.

**Candidate theorem.** For the boundary to be physical (forced), `cost_R` must be
prohibitive. In a finite closed model **at a single instance**, `cost_R` is
finite, so extraction is achievable by finite brute force — the single-instance
boundary is **declared/crackable**. Hence a physical boundary requires leaving the
finite-closed **single-instance** regime, via exactly one of:

- **(E1) Asymptotic / limit gap.** A *family* of models in which the extraction
  cost, or the datum's non-locality, diverges in a limit — so the boundary is a
  limit-invariant, not a single-instance fact. (RG relevant-operator survival;
  the Aumann–Shapley non-atomic value; a diverging recovery cost.)
- **(E2) Forcing assumption.** A hardness or impossibility hypothesis under which
  no *feasible* `M_R`-procedure extracts the datum across the family. (A
  complexity conjecture; a no-go theorem.)

and **never** via:

- **(E0) Stipulated gap.** A declared partial trace or a fiat menu-restriction —
  which is not a resource barrier at all and collapses to *declared* (dies to
  joint-record completion / the reservoir-idealization absorber).

**Stated gap.** "Exactly one of (E1)/(E2)" is an **exhaustiveness claim** over
the ways a co-present datum's extraction cost can be made prohibitive; it is
argued and thrice-witnessed below but **not** proven in full generality. Closing
it (or exhibiting a fourth mode) is the promotion obligation.

## The three witnesses

Each is an executable finite fixture in a *different model class*; each exhibits
the Lemma and lands on a different escape mode.

| Witness | Model class | Datum's co-present locus (Lemma) | Gap mode | Verdict |
| --- | --- | --- | --- | --- |
| **T411** departed-record discriminator | thermal quantum Darwinism | retained tier-1 registers (a single retained-Z measurement separates) | **(E0)** stipulated partial trace | **absorbed** — died to joint-record completion / reservoir idealization, exactly as Part 1 predicts |
| **T413** legitimacy-as-Shapley probe | finite cooperative game | the grand-coalition value `v(N)` (or boundary coalitions) | **(E0/E1)** single grand-coalition query is finite → declared; the Aumann–Shapley non-atomic limit is genuine **(E1)** | R1 object built; R2 declared; physical only in the non-atomic limit |
| **T417** computational finality boundary | number theory (Goldwasser–Micali) | `(x, N)` — brute-force factoring recovers it | **(E2)** QRA/factoring hardness, **+ (E1)** asymptotic cost growth | first door the reservoir killer cannot touch; physical **conditional** on QRA and **family-level** only |

Reading the table: the recurring **reservoir-idealization** death is specific to
witnesses that used **(E0)** (a stipulated gap). Strip the stipulation and the
death vanishes (T417) — but then the boundary is physical only via **(E1)/(E2)**,
i.e. as a *family/limit + assumption*, never as a single-instance closed-model
fact. That is the theorem.

## Corollaries

- **R1/R2, reinterpreted.** The persona pass's repair split is a corollary. **R1**
  (a relabel-proof separator supported on no proper subset) is a witness that the
  Lemma's complement is the *whole* — achievable *inside* finite closed models
  (T413's `v(N)`; T411/T412's β=0 correlation). **R2** (physical forcing) is
  precisely **(E1)/(E2)** — provably *not* a single-instance closed-model fact.
  The program's difficulty was demanding R2 of a single finite closed fixture,
  which the theorem says is impossible.
- **Why every attempt was absorbed.** T398–T406 and the T410/T411 swing each
  supplied a boundary whose datum was co-present (Part 1) and whose gap was **(E0)**
  stipulated — so joint-record completion ate them by construction.
- **The two honest escapes are named and instantiated.** (E1) is Door B
  (asymptotic; Aumann–Shapley); (E2) is Door C (assumption; QRA) — and T417 shows
  they unify (computation as the scaling resource).
- **T416 consistency.** The coupling-graph forcing gate's result — the separator
  cannot self-certify its factorization; independent operation/coupling evidence
  is required — is the operational face of Part 1: the boundary's forcing must come
  from *outside* the separator (an (E1)/(E2) resource structure), never from the
  co-present datum itself.

## What would promote this to a theorem

1. **Close the exhaustiveness gap** in Part 2: a precise definition of
   "extraction resource" and a proof that prohibitive cost in a closed model
   entails (E1) or (E2) — or a fourth mode, which would itself be a result.
2. **A rigorous model-class statement** for the Lemma beyond the elementary
   argument (name the category of finite closed models; state closedness as an
   axiom; prove declarability as a structural fact).
3. **A fourth independent witness** in a genuinely different class (e.g. a
   topological/cohomological one, per the sheaf-cluster reading) would raise
   confidence past the single-process ceiling only if produced by an independent
   process.
4. **Externalization:** the single-process ceiling caps this at *internally
   established* at best; a named-specialist read or an independent reproduction is
   required for any external "theorem" standing.

## Relation to the lead line and guards

This reframes the primary open problem
(`open-problems/region-indexed-capability-discriminator.md`): the physical-
boundary discriminator, *as a single-instance finite-closed object*, is **not
merely unbuilt but provably out of scope** (candidate); its honest successors are
the R1 separator (built, relabel-proof modulo the operational-automorphism
admissibility of T415/T416) and the (E1)/(E2) family/assumption boundaries. No
North Star, canon, public-posture, cross-repo, or ledger movement. GU/TI material
remains stress-test input only. Every promotion decision pauses for Joe.

*Prepared 2026-07-02. Candidate formalization; Part 1 proven (elementary), Part 2
argued + thrice-witnessed with a stated exhaustiveness gap. No repo state modified
beyond this file.*
