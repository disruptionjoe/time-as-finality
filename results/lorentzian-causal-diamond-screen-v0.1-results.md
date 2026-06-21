# T153 Results: Lorentzian Causal-Diamond Screen

## Aggregate Checks

- Remote-signal guardrail passed: True
- Spacelike reconciliation guardrail passed: True
- Domain of dependence absorbs reconstructability: True
- Changed access diamond absorbed: True
- Fixed Lorentzian data gives no residue: True

## Audit Table

| Case | Classification | Residue | TaF independent? | Matched Lorentzian data | Capability split | Causal relation | Required next |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `remote_signal_causal_past` | `remote_signal_is_causal_record_access` | `translation_residue` | `False` | `True` | `False` | `source_in_observer_causal_past` | Keep participation and received-record access as separate typed relations in S1/R1 models. |
| `spacelike_pair_later_reconciliation` | `spacelike_no_invariant_order_later_reconciles` | `translation_residue` | `False` | `True` | `False` | `spacelike_pair_with_common_future` | Any stronger R1 claim must preserve invariant interval structure and frame-independent causal order. |
| `domain_of_dependence_interval` | `domain_of_dependence_absorbs_reconstructability` | `absorbed_by_lorentzian_causality` | `False` | `False` | `True` | `same_initial_slice_different_domain_membership` | Name a capability not represented by causal pasts, diamonds, or domains of dependence before claiming TaF residue. |
| `same_source_changed_access_diamond` | `verdict_split_absorbed_by_changed_access_diamond` | `absorbed_by_lorentzian_access_boundary` | `False` | `False` | `True` | `same_source_different_collection_event` | For any future S1 witness, match the observer world tube and access diamond before scoring finality differences. |
| `fixed_lorentzian_data_control` | `fixed_lorentzian_data_no_finality_split` | `negative_control` | `False` | `True` | `False` | `matched_source_and_access_diamond` | A live residue must split verdicts after matching the Lorentzian causal data, observer world tube, and domain-of-dependence inputs. |

## remote_signal_causal_past

- Classification: `remote_signal_is_causal_record_access`
- Domain-of-dependence status: `not_domain_case`
- Reason: The remote source is in the observer's causal past through a received light signal. Direct local participation is absent, but record access is present.
- Weakened claim: R1 may distinguish received records from direct participation, but must not treat remote astronomical sources as unobserved.

## spacelike_pair_later_reconciliation

- Classification: `spacelike_no_invariant_order_later_reconciles`
- Domain-of-dependence status: `not_domain_case`
- Reason: The two events have no invariant causal order, but both can enter a later common record. This supports no-global-commit-order language only as ordinary Lorentzian causality.
- Weakened claim: R1 should say local records can later reconcile inside a common future, not that TaF supplies a replacement simultaneity rule.

## domain_of_dependence_interval

- Classification: `domain_of_dependence_absorbs_reconstructability`
- Domain-of-dependence status: `inside_control_true_outside_control_false`
- Reason: The reconstruction split is exactly membership in the future domain of dependence of the initial interval. The outside control requires initial data beyond the interval.
- Weakened claim: S1/B1 reconstructability language is absorbed when it tracks only ordinary domains of dependence.

## same_source_changed_access_diamond

- Classification: `verdict_split_absorbed_by_changed_access_diamond`
- Domain-of-dependence status: `not_domain_case`
- Reason: The source is inaccessible to the narrow collection event and accessible to the wider future event. The verdict split follows from a changed access diamond, not from a new finality predicate.
- Weakened claim: Same local source data do not create TaF residue when the observer access diamond changes.

## fixed_lorentzian_data_control

- Classification: `fixed_lorentzian_data_no_finality_split`
- Domain-of-dependence status: `not_domain_case`
- Reason: When the event coordinates and access diamond are matched, a record relabel does not change the causal-access verdict.
- Weakened claim: T153 finds no same-Lorentzian-data finality split in its controls.

## Strongest Claim

In the tested 1+1 Lorentzian controls, R1/S1/B1 access and reconstructability verdicts factor through ordinary causal pasts, causal diamonds, spacelike separation with common futures, and domains of dependence. TaF adds no independent spacetime or black-hole mechanism in this screen.

## What This Improved

T153 upgrades T151 from an abstract record-channel graph to a minimal Lorentzian absorber. It supplies explicit checks for remote observation, spacelike reconciliation, changed access diamonds, and domain-of-dependence reconstructability.

## What This Weakened

S1 and B1 are weakened wherever their verdicts change only because standard causal-access or domain-of-dependence data changed. R1 remains safe as no-global-commit-order language, not as a new relativity substitute.

## Falsification Condition

T153 fails in TaF's favor only if a future fixture matches the Lorentzian causal relation, observer world tube, access diamond, domain-of-dependence inputs, record channels, and boundary data, yet still produces a task-natural finality capability split not expressible as standard causal access or reconstructability.

## R1 Update

Add T153 to R1: spacelike events lack invariant causal order but can reconcile through a common future record. Remote signals are causal record access. This supports locality discipline, not a replacement time rule.

## S1 Update

Add T153 to S1: any finality-colimit or consensus-envelope model must carry Lorentzian causal data, access diamonds, and domain-of-dependence inputs before claiming spacetime-facing residue.

## B1 Update

Add T153 to B1: direct-classical horizon language remains ordinary causal-access/domain-of-dependence bookkeeping unless a native black-hole information capability is typed.

## Claim Ledger Update

T153 gives R1/S1/B1 a Lorentzian causal-diamond screen. The tested verdicts factor through causal pasts, common futures, changed access diamonds, and domains of dependence. No same-Lorentzian-data TaF residue is found.

## Open Blocker

The screen is 1+1 Minkowski only. It has no curvature, global hyperbolicity theorem, black-hole metric, QFT algebra, holographic encoding, semiclassical gravity, or continuum finality-colimit construction.

## Suggested Next

Use T153 as the absorber gate for S1/B1. The next non-null move is either a causal-set/manifoldlikeness implementation for T126 or a named Schwarzschild/de Sitter causal-access witness with native absorber variables declared up front.
