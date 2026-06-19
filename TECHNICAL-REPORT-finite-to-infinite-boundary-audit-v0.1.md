# Technical Report: Finite-to-Infinite Boundary Audit v0.1

## Question

T59 asks which finite Time-as-Finality theorem patterns survive when the domain
is countably infinite or continuous. This v0.1 increment tests the most
consequential boundary identified in the written audit:

```text
Does the T39 signed-graph parity criterion detect continuous orientation-sheaf
obstruction, or is it only a finite/binary special case?
```

## Result

The Mobius orientation witness separates two encodings:

```text
transition-aware Z2 encoding:
  preserves overlap components and transition signs
  parity detects the obstruction

coefficient-blind scalar encoding:
  forgets transition signs
  parity reports a false global section
```

Best-supported verdict:

```text
T39 parity survives the Mobius boundary only as a transition-aware Z2 special
case. It is not licensed as a generic continuous-domain obstruction detector.
```

## Witness

The model uses a two-patch cover with two disconnected overlap components.

| Cover | Transition signs | Monodromy | Orientation section |
| --- | --- | ---: | --- |
| Cylinder control | `+1, +1` | `+1` | exists |
| Mobius witness | `+1, -1` | `-1` | obstructed |

The transition-aware encoding translates the Mobius witness into finite
constraints:

```text
U0 same U1       on I_plus
U0 different U1  on I_minus
```

T39 parity classifies this as a direct parity conflict.

The coefficient-blind encoding translates both overlaps as ordinary agreement:

```text
U0 same U1       on I_plus
U0 same U1       on I_minus
```

This finite CSP is satisfiable even though the Mobius monodromy is nontrivial.
That is the false-global-section boundary witness.

## Hypothesis Evaluation

### H0

The T39 signed-graph parity criterion is a universal continuous-domain
obstruction detector.

Status: refuted.

Evidence: the coefficient-blind scalar Mobius encoding has monodromy `-1`, but
parity reports a satisfiable finite constraint system.

### H1

The Mobius orientation obstruction is detected after a transition-aware Z2
reduction.

Status: supported.

Evidence: preserving both overlap components and their transition signs gives a
same-plus-different direct parity conflict.

### H2

Coefficient and transition data are load-bearing at the finite-to-continuous
boundary.

Status: best_supported.

Evidence: the same Mobius topological case is correctly obstructed by the
transition-aware encoding and incorrectly accepted by the coefficient-blind
encoding; the cylinder controls remain accepted in both encodings.

## Claim Impact

This weakens the broadest possible reading of CSP-PO1:

```text
finite signed parity = a complete continuous-domain obstruction detector
```

That reading is not supported.

The bounded surviving claim is:

```text
finite signed parity is a valid detector after the relevant continuous problem
has been faithfully reduced to a Z2 transition system.
```

For genuinely continuous domains, the coefficient object and transition maps
must be stated first. The replacement target is sheaf cohomology with the
appropriate coefficient data, not a blind reuse of finite same/different CSP
constraints.

## What T59 Does Not Decide

- It does not reject T39 inside finite binary same/different CSPs.
- It does not prove a full sheaf-H1 theorem for continuous domains.
- It does not decide whether PO1 admissibility metadata has a natural
  continuous sheaf-theoretic analogue.
- It does not promote S1, Q1, H7, or HEF to physics claims.

## Recommended Next Goal

Build the sheaf-H1 replacement for continuous orientation data and compare its
obstruction verdict against PO1 admissibility metadata:

```text
continuous orientation sheaf obstruction
  -> coefficient-aware H1 verdict
  -> typed PO1 metadata, if any
```
