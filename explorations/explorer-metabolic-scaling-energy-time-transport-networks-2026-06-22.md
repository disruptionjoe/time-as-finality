# Explorer: Metabolic Scaling, Energy-Time Co-Equality, and Typed Multiscale Transport Networks

**Date:** 2026-06-22  
**Origin:** Cross-program synthesis — Moses (2020 SFI Complexity podcast; Moses et al. 2016, "Energy and time determine scaling in biological and computer designs")  
**Status:** Exploration — candidate connections to TaF formal program, not yet integrated into claims  
**Connects to:** typed multiscale transport network (next research target), temporal issuance source object (`temporal-issuance-source-object-spec.md`), D1RestrictionSystem transport graph

---

## 0. What This Document Does

Melanie Moses's metabolic scaling work establishes a formal result — sublinear metabolic rate scaling B ∝ M^{3/4} — derived from a joint energy-time optimization over hierarchical branching transport networks. The derivation has two properties relevant to TaF:

1. **Time is co-equal with energy as an optimization constraint.** The 3/4 exponent cannot be derived by optimizing energy alone or time alone. It requires minimizing both simultaneously. This is a formal statement that temporal delivery constraints are constitutive of optimal transport network architecture.

2. **The result applies to any substrate where resources are distributed through branching networks under energy and time constraints.** Moses shows empirically and theoretically that microprocessors, server farms, and distributed computing systems exhibit the same scaling, for the same reasons. The principle is substrate-independent.

Both properties bear directly on TaF's program.

---

## 1. The Moses Framework

### The biological result

In biological organisms, resources (oxygen, nutrients, ATP) are distributed from central supply to distributed demand through hierarchical, space-filling, branching transport networks. Natural selection has tuned these networks over evolutionary time.

The West-Brown-Enquist model (extended by Moses et al.) captures this by optimizing a joint cost function over the branching architecture:

```
minimize: α·(energy dissipation) + β·(delivery time)
subject to: network fills volume V; terminal units have fixed size
```

The solution is a self-similar (fractal-like) branching hierarchy. The scaling exponent for metabolic rate falls out as:

```
B ∝ M^{3/4}
```

The exponent **depends on the joint optimization**. Pure energy minimization gives a different exponent. Pure time minimization gives a different exponent. The 3/4 law is the signature of the energy-time tradeoff being simultaneously satisfied across scales.

### Extension to computing

Moses et al. (2016) show that power consumption in microprocessors and server farms scales with system size following the same sublinear pattern, for the same underlying reason: hierarchical distribution of power and signals through on-chip interconnect networks faces the same energy-dissipation vs. delivery-time tradeoff.

The architectural transitions matter: monolithic chip designs saturate the scaling law early (hitting thermal limits). Distributed multi-core and cluster architectures open a new scaling regime — analogous to the evolutionary transition from unicellular to multicellular life, which changed the metabolic scaling exponent by introducing a new level of hierarchical organization.

---

## 2. Connection to TaF: Time Is Co-Equal, Not Secondary

### The formal statement

The 3/4 power law is a proof by construction that **temporal delivery constraints cannot be subordinated to energy constraints in optimal transport network design**. A network optimized for energy alone does not achieve the observed scaling — and is not the architecture evolution or engineering selects. A network optimized for time alone also does not achieve it.

The joint optimization is not a convenience or approximation. It is what the problem requires.

In TaF terms: this is a physical existence proof that time is a co-equal constraint in optimal information and resource transport — not a downstream parameter you tune after solving the energy or capacity problem. The network topology that optimizes purely for throughput (energy analog) or purely for latency (time analog) is strictly suboptimal. The Pareto-efficient architecture is the one that jointly satisfies both.

### Relevance to TaF's core claim

TaF's program is grounded in the claim that temporal finality has fundamental status — that time is not a label on states but a constitutive property of what it means for an event to be real or ordered. The Moses framework provides an independent route to a weaker but related formal claim: in any system that distributes resources through a network under physical constraints, temporal delivery is not derivable from or reducible to energy delivery. Both enter the optimization independently.

This does not prove TaF's full claim (which is stronger), but it provides a formal anchor for the claim that time is not a derived or secondary quantity in the physics of networked systems.

---

## 3. Connection to the Typed Multiscale Transport Network Research Target

TaF's identified next research target is a **typed multiscale transport network**. Moses's framework is the canonical mathematical treatment of exactly this structure in the physical domain.

The key components of the Moses model and their TaF analogs:

| Moses framework | TaF analog |
|---|---|
| Branching transport network | D1RestrictionSystem transport graph |
| Terminal units (cells, processor cores) | Sites in the D1 restriction system |
| Energy dissipation per branch | Edge cost in the transport graph |
| Delivery time per path | Propagation latency from source to site |
| Space-filling constraint | Coverage requirement (all sites accessible) |
| Hierarchical branching levels | Nested restriction maps across scales |
| Self-similar (fractal) architecture | Functorial self-similarity in the D1 formalism |
| B ∝ M^{3/4} scaling law | Candidate: typed scaling law for epistemic throughput |

