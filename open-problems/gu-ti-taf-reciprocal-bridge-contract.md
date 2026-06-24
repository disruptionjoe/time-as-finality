# GU / TI / TaF Reciprocal Bridge Contract

## Status

Open-problem incorporation note. This is not a claim upgrade.

## Purpose

Preserve the 2026-06-24 ten-lens reciprocal review and turn it into a contract
for future Time as Finality work involving Temporal Issuance and GU
formalization.

The contract is intentionally conservative:

```text
GU supplies sharper formal gates and absorbers.
TI supplies a formal source candidate under MLTT.
TaF supplies observer-finality, access, colimit, and source/readout discipline.
None of the three currently proves the others.
```

## Current Cross-Repo State

### Temporal Issuance

The current strongest formal source candidate is `Compat_G^MLTT`: it crosses
the expressiveness threshold as a formal staged-construction model. The
physical source question remains unresolved.

TaF should therefore treat TI as:

```text
formal-source stress test: live
physical-arrow evidence: not earned
```

### GU Formalization

GU's relevant contribution is not a solved physics bridge. It is a discipline:

- six-axis specification before advocacy;
- no-go assumptions and class exits;
- operator-algebra null models for fixed-H / fixed-observable behavior;
- Riemannian/Ehresmannian tests for derived versus independent structure;
- failure tensors such as `R_fail` that distinguish readout closure from
  source-equation closure.

### Time as Finality

TaF's relevant contribution is the observer-side record/finality layer:

- record-bearing observer class;
- accessible records and causal boundaries;
- finality relation;
- signed or semantic readout;
- local/domain-relative guardrails;
- colimit/descent conditions for multi-observer aggregation.

## Required Contract For Future Bridge Claims

Any future TaF/TI/GU bridge claim must fill this contract before it can be
treated as progress.

### 1. Source Object

Declare:

```text
Y_source
source relation or admissibility predicate
source measure or capability object
source-to-record generation map
observer access/cadence/boundary data
identity, overlap, and gluing data
```

For Temporal Issuance, this should specialize the existing `Y_TI`,
`pi_TaF`, `Cap_TI`, and native comparison `R_K_TI` burden from
`temporal-issuance-source-object-spec.md`.

### 2. Six-Axis Table

Fill the GU-style six-axis table:

```text
L1 substrate
L2 observer
L3 pairing
L4 causal order
L5 emergence class
L6 coordination loop
```

If any field is blank or metaphorical, the proposal is not rejected; it is
returned for typing.

### 3. Same-Neighbor-Data Freeze

Before claiming residue, freeze:

```text
causal order
metric or causal-set volume/counting data
observer worldlines/access regions
detector sampling/cadence
thermodynamic and information ledgers
record-generation rule
identity/overlap/gluing data
gauge, label, basis, and foliation convention
```

If a claimed split disappears after this freeze, it belongs to the absorber.

### 4. H-Fixed / H-Growing Split

For quantum or predictive-accessible claims:

```text
fixed-H null:
  fixed Hilbert space, fixed observable algebra, fixed channel/instrument,
  or fixed H_infty with access maps explains the transition.

H-growing success:
  no fixed structure reproduces the transition while preserving observable
  types, record maps, perturbation effects, and admissibility predicates.
```

This is the current physical-source gate for TI-C020-like claims.

### 5. Double-Diagram Separation

Do not collapse TaF colimits and GU/TI filtrations into one construction.
Use a two-axis diagram:

```text
horizontal: observer-domain descent / local-to-global gluing
vertical: record/source filtration or staged admissibility growth
```

The best theorem-shaped target is:

```text
S : Compat_G^MLTT -> FiltSh(C)
R : FiltSh(C) -> ReadoutValues
```

and a witness where `R` depends on a transient `H^1(X, F_tau)` class that is
not determined by the final sheaf alone.

### 6. No Global Commit Order

Any finality, issuance, or consensus language must remain local,
domain-relative, or cover-relative. A hidden universal present, global ledger,
or total order over spacelike-separated events fails the contract.

## Incorporation Into TaF Research Lines

### H7

The bridge does not reopen H7 as a physical-arrow claim. It reinforces H7's
current narrowed role:

```text
source/readout factorization target
reverse-edge and resource-accounting audit discipline
```

### S1

The bridge suggests a useful S1 refinement: represent observer-local finality
aggregation and record/source filtration as separate axes. This may help avoid
confusing a finite colimit control with spacetime derivation.

### Q1 / Signed Readout

The GU signed-readout theorem is a good companion: provenance can remain
monotone while scalar readout is non-monotone. TaF should use this to keep
record accumulation, finality, and scalar interpretation separate.

### MTI / Metric-Causal Separation

The MTI metric-causal separation and GU/TaF rate comparisons should preserve
units and powers. Compare rate-squared quantities with rate-squared quantities
such as `lambda_max^2` or `Gamma_min^2`; do not compare GU `Lambda` directly
to raw rates.

## Guardrails

- Do not treat TI as H7 evidence without the source-object contract.
- Do not treat GU observerse projection as source issuance; it is usually a
  fixed-source projection absorber.
- Do not treat TaF colimits as spacetime derivation without causal, metric,
  covariance, and locality gates.
- Do not cite the cross-repo bridge as canon in any repo.
- Do not merge claim ledgers.

## Best Next TaF-Side Work

1. Create a six-axis version of the TI-C020 fixed-H vs H-growing physical
   fixture.
2. Add the double-diagram requirement to future S1 or source/readout bridge
   proposals.
3. Re-run any `lambda_max` / Sorkin absorption claim with access window,
   cadence, resource clock, and queue/frontier behavior explicitly typed.
4. Test whether TaF's source-object contract can host a filtered sheaf readout
   whose transient obstruction matters to a signed/semantic readout.
