# T128: Minimal Living Arrow

## Route

Thermodynamic arrow of time, narrowed after T80, T82, T84, T106, T110, and
T122.

## Question

What is the smallest finite system that produces a genuine directional scalar
once the required assumption is explicit?

## Controls And Tests

Control A: closed reversible finite cycle.

Expected result: no arrow.

Control B: stationary finite Markov chain.

Expected result: no arrow.

Test C: finite resource drawdown.

Test D: finite maintenance-cost system.

Test E: finite open-boundary system.

Test F: finite constructor-restricted system.

## Success Criteria

- Each model has a finite state space and executable transition rules.
- Each model states resource accounting and direction candidate.
- The closed reversible control fails under T110.
- The stationary Markov control fails under T122.
- Surviving models explicitly state which T122 assumptions they violate.
- Maintenance and open-boundary survivors are tested for reduction to resource
  drawdown, exported history, or sink-capacity accounting.
- Constructor restriction is marked as formal but stipulative.

## Failure Criteria

- Claiming a thermodynamic arrow.
- Hiding a resource, sink, boundary, omitted reverse channel, postselection, or
  transient-only path.
- Treating maintenance as independent when its direction is just finite repair
  budget depletion.
- Treating open boundary as independent when its direction is sink fill or
  exported history.

## Claim Impact

No thermodynamic-arrow promotion. T128 preserves H7 only as a
resource-accounting or constructor lemma. The smallest non-stipulative finite
survivor is explicit finite resource drawdown; the smallest formal survivor is
constructor restriction by stipulation.

## Reproduction

```bash
python -m unittest tests.test_minimal_living_arrow -v
python -m models.run_t128
```