The D1RestrictionSystem already has a transport graph and patch constraints. What Moses's framework adds is:
- A precise cost function (joint energy-time) over the transport graph
- A derivation of the optimal branching architecture from that cost function
- A scaling law that holds across orders of magnitude in system size

The typed multiscale transport network research line would benefit from formalizing this cost function in D1 terms — specifying what plays the role of energy dissipation and delivery time for the relevant TaF substrate (record transport, finality propagation, observer-to-source access).

---

## 4. Connection to Temporal Issuance Source Object

The temporal issuance source object spec (`temporal-issuance-source-object-spec.md`) requires a typed `mu` field — a source measure with units, domain, comparison rule, additivity or monotonicity, and transformation behavior.

Moses's metabolic scaling framework offers a candidate specification for `mu`:

**Candidate: metabolically-scaled source measure**

```
mu_M : R -> R_+
mu_M(r) = c · |r|^{3/4}    where |r| is the "mass" (extent, complexity, or cardinality) of realization r
```

Properties:
- **Units**: energy per unit time (power), or its analog in the relevant substrate
- **Monotonicity**: mu_M is monotone in system size (|r|)
- **Sublinearity**: mu_M(r) / |r| is decreasing in |r| — larger systems are more efficient per unit
- **Transformation behavior**: scales as a power law under size rescaling; this is the key constraint
- **Additivity**: not additively decomposable (which is correct — the whole network is more efficient than the sum of its parts)

The non-additivity is significant. The current absorber candidates for `mu` (volume/counting, entropy production, Shannon information) are all additive or at least sub-additive in ways that prevent the superefficiency-at-scale property. A metabolically-scaled measure that is sublinear in size is genuinely different from any of the standard absorbers.

**Open question**: Does mu_M survive the same-neighbor-data freeze? The freeze requires ruling out that mu_M can be absorbed by the existing absorbers (entropy production, information-theoretic measures, or ordinary event counting) when all other fields in the source object are held fixed. The sublinear scaling under size increase is the discriminating signature — if it persists when `<`, `dR`, and `G` are matched between a small and a large system, mu_M is a genuine residue.

---

## 5. Architectural Transitions and Scaling Regime Shifts

Moses explicitly addresses what happens at evolutionary transitions: multicellularity changed the metabolic scaling exponent by introducing a new hierarchical level. The transition is not continuous — it opens a new scaling regime.

The computing analog: distributed multi-core architectures and cloud computing represent a transition equivalent to multicellularity. The monolithic architecture's scaling law saturates; the distributed architecture operates under a new law with different exponent and efficiency frontier.

**TaF relevance**: If the temporal issuance framework represents an architectural transition — not an incremental improvement on existing record-keeping but a new hierarchical level of epistemic organization — then the scaling law for legitimate validity at scale should change at the transition point. Pre-transition: validity degrades superlinearly with group size (human institutional scaling). Post-transition: validity scales sublinearly (AI-native, network-optimized scaling). Moses's framework provides the formal mechanism: the transition opens a new regime because it introduces a new hierarchical level in the transport network.

---

## 6. Open Questions for the TaF Formal Program

1. **What is the TaF cost function?** What plays the role of energy dissipation and delivery time in the formal TaF transport graph? Candidate: energy dissipation → cost of record propagation; delivery time → finality latency from issuance event to observer confirmation. If these can be formalized in D1 terms, the Moses optimization applies directly.

2. **Does the D1 transport graph admit a hierarchical branching structure?** The D1RestrictionSystem has a transport graph and patch constraints. Can a hierarchical branching restriction system be defined whose global sections satisfy the space-filling and terminal-unit constraints from Moses's model?

3. **Is mu_M a genuine same-neighbor-data residue?** Does the sublinear scaling property survive when all other source object fields are matched between small and large systems? This is the discriminating test for whether a metabolically-scaled mu earns a slot in the temporal issuance source object.

4. **Does the 3/4 exponent have a TaF derivation?** Moses derives 3/4 from 3D space-filling branching with fixed terminal size. In TaF's framework, the relevant "dimensionality" may be different (causal structure, not geometric space). What exponent does the joint energy-time optimization yield under TaF's structural constraints?

5. **Does the architectural transition model apply to finality?** At what participation threshold (if any) does the temporal issuance framework shift from the human-institutional scaling regime to the network-optimized regime? Is this threshold derivable from the transport network formalism?

---

## 7. Summary Assessment

Moses's framework is not a metaphor or loose analogy. It is a formal derivation — joint energy-time optimization over hierarchical branching transport networks — that produces a precise scaling law and applies across biological and engineered substrates. Its relevance to TaF:

- **Formal support for time as co-equal** (not derived from energy) in optimal network architecture — directly supports TaF's core temporal claim
- **Candidate for typed multiscale transport network formalism** — provides the cost function and derivation structure the research target needs
- **Candidate mu specification** for the temporal issuance source object — sublinearly-scaled measure that may not be absorbed by existing standard absorbers

The key tests are the same-neighbor-data freeze for mu_M and whether the D1 transport graph can be given the right hierarchical branching structure. Both are formal rather than conceptual questions.
