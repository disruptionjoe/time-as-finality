# Technical Report: Future Capability Preservation Audit v0.1

## Claim Under Test

Multiple branches have converged on a similar residue:

```text
same current state != same future capability
```

T129 asks whether this residue is a genuine mathematical object, a recurring
framing artifact, a repackaging of existing theory, or a useful cross-domain
audit pattern.

The working label `Future Capability Preservation` is provisional only.

## Result

A common structure exists, but it is not a new primitive.

The smallest structure that explains the witness family is:

```text
visible state
+
task-indexed capability structure
```

where the capability structure names operations plus requirements for
witnesses, operation rights, reconstruction paths, provenance, maintenance or
access, certifications, and an admissibility policy.

Once that hidden structure is included in the state, the apparent same-state
split is absorbed by established frameworks: enriched reachability,
opportunity-set economics, provenance systems, access-control or capability
systems, mechanism design, and viability/control models.

## Finite Witness Table

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

## Strongest Common Object

A task-indexed constrained capability structure over a visible state:
operations plus requirements for witnesses, rights, reconstruction paths,
provenance, maintenance/access, certifications, and an admissibility policy.
It is an enriched state/action object, not a new physical primitive.

## Weakest Point

The candidate object only looks independent while the held-fixed state is
coarse. Once the hidden structure is included in the state, the split becomes
ordinary feasible-action, opportunity-set, provenance, mechanism, access-right,
or viability analysis.

## Closest Prior Art

Closest general homes:

- enriched reachability analysis;
- opportunity-set economics;
- viability kernels over task survival.

Closest evidence/rights homes:

- provenance systems;
- access-control and capability systems;
- mechanism design;
- distributed-systems capability/token models.

## Strongest Separation Witness

T123 is the cleanest separation witness: same raw payload, same immediate
measurement result, and same coarse detector summary, but packet wrapper
differences remove certification, reconstruction, challenge, lineage, and
claim-review operations.

## Strongest Absorption Witness

The Git/history case is the strongest absorption witness. The endpoint tree is
the same only under a deliberately coarse state description. Version-control
theory already treats branch history, merge base, signed tags, and provenance
as operational state.

## Recommendation

Formalize narrowly as an audit normal form. Do not promote.

`FCP` is useful if it means:

```text
check whether a proposed state equality forgot capability-bearing witnesses,
rights, provenance, reconstruction paths, access, maintenance, or certificates
needed for a declared task family.
```

It is not useful if treated as a new ontology or physics primitive.

## Claim Impact Note

No core claim upgrade. FCP should be treated as a cross-domain diagnostic for
missing witness/right/provenance/reconstruction state, not as a new ontology.

## Reproduction

```bash
python -m unittest tests.test_future_capability_preservation_audit -v
python -m models.run_t129
```
