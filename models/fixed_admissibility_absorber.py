"""T376: fixed-admissibility absorber harness.

The harness asks whether a candidate record-finality or source-side witness is
already reproduced by a fixed admissibility structure plus changing access.
If so, the witness is reconstruction-layer discipline, not source-side residue.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Proposal:
    proposal_id: str
    handle: str
    observer: str
    fields: tuple[tuple[str, int], ...]
    phase: str = "default"
    depends_on: tuple[str, ...] = ()

    def value(self, field: str) -> int | None:
        return dict(self.fields).get(field)


@dataclass(frozen=True)
class TraceFixture:
    name: str
    description: str
    proposals: tuple[Proposal, ...]
    target_admitted: tuple[str, ...]
    target_rejected: tuple[str, ...]
    expected_residue_label: str


@dataclass(frozen=True)
class AbsorberSpec:
    absorber_id: str
    description: str
    decide: Callable[[tuple[Proposal, ...], Proposal], bool]


@dataclass(frozen=True)
class AbsorberVerdict:
    absorber_id: str
    reproduces_target: bool
    admitted: tuple[str, ...]
    rejected: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class FixtureVerdict:
    fixture_name: str
    absorber_verdicts: tuple[AbsorberVerdict, ...]
    absorbing_absorbers: tuple[str, ...]
    nonfixed_admissibility_needed: bool
    residue_label: str
    plain_english: str


@dataclass(frozen=True)
class T376Result:
    fixture_verdicts: tuple[FixtureVerdict, ...]
    fixed_predicate_absorbs_count: int
    fixed_latent_access_absorbs_count: int
    fixed_projector_absorbs_count: int
    nonfixed_positive_control_survives: bool
    strongest_claim: str
    claim_ledger_update: str


def run_absorber(spec: AbsorberSpec, fixture: TraceFixture) -> AbsorberVerdict:
    accepted: list[Proposal] = []
    admitted: list[str] = []
    rejected: list[str] = []
    for proposal in fixture.proposals:
        if spec.decide(tuple(accepted), proposal):
            accepted.append(proposal)
            admitted.append(proposal.proposal_id)
        else:
            rejected.append(proposal.proposal_id)
    reproduces = (
        tuple(admitted) == fixture.target_admitted
        and tuple(rejected) == fixture.target_rejected
    )
    return AbsorberVerdict(
        absorber_id=spec.absorber_id,
        reproduces_target=reproduces,
        admitted=tuple(admitted),
        rejected=tuple(rejected),
        reason=(
            "reproduces the target trace exactly"
            if reproduces
            else "does not reproduce the target accept/reject trace"
        ),
    )


def evaluate_fixture(fixture: TraceFixture, specs: tuple[AbsorberSpec, ...]) -> FixtureVerdict:
    verdicts = tuple(run_absorber(spec, fixture) for spec in specs)
    absorbing = tuple(v.absorber_id for v in verdicts if v.reproduces_target)
    nonfixed_needed = len(absorbing) == 0
    residue_label = (
        "nonfixed_admissibility_residue"
        if nonfixed_needed
        else "fixed_admissibility_absorbed"
    )
    return FixtureVerdict(
        fixture_name=fixture.name,
        absorber_verdicts=verdicts,
        absorbing_absorbers=absorbing,
        nonfixed_admissibility_needed=nonfixed_needed,
        residue_label=residue_label,
        plain_english=(
            "No fixed absorber reproduced this trace; a genuinely changing admissibility law is needed."
            if nonfixed_needed
            else "A fixed admissibility structure reproduced the trace, so this is not source-side residue."
        ),
    )


def run_t376_analysis() -> T376Result:
    fixtures = canonical_fixtures()
    verdicts = tuple(evaluate_fixture(fixture, absorber_specs_for(fixture)) for fixture in fixtures)
    fixed_predicate_count = sum(
        "fixed_compatibility_predicate" in verdict.absorbing_absorbers
        for verdict in verdicts
    )
    fixed_latent_count = sum(
        "fixed_latent_source_changing_access" in verdict.absorbing_absorbers
        for verdict in verdicts
    )
    fixed_projector_count = sum(
        "fixed_projector_state_space" in verdict.absorbing_absorbers
        for verdict in verdicts
    )
    positive = next(v for v in verdicts if v.fixture_name == "nonfixed_threshold_positive_control")
    return T376Result(
        fixture_verdicts=verdicts,
        fixed_predicate_absorbs_count=fixed_predicate_count,
        fixed_latent_access_absorbs_count=fixed_latent_count,
        fixed_projector_absorbs_count=fixed_projector_count,
        nonfixed_positive_control_survives=positive.nonfixed_admissibility_needed,
        strongest_claim=(
            "Fixed admissibility is a reusable absorber: parity-style coherence, "
            "latent-source access, and projector-style mode selection are not "
            "source-side residue unless fixed predicate/projector/access models fail."
        ),
        claim_ledger_update=(
            "Register T376 as a guardrail harness only. It demotes witnesses that "
            "are reproduced by fixed admissibility plus changing access and preserves "
            "only traces requiring a genuinely nonfixed admissibility law."
        ),
    )


def canonical_fixtures() -> tuple[TraceFixture, ...]:
    return (
        TraceFixture(
            name="parity_clock_free_trace",
            description="Temporal-issuance style parity coherence with no global tick.",
            proposals=(
                Proposal("p1", "h0", "O_A", (("x_ab", 1),)),
                Proposal("p2", "h0", "O_C", (("x_ca", 0),)),
                Proposal("p3", "h0", "O_B", (("x_bc", 0),)),
                Proposal("p4", "h0", "O_B", (("x_bc", 1),)),
                Proposal("p5", "h1", "O_C", (("x_ca", 1),)),
                Proposal("p6", "h1", "O_A", (("x_ab", 0),)),
                Proposal("p7", "h1", "O_B", (("x_bc", 1),)),
            ),
            target_admitted=("p1", "p2", "p4", "p5", "p6", "p7"),
            target_rejected=("p3",),
            expected_residue_label="fixed_admissibility_absorbed",
        ),
        TraceFixture(
            name="latent_access_trace",
            description="A fixed latent table plus changing observer access reproduces admissions.",
            proposals=(
                Proposal("l1", "h0", "O_A", (("bit", 1),)),
                Proposal("l2", "h0", "O_B", (("bit", 0),)),
                Proposal("l3", "h1", "O_C", (("bit", 0),)),
                Proposal("l4", "h1", "O_A", (("bit", 1),)),
            ),
            target_admitted=("l1", "l3"),
            target_rejected=("l2", "l4"),
            expected_residue_label="fixed_admissibility_absorbed",
        ),
        TraceFixture(
            name="projector_zero_mode_trace",
            description="Projector-style selection of allowed modes absorbs a zero-mode filling story.",
            proposals=(
                Proposal("z1", "mode", "section", (("mode_id", 0),)),
                Proposal("z2", "mode", "section", (("mode_id", 1),)),
                Proposal("z3", "mode", "section", (("mode_id", 2),)),
                Proposal("z4", "mode", "section", (("mode_id", 3),)),
            ),
            target_admitted=("z1", "z2", "z3"),
            target_rejected=("z4",),
            expected_residue_label="fixed_admissibility_absorbed",
        ),
        TraceFixture(
            name="nonfixed_threshold_positive_control",
            description="The same visible proposal flips verdict after the admissibility threshold changes.",
            proposals=(
                Proposal("n1", "a", "O", (("score", 2),), phase="low_threshold"),
                Proposal("n2", "b", "O", (("score", 2),), phase="high_threshold"),
                Proposal("n3", "c", "O", (("score", 5),), phase="high_threshold"),
            ),
            target_admitted=("n1", "n3"),
            target_rejected=("n2",),
            expected_residue_label="nonfixed_admissibility_residue",
        ),
    )


def absorber_specs_for(fixture: TraceFixture) -> tuple[AbsorberSpec, ...]:
    return (
        AbsorberSpec(
            "fixed_compatibility_predicate",
            "One fixed value-level compatibility predicate over the trace.",
            _fixed_compatibility_decider(fixture.name),
        ),
        AbsorberSpec(
            "fixed_projector_state_space",
            "One fixed projector/allowed-state set over proposed mode or state labels.",
            _fixed_projector_decider(fixture.name),
        ),
        AbsorberSpec(
            "fixed_latent_source_changing_access",
            "One fixed latent source table with observers gaining partial access.",
            _fixed_latent_decider(fixture.name),
        ),
        AbsorberSpec(
            "schema_constraint_checking",
            "Ordinary online schema or CHECK-constraint validation.",
            _schema_decider(fixture.name),
        ),
        AbsorberSpec(
            "causal_order_plus_value_predicate",
            "Declared dependencies plus a fixed value predicate.",
            _causal_value_decider(fixture.name),
        ),
    )


def _fixed_compatibility_decider(name: str) -> Callable[[tuple[Proposal, ...], Proposal], bool]:
    if name == "parity_clock_free_trace":
        return _parity_prefix_extendable
    if name == "latent_access_trace":
        return lambda _accepted, proposal: proposal.value("bit") == _latent_bit(proposal.handle)
    if name == "projector_zero_mode_trace":
        return lambda _accepted, proposal: proposal.value("mode_id") in {0, 1, 2}
    if name == "nonfixed_threshold_positive_control":
        return lambda _accepted, proposal: (proposal.value("score") or 0) >= 3
    raise ValueError(name)


def _fixed_projector_decider(name: str) -> Callable[[tuple[Proposal, ...], Proposal], bool]:
    if name == "projector_zero_mode_trace":
        return lambda _accepted, proposal: proposal.value("mode_id") in {0, 1, 2}
    if name == "parity_clock_free_trace":
        return _parity_prefix_extendable
    if name == "latent_access_trace":
        return lambda _accepted, proposal: proposal.value("bit") == _latent_bit(proposal.handle)
    if name == "nonfixed_threshold_positive_control":
        return lambda _accepted, proposal: (proposal.value("score") or 0) >= 3
    raise ValueError(name)


def _fixed_latent_decider(name: str) -> Callable[[tuple[Proposal, ...], Proposal], bool]:
    if name == "latent_access_trace":
        return lambda _accepted, proposal: proposal.value("bit") == _latent_bit(proposal.handle)
    if name == "parity_clock_free_trace":
        return _parity_prefix_extendable
    if name == "projector_zero_mode_trace":
        return lambda _accepted, proposal: proposal.value("mode_id") in {0, 1, 2}
    if name == "nonfixed_threshold_positive_control":
        return lambda _accepted, proposal: (proposal.value("score") or 0) >= 3
    raise ValueError(name)


def _schema_decider(name: str) -> Callable[[tuple[Proposal, ...], Proposal], bool]:
    if name == "parity_clock_free_trace":
        return _parity_prefix_extendable
    return _fixed_compatibility_decider(name)


def _causal_value_decider(name: str) -> Callable[[tuple[Proposal, ...], Proposal], bool]:
    base = _fixed_compatibility_decider(name)

    def decide(accepted: tuple[Proposal, ...], proposal: Proposal) -> bool:
        accepted_ids = {item.proposal_id for item in accepted}
        return set(proposal.depends_on) <= accepted_ids and base(accepted, proposal)

    return decide


def _parity_prefix_extendable(accepted: tuple[Proposal, ...], proposal: Proposal) -> bool:
    by_handle: dict[str, dict[str, int]] = {}
    for item in (*accepted, proposal):
        handle_fields = by_handle.setdefault(item.handle, {})
        for field, value in item.fields:
            if field in handle_fields and handle_fields[field] != value:
                return False
            handle_fields[field] = value
    for fields in by_handle.values():
        if {"x_ab", "x_bc", "x_ca"} <= set(fields):
            if fields["x_ab"] ^ fields["x_bc"] ^ fields["x_ca"] != 0:
                return False
    return True


def _latent_bit(handle: str) -> int:
    return {"h0": 1, "h1": 0}[handle]


def t376_result_to_dict(result: T376Result) -> dict[str, object]:
    return {
        "fixture_verdicts": [
            {
                "fixture_name": verdict.fixture_name,
                "absorbing_absorbers": list(verdict.absorbing_absorbers),
                "nonfixed_admissibility_needed": verdict.nonfixed_admissibility_needed,
                "residue_label": verdict.residue_label,
                "plain_english": verdict.plain_english,
                "absorber_verdicts": [
                    {
                        "absorber_id": item.absorber_id,
                        "reproduces_target": item.reproduces_target,
                        "admitted": list(item.admitted),
                        "rejected": list(item.rejected),
                        "reason": item.reason,
                    }
                    for item in verdict.absorber_verdicts
                ],
            }
            for verdict in result.fixture_verdicts
        ],
        "fixed_predicate_absorbs_count": result.fixed_predicate_absorbs_count,
        "fixed_latent_access_absorbs_count": result.fixed_latent_access_absorbs_count,
        "fixed_projector_absorbs_count": result.fixed_projector_absorbs_count,
        "nonfixed_positive_control_survives": result.nonfixed_positive_control_survives,
        "strongest_claim": result.strongest_claim,
        "claim_ledger_update": result.claim_ledger_update,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t376_result_to_dict(run_t376_analysis()), indent=2))
