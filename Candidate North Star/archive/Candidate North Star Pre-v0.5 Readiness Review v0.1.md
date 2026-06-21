# Candidate North Star Pre-v0.5 Readiness Review v0.1

## Status

Reviewer:

```text
Claude (Cowork)
```

Reviewed baseline:

```text
Candidate North Star v0.4.md
```

This is not canon. It is not a v0.5 draft. It is a review report feeding the
`Candidate North Star Next Version Update Queue v0.5.md`.

Sources read for this review: v0.4; the v0.5 queue; `Output Report v0.4`;
`Fresh-Eyes Review v0.4` (Descartes); `Prior-Art Audit ...-deep-research-report`;
`Database Absorption Test ...-deep-research-report`; `Mathematical Strengthening
Suggestions v0.1`; `Strongman for physics sections`; `Joe notes`.

## Headline

v0.4 is in good shape. The hard structural critique from earlier versions has
been absorbed: absorption-first posture, Blackwell/Le Cam, the
linear-time/branching-time spectrum and testing/bisimulation, abstract
interpretation, the trivial enrichment theorem, the fiber-constancy lemma, and a
no-free-physics rule are all present. The compression is a success and should not
be undone.

The gap is no longer the schema. The gap is that nothing has been run through it.
v0.4 is a well-specified audit instrument with zero completed audits. Every
companion report converges on the same point: the surviving value of this program
is (a) at least one non-self-inflicted witness that survives absorption, and/or
(b) a cross-domain transfer theorem. v0.4 lists both as success criteria and
contains neither. That, not more schema polish, is what gates a credible v0.5.

## What is already done (do not redo)

- Prior-art audit is complete. Verdict: the bare claim is a translation surface
  over settled theories; the single most damaging omission (van Glabbeek) is now
  cited in v0.4. Do not commission another general prior-art sweep.
- Database deep research is complete. Verdict: mostly absorbed once "state"
  includes DB metadata; the cleanest surviving residue is approximate /
  workload-bounded / consistency-sensitive / vector-ANN retrieval.
- Main-note re-expansion is rejected by fresh review and should stay rejected.
- "Find another same-pi / different-Cap pair" is explicitly not success. Do not
  add more of these.

So two of Joe's three "next version" notes (database deep research; missing items
from Claude) are discharged. The third (physics strongman) is written but not yet
executed against v0.4 — see Gate 2.

## Gating items (must resolve before a v0.5 draft is worth making)

### Gate 1. Produce one fully worked witness, end to end

Pick the strongest surviving-residue case and run it all the way through the v0.4
instrument: type `K`, declare `~=_X` and `~=_K`, build the fiber, test
fiber-constancy, identify the minimal capability-preserving quotient, apply the
trivial-enrichment control, then run both state-enrichment and native-theory
absorption, and land it honestly on the residue ladder.

