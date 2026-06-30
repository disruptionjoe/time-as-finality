---
artifact_type: exploration
status: active
governance_role: next_goal_spec
claim_refs:
  - D1
  - R1
  - S1
  - PO1
depends_on:
  - explorations/gu-source-action-salvage-and-taf-restart-2026-06-30.md
  - tests/T376-fixed-admissibility-absorber.md
  - results/fixed-admissibility-absorber-v0.1-results.md
  - ../temporal-issuance/explorations/E098-shared-record-rendering-63-persona-steelman-2026-06-30.md
  - ../temporal-issuance/explorations/E099-rendered-4d-interface-63-persona-triple-steelman-2026-06-30.md
created: 2026-06-30
---

# Relativistic Record Rendering Fixture Goal

## Purpose

Draft the next ambitious TaF goal after T376.

Temporal Issuance has converged on the compact formulation:

```text
Dimensions are columns.
Time is row append.
Time is not one of the columns.
```

This exact sentence appears in the local newest Temporal Issuance exploration
`E100-record-table-time-63-persona-steelman-2026-06-30.md`. That file was
uncommitted in `temporal-issuance` at drafting time, so the stable dependency
list above points to the committed rendered-interface setup files and this
packet records the E100 insight as live cross-repo context.

T376 adds the guardrail:

```text
Record coherence, row filtering, and append order are not source-side residue
if a fixed admissibility rule, fixed projector, fixed latent source, or fixed
schema reproduces the trace.
```

The next fixture should therefore test whether a record-table / rendered-interface
model can recover a genuinely relativistic invariant without adding a primitive
time column and without importing Minkowski spacetime first.

## Goal Statement

Build a relativistic record-rendering fixture:

```text
Define a minimal shared record carrier with no time column.
Define two observer render maps from that carrier.
Test whether both observers recover the same invariant interval/order structure
while disagreeing on coordinate simultaneity.
```

The fixture must answer:

```text
Can invariant interval/order structure be recovered from compatible record
append plus observer rendering, rather than assumed as 4D Minkowski geometry?
```

## Minimal Object

Proposed object:

```text
RelativisticRecordCarrier =
(
  Row,          appended records, with no global time field
  Compat,       admissible row relation
  SignalLinks,  record-to-record propagation / dependency links
  Chains,       observer-local record chains
  Interval,     carrier-native interval/order quantity
)
```

Observer renderings:

```text
Render_A : Carrier -> Hist_A
Render_B : Carrier -> Hist_B
```

Each rendered history may introduce coordinate labels, including a time-like
coordinate, but those labels must be outputs of the rendering, not columns in
the source rows.

## First Executable Shape

Use a finite 1+1-style carrier before any 3+1 or GU-facing ambition.

One plausible construction:

```text
carrier rows contain two propagation lineage ranks, u and v;
records are compatible when lineage ranks are monotone;
carrier interval between records is Delta_u * Delta_v;
observer A renders t_A = (u + v) / 2 and x_A = (u - v) / 2;
observer B renders with a different admissible scaling of u and v;
both recover the same Delta_u * Delta_v but disagree on simultaneity slices.
```

This construction must be stated carefully. The source object is not a
Minkowski manifold. It is a finite record-propagation carrier. The rendered
coordinates are derived labels.

## Required Comparators

The fixture must include hostile nulls:

| comparator | absorber risk | failure condition |
|---|---|---|
| Minkowski-first | invariant imported from 4D geometry | source rows already contain `t`, `x`, or metric data |
| fixed schema/log | ordinary database append | no metric/order invariant beyond fixed constraints |
| fixed completed table | block-universe absorber | all possible rows are precontained and append is only reveal/access |
| hidden preferred foliation | global clock smuggled in | one total order is required to reproduce both observers |
| generic causal order only | order without metric | causal comparability exists but interval-like quantity cannot be recovered |

## Success Criteria

The first version succeeds only if all are true:

```text
1. Source rows have no primitive time column.
2. Two observers render different coordinate simultaneity slices.
3. Both observers recover the same carrier-native interval/order invariant.
4. The invariant is computed from record compatibility / propagation structure,
   not from an imported Minkowski metric.
5. Fixed schema/log and hidden-foliation nulls fail to explain the full result.
6. T376-style fixed-admissibility absorption is explicitly reported.
```

## Failure Criteria

The result is demoted if any are true:

```text
1. A time coordinate is placed in the source rows.
2. The metric or invariant interval is assumed before rendering.
3. A hidden global total order is required.
4. Fixed compatibility or fixed completed-table access explains everything.
5. The fixture recovers only ordinary causal order, with no interval-like
   invariant.
6. The result is only database/log semantics.
```

## Work Products

Expected implementation round:

```text
models/relativistic_record_rendering.py
tests/test_relativistic_record_rendering.py
tests/T377-relativistic-record-rendering-fixture.md
results/relativistic-record-rendering-v0.1-results.md
```

Recommended result labels:

```text
rendered_interval_recovered
fixed_schema_absorbed
minkowski_import_failure
hidden_foliation_failure
causal_order_only
nonfixed_rendering_residue
```

## Claim Posture

No claim promotion is allowed from this goal alone.

Even a positive result is only:

```text
finite toy evidence that interval-like structure can be rendered from a
record-propagation carrier without a source time column.
```

It does not prove relativity, derive spacetime, validate GU, or establish
source-side Temporal Issuance.

## Why This Is Worth Doing

This is the first goal that directly joins three active threads:

```text
Temporal Issuance: time is row append, not a column.
Time as Finality: finality/order must beat fixed-admissibility absorption.
Relativity target: observers disagree on coordinates but agree on invariants.
```

If the fixture fails, it will fail informatively by showing whether the current
record-table idea collapses to one of:

```text
database append,
fixed compatibility,
ordinary causal order,
hidden foliation,
or Minkowski imported first.
```

If it passes, it gives the next real bridge target: move from finite 1+1
record-propagation rendering to a stronger carrier-renderer model with
matter-like persistent records and 3+1-compatible invariants.

## Plain-English Version

Do not put time in the table.

Append records to the table.

Let two observers render the growing table differently.

Then ask:

```text
Do they disagree the way relativistic observers should disagree,
while still recovering the same invariant structure?
```

If yes, the record-rendering idea has earned a real next test. If no, the
absorber won.
