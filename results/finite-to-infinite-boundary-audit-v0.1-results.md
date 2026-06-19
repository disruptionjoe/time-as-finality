# T59 Results: Finite-to-Infinite Boundary Audit

## Verdict

T39 parity survives the Mobius boundary only as a transition-aware Z2 special case. It is not licensed as a generic continuous-domain obstruction detector.

## Audit Table

| Cover | Encoding | Monodromy | Orientation global section | Parity global section | False global section |
| --- | --- | ---: | --- | --- | --- |
| mobius_two_patch_orientation_cover | transition_aware_z2 | -1 | False | False | False |
| mobius_two_patch_orientation_cover | coefficient_blind_scalar | -1 | False | True | True |
| cylinder_two_patch_orientation_cover | transition_aware_z2 | 1 | True | True | False |
| cylinder_two_patch_orientation_cover | coefficient_blind_scalar | 1 | True | True | False |

## Hypothesis Results

### H0: refuted

The T39 signed-graph parity criterion is a universal continuous-domain obstruction detector.

Evidence: The coefficient-blind scalar encoding of the Mobius cover has monodromy -1 but parity reports a satisfiable same/same finite constraint system.

### H1: supported

The Mobius orientation obstruction is detected after a transition-aware Z2 reduction.

Evidence: Preserving both overlap components and their signs gives same plus different constraints on U0/U1, which parity classifies as a direct parity conflict.

### H2: best_supported

Coefficient and transition data are load-bearing at the finite-to-continuous boundary.

Evidence: The same Mobius topological case is correctly obstructed by the transition-aware encoding and incorrectly accepted by the coefficient-blind encoding; the cylinder controls remain accepted in both encodings.

## Boundary

Continuous-domain claims must state the coefficient object and transition maps before applying finite parity language. Forgetting that data can produce a false global section even when the orientation monodromy is nontrivial.

## Recommended Next

Build the sheaf-H1 replacement for continuous orientation data and then compare its obstruction verdict against PO1 admissibility metadata.
