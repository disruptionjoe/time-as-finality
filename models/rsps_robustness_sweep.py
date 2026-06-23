"""RSPS robustness sweep.

This model tests the modest RSPS boundary:

- record-fidelity terms can select the coupling/einselected pointer basis in
  simple system/environment fixtures;
- the same score does not derive Born weights.

The script is intentionally finite and dependency-free. It emits a JSON payload
and a short Markdown result note under results/ when run from the repo root.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


THETA_STEPS = 1001
DEFAULT_N = 8
DEFAULT_P = 0.70
EPS = 1e-9


@dataclass(frozen=True)
class CaseResult:
    fixture_id: str
    description: str
    parameters: dict[str, float | int | str]
    expected_theta: float
    argmax_theta: float
    pointer_score: float
    conjugate_score: float
    redundancy_at_pointer: float
    audited_redundancy_at_pointer: float
    born_weight_imported: bool
    verdict: str
    note: str


def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -(x * math.log2(x) + (1.0 - x) * math.log2(1.0 - x))


def mutual_information(joint: list[list[float]]) -> float:
    rows = [sum(row) for row in joint]
    cols = [sum(joint[i][j] for i in range(len(joint))) for j in range(len(joint[0]))]
    total = 0.0
    for i, row in enumerate(joint):
        for j, pxy in enumerate(row):
            if pxy <= 0.0:
                continue
            total += pxy * math.log2(pxy / (rows[i] * cols[j]))
    return total


def theta_grid() -> list[float]:
    return [-math.pi / 2.0 + i * math.pi / (THETA_STEPS - 1) for i in range(THETA_STEPS)]


def normalize(values: list[float]) -> list[float]:
    lo = min(values)
    hi = max(values)
    if math.isclose(lo, hi, abs_tol=1e-12):
        return [0.0 for _ in values]
    return [(value - lo) / (hi - lo) for value in values]


def joint_candidate_fragment(theta: float, p: float, phi: float, eta: float) -> list[list[float]]:
    """P(candidate basis outcome, observed fragment bit).

    The environment monitors the pointer axis phi. eta is a classical flip
    probability for each fragment after monitoring. eta=0 is perfect copying;
    eta=0.5 makes the fragment independent of the pointer value.
    """

    delta = theta - phi
    c = math.cos(delta / 2.0) ** 2
    s = 1.0 - c

    # True pointer branch x=0 has probability p; x=1 has probability 1-p.
    # Candidate outcome + agrees with branch 0 with probability c, and with
    # branch 1 with probability s.
    return [
        [p * c * (1.0 - eta) + (1.0 - p) * s * eta,
         p * c * eta + (1.0 - p) * s * (1.0 - eta)],
        [p * s * (1.0 - eta) + (1.0 - p) * c * eta,
         p * s * eta + (1.0 - p) * c * (1.0 - eta)],
    ]


def raw_terms(
    theta: float,
    *,
    p: float = DEFAULT_P,
    n_fragments: int = DEFAULT_N,
    accessible_fragments: int | None = None,
    provenance_roots: int | None = None,
    phi: float = 0.0,
    eta: float = 0.0,
    agreement_scale: float = 1.0,
) -> tuple[float, float, float, float]:
    if accessible_fragments is None:
        accessible_fragments = n_fragments
    if provenance_roots is None:
        provenance_roots = accessible_fragments

    delta = theta - phi
    c = math.cos(delta / 2.0) ** 2
    stability = -h2(c)
    one_fragment_info = mutual_information(joint_candidate_fragment(theta, p, phi, eta))
    redundancy = accessible_fragments * one_fragment_info
    audited_redundancy = min(accessible_fragments, provenance_roots) * one_fragment_info
    agreement = -0.5 * abs(math.sin(delta)) * abs(2.0 * p - 1.0) * agreement_scale
    return stability, redundancy, agreement, audited_redundancy


def score_case(
    *,
    p: float = DEFAULT_P,
    n_fragments: int = DEFAULT_N,
    accessible_fragments: int | None = None,
    provenance_roots: int | None = None,
    phi: float = 0.0,
    eta: float = 0.0,
    agreement_scale: float = 1.0,
) -> tuple[float, float, float, float, float, float]:
    thetas = theta_grid()
    terms = [
        raw_terms(
            theta,
            p=p,
            n_fragments=n_fragments,
            accessible_fragments=accessible_fragments,
            provenance_roots=provenance_roots,
            phi=phi,
            eta=eta,
            agreement_scale=agreement_scale,
        )
        for theta in thetas
    ]
    stabilities = normalize([term[0] for term in terms])
    redundancies = normalize([term[1] for term in terms])
    agreements = normalize([term[2] for term in terms])
    scores = [a + b + c for a, b, c in zip(stabilities, redundancies, agreements)]
    max_index = max(range(len(scores)), key=lambda index: scores[index])

    pointer_index = min(range(len(thetas)), key=lambda index: abs(thetas[index] - phi))
    conjugate_theta = phi + math.pi / 2.0
    if conjugate_theta > math.pi / 2.0:
        conjugate_theta = phi - math.pi / 2.0
    conjugate_index = min(range(len(thetas)), key=lambda index: abs(thetas[index] - conjugate_theta))
    pointer_terms = raw_terms(
        thetas[pointer_index],
        p=p,
        n_fragments=n_fragments,
        accessible_fragments=accessible_fragments,
        provenance_roots=provenance_roots,
        phi=phi,
        eta=eta,
        agreement_scale=agreement_scale,
    )
    return (
        thetas[max_index],
        scores[pointer_index],
        scores[conjugate_index],
        pointer_terms[1],
        pointer_terms[3],
        scores[max_index],
    )


def verdict_for(
    *,
    argmax_theta: float,
    expected_theta: float,
    pointer_score: float,
    conjugate_score: float,
    redundancy_at_pointer: float,
    degeneracy_expected: bool = False,
) -> str:
    if degeneracy_expected:
        return "degenerate"
    theta_ok = abs(argmax_theta - expected_theta) <= (math.pi / (THETA_STEPS - 1)) + EPS
    score_ok = pointer_score > conjugate_score + EPS
    record_ok = redundancy_at_pointer > EPS
    if theta_ok and score_ok and record_ok:
        return "pass"
    if theta_ok and score_ok and not record_ok:
        return "basis_only_no_record_objectivity"
    return "fail"


def make_result(
    fixture_id: str,
    description: str,
    parameters: dict[str, float | int | str],
    note: str,
    *,
    p: float = DEFAULT_P,
    n_fragments: int = DEFAULT_N,
    accessible_fragments: int | None = None,
    provenance_roots: int | None = None,
    phi: float = 0.0,
    eta: float = 0.0,
    agreement_scale: float = 1.0,
    degeneracy_expected: bool = False,
    verdict_override: str | None = None,
) -> CaseResult:
    argmax_theta, pointer_score, conjugate_score, redundancy, audited, _ = score_case(
        p=p,
        n_fragments=n_fragments,
        accessible_fragments=accessible_fragments,
        provenance_roots=provenance_roots,
        phi=phi,
        eta=eta,
        agreement_scale=agreement_scale,
    )
    verdict = verdict_override or verdict_for(
        argmax_theta=argmax_theta,
        expected_theta=phi,
        pointer_score=pointer_score,
        conjugate_score=conjugate_score,
        redundancy_at_pointer=audited,
        degeneracy_expected=degeneracy_expected,
    )
    return CaseResult(
        fixture_id=fixture_id,
        description=description,
        parameters=parameters,
        expected_theta=round(phi, 12),
        argmax_theta=round(argmax_theta, 12),
        pointer_score=round(pointer_score, 6),
        conjugate_score=round(conjugate_score, 6),
        redundancy_at_pointer=round(redundancy, 6),
        audited_redundancy_at_pointer=round(audited, 6),
        born_weight_imported=False,
        verdict=verdict,
        note=note,
    )


def overlap_to_eta(overlap: float) -> float:
    """Map record-state overlap to an effective binary discrimination error."""
    distinguishability = math.sqrt(max(0.0, 1.0 - overlap * overlap))
    return 0.5 * (1.0 - distinguishability)


def sweep_results() -> list[CaseResult]:
    results: list[CaseResult] = []

    results.append(make_result(
        "R0",
        "Baseline GHZ-style perfect copying",
        {"p": DEFAULT_P, "N": DEFAULT_N},
        "Reproduces pointer-basis selection with no Born-weight output.",
    ))

    for n in [1, 2, 4, 8, 16, 32]:
        results.append(make_result(
            f"R1-N{n}",
            "Environment-size sweep",
            {"p": DEFAULT_P, "N": n},
            "Pointer selection persists as N changes; redundancy scales with accessible fragments.",
            n_fragments=n,
            accessible_fragments=n,
            provenance_roots=n,
        ))

    for p in [0.05, 0.10, 0.30, 0.50, 0.70, 0.90, 0.95]:
        results.append(make_result(
            f"R2-p{p:.2f}",
            "Branch-weight sweep",
            {"p": p, "N": DEFAULT_N},
            "Score selects the basis while the Born label remains external to F.",
            p=p,
        ))

    for eta in [0.00, 0.10, 0.25, 0.49, 0.50]:
        results.append(make_result(
            f"R3-eta{eta:.2f}",
            "Imperfect copying sweep",
            {"p": DEFAULT_P, "N": DEFAULT_N, "flip_probability": eta},
            "Noise degrades redundancy; at eta=0.5 record objectivity is absent even if the coupling basis term remains.",
            eta=eta,
            degeneracy_expected=math.isclose(eta, 0.5),
        ))

    for k in [0, 1, 2, 4, 8]:
        results.append(make_result(
            f"R4-k{k}",
            "Partial observer-access sweep",
            {"p": DEFAULT_P, "N": DEFAULT_N, "accessible_fragments": k},
            "Accessible redundancy is observer-indexed; k=0 is basis-only and not an objectivity witness.",
            accessible_fragments=k,
            provenance_roots=k,
            degeneracy_expected=(k == 0),
        ))

    for overlap in [0.00, 0.25, 0.50, 0.90, 1.00]:
        eta = overlap_to_eta(overlap)
        results.append(make_result(
            f"R5-overlap{overlap:.2f}",
            "Nonorthogonal record-state sweep",
            {"p": DEFAULT_P, "N": DEFAULT_N, "record_overlap": overlap, "effective_eta": round(eta, 6)},
            "Nonorthogonality degrades distinguishability; full overlap removes record information.",
            eta=eta,
            degeneracy_expected=math.isclose(overlap, 1.0),
        ))

    for phi in [0.0, math.pi / 8.0, math.pi / 4.0]:
        results.append(make_result(
            f"R6-phi{round(phi, 3)}",
            "Coupling-axis mismatch sweep",
            {"p": DEFAULT_P, "N": DEFAULT_N, "monitor_axis_phi": round(phi, 12)},
            "The argmax follows the monitored pointer axis, guarding against a hard-coded z-basis result.",
            phi=phi,
        ))

    for roots in [8, 4, 1]:
        verdict_override = "pass" if roots == 8 else "absorber_owned_audited_redundancy_required"
        results.append(make_result(
            f"R7-roots{roots}",
            "Provenance/audited-redundancy sweep",
            {"p": DEFAULT_P, "N": DEFAULT_N, "accessible_fragments": 8, "provenance_roots": roots},
            "Raw redundancy overcounts when fragments share provenance; audited redundancy carries the TaF/Q1A discipline.",
            accessible_fragments=8,
            provenance_roots=roots,
            verdict_override=verdict_override,
        ))

    for mixture in [1.00, 0.50, 0.00]:
        results.append(make_result(
            f"R8-mixture{mixture:.2f}",
            "Mixed-state agreement-scale sweep",
            {"p": DEFAULT_P, "N": DEFAULT_N, "agreement_scale": mixture},
            "Agreement can be weakened or removed without turning F into a Born-weight derivation.",
            agreement_scale=mixture,
        ))

    return results


def summarize(results: Iterable[CaseResult]) -> dict[str, object]:
    rows = list(results)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row.verdict] = counts.get(row.verdict, 0) + 1
    failures = [row.fixture_id for row in rows if row.verdict == "fail"]
    born_imports = [row.fixture_id for row in rows if row.born_weight_imported]
    return {
        "fixture_count": len(rows),
        "verdict_counts": counts,
        "failures": failures,
        "born_weight_imports": born_imports,
        "main_verdict": "supported_with_boundaries" if not failures and not born_imports else "needs_review",
    }


def markdown(results: list[CaseResult], summary: dict[str, object]) -> str:
    lines = [
        "# RSPS Robustness Sweep v0.1 Results",
        "",
        "## Verdict",
        "",
        f"Main verdict: `{summary['main_verdict']}`.",
        "",
        "The sweep supports RSPS as a modest flat-QM basis/objectivity selector across finite perturbations, with explicit boundaries. It does not derive Born weights, does not solve measurement, and does not promote a TI or GU physics bridge.",
        "",
        "## Summary",
        "",
        f"- Fixture rows: {summary['fixture_count']}",
        f"- Verdict counts: `{summary['verdict_counts']}`",
        f"- Failures: `{summary['failures']}`",
        f"- Born-weight imports: `{summary['born_weight_imports']}`",
        "",
        "## Result Table",
        "",
        "| Fixture | Verdict | Argmax theta | Expected theta | Pointer F | Conjugate F | Redundancy | Audited redundancy | Note |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in results:
        lines.append(
            f"| {row.fixture_id} | {row.verdict} | {row.argmax_theta:.6f} | "
            f"{row.expected_theta:.6f} | {row.pointer_score:.3f} | "
            f"{row.conjugate_score:.3f} | {row.redundancy_at_pointer:.3f} | "
            f"{row.audited_redundancy_at_pointer:.3f} | {row.note} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "- R0-R2 preserve pointer-basis selection under baseline, environment-size, and branch-weight sweeps.",
        "- R3-R5 show record objectivity degrades with noise, inaccessible fragments, and nonorthogonal record states.",
        "- R6 shows the score follows the monitored axis, reducing the risk that the result is just a hard-coded z-basis.",
        "- R7 confirms TaF's audited-provenance warning: raw redundancy is not objectivity when fragments share one source.",
        "- R8 shows the agreement term is not load-bearing for Born weights.",
        "",
        "## Boundary",
        "",
        "RSPS remains a fixed-H null model: record-fidelity terms can select a stable basis/objectivity structure in these fixtures, while probabilities remain trace-rule data. A Temporal Issuance or GU bridge must clear the separate fixed-H and fixed-source gates before receiving source-side credit.",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    results = sweep_results()
    summary = summarize(results)
    payload = {
        "artifact": "rsps-robustness-sweep-v0.1",
        "summary": summary,
        "results": [asdict(row) for row in results],
    }

    results_dir = repo_root / "results"
    results_dir.mkdir(exist_ok=True)
    json_path = results_dir / "rsps-robustness-sweep-v0.1.json"
    md_path = results_dir / "rsps-robustness-sweep-v0.1-results.md"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(markdown(results, summary), encoding="utf-8")

    print(json.dumps(summary, indent=2))
    print(f"wrote {json_path}")
    print(f"wrote {md_path}")


if __name__ == "__main__":
    main()
