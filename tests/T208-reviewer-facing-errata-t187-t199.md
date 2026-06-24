# T208: Reviewer-Facing Errata For T187-T199

## Target Claims

- T187 exact Moses optimization
- T193-T199 downstream Cap_TI / MTI packet

## Origin

T187-T199 overstated harmonic-mean exactness. The repo needs a compact errata
packet preserving valid finite/proxy work while demoting invalid derivation
claims.

## Formal Target

Produce a correction map:

```text
old claim
correction
surviving statement
affected files
```

## Setup / Fixtures

Audit T187, T193, T194, T195, T196, T197, T198, and T199 against:

```text
LP/KKT validity
harmonic normalization
DAG shared-edge assumptions
continuum bridge status
```

## Positive Control

The packet must catch:

- pure LP selects a shortest path;
- lower-bound LP does not imply inverse-time weights;
- `1/sum_i(1/t_i)` and `k/sum_i(1/t_i)` are different;
- shared-edge DAG path summaries are proxy-only.

## Negative Control

The packet must not erase valid arithmetic under the harmonic proxy or the
finite observation that causal order alone does not determine the proxy value.

## Absorber Pass

Standard LP, scheduling, queueing, and network-flow theory absorb the exactness
language unless the objective and constraints are restated.

## Results

Correction map:

| Item | Update |
| --- | --- |
| T187 | Exact derivation killed; harmonic proxy retained. |
| T193 | `(n,T*)` minimality becomes proxy-only. |
| T194 | Hostile family collapse is conditional on proxy statistic. |
| T195 | DAG result is path-summary proxy; shared-edge flow not modeled. |
| T196 | Continuum bridge remains unsupported and is further weakened by T205. |
| T197 | Absorption by scheduling/flow theory is strengthened. |
| T198 | Controls apply to declared harmonic-proxy regime unless restated. |
| T199 | Reviewer packet must foreground errata before export. |

## Verdict: narrowed

The line is not discarded, but its exportable claim is narrowed to finite
harmonic-proxy separation plus corrected LP/DAG caveats.

## Falsification Conditions

Fails if any affected artifact still says harmonic mean follows from the stated
LP/KKT setup without a new objective.

## Next Step

Patch `TESTS.md` and affected result notes, then use T209 as the executable
guardrail.
