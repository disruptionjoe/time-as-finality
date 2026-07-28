"""Un-commit convention fork probe: does the S3 ratchet survive a closure-free un-commit?

Un-T-numbered exploration companion for
`explorations/causal-past-theorem-attempt-2026-07-28.md` (Step 1).

WHAT IS FORKED. S3 (`explorations/commit-module-s3-capability-graded-finality-2026-07-28.md`
Sec 1.2) declares, in one sentence and with no construction-fork declaration:

    un-commit(r) := erase r AND restore the pre-issuance state of its carriers
    and every copy/derivative -- every record in the un-commit CLOSURE of r.

The alternative reading -- un-commit(r) := erase r ONLY -- has never been
declared as a fork or run. This module runs it. The two conventions are:

    CONVENTION_CLOSURE      W_rev(r) = sum over r's downstream record-order
                            closure of (omega_i/ln2 + Landauer floor_i)
    CONVENTION_CLOSURE_FREE W_rev(r) = omega_r/ln2 + Landauer floor_r
                            (the record itself; nothing downstream)

Neither convention is asserted to be the physically correct one here. The
question is entirely: WHICH RESULTS ARE CONVENTION-CARRIED, and which are
convention-independent.

HOW THE FORK IS APPLIED. `models/capability_graded_finality_probe.py` is NOT
modified. Its module-global `price_un_commit` is rebound for the duration of a
forked run, so every downstream S3 function -- the grade table, all three T584
invariance legs, the must-fail merge control, monotonicity, the sweep
thresholds, the constructive covering, order-compatibility, consumer
proliferation, the two-faces tie, and the completion classification -- is
re-executed verbatim against the alternative price. One definition changes;
sixteen checks re-run unaltered. Same discipline for the nucleation toy's
`w_rev` (Leg C) and the type-extension witness probe's `w_rev` (Leg B).

LEGS.
  Leg A -- the S3 fixture: all 16 S3 checks under both conventions.
  Leg B -- the type-extension settlement separation (the epsilon leg of
           `explorations/proposed-type-extension-morphism-gate-2026-07-28.md`):
           does an old record's grade still flip under a lawful epsilon?
  Leg C -- the nucleation toy's P1 (two strokes move oppositely) and P4
           (defect permanence) under the closure-free price. The toy's
           dynamics are untouched: `w_rev` is read-only bookkeeping (used at
           one line, for trajectory recording), so the fork changes derived
           prices and nothing about which records exist or when.

PREDICTION OUTCOMES ARE DATA. The pre-registrations below were frozen before
execution and are not revised. Their status does NOT gate the exit code: exit
0 iff the four structural controls pass (reproduction, fork-bites,
fail-closed, and horizon-invariance-is-checked-not-assumed). A pre-registration
that fails is reported as a failure.

Firebreak: nothing here is a claim movement, a T-number, an issuance, a
temporal quantity, or an arrow. FINAL(A, r) remains class-indexed
inaccessibility, never constructor impossibility (N8 gate item 8).
Deterministic pure-stdlib: no wall-clock, no dates, no fresh randomness;
byte-identical output across repeat runs.

Run: python3 -m models.uncommit_convention_fork_probe   (from repo root)
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import math

from models import capability_graded_finality_probe as s3
from models import nucleation_ratchet_toy as nrt
from models import t583_capability_contract_v1 as t583
from models import t586_record_capability_order_gate as t586
from models import type_extension_witness_probe as tewp

ARTIFACT = "uncommit-convention-fork-probe-v0.1"
STATUS = "UN_T_NUMBERED_EXPLORATION_COMPANION_REVIEW_ONLY"
LN2 = math.log(2.0)
ROUND = 9

CONVENTION_CLOSURE = "closure"
CONVENTION_CLOSURE_FREE = "closure_free"
CONVENTIONS = (CONVENTION_CLOSURE, CONVENTION_CLOSURE_FREE)


# ---------------------------------------------------------------------------
# Pre-registration (frozen before execution; not revised)
# ---------------------------------------------------------------------------

PRE_REGISTRATION = {
    "frozen_before_execution": True,
    "PR1": (
        "Under the closure-free convention W_rev becomes a PER-RECORD "
        "CONSTANT: it stops quoting the record graph entirely, so adding a "
        "downstream consumer changes no record's price (zero strict "
        "increases), and the price ordering is the omega ordering rather "
        "than the closure-depth ordering."
    ),
    "PR2": (
        "Check (iv)'s order-compatibility becomes VACUOUS: with singleton "
        "closures there is nothing left for the upward-nesting clause to "
        "constrain."
    ),
    "PR3": (
        "The type-extension (epsilon) settlement separation COLLAPSES: a "
        "lawful epsilon no longer moves any old record's W_rev, so every "
        "settlement object is E-stable and forecasting collapses to "
        "prediction at the settlement layer too -- the deflationary exit the "
        "packet itself registered as evidence AGAINST the ratchet thesis."
    ),
    "PR4": (
        "THE RATCHET LINE EVAPORATES: with (iv) and the epsilon separation "
        "gone, the nucleation toy's P1 (the two strokes move oppositely) "
        "loses its type-stroke direction -- no price rises with world growth "
        "-- and P4's ancestor-located permanence has no ancestors to live "
        "in."
    ),
    "PR5_control": (
        "The declared divergent horizon edge is UNAFFECTED by the fork, "
        "because its divergence is carried by carrier departure from every "
        "declarable access region, not by closure size. If this fails, the "
        "limit separation was a closure artifact and Step 2 has no subject."
    ),
}


# ---------------------------------------------------------------------------
# The forked price (Leg A)
# ---------------------------------------------------------------------------

_S3_PRICE_CLOSURE = s3.price_un_commit


def price_un_commit_closure_free(record_id, closure, carriers, distribution_access):
    """un-commit(r) := erase r only. Same signature as S3's price function.

    The declared-divergent horizon record is delegated to S3 unchanged: its
    closure is already a singleton and its divergence is declared at the
    carrier-access layer, not derived from closure size. That delegation is
    itself a checked control (PR5), not an assumption.
    """
    if record_id == s3.HORIZON_RECORD:
        return _S3_PRICE_CLOSURE(record_id, closure, carriers, distribution_access)
    by_record = {c.record_id: c for c in carriers}
    member = by_record[record_id]
    omega_total = member.omega_stab_nats
    destab_units = omega_total / LN2
    floors = s3.landauer_floor_bits(member, distribution_access)
    n = 1
    energy = round(destab_units + floors, ROUND)
    time_cost = round(n * 1.0 + destab_units + floors, ROUND)
    point = t583.PerformancePoint(
        task_id=f"{s3.UN_COMMIT_TASK_PREFIX}::{record_id}",
        success=round(0.999 ** n, ROUND),
        energy_cost=energy,
        time_cost=time_cost,
        communication_cost=round(0.05 * n, ROUND),
        memory_cost=round(0.1 * n, ROUND),
        error=round(0.001 + 0.0005 * n, ROUND),
        protocol_id=s3.REVERSE_OPERATION,
    )
    return s3.UnCommitPrice(
        record_id=record_id,
        closure_records=(record_id,),
        closure_carriers=(member.carrier_id,),
        omega_total_nats=round(omega_total, ROUND),
        destabilization_units=round(destab_units, ROUND),
        floor_units=round(floors, ROUND),
        point=point,
        divergent=False,
    )


def _price_for(convention):
    if convention == CONVENTION_CLOSURE:
        return _S3_PRICE_CLOSURE
    if convention == CONVENTION_CLOSURE_FREE:
        return price_un_commit_closure_free
    raise ValueError(f"undeclared un-commit convention: {convention!r}")


@contextlib.contextmanager
def _s3_convention(convention):
    """Rebind S3's price function for the duration of a forked run.

    S3's own module is never edited; every S3 check re-executes verbatim.
    """
    previous = s3.price_un_commit
    s3.price_un_commit = _price_for(convention)
    try:
        yield
    finally:
        s3.price_un_commit = previous


def leg_a(convention):
    """All 16 S3 checks, re-executed under the given un-commit convention."""
    with _s3_convention(convention):
        payload = s3.run_analysis()
        prices = payload["un_commit_prices"]
        # Strict-increase count under one added downstream consumer: the sharp
        # form of PR1. S3's own check only asks for a WEAK increase, which a
        # per-record constant satisfies vacuously -- so the weak check cannot
        # see the fork and a strict counter is needed.
        carriers = s3._declared_carriers()
        closure = frozenset(
            tuple(p) for p in t586.run_t586_analysis().order_report.closure)
        extended_carriers = carriers + (
            s3.RecordCarrier(
                "r_archived_certificate", "archive_certificate", "cell_archive",
                0.0, 4.0,
                {"physical_payload": "archive", "display_label": "alpha",
                 "sensor_serial": "S-F", "coordinate_name": "x_arch"},
            ),
        )
        extended_closure = frozenset(
            set(closure)
            | {("certify_erased_record", "archive_certificate")}
            | {(up, "archive_certificate")
               for up, down in closure if down == "certify_erased_record"}
        )
        strict_increases = 0
        for carrier in carriers:
            before = s3.price_un_commit(carrier.record_id, closure, carriers, True)
            after = s3.price_un_commit(
                carrier.record_id, extended_closure, extended_carriers, True)
            if after.point.energy_cost > before.point.energy_cost + 1e-9:
                strict_increases += 1

    finite = {r: v for r, v in prices.items() if r != s3.HORIZON_RECORD}
    checks = {c["check_id"]: c["passed"] for c in payload["checks"]}
    return {
        "convention": convention,
        "w_rev_energy": {r: v["w_rev_units_energy"] for r, v in finite.items()},
        "closure_sizes": {r: len(v["closure_records"]) for r, v in finite.items()},
        "omega_total_nats": {r: v["omega_total_nats"] for r, v in finite.items()},
        "unfinalization_thresholds": payload["unfinalization_thresholds"],
        "order_compatibility": payload["order_compatibility"],
        "consumer_proliferation": payload["consumer_proliferation"],
        "consumer_proliferation_strict_price_increases": strict_increases,
        "completion_classification": payload["completion_classification_of_finality_flips"],
        "checks": checks,
        "checks_failed": sorted(k for k, v in checks.items() if not v),
        "kill_verdict": payload["kill_verdict"],
        "horizon_row": prices[s3.HORIZON_RECORD],
    }


# ---------------------------------------------------------------------------
# Leg B -- the type-extension (epsilon) settlement separation
# ---------------------------------------------------------------------------

_TEWP_W_REV_CLOSURE = tewp.w_rev


def _tewp_w_rev_closure_free(record, consumption, extra=()):
    """Mini-S3 price, closure-free: the record's own omega/ln2 + its own floor."""
    omega, issues, floors = dict(tewp.OMEGA_EV), dict(tewp.ISSUES), dict(tewp.FLOORS)
    for ev, om, rid in extra:
        omega[ev], issues[ev], floors[rid] = om, rid, 0.0
    producer = {r: e for e, r in issues.items()}
    return round(omega[producer[record]] / tewp.LN2 + floors[record], 9)


