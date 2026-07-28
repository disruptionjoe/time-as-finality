# The H3/R1/T3 Seam: Update Layer and Commit Layer Are Different Structures

**Status:** seam resolved: **ORTHOGONAL** via layer separation; Goal 3 restated —
definitional register, negative-result discipline: no claim movement on
[H3](../HYPOTHESES.md), [R1](../claims/R1-relativity-no-global-commit-order.md),
or [T3](../tests/T3-spacelike-events-no-global-commit-order.md), no
preferred-frame standing established, no charter amendment
**Date:** 2026-07-27
**Resolves:** the seam flagged first in the Lane 1 swing-series proposal
(`repos/private/system-runtime/mailboxes/time-as-finality/20260727-proposed-five-swing-series-lane-1.md`,
Swing 1), including its pre-registered kill condition
**Seam texts:** [HYPOTHESES.md H3](../HYPOTHESES.md),
[R1](../claims/R1-relativity-no-global-commit-order.md) ("What This Does Not
Claim"), [T3](../tests/T3-spacelike-events-no-global-commit-order.md) (success
criteria); charter contact point:
[CHARTER.md](../CHARTER.md) Goal 3
**Builds on (native results, cited by pointer):**
[T588](../tests/T588-record-issuance-contract-fork-gate.md) /
[results](../results/T588-record-issuance-contract-fork-gate-v0.1-results.md);
[T586](../tests/T586-record-capability-order-gate.md) /
[results](../results/T586-record-capability-order-gate-v0.1-results.md);
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md) /
[results](../results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md).
Cross-repo pointer (their truth, not imported as ours): dynamic-unity guard
`NI-DU-87`, `dynamic-unity/COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`, banked
2026-07-27

---

## Verdict

Among the swing's three pre-registered options — the preferred-frame family
*contradicts* R1, is *ruled out by* T3's success criteria, or is *orthogonal*
to both — the answer is **ORTHOGONAL**, and the reason is a layer separation
that the seam texts already respect without naming:

- A **tick** is an **update structure**: when substrate state advances.
- A **commit order** is a **finality structure**: when facts become
  irrevocable and shared.

These are different layers. H3, R1, and T3 live entirely on the commit layer.
The Lane 1 preferred-frame family lives on the update layer. **Update-layer
claims and commit-layer claims can neither entail nor exclude one another
without an additional bridging assumption** — and no seam text asserts a
bridge.

The consequence the swing spec pre-registered for exactly this outcome fires:
Goal 3's comparison, as originally framed (preferred-frame account *versus*
causal-partial-order account, as rivals over the same phenomena), has no
direct contact point. It is restated below as: **what does an update-layer
posit ADD to a commit-layer account that is already complete on its own
terms?** That restatement is the rebuild the kill condition called for; it
needs no charter text change, because Goal 3's own measure — "state exactly
what the preferred-frame model changes, and what it leaves unchanged" — is
precisely the restated question.

## The layer separation

A globally ticking substrate is compatible with purely regional finality,
because commitment requires records to **meet**, and meeting is causally
bounded. However the substrate advances — one global sweep, a foliation's
leaves, or no global structure at all — a fact becomes irrevocable *and
shared* only where records can reach a common causal future and be reconciled
there. So:

- Positing a global update structure does not create any global commit order:
  nothing about how state advances makes remote records meet faster than
  causal access permits.
- Refuting a global commit structure does not refute any global update
  structure: killing a globally readable ledger says nothing about how the
  substrate advances underneath.

In the repository's own construction-fork discipline, "global order" is a
fork: an update-layer construction and a commit-layer construction share the
name. The seam existed because the seam texts and the new Lane 1 charter used
the same name for different constructions. Naming the construction each text
uses dissolves the seam; neither side defaults silently.

## Reading the seam texts under the separation

**H3** says spacelike-separated events "do not require a single
observer-independent commit ordering until records meet in a common causal
future." The operative word is *require*, and the object is a *commit*
ordering. H3 is a commit-layer claim, silent about update structure.

**R1's disclaimer is a scope statement, not an exclusion.** "It does not
introduce a hidden universal present" says R1's account *needs* no such
structure — not that none may exist. The disclaimer polices R1's own
construction (no smuggled global structure inside the commit-layer account);
it does not quantify over the universe of models. Contradiction would require
R1 to assert the *absence* of any global update structure. It asserts
compatibility of relativity with the absence of global *finality* order — a
different layer.

**T3's success criterion "no hidden universal present is introduced" remains
satisfied by every commit-layer construction**, exactly as before. The
criterion is a condition on the model T3 grades, not on the research program.
An update-layer posit researched under the Lane 1 charter does not violate T3
because it introduces nothing *into* those constructions: T3's models remain
as they are, criterion intact. A Lane 1 candidate is a different model, graded
by its own burdens under Goal 2, not by T3's.

