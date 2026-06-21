# P31 - AI Learning Theory Researcher Run

- persona: AI Learning Theory Researcher
- goal_id: P31
- run_timestamp: 2026-06-21T16:04:30-05:00
- queue_source: `explorations/persona-future-run-goals-2026-06-20.md`
- goal: Test whether finality axes remain identifiable under representation
  changes, learned embeddings, and feature transformations.
- posture: bounded exploratory run only; no claim-status update, roadmap
  change, or ledger edit.

## Repo Context Read

- `FORMALISM.md`
- `claims/IPT-invariant-preserving-transformations.md`
- `tests/T22-d1-physical-reduction-map.md`
- `tests/T23-invariant-preserving-transformations.md`
- `tests/T25-minimal-d1-generalization.md`
- `tests/T26-d1-restriction-system.md`
- `tests/test_invariant_preserving_transformations.py`
- `tests/test_d1_restriction_system.py`
- `explorations/persona-goal-runs/2026-06-21-045454-p20-physics-informed-ml-identifiability-audit.md`
- `explorations/persona-goal-runs/2026-06-20-164451-relocation-archetype-audit.md`

## Bounded Run

Question: when a record/state description is reparameterized, compressed, or
sent through a learned representation, which TaF coordinates remain honest
objects of the representation and which become underidentified or replaced by
priors?

Method:

1. Use T26's positive relabel morphism as the exact-control case for
   representation invariance.
2. Use T23/T22 as the conservative positive case for typed but lossy
   reduction: invariance is allowed only for named preserved invariants.
3. Use the P20 identifiability audit and the relocation audit's
   `prior substitution` failure mode as the hostile case for learned
   embeddings and feature transforms.

## Work Performed

I split "representation change" into three regimes:

1. exact relabeling / isomorphism;
2. declared lossy reduction with preserved-invariant certificates; and
3. learned or hand-built feature compression without source-lift witnesses.

The key repo question is not whether downstream performance is stable. It is:

```text
does the representation map preserve the declared D1 object or only a task
surrogate?
```

That is a stricter criterion than "an embedding predicts the same labels."

## Result

### Main Finding

The current repo supports **representation invariance only in typed,
certificate-carrying cases**.

It does **not** support the stronger claim that finality axes are generally
invariant under learned embeddings or arbitrary feature transformations.

Observer access is therefore not representation-free in the current evidence.
It is representation-dependent unless the map carries explicit preservation
data.

### Representation Audit Table

| regime | repo witness | what survives | what fails or remains open | verdict |
| --- | --- | --- | --- | --- |
| exact relabeling / isomorphism | T26 positive relabel morphism | local D1 profiles and trusted reachability survive when the site map and restriction checks pass | none beyond the declared morphism scope | honest invariance |
| typed lossy reduction | T23 observer-access and T23/T22 reduction schema | only named preserved invariants survive: pointer basis, accessible support, holder redundancy, observer-access indexing | unitary history, branch-support detail, and other discarded structure are allowed losses | partial invariance only |
| graph/transport collapse to coarser summaries | T25/T26 boundary | scalar/vector summaries can lose trusted reachability or gluing data even when endpoint values match | representation can hide graph structure required for the verdict | underidentified without transport data |
| learned embedding / feature transform without witness obligations | P20 plus relocation audit `prior substitution` control | maybe task performance, similarity, or coarse prediction | D1-axis identifiability is not certified; missing source structure can be filled by learned priors | not admissible as invariance evidence |

### Axis-by-Axis Consequence

The safest current reading is:

- `accessible_support` and `holder_redundancy` can survive a representation
  change only when the observer access boundary and preserved invariants are
  declared explicitly.
- `branch_support` is still fragile under reduction. Even the T23/T22 positive
  lane treats branch-support detail as losable structure rather than an
  invariant that the reduction preserves.
- `reversal_cost` has no current representation-invariance witness. T22 still
  classifies it as formal only, and P20 shows that trajectory-like observables
  can hide non-identifiability behind proxy features.

So the bounded answer to P31 is conservative:

```text
TaF axes are not "embedding invariant" by default.
They are only invariant relative to a declared transport class.
```

### Smallest Honest Learning-Theory Statement

The repo can presently support this statement:

```text
A representation change is admissible for TaF only if it comes with either
(a) an exact morphism witness, or
(b) a typed preserved-invariant certificate naming exactly which D1
coordinates survive and which are allowed losses.
```

It cannot yet support this stronger statement:

```text
Any sufficiently good learned representation recovers observer access or D1
axes up to equivalence.
```

That stronger claim fails the current hostile controls because equal task
performance can coexist with missing witness obligations, hidden graph
transport, or prior substitution.

## Proposed Next Action

If this lane is continued later, the next bounded step should be an explicit
adversarial representation benchmark:

1. build paired source fixtures with the same coarse features or embedding
   coordinates but different D1-relevant transport/access structure;
2. require the evaluator to classify each axis as `preserved`,
   `underidentified`, or `lost`;
3. include one exact relabel positive control, one typed reduction positive
   control, and one learned-summary negative control; and
4. treat abstention as success whenever the representation lacks a witness
   certificate.

That would convert "representation dependence" from a prose warning into a
finite executable audit.

## Claim-Status Posture

- No claim-status changes proposed.
- No roadmap or ledger changes proposed.
- Status of this run: exploratory representation-invariance boundary audit.
- Best current classification: TaF currently has typed transport invariance,
  not general learned-representation invariance.