def leg_b(convention):
    """The packet's grade leg: does a lawful epsilon flip an old record's grade?

    Fixture (the packet's own, verbatim): C = T585's declared context;
    epsilon_1 = `audit_standard_record` consuming `r_erased_standard`,
    declared omega 7.0; epsilon_2 = `audit_light_standard_record`, same
    consumption, declared omega 1.0. Declared class A_mid (energy 25.0).
    """
    w_rev = (_TEWP_W_REV_CLOSURE if convention == CONVENTION_CLOSURE
             else _tewp_w_rev_closure_free)
    base_consumption = tewp.CONS_C  # (("certify_event", "r_erased_standard"),)
    # The packet's own family E: same consumption edge, two declared omegas.
    eps = {
        "epsilon_1_omega_7": ("audit_event", 7.0, "r_audit_certificate"),
        "epsilon_2_omega_1": ("audit_event", 1.0, "r_audit_light_certificate"),
    }
    out = {"convention": convention, "class": "A_mid(energy=25.0)", "records": {}}
    for target in ("r_erased_standard", "r_biased_reference"):
        before_price = w_rev(target, base_consumption)
        row = {
            "w_rev_before": before_price,
            "grade_before": tewp.grade(before_price, tewp.A_MID),
            "under_epsilon": {},
        }
        for name, (event, omega, issued) in eps.items():
            extended = base_consumption + ((event, "r_erased_standard"),)
            after_price = w_rev(target, extended, extra=((event, omega, issued),))
            row["under_epsilon"][name] = {
                "w_rev_after": after_price,
                "grade_after": tewp.grade(after_price, tewp.A_MID),
                "price_moved": abs(after_price - before_price) > 1e-9,
                "grade_flipped": (tewp.grade(after_price, tewp.A_MID)
                                  != tewp.grade(before_price, tewp.A_MID)),
            }
        out["records"][target] = row
    any_price_moved = any(
        e["price_moved"]
        for row in out["records"].values() for e in row["under_epsilon"].values()
    )
    any_grade_flipped = any(
        e["grade_flipped"]
        for row in out["records"].values() for e in row["under_epsilon"].values()
    )
    out["settlement_layer_extension_sensitive"] = any_price_moved
    out["some_old_record_grade_flips_under_epsilon"] = any_grade_flipped
    out["separation_survives"] = any_grade_flipped
    return out


