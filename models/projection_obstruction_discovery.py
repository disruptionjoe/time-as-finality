"""T35: Projection-Obstruction Discovery Engine.

This module turns the PO1 machinery into a small finite exploration engine.
It does not discover theorems and it does not use domain-specific examples.
It searches bounded families of D1RestrictionSystem pairs, enumerates total
and partial projection maps, classifies each projection with the T31
admissibility checker, reduces obstruction witnesses, and compares discovered
signatures against prior T27-T34 examples.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import combinations
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    global_section,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import (
    AdmissibilityCheck,
    check_admissibility,
)
from models.projection_obstruction_schema import ProjectionCase


SHAPES = (
    "empty",
    "consistent_chain",
    "triangle_obstruction",
    "square_obstruction",
    "local_failure",
)

CLASSIFICATIONS = (
    "admissible_po1",
    "boundary_non_definable",
    "shared_obstruction",
    "lossy_non_obstructing",
    "obstruction_removed",
    "trivial_local_failure",
    "outside_po1",
    "system_invalid",
)


@dataclass(frozen=True)
class GeneratedSystemSpec:
    name: str
    site_count: int
    shape: str
    profile_level: str
    system: D1RestrictionSystem


@dataclass(frozen=True)
class ProjectionCandidate:
    candidate_id: str
    richer_spec: GeneratedSystemSpec
    restricted_spec: GeneratedSystemSpec
    map_mode: str
    named_forgetting: bool
    case: ProjectionCase


@dataclass(frozen=True)
class MinimalWitness:
    candidate_id: str
    witness_type: str
    site_count: int
    patch_count: int
    patch_ids: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class DiscoveryClassification:
    candidate_id: str
    classification: str
    t31_verdict: str
    po1_evidence: bool
    ac_vector: dict[str, bool]
    signature: tuple[Any, ...]
    known_signature_match: bool
    minimal_witness: MinimalWitness
    interest_score: int
    interest_reason: str


@dataclass(frozen=True)
class DiscoverySummary:
    generated_system_count: int
    candidate_count: int
    classification_counts: dict[str, int]
    positive_candidates: tuple[str, ...]
    boundary_candidates: tuple[str, ...]
    minimal_counterexamples: tuple[str, ...]
    novel_positive_candidates: tuple[str, ...]
    rediscovered_known_pattern_count: int
    best_supported_hypothesis: str
    recommendation: str


@dataclass(frozen=True)
class T35Result:
    system_specs: tuple[GeneratedSystemSpec, ...]
    candidates: tuple[ProjectionCandidate, ...]
    classifications: tuple[DiscoveryClassification, ...]
    summary: DiscoverySummary
    known_signatures: tuple[tuple[Any, ...], ...]
    guardrails: tuple[str, ...]


class RestrictionSystemGenerator:
    """Generate small finite D1RestrictionSystem families without domain labels."""

    def generate(self) -> tuple[GeneratedSystemSpec, ...]:
        specs: list[GeneratedSystemSpec] = []
        for site_count in (3, 4):
            for shape in SHAPES:
                if shape == "square_obstruction" and site_count < 4:
                    continue
                for profile_level in ("high", "low"):
                    name = f"gen_{site_count}_{shape}_{profile_level}"
                    specs.append(
                        GeneratedSystemSpec(
                            name=name,
                            site_count=site_count,
                            shape=shape,
                            profile_level=profile_level,
                            system=_build_system(name, site_count, shape, _profile(profile_level)),
                        )
                    )
        return tuple(specs)


class ProjectionGenerator:
    """Enumerate candidate projections among generated systems."""

    def enumerate(
        self,
        specs: tuple[GeneratedSystemSpec, ...],
    ) -> tuple[ProjectionCandidate, ...]:
        candidates: list[ProjectionCandidate] = []
        high_specs = tuple(spec for spec in specs if spec.profile_level == "high")
        low_specs = tuple(spec for spec in specs if spec.profile_level == "low")
        index = 0
        for richer in high_specs:
            for restricted in low_specs:
                modes = ["partial"]
                if richer.site_count == restricted.site_count:
                    modes.insert(0, "total")
                for map_mode in modes:
                    if map_mode == "partial" and richer.site_count < 4:
                        continue
                    for named_forgetting in (True, False):
                        candidate_id = f"cand_{index:03d}"
                        case = _build_projection_case(
                            candidate_id,
                            richer,
                            restricted,
                            map_mode,
                            named_forgetting,
                        )
                        candidates.append(
                            ProjectionCandidate(
                                candidate_id=candidate_id,
                                richer_spec=richer,
                                restricted_spec=restricted,
                                map_mode=map_mode,
                                named_forgetting=named_forgetting,
                                case=case,
                            )
                        )
                        index += 1
        return tuple(candidates)


class AdmissibilityEvaluator:
    """Classify candidates with T31 plus structural discovery labels."""

    def classify(
        self,
        candidate: ProjectionCandidate,
        known_signatures: set[tuple[Any, ...]],
    ) -> DiscoveryClassification:
        check = check_admissibility(candidate.case)
        classification = _classification_for(candidate.case, check)
        signature = structural_signature(candidate.case, check)
        known = signature in known_signatures
        witness = CounterexampleReducer().reduce(candidate, classification)
        score, reason = _interest_score(candidate, classification, known, witness)
        return DiscoveryClassification(
            candidate_id=candidate.candidate_id,
            classification=classification,
            t31_verdict=check.verdict,
            po1_evidence=check.po1_evidence,
            ac_vector=_ac_vector(check),
            signature=signature,
            known_signature_match=known,
            minimal_witness=witness,
            interest_score=score,
            interest_reason=reason,
        )


class CounterexampleReducer:
    """Reduce generated cases to small finite witnesses."""

    def reduce(
        self,
        candidate: ProjectionCandidate,
        classification: str,
    ) -> MinimalWitness:
        restricted = candidate.case.restricted_system
        if classification in {"admissible_po1", "shared_obstruction"}:
            patch_ids = _minimal_obstruction_patch_ids(restricted)
            return MinimalWitness(
                candidate_id=candidate.candidate_id,
                witness_type="minimal_gluing_obstruction",
                site_count=len(restricted.site_ids()),
                patch_count=len(patch_ids),
                patch_ids=patch_ids,
                reason="smallest restricted patch subset that still has a finite gluing obstruction",
            )
        if classification == "boundary_non_definable":
            mapped_sources = {item.source_site for item in candidate.case.morphism.site_map}
            missing = tuple(site for site in candidate.case.richer_system.site_ids() if site not in mapped_sources)
            return MinimalWitness(
                candidate_id=candidate.candidate_id,
                witness_type="missing_site_map",
                site_count=len(missing),
                patch_count=0,
                patch_ids=missing,
                reason="projection is not definable because these source sites have no target",
            )
        if classification == "lossy_non_obstructing":
            return MinimalWitness(
                candidate_id=candidate.candidate_id,
                witness_type="minimal_loss_without_obstruction",
                site_count=len(restricted.site_ids()),
                patch_count=len(restricted.patches),
                patch_ids=tuple(patch.patch_id for patch in restricted.patches),
                reason="profiles are lossy but the restricted system still has a global section",
            )
        if classification == "obstruction_removed":
            return MinimalWitness(
                candidate_id=candidate.candidate_id,
                witness_type="obstruction_removed",
                site_count=len(restricted.site_ids()),
                patch_count=len(restricted.patches),
                patch_ids=tuple(patch.patch_id for patch in restricted.patches),
                reason="richer system is obstructed while restricted endpoint is globally satisfiable",
            )
        return MinimalWitness(
            candidate_id=candidate.candidate_id,
            witness_type="outside_po1",
            site_count=len(restricted.site_ids()),
            patch_count=len(restricted.patches),
            patch_ids=tuple(patch.patch_id for patch in restricted.patches),
            reason="candidate does not satisfy a discovery class with a smaller reducer",
        )


class ObstructionExplorer:
    """Run the bounded T35 discovery experiment."""

    def run(self) -> T35Result:
        specs = RestrictionSystemGenerator().generate()
        candidates = ProjectionGenerator().enumerate(specs)
        known = known_case_signatures()
        evaluator = AdmissibilityEvaluator()
        classifications = tuple(
            evaluator.classify(candidate, set(known))
            for candidate in candidates
        )
        return T35Result(
            system_specs=specs,
            candidates=candidates,
            classifications=classifications,
            summary=_summarize(specs, candidates, classifications),
            known_signatures=tuple(sorted(known, key=str)),
            guardrails=(
                "T35 does not claim automated theorem discovery.",
                "T35 uses no machine learning or statistical pattern recognition.",
                "T35 generated structures are mathematical candidates only.",
                "T35 uses generic finite restriction-system labels, not domain-specific heuristics.",
            ),
        )


def run_t35_discovery() -> T35Result:
    return ObstructionExplorer().run()


def run_t35_analysis() -> dict[str, Any]:
    result = run_t35_discovery()
    return {
        "summary": asdict(result.summary),
        "classification_examples": [
            _classification_to_dict(item)
            for item in sorted(result.classifications, key=lambda x: (-x.interest_score, x.candidate_id))[:16]
        ],
        "positive_candidates": [
            _classification_to_dict(item)
            for item in result.classifications
            if item.classification == "admissible_po1"
        ][:12],
        "boundary_candidates": [
            _classification_to_dict(item)
            for item in result.classifications
            if item.classification == "boundary_non_definable"
        ][:12],
        "minimal_counterexamples": [
            _classification_to_dict(item)
            for item in result.classifications
            if item.candidate_id in result.summary.minimal_counterexamples
        ],
        "novel_positive_candidates": [
            _classification_to_dict(item)
            for item in result.classifications
            if item.candidate_id in result.summary.novel_positive_candidates
        ],
        "known_signature_count": len(result.known_signatures),
        "guardrails": list(result.guardrails),
    }


def known_case_signatures() -> set[tuple[Any, ...]]:
    """Collect structural signatures from T27-T34 examples."""
    known: set[tuple[Any, ...]] = set()
    try:
        from models.po1_admissibility_conditions import _t31_cases

        for case in _t31_cases():
            known.add(structural_signature(case, check_admissibility(case)))
    except Exception:
        pass

    try:
        from models.po1_chained_projection import run_t34_analysis

        t34 = run_t34_analysis()
        for chain in (t34.spectre_chain, t34.stepwise_chain, t34.absorbed_chain):
            known.add(
                structural_signature(
                    chain.chain.endpoint_case,
                    chain.chain.endpoint_admissibility,
                )
            )
    except Exception:
        pass
    return known


def structural_signature(
    case: ProjectionCase,
    check: AdmissibilityCheck,
) -> tuple[Any, ...]:
    rich = global_section(case.richer_system)
    restricted = global_section(case.restricted_system)
    return (
        len(case.richer_system.site_ids()),
        len(case.restricted_system.site_ids()),
        len(case.richer_system.patches),
        len(case.restricted_system.patches),
        rich.obstruction_detected,
        restricted.obstruction_detected,
        check.ac3_projection_definable,
        check.ac5_structure_forgotten,
        _constraint_shape(case.restricted_system),
        check.verdict,
    )


def _build_projection_case(
    candidate_id: str,
    richer: GeneratedSystemSpec,
    restricted: GeneratedSystemSpec,
    map_mode: str,
    named_forgetting: bool,
) -> ProjectionCase:
    site_map = _site_map(richer.system, restricted.system, map_mode)
    morphism = D1RestrictionMorphism(
        name=f"{candidate_id}_projection",
        source=richer.system,
        target=restricted.system,
        site_map=site_map,
        preserved_dimensions=("accessible_support",),
        require_trust_path_preservation=True,
        require_obstruction_preservation=False,
    )
    forgotten = (
        (
            f"generic_resolution_data:{richer.shape}->{restricted.shape}",
            "generic_profile_detail",
        )
        if named_forgetting
        else ()
    )
    return ProjectionCase(
        name=f"{candidate_id}_{richer.shape}_to_{restricted.shape}_{map_mode}",
        source="T35_generated",
        richer_system=richer.system,
        restricted_system=restricted.system,
        morphism=morphism,
        forgotten_structure=forgotten,
        preserved_structure=("finite_site_order",),
        intended_reading="bounded structural discovery candidate; no domain interpretation",
    )


def _build_system(
    name: str,
    site_count: int,
    shape: str,
    profile: D1Profile,
) -> D1RestrictionSystem:
    sites = tuple(f"{name}_S{i}" for i in range(site_count))
    patches = _patches_for_shape(name, sites, shape)
    return D1RestrictionSystem(
        name=name,
        proposition="generated_record",
        local_values=tuple(_local(site_id, name, profile) for site_id in sites),
        transport_edges=tuple(
            TransportEdge(sites[i], sites[i + 1], f"edge_{i}_{i + 1}")
            for i in range(site_count - 1)
        ),
        source_site=sites[0],
        target_site=sites[-1],
        patches=patches,
    )


def _patches_for_shape(
    prefix: str,
    sites: tuple[str, ...],
    shape: str,
) -> tuple[RestrictionPatch, ...]:
    variables = tuple(chr(ord("a") + i) for i in range(len(sites)))

    def patch(idx: int, left: int, right: int, relation: str) -> RestrictionPatch:
        return RestrictionPatch(
            f"{prefix}_p{idx}_{variables[left]}_{relation}_{variables[right]}",
            (sites[left], sites[right]),
            (variables[left], variables[right]),
            (PatchConstraint(variables[left], variables[right], relation),),
        )

    if shape == "empty":
        return ()
    if shape == "consistent_chain":
        return tuple(patch(i, i, i + 1, "same") for i in range(len(sites) - 1))
    if shape == "triangle_obstruction":
        return (
            patch(0, 0, 1, "same"),
            patch(1, 1, 2, "same"),
            patch(2, 0, 2, "different"),
        )
    if shape == "square_obstruction":
        return (
            patch(0, 0, 1, "same"),
            patch(1, 1, 2, "same"),
            patch(2, 2, 3, "same"),
            patch(3, 0, 3, "different"),
        )
    if shape == "local_failure":
        return (
            RestrictionPatch(
                f"{prefix}_p0_local_failure",
                (sites[0], sites[1]),
                (variables[0], variables[1]),
                (
                    PatchConstraint(variables[0], variables[1], "same"),
                    PatchConstraint(variables[0], variables[1], "different"),
                ),
            ),
        )
    raise ValueError(f"unknown generated shape: {shape}")


def _profile(level: str) -> D1Profile:
    if level == "high":
        return D1Profile(4, 4, 2, 4)
    if level == "low":
        return D1Profile(1, 1, 0, 1)
    raise ValueError(f"unknown profile level: {level}")


def _local(site_id: str, tag: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(
        site=ObserverSite(site_id, "generated", "finite_site", 0, tag),
        proposition_value="true",
        profile=profile,
    )


def _site_map(
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
    map_mode: str,
) -> tuple[SiteMap, ...]:
    source_sites = source.site_ids()
    target_sites = target.site_ids()
    count = min(len(source_sites), len(target_sites))
    if map_mode == "partial":
        count = max(0, count - 1)
    return tuple(SiteMap(source_sites[i], target_sites[i]) for i in range(count))


def _classification_for(
    case: ProjectionCase,
    check: AdmissibilityCheck,
) -> str:
    rich = global_section(case.richer_system)
    restricted = global_section(case.restricted_system)
    if not check.ac1_richer_valid or not check.ac2_restricted_valid:
        return "system_invalid"
    if not check.ac3_projection_definable:
        return "boundary_non_definable"
    if not check.ac4_local_compat:
        return "trivial_local_failure"
    if check.po1_evidence:
        return "admissible_po1"
    if rich.obstruction_detected and restricted.obstruction_detected:
        return "shared_obstruction"
    if rich.obstruction_detected and not restricted.obstruction_detected:
        return "obstruction_removed"
    if check.ac5_structure_forgotten and not restricted.obstruction_detected:
        return "lossy_non_obstructing"
    return "outside_po1"


def _minimal_obstruction_patch_ids(system: D1RestrictionSystem) -> tuple[str, ...]:
    if not global_section(system).obstruction_detected:
        return ()
    patches = system.patches
    for size in range(1, len(patches) + 1):
        for subset in combinations(patches, size):
            reduced = D1RestrictionSystem(
                name=f"{system.name}_reduced",
                proposition=system.proposition,
                local_values=system.local_values,
                transport_edges=system.transport_edges,
                source_site=system.source_site,
                target_site=system.target_site,
                patches=tuple(subset),
                overlap_tests=system.overlap_tests,
            )
            if global_section(reduced).obstruction_detected:
                return tuple(patch.patch_id for patch in subset)
    return tuple(patch.patch_id for patch in patches)


def _constraint_shape(system: D1RestrictionSystem) -> tuple[str, ...]:
    return tuple(
        sorted(
            f"{len(patch.site_ids)}:{len(patch.constraints)}:"
            + ",".join(constraint.relation for constraint in patch.constraints)
            for patch in system.patches
        )
    )


def _ac_vector(check: AdmissibilityCheck) -> dict[str, bool]:
    return {
        "AC1": check.ac1_richer_valid,
        "AC2": check.ac2_restricted_valid,
        "AC3": check.ac3_projection_definable,
        "AC4": check.ac4_local_compat,
        "AC5": check.ac5_structure_forgotten,
        "AC6": check.ac6_restricted_obstructed,
        "AC7": check.ac7_richer_unobstructed,
    }


def _interest_score(
    candidate: ProjectionCandidate,
    classification: str,
    known: bool,
    witness: MinimalWitness,
) -> tuple[int, str]:
    score = 0
    reasons: list[str] = []
    if classification == "admissible_po1":
        score += 5
        reasons.append("positive PO1 candidate")
    if classification == "boundary_non_definable":
        score += 3
        reasons.append("non-definable boundary")
    if classification in {"lossy_non_obstructing", "obstruction_removed"}:
        score += 2
        reasons.append("minimal counterexample class")
    if not known:
        score += 3
        reasons.append("signature not present in T27-T34 comparison set")
    if witness.patch_count >= 4:
        score += 2
        reasons.append("requires at least four restricted patches")
    if not candidate.named_forgetting:
        score -= 1
        reasons.append("unnamed forgetting weakens PO1 relevance")
    return score, "; ".join(reasons) if reasons else "low structural interest"


def _summarize(
    specs: tuple[GeneratedSystemSpec, ...],
    candidates: tuple[ProjectionCandidate, ...],
    classifications: tuple[DiscoveryClassification, ...],
) -> DiscoverySummary:
    counts = {classification: 0 for classification in CLASSIFICATIONS}
    for item in classifications:
        counts[item.classification] = counts.get(item.classification, 0) + 1

    positive = tuple(item.candidate_id for item in classifications if item.classification == "admissible_po1")
    boundary = tuple(item.candidate_id for item in classifications if item.classification == "boundary_non_definable")
    minimal_counterexamples = tuple(
        item.candidate_id
        for item in classifications
        if item.classification in {"lossy_non_obstructing", "obstruction_removed"}
    )
    novel_positive = tuple(
        item.candidate_id
        for item in classifications
        if item.classification == "admissible_po1" and not item.known_signature_match
    )
    rediscovered = sum(
        1
        for item in classifications
        if item.classification == "admissible_po1" and item.known_signature_match
    )

    if novel_positive:
        hypothesis = "H2 with H3 caution"
        recommendation = (
            "The finite framework is generative: T35 rediscovers known PO1 signatures "
            "and produces structurally novel positive candidates, including bounded "
            "four-patch obstruction witnesses. Many candidates are redundant, so the "
            "engine should be used as a triage tool for human mathematical analysis, "
            "not as theorem discovery."
        )
    elif positive:
        hypothesis = "H1"
        recommendation = (
            "The engine rediscovers known PO1 patterns but does not yet produce "
            "structurally novel candidates. Richer generators or invariants are needed."
        )
    else:
        hypothesis = "H0"
        recommendation = (
            "The bounded engine did not find positive PO1 cases. Current generative "
            "value is weak under this search space."
        )

    return DiscoverySummary(
        generated_system_count=len(specs),
        candidate_count=len(candidates),
        classification_counts=counts,
        positive_candidates=positive[:12],
        boundary_candidates=boundary[:12],
        minimal_counterexamples=minimal_counterexamples[:12],
        novel_positive_candidates=novel_positive[:12],
        rediscovered_known_pattern_count=rediscovered,
        best_supported_hypothesis=hypothesis,
        recommendation=recommendation,
    )


def _classification_to_dict(item: DiscoveryClassification) -> dict[str, Any]:
    return {
        "candidate_id": item.candidate_id,
        "classification": item.classification,
        "t31_verdict": item.t31_verdict,
        "po1_evidence": item.po1_evidence,
        "ac_vector": item.ac_vector,
        "known_signature_match": item.known_signature_match,
        "minimal_witness": asdict(item.minimal_witness),
        "interest_score": item.interest_score,
        "interest_reason": item.interest_reason,
    }
