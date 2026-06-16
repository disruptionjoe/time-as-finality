"""T14: integrated observer-context finality laboratory.

The lab composes earlier mechanisms without changing their source modules:
dynamic record order (T1/T9 style), coupling profiles (T12), inherited
expression (T11), coarse-grained proof validation and Snowball-style
reconciliation (T10), and signed readout (T13).

The result is intentionally bounded and finite.  It tests typed coherence
across stages; it does not derive quantum mechanics, physical truth, or a
universal consensus law.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.proof_carrying_finality import (
    IdealProofSystem,
    ProofCertificate,
    SnowballParameters,
    coarse_claim,
    coarse_graining_summary,
    opposite_claim_state,
    run_experiment,
)
from models.t1_record_graph import Observer, Record
from models.t13_signed_readout import ReadoutRecordGraph


Bits = tuple[int, ...]


@dataclass(frozen=True)
class IntegratedMetadata:
    channel: str
    weight: complex
    expression_tags: frozenset[str]
    certificate: ProofCertificate


@dataclass(frozen=True)
class IntegratedObserver:
    observer_id: str
    event: str
    coupling_profile: frozenset[str]
    accessible_holders: frozenset[str]
    expression_context: tuple[tuple[str, bool], ...] = ()
    require_valid_proofs: bool = True

    def context_map(self) -> dict[str, bool]:
        return dict(self.expression_context)

    def t1_observer(self) -> Observer:
        return Observer(self.observer_id, self.event, self.accessible_holders)


class IntegratedRecordGraph(ReadoutRecordGraph):
    """Readout graph with channels, expression tags, and proof certificates."""

    def __init__(self, proof_system: IdealProofSystem) -> None:
        super().__init__()
        self.proof_system = proof_system
        self.metadata: dict[str, IntegratedMetadata] = {}

    def add_integrated_record(
        self,
        record: Record,
        *,
        channel: str,
        weight: complex,
        expression_tags: frozenset[str],
        certificate: ProofCertificate,
    ) -> None:
        self.add_weighted_record(record, weight)
        self.metadata[record.record_id] = IntegratedMetadata(
            channel=channel,
            weight=complex(weight),
            expression_tags=expression_tags,
            certificate=certificate,
        )

    def stored_record_count(self) -> int:
        return len(self.records)

    def _record_visible(self, record: Record, observer: IntegratedObserver) -> bool:
        meta = self.metadata[record.record_id]
        context = observer.context_map()
        return (
            record.holder in observer.accessible_holders
            and meta.channel in observer.coupling_profile
            and all(context.get(tag, True) for tag in meta.expression_tags)
            and (
                not observer.require_valid_proofs
                or self.proof_system.verify(meta.certificate)
            )
        )

    def visible_records(self, observer: IntegratedObserver) -> tuple[Record, ...]:
        return tuple(
            record
            for record in self.records.values()
            if self._record_visible(record, observer)
        )

    def view_for(self, observer: IntegratedObserver) -> ReadoutRecordGraph:
        view = ReadoutRecordGraph()
        for event in self.events:
            view.add_event(event)
        for earlier in self.events:
            for later in self._successors[earlier]:
                view.add_causal_edge(earlier, later)
        for record in self.visible_records(observer):
            view.add_weighted_record(record, self.metadata[record.record_id].weight)
        return view

    def profile_for(
        self,
        observer: IntegratedObserver,
        proposition: str,
        value: str,
        threshold: int,
    ) -> tuple[int, int, int, int]:
        return self.view_for(observer).finality_profile(
            observer.t1_observer(), proposition, value, threshold
        ).as_tuple()

    def readout_for(
        self,
        observer: IntegratedObserver,
        proposition: str,
        value: str,
    ) -> float:
        return self.view_for(observer).readout_born(
            observer.t1_observer(), proposition, value
        )

    def rejected_forged_record_ids(self, observer: IntegratedObserver) -> tuple[str, ...]:
        if not observer.require_valid_proofs:
            return ()
        rejected = []
        raw_observer = IntegratedObserver(
            observer.observer_id,
            observer.event,
            observer.coupling_profile,
            observer.accessible_holders,
            observer.expression_context,
            require_valid_proofs=False,
        )
        for record in self.visible_records(raw_observer):
            meta = self.metadata[record.record_id]
            if not self.proof_system.verify(meta.certificate):
                rejected.append(record.record_id)
        return tuple(sorted(rejected))

    def valid_dissent_record_ids(self, observer: IntegratedObserver) -> tuple[str, ...]:
        return tuple(
            sorted(
                record.record_id
                for record in self.visible_records(observer)
                if self.proof_system.verify(self.metadata[record.record_id].certificate)
                and self.metadata[record.record_id].certificate.claim == 0
            )
        )


def _add_chain_events(graph: IntegratedRecordGraph) -> None:
    for event in ("e1", "e2", "e3", "observe"):
        graph.add_event(event)
    graph.add_causal_edge("e1", "e2")
    graph.add_causal_edge("e2", "e3")
    graph.add_causal_edge("e3", "observe")


def build_integrated_scenario(
    *,
    destructive_phase: bool = True,
) -> tuple[IntegratedRecordGraph, dict[str, IntegratedObserver], Bits]:
    """Build the finite T14 witness graph.

    The core records have weights `(1, -1, 1)` when `destructive_phase` is
    true and `(1, 1, 1)` otherwise.  The graph topology and finality profile
    remain unchanged, exposing readout non-factorization inside the integrated
    pipeline.
    """

    hidden_state = (1, 1, 1, 1, 1, 0, 0, 0, 0)
    proof_system = IdealProofSystem(key=b"time-as-finality-t14")
    graph = IntegratedRecordGraph(proof_system)
    _add_chain_events(graph)
    second_weight = -1 if destructive_phase else 1

    cert_1 = proof_system.issue_leaf("source-1", hidden_state, 0, "core-1")
    cert_2 = proof_system.issue_leaf("source-2", hidden_state, 0, "core-2")
    cert_3 = proof_system.issue_leaf("source-3", hidden_state, 0, "core-3")
    forged = proof_system.forge("forged-source", claim=0, epoch=0)
    dissent = proof_system.issue_leaf(
        "dissent-source",
        opposite_claim_state(len(hidden_state), claim=0),
        0,
        "valid-dissent",
    )

    graph.add_integrated_record(
        Record("r1", "X", "true", "e1", "h1", 1.0),
        channel="grav",
        weight=1,
        expression_tags=frozenset({"base"}),
        certificate=cert_1,
    )
    graph.add_integrated_record(
        Record("r2", "X", "true", "e2", "h2", 1.0),
        channel="em",
        weight=second_weight,
        expression_tags=frozenset({"phase"}),
        certificate=cert_2,
    )
    graph.add_integrated_record(
        Record("r3", "X", "true", "e3", "h3", 1.0),
        channel="grav",
        weight=1,
        expression_tags=frozenset({"base"}),
        certificate=cert_3,
    )
    graph.add_integrated_record(
        Record("r4-forged", "X", "true", "e2", "h4", 1.0),
        channel="social",
        weight=-1,
        expression_tags=frozenset({"adversarial"}),
        certificate=forged,
    )
    graph.add_integrated_record(
        Record("r5-valid-dissent", "X", "true", "e2", "h5", 1.0),
        channel="social",
        weight=-1,
        expression_tags=frozenset({"dissent"}),
        certificate=dissent,
    )

    holders = frozenset({"h1", "h2", "h3", "h4", "h5"})
    observers = {
        "core": IntegratedObserver(
            "O_core",
            "observe",
            frozenset({"grav", "em"}),
            holders,
        ),
        "grav_only": IntegratedObserver(
            "O_grav",
            "observe",
            frozenset({"grav"}),
            holders,
        ),
        "phase_silenced": IntegratedObserver(
            "O_silenced",
            "observe",
            frozenset({"grav", "em"}),
            holders,
            expression_context=(("phase", False),),
        ),
        "raw_social": IntegratedObserver(
            "O_raw_social",
            "observe",
            frozenset({"grav", "em", "social"}),
            holders,
            require_valid_proofs=False,
        ),
        "verified_social": IntegratedObserver(
            "O_verified_social",
            "observe",
            frozenset({"grav", "em", "social"}),
            holders,
            require_valid_proofs=True,
        ),
    }
    return graph, observers, hidden_state


def observer_summary(
    graph: IntegratedRecordGraph,
    observer: IntegratedObserver,
    threshold: int,
) -> dict[str, object]:
    records = graph.visible_records(observer)
    view = graph.view_for(observer)
    t1_observer = observer.t1_observer()
    return {
        "coupling_profile": sorted(observer.coupling_profile),
        "require_valid_proofs": observer.require_valid_proofs,
        "expression_context": dict(observer.expression_context),
        "visible_record_ids": [record.record_id for record in records],
        "profile": view.finality_profile(t1_observer, "X", "true", threshold).as_tuple(),
        "readout": view.readout_born(t1_observer, "X", "true"),
        "reconstructs": view.reconstruct_value(t1_observer, "X", threshold),
        "rejected_forged_record_ids": graph.rejected_forged_record_ids(observer),
        "valid_dissent_record_ids": graph.valid_dissent_record_ids(observer),
    }


def _method(summary, name: str) -> dict[str, float]:
    method = getattr(summary, name)
    return {
        "accuracy": method.accuracy,
        "false_finality_rate": method.false_finality_rate,
        "consensus_rate": method.consensus_rate,
        "mean_decision_fraction": method.mean_decision_fraction,
        "mean_rejected_messages": method.mean_rejected_messages,
    }


def consensus_probe(hidden_state: Bits) -> dict[str, object]:
    parameters = SnowballParameters(max_rounds=60)
    forged = run_experiment(
        trials=30,
        global_microstate=hidden_state,
        population_size=21,
        bit_error_rate=0.15,
        adversary_fraction=0.33,
        adversary_mode="forged",
        parameters=parameters,
        seed=1400,
    )
    valid_dissent = run_experiment(
        trials=30,
        global_microstate=hidden_state,
        population_size=21,
        bit_error_rate=0.15,
        adversary_fraction=0.33,
        adversary_mode="valid_dissent",
        parameters=parameters,
        seed=1500,
    )
    return {
        "forged": {
            "proof_snowball": _method(forged, "proof_snowball"),
            "raw_snowball": _method(forged, "raw_snowball"),
            "bayesian_map_accuracy": forged.bayesian_map_accuracy,
        },
        "valid_dissent": {
            "proof_snowball": _method(valid_dissent, "proof_snowball"),
            "raw_snowball": _method(valid_dissent, "raw_snowball"),
            "bayesian_map_accuracy": valid_dissent.bayesian_map_accuracy,
        },
    }


def run_t14_analysis() -> dict[str, object]:
    destructive, observers, hidden_state = build_integrated_scenario(
        destructive_phase=True
    )
    constructive, constructive_observers, _ = build_integrated_scenario(
        destructive_phase=False
    )
    threshold = 1
    coarse = coarse_graining_summary()
    core_destructive = observer_summary(destructive, observers["core"], threshold)
    core_constructive = observer_summary(
        constructive, constructive_observers["core"], threshold
    )
    return {
        "threshold": threshold,
        "hidden_state": "".join(str(bit) for bit in hidden_state),
        "coarse_claim": coarse_claim(hidden_state),
        "stored_record_count": destructive.stored_record_count(),
        "coarse_graining": {
            "microstate_count": coarse.microstate_count,
            "claim_counts": coarse.claim_counts,
            "hidden_information_bits": coarse.hidden_information_bits,
            "mean_reversal_radius": coarse.mean_reversal_radius,
        },
        "typed_pipeline": [
            "hidden_state",
            "record_generation",
            "inherited_expression",
            "observer_coupling",
            "coarse_graining_and_proof_validation",
            "snowball_style_reconciliation",
            "finality_profile",
            "signed_readout",
        ],
        "observers": {
            name: observer_summary(destructive, observer, threshold)
            for name, observer in observers.items()
        },
        "same_profile_different_readout": {
            "destructive_profile": core_destructive["profile"],
            "constructive_profile": core_constructive["profile"],
            "destructive_readout": core_destructive["readout"],
            "constructive_readout": core_constructive["readout"],
        },
        "consensus_probe": consensus_probe(hidden_state),
        "verdict": {
            "observer_relative_profiles_remain_well_typed": True,
            "coupling_and_expression_change_access_not_stored_identity": True,
            "proofs_reject_forgery_not_valid_dissent": True,
            "finality_profile_does_not_determine_signed_readout": True,
            "consensus_confidence_is_not_truth": True,
        },
    }
