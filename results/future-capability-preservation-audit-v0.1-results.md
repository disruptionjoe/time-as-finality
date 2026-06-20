# T129 Results: Future Capability Preservation Audit

## Strongest common object

A task-indexed constrained capability structure over a visible state: operations plus requirements for witnesses, rights, reconstruction paths, provenance, maintenance/access, certifications, and an admissibility policy. It is an enriched state/action object, not a new physical primitive.

## Finite witness table

| Witness | State held fixed | Future capability changed | Candidate cause |
| --- | --- | --- | --- |
| Git history witness | same endpoint repository tree / snapshot | merge, revert, bisect, blame, signed-history review | branch history, merge base, signed tags, provenance witnesses |
| Detector packet witness | same raw payload, measurement result, and coarse detector summary | admissibility, reconstruction, challenge, certification, lineage verification, detector-claim review | packet provenance, authority separation, signatures, key state, revocation, publication, witnesses, reconstruction paths, challenge state |
| Reconstruction debt | same target-visible projected state | future reconstruction, judgment, repair, or attribution | lost source witnesses needed to resolve target judgments |
| Provenance work | same content, record, detector outcome, or colimit result | attribute, audit, certify, challenge, or trust the result | identity, custody, ancestry, signed DAG, intervention metadata |
| Operation-right discussions | same archive/resource/checkpoint or same coarse state | challenge, appeal, sanction, repair, rollback | authority, rights, public rules, challenge windows, quorum |
| ASP | same coarse entropy/information/finality/viability/reachability metrics | observer/task-indexed accessible future task set | witnesses, rights, maintenance budget, reconstruction paths, certifications |
| FOA | same present/coarse state under matched ordinary measures | future operations available under witness/right/path/certification constraints | explicit task-indexed operation requirements |
| LossKernel | same endpoints, map behavior, and naive lost-label set | attribution, obstruction resolution, future repair/judgment | source-anchored witness obligations, not label-only loss |
| Admissibility | same candidate claim, projection, or raw evidence payload | whether the claim/evidence may be used later | admissibility tokens, guard conditions, pre-registration, typed forgotten structure |
| Maintenance-cost investigations | same standard entropy/control/stability/viability/storage metrics | maintained usability, repair, challenge, emergence-platform operation | maintenance budget applied to witnesses, rights, repair paths, and record support |

## Branch representation

| Branch | Components present | Strongest absorber | Verdict |
| --- | --- | --- | --- |
| Git history witness | `['access_boundaries', 'certification_tokens', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | version-control provenance plus enriched reachability | strong separation from coarse endpoint state; absorbed by history-aware state |
| Detector packet witness | `['access_boundaries', 'certification_tokens', 'maintenance_capacity', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | provenance systems plus access-control/admissibility protocol | strong matched-result witness; no detector-physics promotion |
| Reconstruction debt | `['access_boundaries', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | abstract interpretation, lenses, why-not provenance, CSP explanation | common structure present; novelty mostly absorbed by source-fiber prior art |
| Provenance work | `['access_boundaries', 'certification_tokens', 'maintenance_capacity', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | provenance systems | directly absorbed by provenance once provenance is included in state |
| Operation-right discussions | `['access_boundaries', 'certification_tokens', 'maintenance_capacity', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | mechanism design, access control, commons governance | not a new object; rights-aware mechanism state absorbs it |
| ASP | `['access_boundaries', 'certification_tokens', 'maintenance_capacity', 'operation_rights', 'reconstruction_paths', 'task_policy', 'witness_availability']` | enriched reachable-state analysis and opportunity-set economics | ASP is essentially the same audit normal form under a colliding name |
| FOA | `['access_boundaries', 'certification_tokens', 'maintenance_capacity', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | enriched reachability/opportunity set | best internal label but still absorbed by established feasible-action formalisms |
| LossKernel | `['access_boundaries', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | rich effects, abstract interpretation, lenses, why-not provenance | source-witness form fits the common object; novelty remains unearned |
| Admissibility | `['access_boundaries', 'certification_tokens', 'maintenance_capacity', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | evidence law/protocol logic/access-control systems | admissibility is a policy layer over future operations, not FCP itself |
| Maintenance-cost investigations | `['access_boundaries', 'certification_tokens', 'maintenance_capacity', 'operation_rights', 'provenance_structure', 'reconstruction_paths', 'task_policy', 'witness_availability']` | viability kernels/control/resource accounting with enriched state | useful audit pattern; not independent of viability/control/resource frameworks |

## Prior-art pressure

| Framework | Verdict | Reason |
| --- | --- | --- |
| reachability analysis | `absorbs` | If the state includes witnesses, rights, access, provenance, and certificates, FCP is the reachable/action set. |
| viability kernels | `absorbs` | Absorbs FCP when the viability condition is survival of the declared capability set over a horizon. |
| opportunity-set economics | `absorbs` | Directly models feasible future opportunities under constraints and rights. |
| capability theory | `partial` | Close conceptual neighbor for real opportunities, but less formal about witnesses and certifications. |
| mechanism design | `absorbs` | Rights, admissible moves, incentives, challenge rules, and authority are native mechanism variables. |
| affordance theory | `partial` | Captures agent-environment action possibilities but may omit formal proof/admissibility structure. |
| active inference policy spaces | `absorbs` | Absorbs FCP if policies range over witness/right-bearing states and expected future actions. |
| reinforcement-learning action spaces | `partial` | Captures executable actions but usually lacks provenance, certification, and challenge rights. |
| provenance systems | `absorbs` | Directly captures lineage, custody, attribution, replay, and certification prerequisites. |
| access-control systems | `absorbs` | Directly captures authorized operations over protected resources and evidence objects. |
| distributed-systems capability models | `absorbs` | Capability tokens, leases, certificates, and quorum/challenge windows absorb many packet and consensus cases. |

## Weakest point

Once the hidden structure is admitted into the state, the apparent same-state split disappears into standard enriched reachability, opportunity-set, provenance, access-control, mechanism-design, or viability machinery. Novelty survives only against coarse state descriptions, which is not enough.

## Closest prior art

Enriched reachability and opportunity-set economics are closest at the abstract level. Provenance systems, access-control/capability systems, and mechanism design are closest for the evidence/rights cases. Viability kernels absorb the maintenance/horizon reading.

## Strongest separation witness

T123 is the cleanest same-state witness: same raw payload, same immediate measurement result, and same coarse detector summary, but different packet wrappers remove certification, reconstruction, challenge, lineage, and claim-review operations.

## Strongest absorption witness

The Git/history witness is the strongest absorption case: the endpoint tree is the same only under a deliberately coarse state. Version-control theory already treats branch history, merge base, and signed tags as operational state.

## Recommendation

Formalize narrowly as an audit normal form named only provisionally as FCP. Do not promote. The structure explains the witness family, but it is reducible to existing enriched state/action frameworks.

## Claim impact note

No core claim upgrade. FCP should be treated as a cross-domain diagnostic for missing witness/right/provenance/reconstruction state, not as a new ontology.

## Verdict flags

- Common structure exists: `True`
- Reducible to existing frameworks: `True`
- Recommendation: `formalize`
