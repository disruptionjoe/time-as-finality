"""Tests for T420 finite-cycle anti-relabel gate."""

from __future__ import annotations

import pytest

from models.finite_cycle_anti_relabel_gate import (
    audit_public_permutation,
    closed_cycle_transition,
    cycle_audit_for_label,
    run_t420_analysis,
    transition_from_labels,
)
from models.computational_arrow_of_time import N, SEED, forward, quad_residues


R = run_t420_analysis()


def test_t419_qr77_cycles_recover_predecessors_by_public_iteration():
    audit = R.t419_qr77_gate

    assert audit.name == "T419 QR_77 squaring permutation"
    assert audit.feasible_step_bound == 3
    assert audit.every_predecessor_recovered_within_bound is True
    assert audit.max_forward_steps_to_predecessor == 3
    assert audit.anti_relabel_claim_allowed is False
    assert audit.bounded_nonrecovery_is_evidence is False
    assert "absorbs_arrow" in audit.verdict


def test_t419_seed_orbit_is_period_four_with_public_predecessor():
    seed = R.t419_seed_orbit

    assert seed.start_label == SEED
    assert seed.cycle_labels == (4, 16, 25, 9)
    assert seed.cycle_length == 4
    assert seed.public_predecessor_label == 9
    assert seed.forward_steps_to_predecessor == 3
    assert seed.within_feasible_bound is True


def test_t419_full_transition_matches_public_squaring_on_qr77():
    labels = tuple(quad_residues(N))
    transition = transition_from_labels(labels, lambda x: forward(x, N))
    audit = audit_public_permutation(transition, labels=labels, feasible_step_bound=3)

    for cycle in audit.cycles:
        predecessor = cycle.public_predecessor_label
        assert forward(predecessor, N) == cycle.start_label


def test_bounded_nonrecovery_is_not_arrow_evidence():
    small = R.long_cycle_small_bound_control
    full = R.long_cycle_full_bound_control

    assert small.every_predecessor_recovered_within_bound is False
    assert small.anti_relabel_claim_allowed is False
    assert small.bounded_nonrecovery_is_evidence is False
    assert "period-hardness" in small.verdict
    assert full.every_predecessor_recovered_within_bound is True
    assert full.max_forward_steps_to_predecessor == 16


def test_exhaustive_small_cycles_obey_predecessor_formula():
    for length in range(2, 10):
        audit = audit_public_permutation(
            closed_cycle_transition(length),
            feasible_step_bound=length - 1,
            name=f"cycle-{length}",
        )
        assert audit.every_predecessor_recovered_within_bound is True
        assert audit.max_forward_steps_to_predecessor == length - 1
        only_cycle = audit.cycles[0]
        assert only_cycle.public_predecessor_label == length - 1


def test_cycle_lookup_rejects_missing_label():
    with pytest.raises(ValueError):
        cycle_audit_for_label(R.t419_qr77_gate, 999)


def test_invalid_transition_rejected():
    with pytest.raises(ValueError):
        audit_public_permutation((1, 1, 2))


def test_t420_is_guardrail_not_d2_discharge():
    assert R.claim_ledger_update.startswith("none")
    assert "period hardness" in R.redesign_rule
    assert "T110 blocks" in R.relation_to_t110
    assert "T417" in R.redesign_rule
