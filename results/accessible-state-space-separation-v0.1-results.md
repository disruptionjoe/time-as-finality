# T117 Results: Accessible State Space Separation Audit

## Current strongest claim

ASP separates finite systems that coarse entropy, information, finality, viability, persistence, and coarse reachability classify identically, but only by adding task requirements, witnesses, rights, certifications, and reconstruction paths.

## Strongest separation case

Version control is the strongest finite separation: same endpoint repository state, entropy, information, finality, viability, persistence, and coarse reachable count, but branch history and merge-base witnesses change the accessible future task set from {build} to {build, merge, revert, bisect}.

## Strongest absorption case

Reachable-state analysis or opportunity-set economics absorbs ASP once the state includes witness availability, rights, certifications, maintenance budgets, and reconstruction paths. Under that enriched state, ASP is the feasible action/opportunity set, not a new primitive.

## Domain verdicts

| Domain | Entropy | Information | Finality | Viability | Persistence | ASP split | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `version_control` | `True` | `True` | `True` | `True` | `True` | `True` | Separates from coarse metrics; absorbed by history-aware reachability/provenance. |
| `provenance` | `True` | `True` | `True` | `True` | `True` | `True` | Separates from data equality; absorbed by provenance and side-information formalisms. |
| `governance` | `True` | `True` | `True` | `True` | `True` | `True` | Separates from archive equality; absorbed by authority-aware mechanism/commons models. |
| `commons` | `True` | `True` | `True` | `True` | `True` | `True` | Separates from resource equality; absorbed by commons governance if maintenance rights are state. |
| `consensus` | `True` | `True` | `True` | `True` | `True` | `True` | Separates from committed-state equality; absorbed by challenge-window and validator-state models. |
| `record_system` | `True` | `True` | `True` | `True` | `True` | `True` | Separates from stored-record equality; absorbed by schema/provenance/reconstruction-debt state. |

## ASP task sets

| Domain | High-ASP tasks | Low-ASP tasks | Lost-structure chain |
| --- | --- | --- | --- |
| `version_control` | `['bisect', 'build', 'merge', 'revert']` | `['build']` | `True` |
| `provenance` | `['attribute', 'certify', 'repair_lineage', 'use']` | `['use']` | `True` |
| `governance` | `['appeal', 'challenge', 'read_archive', 'repair_rule']` | `['read_archive']` | `True` |
| `commons` | `['audit', 'consume', 'repair', 'sanction']` | `['consume']` | `True` |
| `consensus` | `['accept', 'challenge', 'rollback', 'slash']` | `['accept']` | `True` |
| `record_system` | `['certify', 'read', 'reconstruct', 'repair']` | `['read']` | `True` |

## Prior-art pressure

