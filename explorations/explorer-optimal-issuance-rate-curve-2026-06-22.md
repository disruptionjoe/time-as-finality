# Explorer: Optimal Issuance Rate Curve

**Date:** 2026-06-22  
**Origin:** Idea-capture synthesis note (build-agent placement pass)  
**Status:** Exploration — ideas preserved in full; some are candidates for claims, some for open-problems, some may be absorbed  
**Connects to:** temporal issuance source object (`open-problems/temporal-issuance-source-object-spec.md`), `Ext_S` (admissible extension formalism), metabolic scaling explorer (`explorer-metabolic-scaling-energy-time-transport-networks-2026-06-22.md`), CLAIM-LEDGER

---

## 0. What This Document Does

The central question: **is there an optimal issuance rate curve, and what is its form?**

The answer: not as a pre-existing named object, but the math family exists and is standard. Several fully-worked versions exist in tokenomics and monetary design. A curve is derivable once an objective is named. This exploration preserves the full idea inventory, maps pieces to the TaF formal program, and flags absorption risks.

---

## 1. The Core Formal Object

### State-dependent optimum

The real target is a *curve* `λ*(s)`, not a single number. Issuance rate `λ` controls the rate at which new source-side possibilities (`Ext_S` — admissible extensions of source constraints) are introduced into the shared process. The optimal rate maximizes a net-benefit functional:

```
λ*(s) = argmax_λ [ N(λ, s) − C(λ, s) − K(λ, s) ]
```

Where:
- `λ` = issuance rate (rate of new admissible extensions)
- `N(λ, s)` = novelty / structure formation gained at rate `λ` given state `s`
- `C(λ, s)` = coherence / reconciliation cost (cost of integrating new extensions into consistent global sections)
- `K(λ, s)` = collapse / instability / contradiction risk (probability that extensions at rate `λ` produce irreconcilable branching)
- `s` = current state of the shared process

**Predicted qualitative shape:**
- **Low λ**: collapse / insufficient novelty; system falls into closed rearrangement of prior state
- **Moderate λ**: interior optimum; maximum adaptive structure formation
- **High λ**: incoherence; unreconciled branching; observer record overload

### Toy first model

```
dS/dt = a·λ − b·λ² − c·S        (S = coherent structure formed)
```

Instantaneous optimum (static case, K off):

```
λ* = a / (2b)
```

The constant `a/2b` is the static special case; the genuine curve `λ*(t)` or `λ*(s)` appears once K and state-dependence are activated. Useful as a calibration point: the interior optimum is finite and positive, which rules out "always maximize issuance" or "zero issuance is safest."

### Candidate hypothesis for registration

> **Optimal Issuance Rate Curve Hypothesis:** There exists a nonzero, finite issuance rate λ* that maximizes coherent structure formation by balancing novelty generation against reconciliation cost and collapse risk.

If this is registered as a claim, the corresponding kill conditions are in §5.

---

## 2. Mapping to the TaF Formal Program

### Relation to `Ext_S`

The temporal issuance source object spec (`open-problems/temporal-issuance-source-object-spec.md`) centers on `Ext_S` — admissible extension of source-side constraints — as the formal object. Issuance rate `λ` is the rate at which `Ext_S` is populated. The `λ*(s)` curve is therefore the dynamics equation for how `Ext_S` should grow optimally.

This is a dynamics constraint on the source-object, not a definition of it. It does not resolve what `R`, `<`, or `mu` are — it specifies how fast they should be introduced given the current state of the process.

### Relation to `mu` (source measure)

The `mu` field in the source object requires typed units, monotonicity, and transformation behavior. The `N − C − K` functional suggests a candidate `mu`:

```
mu(r) = N(r) − C(r)        (novelty minus coherence cost, integrated over realization r)
```

This is not the metabolically-scaled `mu_M` from the metabolic scaling explorer — it is a different candidate, optimality-derived rather than network-geometry-derived. Both candidates may be relevant; they address different aspects of the source measure (scaling behavior vs. optimality condition).

The absorption test: does `N − C` as a measure survive the same-neighbor-data freeze? Does it produce different numerical values than entropy production or Shannon information when all other source-object fields are held fixed?

### Relation to the `M` field (source-to-record generation map)

The `M` field maps source realizations to observer records. If `λ` controls the rate of new source events, then `M` generates new records at rate `λ`. The optimal `λ*(s)` curve is a constraint on `M`'s cadence — when it is and is not appropriate to generate new records given the current reconciliation load.

This is a plausible connection to the **observer-side record cadence** flagged in the idea-capture document as a possibility, not a recommendation.

---

