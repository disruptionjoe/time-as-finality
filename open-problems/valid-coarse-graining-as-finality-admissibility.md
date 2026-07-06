# Valid Coarse-Graining as Finality Admissibility

Open-problem stub, opened 2026-06-30 from the Wolfram Observer Theory reading-set council pass
([explorations/wolfram-observer-theory-reading-set-2026-06-30.md](../explorations/wolfram-observer-theory-reading-set-2026-06-30.md)).
External provocation, not evidence. **Projection != finality** and guardrails **G1/G3** held.

## Problem

Wolfram's Observer Theory makes equivalencing/coarse-graining the fundamental observer operation, then leaves
*open* the question that actually carries the content: **which coarse-grainings are valid?** Wolfram notes
some equivalencings are "computationally ornate" (it would take enormous computation to even recognize two
states as equivalent), and that you can coarse-grain so finely you "become synonymous with the system." He
does not give a criterion for the admissible ones. TaF appears to already have that criterion: a coarse-grain
is admissible iff a **causally bounded observer can actually form and certify the corresponding finalized
record** under D1 (bounded accessible records, bounded reversal cost), passing the T10/T29 selection. Question:
**is TaF's finality-admissibility filter exactly the criterion for a valid coarse-graining that Observer Theory
leaves open?**

## Working Claim (to attack)

