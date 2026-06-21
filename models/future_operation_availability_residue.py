"""T119: Future Operation Availability residue audit.

This audit asks whether repeated residues across Q1A, ASP, LossKernel,
reconstruction debt, maintenance, provenance, and admissibility work are
actually the same object.

The candidate object is Future Operation Availability (FOA): the observer- and
task-indexed set of future operations that remain admissible, executable,
reconstructable, certifiable, challengeable, maintainable, or otherwise
available. The audit assumes absorption by existing frameworks until a finite
separation is demonstrated.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class FOARelation(Enum):
    STRONG = "strong"
    WEAK = "weak"
    NONE = "none"


class PriorArtVerdict(Enum):
    ABSORBS = "absorbs"
    PARTIAL = "partial"
    MISSES_COARSE = "misses_coarse"


@dataclass(frozen=True)
class BranchResidueAudit:
    branch: str
    collapsed: str
    survived: str
    involves_foa: FOARelation
    expressible_without_foa: bool
    recurrence_verdict: str


@dataclass(frozen=True)
class PriorArtPressure:
    target: str
    verdict: PriorArtVerdict
    reason: str


@dataclass(frozen=True)
class ExistingMeasures:
    entropy_bits: int
    information_bits: int
    finality_score: int
    viability_score: int
    coarse_reachable_count: int
    control_rank: int
    persistence_horizon: int


@dataclass(frozen=True)
class FOAState:
    witnesses: frozenset[str]
    rights: frozenset[str]
    reconstruction_paths: frozenset[str]
    certifications: frozenset[str]
    maintenance_budget: int


@dataclass(frozen=True)
class Operation:
    name: str
    required_witnesses: frozenset[str]
    required_rights: frozenset[str]
    required_reconstruction_paths: frozenset[str]
    required_certifications: frozenset[str]
    required_maintenance: int


@dataclass(frozen=True)
class FiniteSystem:
    system_id: str
    measures: ExistingMeasures
    foa_state: FOAState


@dataclass(frozen=True)
class FiniteExample:
    example_id: str
    purpose: str
    system_a: FiniteSystem
    system_b: FiniteSystem
    operations: tuple[Operation, ...]
    existing_measures_equal: bool
    existing_measures_differ: bool
    foa_a: frozenset[str]
    foa_b: frozenset[str]
    foa_differs: bool
    foa_collapses_into_existing_framework: bool
    verdict: str


@dataclass(frozen=True)
class T119Result:
    branch_audits: tuple[BranchResidueAudit, ...]
    prior_art_pressure: tuple[PriorArtPressure, ...]
    finite_examples: tuple[FiniteExample, ...]
    strongest_version: str
    weakest_point: str
    closest_prior_art: str
    best_finite_witness: str
    strongest_absorption_argument: str
    strongest_separation_argument: str
    recommendation: str
    chain_supported: bool
    chain_verdict: str
    claim_ledger_update: str


def accessible_operations(system: FiniteSystem, operations: tuple[Operation, ...]) -> frozenset[str]:
    return frozenset(
        operation.name
        for operation in operations
        if operation.required_witnesses <= system.foa_state.witnesses
        and operation.required_rights <= system.foa_state.rights
        and operation.required_reconstruction_paths <= system.foa_state.reconstruction_paths
        and operation.required_certifications <= system.foa_state.certifications
        and operation.required_maintenance <= system.foa_state.maintenance_budget
    )


def branch_audits() -> tuple[BranchResidueAudit, ...]:
    return (
        BranchResidueAudit(
            branch="Q1A",
            collapsed=(
                "Branch support and reversal cost collapsed inside the fixed-data "
                "family; provenance-aware Darwinism absorbed the strongest witness."
            ),
            survived=(
                "Audited accessible provenance-class support plus partition visibility."
            ),
            involves_foa=FOARelation.WEAK,
            expressible_without_foa=True,
            recurrence_verdict=(
                "Weak convergence only: Q1A preserves availability of certified "
                "records, not a full future action set unless a task family is added."
            ),
        ),
        BranchResidueAudit(
            branch="ASP",
            collapsed=(
                "Replacement-primitive and scalar future-opportunity readings collapsed."
            ),
            survived=(
                "Observer/task-indexed admissible future operation set under witnesses, "
                "rights, reconstruction paths, maintenance budget, and certifications."
            ),
            involves_foa=FOARelation.STRONG,
            expressible_without_foa=False,
            recurrence_verdict=(
                "Direct convergence: ASP is essentially FOA under a different name."
            ),
        ),
        BranchResidueAudit(
            branch="Reconstruction debt",
            collapsed=(
                "General lost-information conservation language collapsed."
            ),
            survived=(
                "Missing source witnesses matter when later reconstruction, judgment, "
                "or admissibility depends on them."
            ),
            involves_foa=FOARelation.STRONG,
            expressible_without_foa=True,
            recurrence_verdict=(
                "Structural convergence: debt is the obstruction-side account of "
                "operations no longer reconstructable or certifiable."
            ),
        ),
        BranchResidueAudit(
            branch="Maintenance cost",
            collapsed=(
                "Independent maintenance-cost theory collapsed into provenance, "
                "commons, viability, and reconstruction-debt language."
            ),
            survived=(
                "Maintained witnesses, authority, and repair paths that preserve "
                "future operation rights."
            ),
            involves_foa=FOARelation.STRONG,
            expressible_without_foa=True,
            recurrence_verdict=(
                "Structural convergence, but absorbable by task-enriched viability "
                "or control state."
            ),
        ),
        BranchResidueAudit(
            branch="Provenance",
            collapsed=(
                "Provenance as a first-class event-finality primitive collapsed for "
                "plain colimit, AM, and descent reconstruction."
            ),
            survived=(
                "Audit, identity, custody, attribution, and admissibility evidence."
            ),
            involves_foa=FOARelation.STRONG,
            expressible_without_foa=True,
            recurrence_verdict=(
                "Structural convergence only when future operations require trust, "
                "identity, challenge, or certification."
            ),
        ),
        BranchResidueAudit(
            branch="LossKernel",
            collapsed=(
                "Label-only LossKernel and novelty over rich prior art collapsed."
            ),
            survived=(
                "Source-anchored witness obligations for projection-created judgments."
            ),
            involves_foa=FOARelation.STRONG,
            expressible_without_foa=True,
            recurrence_verdict=(
                "Structural convergence: typed loss matters when projected targets "
                "lose future judgments or repair operations."
            ),
        ),
        BranchResidueAudit(
            branch="Admissibility",
            collapsed=(
                "Seven independent empirical admissibility conditions collapsed to a "
                "smaller structural checklist plus semantic AC5."
            ),
            survived=(
                "A rule for which projections, witnesses, or claims are admissible "
                "as future evidence."
            ),
            involves_foa=FOARelation.STRONG,
            expressible_without_foa=True,
            recurrence_verdict=(
                "Converges at the evidence-protocol layer: admissibility is not FOA, "
                "but it determines which future claims/actions are permitted."
            ),
        ),
    )


def prior_art_pressure() -> tuple[PriorArtPressure, ...]:
    return (
        PriorArtPressure(
            "viability kernels",
            PriorArtVerdict.ABSORBS,
            "Absorbs FOA when the viability set is defined over future task availability under constraints.",
        ),
        PriorArtPressure(
            "reachability analysis",
            PriorArtVerdict.ABSORBS,
            "Absorbs FOA when state includes witnesses, rights, certificates, and reconstruction paths.",
        ),
        PriorArtPressure(
            "affordance landscapes",
            PriorArtVerdict.PARTIAL,
            "Captures available actions for an agent-environment pair, but often omits formal certification and admissibility tokens.",
        ),
        PriorArtPressure(
            "active inference policy spaces",
            PriorArtVerdict.ABSORBS,
            "Absorbs FOA if policies range over witness/right-bearing future states.",
        ),
        PriorArtPressure(
            "reinforcement-learning action spaces",
            PriorArtVerdict.PARTIAL,
            "Captures executable actions, but ordinary RL action sets do not encode reconstruction, certification, or challenge rights by default.",
        ),
        PriorArtPressure(
            "opportunity-set economics",
            PriorArtVerdict.ABSORBS,
            "Directly captures FOA as feasible opportunity set once rights and constraints are included.",
        ),
        PriorArtPressure(
            "capability theory",
            PriorArtVerdict.PARTIAL,
            "Close conceptual neighbor: real freedoms/capabilities, but less formal about witness debt and certification.",
        ),
        PriorArtPressure(
            "mechanism design",
            PriorArtVerdict.ABSORBS,
            "Absorbs operation rights, incentives, admissible moves, challenge rules, and authority.",
        ),
        PriorArtPressure(
            "commons governance",
            PriorArtVerdict.ABSORBS,
            "Absorbs monitoring, sanctioning, repair, public rules, and challenge authority in governance examples.",
        ),
        PriorArtPressure(
            "control theory",
            PriorArtVerdict.ABSORBS,
            "Absorbs FOA when the controlled state and admissible controls include record and authority variables.",
        ),
    )


def finite_examples() -> tuple[FiniteExample, ...]:
    examples = (
        _example_a_foa_differs_measures_do_not(),
        _example_b_measures_differ_foa_does_not(),
        _example_c_foa_absorbed_by_reachability(),
    )
    return tuple(_score_example(example) for example in examples)


def run_t119_analysis() -> T119Result:
    branches = branch_audits()
    examples = finite_examples()
    chain_supported = all(
        _branch_chain_support(branch)
        for branch in branches
        if branch.branch
        in {"ASP", "Reconstruction debt", "Maintenance cost", "Provenance", "LossKernel"}
    )
    return T119Result(
        branch_audits=branches,
        prior_art_pressure=prior_art_pressure(),
        finite_examples=examples,
        strongest_version=(
            "FOA is a prespecified observer/task/horizon-indexed set of future "
            "operations available under witness, right, reconstruction, "
            "certification, and maintenance constraints."
        ),
        weakest_point=(
            "FOA is almost entirely absorbable by enriched reachability, "
            "opportunity-set, viability, control, mechanism-design, and provenance "
            "frameworks. It becomes new only if those frameworks are kept coarse, "
            "which is not a legitimate novelty claim."
        ),
        closest_prior_art=(
            "Enriched reachability analysis and opportunity-set economics are the "
            "closest formal homes; provenance and mechanism design are the closest "
            "homes for certification, authority, and challenge rights."
        ),
        best_finite_witness=(
            "Example A: same endpoint repository state and matched coarse metrics, "
            "but retained merge-base, branch-history, and signed-history witnesses "
            "change FOA from {build} to {build, merge, revert, bisect}."
        ),
        strongest_absorption_argument=(
            "Once witnesses, rights, certificates, maintenance budgets, and "
            "reconstruction paths are included in the state, FOA is just the "
            "feasible action/reachability/opportunity set."
        ),
        strongest_separation_argument=(
            "Against coarse metrics, FOA separates cases where entropy, information, "
            "finality, viability, persistence, coarse reachability, and control rank "
            "all match but future admissible operations differ."
        ),
        recommendation=(
            "Preserve and formalize narrowly as a cross-branch audit normal form. "
            "Do not promote as a new primitive or independent physical object."
        ),
        chain_supported=chain_supported,
        chain_verdict=(
            "The lost-structure -> reconstruction-debt -> reduced-operation-rights "
            "-> reduced-FOA chain is structurally present in ASP, reconstruction "
            "debt, maintenance, provenance, and LossKernel, but Q1A only joins after "
            "adding a task/certification reading to accessible support."
        ),
        claim_ledger_update=(
            "No core claim upgrade. Add T119 as a synthesis audit: multiple branches "
            "converge on observer/task-indexed future operation availability as a "
            "useful normal form, but the object is absorbed by enriched reachability, "
            "opportunity-set, viability/control, provenance, commons governance, and "
            "mechanism-design frameworks. Preserve narrowly; do not promote."
        ),
    )


def t119_result_to_dict(result: T119Result) -> dict[str, object]:
    return {
        "branch_audits": [
            {
                "branch": audit.branch,
                "collapsed": audit.collapsed,
                "survived": audit.survived,
                "involves_foa": audit.involves_foa.value,
                "expressible_without_foa": audit.expressible_without_foa,
                "recurrence_verdict": audit.recurrence_verdict,
            }
            for audit in result.branch_audits
        ],
        "prior_art_pressure": [
            {
                "target": item.target,
                "verdict": item.verdict.value,
                "reason": item.reason,
            }
            for item in result.prior_art_pressure
        ],
        "finite_examples": [_example_to_dict(example) for example in result.finite_examples],
        "strongest_version": result.strongest_version,
        "weakest_point": result.weakest_point,
        "closest_prior_art": result.closest_prior_art,
        "best_finite_witness": result.best_finite_witness,
        "strongest_absorption_argument": result.strongest_absorption_argument,
        "strongest_separation_argument": result.strongest_separation_argument,
        "recommendation": result.recommendation,
        "chain_supported": result.chain_supported,
        "chain_verdict": result.chain_verdict,
        "claim_ledger_update": result.claim_ledger_update,
    }


def _branch_chain_support(branch: BranchResidueAudit) -> bool:
    text = f"{branch.collapsed} {branch.survived} {branch.recurrence_verdict}".lower()
    return (
        branch.involves_foa == FOARelation.STRONG
        and any(term in text for term in ("witness", "structure", "provenance"))
        and any(term in text for term in ("operation", "judgment", "admissibility", "rights"))
    )


def _score_example(example: FiniteExample) -> FiniteExample:
    foa_a = accessible_operations(example.system_a, example.operations)
    foa_b = accessible_operations(example.system_b, example.operations)
    return FiniteExample(
        example_id=example.example_id,
        purpose=example.purpose,
        system_a=example.system_a,
        system_b=example.system_b,
        operations=example.operations,
        existing_measures_equal=example.system_a.measures == example.system_b.measures,
        existing_measures_differ=example.system_a.measures != example.system_b.measures,
        foa_a=foa_a,
        foa_b=foa_b,
        foa_differs=foa_a != foa_b,
        foa_collapses_into_existing_framework=example.foa_collapses_into_existing_framework,
        verdict=example.verdict,
    )


def _example_a_foa_differs_measures_do_not() -> FiniteExample:
    measures = ExistingMeasures(8, 8, 4, 4, 4, 3, 10)
    operations = (
        Operation("build", frozenset({"tree"}), frozenset({"read"}), frozenset(), frozenset(), 1),
        Operation(
            "merge",
            frozenset({"tree", "merge_base"}),
            frozenset({"merge"}),
            frozenset({"history_path"}),
            frozenset({"signed_history"}),
            2,
        ),
        Operation(
            "revert",
            frozenset({"tree", "branch_history"}),
            frozenset({"revert"}),
            frozenset({"history_path"}),
            frozenset({"signed_history"}),
            2,
        ),
        Operation(
            "bisect",
            frozenset({"tree", "branch_history"}),
            frozenset({"bisect"}),
            frozenset({"history_path"}),
            frozenset(),
            1,
        ),
    )
    rich = FiniteSystem(
        "history_preserved_repo",
        measures,
        FOAState(
            witnesses=frozenset({"tree", "merge_base", "branch_history"}),
            rights=frozenset({"read", "merge", "revert", "bisect"}),
            reconstruction_paths=frozenset({"history_path"}),
            certifications=frozenset({"signed_history"}),
            maintenance_budget=2,
        ),
    )
    poor = FiniteSystem(
        "squashed_snapshot_repo",
        measures,
        FOAState(
            witnesses=frozenset({"tree"}),
            rights=frozenset({"read"}),
            reconstruction_paths=frozenset(),
            certifications=frozenset(),
            maintenance_budget=2,
        ),
    )
    return FiniteExample(
        "A_foa_differs_existing_measures_do_not",
        "FOA differs while existing measures do not.",
        rich,
        poor,
        operations,
        False,
        False,
        frozenset(),
        frozenset(),
        False,
        False,
        "Strong finite separation against coarse metrics.",
    )


def _example_b_measures_differ_foa_does_not() -> FiniteExample:
    operations = (
        Operation("read", frozenset({"record"}), frozenset({"read"}), frozenset(), frozenset(), 1),
        Operation("repair", frozenset({"record", "checksum"}), frozenset({"repair"}), frozenset(), frozenset(), 1),
    )
    system_a = FiniteSystem(
        "compressed_archive",
        ExistingMeasures(4, 8, 3, 4, 2, 2, 10),
        FOAState(
            witnesses=frozenset({"record", "checksum"}),
            rights=frozenset({"read", "repair"}),
            reconstruction_paths=frozenset(),
            certifications=frozenset(),
            maintenance_budget=1,
        ),
    )
    system_b = FiniteSystem(
        "redundant_archive",
        ExistingMeasures(12, 10, 5, 5, 4, 3, 20),
        FOAState(
            witnesses=frozenset({"record", "checksum"}),
            rights=frozenset({"read", "repair"}),
            reconstruction_paths=frozenset(),
            certifications=frozenset(),
            maintenance_budget=1,
        ),
    )
    return FiniteExample(
        "B_existing_measures_differ_foa_does_not",
        "Existing measures differ while FOA does not.",
        system_a,
        system_b,
        operations,
        False,
        False,
        frozenset(),
        frozenset(),
        False,
        False,
        "FOA is not just entropy, information, finality, viability, reachability, or persistence.",
    )


def _example_c_foa_absorbed_by_reachability() -> FiniteExample:
    measures = ExistingMeasures(9, 9, 4, 4, 5, 4, 12)
    operations = (
        Operation("accept", frozenset({"checkpoint"}), frozenset({"accept"}), frozenset(), frozenset(), 1),
        Operation(
            "challenge",
            frozenset({"checkpoint", "validator_signatures"}),
            frozenset({"challenge"}),
            frozenset({"fraud_path"}),
            frozenset({"challenge_window"}),
            1,
        ),
        Operation(
            "rollback",
            frozenset({"checkpoint", "fraud_proof"}),
            frozenset({"rollback"}),
            frozenset({"fraud_path"}),
            frozenset({"challenge_window"}),
            2,
        ),
    )
    rich = FiniteSystem(
        "enriched_reachability_state",
        measures,
        FOAState(
            witnesses=frozenset({"checkpoint", "validator_signatures", "fraud_proof"}),
            rights=frozenset({"accept", "challenge", "rollback"}),
            reconstruction_paths=frozenset({"fraud_path"}),
            certifications=frozenset({"challenge_window"}),
            maintenance_budget=2,
        ),
    )
    poor = FiniteSystem(
        "expired_challenge_state",
        measures,
        FOAState(
            witnesses=frozenset({"checkpoint"}),
            rights=frozenset({"accept"}),
            reconstruction_paths=frozenset(),
            certifications=frozenset(),
            maintenance_budget=2,
        ),
    )
    return FiniteExample(
        "C_foa_collapses_into_enriched_reachability",
        "FOA collapses entirely into enriched reachable action states.",
        rich,
        poor,
        operations,
        False,
        False,
        frozenset(),
        frozenset(),
        False,
        True,
        "Absorption control: enriched reachability computes the same operation set as FOA.",
    )


def _example_to_dict(example: FiniteExample) -> dict[str, object]:
    return {
        "example_id": example.example_id,
        "purpose": example.purpose,
        "system_a": _system_to_dict(example.system_a),
        "system_b": _system_to_dict(example.system_b),
        "operations": [operation.name for operation in example.operations],
        "existing_measures_equal": example.existing_measures_equal,
        "existing_measures_differ": example.existing_measures_differ,
        "foa_a": sorted(example.foa_a),
        "foa_b": sorted(example.foa_b),
        "foa_differs": example.foa_differs,
        "foa_collapses_into_existing_framework": (
            example.foa_collapses_into_existing_framework
        ),
        "verdict": example.verdict,
    }


def _system_to_dict(system: FiniteSystem) -> dict[str, object]:
    return {
        "system_id": system.system_id,
        "measures": {
            "entropy_bits": system.measures.entropy_bits,
            "information_bits": system.measures.information_bits,
            "finality_score": system.measures.finality_score,
            "viability_score": system.measures.viability_score,
            "coarse_reachable_count": system.measures.coarse_reachable_count,
            "control_rank": system.measures.control_rank,
            "persistence_horizon": system.measures.persistence_horizon,
        },
        "foa_state": {
            "witnesses": sorted(system.foa_state.witnesses),
            "rights": sorted(system.foa_state.rights),
            "reconstruction_paths": sorted(system.foa_state.reconstruction_paths),
            "certifications": sorted(system.foa_state.certifications),
            "maintenance_budget": system.foa_state.maintenance_budget,
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t119_result_to_dict(run_t119_analysis()), indent=2))
