# Technical Report: MMO Reconciliation Finality

**T61 - v0.1**

## Summary

T61 tests whether Time as Finality can distinguish apparent local finality from
authoritative event finality in a minimal finite distributed simulation with
bounded observers, propagation delay, client prediction, rollback, and conflict
repair.

The domain is deliberately engineered and hostile. This is not a metaphor for
physics and not a claim that reality is server-authoritative. MMO networking is
used because prediction, commit, stale views, rollback, compensation, and
conflict have operational meanings.

Result: the distinction is executable using existing repo machinery.

Best classification:

```text
Strengthens A1 as a formal engineered-domain analogy/homology candidate.
Does not justify a new named claim yet.
```

## Machinery Reused

T61 composes existing objects rather than introducing a parallel formalism:

- T46 `RecordAccessSystem` supplies finite propagation delays and the authority
  membership boundary.
- T37 `TypedTransportNetwork` and `D1RestrictionMorphism` represent movement
  from client local view to edge cache to authority to reconciled client view.
- T55 `ConflictDescentDatum` and conflict completion represent incompatible
  predicted events.
- D1 profiles track observer-access support, holder redundancy, branch support,
  and reversal cost.

T61 adds only small sidecar records for simulation observations and witness
answers.

## Axis Mapping

| T61 axis | Existing support |
| --- | --- |
| causal finality | T46 propagation order plus T55 `AxisProfile.causal` |
| information finality | D1 `holder_redundancy` and propagated record content |
| observer-access finality | D1 `accessible_support` per observer view |
| branch/conflict support | D1 `branch_support` plus T55 conflict pairs |
| reversal cost | D1 `reversal_cost` before and after authoritative commit |

This mapping is intentionally conservative. T61 does not add a new D1 axis.

## Finite System

The system has four nodes:

```text
client_a
client_b
edge_cache
authority_region
```

The propagation graph is:

```text
client_a -> edge_cache      delay 1
client_b -> edge_cache      delay 1
edge_cache -> client_a      delay 1
edge_cache -> client_b      delay 1
edge_cache -> authority     delay 4
authority -> edge_cache     delay 4
```

The authority boundary has one member:

```text
authority_region
```

Only the authority can convert a predicted client action into an authoritative
world event.

## Positive Witness

Name:

```text
positive_prediction_confirmed
```

One client predicts a movement action at local time 1. The authority receives
the prediction at time 6 and commits the same action at time 7. The commit
record reaches both clients at time 12.

| Question | Answer |
| --- | --- |
| What is final locally? | `client_a:pred_move_a@1` is apparent local finality. |
| What is final authoritatively? | `authority_region:commit_move_a@7`. |
| What is only predicted? | `pred_move_a` before the commit record arrives. |
| What gets rolled back? | Nothing. |
| What records propagate? | `pred_move_a`, `commit_move_a`. |
| Which observer sees which event when? | client A sees prediction at 1; edge at 2; authority at 6; authority commits at 7; clients see commit at 12. |
| How does reversal cost change? | `1 -> 7` after authority commit. |
| Interpretation | Reconciliation upgrades apparent local finality without contradiction. |

The positive witness proves that apparent local finality and authoritative
event finality are distinct finite observables even when reconciliation is
successful.

## Failure Witness

Name:

```text
failure_stale_conflicting_prediction
```

Client A predicts a claim on a resource at time 1. Client B, still stale with
respect to A's prediction, predicts an incompatible claim at time 2. Client B
only sees A's prediction at time 3. The authority receives A's branch at time 6,
B's branch at time 7, commits A's branch at time 8, and emits a rollback for
B's branch at time 8.

| Question | Answer |
| --- | --- |
| What is final locally? | `client_a:pred_claim_a@1` and `client_b:pred_claim_b@2` are apparent local finalities. |
| What is final authoritatively? | `authority_region:commit_claim_a@8` and `authority_region:rollback_claim_b@8`. |
| What is only predicted? | `pred_claim_b` until rollback reaches client B. |
| What gets rolled back? | `pred_claim_b`. |
| What records propagate? | `pred_claim_a`, `pred_claim_b`, `commit_claim_a`, `rollback_claim_b`, `compensate_b`. |
| Which observer sees which event when? | B predicts at 2 before seeing A at 3; authority receives A at 6 and B at 7; B receives rollback at 13 and compensation at 14. |
| How does reversal cost change? | B's prediction requires explicit correction after conflict; A's committed branch rises from `1 -> 7`. |
| Interpretation | Clean reconciliation fails unless rollback, compensation, or explicit conflict handling is present. |

T55 conflict completion classifies the incompatible predictions as:

```text
classification = canonical
conflict_valid = True
conflict_pairs = {e_claim_a # e_claim_b}
```

The failure witness is a failure of silent reconciliation, not a failure of the
formal machinery. The machinery succeeds precisely because the conflict is made
explicit.

## Typed Transport Result

Both witnesses use a typed path:

```text
client_local_view -> edge_cache_view -> authority_region_view -> reconciled_client_view
```

The accumulated forgotten structure includes:

```text
remote_client_state
authority_membership
client_prediction_certainty
cache_freshness
```

In the conflict case it also includes:

```text
losing_branch_as_world_state
```

The T37 admissibility verdict is `no_admissible_paths` because T61 is not
claiming a PO1 obstruction theorem. The typed network is used for state
movement and forgotten-structure accounting, not to promote a new PO1 claim.

## Claim Impact

T61 strengthens A1 in a bounded way:

```text
Distributed-simulation finality provides a hostile engineered domain where
observer-relative apparent finality, authoritative event finality, propagation
delay, rollback, and conflict repair are operationally separable.
```

T61 does not create a new named claim because:

- only two finite witnesses are tested;
- no partitioned-authority or authority-migration case is included;
- rollback policy is simple and explicit;
- the result remains an engineered-domain formal analogy/homology candidate.

## Theorem Candidate

Finite MMO Reconciliation Separation:

> In the tested finite distributed simulation, apparent local finality can
> precede authoritative event finality. If the authority commit matches the
> prediction, reconciliation upgrades apparent finality without contradiction.
> If stale predictions are incompatible, reconciliation requires rollback,
> compensation, or explicit conflict handling.

This should remain a theorem candidate until more hostile policy variants are
tested.

## Boundary

T61 does not claim:

- that physical reality is an MMO;
- that reality has a central authority;
- that client prediction is a model of perception;
- that rollback is a physical process;
- that T61 proves a new physics claim;
- that all observer-relative finality reduces to distributed simulation.

The result is useful because the engineered domain forces the formalism to
answer exact operational questions.

## Evidence

Executable files:

- `models/mmo_reconciliation_finality.py`
- `models/run_t61.py`
- `tests/test_mmo_reconciliation_finality.py`

Result artifacts:

- `results/mmo-reconciliation-finality-v0.1.json`
- `results/mmo-reconciliation-finality-v0.1-results.md`

Run:

```bash
python -m pytest tests/test_mmo_reconciliation_finality.py -q
python -m models.run_t61
```

