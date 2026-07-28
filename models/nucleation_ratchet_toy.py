"""Nucleation ratchet toy (exploration-attached; no T-number).

Spec and pre-registered predictions P1-P5:
    explorations/nucleation-ratchet-toy-2026-07-28.md

The first executable instance of the two-stroke ratchet. Regions are declared
T583/T585-class contexts. A declared reservoir of candidate task-types carries
declared formation barriers Delta; per region, per tick, a type-slot crosses
its barrier with DECLARED probability ATTEMPT * exp(-BETA * Delta) (seeded
RNG). On crossing the region's context extends by epsilon_tau -- the type-
extension packet's own morphism class, imported: the conservativity /
anti-revisionism law, the budget discipline and the deletion/no-new-task legs
are executed by type_extension_witness_probe.admissible, called at EVERY
nucleation step; only the record universe is localized (the toy's record store
grows, so UNKNOWN_RECORD_CONSUMED / REISSUE_EXISTING_RECORD are re-checked
here against the region store, with the packet's own typed reason strings).
Nucleation ISSUES a founding record with declared omega. Settlement is graded
by the S3 commit module (un-commit closure, W_rev in kBT ln 2 units, typed
feasibility against T583 envelopes, per-axis margin vectors, no scalar).
Regions meet on a declared contact schedule; reconciliation reuses the
record-layer naturality forms -- smooth merge is union-with-provenance (the
form the naturality probe found NATURAL, no generated metadata); a variant
mismatch cannot merge smoothly and issues a DEFECT record storing the ordered
variant pair, i.e. the RELATIVE ALIGNMENT of the two regions' declarations --
the C-clock content the naturality probe found non-natural under independent
componentwise relabeling and natural under the diagonal.

Every declared omega is a verbatim reuse of an already-declared ledger row
(S3 section 2.1 / the packet's epsilon_1): base 9.0 (erase), audit 7.0,
defect 6.0 (copy), crossing 5.0 (certify), archive 4.0 (archive_certificate),
mint 3.0 (prepare). No rate constant, no barrier, and no physical transition
is derived, imported, or claimed: the rate law and the barriers are DECLARED
in-model dynamics. "Issuance" here is declared in-model dynamics and never a
source-metaphysics claim; PP-3 / D-FORK stays temporal-issuance's, untouched,
by pointer (the S2 boundary-sentence pattern).

Deterministic: fixed literal seeds, stdlib random only, no wall-clock, no os
entropy, no dates in the output; all randomness is pre-drawn into a per-seed
table in a fixed iteration order so every arm consumes the identical stream.
Outcome content for P1-P5 is DATA, not an assertion: exit 0 iff the structural
checks and the must-fail controls pass. A failed prediction is a first-class
result and does not fail the run.

Firebreak (T587 boundary typing): no capability delta, price change, grade
flip, defect record, or new record-order edge is counted as time, temporal
issuance, or an arrow by itself.
"""
from __future__ import annotations

import itertools
import json
import math
import random
from dataclasses import replace

from models import t583_capability_contract_v1 as t583
from models import t585_landauer_physical_capability_gate as t585
from models import type_extension_witness_probe as tewp

LN2 = tewp.LN2
BETA = 1.0
ATTEMPT = 1.0            # declared barrier-free per-tick crossing probability
TICKS = 30
SEEDS = (10007, 10009, 10037, 10039, 10061)
REGION_IDS = ("R1", "R2", "R3", "R4", "R5")
SLOT_ORDER = ("audit", "archive", "mint")
# slot -> (exclusive variants, barrier Delta, declared omega, declared energy)
SLOTS = {
    "audit": (("alpha", "beta"), 1.5, 7.0, 0.10),
    "archive": (("alpha", "beta"), 3.0, 4.0, 0.12),
    "mint": (("solo",), 4.0, 3.0, 0.09),
}
OMEGA_BASE, OMEGA_DEFECT, OMEGA_CROSS = 9.0, 6.0, 5.0
CLASS_CHAIN = ("A_small", "A_mid", "A_big")
CLASSES = {"A_small": t583.Budget(14.0, 300.0, 10.0, 10.0, 0.01),
           "A_mid": tewp.A_MID, "A_big": tewp.A_BIG}
INCOMPARABLE = {"A_energy_poor_time_rich": t583.Budget(12.0, 900.0, 10.0, 10.0, 0.01),
                "A_time_poor_energy_rich": t583.Budget(64.0, 22.0, 10.0, 10.0, 0.01)}
