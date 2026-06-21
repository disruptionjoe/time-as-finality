# T124: Constructor-Admissibility Grounding Audit

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [Arrow of Time as Constructor Theorem](../open-problems/arrow-of-time-as-constructor-theorem.md)
- [T18: Finality Direction Theorem](T18-finality-direction-theorem.md)
- [T80: Reversible Finality Nonmonotonicity](T80-reversible-finality-nonmonotonicity.md)
- [T84: Cyclic Reconciler Entropy Export](T84-cyclic-reconciler-entropy-export.md)
- [T106: Bounded-Sink Reversible Compression](T106-bounded-sink-reversible-compression.md)
- [T110: Finite-Permutation Monotone Obstruction](T110-finite-permutation-monotone-obstruction.md)
- [T116: Open Markov Record-Entropy Comparison](T116-open-markov-record-entropy.md)
- [T122: Stationary Markov Monotone Obstruction](T122-stationary-markov-monotone-obstruction.md)

## Setup

This audit is implemented in v0.1:

- model: `models/constructor_admissibility_grounding_audit.py`
- runner: `models/run_t124.py`
- tests: `tests/test_constructor_admissibility_grounding_audit.py`
- results: `results/constructor-admissibility-grounding-audit-v0.1-results.md`
- report: `TECHNICAL-REPORT-constructor-admissibility-grounding-audit-v0.1.md`

T18 proves a conditional constructor-style claim: if admissible
transformations are componentwise monotone in the D1 vector, strict
finalization induces a partial direction and its reverse is inadmissible.
T124 asks what would be required to ground that admissibility rule in a
physics-facing model rather than treating it as a stipulated ordering.

The audit should classify candidate transformations on record states into at
least four buckets:

```text
constructor-impossible       = forbidden by the stated physical substrate
resource-impossible          = possible only if a named resource is absent
resource-consuming possible  = possible while drawing down named capacity,
                               free energy, sink space, exported history, or
                               boundary conditions
reversible possible          = possible with the full state, memory, sink, and
                               return path included
```

For each candidate D1-increasing edge, the audit must also classify the
reverse edge. A physical reading of H7 is not allowed unless the reverse is
shown to be constructor-impossible or is blocked only after naming the
resource, boundary, excluded environment, postselection condition,
coarse-graining, or impossible transformation that does the blocking.

The starting fixtures should include the witness families already used by
T80, T84, T106, T110, T116, and T122, because those tests identify where
unqualified physical-arrow readings fail.

## v0.1 Result

The reverse-edge ledger audits T18, T80, T84, T106, T110, T116, T122, and
T128-style cases. No current case permits an unqualified physical-arrow
reading. Strict surviving cases split into two weak classes:

- resource-accounting only: exported history, erasure, sink capacity, path
  irreversibility, fresh blank capacity, finite nonrenewed resource drawdown;
- constructor-only: reverse transformations are inadmissible by the declared
  constructor rule.

T124 therefore protects H7 from promotion. The strongest current claim is that
H7 is an audited admissibility ledger: every strict D1-increasing edge must
classify the reverse edge under the same accounting boundary before it can be
used physically.

## Success Criteria

- Restate T18's D1-monotone admissibility rule as an auditable physical
  hypothesis rather than a theorem premise.
- Provide a transformation ledger that separates strict impossibility,
  practical irreversibility, resource drawdown, coarse-graining, and ordinary
  reversible evolution.
- For every proposed strict finalization edge, name the status of the reverse
  edge under the same substrate and accounting boundary.
- Preserve T80's warning that raw reversible local dynamics can decrease the
  observed D1 trace profile.
- Preserve T84 and T106's warning that monotone retained records obtained from
  cyclic or bounded memory require exported history, erasure, sink capacity,
  or a return-path audit.
- Preserve T110's finite closed reversible obstruction: a strict scalar
  finality monotone cannot live on a closed finite permutation orbit.
- Preserve T116 and T122's stochastic constraints: open or stationary Markov
  record arrows must be separated from path irreversibility, fresh capacity,
  exported history, transient sectors, postselection, and nonstationary
  resource drawdown.
- State exactly which surviving H7 content is constructor-theoretic and which
  is open-system/resource-accounting content.

## Failure Criteria

- Treat T18's D1-monotone admissibility rule as physically grounded without an
  audit of the reverse transformations.
- Claim a thermodynamic arrow derivation from finality alone.
- Claim a closed reversible physical arrow while omitting memory, sink,
  environment, return-path, or reverse-channel degrees of freedom.
- Count exported records, erased records, blank capacity, free energy,
  boundary conditions, or hidden postselection as free.
- Infer a strict arrow from entropy production, path log-ratio, or biased
  circulation alone without a scalar finality monotone that clears the T116 and
  T122 controls.
- Count a coarse-grained monotone as a fundamental closed-system monotone
  without naming the coarse-graining and the information discarded by it.
- Upgrade H7 beyond a constructor/resource-accounting lemma unless the audit
  names the impossible transformations or resources that make the reverse
  inadmissible.

## Known Physics Constraints

- This audit must not derive, or claim to derive, the thermodynamic arrow.
- A closed finite reversible substrate is represented by a permutation; on a
  complete orbit, any nondecreasing scalar score is constant if the orbit is
  closed and recurrent.
- Locally reversible dynamics can produce nonmonotone observer-window D1
  profiles, so local reversibility alone does not ground T18 admissibility.
- Monotone record retention in finite cyclic memory requires exported history,
  erasure, hidden garbage, fresh blank capacity, or some other named resource
  or boundary.
- Finite stationary Markov dynamics have zero stationary expected drift for
  any scalar score; strict expected finality must live in transient,
  nonstationary, infinite-state, resource-explicit, or boundary-conditioned
  sectors.
- Practical irreversibility is not constructor impossibility unless the audit
  specifies the limiting resource, excluded operation, or physical law that
  makes the reverse inadmissible.

## Contribution Needed

Define a physics-grounded admissibility ledger for the T1-style record graph
or another explicit record substrate. The ledger should identify which
transformations are strictly impossible, which are possible only with named
resources or excluded reverses, and which remain reversible when all degrees of
freedom are included.

The useful deliverable is a future executable or formal check that takes this
ledger as input and reports whether T18's D1-monotone constructor rule survives
without smuggling in an unacknowledged thermodynamic arrow, hidden environment,
fresh capacity, or omitted reverse path.
