# P12 Bounded Run - Network Propagation Three-Layer Model

- Run timestamp: 2026-06-20T20:49:25-05:00
- Persona: P12 - Network Propagation Researcher
- Goal id: P12
- Queue goal: Build a three-layer finite model separating signal propagation, record formation, and later reconciliation, then classify prior tests by which layer they actually measure.
- Bounded scope: repo-only synthesis across the existing finite access, formation, and reconciliation labs. No claim-status, roadmap, workflow, automation, or executable-model edits.

## Repo Context Read

- `claims/D1-physical-finality-definition.md`
- `claims/A1-distributed-systems-finality-analogy.md`
- `tests/T1-record-graph-temporal-reconstruction.md`
- `tests/T2-quantum-measurement-record-finality.md`
- `tests/T42-local-persistence-reconciliation-split.md`
- `tests/T43-local-persistence-mechanisms.md`
- `tests/T46-open-causal-scarcity-synchronization-boundary.md`
- `tests/T55-conflict-finalievent-descent.md`
- `tests/T61-mmo-reconciliation-finality.md`
- `models/local_persistence_reconciliation.py`
- `models/mmo_reconciliation_finality.py`
- `tests/test_local_persistence_reconciliation.py`
- `tests/test_local_persistence_mechanisms.py`
- `tests/test_record_access_systems.py`
- `tests/test_mmo_reconciliation_finality.py`
- `explorations/T61-mmo-reconciliation-synthesis.md`

## Work Performed

1. Read the nearest existing layer-separation tests to determine which ones are actually about transport delay, which ones are about stable local record creation, and which ones are about later authority or repair.
2. Extracted the smallest finite three-layer object that fits the existing witnesses without introducing new primitives or changing repo formalisms.
3. Classified a bounded set of prior tests by primary measured layer, secondary layer, and the main confusion each test prevents.

## Result

### Minimal three-layer finite object

The cleanest bounded object is:

```text
PropagationFormationReconciliationSystem = (
  sites,
  propagation channels,
  local formation rules,
  reconciliation rules,
  world events,
  formed records,
  reconciliation records
)
```

with three non-collapsible layers:

1. `L1: signal propagation`
   - object: arrivals of signals or records across finite channels;
   - observables: first-access order, path delay, external arrival order, visibility lag;
   - does not decide whether a stable record has been formed or whether any record is authoritative.

2. `L2: record formation`
   - object: a site-local transition from incoming signal or local interaction into a stable record token;
   - observables: stable pointer record, local accumulator update, predicted local record, holder creation;
   - does not by itself settle cross-site agreement or authority.

3. `L3: later reconciliation`
   - object: comparison, commit, rollback, compensation, or conflict completion over already formed records;
   - observables: authoritative commit, demotion, rollback record, compensation record, conflict classification;
   - does not change the fact that earlier propagation and local formation already occurred.

### Concrete finite witness assembled from existing labs

One bounded witness can be read directly out of `T46 + T61`:

```text
world event
  -> propagated signal reaches client_a first and client_b later        (L1)
  -> client_a and client_b each form local predicted claim records      (L2)
  -> authority later emits commit_a, rollback_b, compensate_b           (L3)
```

The key discipline is:

- `pred_claim_a` and `pred_claim_b` are not propagation events; they are formed local records.
- `commit_claim_a` and `rollback_claim_b` are not the original record formation; they are reconciliation records over already formed local claims.
- path delay explains who sees what when, but it does not itself explain why a prediction becomes authoritative.

### Negative controls implied by the model

To keep the layers separate, each layer needs a control the others cannot fake:

- vary only `L1`: change channel delay while holding local formation traces and reconciliation policy fixed; only visibility/reconciliation lag should move.
- vary only `L2`: change local formation mechanism or threshold while holding channels fixed; formed record counts or local accumulators should move without forcing extra lag.
- vary only `L3`: keep the same propagated and formed records but change the later authority or conflict outcome; commit/rollback status should move without rewriting the earlier arrivals.

This is exactly the guardrail the repo has been approaching piecemeal, but not yet naming as one three-layer object.

## Prior-Test Classification

| Test | Primary layer actually measured | Secondary layer | What it does **not** measure |
| --- | --- | --- | --- |
| `T42` local persistence / reconciliation split | `L1` propagation and visibility lag | weak `L2` surrogate via local accumulation traces | stable record formation mechanism and authority reconciliation |
| `T43` local persistence mechanisms | `L2` local formation surrogate | checked against fixed `L1` control | authority, commit, rollback, or conflict repair |
| `T46` open scarcity / closed synchronization boundary | `L1` access frontier and boundary-delayed visibility | precondition for `L3` authority boundaries | record formation dynamics |
| `T1` record-graph temporal reconstruction | `L2` record existence and stabilization profile | observer access boundary | explicit later reconciliation policy |
| `T2` quantum measurement finality | `L2` pointer-record formation and redundancy | observer access restriction | reconciliation, rollback, or conflict repair |
| `T55` conflict-enriched FinaliEvent descent | `L3` conflict completion over formed events | depends on prior event/record structure | transport delay as a measured object |
| `T61` MMO reconciliation finality | `L3` authoritative reconciliation, rollback, compensation | `L1` delay and `L2` local predicted record formation as prerequisites | physical record-generation dynamics |
| `T17` consensus finality crosswalk | mostly `L3` protocol-side finalization summaries | projects onto D1 bookkeeping | physical signal propagation or substrate-level record formation |

### Short reading of the table

- The repo already has strong `L1` and `L3` witnesses.
- The repo has several `L2` witnesses, but they are spread across different domains: record graph, decoherence toy model, and local accumulation surrogates.
- What is still missing is one executable sidecar that contains all three layers in one file with explicit controls showing which outputs belong to which layer.

## Main Finding

The phrase "access" is currently carrying at least three different loads:

1. path-limited arrival of information (`L1`);
2. existence of a stable local record once information arrives (`L2`);
3. later authority/reconciliation status of that record (`L3`).

The prior tests do not all measure the same thing. In the bounded sample above:

- `T42` and `T46` are mainly access-frontier / propagation tests;
- `T1`, `T2`, and `T43` are mainly record-formation or formation-surrogate tests;
- `T55`, `T61`, and part of `T17` are mainly reconciliation/finality-status tests.

So the useful correction is not a new claim. It is a routing rule:

```text
do not infer reconciliation from propagation
do not infer record formation from mere arrival
do not infer authority from stable local records
```

## Blocker

No current executable model in the repo jointly implements `L1`, `L2`, and
`L3` as one named finite object with ablation controls. The layers exist, but
they are distributed across `T42/T43/T46/T1/T2/T55/T61` rather than unified in
one harness.

## Proposed Next Action

Take one of these bounded follow-ups:

1. Build a small `models/propagation_formation_reconciliation.py` harness by reusing `RecordAccessSystem` arrivals from `T46` and the commit/rollback structure from `T61`, with one explicit local formation rule in the middle.
2. Add a one-page routing note near `D1` defining `L1/L2/L3` and assigning nearby tests to them, without changing claim status.
3. Use the three-layer object as a review gate: any future argument using "observer access" must state whether it means arrival, formation, or reconciliation.

## Claim-Status Posture

- No claim promotion is warranted from this run.
- The result is a bounded bookkeeping improvement over existing tests, not a new theorem.
- `A1` and `D1` both get a cleaner interpretation if propagation, formation, and reconciliation are treated as separate audited layers rather than one scalar access variable.