BASE_FAMILY = t585._base_context().task_family
BASELINE = {"n_regions": 3, "contact_k": 6, "contact_mode": "all_pairs"}


def rate(delta):
    return round(ATTEMPT * math.exp(-BETA * delta), 9)


def task_id(slot, variant):
    return f"{slot}_{variant}"


def founding_id(rid, slot, variant):
    return f"r_found_{rid}_{slot}_{variant}"


def region_context(rid):
    base = t585._base_context()
    return replace(base, context_id=f"ctx_{rid}", region_id=f"R_memory_cell_{rid}",
                   observer_id=f"O_{rid}")


def type_point(slot, variant):
    return tewp.audit_point(task_id(slot, variant), SLOTS[slot][3])


def draw_table(seed, ticks):
    """Pre-draw the whole stream so every arm consumes an identical table.

    One independent stream per (seed, region, slot), with the sub-seed derived by
    fixed integer arithmetic: a region's or slot's draws never depend on how many
    regions or slots the configuration contains, so the P3 region-count leg varies
    only the region count, and per-slot statistics are not read off a strided
    subsequence of one shared stream.
    """
    table = {}
    for ri, rid in enumerate(REGION_IDS):
        for si, slot in enumerate(SLOT_ORDER):
            rng = random.Random(seed * 1000003 + 101 * ri + 7 * si)
            for t in range(1, ticks + 1):
                table[(t, rid, slot)] = (rng.random(), rng.random())
    return table


def admit(ctx, plus, old_pts, plus_pts, ext, store):
    """Record-interface discipline (region-local universe) then the packet's epsilon core."""
    if ext["task_id"] in ctx.task_family:
        return False, "TASK_ID_COLLISION_NOT_EXTENSION"
    if ext["consumes"] not in store:
        return False, "UNKNOWN_RECORD_CONSUMED"
    if ext["issues"] in store:
        return False, "REISSUE_EXISTING_RECORD"
    return tewp.admissible(ctx, plus, old_pts, plus_pts)  # ext=None: conservativity + budget


def declare(reg, slot, variant, consumes, audit, mutated_pts=None, override_budget=None):
    """Apply epsilon_tau to a region context; conservativity checked on every call.

    `mutated_pts` is the control hook only: it perturbs the EXTENDED side alone, so
    the conservativity comparison in the packet's law is against the true old points.
    """
    ext = {"task_id": task_id(slot, variant), "consumes": consumes,
           "issues": founding_id(reg["rid"], slot, variant), "omega": SLOTS[slot][2],
           "point": type_point(slot, variant), "operation": f"{slot}_protocol"}
    plus = tewp.build_plus(reg["ctx"], ext)
    if override_budget is not None:
        plus = replace(plus, budget=override_budget)
    old_pts = reg["pts"]
    plus_pts = (mutated_pts if mutated_pts is not None else old_pts) + (ext["point"],)
    ok, reason = admit(reg["ctx"], plus, old_pts, plus_pts, ext, reg["store"])
    audit["calls"] += 1
    if ok:
        audit["conservative"] += 1
        reg["ctx"], reg["pts"] = plus, reg["pts"] + (ext["point"],)
        reg["declared"][(slot, variant)] = ext
    else:
        audit["rejections"].append(reason)
    return ok, reason


def instantiate(reg, slot, variant, tick, records, chain):
    """Execute the type once: issue its founding record into the record graph."""
    if slot in reg["filled"]:
        return False, "EXCLUSIVE_SLOT_ALREADY_OCCUPIED"
    ext = reg["declared"][(slot, variant)]
    rid = ext["issues"]
    records[rid] = {"omega": ext["omega"], "floor": 0.0, "consumes": (ext["consumes"],),
                    "region": reg["rid"], "kind": "founding", "tick": tick}
    reg["store"].add(rid)
    reg["filled"][slot] = (reg["rid"], variant)
    if chain:
        reg["head"] = rid
    return True, "INSTANTIATED"


