# Consensus Parametric Tradeoff Boundary

## Research line

RL-003: Distributed-systems / consensus finality crosswalk.

## Why this note exists

T17 already identifies the next contribution needed for the consensus line:
generalize the bounded theorem check into a parameterized result and state which
resource-budget families preserve or break the tradeoff.

This note is a bounded scout for that next contribution. It does not change A1,
D1, T17, T20, or RL-003 status. It records a small parameter sweep over the
existing T17 verifier and turns the result into a sharper future-test target.

## Surfaces inspected

- `workflows/registries/line-registry.md`
- `workflows/registries/research-line-scorecard.md`
- `ROADMAP.md`
- `tests/T17-consensus-finality-crosswalk.md`
- `tests/T20-consensus-record-theorem-transfer.md`
- `tests/T28-cap-theorem-bridge.md`
- `models/consensus_finality_crosswalk.py`
- `models/consensus_record_theorem_transfer.py`
- `results/consensus-finality-crosswalk-v0.1-results.md`
- `results/consensus-record-theorem-transfer-v0.1-results.md`
- `TECHNICAL-REPORT-consensus-finality-impossibility-v0.1.md`

## Scout method

The existing verifier was run without changing model code:

```bash
python - <<'PY'
from models.consensus_finality_crosswalk import verify_bounded_impossibility_theorem

for delay in range(1, 8):
    for budget in range(5, 25):
        theorem = verify_bounded_impossibility_theorem(
            budget=budget,
            adversarial_delay=delay,
        )
        if not theorem.holds:
            print(
                delay,
                budget,
                theorem.component_maxima.as_tuple() + (theorem.progress_maximum,),
                [item.config.name for item in theorem.joint_maximizers[:8]],
            )
PY
```

The loop scans `adversarial_delay in 1..7` and `budget in 5..24` using the same
finite protocol family as T17:

```text
(nodes, quorum, branches, confirmations, timeout)
```

with admissibility:

```text
nodes + branches + confirmations + timeout <= budget
```

## Observed boundary

The T17 theorem holds for the canonical setting:

```text
budget = 10
adversarial_delay = 2
```

Within the scout range, failures occur in two visible regimes.

### Degenerate low-budget regime

For `budget = 5`, all checked delays `1..7` admit a joint maximizer:

```text
n1-q1-b1-c2-t1
objective maxima = (1, 1, 1, 2, 1)
```

Interpretation: the model is too small to express the tradeoff. The single-node
case collapses the objectives into one admissible configuration. This should be
treated as a degeneracy boundary, not as evidence against the canonical T17
result.

### Relaxed-delay / high-budget regime

For `adversarial_delay >= 4` and `budget >= 16`, the verifier admits joint
maximizers such as:

```text
n4-q4-b4-c4-t4
objective maxima = (4, 4, 4, 16, 1)
```

For larger budgets, extra nodes can be added without changing the same maxima:

```text
n5-q4-b4-c4-t4
n6-q4-b4-c4-t4
```

Interpretation: once the resource budget is large enough to max out quorum,
branch support, confirmations, and timeout inside the finite caps, and once the
delay bound is relaxed enough that `t4` counts as progress, the tradeoff no
longer holds in the v0.1 search space.

## Candidate theorem shape

A future T17 follow-up should not try to prove the broad sentence:

```text
No admissible configuration ever maximizes all D1 dimensions and progress.
```

The scout suggests a safer theorem family:

```text
In the bounded T17 protocol family, the joint-maximizer obstruction is preserved
only in a non-degenerate scarcity window where the budget is high enough to
express independent objectives but low enough that quorum, branch support,
confirmation weight, and timeout cannot all reach their finite caps while also
satisfying bounded progress.
```

This is still only a candidate theorem shape. It needs a proof or exhaustive
classification over declared caps before it should be promoted.

## Why this matters

RL-003 has high leverage because it gives D1 an externally legible theorem
interface without requiring speculative physics claims. The parameter boundary
found here improves the line by converting a vague next step ("generalize T17")
into a concrete classification problem:

```text
Which resource and delay regimes preserve the T17 tradeoff, and which regimes
collapse it?
```

That classification would make the consensus analogy more rigorous and less
overclaimed. It would also prevent the canonical T17 result from being quoted
outside its scarcity assumptions.

## Deliberately not decided

- No claim status changed.
- No lifecycle stage or line status changed.
- No new theorem was accepted.
- No assertion was made that consensus impossibility theorems constrain physics.
- No assumption was made that the current finite caps are physically meaningful.

## Governance signal

RL-003 appears underworked relative to recent repo activity, but this note does
not recommend promotion or demotion. It flags one future review question:

```text
Should RL-003 remain incubated until T17 has a parameter-preservation theorem,
or is the current finite crosswalk already enough for a secondary-exploit paper
track?
```

That is a lifecycle/portfolio question for the appropriate governance workflow,
not for this exploration note.

## Recommended next test

Create a T17 follow-up that enumerates the preservation window symbolically or
semi-symbolically:

1. expose the finite caps on nodes, branches, confirmations, and timeout as named
   parameters;
2. classify budgets into degenerate, scarcity, and saturated regimes;
3. prove or exhaustively verify the threshold at which joint maximizers appear;
4. keep bounded progress outside D1, as T17 currently does.
