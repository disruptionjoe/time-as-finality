# T142: Thermodynamic Erasure Calibration

## Route

Thermodynamic arrow of time.

## Question

After T141 grounds H7 on the explicit T1 record graph, do the surviving copy
and branch-support gains still carry any physical arrow content once reversible
uncopy and standard erasure/free-energy accounting are included?

## Motivation

T141 showed that no tested strict T1 D1 increase has a
constructor-impossible reverse. The next absorber is thermodynamics: a copied
record may be reversible when the source-copy correlation and control handle
remain available, or it may require ordinary erasure/free-energy accounting
when blindly reset. T142 makes that split explicit.

## Setup

Calibrate the T141 cases:

1. Access grant to an existing record.
2. Copy to a fresh holder on the same causal chain.
3. Copy to a fresh holder on an additional branch.
4. Access-loss control.

For copy cases, distinguish:

- correlated uncopy with source, copy, provenance, and reversible control
  available;
- blind reset or overwrite with those handles unavailable, carrying a
  dimensionless lower bound `beta*W >= erased_bits * ln 2`.

Also audit the T128 finite resource-drawdown survivor and ask whether its
resource unit is physically typed.

## Success Criteria

- Access grants classify as boundary changes, not thermodynamic arrows.
- Copy and branch-support reverses include a zero-blind-erasure correlated
  uncopy mode.
- Copy and branch-support reverses include a one-bit blind-reset erasure mode
  absorbed by standard free-energy accounting.
- The artifact preserves the distinction between D1 topology and
  thermodynamic cost: two cases may have the same blind-reset floor but
  different D1 deltas.
- T128 resource drawdown is not treated as physics-facing until its resource
  unit is mapped to a real free-energy, blank-memory, fuel, sink, or capacity
  variable.

## Failure Criteria

- Treating every copy deletion as Landauer erasure even when reversible uncopy
  handles are available.
- Treating every copy deletion as free when the only available operation is a
  blind reset or overwrite.
- Promoting D1 topology at fixed erasure floor to a thermodynamic-arrow claim
  without a physical task and absorber pass.
- Treating T128's resource token as a physical variable before it is typed.

## Claim Impact

H7 is not upgraded. The T1/T141 survivor is absorbed by boundary accounting,
reversible uncopy, or ordinary erasure/free-energy accounting. D1 topology may
still be useful, but it does not by itself ground a physical arrow.

## Reproduction

```bash
python -m unittest tests.test_thermodynamic_erasure_calibration -v
python -m models.run_t142
```