## 3. Existing Math Families and Absorption Risk

### What already exists

The `λ*(s)` problem is structurally covered by:

- **Optimal control** (HJB / Pontryagin): given a state process with cost functional, find the optimal control trajectory. `λ*(s)` is a standard optimal control problem once `N`, `C`, `K` are typed.
- **Exploration-exploitation** (multi-armed bandit, Thompson sampling): the optimal exploration rate trades novelty against regret — direct structural analogue of `N` vs. `C`.
- **Logistic / bounded-resource growth**: the hump-shaped rate curve emerges naturally when drawing on a finite reservoir under a growing suppression term.
- **Maximum Entropy Production Principle** (contested): a non-equilibrium system settles at the rate that maximizes entropy production under its constraints — selects a rate rather than assuming one. Physics-native option.

### The absorption question

The live question for the TaF program is not whether the `λ*(s)` object exists — it does. The question is whether `N`, `C`, `K` can be given **substrate-native TaF definitions** that a generic optimal-control formulation does not already supply for free.

If they can: `λ*(s)` is a TaF-specific formal object with a non-arbitrary interior optimum derivable from TaF's own structural constraints. This is a new claim.

If they cannot: the `λ*(s)` formalism is *absorbed* by generic optimal control — which is itself a clean result (it means issuance dynamics are standard and the program's distinctiveness must come from elsewhere).

Absorption is not defeat. Knowing that `λ*(s)` is a standard optimal control problem with TaF-defined inputs is progress; it points to what TaF needs to specify.

### The recurrence observation

Declining / hump-shaped rate curves recur as optima whenever a finite reservoir is drawn down under a growing suppression term. This pattern appears in:
- Token issuance (empirical: issuance rates decline with token age across ~2,000 tokens)
- Cosmic star-formation history (Madau-Dickinson curve: structure-formation rate peaked at redshift z≈2 then declined as dark energy suppressed collapse)
- Biological growth under metabolic constraints
- Exploration-exploitation optimal rates

The recurrence is either the strongest supporting analogy for the Optimal Issuance Rate Curve Hypothesis — or the route by which it gets absorbed into generic dynamical systems theory. The distinction depends on whether TaF's `N`, `C`, `K` are substrate-native.

---

## 4. Tokenomics Evidence (Prior Art)

Fully-worked optimal issuance rate curves exist in tokenomics. Relevant results:

**Jermann & Xiang (2024/25) — "Tokenomics: Optimal Monetary and Fee Policies"**
- Issuer chooses issuance rate and fees to maximize value. Users derive utility from holding and transacting.
- Result: **gradually declining money-growth rates are optimal** — high short-run issuance to bootstrap, smooth taper to low long-run growth.
- Key property: **commitment** to a low future growth rate boosts the current price, enabling more total issuance without value collapse.
- Functional form: `g_t ≈ λ·g_long + (1−λ)·g_short` (geometric convergence).
- Hard-coded on-chain schedules act as credible commitment devices — blockchains excel at this vs. discretionary governance.

**Empirical pattern (~2,000 tokens):** issuance rates start higher and decline with token age, stabilizing near ~0.2%/month. This is the empirical signature of the theoretical optimum.

**TaF implication:** The commitment device insight is directly relevant. A TaF finality record that encodes a fixed issuance schedule is a source of finality precisely because the schedule cannot be revised after commitment. This is the same mechanism that makes Bitcoin's halving schedule credibility-enhancing: the fixed schedule is the commitment, not a constraint on it.

---

## 5. Kill Conditions (for the Claim Candidate)

The Optimal Issuance Rate Curve Hypothesis weakens or dies under:

1. **Monotone `N − C − K`**: If the net functional is monotone in `λ` over the admissible range (optimum at a boundary — always maximize or always minimize), no interior curve exists. This happens if the coherence cost grows faster than any novelty gain for all `λ > 0`.

2. **Non-substrate-native `K`**: If the collapse risk term `K` cannot be defined without importing a cost term from outside TaF's own structural constraints, the interior optimum is an artifact of the external import, not a TaF result.

3. **Circular `N`, `C`, `K` definitions**: If `N`, `C`, or `K` can only be defined with reference to `λ` in a way that trivializes the optimization (e.g., `N = a·λ` by definition), the hypothesis reduces to a tautology.

4. **Absorber closure**: If the full `λ*(s)` formalism — including all substrate-native definitions of `N`, `C`, `K` for TaF — maps cleanly onto a standard absorber (entropy production, Fisher information, Kolmogorov complexity), the hypothesis is absorbed. This is a clean result, not a failure.

---

## 5b. Investigation Routes and Success Criteria

The Note to Build Agent names four investigation routes and three possible outcomes. Mapped here for the TaF formal program:

**Route A — Dynamical Systems**
Does coherent structure formation maximize at some nonzero `λ`? Are there phase transitions, collapse regimes, or instability regimes? Covered by §1 (toy model) and §3 (absorption risk via optimal control). The key TaF-specific question: do the `N`, `C`, `K` terms have substrate-native TaF definitions (from `Ext_S` geometry, gluing costs, and obstruction classes) that produce a non-trivial interior optimum?

**Route B — Extension Category**
Can an extension category naturally induce an issuance rate? Is there a notion of extension density? Can extension density be optimized? Covered by §2 (mapping to `Ext_S` and `M` field). The open question is whether composition in the extension category imposes natural limits on `λ` — whether some `λ > λ_max` produces incoherent extension sequences that cannot form global sections.

**Route C — Observer-Reconciliation**
What issuance rates can be reconciled by a finite observer? What rates overwhelm the reconciliation machinery? This route connects to `kappa_i` (observer cadence) in the source-object spec. Also the most direct connection to GU formalization: the D2 claim (observer as record-bearing system) faces the same question — at what issuance rate does the observer's record-generation capacity saturate? See GU `explorations/time-as-finality-crosswalk/` for the observer-protocol contact point.

**Route D — Cosmological Analogy (strictly controlled)**
Do not derive cosmology. Do not claim dark energy. The Madau-Dickinson star-formation curve (§3) is the correct use of this route: it shows the same hump/decline shape arising from a completely different substrate (gravity vs. dark energy vs. structure collapse), confirming that the shape is generic. The goal of Route D is classification, not identification.

**Outcome criteria:**
- **Outcome 1**: No meaningful `λ*(s)` object exists; issuance is binary or categorical in TaF's formalism
- **Outcome 2**: `λ*(s)` exists but has no interior optimum (monotone in `λ`)
- **Outcome 3**: `λ*(s)` exists and admits an interior optimum derivable from TaF structural constraints — this registers as a new claim

All three outcomes are clean results. Outcome 1 and 2 constrain the program; Outcome 3 extends it.

---

## 6. Open Questions

1. **Can `N`, `C`, `K` be given substrate-native TaF definitions?** What plays the role of novelty gain in TaF's source-object formalism? What is the reconciliation cost in terms of the gluing data `G` and colimit machinery? What is the collapse risk in terms of obstruction classes?

2. **Is there a TaF derivation of the declining curve?** The tokenomics result (declining issuance is optimal under commitment) and the Madau-Dickinson cosmic curve suggest the hump/decline shape is robust. Can it be derived from TaF's structural constraints — the geometry of `Ext_S`, the cost of extending a restriction system, and the obstruction risk?

3. **What is the connection to observer cadence (`kappa_i`)?** If `λ` is the source-side issuance rate and `kappa_i` is the observer-side sampling cadence, the optimal `λ*(s)` implies constraints on `kappa_i` — how fast observers should sample to remain in the coherent regime. This is flagged as a possibility in the idea-capture, not yet a recommendation.

4. **Does the toy model `dS/dt = a·λ − b·λ² − c·S` have a TaF-typed version?** What are `a`, `b`, `c` in terms of TaF's formal objects? If `S` is the count of coherent global sections, `a` and `b` should be derivable from the restriction system's branching structure and the cost of patch reconciliation.

5. **Is a Python implementation of `λ*(s)` for a simple TaF-typed case useful?** Could live in `models/` alongside the existing Python implementations. Starting point: define `N`, `C`, `K` as simple functions of a scalar restriction system state and optimize numerically.

---

## 7. Placement Summary

| Idea | TaF destination | Action |
|---|---|---|
| `λ*(s) = argmax [N-C-K]` as dynamics of `Ext_S` | `open-problems/` or new claim | Register hypothesis candidate |
| `mu(r) = N(r) − C(r)` as optimality-derived source measure | `open-problems/temporal-issuance-source-object-spec.md` | Add as second mu candidate alongside mu_M |
| Observer cadence constraint from `λ*(s)` | Flagged only — not yet a recommendation | Hold until `kappa_i` layer is live |
| Tokenomics declining-curve result as existence proof | This exploration | Preserved — not a separate file |
| Commitment device → fixed issuance schedule → finality source | `CLAIM-LEDGER` or new claim | Candidate connection to finality |
| Absorption test for `N`, `C`, `K` | `open-problems/` | New open problem to add |
| Python implementation of toy model | `models/` | Optional; implement when `N`, `C`, `K` are typed |
