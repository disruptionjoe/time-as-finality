"""T522: recent test registry link audit.

High-volume progress runs update `TESTS.md` quickly. This gate treats the
recent T492+ registry segment as data and checks that each row points to a
real test spec, a real result Markdown artifact, and a matching Executable
Suite pointer.

Run: python -m models.test_registry_recent_link_audit
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re


TESTS_PATH = Path("TESTS.md")
RESULT_PATH = Path("results/T522-test-registry-recent-link-audit-v0.1.json")
MIN_RECENT_TEST_ID = 492

VERDICT_PASS = "RECENT_TEST_REGISTRY_LINKS_COHERENT"
VERDICT_FAIL = "RECENT_TEST_REGISTRY_LINKS_DRIFT"

TEST_ROW_RE = re.compile(
    r"^\| \[T(?P<id>\d+)\]\((?P<spec>tests/[^)]+)\) \| "
    r"(?P<title>[^|]+) \| (?P<targets>[^|]*) \| (?P<status>.*) \|$"
)
RESULT_PATH_RE = re.compile(r"results/[A-Za-z0-9_.\-/]+-results\.md")
HOME_PATH_RE = re.compile(r"(?:[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]|/Users/)")


@dataclass(frozen=True)
class RecentRegistryEntry:
    test_id: int
    spec_path: str
    title: str
    result_paths: tuple[str, ...]


@dataclass(frozen=True)
class RegistryLinkAudit:
    min_test_id: int
    max_test_id: int
    audited_count: int
    audited_ids: tuple[int, ...]
    missing_ids: tuple[int, ...]
    duplicate_ids: tuple[int, ...]
    missing_spec_paths: tuple[str, ...]
    spec_id_mismatches: tuple[str, ...]
    missing_result_links: tuple[int, ...]
    missing_result_paths: tuple[str, ...]
    missing_executable_suite_links: tuple[str, ...]
    home_path_hits: tuple[str, ...]
    verdict: str

    @property
    def passed(self) -> bool:
        return self.verdict == VERDICT_PASS

    def to_payload(self) -> dict[str, object]:
        payload = asdict(self)
        payload["artifact_id"] = "T522-test-registry-recent-link-audit-v0.1"
        payload["scope"] = "TESTS.md T492+ registry rows and Executable Suite links"
        payload["no_movement_boundary"] = (
            "registry hygiene only; no claim-ledger, canon verdict, roadmap, "
            "North Star, public-posture, detector-evidence, Jevons-accounting, "
            "external-publication, or cross-repo truth movement"
        )
        return payload


def audit_recent_registry(path: Path = TESTS_PATH) -> RegistryLinkAudit:
    text = path.read_text(encoding="utf-8")
    entries = _recent_entries(text)
    suite_paths = _executable_suite_result_paths(text)
    ids = tuple(entry.test_id for entry in entries)
    max_test_id = max(ids) if ids else MIN_RECENT_TEST_ID - 1
    expected_ids = tuple(range(MIN_RECENT_TEST_ID, max_test_id + 1))

    duplicate_ids = tuple(sorted({test_id for test_id in ids if ids.count(test_id) > 1}))
    missing_ids = tuple(test_id for test_id in expected_ids if test_id not in ids)
    missing_spec_paths = tuple(
        entry.spec_path for entry in entries if not Path(entry.spec_path).is_file()
    )
    spec_id_mismatches = tuple(
        f"T{entry.test_id}:{entry.spec_path}"
        for entry in entries
        if not Path(entry.spec_path).name.startswith(f"T{entry.test_id}-")
    )
    missing_result_links = tuple(entry.test_id for entry in entries if not entry.result_paths)
    missing_result_paths = tuple(
        result_path
        for entry in entries
        for result_path in entry.result_paths
        if not Path(result_path).is_file()
    )
    missing_suite_links = tuple(
        result_path
        for entry in entries
        for result_path in entry.result_paths
        if result_path not in suite_paths
    )
    home_path_hits = _home_path_hits(text, entries)

    blockers = (
        missing_ids
        + duplicate_ids
        + missing_spec_paths
        + spec_id_mismatches
        + missing_result_links
        + missing_result_paths
        + missing_suite_links
        + home_path_hits
    )
    verdict = VERDICT_FAIL if blockers or not entries else VERDICT_PASS

    return RegistryLinkAudit(
        min_test_id=MIN_RECENT_TEST_ID,
        max_test_id=max_test_id,
        audited_count=len(entries),
        audited_ids=ids,
        missing_ids=missing_ids,
        duplicate_ids=duplicate_ids,
        missing_spec_paths=missing_spec_paths,
        spec_id_mismatches=spec_id_mismatches,
        missing_result_links=missing_result_links,
        missing_result_paths=missing_result_paths,
        missing_executable_suite_links=missing_suite_links,
        home_path_hits=home_path_hits,
        verdict=verdict,
    )


def write_result(path: Path = RESULT_PATH) -> RegistryLinkAudit:
    audit = audit_recent_registry()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(audit.to_payload(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return audit


def _recent_entries(text: str) -> tuple[RecentRegistryEntry, ...]:
    entries: list[RecentRegistryEntry] = []
    for line in text.splitlines():
        match = TEST_ROW_RE.match(line)
        if not match:
            continue
        test_id = int(match.group("id"))
        if test_id < MIN_RECENT_TEST_ID:
            continue
        status = match.group("status")
        result_paths = tuple(dict.fromkeys(RESULT_PATH_RE.findall(status)))
        entries.append(
            RecentRegistryEntry(
                test_id=test_id,
                spec_path=match.group("spec"),
                title=match.group("title").strip(),
                result_paths=result_paths,
            )
        )
    return tuple(sorted(entries, key=lambda entry: entry.test_id))


def _executable_suite_result_paths(text: str) -> set[str]:
    section = _section(text, "## Executable Suite")
    return set(RESULT_PATH_RE.findall(section))


def _section(text: str, heading: str) -> str:
    start = text.index(heading)
    next_heading = text.find("\n## ", start + len(heading))
    if next_heading == -1:
        return text[start:]
    return text[start:next_heading]


def _home_path_hits(text: str, entries: tuple[RecentRegistryEntry, ...]) -> tuple[str, ...]:
    recent_ids = {entry.test_id for entry in entries}
    suite_section = _section(text, "## Executable Suite")
    hits: list[str] = []

    for line in text.splitlines():
        match = TEST_ROW_RE.match(line)
        if match and int(match.group("id")) in recent_ids and HOME_PATH_RE.search(line):
            hits.append(f"T{match.group('id')}:test-row")

    for line in suite_section.splitlines():
        if RESULT_PATH_RE.search(line) and HOME_PATH_RE.search(line):
            hits.append(f"executable-suite:{line.strip()[:80]}")

    return tuple(hits)


if __name__ == "__main__":
    result = write_result()
    print(json.dumps(result.to_payload(), indent=2, sort_keys=True))
