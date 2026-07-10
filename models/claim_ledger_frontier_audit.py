"""T523: claim-ledger frontier audit.

The Ledger Reconciliation Trigger may honestly leave a frontier due, but the
frontier declaration itself should stay mechanically checkable. This audit
verifies that the Canon Index coverage note names the current test-registry
ceiling and separates still-untriaged tests from already-routed no-row
infrastructure.

Run: python -m models.claim_ledger_frontier_audit
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re


TESTS_PATH = Path("TESTS.md")
CLAIM_LEDGER_PATH = Path("CLAIM-LEDGER.md")
RESULT_PATH = Path("results/T523-claim-ledger-frontier-audit-v0.1.json")

EXPECTED_MAX_TEST_ID = 525
EXPECTED_UNTRIAGED_RANGES = ((249, 513),)

VERDICT_PASS = "CLAIM_LEDGER_FRONTIER_DECLARED_COHERENT"
VERDICT_FAIL = "CLAIM_LEDGER_FRONTIER_DECLARATION_DRIFT"

TEST_ID_RE = re.compile(r"^\| \[T(?P<id>\d+)\]\(tests/", re.MULTILINE)
COVERAGE_MAX_RE = re.compile(r"test registry \(`TESTS\.md`\) is now at \*\*T(?P<id>\d+)\*\*")
UNTRIAGED_RE = re.compile(r"un-triaged frontier remains \*\*(?P<ranges>[^*]+)\*\*")
RANGE_RE = re.compile(r"T(?P<start>\d+)(?:-T?(?P<end>\d+))?")


@dataclass(frozen=True)
class ClaimLedgerFrontierAudit:
    max_test_id: int
    coverage_note_max_test_id: int | None
    declared_untriaged_ranges: tuple[tuple[int, int], ...]
    expected_untriaged_ranges: tuple[tuple[int, int], ...]
    t517_t519_no_row_receipt_present: bool
    t521_t523_infrastructure_no_row_present: bool
    t524_diagnostic_repair_no_status_movement_present: bool
    t525_repaired_suite_no_status_movement_present: bool
    twl_claim_row_present: bool
    t523_claim_row_present: bool
    t524_claim_row_present: bool
    t525_claim_row_present: bool
    blockers: tuple[str, ...]
    verdict: str

    @property
    def passed(self) -> bool:
        return self.verdict == VERDICT_PASS

    def to_payload(self) -> dict[str, object]:
        payload = asdict(self)
        payload["artifact_id"] = "T523-claim-ledger-frontier-audit-v0.1"
        payload["scope"] = "CLAIM-LEDGER.md Canon Index coverage note and TESTS.md ceiling"
        payload["no_movement_boundary"] = (
            "ledger-frontier declaration only; no claim-status, canon-verdict, "
            "Canon Index tier, roadmap, North Star, public-posture, external-"
            "publication, or cross-repo truth movement"
        )
        return payload


def audit_claim_ledger_frontier(
    tests_path: Path = TESTS_PATH,
    claim_ledger_path: Path = CLAIM_LEDGER_PATH,
) -> ClaimLedgerFrontierAudit:
    tests_text = tests_path.read_text(encoding="utf-8")
    ledger_text = claim_ledger_path.read_text(encoding="utf-8")

    max_test_id = max(int(match.group("id")) for match in TEST_ID_RE.finditer(tests_text))
    coverage_note = _coverage_supersession_note(ledger_text)
    coverage_note_max = _coverage_note_max_test_id(coverage_note)
    declared_untriaged = _declared_untriaged_ranges(coverage_note)
    t517_t519_no_row_receipt = _nearby_contains(
        ledger_text,
        "T517",
        required=("T519", "no rows"),
    )
    t521_t523_infra_no_row = all(token in coverage_note for token in ("T521", "T522", "T523"))
    t524_no_status_movement = _nearby_contains(
        coverage_note,
        "T524",
        required=("S1 diagnostic-repair", "no claim row", "claim-status movement"),
    )
    t525_no_status_movement = _nearby_contains(
        coverage_note,
        "T525",
        required=("S1 repaired-suite", "no claim row", "claim-status movement"),
    )
    twl_claim_row_present = "| [TWL](" in ledger_text
    t523_claim_row_present = "| [T523](" in ledger_text
    t524_claim_row_present = "| [T524](" in ledger_text
    t525_claim_row_present = "| [T525](" in ledger_text

    blockers: list[str] = []
    if max_test_id != EXPECTED_MAX_TEST_ID:
        blockers.append(f"max_test_id={max_test_id}, expected {EXPECTED_MAX_TEST_ID}")
    if coverage_note_max != max_test_id:
        blockers.append(f"coverage_note_max={coverage_note_max}, max_test_id={max_test_id}")
    if declared_untriaged != EXPECTED_UNTRIAGED_RANGES:
        blockers.append(
            f"declared_untriaged={declared_untriaged}, expected {EXPECTED_UNTRIAGED_RANGES}"
        )
    if not t517_t519_no_row_receipt:
        blockers.append("missing T517-T519 no-row receipt")
    if not t521_t523_infra_no_row:
        blockers.append("missing T521-T523 infrastructure no-row language")
    if not t524_no_status_movement:
        blockers.append("missing T524 diagnostic-repair no-status-movement language")
    if not t525_no_status_movement:
        blockers.append("missing T525 repaired-suite no-status-movement language")
    if not twl_claim_row_present:
        blockers.append("missing TWL claim row")
    if t523_claim_row_present:
        blockers.append("T523 unexpectedly has a claim row")
    if t524_claim_row_present:
        blockers.append("T524 unexpectedly has a claim row")
    if t525_claim_row_present:
        blockers.append("T525 unexpectedly has a claim row")

    verdict = VERDICT_FAIL if blockers else VERDICT_PASS
    return ClaimLedgerFrontierAudit(
        max_test_id=max_test_id,
        coverage_note_max_test_id=coverage_note_max,
        declared_untriaged_ranges=declared_untriaged,
        expected_untriaged_ranges=EXPECTED_UNTRIAGED_RANGES,
        t517_t519_no_row_receipt_present=t517_t519_no_row_receipt,
        t521_t523_infrastructure_no_row_present=t521_t523_infra_no_row,
        t524_diagnostic_repair_no_status_movement_present=t524_no_status_movement,
        t525_repaired_suite_no_status_movement_present=t525_no_status_movement,
        twl_claim_row_present=twl_claim_row_present,
        t523_claim_row_present=t523_claim_row_present,
        t524_claim_row_present=t524_claim_row_present,
        t525_claim_row_present=t525_claim_row_present,
        blockers=tuple(blockers),
        verdict=verdict,
    )


def write_result(path: Path = RESULT_PATH) -> ClaimLedgerFrontierAudit:
    audit = audit_claim_ledger_frontier()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(audit.to_payload(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return audit


def _coverage_supersession_note(text: str) -> str:
    marker = "**Coverage / staleness supersession (2026-07-10).**"
    start = text.index(marker)
    next_note = text.find("\n\n**", start + len(marker))
    if next_note == -1:
        return text[start:]
    return text[start:next_note]


def _coverage_note_max_test_id(note: str) -> int | None:
    match = COVERAGE_MAX_RE.search(note)
    if not match:
        return None
    return int(match.group("id"))


def _declared_untriaged_ranges(note: str) -> tuple[tuple[int, int], ...]:
    match = UNTRIAGED_RE.search(note)
    if not match:
        return ()
    ranges: list[tuple[int, int]] = []
    for range_match in RANGE_RE.finditer(match.group("ranges")):
        start = int(range_match.group("start"))
        end = int(range_match.group("end") or start)
        ranges.append((start, end))
    return tuple(ranges)


def _nearby_contains(text: str, anchor: str, required: tuple[str, ...], window: int = 800) -> bool:
    for match in re.finditer(re.escape(anchor), text):
        chunk = text[match.start() : match.start() + window]
        lowered = chunk.lower()
        if all(token.lower() in lowered for token in required):
            return True
    return False


if __name__ == "__main__":
    result = write_result()
    print(json.dumps(result.to_payload(), indent=2, sort_keys=True))
