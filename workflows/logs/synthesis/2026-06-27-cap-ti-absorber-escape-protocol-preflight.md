---
document_type: synthesis_preflight
queue_item: fifth_batch_6
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/cap-ti-capability-object-spec.md
source_results: results/T197-mti-absorber-audit-against-scheduling-queueing-flow-theory-v0.1-results.md; results/T206-native-wbe-allometric-network-absorber-audit-v0.1-results.md
---

# Cap_TI Absorber-Escape Protocol Preflight

## Scope

This preflight names the only live route by which Cap_TI Candidate C could
escape the current absorber verdicts. It does not implement the route, promote
Cap_TI, promote MTI, promote H7, or update any claim ledger.

The current safe posture is:

```text
Candidate C is absorbed as a timing-summary/native-network capability in the
exact harmonic and native WBE/allometric regimes.
```

Any future escape must change reconciliation behavior at fixed standard
timing and fixed native-network summaries.

## Read Surfaces

- `open-problems/cap-ti-capability-object-spec.md`.
- `results/T197-mti-absorber-audit-against-scheduling-queueing-flow-theory-v0.1-results.md`.
- `results/T206-native-wbe-allometric-network-absorber-audit-v0.1-results.md`.

## Absorbed Starting Point

T197 says the current Candidate C predictive content collapses to the
harmonic/effective delivery-time summary `T*` in the exact family:

```text
different T* -> split, but absorber-owned
same T* -> null
```

T206 extends the absorber posture once native allometric-network state is
granted:

```text
incidence, conductance/capacity, cost, demand, and optimization structure
explain the corrected finite proxy.
```

Therefore, the next protocol must not ask whether `R(beta,n)` can split when
ordinary timing or native network state splits. That is already absorbed.

## Only Live Escape

The only live escape is a reconciliation protocol:

```text
P_rec(Y_TI, O, A, G, beta, n, protocol_state) -> K_TI
```

whose observed or bounded reconciliation cost differs while all absorber-owned
summaries are held fixed:

```text
n
T_star or standard effective-delay summary
incidence
conductance_or_capacity
cost
demand
optimization_objective
causal_order
entropy_or_information_ledger
observer_access_boundary
observer_cadence
identity_overlap_gluing_topology G
```

The protocol must make the split depend on record-finality or PO1/gluing
structure that standard timing and native network theory do not already read.

## Required Protocol Semantics

The next executable must define a round before scoring cases.

Minimum round definition:

```text
round_id
observer_frontiers
published_local_order_fragments
overlap_witnesses_used
new_dependency_witnesses_delivered
conflicts_opened
conflicts_resolved
gluing_section_status
halt_condition
```

A reconciliation round is admissible only if:

```text
each observer publishes a frontier-limited local order fragment
overlap witnesses are matched through G
no timing data is added to G during the run
a conflict resolves only when a new dependency witness or source-order
  certificate enters the shared frontier
the protocol halts only when local fragments descend to one source-order
  section on the declared cover, or when the fixture marks failure
```

The old continuous proxy may be retained only as a baseline:

```text
R_continuous(n,beta) = n^(1 - beta)
```

It cannot be the capability theorem unless the protocol independently explains
why the round count changes at fixed absorber summaries.

## Freeze Vector

Before scoring, freeze:

```text
Y_TI
pi_TaF
Cap_TI_candidate
R_K_TI
n
T_star
native_network_state
causal_order
entropy_ledger
information_ledger
observer_family
access_boundary
cadence
record_generation_rule
identity_overlap_gluing_data
protocol_round_rule
halt_condition
```

If any split requires changing `T_star`, native network state, access, cadence,
or G, it is not an absorber escape.

## Controls

| Control | Required verdict |
| --- | --- |
| Positive timing split | Different `T_star` splits, but label `absorber_owned_positive`. |
| Matched `T_star` null | Same `T_star` and same native network state gives no split unless protocol-specific witnesses differ. |
| Native-network grant | Grant incidence, conductance/capacity, cost, demand, and optimization first. |
| Same beta, different G | Reject as G-owned unless G is part of the declared capability object. |
| Same beta, same G, different cadence | Reject as cadence-owned. |
| Same beta, same G, different access | Reject as access-owned. |
| Same absorber summaries, different PO1/gluing witness schedule | Candidate escape only if the protocol round count changes without changing frozen absorber fields. |
| Protocol-free formula | Reject as timing-summary residue. |

