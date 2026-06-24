from fractions import Fraction

from models.mti_lp_harmonic_sanity import (
    beta_from_proxy,
    harmonic_mean,
    has_shared_edges,
    inverse_time_weights,
    lower_bound_lp_optimum,
    path_edge_loads,
    pure_lp_optimum,
)


def test_harmonic_proxy_is_not_the_lp_optimum_for_alpha_beta() -> None:
    alpha = (4, 2, 1)
    beta = (3, 2, 1)

    assert Fraction(harmonic_mean(alpha)).limit_denominator() == Fraction(12, 7)
    assert Fraction(harmonic_mean(beta)).limit_denominator() == Fraction(18, 11)
    assert pure_lp_optimum(alpha) == 1
    assert pure_lp_optimum(beta) == 1


def test_lower_bound_lp_keeps_excess_mass_on_shortest_path() -> None:
    alpha_weights, alpha_objective = lower_bound_lp_optimum((4, 2, 1), 0.1)
    beta_weights, beta_objective = lower_bound_lp_optimum((3, 2, 1), 0.1)

    assert alpha_weights == (0.1, 0.1, 0.8)
    assert beta_weights == (0.1, 0.1, 0.8)
    assert Fraction(alpha_objective).limit_denominator() == Fraction(7, 5)
    assert Fraction(beta_objective).limit_denominator() == Fraction(13, 10)


def test_inverse_time_weights_are_feasible_but_not_lp_optimal() -> None:
    weights = inverse_time_weights((4, 2, 1))
    objective = sum(weight * value for weight, value in zip(weights, (4, 2, 1)))

    assert tuple(Fraction(weight).limit_denominator() for weight in weights) == (
        Fraction(1, 7),
        Fraction(2, 7),
        Fraction(4, 7),
    )
    assert Fraction(objective).limit_denominator() == Fraction(12, 7)
    assert objective > lower_bound_lp_optimum((4, 2, 1), 0.1)[1]


def test_t195_arithmetic_values_remain_proxy_consistent() -> None:
    gamma = (4, 2, 5, 3)
    delta = (3, 2, 4, 3)

    assert Fraction(harmonic_mean(gamma)).limit_denominator() == Fraction(240, 77)
    assert Fraction(harmonic_mean(delta)).limit_denominator() == Fraction(48, 17)
    assert beta_from_proxy(harmonic_mean(delta), 5) > beta_from_proxy(
        harmonic_mean(gamma), 5
    )


def test_shared_edge_dag_fixture_flags_path_proxy_underdescription() -> None:
    paths = (
        ("s-a", "a-t"),
        ("s-b", "b-t"),
        ("s-a", "a-c", "c-t"),
        ("s-b", "b-c", "c-t"),
    )

    loads = path_edge_loads(paths)

    assert has_shared_edges(paths)
    assert loads["s-a"] == 2
    assert loads["s-b"] == 2
    assert loads["c-t"] == 2


def test_all_equal_paths_do_not_create_a_false_mismatch() -> None:
    values = (3, 3, 3)

    assert harmonic_mean(values) == pure_lp_optimum(values)
