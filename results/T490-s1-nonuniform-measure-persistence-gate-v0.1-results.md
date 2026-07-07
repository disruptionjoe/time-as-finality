# T490 - S1 Nonuniform Measure Persistence Gate - v0.1 results

> Measure-persistence gate only. No S1 promotion, T223 reversal, claim-ledger movement, roadmap movement, README movement, North Star movement, public posture, or cross-repo truth.

- Spec: `tests/T490-s1-nonuniform-measure-persistence-gate.md`
- Model: `models/s1_nonuniform_measure_persistence_gate.py`
- Tests: `tests/test_s1_nonuniform_measure_persistence_gate.py`
- Artifact JSON: `results/T490-s1-nonuniform-measure-persistence-gate-v0.1.json`
- Sources: `results/t54-ordinal-scaling-decisive-v0.1-results.md`, `results/T464-s1-added-assumption-admission-gate-v0.1-results.md`, `open-problems/spacetime-as-finality-colimit.md`

## Overall verdict: S1_NONUNIFORM_MEASURE_PERSISTENCE_GATE_BUILT_SCREEN_CONDITIONING_NOT_ENOUGH

T490 makes T464's nonuniform-measure branch sharper. The T223 uniform baseline stays closed; putting mass on known survivors is tail tuning; normalizing over parent-interval or screen-stack passes is guardrail conditioning, not an independent natural measure; and a single-size positive is insufficient. Only a future packet with a predeclared independent generating law, fixed finite screens, multi-size or limit persistence, a nonvanishing-mass claim, and named later Lorentzian constraints is admitted for review. Admission is not S1 evidence.

## T223 Baseline Used By This Gate

| n | total cases | parent-interval pass | stable survivors | uniform survivor mass | parent-conditioned survivor mass |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 6 | 720 | 156 | 26 | 13/360 | 1/6 |
| 7 | 5040 | 561 | 174 | 29/840 | 58/187 |
| 8 | 40320 | 2057 | 361 | 361/40320 | 361/2057 |

The parent-conditioned trajectory is reported as a diagnostic. It is not a natural measure by itself because it normalizes over an existing guardrail predicate.

## Packet Decisions

| packet | admitted? | gate label | classification | survivor mass trajectory | missing requirements | notes |
| --- | --- | --- | --- | --- | --- | --- |
| uniform_ordinal_baseline | False | REJECTED_UNIFORM_BASELINE_CLOSED_BY_T223 | uniform_t223_baseline_rejection | n=6:13/360, n=7:29/840, n=8:361/40320 | nonvanishing_mass_claim, nonvanishing_review_floor, later_lorentzian_constraints_named, not_uniform_t223_baseline | Uniform finite ordinal enumeration is the T223 no-go baseline. |
| known_survivor_tail_indicator | False | REJECTED_TAIL_INDICATOR_OR_SUCCESS_CONDITIONING | tail_tuned_measure_rejection | n=6:1/1, n=7:1/1, n=8:1/1 | predeclared_before_scoring, independent_generating_law, later_lorentzian_constraints_named, not_conditioned_on_survivor_success | Conditioning on the known survivor tail is circular. |
| parent_interval_conditioned_measure | False | REJECTED_GUARDRAIL_SCREEN_CONDITIONING | screen_conditioned_measure_rejection | n=6:1/6, n=7:58/187, n=8:361/2057 | predeclared_before_scoring, independent_generating_law, later_lorentzian_constraints_named, not_guardrail_screen_conditioned | Guardrail conditioning is diagnostic normalization, not a natural measure. |
| full_screen_stack_conditioned_measure | False | REJECTED_TAIL_INDICATOR_OR_SUCCESS_CONDITIONING | tail_tuned_measure_rejection | n=6:1/1, n=7:1/1, n=8:1/1 | predeclared_before_scoring, independent_generating_law, later_lorentzian_constraints_named, not_conditioned_on_survivor_success, not_guardrail_screen_conditioned | Conditioning on the known survivor tail is circular. |
| screen_drift_after_t223 | False | REJECTED_SCREEN_DRIFT_AFTER_T223 | screen_drift_rejection | n=8:361/40320 | predeclared_before_scoring, independent_generating_law, finite_audit_fixed_screens, multi_size_or_limit_audit, nonvanishing_review_floor, later_lorentzian_constraints_named, no_screen_drift | Changing screens after T223 is target drift. |
| single_size_n8_positive | False | REJECTED_SINGLE_SIZE_POSITIVE | single_size_rejection | n=8:1/4 | multi_size_or_limit_audit | T490 requires multi-size persistence or a declared limit target. |
| unjustified_nonuniform_weight | False | REJECTED_NO_INDEPENDENT_GENERATING_LAW | missing_measure_requirement_rejection | n=6:1/5, n=7:1/6, n=8:1/7 | independent_generating_law | The packet lacks the T490 measure-persistence burden. |
| nonvanishing_but_no_lorentzian_targets | False | REJECTED_NO_LORENTZIAN_CONSTRAINT_TARGETS | missing_measure_requirement_rejection | n=6:1/5, n=7:3/16, n=8:1/6 | later_lorentzian_constraints_named | The packet lacks the T490 measure-persistence burden. |
| claim_promotion_shortcut | False | BLOCKED_S1_PROMOTION_REQUEST | governance_boundary_block | n=6:1/5, n=7:3/16, n=8:1/6 | no_s1_promotion_request | Measure admission is not S1 evidence or promotion. |
| external_publication_shortcut | False | BLOCKED_EXTERNAL_ACTION_REQUIRED | external_action_block | n=6:1/5, n=7:3/16, n=8:1/6 | no_external_action_required | External publication or outreach needs separate authorization. |
| synthetic_predeclared_measure_review_target | True | ADMITTED_MEASURE_PERSISTENCE_REVIEW_TARGET_NO_PROMOTION | future_measure_persistence_review_target | n=6:1/5, n=7:3/16, n=8:1/6 | none | Admission is review-only and counts as no S1 evidence. |
| synthetic_continuum_bridge_weight_target | True | ADMITTED_MEASURE_PERSISTENCE_REVIEW_TARGET_NO_PROMOTION | future_measure_persistence_review_target | n=6:3/20, n=7:7/50, n=8:1/8 | none | Admission is review-only and counts as no S1 evidence. |

## Future Packet Minimum

- inherit T223 finite no-go and T464 admission burden
- predeclare the nonuniform measure, selection law, sprinkling law, or continuum bridge before scoring survivors
- supply an independent finality-native or neighbor-theory generating law
- keep T126/T156/T159/T223 finite screens fixed
- audit at least two finite sizes or declare a real limit target
- state a nonvanishing survivor-mass or concentration target before scoring
- do not condition directly on survivor success or guardrail-screen pass predicates
- name later causal, metric, covariance, locality, embedding, or Lorentzian constraints
- make no S1 promotion, spacetime derivation, public-posture, or external-action shortcut

## What This Does Not Earn

- S1 promotion
- T223 reversal
- spacetime derivation
- manifoldlikeness result
- dimension estimate
- sprinkling law
- Lorentzian metric
- locality or covariance theorem
- embedding theorem
- continuum theorem
- GR or QFT result
- claim-ledger movement
- ROADMAP movement
- README movement
- North Star movement
- public-posture movement
- cross-repo truth movement
