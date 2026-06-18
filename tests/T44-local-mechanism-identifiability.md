# T44: Local Mechanism Identifiability Audit

## Target Claims

- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
- [G2: Not A Replacement Theory](../guardrails/G2-not-a-replacement-theory.md)
- [T42: Local Persistence And Reconciliation Split Audit](T42-local-persistence-reconciliation-split.md)
- [T43: Local Persistence Accumulation Mechanism Audit](T43-local-persistence-mechanisms.md)

## Setup

Start from the T43 trace-equivalent mechanisms:

- intrinsic stabilization rate;
- finite resource budget;
- interaction density.

Each mechanism is configured to generate the same baseline local accumulation
trace. T44 applies finite probe protocols and asks which probes separate the
mechanisms.

## Probe Protocols

1. Baseline:
   - no perturbation;
   - expected to preserve T43 equivalence.

2. Event-count scaling:
   - increase event count while preserving per-event parameters;
   - expected to preserve equivalence.

3. Demand drop:
   - lower update demand;
   - expected to separate resource budget from the other mechanisms.

4. Resource shock:
   - lower stabilization budget;
   - expected to separate resource budget from the other mechanisms.

5. Coupling rewiring:
   - reduce local interaction count;
   - expected to separate interaction density from the other mechanisms.

6. Load recovery:
   - apply finite load then recovery;
   - in the simple trace model, expected to remain unresolved.

## Success Criteria

1. Implement at least three finite probe protocols.
2. Separate at least one mechanism pair.
3. Preserve at least one unresolved equivalence.
4. Find a minimal observable basis if one exists.
5. State verdicts for H0-H5.
6. Avoid physical proper-time claims.

## Failure Criteria

1. All mechanisms remain indistinguishable under every probe.
2. The probe set separates mechanisms only by adding domain-specific story.
3. The result modifies `D1RestrictionSystem`.
4. The report claims a physical clock mechanism.

## Known Physics Constraints

- This does not explain relativity.
- This does not derive proper time.
- This does not identify a physical local clock.
- This does not introduce spacetime dynamics.

## Contribution Needed

- Add richer probes if future mechanisms share the same demand and coupling
  response vector.
- Test whether any candidate probe maps to an operational physical observable
  before using it in physics-facing language.
