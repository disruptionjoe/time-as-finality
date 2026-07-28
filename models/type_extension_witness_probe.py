"""Type-extension witness probe (exploration-attached; no T-number).

Executes the epsilon-witness, commutation legs, grade leg, and must-fail
controls of explorations/proposed-type-extension-morphism-gate-2026-07-28.md
via that packet's own fallback path (the composition-extensivity discipline).

epsilon: C -> C+ adds declared task types and only adds: no deletion, no
mutation of existing tasks, no budget growth; a new task consumes existing
records per declared unique-producer consumption edges and is charged against
the SAME declared budget. Admissibility = conservativity of the old envelope
(anti-revisionism) + commutation with T584's classes and the composition
clause's namespaced oplus. Grade leg: mini-S3 un-commit pricing (declared
omega ledger rows reused verbatim) showing an OLD record's finality grade
lawfully changes under extension while the old envelope cannot -- the
prediction/forecasting SPLIT BY LAYER. Closure depth-1 by declared fixture.

Deterministic; stdlib + in-repo models only; no randomness, no wall-clock in
output. Firebreak (T587 boundary typing): no capability delta, grade flip, or
new order edge is time, temporal issuance, or an arrow claim by itself.
"""
from __future__ import annotations

import json
import math
from dataclasses import asdict, replace

from models import t583_capability_contract_v1 as t583
from models import t585_landauer_physical_capability_gate as t585

LN2 = math.log(2.0)
OMEGA_EV = {"erase_event": 9.0, "certify_event": 5.0, "prepare_event": 3.0}
ISSUES = {"erase_event": "r_erased_standard", "certify_event": "r_erasure_certificate",
          "prepare_event": "r_biased_reference"}
FLOORS = {"r_erased_standard": 0.0, "r_erasure_certificate": 0.0,
          "r_biased_reference": 0.468995594}
CONS_C = (("certify_event", "r_erased_standard"),)  # event consumes record
A_MID = t583.Budget(25.0, 300.0, 10.0, 10.0, 0.01)
A_BIG = t583.Budget(64.0, 300.0, 10.0, 10.0, 0.01)


def biased_state(swapped=False):
    if swapped:
        return t585.MemoryState("biased_swapped", 0.90, True, "bit_label_swapped", "b-s", "S-2")
    return t585.MemoryState("biased_record", 0.10, True, "canonical", "biased", "S-1")


def points_for(ctx, state=None, representation="normalized"):
    return t585._points_for_state(context=ctx, state=state or biased_state(),
                                  observer_mode="state_aware", representation=representation)


def audit_point(task, energy=0.10):
    return t583.PerformancePoint(task, 0.99, energy, 0.5, 0.2, 0.1, 0.003, "audit_readout")


def extension(task_id="audit_standard_record", consumes="r_erased_standard",
              issues="r_audit_certificate", omega=7.0, point=None):
    return {"task_id": task_id, "consumes": consumes, "issues": issues, "omega": omega,
            "point": point or audit_point(task_id), "operation": "audit_readout"}


def build_plus(ctx, ext):
    return replace(ctx, context_id=ctx.context_id + "+" + ext["task_id"],
                   task_family=ctx.task_family + (ext["task_id"],),
                   operation_menu=ctx.operation_menu + (ext["operation"],))


def envelope(ctx, pts, sid="biased_record"):
    return t583.attainable_envelope(context=ctx, state_id=sid, candidates=pts)


def restrict(points, family):
    return tuple(p for p in points if p.task_id in family)


def admissible(ctx, plus, old_pts, plus_pts, ext=None):
    """The extension admissibility law; every rejection is typed, fail-closed."""
    if ext is not None:
        if ext["task_id"] in ctx.task_family:
            return False, "TASK_ID_COLLISION_NOT_EXTENSION"
        if ext["consumes"] not in ISSUES.values():
            return False, "UNKNOWN_RECORD_CONSUMED"
        if ext["issues"] in ISSUES.values():
            return False, "REISSUE_EXISTING_RECORD"
    if sorted(set(ctx.task_family) - set(plus.task_family)):
        return False, "VOCABULARY_MERGE_OR_DELETION_NOT_EXTENSION"
    if not (set(plus.task_family) - set(ctx.task_family)):
        return False, "NO_NEW_TASK_TYPE"
    if plus.budget != ctx.budget:
        return False, "SILENT_BUDGET_GROWTH"
    if restrict(envelope(plus, plus_pts).points, ctx.task_family) != envelope(ctx, old_pts).points:
        return False, "EXISTING_TASK_MUTATION"
    return True, "ADMISSIBLE"