Recommended candidate: approximate nearest-neighbor / vector retrieval (the
database report's clearest residue) or quantum resource theory under an explicit
access profile (the prior-art and strongman reports' strongest physics-adjacent
anchor). One worked example beats ten more schema clauses.

Why it gates: until a witness has actually been pushed through the protocol, "the
value is a disciplined audit surface" is an unproven promise. The first real audit
will also tell you whether the protocol is usable as written or whether the
checklist needs to change — feedback you cannot get from inspection.

### Gate 2. Make the physics decision explicitly

`Strongman for physics sections` was written against v0.2 and asks for each
physics domain to be fully instantiated (`Y, X, pi, Cap, K, equivalence,
non-factorization question, absorber, falsifier`). v0.4 added the no-free-physics
template and a physics witness posture, but it instantiates none of them. The
strongman critique has therefore not actually been applied. This is currently in
limbo, and it should be decided rather than drifted:

- Option A: execute one or two typed physics witnesses for v0.5 — quantum
  resource theory is the strongest and the least likely to collapse into "you
  threw away the obvious state." Treat GR causal accessibility as the second.
- Option B: formally scope physics to appendix-level calibration for v0.5 and
  defer typed witnesses, with a one-line note saying so, so the absence reads as a
  decision rather than an oversight.

Either is defensible. Leaving it unstated is not, because the strongman doc sets
an expectation the main note silently does not meet.

## Mergeable patches (low-risk, already supported by the reports)

These can go straight into v0.5; each is backed by a source.

- Fold the database same-visible-state fields into the reviewer checklist
  (queue Q6). The database report's audit template gives the exact list: schema,
  constraints, view/query language, transaction/isolation, provenance,
  index/materialization, access policy, consistency model, approximation
  tolerance, workload, budget. This is a correctness gate, not polish.
- Make approximate equivalence first-class in the audit template (queue Q7):
  epsilon, probabilistic, top-k, recall@k, latency/recall envelope, workload
  equivalence. The database report shows this is precisely where residue
  survives, so it is load-bearing, not cosmetic.
- Add the single compact worked-and-demoted example to the main note (queue Q2) —
  but only after Gate 1, so the example is a real audit rather than a toy.
- Minor: compress the status/caveat block slightly (Descartes finding 4); it is
  accurate but over-defensive.

## Open theory gaps (name them in v0.5; do not pretend they are solved)

### The canonicity / interestingness criterion is still missing

The prior-art audit names this as the core unresolved problem: pre-registering
`Cap` does not prevent gerrymandering, because one can always pre-commit to a
`Cap` that reads the latent state. v0.4 answers this only with adjectives —
"domain-natural, minimal, canonical" — and no operational test. Neighboring
fields already have the canonicity bars: minimal sufficient statistic, coarsest
adequate congruence, fully abstract semantics, Nerode congruence, minimal
predictive state. v0.5 should either adopt one of these as the explicit canonicity
test or log "canonicity criterion for when a witness is interesting" as open
problem number one. This is the difference between formal residue and canonical
residue, which the whole ladder hinges on.

### The transfer theorem is the real prize and has not been attempted

A reusable audit pattern proven across two mature fields is the highest-value,
most publishable target in the success criteria, and nothing in the corpus even
sketches it. Recommend a short scoping note that picks two fields (e.g., Blackwell
sufficiency and resource convertibility, or testing equivalence and POMDP
belief-state sufficiency) and attempts one transfer statement. If it does not go
through, that is itself a useful finding for the residue ledger.

### No executable witness suite exists yet

Success criteria call for "a finite executable suite with preservation controls
and non-factorization fixtures." The repo already has a `tests/` + `results/`
culture (T-numbered). Wiring even two fixtures (one preservation control, one
non-factorization witness) into that harness would convert the schema from prose
into something runnable and falsifiable, and would naturally house the Gate 1
witness.

## Minor / housekeeping

- Terminology consistency pass. v0.4 standardized on `capability-insufficient`,
  but companion docs still carry `capability-nondetermining` and the deprecated
  `capability-nonfaithful`. Align companions to the v0.4 term.
- The `~=_X` carry-through cleanup from the Descartes review is in the v0.4 body;
  confirm it is reflected anywhere the formalism is restated in companions.

## Recommended sequence

1. Gate 1: one worked witness through the full protocol (ANN retrieval or quantum
   resource theory).
2. Gate 2: decide physics — execute one typed physics witness, or scope physics
   to appendix and say so.
3. Merge the Q6 / Q7 checklist patches; add the Q2 worked example built from the
   Gate 1 witness.
4. Add an "open problems" block naming the canonicity criterion and the
   transfer-theorem target.
5. Only then draft v0.5, holding the v0.4 structure and length.

## One-line verdict

The instrument is built and well disciplined; v0.5 should not refine the
instrument further until it has been used at least once. Build a witness, decide
the physics, name the two open problems honestly — then draft.
