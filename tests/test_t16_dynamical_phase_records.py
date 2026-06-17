"""Unit tests for T16: dynamical phase-bearing records."""

from __future__ import annotations

import unittest

from models.emergence_lab import ElementaryCA, int_to_bits
from models.t16_dynamical_phase_records import (
    build_readout_graph,
    find_cancellation_trajectory,
    find_profile_separation_witness,
    run_t16_analysis,
    signed_trace_records,
    sweep_dynamic_phase_records,
)


class DynamicalPhaseRecordTests(unittest.TestCase):
    def test_signed_weights_are_derived_from_terminal_bit_direction(self) -> None:
        ca = ElementaryCA(110, 5)
        records = signed_trace_records(ca, int_to_bits(0b00100, 5), 2, 1)
        self.assertTrue(records)
        for record in records:
            self.assertNotEqual(record.baseline_bit, record.counterfactual_bit)
            self.assertEqual(
                record.weight,
                1 if record.baseline_bit == 0 else -1,
            )

    def test_profile_separation_witness_uses_same_profile_different_readout(self) -> None:
        witness = find_profile_separation_witness(width=4, max_layers=3)
        self.assertEqual(witness.left.profile, witness.right.profile)
        self.assertNotEqual(witness.left.readout, witness.right.readout)
        self.assertNotEqual(witness.left.weights, witness.right.weights)

    def test_generated_records_work_with_t13_readout_graph(self) -> None:
        witness = find_profile_separation_witness(width=4, max_layers=3).left
        graph, observer = build_readout_graph(witness)
        self.assertEqual(
            graph.finality_profile(observer, "X", "true", 1).as_tuple(),
            witness.profile,
        )
        self.assertEqual(graph.readout_born(observer, "X", "true"), witness.readout)

    def test_cancellation_trajectory_has_nonmonotone_readout(self) -> None:
        trajectory = find_cancellation_trajectory(width=4, max_layers=6)
        readouts = trajectory.readouts
        self.assertGreaterEqual(len(readouts), 3)
        self.assertTrue(
            any(
                readouts[i] > 0.0 and readouts[j] == 0.0 and readouts[k] > 0.0
                for i in range(len(readouts))
                for j in range(i + 1, len(readouts))
                for k in range(j + 1, len(readouts))
            )
        )

    def test_sweep_reports_separating_profiles_and_cancellation(self) -> None:
        summary = sweep_dynamic_phase_records(width=4, max_layers=3)
        self.assertGreater(summary["nonempty_trace_cases"], 0)
        self.assertGreater(summary["mixed_sign_fraction"], 0.0)
        self.assertGreater(summary["zero_readout_fraction"], 0.0)
        self.assertGreater(summary["separating_profile_count"], 0)

    def test_full_analysis_states_limits(self) -> None:
        result = run_t16_analysis()
        self.assertTrue(result["verdict"]["phase_weights_are_dynamically_derived"])
        self.assertTrue(result["verdict"]["does_not_derive_quantum_mechanics"])


if __name__ == "__main__":
    unittest.main()