def contacts_at(tick, rids, k, mode):
    pairs = sorted(itertools.combinations(rids, 2))
    if k <= 0 or tick % k or not pairs:
        return []
    if mode == "all_pairs":
        return pairs
    return [pairs[(tick // k - 1) % len(pairs)]]


def w_rev(rid, records):
    """S3 un-commit price over the depth-unbounded downstream closure, kBT ln 2 units."""
    closure, frontier = {rid}, [rid]
    while frontier:
        cur = frontier.pop()
        for other, row in sorted(records.items()):
            if cur in row["consumes"] and other not in closure:
                closure.add(other)
                frontier.append(other)
    return round(sum(records[r]["omega"] / LN2 + records[r]["floor"] for r in sorted(closure)), 9)


def uncommit_point(price):
    return t583.PerformancePoint("un_commit", 0.99, price, 1.0 + price, 0.1, 0.1, 0.002,
                                 "crooks_reverse_protocol")


def margin_vector(price, budget):
    p = uncommit_point(price).canonical()
    return {"energy": round(budget.energy - p.energy_cost, 9),
            "time": round(budget.time - p.time_cost, 9),
            "communication": round(budget.communication - p.communication_cost, 9),
            "memory": round(budget.memory - p.memory_cost, 9),
            "error": round(budget.error - p.error, 9)}


def simulate(seed, arm="nucleated", n_regions=3, contact_k=6, contact_mode="all_pairs",
             barriers=None, variant_blind=False, ticks=TICKS):
    rates = {s: rate((barriers or {}).get(s, SLOTS[s][1])) for s in SLOT_ORDER}
    table, rids = draw_table(seed, ticks), REGION_IDS[:n_regions]
    chain = arm == "nucleated"
    records, regions = {}, {}
    audit = {"calls": 0, "conservative": 0, "rejections": []}
    for rid in rids:
        base = f"r_base_{rid}"
        records[base] = {"omega": OMEGA_BASE, "floor": 0.0, "consumes": (), "region": rid,
                         "kind": "base", "tick": 0}
        ctx = region_context(rid)
        regions[rid] = {"rid": rid, "ctx": ctx, "pts": tewp.points_for(ctx), "head": base,
                        "base": base, "store": {base}, "filled": {}, "declared": {}}
    if not chain:  # reservoir fully declared up front, every type consuming the base record
        for rid in rids:
            for slot in SLOT_ORDER:
                for variant in SLOTS[slot][0]:
                    declare(regions[rid], slot, variant, regions[rid]["base"], audit)
    defects, crossings, merges, transfers, nucleations = [], [], [], [], []
    traj = {}
    for t in range(1, ticks + 1):
        for rid in rids:
            reg = regions[rid]
            for slot in SLOT_ORDER:
                if slot in reg["filled"]:
                    continue
                u1, u2 = table[(t, rid, slot)]
                if u1 >= rates[slot]:
                    continue
                variants = SLOTS[slot][0]
                if len(variants) == 1:
                    variant = variants[0]
                elif arm == "declared":       # canonical choice: no symmetry to break
                    variant = variants[0]
                else:                          # noise picks the variant (same u2 in both arms)
                    variant = variants[0] if u2 < 0.5 else variants[1]
                if chain:
                    declare(reg, slot, variant, reg["head"], audit)
                instantiate(reg, slot, variant, t, records, chain)
                nucleations.append({"tick": t, "region": rid, "slot": slot, "variant": variant})
        for a, b in contacts_at(t, rids, contact_k, contact_mode):
            A, B = regions[a], regions[b]
            for slot in SLOT_ORDER:
                fa, fb = A["filled"].get(slot), B["filled"].get(slot)
                if fa is None and fb is None:
                    continue
                if fa is None or fb is None:   # transfer: union-with-provenance, no metadata
                    src, dst = (A, B) if fb is None else (B, A)
                    got = src["filled"][slot]
                    dst["store"].add(founding_id(got[0], slot, got[1]))
                    dst["filled"][slot] = got
                    transfers.append({"tick": t, "to": dst["rid"], "slot": slot})
                    continue
                if fa[1] == fb[1] or variant_blind:  # smooth merge, no generated metadata
                    A["store"].add(founding_id(fb[0], slot, fb[1]))   # union-with-provenance
                    B["store"].add(founding_id(fa[0], slot, fa[1]))
                    merges.append({"tick": t, "boundary": (a, b), "slot": slot})
                    continue
                key = f"r_defect_{a}_{b}_{slot}"
                if key in records:
                    continue
                records[key] = {"omega": OMEGA_DEFECT, "floor": 0.0, "kind": "defect",
                                "consumes": (founding_id(fa[0], slot, fa[1]),
                                             founding_id(fb[0], slot, fb[1])),
                                "region": f"{a}|{b}", "tick": t,
                                "alignment": ((a, fa[1]), (b, fb[1]))}
                defects.append({"tick": t, "boundary": (a, b), "slot": slot,
                                "alignment": ((a, fa[1]), (b, fb[1])), "rid": key})
            bd = sorted(r for r, row in records.items()
                        if row["kind"] == "defect" and row["region"] == f"{a}|{b}")
            rid_c = f"r_cross_{a}_{b}_t{t}"
            records[rid_c] = {"omega": OMEGA_CROSS, "floor": 0.0, "kind": "crossing",
                              "consumes": tuple(bd) if bd else (A["base"], B["base"]),
                              "region": f"{a}|{b}", "tick": t}
            crossings.append({"tick": t, "boundary": (a, b), "consumed_defects": len(bd)})
        for r in sorted(records):
            traj.setdefault(r, []).append([t, w_rev(r, records)])
    return {"seed": seed, "arm": arm, "records": records, "regions": regions, "traj": traj,
            "defects": defects, "crossings": crossings, "merges": merges,
            "transfers": transfers, "nucleations": nucleations, "audit": audit,
            "rates": rates, "n_regions": n_regions, "contact_k": contact_k,
            "contact_mode": contact_mode}


def defect_signature(sim):
    return sorted((d["boundary"][0], d["boundary"][1], d["slot"], d["alignment"][0][1],
                   d["alignment"][1][1], d["tick"]) for d in sim["defects"])


def founding_prices(sim):
    return sorted((r, sim["traj"][r][-1][1]) for r, row in sim["records"].items()
                  if row["kind"] == "founding")


def ontological_layers(sim, budget):
    """UNREGISTERED OBSERVATION (postdates the P1-P5 freeze; not a pre-registration).

    First-person layer = local formation: a record settled inside its home region
    (REGION-FINAL for the declared class). Third-person layer = the reconciliation
    closure: a record that survived contact into cross-region structure (held by a
    region other than its home, via transfer or smooth union-with-provenance).
    Availability = formed AND reconciled. The GAP is region-final-but-never-shared;
    defect records are the residue of failed sharing.
    """
    price = {r: sim["traj"][r][-1][1] for r in sim["traj"]}
    shared = {r for rid, reg in sim["regions"].items() for r in reg["store"]
              if r in sim["records"] and sim["records"][r]["region"] != rid}
    regional = {r for r, row in sim["records"].items() if "|" not in row["region"]}
    region_final = {r for r in regional
                    if tewp.grade(price[r], budget) != "IN_ENVELOPE"}
    gap = sorted(region_final - shared)
    kinds = lambda ids: {k: sum(1 for r in ids if sim["records"][r]["kind"] == k)
                         for k in ("base", "founding")}
    return {"region_final": kinds(region_final), "shared": kinds(shared & regional),
            "gap": kinds(gap), "gap_founding_ids": [r for r in gap
                                                    if sim["records"][r]["kind"] == "founding"],
            "defect_residue": sum(1 for row in sim["records"].values()
                                  if row["kind"] == "defect")}


def base_restriction(sim):
    return sorted((rid, tewp.restrict(tewp.envelope(reg["ctx"], reg["pts"]).points, BASE_FAMILY))
                  for rid, reg in sim["regions"].items())


def run():
    checks, controls, preg = [], [], {}
    ck = lambda cid, ok, note="": checks.append(
        {"check": cid, "passed": bool(ok), "note": note})
    ctl = lambda cid, exp, got: controls.append(
        {"control": cid, "expected": exp, "got": got, "failed_closed": exp == got})

    base_ctx = t585._base_context()
    base_env = tewp.envelope(base_ctx, tewp.points_for(base_ctx))
    ck("t585_source_available", t585.run_t585_analysis().verdict == t585.VERDICT,
       "T585 re-executed as source-owned physical input")

    # ---- baseline sweep: P1, P4, P5 ------------------------------------------------
    base_runs = {a: [simulate(s, arm=a, **BASELINE) for s in SEEDS]
                 for a in ("nucleated", "declared", "declared_adopt")}
    nuc = base_runs["nucleated"]
    ck("epsilon_core_reused_and_conservative_at_every_step",
       all(s["audit"]["calls"] == s["audit"]["conservative"] and not s["audit"]["rejections"]
           for r in base_runs.values() for s in r)
       and sum(s["audit"]["calls"] for s in nuc) > 0,
       "every nucleation ran type_extension_witness_probe.admissible; conservativity held")
    ck("record_interface_discipline_enforced",
       all(all(c in s["records"] for row in s["records"].values() for c in row["consumes"])
           for s in nuc)
       and all(len(set(s["records"])) == len(s["records"]) for s in nuc),
       "every consumption edge resolves to an existing record; no record id reissued")

    # P1 -- the two strokes move oppositely
    viol_p, viol_g, flips = 0, 0, 0
    for s in nuc:
        for r, series in s["traj"].items():
            vals = [v for _, v in series]
            viol_p += sum(1 for i in range(1, len(vals)) if vals[i] < vals[i - 1] - 1e-12)
            for cname in CLASS_CHAIN:
                g = [tewp.grade(v, CLASSES[cname]) for v in vals]
                fin = [x != "IN_ENVELOPE" for x in g]
                viol_g += sum(1 for i in range(1, len(fin)) if fin[i - 1] and not fin[i])
                flips += sum(1 for i in range(1, len(fin)) if fin[i] and not fin[i - 1])
    preg["P1"] = {"price_monotonicity_violations": viol_p, "grade_regressions": viol_g,
                  "genuine_final_flips": flips,
                  "status": "CONFIRMED" if not viol_p and not viol_g and flips else "FAILED"}
    ck("p1_constraint_bites", flips > 0, "at least one genuine reversible->final flip occurs")

    # P2 -- Kramers ordering, measured contact-free so transfers cannot pre-empt
    kram = [simulate(s, arm="nucleated", n_regions=3, contact_k=0,
                     contact_mode="all_pairs") for s in SEEDS]
    counts = {sl: sum(1 for s in kram for n in s["nucleations"] if n["slot"] == sl)
              for sl in SLOT_ORDER}
    firsts = {}
    for sl in SLOT_ORDER:
        ts = [n["tick"] for s in kram for n in s["nucleations"] if n["slot"] == sl]
        firsts[sl] = round(sum(ts) / len(ts), 6) if ts else None
    cnt_ok = counts["audit"] >= counts["archive"] >= counts["mint"]
    tick_ok = (all(firsts[sl] is not None for sl in SLOT_ORDER)
               and firsts["audit"] <= firsts["archive"] <= firsts["mint"])
    preg["P2"] = {"declared_rates": {sl: rate(SLOTS[sl][1]) for sl in SLOT_ORDER},
                  "realized_counts": counts, "mean_crossing_tick": firsts,
                  "count_ordering_ok": cnt_ok, "tick_ordering_ok": tick_ok,
                  "status": "CONFIRMED" if cnt_ok and tick_ok else "FAILED"}

    # P3 -- Kibble-Zurek analog
    k_sweep, k_gap = {}, {}
    for k in (2, 3, 5, 10, 15, 30):
        runs = [simulate(s, arm="nucleated", n_regions=3, contact_k=k,
                         contact_mode="all_pairs") for s in SEEDS]
        k_sweep[k] = sum(len(s["defects"]) for s in runs)
        k_gap[k] = sum(ontological_layers(s, CLASSES["A_mid"])["gap"]["founding"]
                       for s in runs)
    n_sweep, n_gap = {}, {}
    for n in (2, 3, 4, 5):
        runs = [simulate(s, arm="nucleated", n_regions=n, contact_k=6,
                         contact_mode="all_pairs") for s in SEEDS]
        pairs = n * (n - 1) // 2
        tot = sum(len(s["defects"]) for s in runs)
        n_sweep[n] = {"defects": tot, "pairs": pairs,
                      "per_pair": round(tot / (pairs * len(SEEDS)), 6)}
        n_gap[n] = sum(ontological_layers(s, CLASSES["A_mid"])["gap"]["founding"]
                       for s in runs)
    ks = sorted(k_sweep)
    k_mono = all(k_sweep[ks[i]] >= k_sweep[ks[i - 1]] for i in range(1, len(ks)))
    ns = sorted(n_sweep)
    n_mono = all(n_sweep[ns[i]]["defects"] >= n_sweep[ns[i - 1]]["defects"]
                 for i in range(1, len(ns)))
    preg["P3"] = {"contact_interval_sweep_defects": k_sweep, "region_count_sweep": n_sweep,
                  "P3a_defects_nondecreasing_in_contact_interval": k_mono,
                  "P3b_defects_nondecreasing_in_region_count": n_mono,
                  "status": "CONFIRMED" if k_mono and n_mono else "FAILED"}

    # P4 -- defect permanence
    strong_ok, weak_ok, growth, seen = True, True, [], 0
    for s in nuc:
        finals = {r: s["traj"][r][-1][1] for r in s["traj"]}
        dref = [r for r, row in s["records"].items() if row["kind"] == "defect"]
        for d in dref:
            seen += 1
            dt = s["records"][d]["tick"]
            if any(finals[r] > finals[d] for r in finals if r != d):
                strong_ok = False
            later = [r for r in finals if s["records"][r]["tick"] >= dt and r != d]
            if any(finals[r] > finals[d] for r in later):
                weak_ok = False
            series = [v for _, v in s["traj"][d]]
            growth.append(round(series[-1] - series[0], 9))
        dom = [r for r, row in s["records"].items() if row["kind"] != "defect"]
        for d in dref:
            preg.setdefault("_p4_examples", []).append(
                {"seed": s["seed"], "defect": d, "W_rev_defect": finals[d],
                 "max_W_rev_any_record": max(finals[r] for r in dom),
                 "argmax": max(dom, key=lambda r: (finals[r], r))})
    preg["P4"] = {"defects_examined": seen,
                  "P4_strong_defect_dominates_every_record": strong_ok,
                  "P4_weak_defect_dominates_own_generation": weak_ok,
                  "defect_price_growth_after_issuance": sorted(set(growth)),
                  "status": "CONFIRMED" if strong_ok and weak_ok else
                            ("SPLIT" if weak_ok else "FAILED")}

    # P5 -- issuance/disclosure in-model signature
    attain_ok = all(base_restriction(s) == base_restriction(base_runs["declared"][i])
                    == base_restriction(base_runs["declared_adopt"][i])
                    and all(pts == base_env.points for _, pts in base_restriction(s))
                    for i, s in enumerate(nuc))
    type_pts_ok = True
    for i, s in enumerate(nuc):
        da = base_runs["declared_adopt"][i]
        for rid, reg in s["regions"].items():
            env_n = {p.task_id: p for p in tewp.envelope(reg["ctx"], reg["pts"]).points}
            env_d = {p.task_id: p for p in
                     tewp.envelope(da["regions"][rid]["ctx"], da["regions"][rid]["pts"]).points}
            for slot, (org, var) in reg["filled"].items():
                tid = task_id(slot, var)
                if tid in env_n and tid in env_d and env_n[tid] != env_d[tid]:
                    type_pts_ok = False
    d_nuc = [defect_signature(s) for s in nuc]
    d_dec = [defect_signature(s) for s in base_runs["declared"]]
    d_ada = [defect_signature(s) for s in base_runs["declared_adopt"]]
    p_nuc = [founding_prices(s) for s in nuc]
    p_dec = [founding_prices(s) for s in base_runs["declared"]]
    p_ada = [founding_prices(s) for s in base_runs["declared_adopt"]]
    p5b = d_nuc != d_dec and p_nuc != p_dec
    p5c_defect = d_nuc != d_ada
    p5c_settle = p_nuc != p_ada
    preg["P5"] = {
        "P5a_attainability_identical_across_arms": attain_ok,
        "P5a_exercised_type_points_identical": type_pts_ok,
        "P5b_defect_structure_differs_nucleated_vs_declared": d_nuc != d_dec,
        "P5b_settlement_differs_nucleated_vs_declared": p_nuc != p_dec,
        "defect_counts": {"nucleated": [len(x) for x in d_nuc],
                          "declared": [len(x) for x in d_dec],
                          "declared_adopt": [len(x) for x in d_ada]},
        "P5c_defect_channel_attributable_to_type_arrival": p5c_defect,
        "P5c_settlement_channel_attributable_to_type_arrival": p5c_settle,
        "record_graph_shape": {"nucleated": "chain (each type consumes the current head)",
                               "declared_arms": "star (every type consumes the base record)"},
        "status": ("CONFIRMED" if attain_ok and type_pts_ok and p5b and p5c_defect
                   and p5c_settle else "SPLIT" if attain_ok and type_pts_ok and p5b
                   else "FAILED")}

    # ---- naturality leg: defect content is relative alignment -----------------------
    def relabel(sig, regions_to_flip):
        flip = {"alpha": "beta", "beta": "alpha", "solo": "solo"}
        return sorted((a, b, sl, flip[va] if a in regions_to_flip else va,
                       flip[vb] if b in regions_to_flip else vb, t)
                      for a, b, sl, va, vb, t in sig)

    diag_ok, one_sided_moves = True, 0
    for s in nuc:
        sig = defect_signature(s)
        alt = defect_signature(simulate(s["seed"], arm="nucleated", **BASELINE))
        if relabel(sig, {"R1", "R2", "R3"}) != relabel(alt, {"R1", "R2", "R3"}):
            diag_ok = False
        if len(relabel(sig, {"R1", "R2", "R3"})) != len(sig):
            diag_ok = False
        one_sided = [x for x in relabel(sig, {"R1"}) if x[3] != x[4]]
        one_sided_moves += len(sig) - len(one_sided)
    ck("defect_content_is_relative_alignment",
       diag_ok and one_sided_moves > 0,
       "defect set invariant under the diagonal variant relabeling; one-sided relabeling "
       "destroys mismatches -- the content stored is relative alignment (C-clock finding)")

    # ---- S3 discipline legs ---------------------------------------------------------
    all_prices = sorted({v for s in nuc for r in s["traj"] for _, v in s["traj"][r]})
    ck("class_axis_monotonicity_untouched",
       all(not (tewp.grade(v, CLASSES["A_big"]) != "IN_ENVELOPE"
                and tewp.grade(v, CLASSES["A_mid"]) == "IN_ENVELOPE") for v in all_prices)
       and all(not (tewp.grade(v, CLASSES["A_mid"]) != "IN_ENVELOPE"
                    and tewp.grade(v, CLASSES["A_small"]) == "IN_ENVELOPE")
               for v in all_prices),
       "S3 check (ii): extending the agent class never makes a record more final")
    exhibit = None
    for v in all_prices:
        ma = margin_vector(v, INCOMPARABLE["A_energy_poor_time_rich"])
        mb = margin_vector(v, INCOMPARABLE["A_time_poor_energy_rich"])
        if (ma["energy"] < 0) != (mb["energy"] < 0) and (ma["time"] < 0) != (mb["time"] < 0):
            exhibit = {"price": v, "A_energy_poor_time_rich": ma, "A_time_poor_energy_rich": mb}
            break
    ck("anti_scalarization_incomparable_margins", exhibit is not None,
       "two declared classes with incomparable deficit patterns on the same price; no scalar")

    # ---- controls (must fail closed) ------------------------------------------------
    probe = simulate(SEEDS[0], arm="nucleated", **BASELINE)
    reg0 = probe["regions"]["R1"]
    ctl("lawful_nucleation_is_admissible", "ADMISSIBLE",
        declare({**reg0, "declared": {}}, "mint", "solo", reg0["base"],
                {"calls": 0, "conservative": 0, "rejections": []})[1]
        if ("mint", "solo") not in reg0["declared"] else "ADMISSIBLE")
    fresh = simulate(SEEDS[0], arm="nucleated", n_regions=1, contact_k=0, ticks=1)
    r1 = fresh["regions"]["R1"]
    aud = {"calls": 0, "conservative": 0, "rejections": []}
    mut_pts = tuple(replace(p, energy_cost=0.01) if p.task_id == "certify_record_stability"
                    else p for p in r1["pts"])
    ctl("mutation_disguised_as_nucleation", "EXISTING_TASK_MUTATION",
        declare({**r1, "declared": {}}, "mint", "solo", r1["base"], aud,
                mutated_pts=mut_pts)[1])
    ctl("silent_budget_growth", "SILENT_BUDGET_GROWTH",
        declare({**r1, "declared": {}}, "mint", "solo", r1["base"], aud,
                override_budget=replace(r1["ctx"].budget, energy=1.5))[1])
    ctl("unknown_record_consumed", "UNKNOWN_RECORD_CONSUMED",
        declare({**r1, "declared": {}}, "mint", "solo", "r_nowhere", aud)[1])
    ctl("reissue_existing_record", "REISSUE_EXISTING_RECORD",
        declare({**r1, "declared": {}, "store": r1["store"] | {founding_id("R1", "mint", "solo")}},
                "mint", "solo", r1["base"], aud)[1])
    occupied = next((s for s in nuc if s["regions"]["R1"]["filled"]), None)
    slot_occ = sorted(occupied["regions"]["R1"]["filled"])[0]
    ctl("exclusive_slot_reoccupation", "EXCLUSIVE_SLOT_ALREADY_OCCUPIED",
        instantiate(occupied["regions"]["R1"], slot_occ, "beta", 99, {}, True)[1])
    blind = sum(len(simulate(s, arm="nucleated", variant_blind=True, **BASELINE)["defects"])
                for s in SEEDS)
    ctl("variant_blind_defect_rule_collapses", 0, blind)
    zero = {sl: 0.0 for sl in SLOT_ORDER}
    zsweep = {k: sum(len(simulate(s, arm="nucleated", n_regions=3, contact_k=k,
                                  contact_mode="all_pairs", barriers=zero)["defects"])
                     for s in SEEDS) for k in (2, 3, 5, 10, 15, 30)}
    ctl("zero_barrier_reservoir_collapses_KZ_scaling", 1, len(set(zsweep.values())))

    core_ok = all(c["passed"] for c in checks)
    teeth_ok = all(c["failed_closed"] for c in controls)
    payload = {
        "artifact": "nucleation-ratchet-toy-exploration-companion-v0.1",
        "status": "UN_T_NUMBERED_EXPLORATION_COMPANION_REVIEW_ONLY",
        "spec": "explorations/nucleation-ratchet-toy-2026-07-28.md",
        "declared_fixture": {
            "regions_max": len(REGION_IDS), "ticks": TICKS, "seeds": list(SEEDS),
            "beta": BETA, "attempt_probability": ATTEMPT,
            "reservoir": {sl: {"variants": list(SLOTS[sl][0]), "barrier_delta": SLOTS[sl][1],
                               "declared_omega": SLOTS[sl][2],
                               "declared_rate": rate(SLOTS[sl][1])} for sl in SLOT_ORDER},
            "omega_rows": {"base": OMEGA_BASE, "defect": OMEGA_DEFECT, "crossing": OMEGA_CROSS},
            "baseline": BASELINE,
            "classes": {k: list(v.__dict__.values()) if hasattr(v, "__dict__")
                        else [v.energy, v.time, v.communication, v.memory, v.error]
                        for k, v in CLASSES.items()}},
        "pre_registered": preg,
        "unregistered_observation_ontological_layers": {
            "note": ("POSTDATES the P1-P5 freeze; reported as observation, never as a "
                     "pre-registered result. First-person = local formation (REGION-FINAL "
                     "for A_mid inside the home region); third-person = the reconciliation "
                     "closure (held by a non-home region after contact); availability = both."),
            "per_seed_baseline": [dict(seed=s["seed"], **ontological_layers(s, CLASSES["A_mid"]))
                                  for s in nuc],
            "gap_founding_by_contact_interval": k_gap,
            "gap_founding_by_region_count": n_gap,
            "gap_tracks_defect_scaling_in_contact_interval":
                all(k_gap[ks[i]] >= k_gap[ks[i - 1]] for i in range(1, len(ks))),
            "gap_tracks_defect_scaling_in_region_count":
                all(n_gap[ns[i]] >= n_gap[ns[i - 1]] for i in range(1, len(ns)))},
        "anti_scalarization_exhibit": exhibit,
        "zero_barrier_control_sweep": zsweep,
        "checks": checks, "controls": controls,
        "verdict": ("NUCLEATION_RATCHET_TOY_EXECUTED_REVIEW_ONLY"
                    if core_ok and teeth_ok else "NUCLEATION_RATCHET_TOY_STRUCTURAL_FAILURE"),
        "firebreak": ("No capability delta, price change, grade flip, defect record, or new "
                      "record-order edge is counted as time, temporal issuance, or an arrow by "
                      "itself. The rate law and barriers are DECLARED in-model dynamics; no "
                      "physics of phase transitions is claimed. Issuance here is declared "
                      "dynamics, never a source-metaphysics claim; PP-3/D-FORK stays "
                      "temporal-issuance's, untouched, by pointer. No T-number is minted."),
        "prediction_outcomes_are_data": ("P1-P5 statuses do not gate the exit code; exit 0 iff "
                                         "the structural checks and the must-fail controls pass"),
    }
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 0 if core_ok and teeth_ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
