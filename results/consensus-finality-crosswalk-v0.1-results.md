# Consensus Finality Crosswalk Results

Result: T17 focused tests pass `6/6`; the current full branch suite passes
`35/35`.

## Model

Each protocol configuration is:

```text
(nodes, quorum, branches, confirmations, timeout)
```

The lab computes:

```text
D1 = (accessible support, holder redundancy, branch support, reversal cost)
```

It also computes three distributed-systems summaries:

- safety finality;
- liveness under bounded adversarial delay;
- economic finality.

## Collapse Maps

| Distributed definition | D1 dimensions used | D1 dimensions collapsed | Verdict |
| --- | --- | --- | --- |
| safety finality | support, holder redundancy, reversal cost | branch support | partial collapse |
| liveness finality | support at deadline | redundancy, branch support, reversal cost | protocol progress condition, not a D1 dimension |
| economic finality | reversal cost | support, redundancy, branch support | strict one-dimensional collapse |

## Divergence Witnesses

The search evaluates `392` bounded configurations.

It finds three useful divergences:

1. **Same safety, different branch finality.** Two configurations can both be
   safety-final while D1 distinguishes their independent branch support.
2. **Same economic cost, different D1 profile.** Reversal cost can match while
   support, redundancy, and branch structure differ.
3. **Same distributed signature, different D1 profile.** Safety, liveness,
   and economic cost can agree while D1 remains different.

This is the formal point: D1 is not just a synonym for distributed finality.
It is a higher-resolution profile that can be collapsed into distributed
definitions under stated assumptions.

## Bounded Impossibility Witness

Under budget `10`, the component maxima are:

```text
(support=4, redundancy=4, branch_support=3, reversal_cost=9)
```

No admissible configuration reaches all four maxima simultaneously. The search
returns a five-point Pareto frontier:

```text
n2-q2-b2-c4-t2 -> (2, 2, 2, 8)
n3-q3-b1-c3-t3 -> (3, 3, 1, 9)
n3-q3-b2-c2-t3 -> (3, 3, 2, 6)
n3-q3-b3-c1-t3 -> (3, 3, 3, 3)
n4-q4-b1-c1-t4 -> (4, 4, 1, 4)
```

Each frontier point gives up something: branch support, reversal cost,
liveness, or support/redundancy.

## Verdict

T17 strengthens A1 as a precise analogy:

```text
distributed finality definitions = collapses or protocol-side projections of D1
```

It also strengthens D1 by showing why keeping dimensions separate matters.

Limits:

- The impossibility is a bounded search witness, not a general theorem.
- Liveness is modeled as a simple deadline condition.
- The lab does not claim physical systems literally run consensus protocols.

## Reproduction

```bash
python -m unittest tests.test_consensus_finality_crosswalk -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t17
```

Machine-readable output:

- [consensus-finality-crosswalk-v0.1.json](consensus-finality-crosswalk-v0.1.json)
