# T46 Results: Open Causal Scarcity And Closed Synchronization Boundary

## Verdict

- Best-supported hypothesis: `H3`
- Named-claim recommendation: CS1 should remain a candidate claim, not a new claim file yet: T46 supports the finite principle, but more hostile cases are needed.

## Open Causal Scarcity

- First-access order: `('colocated_rack', 'metro_pop', 'remote_region')`
- Proximity advantage: `749`
- Proximity driven: `True`
- Finding: Open causal scarcity witnessed: first access follows finite path delay from the generating node; advantage=749 abstract units.

## Closed Synchronization Boundary

- Internal commit order: `('tx_west', 'tx_east')`
- Outside raw arrival order: `('tx_east', 'tx_west')`
- Outside commit-record arrival order: `('tx_east', 'tx_west')`
- Outside reconstruction time: `60`
- Raw order differs from commit order: `True`
- Membership boundary active: `True`
- Propagation constraints respected: `True`
- Synchronization cost total: `16`

## Boundary Comparison

- Open scarcity axis: `causal_proximity`
- Closed scarcity axis: `membership_plus_synchronization_rule`
- Outside observer lag: `35`
- Statement: Open systems expose a causal-proximity gradient. Closed systems can impose an internal commit order, but only for members and only with bounded synchronization costs; outside observers wait for propagated records before reconstructing that order.

## Measurement Projection Boundary

- Source layer: `richer_pre_record_structure_Y_candidate`
- Target layer: `observer_accessible_record_layer_X`
- Assumes 14D Y: `False`
- PO1 status: candidate_projection_boundary_only; AC5-like forgotten structure is named, but T46 does not claim AC1-AC7 or a full measurement PO1 theorem
- Preserved structure:
  - `classical_outcome_label`
  - `stable_pointer_record`
  - `accessible_correlation_statistics`
  - `conservation-compatible coarse quantities`
  - `record-holder accessibility relation`
- Forgotten structure:
  - `relative_phase_information`
  - `unmeasured_counterfactual_contexts`
  - `coherence_not_preserved_in_accessible_records`
  - `environment_entanglement_not_available_to_the_observer`

## Hypotheses

- `H0`: `rejected_for_finite_abstraction`
- `H1`: `supported`
- `H2`: `supported`
- `H3`: `best_supported`
- `H4`: `partially_supported`
- `H5`: `rejected_for_finite_access_distinction`

## Theorem

Finite Record-Access Scarcity Theorem: in the T46 RecordAccessSystem witnesses, open systems expose finality scarcity as causal-proximity advantage, while closed synchronized systems relocate scarcity to membership plus bounded commit rules. The closed system does not abolish propagation delay; outside observers can reconstruct internal order only after commit records propagate outward.

## Boundary

The theorem is finite and synthetic. It does not model actual NYSE market microstructure, does not implement Google Spanner, does not derive the speed of light, and does not claim a quantum measurement theorem.
