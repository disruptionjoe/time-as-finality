# Candidate North Star Next Version Update Queue v0.5

## Status

This is the next-version review queue after:

```text
Candidate North Star v0.4.md
```

It is not a new Candidate North Star draft.
It is not canon.
It is not a replacement for v0.4.
It is a shareable handoff file for fresh reviewers and other agents.

Purpose:

```text
Give reviewers one file that states the current baseline, locked posture,
required source documents, and possible adjustments to check before any v0.5
draft is made.
```

Current instruction:

```text
Do not draft v0.5 yet.
Use this queue to capture only adjustments that may be needed.
Preserve the v0.4 posture unless a concrete correctness issue requires change.
```

## Current Baseline

The current working version is:

```text
Candidate North Star/Candidate North Star v0.4.md
```

v0.4 should be treated as the baseline for all fresh-eye review.

The core v0.4 posture is:

```text
Capability Projection is a typed projection-sufficiency audit language.
It is not, by itself, a novelty claim that projection loses information.
It is not a replacement physics program.
It is not allowed to derive known physics from Cap.
```

The main value claim is deliberately modest and strong:

```text
The bare non-factorization pattern is heavily absorbed by existing fields.
The possible surviving value is a disciplined cross-domain audit language for
typing projections, capabilities, equivalences, absorbers, and any residue that
survives same-neighbor-data testing.
```

## Document Strategy

The current document strategy is locked unless reviewers find a concrete reason
to change it:

```text
Make the main Candidate North Star note shorter.
Let appendices, reports, and future companion notes do the heavy lifting.
```

Implications:

- The main note should carry the formal spine, audit posture, success/failure
  criteria, and reviewer checklist.
- It should not try to teach all prior art, all mathematics, all physics, or
  all database absorption inside the main body.
- Dense material should move into appendices or companion reports.
- Additions to the main note should pass a high bar: they must prevent a
  foreseeable misunderstanding or repair a correctness gap.

Fresh reviewers should explicitly answer:

```text
Is this proposed change necessary for the main note, or should it be appendix
material?
```

## Required Source Map For Reviewers

Reviewers should treat the following as the relevant source bundle for v0.5
queue work:

```text
Candidate North Star/Candidate North Star v0.4.md
Candidate North Star/Candidate North Star Output Report v0.4.md
Candidate North Star/Fresh-Eyes Review Candidate North Star v0.4.md
Candidate North Star/Candidate North Star Low-Hanging Dispatch Synthesis v0.1.md
Candidate North Star/Candidate North Star Low-Hanging Formal Patch Report v0.1.md
Candidate North Star/Candidate North Star Low-Hanging Physics Patch Report v0.1.md
Candidate North Star/Candidate North Star Low-Hanging Editorial Patch Report v0.1.md
Candidate North Star/Candidate North Star Mathematical Strengthening Suggestions v0.1.md
Candidate North Star/Candidate North Star 20 Mathematics Perspectives Report v0.1.md
Candidate North Star/Candidate North Star 20 Physics Perspectives Report v0.1.md
Candidate North Star/Prior-Art Audit of Capability Projection-deep-research-report.md
Candidate North Star/Database Absorption Test for Capability Projection-deep-research-report.md
Candidate North Star/Prior Art And Physics Grounding For Capability Projection - Deep Research.md
Candidate North Star/Strongman for physics sections.md
Candidate North Star/Database Expert Lens Review v0.1.md
Candidate North Star/Capability Projection Schema v0.1.md
Candidate North Star/Capability Projection Action Report v0.2.md
```

The math and physics reports are especially important for this queue. The
review should not only ask whether v0.4 is readable; it should ask whether v0.4
preserves the mathematical discipline and physics strength those reports
required.

## Linked Review Reports

```text
Candidate North Star/Candidate North Star Pre-v0.5 Readiness Review v0.1.md
```