def rec_order(consumption, issues):
    producer = {r: e for e, r in issues.items()}
    return tuple(sorted((producer[r], e) for e, r in consumption))


def w_rev(record, consumption, extra=()):
    """Mini-S3 un-commit price: sum over depth-1 closure of omega/ln2 + floor."""
    omega, issues, floors = dict(OMEGA_EV), dict(ISSUES), dict(FLOORS)
    for ev, om, rid in extra:
        omega[ev], issues[ev], floors[rid] = om, rid, 0.0
    producer = {r: e for e, r in issues.items()}
    downstream = sorted(issues[e] for e, r in consumption if producer[r] == producer[record])
    return round(sum(omega[producer[r]] / LN2 + floors[r] for r in [record] + downstream), 9)


def grade(price, budget):
    pt = t583.PerformancePoint("un_commit", 0.99, price, 1.0 + price, 0.1, 0.1, 0.002,
                               "crooks_reverse_protocol")
    return "IN_ENVELOPE" if t583.point_is_feasible(pt.canonical(), budget) else "FINAL_OUT_OF_ENVELOPE_BUDGET"


def iota(points, ns):
    return tuple(replace(p, task_id=f"{ns}::{p.task_id}") for p in points)


def sortp(points):
    return tuple(sorted(points, key=lambda p: (p.task_id, -p.success, p.energy_cost,
                 p.time_cost, p.communication_cost, p.memory_cost, p.error)))


