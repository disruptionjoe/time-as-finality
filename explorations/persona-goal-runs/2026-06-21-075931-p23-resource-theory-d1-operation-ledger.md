# P23 Run - Resource Theory Researcher

- timestamp: 2026-06-21T07:59:31-05:00
- goal_id: P23
- selected_persona: Resource Theory Researcher
- selected_goal: Define allowed operations for D1 coordinates and prove which coordinates are monotone, nonmonotone, incomparable, or resource-convertible.
- bounded_question: Within the existing D1 fixtures, what is the smallest honest allowed-operation vocabulary under which the coordinates behave like resource data rather than loose observer bookkeeping?

## Repo Context Read

- `explorations/persona-future-run-goals-2026-06-20.md`
- `claims/D1-physical-finality-definition.md`
- `claims/Q1A-access-boundary-record-accounting.md`
- `tests/T22-d1-physical-reduction-map.md`
- `tests/T26-d1-restriction-system.md`
- `tests/T111-d1-gauge-invariance-audit.md`
- `models/t111_d1_gauge_invariance_audit.py`
- `models/reversible_finality_nonmonotonicity.py`
- `models/t1_record_graph_admissibility_ledger.py`
- `models/q1a_current_family_closure.py`

## Work Performed

1. Read the current D1 claim posture to keep the run inside already earned
   boundaries:
   - accessible support and holder redundancy have limited executable traction;
   - branch support and reversal cost remain weaker and domain-dependent.
2. Collected the existing finite operation families that already act on D1-like
   profiles:
   - pure relabeling/isomorphism maps from T111;
   - access-boundary refinement/coarsening from T111;
   - record-copy / branch-spread / access-control moves from T141;
   - reversible local dynamics from T80;
   - current Q1A closure behavior from T147.
3. Asked a narrower resource-theory question than the original persona brief:

```text
Does the repo already earn one D1 resource preorder,
or only an operation-class ledger?
```

## Result

### Main Finding

The repo does not yet earn a single resource theory for D1.

It does earn a conservative operation-class audit:

- some maps are pure transport and preserve all four coordinates exactly;
- some maps change coordinates only because the observer boundary changed;
- some maps increase coordinates by spending explicit holder/erasure resources;
- raw reversible physical time evolution can decrease coordinates again.

So the correct object today is not:

```text
one global D1 resource preorder
```

but:

```text
an operation-class ledger for D1 coordinates
```

### Smallest Honest Allowed-Operation Vocabulary

The smallest useful split is:

```text
G = pure gauge / transport maps
B = boundary-change maps
C = budgeted copy / branch-spread / erase maps
R = ordinary reversible local time evolution
```

#### G: pure gauge / transport maps

T111 gives the cleanest result. In the reference fixture:

```text
D1 = (4, 2, 2, 2)
```

and the following preserve all four coordinates exactly:

- observer relabeling;
- record-label permutation preserving incidence;
- holder relabeling preserving independence partitions;
- causal-graph isomorphism preserving reachability.

These are not resource-generating operations. They show that D1 coordinates can
be transported as boundary-indexed data.

#### B: boundary-change maps

T111 also shows that access-boundary changes are covariant, not gauge:

```text
(4, 2, 2, 2) -> (2, 2, 2, 0)   access-boundary refinement
(4, 2, 2, 2) -> (5, 3, 3, 3)   access-boundary coarsening
```

This means all four coordinates are monotone with respect to boundary
inclusion in that finite fixture, but this is not yet a resource monotone in a
strong sense because T141 shows the reverse move can be an ordinary admissible
policy/access change:

```text
(1, 1, 1, 0) -> (2, 2, 1, 1)   grant access to an existing record holder
(2, 2, 1, 1) -> (1, 1, 1, 0)   revoke that access
```

So under `B`, D1 is observer-boundary bookkeeping, not irreversibility.

#### C: budgeted copy / branch-spread / erase maps

T141 is the strongest current resource-style fixture. Two cases matter:

```text
copy_to_fresh_holder:
(2, 2, 1, 0) -> (3, 3, 1, 1)

branch_spread_copy:
(2, 2, 1, 1) -> (3, 3, 2, 2)
```

These increases require named additional substrate structure:

- fresh holder capacity and erasure work;
- fresh branch-support holder and erasure work.

The reverse is not constructor-impossible. It is resource-accounted erasure or
overwrite. So the earned statement is:

- accessible support is resource-convertible under copy/erase;
- holder redundancy is resource-convertible under fresh independent holders;
- branch support is resource-convertible under explicit incomparable-branch
  copying;
- reversal proxy can rise with these same moves, but only as a named undo-cost
  surrogate, not as thermodynamic work by default.

#### R: ordinary reversible local time evolution

T80 blocks the tempting overreach. In the canonical reversible witness:

