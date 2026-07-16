# T583: CapabilityContract v1

## Target Claims

The TaF-owned region-indexed capability object, TAF3, TAF8, T407, T408, and
T582.

## Setup

Implement CapabilityContract v1 as a finite source definition plus executable
review instrument. Use a bounded region, observer/access profile, task family,
operation menu, provenance fields, resources, explicit cost/error budget,
physical equivalence, gauge quotient, horizon, and native comparison.

Construct capability as the task-indexed Pareto frontier of attainable
performance-cost-error points. Do not scalarize by default.

## Success Criteria

- The context carries access, menu, resource, and budget provenance.
- Capability is a region-indexed attainable envelope with a native preorder.
- Renaming, representation, and gauge changes preserve the envelope.
- Declared irrelevant coarse-graining preserves the physical payload.
- Distinct state identifiers can have equal capability.
- A positive preservation control passes.
- A negative nonfactorization fixture is detected without being promoted.
- Access, menu, resource, budget, fixed-source, and native-state completions
  fail closed.
- W192 remains `EXPLICIT_STATE_RESOURCE_COMPLETION`.
- A complete synthetic candidate stops at review-candidate status.

## Failure Criteria

- Capability defaults to one scalar.
- A label, gauge representative, or presentation field changes capability.
- A changed task, operation menu, access profile, resource, budget, or horizon
  is treated as a matched intrinsic-capability comparison.
- W192 receives a positive physical capability verdict.
- A synthetic fixture moves a claim, canon, public posture, or cross-repo
  result.

## Run Commands

```text
python -m models.t583_capability_contract_v1 --write-results
python -m unittest tests.test_t583_capability_contract_v1 -v
```

## Boundary

T583 is a finite executable contract. It does not establish a universal
capability measure, physical time, issuance, a source law, or cross-repository
identity. It does not move claims, canon, public posture, or publication.