[Pre-v0.5 Readiness Review v0.1](./Candidate%20North%20Star%20Pre-v0.5%20Readiness%20Review%20v0.1.md)
— Claude (Cowork) review of v0.4. Headline: the schema is sound and the prior-art
and database research are discharged; the gating work before v0.5 is to run at
least one witness end-to-end through the audit (Gate 1), decide the physics-forward
question explicitly (Gate 2), and name the canonicity criterion and transfer
theorem as open problems. Mergeable patches map to queue items Q2, Q6, Q7.

## Locked Postures

### 1. Global Absorption First

The database result generalized into a broader posture:

```text
Absorption is not a database-only issue.
The bare factorization failure is old across many mature fields.
```

Reviewers should ask which existing field already owns each version of the
claim before treating anything as Candidate North Star residue.

Primary absorbers include:

- database view/query determinacy, provenance, indexing, MVCC, access control,
  approximate retrieval, and workload equivalence;
- statistical decision theory, Blackwell comparison, and Le Cam deficiency;
- abstract interpretation, complete abstractions, and Galois connections;
- concurrency, process semantics, testing equivalence, bisimulation, and
  linear-time/branching-time spectra;
- POMDP belief states, observability, controllability, and sufficient
  statistics;
- causal observational/interventional equivalence;
- quantum information, resource theory, gauge theory, and algebraic/local
  observables.

Do not let v0.5 drift back into:

```text
projection loss is surprising
```

The stronger position is:

```text
projection loss is common; the question is what typed capability audit,
absorber mapping, and residue discipline still add.
```

### 2. Strong Physics Stance

The physics posture from `Strongman for physics sections.md` and the physics
reviews remains locked:

```text
Known physics induces Cap.
Cap does not derive known physics.
```

Physics sections must be strong enough to be worth expert scrutiny while
avoiding free-physics claims.

Locked constraints:

- Every physics witness must state the model family, observer, access profile,
  gauge constraints, equivalence relation, horizon, and resource boundary.
- Gauge-variant capability is not allowed as a physical witness.
- A strictly local observer may not be credited with global, purifier,
  environment, horizon, or asymptotic access unless the access profile grants a
  physical route.
- Dark matter, dark energy, holography, quantum error correction, horizon
  thermodynamics, and related cases are at most typed tests unless the same
  neighboring data and access conditions are specified.
- Physics examples should be absorbers, calibration cases, or carefully typed
  stress tests before they are called residue.

Reviewer question:

```text
Does v0.4 preserve the strong physics posture, or does any sentence imply that
Capability Projection explains, derives, or replaces existing physics?
```

### 3. Mathematical Type Discipline

v0.4's formal core should remain centered on typed projection sufficiency:

```text
pi_{O,Sigma,r,U}: Y -> X_{O,Sigma,r}(U)
Cap_{O,T,h,B}: Y -> K_{O,T,h,B}
```

The quotient/equivalence discipline is now part of the baseline:

```text
Cap factors through visible state only after the relevant visible equivalence
and capability equivalence are declared.
```

Reviewers should check:

- `~=_X` is clear enough for visible-state equality.
- `~=_K` is either an equivalence relation or explicitly replaced by its
  induced equivalence when quotienting is used.
- The factorization claim is through `X / ~=_X`, not accidentally through raw
  `X` when equivalence classes are intended.
- The fiber-constancy lemma, minimal capability-preserving quotient,
  capability spread, and trivial enrichment theorem are mutually consistent.
- Approximate equivalence is first-class where exact equality is the wrong bar.

Do not weaken this into informal sameness language.

### 4. Finite Pair Tests Are Necessary But Weak

Finite witnesses remain useful, but they are not decisive by themselves.

Locked posture:

```text
Finite pairs can show a typed failure under declared pi, Cap, equivalences,
and access.
They do not by themselves prove novelty, canonicity, or non-absorption.
```

Reviewers should flag any example that uses:

```text
same payload
same current value
same visible state
```

without declaring the relevant schema, constraints, view, transaction context,
lineage, materialization/index state, access policy, consistency model,
embedding model, metric, workload, or physical access profile.

