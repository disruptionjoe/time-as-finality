# T172: Issuance-To-Finality Bridge

## Route

Thermodynamic arrow of time / Time as Finality source-readout bridge.

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [Temporal Issuance Bridge v0.1](../explorations/temporal-issuance-bridge-v0.1.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)

## Question

If a source-side realization order exists, when does observer-side TaF finality
preserve it?

The bridge hypothesis is:

```text
source realization order
  -> observer records
  -> finality readout
```

not:

```text
finality alone creates the source-level arrow
```

## Motivation

The Temporal Issuance bridge note suggests a directional correction for H7.
Record-finality should not be asked to generate physical time or the
thermodynamic arrow by itself. It may instead be a sound observer-readable
certificate, reflection, or projection of a source-side realization process,
if such a process can be typed without circularly importing ordinary time,
entropy, information growth, record finality, or a preferred global frontier.

T172 makes the correction executable before any claim promotion.

## Setup

Audit six finite fixtures:

1. `sound_record_generation_reflection_control`
   A positive preservation control: one observer records a source chain in
   source order, and the readout recovers the visible source order.
2. `same_issuance_different_cadence`
   Same source order and same `mu`, different observer cadence. Apparent
   finality profiles differ without changing the source order.
3. `same_records_different_hidden_issuance`
   Same observer records and same TaF readout, different hidden source edge.
   Source capability does not factor through the readout.
4. `same_issuance_records_different_mu`
   Same source order and observer records, different `mu`. The measure is
   invisible to plain finality order but task-relevant when the declared source
   capability needs it.
5. `nonmonotone_access_loss`
   Same source order and records, but observer access support decreases. The
   nonmonotonicity is an observer-boundary effect, not a source arrow.
6. `gluing_failure_global_order_not_assumed`
   Same unglued local records are compatible with different source orders.
   Global order must be reconstructed through declared gluing data.

## Success Criteria

- The positive control recovers visible source order.
- Cadence changes apparent finality without changing source order.
- Same observer records can hide source realization differences.
- `mu` is not silently promoted: it is decorative for plain finality order and
  lost when a `mu`-sensitive source task is declared.
- Nonmonotone accessible support is classified as observer-boundary loss.
- Unglued local records do not determine a global order.
- No fixture promotes H7 as a source-level physical-arrow claim.

## Failure Criteria

- A cadence split is mistaken for a source-order split.
- Hidden source order or `mu` differences are declared preserved by TaF
  readout when the readout has no such data.
- Access loss is treated as a source-arrow result.
- Global source order is assumed without gluing data.
- The positive control is read as evidence that records create source order.

## Claim Impact

H7 remains `weakened_conditional`.

Add this sharpening:

```text
Finality-induced direction should be treated as an observer-side reflection or
factorization test. A TaF readout can certify or project a source realization
order only after record generation, access, cadence, source-measure, and
gluing data are declared. Finality alone has not derived a source-level arrow.
```

## Reproduction

```bash
python -m unittest tests.test_issuance_to_finality_bridge -v
python -m models.run_t172
```
