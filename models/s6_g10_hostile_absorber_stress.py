"""G10: hostile absorber stress test for S6.

This audit tries to absorb the S6 sheafification bridge into standard
neighbors after the G6-G9 witness sequence:

  G6: density-matrix controlled-rotation bridge
  G7: SBS-style objectivity approximation
  G8: finite associated-record / descent engine
  G9: same final record, different presheaf capability pair

The result is deliberately conservative. If every standard neighbor can own the
mechanism it normally owns, S6 is left only as a typed bridge workflow:
declare local data, declare projection, compute associated record, account for
loss, and state the first obstruction.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.s6_g6_density_matrix_bridge import run_g6_density_matrix_bridge
from models.s6_g7_sbs_approximation import run_g7_sbs_approximation
from models.s6_g8_finite_sheaf_engine import run_g8_finite_sheaf_engine
from models.s6_g9_same_final_record_pair import run_g9_same_final_record_pair


@dataclass(frozen=True)
class AbsorberChallenge:
    absorber: str
    owns: tuple[str, ...]
    evidence: tuple[str, ...]
    status: str
    s6_residue: str
    reopen_burden: str
    promotes_s6_claim: bool


def run_g10_hostile_absorber_stress() -> dict[str, Any]:
    sources = {
        "G6": run_g6_density_matrix_bridge(),
        "G7": run_g7_sbs_approximation(),
        "G8": run_g8_finite_sheaf_engine(),
        "G9": run_g9_same_final_record_pair(),
    }
    challenges = absorber_challenges(sources)
    all_absorbers_granted = all(
        challenge.status == "granted" for challenge in challenges
    )
    any_claim_promoted = any(challenge.promotes_s6_claim for challenge in challenges)
    residue = surviving_residue(challenges)
    checks = {
        "source_witnesses_pass": all(
            bool(source["all_checks_passed"]) for source in sources.values()
        ),
        "g7_grants_qd_sbs_absorber": (
            sources["G7"]["absorber_verdict"]["Quantum_Darwinism_or_SBS"]
            == "granted_as_neighbor_absorber"
        ),
        "g8_not_general_sheafification": "not a general sheafification theorem"
        in sources["G8"]["guardrail"],
        "g9_not_quantum_separation": "not a new quantum separation theorem"
        in sources["G9"]["guardrail"],
        "all_absorbers_granted": all_absorbers_granted,
        "no_s6_claim_promotion": not any_claim_promoted,
        "residue_is_bridge_workflow_only": (
            residue["classification"] == "typed_bridge_workflow_only"
        ),
    }
    return {
        "test": "s6-g10-hostile-absorber-stress-v0.1",
        "tag": ["absorber_stress", "hostile_review", "no_claim_promotion"],
        "guardrail": (
            "Absorber audit only: this can demote or sharpen S6, but it cannot "
            "promote S6 without a same-neighbor-data physical capability split."
        ),
        "source_summary": source_summary(sources),
        "absorber_challenges": [challenge_to_dict(challenge) for challenge in challenges],
        "surviving_residue": residue,
        "checks": checks,
        "all_checks_passed": all(checks.values()),
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "stress_verdict": {
            "claim_status": "do_not_promote",
            "best_reading": (
                "S6 currently survives as a typed bridge and audit harness, not "
                "as an independent physical mechanism."
            ),
            "same_neighbor_data_escape_found": False,
        },
        "strongest_result": (
            "After granting density-matrix decoherence, Quantum Darwinism/SBS, "
            "finite descent, resource/contextuality, provenance, and fixed-source "
            "absorbers, S6 still usefully organizes the bridge as eta_F: local "
            "data -> associated final record -> loss profile. No stronger claim "
            "survives the hostile pass."
        ),
        "first_obstruction": (
            "The G9 capability difference is declared rather than sourced from a "
            "known quantum task while holding SBS/resource/provenance data fixed. "
            "That is the reopen burden."
        ),
        "next_step": (
            "Build a nonideal density-matrix or lab-facing fixture where the "
            "same SBS closure data is held fixed while a task-natural capability "
            "still separates before eta_F."
        ),
    }


def absorber_challenges(
    sources: dict[str, dict[str, Any]]
) -> tuple[AbsorberChallenge, ...]:
    g6_threshold = sources["G6"]["threshold"]
    g7_threshold = sources["G7"]["sbs_threshold"]
    g8_threshold = sources["G8"]["threshold"]
    g9_checks = sources["G9"]["checks"]
    return (
        AbsorberChallenge(
            absorber="density_matrix_open_system",
            owns=(
                "offdiagonal decay",
                "finite controlled-rotation environment model",
                "mutual information threshold",
            ),
            evidence=(
                "G6 all checks passed",
                f"threshold strength={g6_threshold['strength']}",
                f"offdiag={g6_threshold['offdiag_magnitude']}",
            ),
            status="granted",
            s6_residue=(
                "S6 may label the transition effect, but does not own the "
                "density-matrix dynamics."
            ),
            reopen_burden=(
                "Use a Hamiltonian/Lindblad or lab fixture and show a capability "
                "split not absorbed by the open-system model."
            ),
            promotes_s6_claim=False,
        ),
        AbsorberChallenge(
            absorber="quantum_darwinism_sbs",
            owns=(
                "redundant pointer broadcasting",
                "fragment agreement",
                "objectivity threshold",
            ),
            evidence=(
                "G7 all checks passed",
                f"sbs strength={g7_threshold['strength']}",
                f"objective fragments={g7_threshold['objective_fragment_count']}",
            ),
            status="granted",
            s6_residue=(
                "S6 records the typed loss and projection around the SBS threshold, "
                "while SBS owns physical objectivity."
            ),
            reopen_burden=(
                "Hold the SBS closure key fixed and show an S6 capability split "
                "that the SBS object cannot import."
            ),
            promotes_s6_claim=False,
        ),
        AbsorberChallenge(
            absorber="finite_sheaf_descent",
            owns=(
                "finite site",
                "support threshold",
                "associated-record construction",
            ),
            evidence=(
                "G8 all checks passed",
                f"field support={g8_threshold['field_support']}",
                f"stable={g8_threshold['stable']}",
            ),
            status="granted",
            s6_residue=(
                "The categorical wording is useful, but the current executable "
                "object is a finite descent reflector."
            ),
            reopen_burden=(
                "Prove a site-independent or physically forced sheafification "
                "condition, or keep the claim finite."
            ),
            promotes_s6_claim=False,
        ),
        AbsorberChallenge(
            absorber="resource_contextuality_task_theory",
            owns=(
                "phase-sensitive capability",
                "contextual residue",
                "known quantum task separations",
            ),
            evidence=(
                "G9 all checks passed",
                f"same final record={g9_checks['same_associated_record']}",
                f"different presheaf capability={g9_checks['different_presheaf_capability']}",
            ),
            status="granted",
            s6_residue=(
                "G9 gives a finite eta_F loss witness, but not a new resource "
                "theory separation."
            ),
            reopen_burden=(
                "Source phase_sensitive_branch from a task-natural quantum "
                "resource while holding neighbor data fixed."
            ),
            promotes_s6_claim=False,
        ),
        AbsorberChallenge(
            absorber="distributed_provenance_event_dag",
            owns=(
                "committed final records",
                "who-knew-what-when structure",
                "classical provenance DAG",
            ),
            evidence=(
                "G8 final capabilities include reconstruct_provenance_order",
                "G9 final records are identical after association",
            ),
            status="granted",
            s6_residue=(
                "S6 can connect local quantum-side records to the provenance DAG, "
                "but ordinary provenance owns the final record format."
            ),
            reopen_burden=(
                "Show a provenance-relevant capability split after fixing the "
                "same Event-DAG data."
            ),
            promotes_s6_claim=False,
        ),
        AbsorberChallenge(
            absorber="fixed_source_issuance_null",
            owns=(
                "no source-side issuance",
                "no arrow-of-time promotion",
                "Project/Finalize/Lose only",
            ),
            evidence=(
                "G6-G9 all mark Issue[S]=false",
                "all effects are projection/finality/loss effects",
            ),
            status="granted",
            s6_residue=(
                "S6 remains a bridge effect, not evidence that finality issues "
                "time at the source."
            ),
            reopen_burden=(
                "Type a source object with H/A held fixed and show new operation "
                "availability that cannot be read out as projection."
            ),
            promotes_s6_claim=False,
        ),
    )


def source_summary(sources: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        name: {
            "test": source["test"],
            "all_checks_passed": source["all_checks_passed"],
            "guardrail": source["guardrail"],
            "effect_verdict": source["effect_verdict"],
        }
        for name, source in sources.items()
    }


def surviving_residue(
    challenges: tuple[AbsorberChallenge, ...]
) -> dict[str, Any]:
    granted = [challenge.absorber for challenge in challenges if challenge.status == "granted"]
    return {
        "classification": "typed_bridge_workflow_only",
        "absorbers_granted": granted,
        "survives_as": (
            "A disciplined eta_F workflow: local context data, associated final "
            "record, capability loss, provenance output, and explicit reopen burden."
        ),
        "does_not_survive_as": (
            "A new quantum dynamics, a proof of general sheafification, an SBS "
            "alternative, or source-side time issuance."
        ),
        "minimum_reopen_packet": (
            "same-SBS-data, same-resource-data, same-Event-DAG-data pair with a "
            "task-natural capability split before eta_F and no absorber-owned "
            "field changes."
        ),
    }


def challenge_to_dict(challenge: AbsorberChallenge) -> dict[str, Any]:
    return {
        "absorber": challenge.absorber,
        "owns": list(challenge.owns),
        "evidence": list(challenge.evidence),
        "status": challenge.status,
        "s6_residue": challenge.s6_residue,
        "reopen_burden": challenge.reopen_burden,
        "promotes_s6_claim": challenge.promotes_s6_claim,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_g10_hostile_absorber_stress(), indent=2, sort_keys=True))