### 5. Canonical Residue Is The Hard Target

The residue ladder should remain central:

```text
canonical residue
formal residue
translation residue
heuristic residue
redundant/demoted
```

The hard target is not to find any non-factorization example. The hard target
is to find a case where:

- the projection is independently natural;
- the capability is independently natural;
- same-neighbor-data comparison has been done;
- mature absorber theories have been checked;
- enrichment is not natural, available, minimal, or standard;
- the remaining failure is not merely a translation of known theory.

Fresh reviewers should be strict here.

### 6. Enrichment Is Allowed And Often Absorbs The Claim

The trivial enrichment theorem is not a weakness to hide. It is a control:

```text
pi'(y) = (pi(y), Cap(y))
```

makes factorization trivial.

The real question is whether the enrichment is:

- domain-natural;
- minimal;
- canonical;
- available to the observer;
- standard in an absorber field.

If enrichment is standard, the case probably becomes translation residue or
redundant/demoted rather than canonical residue.

### 7. Time As Finality Relationship

Candidate North Star is adjacent to Time as Finality, not a replacement for it.

Locked posture:

```text
TaF may motivate why projection, irreversibility, and observer-relative
capability matter.
Candidate North Star should still stand or fall as a typed sufficiency audit.
```

Avoid making TaF carry proofs that belong in the typed audit schema.

## Review Questions For Fresh Agents

Fresh agents should use the source map above and leave only concrete queue
items. Useful review questions:

1. Is anything in v0.4 mathematically incorrect?
2. Is anything in v0.4 physically incorrect or overclaimed?
3. Does v0.4 still underspecify visible-state equality anywhere?
4. Does v0.4 clearly distinguish exact, approximate, probabilistic, top-k,
   recall, latency/recall, and workload equivalence where relevant?
5. Are database cases properly framed as absorbers, finite witnesses, or
   teaching fixtures rather than automatic novelty evidence?
6. Are physics cases properly framed as known-physics-induced typed witnesses?
7. Is the main note now too compressed for a reader to use without the
   appendices?
8. Is any appendix/report burden missing from the appendix map?
9. Does the residue ladder create enough pressure against premature novelty
   claims?
10. Are there any low-risk edits that would prevent predictable expert
    misunderstanding?

## Queue For Potential v0.5 Adjustments

These are not approved edits yet. They are items to test during fresh review.

### Q1. Verify quotient formalism one more time

Check that every factorization, spread, quotient, and equivalence-class
statement in v0.4 is internally consistent.

Potential patch if needed:

```text
Add one short sentence clarifying that whenever quotient notation is used,
the relevant equivalence relation is part of the declared audit context.
```

### Q2. Decide whether v0.4 needs one compact positive example

v0.4 is intentionally short and template-centered. Fresh reviewers should test
whether the absence of one canonical worked mini-example makes the note harder
to audit.

Potential patch if needed:

```text
Add one compact example that is explicitly demoted after absorber testing,
showing how the audit prevents overclaim.
```

Do not add a long examples section to the main note by default.

### Q3. Check whether the appendix map is navigable enough

The document strategy puts weight on appendices and companion reports.

Potential patch if needed:

```text
Add a small appendix map table that says which companion report carries which
burden: math strengthening, database absorption, prior art, physics strongman,
low-hanging patch synthesis, and fresh-eye review.
```

### Q4. Check whether domain calibration is too compressed

v0.4 compresses database, math, physics, and prior-art calibration.

Potential patch if needed:

```text
Add one paragraph saying that domain sections are calibration gates, not
evidence of novelty.
```

### Q5. Check whether the physics stance needs a miniature typed witness

The physics posture is correct in principle, but fresh reviewers should see
whether a tiny model-shaped example would reduce ambiguity.

Potential patch if needed:

```text
Add a brief physics witness template, not a new physics claim:
model family, observer, access profile, gauge-invariant observable algebra,
projection, induced Cap, equivalence, absorber check, residue status.
```

