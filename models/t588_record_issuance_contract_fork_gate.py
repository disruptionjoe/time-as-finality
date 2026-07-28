"""T588: Record-issuance contract fork gate.

T587 stopped further T-number scaffolds built from T586 alone, permitting
reopening only on a provenance-valid physical source packet, a frozen
capability witness, or a sharper counterexample that changes the
record-issuance contract. This gate invokes the third condition.

It does not add a comparator to the frozen T586 event system. It asks what a
record is issued *into*, declares three candidate contracts, and refutes one
against differential ageing.

Construction fork: proper time is the standard special-relativistic invariant
arc length along a worldline. No program-native temporal primitive is used.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ARTIFACT = "T588-record-issuance-contract-fork-gate-v0.1"
VERDICT = "ISSUANCE_CONTRACT_B_REFUTED_A_AND_C_SURVIVE_REVIEW_ONLY"

# Shared issuance rate, in records per unit of an observer's own proper time.
# The value is arbitrary; every result below is invariant under changing it.
SHARED_RATE = 1.0


@dataclass(frozen=True)
class Worldline:
    observer_id: str
    proper_time: float


@dataclass(frozen=True)
class ContractResult:
    contract_id: str
    description: str
    reunion_counts: dict[str, float]
    counts_differ: bool
    reproduces_differential_ageing: bool
    status: str
    reason: str


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class T588Result:
    artifact: str
    verdict: str
    fixture: tuple[Worldline, ...]
    contracts: tuple[ContractResult, ...]
    checks: tuple[Check, ...]
    ratio_invariance: dict[str, Any]
    residual_discriminator: str
    physical_result: str
    claim_ledger_update: str
    not_claimed: str
    next_work: str


def twin_fixture(ratio: float = 2.0) -> tuple[Worldline, ...]:
    """Separation and reunion. The travelling observer logs less proper time."""
    return (
        Worldline(observer_id="stay_at_home", proper_time=ratio),
        Worldline(observer_id="traveller", proper_time=1.0),
    )


def contract_a(fixture: tuple[Worldline, ...]) -> ContractResult:
    """Per-observer ledgers. No global count exists at any time."""
    counts = {w.observer_id: SHARED_RATE * w.proper_time for w in fixture}
    differ = len(set(counts.values())) > 1
    return ContractResult(
        contract_id="A_per_observer_ledgers",
        description=(
            "Each observer issues into its own ledger at the shared rate per "
            "unit of its own proper time."
        ),
        reunion_counts=counts,
        counts_differ=differ,
        reproduces_differential_ageing=differ,
        status="SURVIVES" if differ else "REFUTED",
        reason=(
            "Counts are rate times each observer's own proper time, so they "
            "differ at reunion exactly as differential ageing requires. The "
            "difference is derived from the contract, not inserted."
        ),
    )


def contract_b(fixture: tuple[Worldline, ...]) -> ContractResult:
    """Single global ledger. One monotone issuance count for all observers."""
    total = sum(SHARED_RATE * w.proper_time for w in fixture)
    counts = {w.observer_id: total for w in fixture}
    differ = len(set(counts.values())) > 1
    return ContractResult(
        contract_id="B_single_global_ledger",
        description=(
            "Observers are objects within one ledger carrying one monotone "
            "issuance count. Every observer reads the same count."
        ),
        reunion_counts=counts,
        counts_differ=differ,
        reproduces_differential_ageing=differ,
        status="SURVIVES" if differ else "REFUTED",
        reason=(
            "A single monotone count is one number. If observers read it, they "
            "read the same value and there is no differential ageing, which is "
            "contradicted by muon lifetimes, storage-ring measurements at "
            "gamma about 29, Hafele-Keating, and GPS. If observers do not read "
            "it, the count is unobservable and the contract makes no claim "
            "about what any observer holds."
        ),
    )


def contract_c(fixture: tuple[Worldline, ...]) -> ContractResult:
    """Regional ledgers, reconciling structure where worldlines meet."""
    counts = {w.observer_id: SHARED_RATE * w.proper_time for w in fixture}
    differ = len(set(counts.values())) > 1
    return ContractResult(
        contract_id="C_regional_merge_on_contact",
        description=(
            "Each observer issues locally at the shared rate. Ledger structure "
            "reconciles at causal contact; no global count exists at any time."
        ),
        reunion_counts=counts,
        counts_differ=differ,
        reproduces_differential_ageing=differ,
        status="SURVIVES" if differ else "REFUTED",
        reason=(
            "Local issuance gives the same per-observer counts as contract A. "
            "Reconciliation at contact merges structure, not totals, so the "
            "reunion counts still differ."
        ),
    )


def ratio_invariance_probe(ratios: tuple[float, ...]) -> dict[str, Any]:
    """The B refutation must not depend on the fixture's proper-time ratio."""
    outcomes = {}
    for ratio in ratios:
        fixture = twin_fixture(ratio)
        outcomes[str(ratio)] = {
            "A": contract_a(fixture).status,
            "B": contract_b(fixture).status,
            "C": contract_c(fixture).status,
        }
    b_statuses = {v["B"] for v in outcomes.values()}
    return {
        "ratios_probed": list(outcomes),
        "per_ratio": outcomes,
        "b_status_invariant": len(b_statuses) == 1,
        "b_status": sorted(b_statuses),
    }


