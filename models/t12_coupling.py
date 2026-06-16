"""T12: coupling-profile reconstruction on the T1 causal record graph.

Typed extension of the T1 model. Records carry channel tags; observers carry
coupling profiles. Reconstruction runs the unmodified T1 machinery on the
observer's coupled view, so any divergence between observers is attributable
solely to coupling profiles. No T1 source is modified.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.t1_record_graph import CausalRecordGraph, Observer, Record

UNCONDITIONAL = "unconditional"
CONDITIONAL = "conditional"


@dataclass(frozen=True)
class ChannelTag:
    channel: str
    binding: str = UNCONDITIONAL


@dataclass(frozen=True)
class CouplingObserver:
    observer_id: str
    event: str
    profile: frozenset[str]
    accepts_conditional: bool = True


class CouplingRecordGraph(CausalRecordGraph):
    """Causal record graph whose records carry channel tags."""

    def __init__(self) -> None:
        super().__init__()
        self.channel_tags: dict[str, ChannelTag] = {}

    def add_channel_record(self, record: Record, channel: str, binding: str = UNCONDITIONAL) -> None:
        if binding not in (UNCONDITIONAL, CONDITIONAL):
            raise ValueError(f"unknown binding: {binding!r}")
        self.add_record(record)
        self.channel_tags[record.record_id] = ChannelTag(channel, binding)

    def all_holders(self) -> frozenset[str]:
        return frozenset(record.holder for record in self.records.values())

    def coupled_view(self, profile: frozenset[str]) -> CausalRecordGraph:
        """The graph as filtered by a coupling profile.

        Events and causal edges are preserved in full (causal structure is
        not observer-relative); only record visibility is filtered.
        """
        view = CausalRecordGraph()
        for event in self.events:
            view.add_event(event)
        for earlier in self.events:
            for later in self._successors[earlier]:
                view.add_causal_edge(earlier, later)
        for record in self.records.values():
            if self.channel_tags[record.record_id].channel in profile:
                view.add_record(record)
        return view

    def _t1_observer(self, observer: CouplingObserver) -> Observer:
        return Observer(observer.observer_id, observer.event, self.all_holders())

    def reconstructible(
        self, observer: CouplingObserver, proposition: str, threshold: int
    ) -> bool:
        view = self.coupled_view(observer.profile)
        return view.reconstruct_value(self._t1_observer(observer), proposition, threshold) is not None

    def observer_relation(
        self,
        observer: CouplingObserver,
        propositions: tuple[str, ...],
        threshold: int,
    ) -> frozenset[tuple[str, str]]:
        view = self.coupled_view(observer.profile)
        visible = tuple(
            proposition
            for proposition in propositions
            if view.reconstruct_value(self._t1_observer(observer), proposition, threshold) is not None
        )
        return view.reconstructed_relation(self._t1_observer(observer), visible, threshold)

    def proposition_channel(self, proposition: str) -> ChannelTag:
        tags = {
            self.channel_tags[record.record_id]
            for record in self.records.values()
            if record.proposition == proposition
        }
        if len(tags) != 1:
            raise ValueError(f"proposition {proposition!r} must use exactly one channel tag in T12")
        return next(iter(tags))

    def constrained(
        self, observer: CouplingObserver, proposition: str, threshold: int
    ) -> bool:
        tag = self.proposition_channel(proposition)
        if tag.channel not in observer.profile:
            return False
        if not self.reconstructible(observer, proposition, threshold):
            return False
        if tag.binding == CONDITIONAL and not observer.accepts_conditional:
            return False
        return True

    def reach(self, proposition: str, population: tuple[CouplingObserver, ...]) -> float:
        tag = self.proposition_channel(proposition)
        coupled = [observer for observer in population if tag.channel in observer.profile]
        return len(coupled) / len(population)

    def hardness(
        self, proposition: str, population: tuple[CouplingObserver, ...], threshold: int
    ) -> float:
        tag = self.proposition_channel(proposition)
        coupled = [observer for observer in population if tag.channel in observer.profile]
        if not coupled:
            return 0.0
        constrained = [observer for observer in coupled if self.constrained(observer, proposition, threshold)]
        return len(constrained) / len(coupled)


def build_t12_scenario() -> tuple[CouplingRecordGraph, tuple[CouplingObserver, ...]]:
    """Four propositions on three channels, four observers, threshold 2."""
    graph = CouplingRecordGraph()
    events = ("a", "a2", "b", "b2", "d", "d2", "merge", "c", "c2", "observe")
    for event in events:
        graph.add_event(event)
    for earlier, later in (
        ("a", "a2"),
        ("b", "b2"),
        ("d", "d2"),
        ("a2", "merge"),
        ("b2", "merge"),
        ("d2", "merge"),
        ("merge", "c"),
        ("c", "c2"),
        ("c2", "observe"),
    ):
        graph.add_causal_edge(earlier, later)

    channel_records = (
        (Record("ra1", "A", "true", "a", "ha1", 1.0), "grav", UNCONDITIONAL),
        (Record("ra2", "A", "true", "a2", "ha2", 1.0), "grav", UNCONDITIONAL),
        (Record("rb1", "B", "true", "b", "hb1", 1.0), "em", UNCONDITIONAL),
        (Record("rb2", "B", "true", "b2", "hb2", 1.0), "em", UNCONDITIONAL),
        (Record("rd1", "D", "true", "d", "hd1", 1.0), "social", CONDITIONAL),
        (Record("rd2", "D", "true", "d2", "hd2", 1.0), "social", CONDITIONAL),
        (Record("rc1", "C", "true", "c", "hc1", 1.0), "grav", UNCONDITIONAL),
        (Record("rc2", "C", "true", "c2", "hc2", 1.0), "grav", UNCONDITIONAL),
    )
    for record, channel, binding in channel_records:
        graph.add_channel_record(record, channel, binding)

    population = (
        CouplingObserver("O1", "observe", frozenset({"grav", "em"})),
        CouplingObserver("O2", "observe", frozenset({"grav", "social"}), accepts_conditional=True),
        CouplingObserver("O3", "observe", frozenset({"grav"})),
        CouplingObserver("O4", "observe", frozenset({"grav", "social"}), accepts_conditional=False),
    )
    return graph, population


def omniscient_relation(
    graph: CouplingRecordGraph, propositions: tuple[str, ...], threshold: int
) -> frozenset[tuple[str, str]]:
    all_channels = frozenset(tag.channel for tag in graph.channel_tags.values())
    omniscient = CouplingObserver("omni", "observe", all_channels)
    return graph.observer_relation(omniscient, propositions, threshold)
