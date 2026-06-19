# T61 MMO Reconciliation Synthesis

## Status

Short synthesis note after the MMO reconciliation lab was renumbered from T60 to
T61 because T60 is already assigned to Observer Closure.

This note is interpretive. The executable evidence lives in:

- `tests/T61-mmo-reconciliation-finality.md`
- `models/mmo_reconciliation_finality.py`
- `TECHNICAL-REPORT-mmo-reconciliation-finality-v0.1.md`

## Why T61 Matters

T61 makes the apparent-finality / event-finality split concrete in a hostile
engineered domain.

Before T61, that split could be read as mostly conceptual:

```text
an observer may treat a record as final before the larger event structure does
```

T61 turns it into an operational distinction:

```text
client-predicted state
  != edge-cached state
  != authority-committed state
  != reconciled observer state
```

Each layer has finite arrival times, D1 profiles, propagated records, and
possible correction records. The distinction is no longer only about how a
claim is described. It is about which observer can act on which record, when
the authority commits it, and what must be repaired if the local prediction
does not survive.

## Relation To T42

T42 separated local persistence accumulation from reconciliation lag.

T61 imports that split into a distributed simulation:

- the client accumulates apparent local finality when a predicted action is
  usable locally;
- the authority accumulates event finality only when the action is committed
  inside the authority boundary;
- the client receives the authoritative record later, so the local view and
  authoritative view are separated by reconciliation lag.

The important T42 guardrail survives:

```text
propagation delay is not the same thing as local finality
```

In T61, delay explains why the client sees stale or late records. It does not
by itself decide whether the predicted event is authoritative.

## Relation To T46

T46 distinguished open causal scarcity from closed synchronization scarcity.

T61 uses both:

- open causal scarcity: client and edge observations arrive through finite
  propagation paths;
- closed synchronization scarcity: the authority region is the only member
  allowed to commit world events.

This makes the authority boundary explicit without treating it as a metaphor
for physics. It is an engineered adversarial boundary: local access can be
early, useful, and still non-authoritative.

## Relation To T55

T55 showed that conflict is independent data. It cannot be reconstructed from
order or Axis Monotonicity alone.

T61 uses that result in the failure witness. Two clients predict incompatible
claims over the same resource. The system cannot silently merge both apparent
finalities into one authoritative result. The losing branch must be represented
as:

- rollback;
- compensation;
- explicit conflict.

The T55 conflict completion is what prevents the failure witness from being
hand-waved away as a stale-cache artifact. The conflict is a first-class event
structure feature.

## Concrete Payoff

T61 answers, in executable form:

| Question | T61 answer |
| --- | --- |
| What is locally final? | A predicted action usable in a bounded observer view. |
| What is event-final? | An authority-committed record inside the synchronization boundary. |
| What is only predicted? | A local or edge-cached branch before commit confirmation. |
| What gets rolled back? | A predicted branch rejected by the authority. |
| What propagates? | Prediction, commit, rollback, and compensation records. |
| What changes reversal cost? | Authority commit and propagated holder redundancy. |
| What handles incompatibility? | T55-style explicit conflict data. |

## Claim Status

T61 strengthens A1 as a hostile engineered-domain test. It does not promote a
new named claim.

The useful result is narrower:

```text
observer-relative finality can be operationally separated into apparent local
finality, authoritative event finality, delayed reconciliation, and explicit
conflict repair in a finite distributed simulation.
```

That is enough to make the distinction testable. It is not enough to claim a
general theorem about all observer-relative finality.
