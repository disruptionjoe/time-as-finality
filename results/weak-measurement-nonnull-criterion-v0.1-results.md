# T132 Results: Weak-Measurement Non-Null Criterion

Null protocols: `6`
Candidate protocols: `1`

| Protocol | Independent axes | Classification | Passes gate |
| --- | --- | --- | --- |
| `threshold_only_homodyne` | none | `null_same_record_derivation` | `False` |
| `semantic_partition_relabel` | branch_support | `null_unpreregistered_or_post_hoc` | `False` |
| `same_record_branch_live` | branch_support | `null_same_record_derivation` | `False` |
| `constant_branch_support_family` | branch_support | `null_constant_branch_support` | `False` |
| `undo_energy_proxy` | reversal_cost | `null_monotone_proxy_cost` | `False` |
| `independent_meter_not_decisive` | reversal_cost | `independent_but_not_decisive` | `False` |
| `preregistered_channel_intervention_candidate` | holder_redundancy | `candidate_non_null_protocol` | `True` |

## Strongest claim

The weak-measurement route is non-null only in a narrow shape: a pre-registered, event-level or intervention-defined D1 axis must change the TaF verdict while the ordinary decoherence and redundancy verdict stays fixed.

## What improved

T132 upgrades the weak-measurement gate from prose into a reusable audit that can reject same-record, post hoc, constant-branch, and monotone-proxy proposals before platform-specific modeling.

## Weakened claim

Most apparent T12 rescue moves are null in the present repo framing. Naming a second label, a different threshold, a constant branch count, or an undo-energy proxy does not produce a discriminator.

## Falsification condition

T132 fails if a protocol lacking a pre-registered independent axis legitimately changes the TaF verdict under fixed standard statistics, or if an admitted candidate turns out to be reconstructible from the same monitored record.

## Q1C update

Keep Q1C dormant. The surviving task is not to search for another suggestive weak-measurement story, but to name one concrete independent measured axis and show that it alone changes the TaF verdict.

## Blocker

No real platform in the repo currently instantiates the admissible candidate shape with a measured, verdict-changing independent axis.

## Recommended next

Try a single monitored platform with an intervention-defined provenance or duplicated-channel axis; if that cannot be specified before modeling, demote T12 from experimental route to standing obstruction.
