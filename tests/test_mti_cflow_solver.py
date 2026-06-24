from fractions import Fraction

from models.mti_cflow_solver import (
    PathNetwork,
    RecordPolicy,
    disjoint_two_path_network,
    fixed_network_record_capability,
    harmonic_mean,
    has_shared_edges,
    shared_prefix_two_path_network,
    solve_minimax_cflow,
)


def assert_fraction(value: float, expected: Fraction) -> None:
    assert Fraction(value).limit_denominator(1000) == expected


def test_t204_disjoint_and_shared_prefix_values() -> None:
    disjoint = solve_minimax_cflow(disjoint_two_path_network())
    shared = solve_minimax_cflow(shared_prefix_two_path_network())

    assert disjoint.flows == (0.5, 0.5)
    assert shared.flows == (0.5, 0.5)
    assert_fraction(disjoint.value, Fraction(8, 3))
    assert_fraction(shared.value, Fraction(10, 3))
    assert shared.value > disjoint.value


def test_same_free_path_harmonic_different_cflow() -> None:
    disjoint = disjoint_two_path_network()
    shared = shared_prefix_two_path_network()

    assert disjoint.free_path_times() == (2, 2)
    assert shared.free_path_times() == (2, 2)
    assert harmonic_mean(disjoint.free_path_times()) == 2
    assert harmonic_mean(shared.free_path_times()) == 2
    assert solve_minimax_cflow(disjoint).value != solve_minimax_cflow(shared).value


def test_relabeling_preserves_cflow_value() -> None:
    original = disjoint_two_path_network()
    relabeled = PathNetwork(
        edges={
            "x-y": original.edges["s-a"],
            "y-z": original.edges["a-t"],
            "x-w": original.edges["s-b"],
            "w-z": original.edges["b-t"],
        },
        paths=(("x-y", "y-z"), ("x-w", "w-z")),
    )

    assert solve_minimax_cflow(original).value == solve_minimax_cflow(relabeled).value


def test_capacity_increase_reduces_or_preserves_cflow() -> None:
    base = shared_prefix_two_path_network()
    boosted = PathNetwork(
        edges={
            edge_id: edge if edge_id != "s-u" else type(edge)(edge.tau, edge.capacity * 2)
            for edge_id, edge in base.edges.items()
        },
        paths=base.paths,
    )

    assert solve_minimax_cflow(boosted).value < solve_minimax_cflow(base).value


def test_shared_edge_detection_distinguishes_path_proxy_from_flow_model() -> None:
    assert not has_shared_edges(disjoint_two_path_network().paths)
    assert has_shared_edges(shared_prefix_two_path_network().paths)


def test_fixed_native_network_record_finality_split() -> None:
    network = disjoint_two_path_network()
    append_policy = RecordPolicy(
        name="append-only", append_only=True, retains_history=True, challenge_window=1
    )
    overwrite_policy = RecordPolicy(
        name="overwrite", append_only=False, retains_history=False, challenge_window=0
    )

    append_cap = fixed_network_record_capability(network, append_policy)
    overwrite_cap = fixed_network_record_capability(network, overwrite_policy)

    assert append_cap[0] == overwrite_cap[0]
    assert append_cap[1] is True
    assert overwrite_cap[1] is False