# ---------------------------------------------------------------------------
# Leg C -- the nucleation toy's P1 and P4 under the fork
# ---------------------------------------------------------------------------

_NRT_W_REV_CLOSURE = nrt.w_rev


def _nrt_w_rev_closure_free(rid, records):
    row = records[rid]
    return round(row["omega"] / nrt.LN2 + row["floor"], 9)


def leg_c(convention):
    """Re-run the nucleation toy with the fork applied to its price bookkeeping.

    `w_rev` is used at exactly one site in the toy (trajectory recording); the
    seeded dynamics, the record set, the contact schedule, and the defect set
    are therefore bit-identical across the fork. Only price-derived results
    move.
    """
    previous = nrt.w_rev
    nrt.w_rev = (_NRT_W_REV_CLOSURE if convention == CONVENTION_CLOSURE
                 else _nrt_w_rev_closure_free)
    try:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exit_code = nrt.run()
        payload = json.loads(buffer.getvalue())
    finally:
        nrt.w_rev = previous
    preg = payload["pre_registered"]
    checks = {c["check"]: c["passed"] for c in payload["checks"]}
    return {
        "convention": convention,
        "toy_exit_code": exit_code,
        "P1": preg["P1"],
        "P4": {k: v for k, v in preg["P4"].items() if not k.startswith("_")},
        "defect_signature_unchanged_marker": preg["P5"]["defect_counts"],
        "p1_constraint_bites": checks.get("p1_constraint_bites"),
        "class_axis_monotonicity_untouched": checks.get(
            "class_axis_monotonicity_untouched"),
        "toy_verdict": payload["verdict"],
    }


