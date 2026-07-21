from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "steward" / "research-portfolio.json"


class HourlyResearchPortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(PORTFOLIO.read_text(encoding="utf-8"))

    def test_active_lane_frontier_state_is_explicit(self) -> None:
        lane_1 = next(
            group
            for group in self.data["work_groups"]
            if group["id"] == self.data["lane_1_work_group"]
        )
        self.assertEqual(lane_1["state"], "WAITING_FOR_SOURCE_PACKET")
        self.assertFalse(lane_1["hourly_eligible"])
        items = {item["id"]: item for item in lane_1["internal_work_items"]}
        ready = [
            item
            for item in lane_1["internal_work_items"]
            if item["state"] == "READY" and item["hourly_eligible"]
        ]
        self.assertEqual(ready, [])
        self.assertEqual(
            items["TAF-RECORD-CAPABILITY-ORDER"]["state"],
            "ENDPOINT_POSITIVE_REVIEW_ONLY",
        )
        self.assertFalse(items["TAF-RECORD-CAPABILITY-ORDER"]["hourly_eligible"])
        self.assertEqual(items["TAF-P2C-WITNESS-ADJUDICATION"]["state"], "GATED_FROZEN_PACKET")

    def test_gated_work_has_activation_and_material_rule(self) -> None:
        for group in self.data["work_groups"]:
            for item in group.get("internal_work_items", []):
                if item["state"].startswith("READY_AFTER") or item["state"].startswith("GATED"):
                    self.assertTrue(item.get("activation"))
        contract = self.data["selection_contract"]
        self.assertTrue(contract["select_highest_ranked_unblocked_item"])
        self.assertTrue(contract["rerank_after_every_material_run"])
        self.assertIn("insufficient", contract["minimum_material_output"])

    def test_t583_is_baseline_not_completion(self) -> None:
        lane_1 = next(
            group
            for group in self.data["work_groups"]
            if group["id"] == self.data["lane_1_work_group"]
        )
        self.assertIn("finite review instrument", lane_1["current_authority"])
        context = (ROOT / "LANES.yaml").read_text(encoding="utf-8")
        self.assertIn("steward/research-portfolio.json", context)
        self.assertIn("Formalization and truth testing", context)


if __name__ == "__main__":
    unittest.main()
