# Cross-Domain Shadow Protection Theorem

> **DORMANT (as of 2026-06-26).** No downstream references in tests/, models/,
> results/, CLAIM-LEDGER, or ROADMAP. Kept for the record; not an active line.

## Status

Open theorem target. This file is a research target extracted from the
North Star v0.8 62-persona steelman and Hegelian pass.

It does not promote the North Star vision. It defines the theorem-shaped
object that would make the vision non-rhetorical in a bounded form.

## Problem

Can one projection-sufficiency theorem shape survive across more than one
mature domain without collapsing into unrelated domain-specific bookkeeping?

The candidate theorem shape from the North Star is:

```text
For an internal observer O embedded in a source system Y, and for a task family
T under horizon h and boundary B, the observer shadow pi_O is capability-
sufficient exactly when it preserves the minimal native data required for the
relevant transport, access, representation, boundary, record, and operation
structures.
```

This is not yet a theorem. The open problem is to find the smallest version
that can be stated, tested, and refuted.

## Minimal Formal Shape

For each domain `D`, declare:

```text
Y_D       source structure
O_D       observer/access profile
pi_D      observer shadow
X_D       visible codomain
~=_X,D    visible equivalence
Cap_D     domain-native capability object
K_D       capability codomain
R_K,D     native capability comparison
A_D       admissible source states
```

Define shadow protection in domain `D`:

```text
pi_D(y1) ~=_X,D pi_D(y2) => Cap_D(y1) R_K,D Cap_D(y2)
```

The cross-domain target is not that all `K_D` are the same. It is that the
same proof spine works:

```text
shadow protection <=> native capability spread over visible fibers is
singleton, bounded, or collapsed by the declared native comparison
```

## Candidate Domains

Start with at least two, preferably one formal/computational and one
physics-facing domain.

1. Database or process-semantics projection.
2. Quantum resource theory under explicit access profiles.
3. Causal-access or horizon records.
4. Typed transport networks and LossKernel witness obligations.
5. Distributed consensus finality.

## Success Criteria

The target strengthens if:

- two mature domains instantiate the same audit spine without changing the
  definition after seeing the examples;
- each domain has a positive preservation control and a negative
  non-factorization fixture;
- native absorber state and theorems are granted before residue is assigned;
- the theorem statement can name exactly which minimal enrichment repairs
  shadow failure;
- the result is useful even when all residue is translation residue.

## Failure Criteria

The target should be demoted if:

- every domain requires unrelated ad hoc definitions;
- `Cap` is gerrymandered to match the hidden variable;
- mature absorber fields restore sufficiency with no useful transfer;
- the only universal statement left is the trivial fiber-constancy lemma;
- no domain supplies a nontrivial negative fixture after native state
  completion.

## First Bounded Run

Use the template:

```text
workflows/templates/north-star-shadow-audit.template.md
```

Fill it twice:

1. Once for a database/view-determinacy or process-semantics example.
2. Once for a quantum resource theory access-profile example.

Then compare only the proof spine:

```text
visible fiber -> capability spread -> native absorber -> minimal enrichment
```

Do not compare surface vocabulary.

## Claim Impact If Successful

Do not promote a physics claim.

A successful first run would justify this narrower statement:

```text
The North Star shadow-protection theorem has a reusable audit spine across at
least two mature domains.
```

That would support further theorem hunting, not the maximal vision itself.

## Claim Impact If Refuted

If the theorem shape collapses, preserve the negative result:

```text
The maximal North Star currently functions as a heuristic atlas problem, not a
single cross-domain theorem target.
```

That is still useful because it tells the project not to force unity before
the charts glue.