| Domain | Target | Capture | Explanation |
| --- | --- | --- | --- |
| `version_control` | viability kernels | `captures_if_enriched` | Coarse viability is matched; viability theory absorbs ASP if the viability set is future-task availability. |
| `version_control` | reachable-state analysis | `captures_if_enriched` | Coarse reachable count is matched; enriched reachable sets over rights and witnesses are essentially ASP. |
| `version_control` | control-theoretic controllability | `captures_if_enriched` | Coarse control rank is matched; controllability over certified operation states captures the split. |
| `version_control` | active inference | `captures_if_enriched` | Policies over future usable states absorb ASP when witnesses and rights are part of the generative state. |
| `version_control` | free-energy approaches | `partial` | Free-energy style maintenance can absorb expected opportunity preservation, but coarse free-energy does not encode legal/admissible rights. |
| `version_control` | opportunity-set economics | `captures_directly` | ASP is very close to a feasible opportunity set under constraints and rights. |
| `version_control` | ecological resilience | `partial` | Resilience captures persistence of function if function is defined as future task availability. |
| `version_control` | adaptive-cycle models | `partial` | Adaptive-cycle language can describe changing opportunity sets, but does not by itself encode witness admissibility. |
| `version_control` | commons governance | `partial` | Monitoring, sanctioning, repair, authority, and challenge rights absorb shared-resource ASP cases. |
| `version_control` | niche construction | `partial` | Niche construction captures modified future option spaces for lineages, but not all record-witness cases. |
| `version_control` | mechanism design | `captures_if_enriched` | Rights, incentives, challenge rules, and admissible moves are mechanism-design variables. |
| `provenance` | viability kernels | `captures_if_enriched` | Coarse viability is matched; viability theory absorbs ASP if the viability set is future-task availability. |
| `provenance` | reachable-state analysis | `captures_if_enriched` | Coarse reachable count is matched; enriched reachable sets over rights and witnesses are essentially ASP. |
| `provenance` | control-theoretic controllability | `captures_if_enriched` | Coarse control rank is matched; controllability over certified operation states captures the split. |
| `provenance` | active inference | `captures_if_enriched` | Policies over future usable states absorb ASP when witnesses and rights are part of the generative state. |
| `provenance` | free-energy approaches | `partial` | Free-energy style maintenance can absorb expected opportunity preservation, but coarse free-energy does not encode legal/admissible rights. |
| `provenance` | opportunity-set economics | `captures_directly` | ASP is very close to a feasible opportunity set under constraints and rights. |
| `provenance` | ecological resilience | `partial` | Resilience captures persistence of function if function is defined as future task availability. |
| `provenance` | adaptive-cycle models | `partial` | Adaptive-cycle language can describe changing opportunity sets, but does not by itself encode witness admissibility. |
| `provenance` | commons governance | `partial` | Monitoring, sanctioning, repair, authority, and challenge rights absorb shared-resource ASP cases. |
| `provenance` | niche construction | `partial` | Niche construction captures modified future option spaces for lineages, but not all record-witness cases. |
| `provenance` | mechanism design | `captures_if_enriched` | Rights, incentives, challenge rules, and admissible moves are mechanism-design variables. |
| `governance` | viability kernels | `captures_if_enriched` | Coarse viability is matched; viability theory absorbs ASP if the viability set is future-task availability. |
| `governance` | reachable-state analysis | `captures_if_enriched` | Coarse reachable count is matched; enriched reachable sets over rights and witnesses are essentially ASP. |
| `governance` | control-theoretic controllability | `captures_if_enriched` | Coarse control rank is matched; controllability over certified operation states captures the split. |
| `governance` | active inference | `captures_if_enriched` | Policies over future usable states absorb ASP when witnesses and rights are part of the generative state. |
| `governance` | free-energy approaches | `partial` | Free-energy style maintenance can absorb expected opportunity preservation, but coarse free-energy does not encode legal/admissible rights. |
| `governance` | opportunity-set economics | `captures_directly` | ASP is very close to a feasible opportunity set under constraints and rights. |
| `governance` | ecological resilience | `partial` | Resilience captures persistence of function if function is defined as future task availability. |
| `governance` | adaptive-cycle models | `partial` | Adaptive-cycle language can describe changing opportunity sets, but does not by itself encode witness admissibility. |
| `governance` | commons governance | `captures_if_enriched` | Monitoring, sanctioning, repair, authority, and challenge rights absorb shared-resource ASP cases. |
| `governance` | niche construction | `partial` | Niche construction captures modified future option spaces for lineages, but not all record-witness cases. |
| `governance` | mechanism design | `captures_if_enriched` | Rights, incentives, challenge rules, and admissible moves are mechanism-design variables. |
| `commons` | viability kernels | `captures_if_enriched` | Coarse viability is matched; viability theory absorbs ASP if the viability set is future-task availability. |
| `commons` | reachable-state analysis | `captures_if_enriched` | Coarse reachable count is matched; enriched reachable sets over rights and witnesses are essentially ASP. |
| `commons` | control-theoretic controllability | `captures_if_enriched` | Coarse control rank is matched; controllability over certified operation states captures the split. |
| `commons` | active inference | `captures_if_enriched` | Policies over future usable states absorb ASP when witnesses and rights are part of the generative state. |
| `commons` | free-energy approaches | `partial` | Free-energy style maintenance can absorb expected opportunity preservation, but coarse free-energy does not encode legal/admissible rights. |
| `commons` | opportunity-set economics | `captures_directly` | ASP is very close to a feasible opportunity set under constraints and rights. |
| `commons` | ecological resilience | `partial` | Resilience captures persistence of function if function is defined as future task availability. |
| `commons` | adaptive-cycle models | `partial` | Adaptive-cycle language can describe changing opportunity sets, but does not by itself encode witness admissibility. |
| `commons` | commons governance | `captures_if_enriched` | Monitoring, sanctioning, repair, authority, and challenge rights absorb shared-resource ASP cases. |
| `commons` | niche construction | `partial` | Niche construction captures modified future option spaces for lineages, but not all record-witness cases. |
| `commons` | mechanism design | `captures_if_enriched` | Rights, incentives, challenge rules, and admissible moves are mechanism-design variables. |
| `consensus` | viability kernels | `captures_if_enriched` | Coarse viability is matched; viability theory absorbs ASP if the viability set is future-task availability. |
| `consensus` | reachable-state analysis | `captures_if_enriched` | Coarse reachable count is matched; enriched reachable sets over rights and witnesses are essentially ASP. |
| `consensus` | control-theoretic controllability | `captures_if_enriched` | Coarse control rank is matched; controllability over certified operation states captures the split. |
| `consensus` | active inference | `captures_if_enriched` | Policies over future usable states absorb ASP when witnesses and rights are part of the generative state. |
| `consensus` | free-energy approaches | `partial` | Free-energy style maintenance can absorb expected opportunity preservation, but coarse free-energy does not encode legal/admissible rights. |
| `consensus` | opportunity-set economics | `captures_directly` | ASP is very close to a feasible opportunity set under constraints and rights. |
| `consensus` | ecological resilience | `partial` | Resilience captures persistence of function if function is defined as future task availability. |
| `consensus` | adaptive-cycle models | `partial` | Adaptive-cycle language can describe changing opportunity sets, but does not by itself encode witness admissibility. |
| `consensus` | commons governance | `captures_if_enriched` | Monitoring, sanctioning, repair, authority, and challenge rights absorb shared-resource ASP cases. |
| `consensus` | niche construction | `partial` | Niche construction captures modified future option spaces for lineages, but not all record-witness cases. |
| `consensus` | mechanism design | `captures_if_enriched` | Rights, incentives, challenge rules, and admissible moves are mechanism-design variables. |
| `record_system` | viability kernels | `captures_if_enriched` | Coarse viability is matched; viability theory absorbs ASP if the viability set is future-task availability. |
| `record_system` | reachable-state analysis | `captures_if_enriched` | Coarse reachable count is matched; enriched reachable sets over rights and witnesses are essentially ASP. |
| `record_system` | control-theoretic controllability | `captures_if_enriched` | Coarse control rank is matched; controllability over certified operation states captures the split. |
| `record_system` | active inference | `captures_if_enriched` | Policies over future usable states absorb ASP when witnesses and rights are part of the generative state. |
| `record_system` | free-energy approaches | `partial` | Free-energy style maintenance can absorb expected opportunity preservation, but coarse free-energy does not encode legal/admissible rights. |
| `record_system` | opportunity-set economics | `captures_directly` | ASP is very close to a feasible opportunity set under constraints and rights. |
| `record_system` | ecological resilience | `partial` | Resilience captures persistence of function if function is defined as future task availability. |
| `record_system` | adaptive-cycle models | `partial` | Adaptive-cycle language can describe changing opportunity sets, but does not by itself encode witness admissibility. |
| `record_system` | commons governance | `partial` | Monitoring, sanctioning, repair, authority, and challenge rights absorb shared-resource ASP cases. |
| `record_system` | niche construction | `partial` | Niche construction captures modified future option spaces for lineages, but not all record-witness cases. |
| `record_system` | mechanism design | `captures_if_enriched` | Rights, incentives, challenge rules, and admissible moves are mechanism-design variables. |

## Falsification result

ASP is not killed by coarse metrics, but it is mostly absorbed by enriched reachability, controllability, opportunity-set economics, commons governance, provenance, and reconstruction-debt formalisms.

## Missing object

A prespecified observer-task admissibility structure: task universe, witness requirements, operation rights, certification tokens, maintenance budget, reconstruction paths, horizon, and observer access. Without these, ASP is post hoc.

## Recommended disposition

Preserve and formalize only as an observer/task-indexed set-valued audit object. Do not promote ASP as independent physics. Reject any scalar or global 'future opportunity' reading.

## Claim ledger update

No core claim upgrade. T117 preserves ASP only as a set-valued observer/task-indexed audit object. It separates from coarse entropy/information/finality/viability metrics, but collapses into enriched reachable-state/opportunity/provenance analysis when those frameworks include witnesses and operation rights.