### Q6. Check whether database-specific equality fields are visible enough

Database absorption was a major correction. Fresh reviewers should verify that
v0.4 still makes database equality strict enough.

Potential patch if needed:

```text
Add database equality fields to the audit checklist: schema, constraints,
query/view language, transaction and isolation context, provenance,
index/materialization context, access policy, consistency model, approximation
tolerance, and workload.
```

### Q7. Check whether approximate capability equivalence is first-class enough

Vector, search, time-series, approximate query processing, and ML retrieval
systems often require approximate rather than exact capability equivalence.

Potential patch if needed:

```text
Add epsilon, probabilistic, top-k, recall@k, latency/recall envelope, and
workload equivalence as named options in the audit template.
```

### Q8. Check whether failure labels overlap too much

Fresh reviewers should verify that these labels are distinguishable in use:

```text
under_typed
same_visible_state_underspecified
projection_underdescribed
gerrymandered_capability
access_profile_underdeclared
local_capability_smuggling
physics_direction_reversal
typed_model_missing
```

Potential patch if needed:

```text
Add a compact distinction table only if reviewers find repeated ambiguity.
```

### Q9. Check whether canonical residue and formal residue are separated enough

Fresh reviewers should test whether a reader could mistake formal
non-factorization for canonical residue.

Potential patch if needed:

```text
Strengthen the sentence that formal residue is not enough unless canonicity,
absorber resistance, and same-neighbor-data testing also survive.
```

### Q10. Check whether v0.4 should explicitly say "default equality is not enough"

The note already warns against sloppy visible-state equality. It may still need
a sharper default rule.

Potential patch if needed:

```text
Add: The default equality relation is not "same payload" or "same current
value"; equality must be declared by the audit context.
```

### Q11. Check whether the prior-art posture is visible enough in the opening

The prior-art reports push humility strongly. Fresh reviewers should verify
that the opening of v0.4 cannot be read as claiming the non-factorization
pattern itself is new.

Potential patch if needed:

```text
Move the absorption warning earlier or make the first-page novelty limitation
more explicit.
```

### Q12. Check whether the main note needs a "what would falsify this?" line

The schema is supposed to be falsifiable.

Potential patch if needed:

```text
Add one sentence: A proposed witness fails if a mature absorber supplies a
natural sufficient enrichment or quotient under the declared audit context.
```

## Review Reports Filed Against This Queue

- [`Pre-v0.5 Review Report v0.1.md`](Pre-v0.5%20Review%20Report%20v0.1.md) — Claude Sonnet 4.6, 2026-06-20. Verdicts on Q1–Q12, two new items (N1, N2), five main-note patches recommended, three companion-report items confirmed, four items closed as no-patch.

- [`Pre-v0.5 Readiness Action Report v0.1.md`](Pre-v0.5%20Readiness%20Action%20Report%20v0.1.md) - Codex GPT-5, 2026-06-20. Consolidated action report on what must be done before v0.5: five compact main-note patches, companion-report/example work, navigation/posture checks, and source-hygiene cleanup.

## Instructions To Agents Using This File

When reviewing, do not draft v0.5.

Add proposed changes to this queue only if they are concrete. Each proposed
change should include:

- the issue;
- why it matters;
- the source file or argument that supports it;
- the smallest viable patch;
- whether the patch belongs in the main note or an appendix.

If a reviewed area is sound, say so plainly and do not manufacture a queue
item.

Preserve the current posture:

```text
shorter main document
appendices do heavy lifting
global absorption first
strong physics without free physics
typed Cap before examples
finite tests are useful but weak
canonical residue is hard
```

## Current Open Decision

The next draft should be made only after this queue has absorbed fresh reviews.

The expected v0.5 direction, if no major issue appears, is:

```text
retain v0.4's compact main-document structure;
patch only clarity/correctness gaps;
move expanded math, database, physics, and prior-art support into appendices or
companion notes.
```
