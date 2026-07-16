# T585 Results: Landauer Physical Capability Gate

## Verdict

- Verdict: `LANDAUER_PHYSICAL_CAPABILITY_INSTANTIATES_QUOTIENT_REVIEW_ONLY`
- Source contract: T583 CapabilityContract v1 plus T584 invariance quotient
- Source system: `one_bit_memory_erasure_with_thermal_bath_and_work_store`

## Source Law

Minimum reset work is represented in normalized kBT ln 2 units as the binary entropy of the one-bit memory state.

| state | reset work in kBT ln 2 units |
| --- | ---: |
| `known_zero_record` | 0.0 |
| `biased_record` | 0.468995594 |
| `max_entropy_record` | 1.0 |
| `biased_record_bit_label_swapped` | 0.468995594 |

## Audits

| audit | relation | passed? | completion class | reason |
| --- | --- | :---: | --- | --- |
| `source_law_capability_distinction` | `SUPERSET` | True | `SOURCE_STATE_INDUCED_PHYSICAL_CAPABILITY_DELTA` | A low-entropy memory can erase inside the fixed work budget while a max-entropy memory cannot. |
| `joule_unit_representation` | `EQUIVALENT` | True | `RENAMING_OR_REPRESENTATION_EQUIVALENCE` | Joule costs at the reference temperature normalize back to the same kBT ln 2 units. |
| `bit_label_gauge_swap` | `EQUIVALENT` | True | `RENAMING_OR_GAUGE_EQUIVALENCE` | Swapping bit labels changes p_one to 1-p_one but preserves entropy and the native envelope. |
| `irrelevant_metadata_coarse_graining` | `EQUIVALENT` | True | `IRRELEVANT_COARSE_GRAINING` | Display and sensor fields drop while entropy, encoding, and record stability remain fixed. |
| `blind_distribution_access_control` | `SUPERSET` | True | `ACCESS_COMPLETION` | Removing distribution access forces a worst-case reset accounting and is classified as access completion. |
| `low_work_store_budget_control` | `SUPERSET` | True | `RESOURCE_BUDGET_COMPLETION` | Changing the work budget removes feasible erasure and is classified as resource/budget completion. |
| `same_display_hidden_entropy_completion` | `SUPERSET` | True | `NATIVE_STATE_COMPLETION` | Same display label with different source entropy is absorbed by native thermodynamic state completion. |

## Checks

| check | passed? | reason |
| --- | :---: | --- |
| `landauer_costs_ordered` | True | The source law separates known, biased, and max-entropy one-bit memories. |
| `physical_capability_nontrivial` | True | Under the fixed work budget, erasure is feasible for the known record but not for the max-entropy record. |
| `unit_representation_invariant` | True | Changing from normalized units to joules and back preserves the capability envelope. |
| `bit_label_gauge_invariant` | True | The bit-label gauge swap preserves the entropy-derived capability envelope. |
| `irrelevant_coarse_graining_invariant` | True | Display and sensor fields declared irrelevant do not alter the physical payload. |
| `access_control_absorbed` | True | Loss of distribution access is not counted as intrinsic capability change. |
| `resource_budget_control_absorbed` | True | A changed work budget is not counted as intrinsic capability change. |
| `hidden_state_completion_absorbed` | True | Hidden entropy differences are handled as native source-state completion. |

## Physical Result

The surviving capability quotient has a concrete physical instantiation: a fixed work budget distinguishes erasure capability for known, biased, and max-entropy one-bit memory states while remaining invariant under unit representation, bit-label gauge, and declared irrelevant metadata.

## Claim Status

No claim-ledger or Canon Index update is earned.

## Not Claimed

T585 does not derive time, temporal order, issuance, a universal capability measure, a new thermodynamic theorem, a source law beyond the declared Landauer-style input, public posture, publication, TAF3, TAF8, S1, or cross-repo truth.

## Next Work

Use the physical capability model only as a source-owned input for the next burden: test whether record-dependent capability change can define a noncircular order rather than restating background time, entropy, access, or resources.