def run():
    checks, controls = [], []
    check = lambda cid, ok, note="": checks.append({"check": cid, "passed": bool(ok), "note": note})
    control = lambda cid, expected, got: controls.append(
        {"control": cid, "expected": expected, "got": got, "failed_closed": expected == got})

    check("t585_source_available", t585.run_t585_analysis().verdict == t585.VERDICT,
          "T585 re-executed as source-owned physical input, not consumed from cache")
    ctx, state = t585._base_context(), biased_state()
    old_pts = points_for(ctx)
    eps1, eps2 = extension(), extension(task_id="audit_light_standard_record", omega=1.0,
                                        issues="r_audit_light_certificate",
                                        point=audit_point("audit_light_standard_record", 0.08))
    plus1, plus2 = build_plus(ctx, eps1), build_plus(ctx, eps2)
    pts1, pts2 = old_pts + (eps1["point"],), old_pts + (eps2["point"],)
    env_c, env_p1, env_p2 = envelope(ctx, old_pts), envelope(plus1, pts1), envelope(plus2, pts2)

    check("epsilon_admissible_both_members_of_E",
          admissible(ctx, plus1, old_pts, pts1, eps1) == (True, "ADMISSIBLE")
          and admissible(ctx, plus2, old_pts, pts2, eps2) == (True, "ADMISSIBLE"))
    check("conservativity_anti_revisionism",
          restrict(env_p1.points, ctx.task_family) == env_c.points
          and restrict(env_p2.points, ctx.task_family) == env_c.points,
          "Env(C+) restricted to old tasks equals Env(C) bitwise, both extensions")
    check("extension_strictly_grows_envelope",
          len(env_p1.points) == len(env_c.points) + 1
          and any(p.task_id == eps1["task_id"] for p in env_p1.points))
    raw = t583.assess_pair(pair_id="c_vs_cplus_raw", left_context=ctx, right_context=plus1,
                           left_envelope=env_c, right_envelope=env_p1,
                           evidence=t583.PairEvidence(source_law_present=True))
    check("current_contract_absorbs_extension_as_completion",
          raw.verdict == "TASK_REDEFINITION_COMPLETION" and raw.capability_relation == "SUBSET",
          "the sharpness: T583-T588 cannot distinguish lawful extension from arbitrary task change")

    check("commutes_with_gauge_swap",
          envelope(plus1, points_for(ctx, biased_state(True)) + (eps1["point"],)).points == env_p1.points)
    check("commutes_with_representation_joule",
          envelope(plus1, points_for(ctx, representation="joule") + (eps1["point"],)).points == env_p1.points)
    coarse = replace(biased_state(), display_label="coarse", sensor_serial="S-Z")
    check("commutes_with_coarse_graining",
          t585.projected_metadata(coarse, plus1) == t585.projected_metadata(biased_state(), plus1))
    lhs = sortp(iota(env_p1.points, "ns1") + iota(env_c.points, "ns2"))
    new_canon = tuple(p for p in env_p1.points if p.task_id == eps1["task_id"])
    rhs = sortp(iota(env_c.points, "ns1") + iota(env_c.points, "ns2") + iota(new_canon, "ns1"))
    check("commutes_with_oplus_composition",
          lhs == rhs and restrict(lhs, {f"ns2::{t}" for t in ctx.task_family}) == iota(env_c.points, "ns2"),
          "extend-then-oplus equals oplus-then-extend; other namespace untouched (conservativity on composites)")

    cons_p1 = CONS_C + (("audit_event", eps1["consumes"]),)
    extra1 = (("audit_event", eps1["omega"], eps1["issues"]),)
    order_c, order_p1 = rec_order(CONS_C, ISSUES), rec_order(cons_p1, dict(ISSUES, audit_event=eps1["issues"]))
    old_ev = set(OMEGA_EV)
    check("record_order_conservative_and_strictly_grows",
          tuple(p for p in order_p1 if set(p) <= old_ev) == order_c and set(order_c) < set(order_p1))

    w_std_c, w_ref_c = w_rev("r_erased_standard", CONS_C), w_rev("r_biased_reference", CONS_C)
    w_std_1 = w_rev("r_erased_standard", cons_p1, extra1)
    w_std_2 = w_rev("r_erased_standard", CONS_C + (("audit_event", eps2["consumes"]),),
                    (("audit_event", eps2["omega"], eps2["issues"]),))
    w_ref_1 = w_rev("r_biased_reference", cons_p1, extra1)
    grades = {"w_std_C": w_std_c, "w_std_eps1": w_std_1, "w_std_eps2": w_std_2,
              "w_ref_C": w_ref_c, "w_ref_eps1": w_ref_1}
    check("grade_flip_under_admissible_extension",
          grade(w_std_c, A_MID) == "IN_ENVELOPE" and grade(w_std_1, A_MID) == "FINAL_OUT_OF_ENVELOPE_BUDGET",
          "old record r_erased_standard flips reversible->final under eps1 with the old envelope untouched")
    check("grade_sensitivity_is_epsilon_dependent", grade(w_std_2, A_MID) == "IN_ENVELOPE",
          "eps2 (omega 1.0) does not flip it: sensitivity is not automatic")
    check("grade_stable_record_across_E",
          w_ref_c == w_ref_1 and grade(w_ref_c, A_MID) == "IN_ENVELOPE",
          "r_biased_reference: closure untouched by E, grade E-stable")
    check("class_axis_monotonicity_untouched",
          all(not (grade(w, A_BIG) != "IN_ENVELOPE" and grade(w, A_MID) == "IN_ENVELOPE")
              for w in grades.values()),
          "S3 check (ii) direction on the agent-class axis is never violated; the flip lives on the other axis")
    check("forecasting_prediction_split_by_layer",
          restrict(env_p1.points, ctx.task_family) == env_c.points
          and grade(w_std_c, A_MID) == grade(w_ref_c, A_MID)
          and {r for r in ("r_erased_standard",) if grade(w_std_1, A_MID) != grade(w_std_c, A_MID)}
          == {"r_erased_standard"},
          "attainability layer coincides by law; settlement layer separates: stable {r_biased_reference}, "
          "sensitive {r_erased_standard}; prediction at fixed C grades both records identically")

    mut_pts = tuple(replace(p, energy_cost=0.01) if p.task_id == "certify_record_stability" else p
                    for p in old_pts) + (eps1["point"],)
    control("mutation_disguised_as_extension", "EXISTING_TASK_MUTATION",
            admissible(ctx, plus1, old_pts, mut_pts, eps1)[1])
    heavy = extension(task_id="audit_heavy", point=audit_point("audit_heavy", 1.2))
    grown = replace(build_plus(ctx, heavy), budget=replace(ctx.budget, energy=1.5))
    control("budget_growing_extension", "SILENT_BUDGET_GROWTH",
            admissible(ctx, grown, old_pts, old_pts + (heavy["point"],), heavy)[1])
    maxent = t585.MemoryState("max_entropy_record", 0.50, True, "canonical", "max_entropy", "S-9")
    me_pts = points_for(ctx, maxent)
    grown_same = replace(ctx, context_id="ctx_grown", budget=replace(ctx.budget, energy=1.5))
    control("pure_budget_growth_reclassified", "RESOURCE_BUDGET_COMPLETION",
            t583.assess_pair(pair_id="pure_budget_growth", left_context=ctx, right_context=grown_same,
                             left_envelope=envelope(ctx, me_pts, "max_entropy_record"),
                             right_envelope=envelope(grown_same, me_pts, "max_entropy_record"),
                             evidence=t583.PairEvidence(source_law_present=True)).verdict)
    merged = replace(ctx, context_id="ctx_merged",
                     task_family=tuple(t for t in ctx.task_family if t != "certify_record_stability"))
    merged_pts = tuple(p.canonical({"certify_record_stability": "erase_to_standard_record"}) for p in old_pts)
    control("vocabulary_merge_replay_t584_descendant", "VOCABULARY_MERGE_OR_DELETION_NOT_EXTENSION",
            admissible(ctx, merged, old_pts, merged_pts)[1])
    check("merge_changes_native_envelope_t584_mechanism",
          envelope(merged, merged_pts).points != env_c.points,
          "the merged vocabulary changes the native envelope, exactly T584's rejected counterexample")
    ghost = extension(task_id="audit_ghost", consumes="r_nonexistent")
    control("unknown_record_consumed", "UNKNOWN_RECORD_CONSUMED",
            admissible(ctx, build_plus(ctx, ghost), old_pts, old_pts + (ghost["point"],), ghost)[1])
    reissue = extension(task_id="audit_reissue", issues="r_erased_standard")
    control("reissue_existing_record", "REISSUE_EXISTING_RECORD",
            admissible(ctx, build_plus(ctx, reissue), old_pts, old_pts + (reissue["point"],), reissue)[1])
    collide = extension(task_id="certify_record_stability", point=audit_point("certify_record_stability"))
    control("task_id_collision_merge_face", "TASK_ID_COLLISION_NOT_EXTENSION",
            admissible(ctx, build_plus(ctx, collide), old_pts, old_pts + (collide["point"],), collide)[1])

    core_ok, teeth_ok = all(c["passed"] for c in checks), all(c["failed_closed"] for c in controls)
    exit_taken = ("EXIT_A_EXTENSION_CLASS_DEFINABLE_SPLIT_BY_LAYER" if core_ok and teeth_ok
                  else "EXIT_B_EXTENSION_CLASS_FAILS_OR_NO_TEETH")
    payload = {
        "artifact": "type-extension-witness-probe-exploration-companion-v0.1",
        "status": "UN_T_NUMBERED_EXPLORATION_COMPANION_REVIEW_ONLY",
        "spec": "explorations/proposed-type-extension-morphism-gate-2026-07-28.md",
        "epsilon_witness": {"tau": eps1["task_id"], "consumes": eps1["consumes"],
                            "issues": eps1["issues"], "declared_omega": eps1["omega"],
                            "env_C_points": [asdict(p) for p in env_c.points],
                            "env_Cplus_points": [asdict(p) for p in env_p1.points]},
        "raw_pair_assessment": {"relation": raw.capability_relation, "verdict": raw.verdict},
        "record_order": {"C": order_c, "C_plus_eps1": order_p1},
        "grade_leg": {"prices_kBTln2": grades, "class_A_mid_energy": A_MID.energy,
                      "flip": "r_erased_standard IN_ENVELOPE -> FINAL under eps1",
                      "stable": "r_biased_reference IN_ENVELOPE across E"},
        "checks": checks, "controls": controls,
        "exit_taken": exit_taken,
        "verdict": ("TYPE_EXTENSION_WITNESS_EXECUTED_" + exit_taken + "_REVIEW_ONLY"
                    if core_ok and teeth_ok else "TYPE_EXTENSION_WITNESS_CHECK_FAILED_" + exit_taken),
        "firebreak": ("No capability delta, grade flip, or new record-order edge is counted as time, "
                      "temporal issuance, or an arrow by itself; the record layer supplies typed "
                      "executable-task prerequisites only. No T-number is minted; owner decides adoption."),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if core_ok and teeth_ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