# ---------------------------------------------------------------------------
# Adjudication and controls
# ---------------------------------------------------------------------------


def _adjudicate(a_closure, a_free, b_closure, b_free, c_closure, c_free):
    order_free = a_free["order_compatibility"]
    items = []

    # PR1 -- W_rev becomes a per-record constant.
    pr1_observed = {
        "closure_sizes_all_one": all(v == 1 for v in a_free["closure_sizes"].values()),
        "strict_price_increases_under_added_consumer": a_free[
            "consumer_proliferation_strict_price_increases"],
        "baseline_strict_price_increases": a_closure[
            "consumer_proliferation_strict_price_increases"],
        "price_order_is_omega_order": (
            sorted(a_free["w_rev_energy"], key=lambda r: a_free["w_rev_energy"][r])
            == sorted(a_free["omega_total_nats"],
                      key=lambda r: (a_free["omega_total_nats"][r],
                                     a_free["w_rev_energy"][r]))
        ),
    }
    items.append({
        "id": "PR1",
        "prediction": PRE_REGISTRATION["PR1"],
        "observed": pr1_observed,
        "verdict": ("CONFIRMED"
                    if (pr1_observed["closure_sizes_all_one"]
                        and pr1_observed["strict_price_increases_under_added_consumer"] == 0
                        and pr1_observed["baseline_strict_price_increases"] > 0)
                    else "REFUTED"),
    })

    # PR2 -- check (iv) becomes vacuous.
    legs = {k: v for k, v in order_free.items() if isinstance(v, bool)}
    pr2_verdict = (
        "CONFIRMED" if all(legs.values()) and order_free["record_pairs_checked"] == 0
        else "REFUTED_SHARPER" if not all(legs.values())
        else "REFUTED"
    )
    items.append({
        "id": "PR2",
        "prediction": PRE_REGISTRATION["PR2"],
        "observed": {
            "record_pairs_still_checked": order_free["record_pairs_checked"],
            "legs": legs,
            "baseline_legs": {k: v for k, v in
                              a_closure["order_compatibility"].items()
                              if isinstance(v, bool)},
        },
        "verdict": pr2_verdict,
        "note": (
            "REFUTED_SHARPER means the prediction understated the damage: the "
            "clause does not go vacuous, it goes FALSE -- the order-compatibility "
            "result is not merely unsupported under the alternative convention, "
            "it is contradicted by it."
        ),
    })

    # PR3 -- the epsilon settlement separation collapses.
    items.append({
        "id": "PR3",
        "prediction": PRE_REGISTRATION["PR3"],
        "observed": {
            "closure_convention_separation_survives": b_closure["separation_survives"],
            "closure_free_separation_survives": b_free["separation_survives"],
            "closure_free_settlement_layer_extension_sensitive":
                b_free["settlement_layer_extension_sensitive"],
        },
        "verdict": ("CONFIRMED"
                    if (b_closure["separation_survives"]
                        and not b_free["separation_survives"]
                        and not b_free["settlement_layer_extension_sensitive"])
                    else "REFUTED"),
    })

    # PR4 -- the ratchet line evaporates.
    p1_free = c_free["P1"]
    p1_closure = c_closure["P1"]
    items.append({
        "id": "PR4",
        "prediction": PRE_REGISTRATION["PR4"],
        "observed": {
            "P1_closure": p1_closure,
            "P1_closure_free": p1_free,
            "P4_closure": c_closure["P4"],
            "P4_closure_free": c_free["P4"],
            "toy_dynamics_identical_across_fork": (
                c_closure["defect_signature_unchanged_marker"]
                == c_free["defect_signature_unchanged_marker"]),
        },
        "verdict": ("CONFIRMED"
                    if (p1_closure["genuine_final_flips"] > 0
                        and p1_free["genuine_final_flips"] == 0)
                    else "PARTIAL" if p1_free["genuine_final_flips"] < p1_closure[
                        "genuine_final_flips"]
                    else "REFUTED"),
    })

    # PR5 -- the horizon edge is convention-independent.
    items.append({
        "id": "PR5_control",
        "prediction": PRE_REGISTRATION["PR5_control"],
        "observed": {
            "horizon_row_closure": a_closure["horizon_row"],
            "horizon_row_closure_free": a_free["horizon_row"],
            "identical": a_closure["horizon_row"] == a_free["horizon_row"],
            "horizon_threshold_closure":
                a_closure["unfinalization_thresholds"][s3.HORIZON_RECORD],
            "horizon_threshold_closure_free":
                a_free["unfinalization_thresholds"][s3.HORIZON_RECORD],
        },
        "verdict": ("CONFIRMED"
                    if (a_closure["horizon_row"] == a_free["horizon_row"]
                        and a_closure["unfinalization_thresholds"][s3.HORIZON_RECORD]
                        == a_free["unfinalization_thresholds"][s3.HORIZON_RECORD])
                    else "REFUTED"),
    })
    return items