```text
(2, 2, 1, 2) -> (1, 1, 1, 1)
```

with decreases in:

- accessible support;
- spatial/holder redundancy analogue;
- terminal intervention cost / reversal proxy.

So D1 coordinates are not monotones of ordinary physical time evolution, even
inside a clean reversible finite substrate.

### Coordinate Classification

| Coordinate | Under `G` | Under `B` | Under `C` | Under `R` | Current status |
| --- | --- | --- | --- | --- | --- |
| accessible support | invariant | monotone with boundary inclusion, reversible under access revocation | resource-convertible by copy/erase or access grant/revoke | nonmonotone | best current candidate coordinate, but observer-boundary indexed |
| holder redundancy | invariant | monotone with boundary inclusion when new independent holders become visible | resource-convertible if fresh independent holders exist | nonmonotone in the T80 analogue | conditionally physical after access/partition audit |
| branch support | invariant/covariant as transported coordinate | can rise or fall with boundary and branch visibility | resource-convertible in the T141 branch-spread fixture | not earned as time monotone | still formal-only in strong physical claims |
| reversal cost / graph reversal count proxy | invariant/covariant as bookkeeping coordinate | changes with visible support thresholding | rises under budgeted copy/branch-spread, falls under erase/access loss | nonmonotone | weakest coordinate; not thermodynamic work and not a stable standalone resource yet |

### Monotone, Nonmonotone, Incomparable, Resource-Convertible

#### Monotone

What survives honestly:

- all four coordinates are invariant under `G`;
- all four are weakly monotone under boundary inclusion inside the audited T111
  fixture;
- accessible support and holder redundancy are weakly monotone under the
  budgeted copy-style `C` moves tested so far.

#### Nonmonotone

What is already disproved:

- D1 coordinates are not monotones under unrestricted reversible physical time
  evolution;
- boundary-relative D1 values are not monotones once both access grant and
  access revocation are allowed symmetrically.

#### Incomparable

The current repo has not yet earned a single shared preorder on the four
coordinates across `G + B + C + R`.

The operative incomparability is between operation classes, not just between
coordinate values:

- `G` is transport, not resource conversion;
- `B` is observer-boundary change;
- `C` is budgeted resource conversion;
- `R` can undo apparent gains.

So the right statement is not "D1 has one resource order." It is:

```text
different allowed-operation classes induce different partial orderings
or no useful ordering at all
```

#### Resource-Convertible

The strongest earned resource-theoretic content is local:

- some D1 improvements are convertible from explicit budgets such as fresh
  holders, branch-support carriers, and erasure work;
- none of the tested improvements are one-way in a constructor-theoretic sense;
- current resource conversion is therefore accounting-laden, not impossibility-
  grounded.

### Q1A Boundary

The quantum fixed-data family sharply limits what can be claimed.

T147 shows that the current family factors through:

```text
partition visibility + audited accessible provenance-support count
```

and that inside that family:

- branch support is not load-bearing;
- reversal-cost proxy is not load-bearing.

So branch support and reversal cost are not presently independent D1 resources
in the strongest current quantum witness family, even if they remain useful
formal coordinates elsewhere.

### Smallest Useful Formal Object

The smallest useful next object is an operation ledger, not a theorem-sized
resource theory:

```text
D1OperationLedger = (
  operation_class,
  admissibility_conditions,
  preserved_coordinates,
  weakly_monotone_coordinates,
  reversible_coordinates,
  required_budget_or_boundary_data,
  nonmonotone_counterexample_if_any
)
```

This would let future runs distinguish:

- transport invariants;
- observer-boundary covariants;
- budgeted resource conversions;
- genuinely blocked or impossible reversals.

## Blocker

The repo still lacks a physically calibrated operation class under which all
four D1 coordinates are simultaneously meaningful and nontrivially monotone.

Two specific blockers dominate:

- branch support and reversal cost are still partly formal or proxy-level;
- current strong examples show reversibility or resource-accounted reversal,
  not constructor-impossible one-way conversion.

## Proposed Next Action

If Joe wants a follow-on run, the next bounded step should be:

1. define `D1OperationLedger` explicitly on one substrate family;
2. start with the T1/T111/T141 finite record systems rather than quantum;
3. require every allowed operation to declare whether it is transport,
   boundary-change, or budgeted conversion;
4. only then ask whether any nontrivial monotone theorem survives.

That would turn the current classification into a reusable audit object without
pretending the full D1 resource theory already exists.

## Claim-Status Posture

- No claim-status changes recommended.
- No roadmap, test-status, or automation changes recommended.
- Positive narrow statement: D1 already supports an operation-class audit with
  transport invariants, boundary covariants, and budgeted conversion examples.
- Negative narrow statement: the repo has not yet earned a single D1
  resource-theoretic preorder, and should not present D1 coordinates as global
  monotones of physical time.