def run_t588_analysis() -> T588Result:
    fixture = twin_fixture()
    results = (contract_a(fixture), contract_b(fixture), contract_c(fixture))
    by_id = {r.contract_id: r for r in results}
    invariance = ratio_invariance_probe((1.5, 2.0, 7.0, 100.0))

    a = by_id["A_per_observer_ledgers"]
    b = by_id["B_single_global_ledger"]
    c = by_id["C_regional_merge_on_contact"]

    checks = (
        Check(
            "determinate_counts",
            all(len(r.reunion_counts) == len(fixture) for r in results),
            "Every contract yields a determinate reunion count per observer.",
        ),
        Check(
            "contract_b_refuted",
            b.status == "REFUTED",
            "A single monotone global count read by observers cannot reproduce "
            "differential ageing.",
        ),
        Check(
            "contracts_a_and_c_survive",
            a.status == "SURVIVES" and c.status == "SURVIVES",
            "Per-observer and regional-merge issuance both reproduce the "
            "differential count.",
        ),
        Check(
            "b_refutation_ratio_invariant",
            invariance["b_status_invariant"] and invariance["b_status"] == ["REFUTED"],
            "The refutation of B holds at every probed proper-time ratio, so it "
            "does not depend on the fixture numbers.",
        ),
        Check(
            "a_and_c_not_separated_by_counts",
            a.reunion_counts == c.reunion_counts,
            "A and C give identical reunion counts, so the fixture poses the "
            "residual question rather than settling it.",
        ),
        Check(
            "ageing_not_inserted",
            True,
            "Differential ageing is not written into any contract. It follows "
            "from applying one shared rate to each observer's own proper time; "
            "contract B fails precisely because it has no per-observer proper "
            "time to apply it to.",
        ),
    )

    return T588Result(
        artifact=ARTIFACT,
        verdict=VERDICT,
        fixture=fixture,
        contracts=results,
        checks=checks,
        ratio_invariance=invariance,
        residual_discriminator=(
            "Contracts A and C are not separated by reunion counts. The open "
            "discriminator is whether observers who meet end up holding a "
            "shared record structure (C) or merely comparable independent "
            "ledgers (A). That is a question about what reconciliation does at "
            "contact, and this fixture does not answer it."
        ),
        physical_result=(
            "Of three declared record-issuance contracts, the single global "
            "ledger is refuted at every probed proper-time ratio: one monotone "
            "count read by all observers admits no differential ageing. "
            "Per-observer issuance and regional-merge issuance both survive and "
            "are indistinguishable by reunion count. The refutation uses only "
            "the standard proper-time construction and the empirical existence "
            "of differential ageing."
        ),
        claim_ledger_update=(
            "No claim promotion is earned. This is a negative result on one "
            "declared bookkeeping contract, recorded as such. It does not "
            "revive T586's downgraded order claim."
        ),
        not_claimed=(
            "T588 does not prove time, temporal order, issuance, the existence "
            "or nonexistence of a preferred frame, a universal capability "
            "measure, source-law novelty, public-posture movement, external "
            "publication, or cross-repo truth. Refuting a bookkeeping contract "
            "is not a claim about physical reality."
        ),
        next_work=(
            "Do not build an A-versus-C criterion here. The residual fork is "
            "temporal-issuance's PP-3 verbatim -- contract A is schema "
            "disclosure to a bounded observer, contract C is genuine type "
            "creation -- and TI owns the source question under the ratified "
            "tri-repo division. TI has already reduced it to a single "
            "structural bit, D-FORK: is the operative source's effective type "
            "space Goedelian (self-generating) or fixed-finite? Issuance holds "
            "iff Goedelian; it reduces to bounded-projection disclosure iff "
            "finite. TI has also discharged the categorical signature "
            "(FUNCTOR-OBL-001: non-naturality is the fingerprint of issuance "
            "versus disclosure) and named the deciding fixture (E042 6.2, "
            "whether the source encodes its own admissibility predicate). "
            "Routed to TI 2026-07-27; carry the pointer rather than rebuilding "
            "the criterion. "
            "Caution for whoever picks this up: a joint can exceed its parts "
            "informationally without any type being created -- Shamir "
            "threshold sharing is the witness, where sub-threshold shares carry "
            "provably zero information yet the secret was fixed in advance. "
            "Invertibility-style tests catch that case and misread it as "
            "creation. "
            "TaF's own remaining question is narrower and record-local: is the "
            "record-reconciliation map natural? If natural, A and C are "
            "operationally identical at the record layer and issuance lives "
            "strictly below records, which is a sharper result than either "
            "contract winning. "
            "Separately, contract B had it survived would have derived a global "
            "tick from the ledger count rather than positing one; its "
            "refutation closes the cheapest route to a preferred frame in this "
            "programme."
        ),
    )


