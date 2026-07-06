"""T465: Abramsky-Brandenburger contextuality kappa absorber.

This module makes the current kappa-integrator objection executable.

The hostile target is Abramsky-Brandenburger style contextuality: an empirical
support table has local sections but no compatible global section. In that
setting, a kappa calculation over the same signed support cover is not an
independent prediction. It is a faithful re-encoding of the native H1/global
section obstruction.

The result is intentionally conservative:

- it does not refute the finite kappa re-encoding catalogue;
- it does not promote T224 into a genre-agnostic theorem;
- it does not claim a physics, quantum, or contextuality novelty;
- it turns the absorber into a reusable audit guardrail.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any

from models.typed_loss_transport import NeighborVisibleCover, compute_kappa


ARTIFACT_ID = "T465-ab-contextuality-kappa-absorber-v0.1"
VERDICT = "AB_CONTEXTUALITY_KAPPA_ABSORBER_BUILT_REENCODING_NOT_PREDICTION"
HONEST_CEILING = (
    "AB contextuality is a decisive absorber for prediction-language: once the "
    "native support table is admitted, kappa reads the same global-section/H1 "
    "obstruction. This supports the finite re-encoding catalogue only; it does "
    "not earn a genre-agnostic theorem or claim promotion."
)


@dataclass(frozen=True)
class ABContext:
    """One binary parity context in an AB-style support table."""

    name: str
    left: str
    right: str
    parity: int
    block: str

    @property
    def relation(self) -> str:
        return "same" if self.parity == 1 else "different"

    def is_satisfied_by(self, assignment: dict[str, int]) -> bool:
        return assignment[self.left] * assignment[self.right] == self.parity


@dataclass(frozen=True)
class ABEmpiricalModel:
    """A finite AB-style support model assembled from CHSH-shaped blocks."""

    model_id: str
    contexts: tuple[ABContext, ...]


@dataclass(frozen=True)
class TransportAudit:
    """One claimed source-kappa to AB-contextuality comparison."""

    model_id: str
    claimed_source_kappa: int
    native_ab_rank: int
    kappa_from_same_support_cover: int
    pairing_passes: bool
    transport_map_is_identity_on_integer_k: bool
    independent_prediction_branch: bool
    native_and_kappa_read_same_support_table: bool
    gate_label: str


def build_ab_empirical_model(
    contextual_blocks: int,
    balanced_blocks: int = 0,
    model_id: str | None = None,
) -> ABEmpiricalModel:
    """Build a disjoint union of CHSH-shaped AB support blocks.

    A contextual block uses the parity pattern + + + -, so local sections exist
    but no global assignment can satisfy all four contexts. A balanced block
    uses + + + + and is the noncontextual control.
    """

    if contextual_blocks < 0 or balanced_blocks < 0:
        raise ValueError("block counts must be nonnegative")
    if contextual_blocks + balanced_blocks == 0:
        raise ValueError("at least one block is required")

    contexts: list[ABContext] = []
    for index in range(contextual_blocks):
        contexts.extend(_block_contexts(f"C{index}", contextual=True))
    for index in range(balanced_blocks):
        contexts.extend(_block_contexts(f"N{index}", contextual=False))

    name = model_id or (
        f"ab_contextual_{contextual_blocks}_balanced_{balanced_blocks}"
    )
    return ABEmpiricalModel(model_id=name, contexts=tuple(contexts))


def variables(model: ABEmpiricalModel) -> tuple[str, ...]:
    """Variables in first-seen order."""

    seen: set[str] = set()
    ordered: list[str] = []
    for context in model.contexts:
        for variable in (context.left, context.right):
            if variable not in seen:
                seen.add(variable)
                ordered.append(variable)
    return tuple(ordered)


def native_ab_obstruction(model: ABEmpiricalModel) -> dict[str, Any]:
    """Compute native AB obstruction without calling kappa.

    Native test: each binary context has local support; contextuality appears
    when no global assignment over the named measurements satisfies all local
    contexts. For the disjoint CHSH-shaped blocks here, each contextual block
    contributes exactly one independent native H1/global-section obstruction.
    """

    block_rows: list[dict[str, Any]] = []
    total_rank = 0
    all_local_sections_exist = True
    grouped = _contexts_by_block(model)

    for block, contexts in grouped.items():
        block_variables = _variables_for_contexts(contexts)
        parity_product = 1
        for context in contexts:
            parity_product *= context.parity
        local_sections_exist = all(_context_has_local_section(context) for context in contexts)
        global_section_exists = _global_assignment_exists(block_variables, contexts)
        contextual = local_sections_exist and not global_section_exists
        native_rank = 1 if contextual else 0
        total_rank += native_rank
        all_local_sections_exist = all_local_sections_exist and local_sections_exist
        block_rows.append(
            {
                "block": block,
                "variables": list(block_variables),
                "contexts": [
                    {
                        "name": context.name,
                        "left": context.left,
                        "right": context.right,
                        "parity": context.parity,
                        "relation": context.relation,
                    }
                    for context in contexts
                ],
                "parity_product": parity_product,
                "local_sections_exist": local_sections_exist,
                "global_section_exists": global_section_exists,
                "native_contextual": contextual,
                "native_h1_rank": native_rank,
            }
        )

    return {
        "model_id": model.model_id,
        "all_local_sections_exist": all_local_sections_exist,
        "global_section_exists": all(row["global_section_exists"] for row in block_rows),
        "native_contextuality_rank": total_rank,
        "native_source": "AB support table plus global-section existence",
        "native_computation_independent_of_compute_kappa": True,
        "blocks": block_rows,
    }


def nu_from_ab_empirical_model(model: ABEmpiricalModel) -> NeighborVisibleCover:
    """Forget AB semantics into the neighbor-visible same/different cover."""

    edges = tuple(
        (context.left, context.right, context.parity)
        for context in model.contexts
    )
    return NeighborVisibleCover(
        name=f"AB:{model.model_id}",
        variables=variables(model),
        signed_edges=edges,
    )


def audit_claimed_transport(
    model: ABEmpiricalModel,
    claimed_source_kappa: int | None = None,
) -> TransportAudit:
    """Compare claimed source kappa with native AB and kappa-on-same-support.

    Passing paired fixtures are intentionally identity-on-integer-k. The mismatch
    control proves the harness can fail when the claimed source rank differs
    from the native AB obstruction.
    """

    native = native_ab_obstruction(model)
    kappa_result = compute_kappa(nu_from_ab_empirical_model(model))
    native_rank = int(native["native_contextuality_rank"])
    claimed = native_rank if claimed_source_kappa is None else claimed_source_kappa
    same_support = True
    pairing_passes = claimed == native_rank == kappa_result.kappa
    identity_on_k = pairing_passes
    label = (
        "NATIVE_H1_REENCODING_NOT_PREDICTION"
        if pairing_passes
        else "MISMATCH_CONTROL_FAILS_AS_EXPECTED"
    )
    return TransportAudit(
        model_id=model.model_id,
        claimed_source_kappa=claimed,
        native_ab_rank=native_rank,
        kappa_from_same_support_cover=kappa_result.kappa,
        pairing_passes=pairing_passes,
        transport_map_is_identity_on_integer_k=identity_on_k,
        independent_prediction_branch=False,
        native_and_kappa_read_same_support_table=same_support,
        gate_label=label,
    )


def run() -> dict[str, Any]:
    """Run the T465 absorber audit."""

    paired_models = (
        build_ab_empirical_model(1, model_id="ab_single_contextual_block"),
        build_ab_empirical_model(2, model_id="ab_two_contextual_blocks"),
        build_ab_empirical_model(3, model_id="ab_three_contextual_blocks"),
        build_ab_empirical_model(
            2,
            balanced_blocks=1,
            model_id="ab_mixed_two_contextual_one_balanced",
        ),
        build_ab_empirical_model(
            0,
            balanced_blocks=1,
            model_id="ab_balanced_control",
        ),
    )
    paired_audits = tuple(audit_claimed_transport(model) for model in paired_models)

    mismatch_model = build_ab_empirical_model(
        1,
        model_id="ab_single_contextual_mismatch_control",
    )
    mismatch_control = audit_claimed_transport(
        mismatch_model,
        claimed_source_kappa=2,
    )

    native_rows = {
        model.model_id: native_ab_obstruction(model)
        for model in paired_models
    }
    kappa_rows = {
        model.model_id: _kappa_dict(compute_kappa(nu_from_ab_empirical_model(model)))
        for model in paired_models
    }
    paired = [_audit_dict(audit) for audit in paired_audits]
    paired_identity = all(audit.transport_map_is_identity_on_integer_k for audit in paired_audits)
    all_same_support = all(audit.native_and_kappa_read_same_support_table for audit in paired_audits)
    no_prediction_branch = all(
        audit.independent_prediction_branch is False for audit in paired_audits
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Make Abramsky-Brandenburger contextuality an executable hostile "
            "absorber for kappa prediction-language."
        ),
        "models": {
            "native_ab_obstructions": native_rows,
            "kappa_on_same_support_cover": kappa_rows,
        },
        "paired_fixture_audits": paired,
        "mismatch_control": _audit_dict(mismatch_control),
        "absorber_findings": {
            "paired_fixtures_pass": all(audit.pairing_passes for audit in paired_audits),
            "paired_fixtures_are_identity_on_integer_k": paired_identity,
            "native_and_kappa_read_same_support_table": all_same_support,
            "independent_prediction_branch_present": not no_prediction_branch,
            "mismatch_control_fails": mismatch_control.pairing_passes is False,
            "native_ab_witness_independent_of_compute_kappa": (
                "compute_kappa" not in native_ab_obstruction.__code__.co_names
            ),
            "t224_promotion_earned": False,
            "genre_agnostic_theorem_earned": False,
            "claim_ledger_update": "none; no claim promotion or demotion",
        },
        "overall_verdict": {
            "verdict": VERDICT,
            "claim_movement": "none",
            "reading": (
                "T465 does not kill the finite kappa re-encoding catalogue. It "
                "does kill the stronger reading that AB contextuality supplies an "
                "independent kappa prediction: the native AB obstruction and "
                "kappa both read the same support/global-section data."
            ),
        },
        "not_earned": [
            "T224 promotion",
            "CSP-PO1 promotion",
            "genre-agnostic kappa theorem",
            "Abramsky-Brandenburger novelty",
            "physics or quantum prediction",
            "claim-ledger movement",
            "public-posture movement",
        ],
        "recommended_next": [
            "Use T465 as the hostile AB absorber before calling kappa predictive in sheaf contextuality.",
            "Do not reopen T224 as a genre-agnostic theorem without a non-identity target-side witness.",
            "If kappa work continues, seek a target whose native invariant is not just the same support H1/global-section rank.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {model_id} | {claimed_source_kappa} | {native_ab_rank} | "
        "{kappa_from_same_support_cover} | {pairing_passes} | {gate_label} |".format(
            **audit
        )
        for audit in result["paired_fixture_audits"]
    ]
    not_earned = [f"- {item}" for item in result["not_earned"]]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    mismatch = result["mismatch_control"]
    return "\n".join(
        [
            "# T465 - AB Contextuality Kappa Absorber - v0.1 results",
            "",
            "> Absorber audit only. `CLAIM-LEDGER.md`, `ROADMAP.md`, README, "
            "North Star files, public posture, hard policy, and cross-repo "
            "truth are untouched.",
            "",
            "- Spec: `tests/T465-ab-contextuality-kappa-absorber.md`",
            "- Model: `models/ab_contextuality_kappa_absorber.py`",
            "- Tests: `tests/test_ab_contextuality_kappa_absorber.py`",
            "- Artifact JSON: `results/T465-ab-contextuality-kappa-absorber-v0.1.json`",
            "- Sources: T21, T224/T229/T234/T239/T244 kappa transport line, and the CSP-PO1 integrator objection",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Paired Fixture Audit",
            "",
            "| model | claimed source kappa | native AB rank | kappa on same support | passes? | label |",
            "| --- | ---: | ---: | ---: | --- | --- |",
            *rows,
            "",
            "## Mismatch Control",
            "",
            (
                f"- Model: `{mismatch['model_id']}`; claimed source kappa "
                f"{mismatch['claimed_source_kappa']} vs native AB rank "
                f"{mismatch['native_ab_rank']} -> `{mismatch['gate_label']}`."
            ),
            "",
            "## What This Earns",
            "",
            "Earns: an executable absorber for AB contextuality in the kappa line. "
            "The paired fixtures show faithful equality only because both sides "
            "read the same support/global-section obstruction.",
            "",
            "Does not earn:",
            "",
            *not_earned,
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_steps,
            "",
        ]
    )


def _block_contexts(block: str, contextual: bool) -> tuple[ABContext, ...]:
    a0 = f"{block}_A0"
    a1 = f"{block}_A1"
    b0 = f"{block}_B0"
    b1 = f"{block}_B1"
    last_parity = -1 if contextual else 1
    return (
        ABContext(f"{block}_A0B0", a0, b0, 1, block),
        ABContext(f"{block}_A0B1", a0, b1, 1, block),
        ABContext(f"{block}_A1B0", a1, b0, 1, block),
        ABContext(f"{block}_A1B1", a1, b1, last_parity, block),
    )


def _contexts_by_block(model: ABEmpiricalModel) -> dict[str, tuple[ABContext, ...]]:
    grouped: dict[str, list[ABContext]] = {}
    for context in model.contexts:
        grouped.setdefault(context.block, []).append(context)
    return {block: tuple(contexts) for block, contexts in grouped.items()}


def _variables_for_contexts(contexts: tuple[ABContext, ...]) -> tuple[str, ...]:
    seen: set[str] = set()
    ordered: list[str] = []
    for context in contexts:
        for variable in (context.left, context.right):
            if variable not in seen:
                seen.add(variable)
                ordered.append(variable)
    return tuple(ordered)


def _context_has_local_section(context: ABContext) -> bool:
    for left, right in product((-1, 1), repeat=2):
        if left * right == context.parity:
            return True
    return False


def _global_assignment_exists(
    block_variables: tuple[str, ...],
    contexts: tuple[ABContext, ...],
) -> bool:
    for values in product((-1, 1), repeat=len(block_variables)):
        assignment = dict(zip(block_variables, values))
        if all(context.is_satisfied_by(assignment) for context in contexts):
            return True
    return False


def _kappa_dict(result: Any) -> dict[str, Any]:
    return {
        "cover_name": result.cover_name,
        "num_variables": result.num_variables,
        "num_edges": result.num_edges,
        "num_components": result.num_components,
        "kappa": result.kappa,
        "cycle_space_rank": result.cycle_space_rank,
        "global_section_exists": result.global_section_exists,
        "frustrated": result.frustrated,
    }


def _audit_dict(audit: TransportAudit) -> dict[str, Any]:
    return {
        "model_id": audit.model_id,
        "claimed_source_kappa": audit.claimed_source_kappa,
        "native_ab_rank": audit.native_ab_rank,
        "kappa_from_same_support_cover": audit.kappa_from_same_support_cover,
        "pairing_passes": audit.pairing_passes,
        "transport_map_is_identity_on_integer_k": (
            audit.transport_map_is_identity_on_integer_k
        ),
        "independent_prediction_branch": audit.independent_prediction_branch,
        "native_and_kappa_read_same_support_table": (
            audit.native_and_kappa_read_same_support_table
        ),
        "gate_label": audit.gate_label,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