## The separation runs both directions — native witnesses, by pointer

**Update does not come from commit (T588).** The single-global-ledger contract
(contract B) — one monotone issuance count *read by all observers* — is a
commit-layer object, and it is refuted by the empirical existence of
differential ageing, invariantly across probed proper-time ratios. The
update-layer tick is untouched by that refutation; what died is precisely the
attempt to have a globally *readable* count, i.e. global commit structure.
T588's Lane 1 note — contract B, had it survived, would have *derived* a
global tick from the ledger count — is, under this separation, the closure of
the cheapest bridging attempt: you do not get the update layer from commit
structure for free. That is the layer separation doing work.

**Commit does not fix update (T586/T587).** The frozen T586 fixture's record
order is a strict subrelation of its supplied causal order (T587:
`RECORD_SUBRELATION`, absorbed as a typed prerequisite filter). Even the
*full* causal closure of that fixture admits **exactly three** total
orderings of its five events — a three-fold degeneracy of admissible global
orderings — and the weaker record order admits five. Checkable from the
published artifact alone: enumerate the 120 permutations of the five events in
`results/T586-record-capability-order-gate-v0.1.json`; 3 respect the causal
closure (from `causal_parents`), 5 respect `order_report.closure`. Record
structure therefore under-constrains any foliation: nothing on the commit
layer selects among the compatible global orderings. The update layer is not
fixed by the commit layer either.

Neither direction entails or excludes. That is the content of ORTHOGONAL.

## What an update-layer posit would add — with the qualifier that matters

The restated Goal 3 question has a definite first answer, and it comes with a
load-bearing qualifier:

- **A foliation alone adds nothing.** Slicing a commit-layer account that is
  already complete on its own terms changes no record, no reconciliation, no
  observable, and — per the three-fold degeneracy above — is not even selected
  by the structure it slices.
- **What would add something is the foliation PLUS definite configurations
  per leaf** (Bohm-type beables): that package, not the slicing, is what
  purchases a single consistent history and the evasion of the
  Wigner's-friend-class no-go results.

Dynamic-unity banked the complementary guard the same day (`NI-DU-87`): a
preferred foliation by itself does not evade Bell or Wigner-friend no-gos; the
logical escape belongs to the complete model, and the rejected premise must be
stated rather than crediting the foliation alone. Cited by pointer per Goal
3's routing measure; their register, their truth.

## Effect on the swing series

- **Goal 3, restated:** not "which account explains records, finality, and
  observer access better," but "what does an update-layer posit add to a
  commit-layer account that is already complete on its own terms — and what
  does it leave unchanged?" First answer above: nothing, unless the posit
  carries beables; then say so and pay Goal 2's burdens for the package.
- **The ledger-fork gate's landed result already conforms.** T588 (reopened under T587's third condition; not one of the numbered swings) is of the restated form:
  it graded issuance contracts on their own commit-layer terms, refuted the
  one contract that would have *derived* a global tick from commit structure,
  and left the update layer untouched. No regrading is needed.
- **Downstream swings unblock.** Family classification and constraint work
  (swings 3 and 5) proceed under the restated question; any future foliation
  run through the capability machinery is graded on what the foliation
  *changes* in the fixture, with the pre-registered expectation from
  `NI-DU-87` and the degeneracy result that slicing alone changes nothing.

## What This Does Not Claim

- **No claim movement.** H3, R1, and T3 keep their texts, statuses, and
  success criteria unchanged; this note edits none of them, and T3's
  criterion remains satisfied by every commit-layer construction in the
  repository.
- **No preferred-frame standing.** Orthogonality is not evidence for the
  family. No empirical, explanatory, or interpretive credit is banked for any
  update-layer posit here; the family still owes Goal 2 its burdens.
- **No charter amendment.** The restatement is a reading of Goal 3's
  comparison strategy under the layer separation, recorded for the swing
  series; the charter text is untouched, and Goal 3's own
  changes/leaves-unchanged measure already demands the restated question.
- **Definitional work, not physics.** The layer separation introduces no
  observable, mechanism, model, or bridging assumption; it asserts no bridging
  assumption true or false. It is vocabulary discipline of the
  construction-fork kind.
- **The degeneracy counts are fixture-local.** Three-fold (causal) and
  five-fold (record) degeneracy are properties of one frozen finite fixture,
  not of relativity, and support no continuum or physical-spacetime claim.
- **`NI-DU-87` is dynamic-unity's result.** It is cited as a pointer under
  Goal 3's routing measure, not imported as this repository's truth.
