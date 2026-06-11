# T5: Thermodynamic Record Support

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [C1: Experienced Time As Record Finality](../claims/C1-experienced-time-as-record-finality.md)

## Setup

Compare two reversal quantities on the same finite record graph:

1. graph reversal count: the fewest accessible records that must be erased to
   put a proposition below its reconstruction threshold;
2. thermodynamic proxy: the least summed per-record erasure-cost proxy for the
   same operation.

## Success Criteria

- The framework states clearly that it does not derive the thermodynamic arrow.
- The model explains how thermodynamic irreversibility supports durable records.
- Record-finality language adds clarity without replacing entropy or coarse-graining.

## Failure Criteria

- The framework claims records explain entropy without proof.
- It ignores low-entropy initial conditions.
- It cannot distinguish microscopic reversibility from macroscopic record stability.
- Graph reversal count is presented as physical work without a dynamics or
  temperature-dependent model.

## Contribution Needed

Replace the assigned erasure-cost proxy with a physical memory model and
calculate dissipated work under a specified erasure protocol.

## v0.1 Result

Status: **implemented as a finite information-thermodynamic lower-bound
model**.

In the reference scenario, propositions `A`, `B`, and `C` each require one
record deletion to fall below threshold, while their least erasure-cost
proxies are `1.0`, `2.0`, and `0.5`. Therefore graph reversal count does not
determine the thermodynamic proxy. This establishes dimension separation
inside the toy model, but not a new physical law.

## Emergence Laboratory Result

The lab models degenerate binary memories in contact with a 300 K heat bath
and quasistatic reset. For a deterministic finite transition map under a
uniform input distribution:

```text
lost_bits = H(X|Y)
minimum_heat = k_B T ln(2) * lost_bits
```

Width-five Rule 110 loses `0.737801` bits per update, producing a Landauer
lower bound of `2.1182e-21 J`. Its reversible second-order lift loses zero
bits while still carrying a counterfactual record trace. Thermodynamic
information loss therefore does not define record finality.