The valid coarse-grainings (Wolfram's open slot) are precisely the **bounded-observer-certifiable** ones, and
TaF's D1 + T10/T29 machinery is the criterion. A coarse-graining whose equivalence relation is not computable
within the observer's record/causal budget is *not* a finality the observer can hold; one fine enough to track
microstates is no coarse-graining at all. Finality lives in the admissible band between.

## Why It Might Help

- Converts a vague "we do equivalencing" into a falsifiable criterion: enumerate candidate coarse-grainings on
  a finite model, mark which are bounded-observer-certifiable under D1, and check that exactly those are the
  "valid" ones a bounded observer would use.
- Supplies a concrete distinguishing prediction vs Observer Theory: TaF predicts the *cost/certifiability
  boundary* of valid coarse-grainings; Observer Theory currently does not specify it.

## How It Could Mislead

- "Computationally ornate" (Wolfram) is a computation-cost notion; D1 reversal-cost is "formal only, not
  thermodynamic work by default." Mapping them risks importing a cost model TaF has not committed to. State
  the cost model explicitly before claiming the identification.
- An observer choosing a coarse-graining is not the same as a record finalizing; do not let "valid
  coarse-graining" smuggle in observer-creates-reality (G3). The filter is about what can be *certified*, not
  what is *made true*.

## Connection to Existing Claims and Tests

- [T10: Finality Superselection Rule](../tests/T10-finality-superselection-rule.md)
- [T29: Projection Obstruction Schema](../tests/T29-projection-obstruction-schema.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [unitarity-as-finality-precondition](unitarity-as-finality-precondition.md) (sibling external-provocation note)

## Contribution Needed

On a finite record-graph model, enumerate candidate equivalence relations (coarse-grainings), compute for each
whether it is bounded-observer-certifiable under D1, and test whether that set coincides with the
intuitively-valid coarse-grainings. A clean coincidence is the constructive version of the claim; a mismatch
bounds what TaF's filter actually characterizes. Keep cost-model assumptions explicit.

## T467 addendum: finite admissibility gate

T467 converts the contribution request into an executable finite gate:
`results/T467-valid-coarse-graining-admissibility-gate-v0.1-results.md`; spec
`tests/T467-valid-coarse-graining-admissibility-gate.md`; model
`models/valid_coarse_graining_admissibility_gate.py`.

Verdict:

```text
VALID_COARSE_GRAINING_ADMISSIBILITY_GATE_BUILT_NO_PROMOTION
```

In the finite fixture, the bounded-observer certification filter admits only
the two predeclared positive controls: a two-holder finality-status band and a
bounded local count. Microstate identity fails as too fine, all-state collapse
fails as too coarse, a hidden-field relation fails the access boundary, an
ornate lookup fails the computation budget, a posthoc exception relation fails
predeclaration, a projection-only shadow fails because projection is not
finality, a one-holder dashboard fails D1 redundancy, and an observer-creates-
truth overread is blocked.

This strengthens the open problem only as an admission gate. It does not prove
that TaF supplies the exact missing Observer Theory criterion, does not promote
D1/T10/T29, and does not earn a physics, consciousness, or public-posture move.
Future packets must declare the finite state universe, equivalence relation,
observer access boundary, recognition budget, D1-style certification fields,
nontrivial coarse-graining condition, certified-record object, and hostile
controls before any claim movement.

## T468 addendum: positive-control independence audit

T468 audits T467's fixture rather than strengthening the claim:
`results/T468-coarse-graining-positive-control-independence-v0.1-results.md`;
spec `tests/T468-coarse-graining-positive-control-independence.md`; model
`models/coarse_graining_positive_control_independence.py`.

Verdict:

```text
T467_POSITIVE_CONTROLS_COLLAPSE_TASK_GATE_LOAD_BEARING
```

The two T467 admitted positive controls are extensionally identical in the
binary two-holder fixture: finality band and local count induce the same
partition. They first separate at three binary holders, where finality band has
three classes and local count has four. T468 also shows that a cheap accessible
xor partition is rejected only when the finality-native-task requirement is
enforced; if that task flag is merely asserted, the mechanical budget gate would
admit it.

This weakens the constructive reading of T467. Future packets should use at
least three binary holders or a multi-valued fixture when claiming independent
positive controls, include a cheap accessible non-finality partition as a
hostile control, and supply a predeclared task-naturalness account rather than
only a boolean finality-task flag. No D1/T10/T29, Observer Theory, physics,
consciousness, claim-ledger, roadmap, or public-posture movement is earned.

## T469 addendum: task-naturalness gate

T469 converts T468's future-packet burden into an executable admission gate:
`results/T469-coarse-graining-task-naturalness-gate-v0.1-results.md`; spec
`tests/T469-coarse-graining-task-naturalness-gate.md`; model
`models/coarse_graining_task_naturalness_gate.py`.

Verdict:

```text
TASK_NATURALNESS_GATE_BUILT_FIXTURE_REPAIRED_NO_PROMOTION
```

The repaired three-holder packet clears review admission: three-holder
finality band and support count are independent positive controls, and cheap
accessible xor, label restatement, hidden-field dependence, and
observer-creates-truth overread are blocked. The inherited two-holder T467
packet remains individually well formed but fails packet admission because its
positive controls are not independent.

This repairs the fixture and hardens future intake; it does not prove that TaF
supplies Observer Theory's missing criterion. Future packets must include
independent positive controls when claiming constructive support, cheap
accessible non-finality hostile controls, a named certified record object, a
task account that preserves record value/support/finality status, and a
demotion condition for label restatement or observer-creates-truth overread.
No D1/T10/T29, Observer Theory, physics, consciousness, claim-ledger, roadmap,
or public-posture movement is earned.

## T471 addendum: multi-valued fixture gate

T471 stress-tests the T469 repair against a non-binary record alphabet:
`results/T471-coarse-graining-multivalued-fixture-gate-v0.1-results.md`; spec
`tests/T471-coarse-graining-multivalued-fixture-gate.md`; model
`models/coarse_graining_multivalued_fixture_gate.py`.

Verdict:

```text
MULTIVALUED_FIXTURE_GATE_BUILT_NO_PROMOTION
```

The T469 packet shape survives a ternary holder alphabet: finality band and
support count remain independent positive controls, while cheap modular sum,
label restatement, hidden-field dependence, microstate identity, and
observer-creates-truth overread are blocked. The binary three-holder packet is
retained as a reference control and also clears.

This hardens the fixture against a binary-only objection, but it still does
not prove that TaF supplies Observer Theory's missing criterion. Future packets
should stress constructive support across at least one non-binary alphabet,
keep cheap accessible arithmetic partitions as hostile controls, and block
label restatement and microstate identity before any claim movement. No
D1/T10/T29, Observer Theory, physics, consciousness, claim-ledger, roadmap, or
public-posture movement is earned.

## T477 addendum: budget-index gate

T477 stress-tests the T469/T471 repair across nested observer budgets:
`results/T477-coarse-graining-budget-index-gate-v0.1-results.md`; spec
`tests/T477-coarse-graining-budget-index-gate.md`; model
`models/coarse_graining_budget_index_gate.py`.

Verdict:

```text
BUDGET_INDEX_GATE_BUILT_OBSERVER_INDEXED_NO_PROMOTION
```

The repaired valid-coarse-graining packet is observer-budget indexed rather
than a fixed global whitelist. Three-holder finality-band and support-count
positives persist when the observer budget expands. A boundary-pair record
using holder 3 is rejected as inaccessible under the three-holder budget and
admitted only when holder 3 enters the declared access boundary. Cheap
arithmetic, label restatement, microstate identity, and observer-creates-truth
controls remain blocked under expanded access.

This supports the bounded-observer intake discipline only. Future packets must
declare the observer budget before relation selection, report budget
transitions for candidate relations, treat newly accessible record tasks as
observer-indexed admissions rather than global criteria, and keep cheap
arithmetic, label-restatement, microstate, and observer-creates-truth hostile
controls active before any claim movement. No D1/T10/T29, Observer Theory,
global valid-coarse-graining criterion, physics, consciousness, claim-ledger,
roadmap, or public-posture movement is earned.

## T478 addendum: budget-lattice gate

T478 expands T477 from a single nested-budget chain to a finite access-budget
lattice:
`results/T478-coarse-graining-budget-lattice-gate-v0.1-results.md`; spec
`tests/T478-coarse-graining-budget-lattice-gate.md`; model
`models/coarse_graining_budget_lattice_gate.py`.

Verdict:

```text
BUDGET_LATTICE_GATE_BUILT_PATH_INDEPENDENT_NO_PROMOTION
```

The repaired coarse-graining packet is coherent across the tested lattice.
Admitted finality-natural relations persist across budget-inclusion edges,
incomparable-budget joins preserve prior admissions, new join admissions are
explained by newly accessible certified record fields, and top-budget verdicts
are independent of the access-expansion path. Cheap arithmetic,
label-restatement, microstate identity, and observer-creates-truth controls
remain blocked whenever they become accessible.

This hardens the bounded-observer intake discipline from chain-indexed to
lattice-indexed review, but it is still only a finite guardrail. Future packets
must declare the observer-budget poset, report edge monotonicity and join/path
checks, explain every new admission by certified record access, and treat
budget-indexed admissions as local review targets rather than a global valid
coarse-graining criterion. No D1/T10/T29 promotion, Observer Theory equivalence
theorem, global valid-coarse-graining criterion, physics, consciousness,
claim-ledger, roadmap, README, public-posture, hard-policy, protected-license,
or cross-repo truth movement is earned.
