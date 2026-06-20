"""T129: same-state/different-future-capability audit.

Several branches have produced a similar residue:

    same visible/current state != same future capability

This module tests whether the residue requires a new primitive.  It represents
each witness as a visible state plus a task-indexed capability structure, then
pressures that structure against existing frameworks.  The intended outcome is
conservative: preserve a useful audit normal form only if it explains the
witness family, and do not promote a new ontology unless absorption fails.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Recommendation(Enum):
    REJECT = "reject"
    PRESERVE = "preserve"
    FORMALIZE = "formalize"
    PROMOTE = "promote"


class PriorArtVerdict(Enum):
    ABSORBS = "absorbs"
    PARTIAL = "partial"
    MISSES_ONLY_IF_COARSE = "misses_only_if_coarse"


@dataclass(frozen=True)
class CapabilityStructure:
    witnesses: frozenset[str]
    rights: frozenset[str]
    reconstruction_paths: frozenset[str]
    provenance: frozenset[str]
    maintenance: frozenset[str]
    access: frozenset[str]
    certifications: frozenset[str]
    task_policy: frozenset[str]

    def components_present(self) -> frozenset[str]:
        components: set[str] = set()
        if self.witnesses:
            components.add("witness_availability")
        if self.rights:
            components.add("operation_rights")
        if self.reconstruction_paths:
            components.add("reconstruction_paths")
        if self.provenance:
            components.add("provenance_structure")
        if self.maintenance:
            components.add("maintenance_capacity")
        if self.access:
            components.add("access_boundaries")
        if self.certifications:
            components.add("certification_tokens")
        if self.task_policy:
            components.add("task_policy")
        return frozenset(components)


@dataclass(frozen=True)
class BranchWitness:
    branch: str
    source_artifacts: tuple[str, ...]
    state_held_fixed: str
    future_capability_changed: str
    candidate_cause: str
    capability_structure: CapabilityStructure
    strongest_existing_absorber: str
    uniform_representation: bool
    superficial_state_difference: bool
    verdict: str


@dataclass(frozen=True)
class PriorArtPressure:
    framework: str
    verdict: PriorArtVerdict
    reason: str


@dataclass(frozen=True)
class T129Result:
    witnesses: tuple[BranchWitness, ...]
    prior_art: tuple[PriorArtPressure, ...]
    strongest_common_object: str
    weakest_point: str
    closest_prior_art: str
    strongest_separation_witness: str
    strongest_absorption_witness: str
    recommendation: Recommendation
    recommendation_rationale: str
    claim_impact_note: str
    finite_witness_table: tuple[tuple[str, str, str, str], ...]
    reducible_to_existing_frameworks: bool
    common_structure_exists: bool


def branch_witnesses() -> tuple[BranchWitness, ...]:
    return (
        BranchWitness(
            branch="Git history witness",
            source_artifacts=("T115", "T117", "T119"),
            state_held_fixed="same endpoint repository tree / snapshot",
            future_capability_changed="merge, revert, bisect, blame, signed-history review",
            candidate_cause="branch history, merge base, signed tags, provenance witnesses",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"tree", "merge_base", "branch_history"}),
                rights=frozenset({"merge", "revert", "bisect"}),
                reconstruction_paths=frozenset({"history_path"}),
                provenance=frozenset({"signed_history"}),
                maintenance=frozenset(),
                access=frozenset({"history_visible"}),
                certifications=frozenset({"signed_tags"}),
                task_policy=frozenset({"git_operation_policy"}),
            ),
            strongest_existing_absorber="version-control provenance plus enriched reachability",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="strong separation from coarse endpoint state; absorbed by history-aware state",
        ),
        BranchWitness(
            branch="Detector packet witness",
            source_artifacts=("T121", "T123"),
            state_held_fixed="same raw payload, measurement result, and coarse detector summary",
            future_capability_changed=(
                "admissibility, reconstruction, challenge, certification, "
                "lineage verification, detector-claim review"
            ),
            candidate_cause=(
                "packet provenance, authority separation, signatures, key state, "
                "revocation, publication, witnesses, reconstruction paths, challenge state"
            ),
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"packet_witnesses", "raw_export"}),
                rights=frozenset({"challenge", "certify", "claim_review"}),
                reconstruction_paths=frozenset({"event_replay", "calibration_bind"}),
                provenance=frozenset({"custody_chain", "authority_domains"}),
                maintenance=frozenset({"revocation_check", "key_continuity"}),
                access=frozenset({"packet_visible"}),
                certifications=frozenset({"signatures", "publication_token"}),
                task_policy=frozenset({"admissibility_gate"}),
            ),
            strongest_existing_absorber="provenance systems plus access-control/admissibility protocol",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="strong matched-result witness; no detector-physics promotion",
        ),
        BranchWitness(
            branch="Reconstruction debt",
            source_artifacts=("T107", "T108"),
            state_held_fixed="same target-visible projected state",
            future_capability_changed="future reconstruction, judgment, repair, or attribution",
            candidate_cause="lost source witnesses needed to resolve target judgments",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"source_lift_witnesses"}),
                rights=frozenset({"judge", "repair"}),
                reconstruction_paths=frozenset({"source_fiber_lift"}),
                provenance=frozenset({"projection_map"}),
                maintenance=frozenset(),
                access=frozenset({"source_access"}),
                certifications=frozenset(),
                task_policy=frozenset({"target_judgment_policy"}),
            ),
            strongest_existing_absorber="abstract interpretation, lenses, why-not provenance, CSP explanation",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="common structure present; novelty mostly absorbed by source-fiber prior art",
        ),
        BranchWitness(
            branch="Provenance work",
            source_artifacts=("T55B", "T68", "T70", "T72", "T121"),
            state_held_fixed="same content, record, detector outcome, or colimit result",
            future_capability_changed="attribute, audit, certify, challenge, or trust the result",
            candidate_cause="identity, custody, ancestry, signed DAG, intervention metadata",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"identity_witness", "custody_log", "ancestry_dag"}),
                rights=frozenset({"audit", "attribute", "challenge"}),
                reconstruction_paths=frozenset({"lineage_replay"}),
                provenance=frozenset({"signed_dag", "origin_tags"}),
                maintenance=frozenset({"trust_boundary"}),
                access=frozenset({"provenance_visible"}),
                certifications=frozenset({"signature"}),
                task_policy=frozenset({"provenance_policy"}),
            ),
            strongest_existing_absorber="provenance systems",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="directly absorbed by provenance once provenance is included in state",
        ),
        BranchWitness(
            branch="Operation-right discussions",
            source_artifacts=("T115", "T117", "T119"),
            state_held_fixed="same archive/resource/checkpoint or same coarse state",
            future_capability_changed="challenge, appeal, sanction, repair, rollback",
            candidate_cause="authority, rights, public rules, challenge windows, quorum",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"audit_log", "rulebook", "challenge_window"}),
                rights=frozenset({"challenge", "appeal", "repair", "rollback"}),
                reconstruction_paths=frozenset({"appeal_path", "fraud_path"}),
                provenance=frozenset({"public_rule_record"}),
                maintenance=frozenset({"monitoring", "repair_budget"}),
                access=frozenset({"public_access"}),
                certifications=frozenset({"quorum"}),
                task_policy=frozenset({"governance_mechanism"}),
            ),
            strongest_existing_absorber="mechanism design, access control, commons governance",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="not a new object; rights-aware mechanism state absorbs it",
        ),
        BranchWitness(
            branch="ASP",
            source_artifacts=("T117",),
            state_held_fixed="same coarse entropy/information/finality/viability/reachability metrics",
            future_capability_changed="observer/task-indexed accessible future task set",
            candidate_cause="witnesses, rights, maintenance budget, reconstruction paths, certifications",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"task_witnesses"}),
                rights=frozenset({"task_rights"}),
                reconstruction_paths=frozenset({"task_reconstruction_paths"}),
                provenance=frozenset(),
                maintenance=frozenset({"maintenance_budget"}),
                access=frozenset({"observer_access"}),
                certifications=frozenset({"task_certifications"}),
                task_policy=frozenset({"task_universe"}),
            ),
            strongest_existing_absorber="enriched reachable-state analysis and opportunity-set economics",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="ASP is essentially the same audit normal form under a colliding name",
        ),
        BranchWitness(
            branch="FOA",
            source_artifacts=("T119",),
            state_held_fixed="same present/coarse state under matched ordinary measures",
            future_capability_changed="future operations available under witness/right/path/certification constraints",
            candidate_cause="explicit task-indexed operation requirements",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"operation_witnesses"}),
                rights=frozenset({"operation_rights"}),
                reconstruction_paths=frozenset({"operation_reconstruction_paths"}),
                provenance=frozenset({"operation_provenance"}),
                maintenance=frozenset({"operation_maintenance_budget"}),
                access=frozenset({"observer_access"}),
                certifications=frozenset({"operation_certifications"}),
                task_policy=frozenset({"operation_family"}),
            ),
            strongest_existing_absorber="enriched reachability/opportunity set",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="best internal label but still absorbed by established feasible-action formalisms",
        ),
        BranchWitness(
            branch="LossKernel",
            source_artifacts=("T99", "T107", "T108"),
            state_held_fixed="same endpoints, map behavior, and naive lost-label set",
            future_capability_changed="attribution, obstruction resolution, future repair/judgment",
            candidate_cause="source-anchored witness obligations, not label-only loss",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"source_anchor", "obstruction_resolver"}),
                rights=frozenset({"attribute", "repair"}),
                reconstruction_paths=frozenset({"source_preimage"}),
                provenance=frozenset({"projection_history"}),
                maintenance=frozenset(),
                access=frozenset({"source_fiber_access"}),
                certifications=frozenset(),
                task_policy=frozenset({"attribution_policy"}),
            ),
            strongest_existing_absorber="rich effects, abstract interpretation, lenses, why-not provenance",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="source-witness form fits the common object; novelty remains unearned",
        ),
        BranchWitness(
            branch="Admissibility",
            source_artifacts=("T31", "T32", "T78", "T87", "T121"),
            state_held_fixed="same candidate claim, projection, or raw evidence payload",
            future_capability_changed="whether the claim/evidence may be used later",
            candidate_cause="admissibility tokens, guard conditions, pre-registration, typed forgotten structure",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"admissibility_witnesses"}),
                rights=frozenset({"claim_use"}),
                reconstruction_paths=frozenset({"audit_path"}),
                provenance=frozenset({"pre_registration", "custody"}),
                maintenance=frozenset({"policy_stability"}),
                access=frozenset({"audit_access"}),
                certifications=frozenset({"tokens"}),
                task_policy=frozenset({"admissibility_policy"}),
            ),
            strongest_existing_absorber="evidence law/protocol logic/access-control systems",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="admissibility is a policy layer over future operations, not FCP itself",
        ),
        BranchWitness(
            branch="Maintenance-cost investigations",
            source_artifacts=("T114", "T115", "T128"),
            state_held_fixed="same standard entropy/control/stability/viability/storage metrics",
            future_capability_changed="maintained usability, repair, challenge, emergence-platform operation",
            candidate_cause="maintenance budget applied to witnesses, rights, repair paths, and record support",
            capability_structure=CapabilityStructure(
                witnesses=frozenset({"maintained_witnesses"}),
                rights=frozenset({"repair", "challenge"}),
                reconstruction_paths=frozenset({"repair_path"}),
                provenance=frozenset({"maintenance_log"}),
                maintenance=frozenset({"budget", "refresh_protocol"}),
                access=frozenset({"maintainer_access"}),
                certifications=frozenset({"maintenance_attestation"}),
                task_policy=frozenset({"viability_task_family"}),
            ),
            strongest_existing_absorber="viability kernels/control/resource accounting with enriched state",
            uniform_representation=True,
            superficial_state_difference=False,
            verdict="useful audit pattern; not independent of viability/control/resource frameworks",
        ),
    )


def prior_art_pressure() -> tuple[PriorArtPressure, ...]:
    return (
        PriorArtPressure(
            "reachability analysis",
            PriorArtVerdict.ABSORBS,
            "If the state includes witnesses, rights, access, provenance, and certificates, FCP is the reachable/action set.",
        ),
        PriorArtPressure(
            "viability kernels",
            PriorArtVerdict.ABSORBS,
            "Absorbs FCP when the viability condition is survival of the declared capability set over a horizon.",
        ),
        PriorArtPressure(
            "opportunity-set economics",
            PriorArtVerdict.ABSORBS,
            "Directly models feasible future opportunities under constraints and rights.",
        ),
        PriorArtPressure(
            "capability theory",
            PriorArtVerdict.PARTIAL,
            "Close conceptual neighbor for real opportunities, but less formal about witnesses and certifications.",
        ),
        PriorArtPressure(
            "mechanism design",
            PriorArtVerdict.ABSORBS,
            "Rights, admissible moves, incentives, challenge rules, and authority are native mechanism variables.",
        ),
        PriorArtPressure(
            "affordance theory",
            PriorArtVerdict.PARTIAL,
            "Captures agent-environment action possibilities but may omit formal proof/admissibility structure.",
        ),
        PriorArtPressure(
            "active inference policy spaces",
            PriorArtVerdict.ABSORBS,
            "Absorbs FCP if policies range over witness/right-bearing states and expected future actions.",
        ),
        PriorArtPressure(
            "reinforcement-learning action spaces",
            PriorArtVerdict.PARTIAL,
            "Captures executable actions but usually lacks provenance, certification, and challenge rights.",
        ),
        PriorArtPressure(
            "provenance systems",
            PriorArtVerdict.ABSORBS,
            "Directly captures lineage, custody, attribution, replay, and certification prerequisites.",
        ),
        PriorArtPressure(
            "access-control systems",
            PriorArtVerdict.ABSORBS,
            "Directly captures authorized operations over protected resources and evidence objects.",
        ),
        PriorArtPressure(
            "distributed-systems capability models",
            PriorArtVerdict.ABSORBS,
            "Capability tokens, leases, certificates, and quorum/challenge windows absorb many packet and consensus cases.",
        ),
    )


def finite_witness_table(
    witnesses: tuple[BranchWitness, ...],
) -> tuple[tuple[str, str, str, str], ...]:
    return tuple(
        (
            witness.branch,
            witness.state_held_fixed,
            witness.future_capability_changed,
            witness.candidate_cause,
        )
        for witness in witnesses
    )


def run_t129_analysis() -> T129Result:
    witnesses = branch_witnesses()
    prior_art = prior_art_pressure()
    common_structure_exists = all(witness.uniform_representation for witness in witnesses)
    reducible = all(item.verdict != PriorArtVerdict.MISSES_ONLY_IF_COARSE for item in prior_art)
    if not common_structure_exists:
        recommendation = Recommendation.REJECT
    elif reducible:
        recommendation = Recommendation.FORMALIZE
    else:
        recommendation = Recommendation.PRESERVE

    return T129Result(
        witnesses=witnesses,
        prior_art=prior_art,
        strongest_common_object=(
            "A task-indexed constrained capability structure over a visible "
            "state: operations plus requirements for witnesses, rights, "
            "reconstruction paths, provenance, maintenance/access, "
            "certifications, and an admissibility policy. It is an enriched "
            "state/action object, not a new physical primitive."
        ),
        weakest_point=(
            "Once the hidden structure is admitted into the state, the apparent "
            "same-state split disappears into standard enriched reachability, "
            "opportunity-set, provenance, access-control, mechanism-design, or "
            "viability machinery. Novelty survives only against coarse state "
            "descriptions, which is not enough."
        ),
        closest_prior_art=(
            "Enriched reachability and opportunity-set economics are closest at "
            "the abstract level. Provenance systems, access-control/capability "
            "systems, and mechanism design are closest for the evidence/rights "
            "cases. Viability kernels absorb the maintenance/horizon reading."
        ),
        strongest_separation_witness=(
            "T123 is the cleanest same-state witness: same raw payload, same "
            "immediate measurement result, and same coarse detector summary, "
            "but different packet wrappers remove certification, reconstruction, "
            "challenge, lineage, and claim-review operations."
        ),
        strongest_absorption_witness=(
            "The Git/history witness is the strongest absorption case: the "
            "endpoint tree is the same only under a deliberately coarse state. "
            "Version-control theory already treats branch history, merge base, "
            "and signed tags as operational state."
        ),
        recommendation=recommendation,
        recommendation_rationale=(
            "Formalize narrowly as an audit normal form named only provisionally "
            "as FCP. Do not promote. The structure explains the witness family, "
            "but it is reducible to existing enriched state/action frameworks."
        ),
        claim_impact_note=(
            "No core claim upgrade. FCP should be treated as a cross-domain "
            "diagnostic for missing witness/right/provenance/reconstruction "
            "state, not as a new ontology."
        ),
        finite_witness_table=finite_witness_table(witnesses),
        reducible_to_existing_frameworks=reducible,
        common_structure_exists=common_structure_exists,
    )


def t129_result_to_dict(result: T129Result) -> dict[str, object]:
    return {
        "witnesses": [_witness_to_dict(witness) for witness in result.witnesses],
        "prior_art": [
            {
                "framework": item.framework,
                "verdict": item.verdict.value,
                "reason": item.reason,
            }
            for item in result.prior_art
        ],
        "strongest_common_object": result.strongest_common_object,
        "weakest_point": result.weakest_point,
        "closest_prior_art": result.closest_prior_art,
        "strongest_separation_witness": result.strongest_separation_witness,
        "strongest_absorption_witness": result.strongest_absorption_witness,
        "recommendation": result.recommendation.value,
        "recommendation_rationale": result.recommendation_rationale,
        "claim_impact_note": result.claim_impact_note,
        "finite_witness_table": [
            {
                "witness": row[0],
                "state_held_fixed": row[1],
                "future_capability_changed": row[2],
                "candidate_cause": row[3],
            }
            for row in result.finite_witness_table
        ],
        "reducible_to_existing_frameworks": result.reducible_to_existing_frameworks,
        "common_structure_exists": result.common_structure_exists,
    }


def _witness_to_dict(witness: BranchWitness) -> dict[str, object]:
    return {
        "branch": witness.branch,
        "source_artifacts": list(witness.source_artifacts),
        "state_held_fixed": witness.state_held_fixed,
        "future_capability_changed": witness.future_capability_changed,
        "candidate_cause": witness.candidate_cause,
        "capability_structure": {
            "witnesses": sorted(witness.capability_structure.witnesses),
            "rights": sorted(witness.capability_structure.rights),
            "reconstruction_paths": sorted(
                witness.capability_structure.reconstruction_paths
            ),
            "provenance": sorted(witness.capability_structure.provenance),
            "maintenance": sorted(witness.capability_structure.maintenance),
            "access": sorted(witness.capability_structure.access),
            "certifications": sorted(witness.capability_structure.certifications),
            "task_policy": sorted(witness.capability_structure.task_policy),
            "components_present": sorted(
                witness.capability_structure.components_present()
            ),
        },
        "strongest_existing_absorber": witness.strongest_existing_absorber,
        "uniform_representation": witness.uniform_representation,
        "superficial_state_difference": witness.superficial_state_difference,
        "verdict": witness.verdict,
    }