## Acceptance Criteria

The next artifact is accepted as useful only if all of the following hold:

- It starts from T197/T206 absorption, not from pre-absorption Candidate C
  language.
- It freezes `Y_TI`, `pi_TaF`, `Cap_TI`, and `R_K_TI`.
- It freezes standard timing summaries and native allometric-network state.
- It defines reconciliation rounds, conflict resolution, and halt conditions
  before scoring cases.
- It grants scheduling, queueing, flow, control, and native WBE/allometric
  absorbers before assigning residue.
- It includes matched `T_star` and matched native-network controls.
- It reports whether any split remains at fixed absorber summaries.
- It uses one of these final verdicts:

```text
absorbed_timing_summary_only
absorbed_native_network_only
protocol_escape_candidate_at_fixed_absorber_state
null_matched_absorber_controls
inconclusive_protocol_not_frozen
```

Only `protocol_escape_candidate_at_fixed_absorber_state` authorizes a later
test/model/results artifact. It still does not promote Cap_TI.

## Null Or Demotion Conditions

Demote Candidate C to timing-summary residue for this route if any condition
holds:

- The capability value is determined by `T_star`, effective service time,
  queueing congestion, or standard completion-time summaries.
- The capability value is determined by native network incidence,
  conductance/capacity, cost, demand, and optimization structure.
- The positive split appears only when standard timing or native state changes.
- Matched `T_star` and matched native state controls are null.
- The protocol changes access, cadence, G, or record-generation rules between
  arms.
- The round rule is chosen after seeing which system wins.
- `Cap_TI` is defined as recovering beta, mu_M, or a hidden issuance variable
  rather than as a task-natural capability.
- The protocol cannot distinguish reconciliation work from ordinary delivery
  delay.

Null result language to preserve:

```text
The absorber-escape protocol did not produce a capability split at fixed
standard timing and fixed native-network summaries. Cap_TI Candidate C remains
translation residue for this regime, and no formal-promotion language is
licensed.
```

## No-Promotion Guardrails

- Do not promote Cap_TI Candidate C to a supported formal capability.
- Do not promote MTI past its current ledger status.
- Do not treat Candidate C as H7, physical-arrow, or source-arrow evidence.
- Do not cite a timing-summary split as independent capability residue.
- Do not treat native WBE/allometric network quantities as TaF novelty.
- Do not use `R_continuous(n,beta)` alone as a protocol.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, models, results, README,
  or open-problem files from this preflight.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-cap-ti-absorber-escape-protocol-run-card.md
```

If later authorized for implementation, convert only a frozen run-card into:

```text
tests/TXXX-cap-ti-absorber-escape-protocol.md
models/cap_ti_absorber_escape_protocol.py
results/cap-ti-absorber-escape-protocol-v0.1-results.md
```

Required run-card sections:

```text
not_claimed
absorbed_starting_point
source_object_fields
absorber_freeze_vector
protocol_round_semantics
case_fixtures
positive_and_null_controls
native_absorber_grant
matched_summary_results
protocol_specific_residue_check
null_or_demotion_check
no_promotion_guardrail_check
final_verdict
```

Minimum machine-readable record:

```text
artifact_type: cap_ti_absorber_escape_protocol_run_card
case_id:
Y_TI:
pi_TaF:
Cap_TI_candidate:
R_K_TI:
fixed_T_star:
fixed_native_network_state:
fixed_access:
fixed_cadence:
fixed_G:
round_rule:
halt_condition:
changed_protocol_field:
observed_or_bounded_rounds:
absorber_verdict:
cap_ti_escape_verdict:
  absorbed_timing_summary_only |
  absorbed_native_network_only |
  protocol_escape_candidate_at_fixed_absorber_state |
  null_matched_absorber_controls |
  inconclusive_protocol_not_frozen
claim_impact: no_status_change
```