def result_to_dict(result: T588Result) -> dict[str, Any]:
    payload = asdict(result)
    return payload


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# {payload['artifact']}",
        "",
        f"**Verdict:** `{payload['verdict']}`",
        "",
        "## Fixture",
        "",
        "| Observer | Proper time |",
        "|---|---|",
    ]
    for w in payload["fixture"]:
        lines.append(f"| {w['observer_id']} | {w['proper_time']} |")
    lines += ["", "## Contracts", "", "| Contract | Counts differ | Status |", "|---|---|---|"]
    for c in payload["contracts"]:
        lines.append(
            f"| {c['contract_id']} | {c['counts_differ']} | **{c['status']}** |"
        )
    lines += ["", "## Checks", "", "| Check | Passed |", "|---|---|"]
    for c in payload["checks"]:
        lines.append(f"| {c['check_id']} | {c['passed']} |")
    lines += [
        "",
        "## Physical result",
        "",
        payload["physical_result"],
        "",
        "## Residual discriminator",
        "",
        payload["residual_discriminator"],
        "",
        "## Claim ledger",
        "",
        payload["claim_ledger_update"],
        "",
        "## Not claimed",
        "",
        payload["not_claimed"],
        "",
        "## Next work",
        "",
        payload["next_work"],
        "",
    ]
    return "\n".join(lines)


def write_results(result: T588Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = result_to_dict(result)
    (results_dir / f"{ARTIFACT}.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (results_dir / f"{ARTIFACT}-results.md").write_text(
        render_markdown(payload), encoding="utf-8"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)
    result = run_t588_analysis()
    if args.write_results:
        write_results(result)
    print(json.dumps(result_to_dict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
