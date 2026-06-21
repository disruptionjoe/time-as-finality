# Technical Report: Accessible State Space Separation Audit v0.1

## Claim Under Test

Accessible State Space (ASP) is proposed as the future state-space that remains
causally reachable, structurally maintainable, and operationally usable for an
embedded observer or system.

T117 tries to kill ASP. The audit asks whether ASP does anything beyond
entropy, information, finality, viability, persistence, reachability,
controllability, opportunity sets, active inference, free-energy approaches,
resilience, commons governance, niche construction, or mechanism design.

## Finite Definition Used

For this artifact:

```text
ASP = admissible future task set
```

A task is in ASP only if all of these are available:

- required witnesses;
- required operation rights;
- sufficient maintenance budget;
- required reconstruction paths;
- required certification/admissibility tokens.

The task universe is fixed within each paired example. ASP is not assigned by
intuition after scoring.

## Matched Baseline Metrics

Each domain pair has equal:

- entropy bits;
- information bits;
- finality score;
- viability score;
- persistence horizon;
- coarse reachable count;
- coarse control rank.

The low-ASP system is therefore not worse by the baseline hierarchy. It differs
only in witness/right/certification/reconstruction structure.

## Domains Tested

| Domain | Matched state | ASP split |
| --- | --- | --- |
| Version control | Same endpoint repository state | `{build}` versus `{build, merge, revert, bisect}` |
| Provenance | Same data | use-only versus attribution/certification/lineage repair |
| Governance | Same archive | read-only versus challenge/appeal/repair |
| Commons | Same resource | consume-only versus audit/sanction/repair |
| Consensus | Same committed checkpoint | accept-only versus challenge/slash/rollback |
| Record system | Same stored records | read/repair versus reconstruct/certify/repair |

## Strongest Separation Case

Version control is the strongest finite separation. A squashed snapshot and a
history-preserving repository can have the same endpoint tree, entropy,
information, finality, viability, persistence, coarse reachable count, and
coarse control rank. The history-preserving repository keeps merge bases,
branch history, and signed-history witnesses. That changes future operations:

```text
{build} -> {build, merge, revert, bisect}
```

This is a real finite split against the coarse hierarchy.

## Strongest Absorption Case

The same version-control case is also the strongest absorption case. Once
reachable-state analysis, opportunity-set economics, or provenance systems
include branch history, merge bases, signed tags, and operation rights in the
state, ASP is absorbed. It becomes the feasible future action set.

That is the central result: ASP survives coarse-metric comparison but collapses
into enriched opportunity/reachability/provenance formalisms.

## Prior-Art Pressure

| Target | Verdict |
| --- | --- |
| Viability kernels | Absorb ASP if the viability set is future-task availability. |
| Reachable-state analysis | Absorbs ASP when the state includes witnesses, rights, and certificates. |
| Control-theoretic controllability | Absorbs ASP over certified operation states. |
| Active inference | Absorbs ASP if policies range over witness/right-bearing future states. |
| Free-energy approaches | Partially absorb expected opportunity preservation, but coarse free-energy omits legal/admissible rights. |
| Opportunity-set economics | Directly captures ASP as a feasible opportunity set. |
| Ecological resilience | Partially captures ASP when function is future task availability. |
| Adaptive-cycle models | Partially capture changing opportunity sets, but not witness admissibility by default. |
| Commons governance | Absorbs shared-resource, governance, and consensus examples when rights and monitoring are state. |
| Niche construction | Partially captures modified future option spaces for lineages. |
| Mechanism design | Absorbs rights, incentives, challenge rules, and admissible moves. |

## Lost-Structure Chain

The tested pairs instantiate:

```text
lost structure
-> reconstruction debt
-> maintenance/admissibility loss
-> reduced future options
-> ASP reduction
```

But this chain is not independent of existing theory. It is naturally described
by provenance, reconstruction debt, enriched reachability, and mechanism design.

## Recommended Disposition

Preserve and formalize narrowly. Do not promote.

ASP is useful as a set-valued observer/task-indexed audit object. It is not
earned as a new primitive, a scalar, or a replacement for entropy, information,
finality, viability, or reachability.

## Falsification Result

ASP is not killed by coarse entropy/information/finality/viability metrics.
It is mostly killed as an independent object by enriched reachable-state and
opportunity-set theories.

## Open Requirement

Any future ASP use must pre-register:

- task universe;
- observer/horizon;
- witness requirements;
- operation rights;
- maintenance budget;
- reconstruction paths;
- admissibility tokens.

Without those, ASP is post hoc vocabulary.

## Reproduction

```bash
python -m unittest tests.test_accessible_state_space_separation -v
python -m models.run_t117
```
