"""T521: detector pre-registration manifest template gate.

T136 sharpened the Q1B detector route to one pre-event object: a signed
manifest that binds T97 table commitments, T121/T133 wrapper-field
commitments, T100 authority separation, the claimed tier, and the no-data
boundary before detector event collection. T136's recommended next step was a
human-fillable template.

This gate treats the Markdown template as data and checks that it covers the
T136 obligations without smuggling observed detector payload values into the
pre-data manifest.

Run: python -m models.detector_manifest_template_gate
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re

from models.detector_authority_domain_bound import DOMAINS
from models.detector_dry_run_packet_skeleton import locked_detector_dry_run_packet_skeleton
from models.detector_preregistration_manifest import (
    ALLOWED_TIERS,
    CLAIM_REVIEW_EXTENSION_FIELDS,
    PROVISIONAL_ADMISSION_FIELDS,
)
from models.real_detector_packet_schema_audit import SCHEMA_FIELDS


TEMPLATE_PATH = Path("templates/detector-preregistration-manifest.template.md")
RESULT_PATH = Path("results/T521-detector-manifest-template-gate-v0.1.json")

OBSERVED_VALUE_KIND = "observed_value_commitment"
VERDICT_PASS = "DETECTOR_MANIFEST_TEMPLATE_GATE_BUILT_REVIEW_ONLY"
VERDICT_FAIL = "DETECTOR_MANIFEST_TEMPLATE_GATE_FAILED"


@dataclass(frozen=True)
class TemplateGateAudit:
    template_path: str
    missing_t97_tables: tuple[str, ...]
    missing_wrapper_fields: tuple[str, ...]
    wrong_commitment_kinds: tuple[str, ...]
    missing_authority_domains: tuple[str, ...]
    missing_tier_choices: tuple[str, ...]
    has_no_data_boundary: bool
    has_observed_value_commitment: bool
    verdict: str

    @property
    def passed(self) -> bool:
        return self.verdict == VERDICT_PASS


def audit_template(path: Path = TEMPLATE_PATH) -> TemplateGateAudit:
    text = path.read_text(encoding="utf-8")
    t97_tables = _first_cells(_section(text, "T97 Table Commitments"))
    wrapper_rows = _rows_by_first_cell(_section(text, "T121/T133 Wrapper Field Commitments"))
    authority_domains = _authority_domains(_section(text, "Authority Partition"))
    tier_choices = _checked_choices(_section(text, "Claimed Tier"))

    expected_t97 = tuple(table.table_name for table in locked_detector_dry_run_packet_skeleton().tables)
    missing_t97 = tuple(name for name in expected_t97 if name not in t97_tables)
    missing_wrapper = tuple(field for field in SCHEMA_FIELDS if field not in wrapper_rows)
    wrong_kinds = tuple(
        f"{field}:{wrapper_rows[field][1]}!= {expected_commitment_kind(field)}"
        for field in SCHEMA_FIELDS
        if field in wrapper_rows and wrapper_rows[field][1] != expected_commitment_kind(field)
    )
    missing_authority = tuple(domain for domain in DOMAINS if domain not in authority_domains)
    missing_tiers = tuple(tier for tier in ALLOWED_TIERS if tier not in tier_choices)
    has_no_data_boundary = all(
        phrase in text
        for phrase in (
            "No data analyzed before manifest lock",
            "Do not enter detector outcome values before event collection",
            "No detector event rows or payload values inspected before manifest lock",
        )
    )
    has_observed_value_kind = OBSERVED_VALUE_KIND in text

    passed = not any(
        (
            missing_t97,
            missing_wrapper,
            wrong_kinds,
            missing_authority,
            missing_tiers,
            not has_no_data_boundary,
            has_observed_value_kind,
        )
    )

    return TemplateGateAudit(
        template_path=str(path),
        missing_t97_tables=missing_t97,
        missing_wrapper_fields=missing_wrapper,
        wrong_commitment_kinds=wrong_kinds,
        missing_authority_domains=missing_authority,
        missing_tier_choices=missing_tiers,
        has_no_data_boundary=has_no_data_boundary,
        has_observed_value_commitment=has_observed_value_kind,
        verdict=VERDICT_PASS if passed else VERDICT_FAIL,
    )


def expected_commitment_kind(field: str) -> str:
    if field in {"raw_measurement_payload", "causal_ordering_data"}:
        return "export_rule_commitment"
    if field in {"publication_status", "revocation_status", "key_state", "challenge_status"}:
        return "state_commitment"
    return "schema_commitment"


def audit_to_dict(audit: TemplateGateAudit) -> dict[str, object]:
    return {
        "artifact_id": "T521-detector-manifest-template-gate-v0.1",
        "template_path": audit.template_path,
        "verdict": audit.verdict,
        "missing_t97_tables": list(audit.missing_t97_tables),
        "missing_wrapper_fields": list(audit.missing_wrapper_fields),
        "wrong_commitment_kinds": list(audit.wrong_commitment_kinds),
        "missing_authority_domains": list(audit.missing_authority_domains),
        "missing_tier_choices": list(audit.missing_tier_choices),
        "has_no_data_boundary": audit.has_no_data_boundary,
        "has_observed_value_commitment": audit.has_observed_value_commitment,
        "required_claim_review_fields": list(
            PROVISIONAL_ADMISSION_FIELDS + CLAIM_REVIEW_EXTENSION_FIELDS
        ),
        "scope_boundary": (
            "Template/review gate only: no detector evidence, Q1B movement, claim-ledger "
            "movement, public-posture movement, external publication, or observed payload values."
        ),
    }


def write_result(path: Path = RESULT_PATH) -> TemplateGateAudit:
    audit = audit_template()
    path.write_text(json.dumps(audit_to_dict(audit), indent=2) + "\n", encoding="utf-8")
    return audit


def _section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    return match.group("body")


def _markdown_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in stripped.strip("|").split("|")]
        if not cells or cells[0] in {"---", "Table", "Field"}:
            continue
        if all(set(cell) <= {"-", " "} for cell in cells):
            continue
        rows.append(cells)
    return rows


def _first_cells(section: str) -> tuple[str, ...]:
    return tuple(row[0] for row in _markdown_rows(section))


def _rows_by_first_cell(section: str) -> dict[str, list[str]]:
    return {row[0]: row for row in _markdown_rows(section) if row}


def _authority_domains(section: str) -> tuple[str, ...]:
    domains: list[str] = []
    for line in section.splitlines():
        match = re.match(r"^-\s+([a-z_]+):", line.strip())
        if match:
            domains.append(match.group(1))
    return tuple(domains)


def _checked_choices(section: str) -> tuple[str, ...]:
    choices: list[str] = []
    for line in section.splitlines():
        match = re.match(r"^-\s+\[ \]\s+([a-z_]+)", line.strip())
        if match:
            choices.append(match.group(1))
    return tuple(choices)


def main() -> None:
    audit = write_result()
    print("[T521] detector manifest template gate")
    print(f"  verdict: {audit.verdict}")
    print(f"  missing T97 tables: {len(audit.missing_t97_tables)}")
    print(f"  missing wrapper fields: {len(audit.missing_wrapper_fields)}")
    print(f"  wrong commitment kinds: {len(audit.wrong_commitment_kinds)}")
    print(f"  missing authority domains: {len(audit.missing_authority_domains)}")
    print(f"  missing tier choices: {len(audit.missing_tier_choices)}")
    if not audit.passed:
        raise SystemExit(1)
    print("  exit 0 = template covers the T136 pre-event manifest gate.")


if __name__ == "__main__":
    main()
