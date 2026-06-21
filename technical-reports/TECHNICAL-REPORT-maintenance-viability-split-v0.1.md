# Technical Report: Maintenance-Cost Viability Split v0.1

## Claim Under Test

The maintenance-cost direction is interesting only if it identifies something
that is not already exhausted by entropy production, control theory, viability
theory, resilience theory, free-energy approaches, commons governance,
information theory, provenance systems, or LossKernel/reconstruction debt.

T115 therefore does not ask whether maintenance matters. It asks whether finite
systems can match on ordinary stability and maintenance metrics while splitting
on future operation capability.

## Finite Object

Each paired case has identical standard metrics:

```text
entropy_export
control_effort
stability_window
viability_kernel
resilience_recovery_steps
storage_bits
maintained_record_count
```

The pair is then scored on future usability:

```text
accessible_witnesses
required_witnesses
operation_rights
required_rights
reconstruction_paths
admissibility_tokens
required_tokens
```

A system is future-usable only if required witnesses, required operation
rights, required admissibility tokens, and at least one reconstruction path are
available.

## Finite Examples

T115 constructs five matched-standard splits:

| Domain | Split |
| --- | --- |
| Record commons | Same records and maintenance metrics; only one system has public audit witnesses plus challenge/repair authority. |
| Provenance | Same output and storage metrics; only one system has signed lineage and source witness for attribution/certification. |
| Version control | Same endpoint tree and stability; only one system retains merge base, branch history, signed tags, and future merge/revert rights. |
| Governance | Same archive and maintenance level; only one system preserves quorum, appeal, and challenge authority. |
| Consensus | Same committed checkpoint; only one system preserves validator signatures, challenge window, and slashing rights. |

## Strongest Separation Case

The version-control pair is the sharpest finite separation. Two repositories
can have the same endpoint files, storage bits, stability window, ordinary
control effort, and viability label. One retains branch history and merge base;
the other is a squashed snapshot. The endpoint is equally maintained, but
future merge, revert, blame, and bisect operations differ.

Coarse entropy, control, resilience, viability, and storage metrics do not see
the split.

## Strongest Absorption Case

The same version-control pair is also the strongest absorption case. Ordinary
version-control/provenance semantics already treat merge bases, signed tags,
and branch history as operational state. Once that state is included, the
maintenance-cost direction is not a new object. It is operation-right-bearing
provenance.

## Comparison With Required Targets

| Target | T115 verdict |
| --- | --- |
| Entropy production | Coarse entropy/export does not capture the split because entropy metrics are matched. |
| Control-theoretic state maintenance | Absorbs the split if the controlled state includes operation rights and witness availability. |
| Viability kernels | Absorbs the split if the viability constraint set includes future operation rights. |
| Resilience/adaptive-cycle models | Partial: captures functional persistence if the function is explicitly audit/repair/challenge capability. |
| Free-energy formulations | Absorbs if the generative state/policy space includes witnesses, authority, and future operations. |
| Commons/public-goods models | Strongly absorbs record-commons, governance, and consensus cases through monitoring, sanctioning, authority, and repair rights. |
| Information-theoretic storage | Coarse storage bits do not capture the split; side information and access constraints can. |
| Provenance systems | Strongly absorbs witness, lineage, custody, signature, and admissibility-token splits. |
| LossKernel/reconstruction debt | Strongly absorbs missing witnesses as reconstruction obligations for a declared operation family. |

## Closest Existing Theory

The closest existing theory is not one framework. It is provenance systems plus
task-enriched viability/control theory. Commons governance captures authority
and challenge rights. LossKernel/reconstruction debt captures missing witness
obligations. Information theory captures the split only after replacing raw
storage quantity with accessible side information.

## Missing Mathematical Object

If anything is worth preserving, it is:

```text
operation-right-bearing record state
```

That means maintained records together with accessible witnesses,
authority/admissibility tokens, and reconstruction obligations for a declared
future operation family.

This is not simply "maintenance cost." It is maintained usability.

## Recommendation

Preserve and formalize narrowly. Do not promote.

The maintenance-cost direction should be kept only as operation-right-bearing
provenance/reconstruction-debt accounting. It should not be described as a
replacement for entropy production, viability theory, control theory, or
free-energy approaches.

## What This Weakened Or Falsified

T115 weakens the maintenance-cost direction as an independent theory. Finite
separations exist against coarse entropy/control/stability/viability/storage
metrics, but the strongest separations are absorbed by existing theories once
those theories are given witness availability, authority rights, and
operation-state data.

## Open Blocker

There is still no non-engineered physical example where operation-right-bearing
record usability separates from enriched viability, free-energy/control,
provenance, and information-theoretic side information.

## Reproduction

```bash
python -m unittest tests.test_maintenance_viability_split -v
python -m models.run_t115
```
