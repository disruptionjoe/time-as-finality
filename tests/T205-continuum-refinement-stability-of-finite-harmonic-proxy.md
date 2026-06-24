# T205: Continuum / Refinement Stability Of Finite Harmonic Proxy

## Target Claims

- T196 continuum bridge audit
- T203 corrected finite DAG proxy
- T204 same-harmonic congestion counterfixture

## Origin

A finite proxy cannot bridge to continuum WBE-style claims unless it is stable
under declared refinements or comes with a measure / weighting rule.

## Formal Target

Test whether the unweighted finite path harmonic is invariant under refinement
maps that preserve the intended macroscopic network.

## Setup / Fixtures

Positive refinement:

```text
serially subdivide an edge while preserving total time and capacity.
```

Path times stay fixed, so the harmonic mean stays fixed.

Hostile refinement:

```text
base path times {1,3}
T_H0 = 2 / (1 + 1/3) = 3/2
```

Refine the fast corridor into two parallel microchannels representing the same
macroscopic corridor capacity. The unweighted path list becomes:

```text
{1,1,3}
T_H1 = 3 / (1 + 1 + 1/3) = 9/7
```

## Positive Control

Serial subdivision should not change the proxy, and it does not.

## Negative Control

Capacity-preserving path multiplicity changes the unweighted harmonic solely
because the representation has more listed paths.

## Absorber Pass

Continuum network theory would use measure, capacity, conductance, or
cross-section weighting. Unweighted path counting is not a native continuum
object.

## Results

The finite harmonic proxy is stable under trivial serial subdivision but
unstable under path-multiplicity refinement.

## Verdict: killed

Killed as a continuum-stable bridge object. A capacity-weighted or
flow-conservation proxy remains open.

## Falsification Conditions

Revisit if a declared refinement functor and path measure make the proxy
invariant and convergent across hostile refinements.

## Next Step

T206 grants WBE/allometric network theory its native variables.
