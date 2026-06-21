# P32 - Reinforcement Learning Researcher Run

- persona: Reinforcement Learning Researcher
- goal_id: P32
- run_timestamp: 2026-06-21T17:04:26-05:00
- queue_source: `explorations/persona-future-run-goals-2026-06-20.md`
- goal: Model finality as what an agent can safely condition future action on
  under rollback risk, delayed observation, and policy-dependent information.
- posture: bounded exploratory run only; no claim-status update, roadmap
  change, or ledger edit.

## Repo Context Read

- `tests/T61-mmo-reconciliation-finality.md`
- `tests/test_mmo_reconciliation_finality.py`
- `tests/T77-measured-detector-policy-sensitivity.md`
- `tests/T80-reversible-finality-nonmonotonicity.md`
- `tests/T82-persistent-reconciler-cost-boundary.md`
- `tests/T119-future-operation-availability-residue.md`
- `tests/T121-real-detector-packet-schema-audit.md`
- `tests/test_future_operation_availability_residue.py`
- `models/future_operation_availability_residue.py`
- `models/same_payload_packet_foa_witness.py`
- `explorations/persona-goal-runs/2026-06-21-160430-p31-ai-learning-theory-representation-audit.md`

## Bounded Run

Question: what does the RL lens add if we restate finality as a condition on
which observations or records an agent may safely use for future policy
selection?

Method:

1. Use `T61` as the rollback and delayed-observation control.
2. Use `T77`, `T121`, and `T123` as the policy-sensitive evidence gate.
3. Use `T119` as the absorber check against ordinary RL action spaces,
   enriched reachability, and control language.

## Work Performed

I separated three objects that are easy to blur:

1. an action the agent can physically execute now;
2. an action that looks locally optimal under the current observation; and
3. an action that remains admissible if the current observation is later
   revised, challenged, or downgraded.

The third object is the useful TaF-facing one.

In RL language, the bounded question is not:

```text
what action maximizes reward from the current observation?
```

It is:

```text
which policy updates are safe to condition on this record as if it were
settled?
```

That reformulation fits the repo better because the existing witnesses are
about rollback, authority, admissibility, challenge rights, and delayed
reconciliation rather than reward optimization.

## Result

### Main Finding

The current repo supports an RL-style reading of finality only in a narrow,
audit-oriented sense:

```text
finality = safe conditioning boundary for future action,
not value itself and not a new action-space primitive
```

Ordinary RL action spaces only partially absorb this object. `T119` is already
correct to classify them as partial absorbers, because plain action sets do not
normally encode:

- rollback exposure;
- witness and reconstruction obligations;
- certification and challenge rights; or
- policy-corridor dependence.

### Smallest Honest RL Restatement

The safest current formulation is:

```text
A record is final for observer-agent O relative to task family T and horizon h
only when treating that record as settled keeps the resulting policy inside the
admissible future-operation set across the model's allowed delayed-observation,
rollback, authority, and policy-review continuations.
```

This is not yet a theorem. It is a bounded audit normal form extracted from
existing witnesses.

### Three Regimes

| regime | repo witness | RL-style reading | verdict |
| --- | --- | --- | --- |
| prediction later confirmed | `T61` positive witness | local policy may act provisionally before authority arrives, but the observation becomes safely conditionable only when later authoritative reconciliation does not force rollback | finality behaves like rollback-robust policy conditioning |
| stale conflicting prediction | `T61` failure witness | a locally good-looking action can still be unsafe because delayed information forces rollback, compensation, or explicit conflict repair | apparent value is not safe conditioning |
| same payload, different rights/policy state | `T77`, `T121`, `T123` | identical observations can license different future actions because challenge, certification, publication, authority, and policy corridor differ | state must include rights/witness/policy variables, not just observations |

### What the RL Lens Clarifies

The RL lens helps separate:

- `predicted_only` records: usable for reversible or low-commitment action, but
  not safe for irreversible conditioning;
- `conditionally_actionable` records: usable only under declared challenge,
  authority, and audit policy;
- `safely_conditionable` records: later compatible continuations do not eject
  the induced policy from the admissible future-operation class.

This is the useful residue. It is narrower than "finality explains agency" and
more precise than "finality is just what actions are available."

### What the RL Lens Does Not Yet Earn

The current evidence does not support:

- a claim that D1 is a reward function;
- a claim that finality is identical to ordinary value or Q-value;
- a claim that standard POMDP/RL state alone already captures the repo's
  witness, certification, authority, and challenge constraints; or
- a claim that policy dependence itself is new.

So the honest posture is:

```text
TaF adds an admissibility/rollback audit on top of sequential decision-making.
It does not yet add a new general RL theorem.
```

## Proposed Next Action

If this lane is continued later, the next bounded step should be a tiny
decision benchmark with three labels per observation:

1. `safe_to_condition`;
2. `provisional_only`; and
3. `must_abstain`.

The benchmark should reuse `T61` and `T123`-style fixtures and require at least
one pair with:

- same immediate observation;
- different rollback or challenge exposure; and
- different admissible future policy sets.

That would test whether the RL framing adds anything beyond enriched
reachability and constrained-control bookkeeping.

## Claim-Status Posture

- No claim-status changes proposed.
- No roadmap or ledger changes proposed.
- Status of this run: exploratory sequential-decision boundary audit.
- Best current classification: finality is usefully read as a safe
  conditioning boundary only when the policy state is enriched with witnesses,
  rights, authority, and rollback structure; otherwise ordinary RL/control
  language absorbs the result.