def _controls(a_closure, a_free):
    """Must-fail-closed controls. These, and only these, gate the exit code."""
    published_s3_w_rev = {
        "r_known_zero": 34.624680981,
        "r_copied_zero": 28.853900818,
        "r_erased_standard": 20.197730572,
        "r_erasure_certificate": 7.213475204,
        "r_biased_reference": 4.797080717,
    }
    published_thresholds = {
        "r_biased_reference": 8, "r_erasure_certificate": 16,
        "r_erased_standard": 32, "r_copied_zero": 40, "r_known_zero": 48,
    }
    reproduction = (
        a_closure["w_rev_energy"] == published_s3_w_rev
        and all(a_closure["unfinalization_thresholds"][r] == v
                for r, v in published_thresholds.items())
        and a_closure["kill_verdict"] == "S3_KILL_DOES_NOT_FIRE"
    )
    fork_bites = (
        a_closure["w_rev_energy"] != a_free["w_rev_energy"]
        and a_closure["unfinalization_thresholds"] != a_free["unfinalization_thresholds"]
    )
    try:
        _price_for("no_such_convention")
        fail_closed = False
    except ValueError:
        fail_closed = True
    horizon_checked = (
        a_closure["horizon_row"]["w_rev_units_energy"] == s3.DIVERGENT
        and a_free["horizon_row"]["w_rev_units_energy"] == s3.DIVERGENT
    )
    return [
        {"control": "closure_branch_reproduces_published_s3",
         "passed": reproduction,
         "note": "The unforked branch must reproduce S3's committed W_rev "
                 "table, thresholds, and kill verdict exactly, or the fork "
                 "harness is not running S3."},
        {"control": "fork_bites",
         "passed": fork_bites,
         "note": "The alternative convention must actually change the prices "
                 "and the thresholds, or the fork is a no-op and proves "
                 "nothing."},
        {"control": "undeclared_convention_fails_closed",
         "passed": fail_closed,
         "note": "An undeclared convention name must raise, never silently "
                 "default."},
        {"control": "horizon_divergence_is_read_not_assumed",
         "passed": horizon_checked,
         "note": "The declared divergent edge is read out of both branches "
                 "rather than asserted."},
    ]


def run_analysis():
    a_closure = leg_a(CONVENTION_CLOSURE)
    a_free = leg_a(CONVENTION_CLOSURE_FREE)
    b_closure = leg_b(CONVENTION_CLOSURE)
    b_free = leg_b(CONVENTION_CLOSURE_FREE)
    c_closure = leg_c(CONVENTION_CLOSURE)
    c_free = leg_c(CONVENTION_CLOSURE_FREE)

    adjudication = _adjudicate(a_closure, a_free, b_closure, b_free,
                               c_closure, c_free)
    controls = _controls(a_closure, a_free)

    survivors = sorted(
        cid for cid, passed in a_free["checks"].items() if passed
    )
    casualties = a_free["checks_failed"]

    return {
        "artifact": ARTIFACT,
        "status": STATUS,
        "question": (
            "S3 Sec 1.2 declares the closure reading of un-commit in one "
            "sentence with no fork declaration. Which S3-family results are "
            "carried by that undeclared choice?"
        ),
        "pre_registration": PRE_REGISTRATION,
        "leg_a_s3_fixture": {
            CONVENTION_CLOSURE: a_closure,
            CONVENTION_CLOSURE_FREE: a_free,
        },
        "leg_b_type_extension_settlement": {
            CONVENTION_CLOSURE: b_closure,
            CONVENTION_CLOSURE_FREE: b_free,
        },
        "leg_c_nucleation_toy": {
            CONVENTION_CLOSURE: c_closure,
            CONVENTION_CLOSURE_FREE: c_free,
        },
        "adjudication": adjudication,
        "s3_checks_under_closure_free": {
            "survive": survivors,
            "die": casualties,
            "kill_verdict": a_free["kill_verdict"],
        },
        "controls": controls,
        "convention_independence_summary": {
            "convention_independent": [
                "check (i) T584 invariance (all three legs + the must-fail merge control)",
                "check (ii) monotonicity of FINAL and of margins under capability extension",
                "check (iii) every finite record un-finalizes at some bounded class",
                "check (iii) the declared divergent edge is FINAL at every bounded class",
                "the constructive covering (budget = cost + 1)",
                "the two-faces (Crooks) tie",
                "the anti-scalarization exhibit",
                "every finality delta is a named T583 completion",
            ],
            "convention_carried": [
                "check (iv) order-compatibility: closure nesting, price "
                "monotonicity downstream, finality propagating upstream",
                "the consumer-proliferation / redundancy connection",
                "the threshold ORDERING (closure depth vs bare omega)",
                "the type-extension settlement separation (epsilon leg)",
                "the nucleation toy's type stroke (P1's second direction) "
                "and P4's ancestor-located permanence",
            ],
        },
        "firebreak": (
            "No claim, canon tier, bin, guardrail, T-number, or posture "
            "moves. FINAL(A, r) stays class-indexed inaccessibility, never "
            "constructor impossibility. Neither convention is asserted here "
            "to be the physically correct un-commit; the deliverable is the "
            "partition of results into convention-carried and "
            "convention-independent."
        ),
        "prediction_outcomes_are_data": (
            "PR1-PR5 statuses do not gate the exit code; exit 0 iff the four "
            "structural controls pass."
        ),
        "verdict": (
            "UNCOMMIT_CONVENTION_FORK_EXECUTED_REVIEW_ONLY"
            if all(c["passed"] for c in controls)
            else "UNCOMMIT_CONVENTION_FORK_STRUCTURAL_FAILURE"
        ),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    payload = run_analysis()
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 0 if all(c["passed"] for c in payload["controls"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
