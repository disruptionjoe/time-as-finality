"""T19: Phenomenal Bridge as Complexity Separation.

Extends the T60 observer closure witness with external witness nodes to
demonstrate the phenomenal bridge gap as a formal record-graph separation.

Graph structure:

    CORE (R's internal world):
        e_src --> e_R_recv --> e_R_rec1 --> e_R_final

    EXTERNAL (third-person witnesses, causally after R's finalization):
        e_R_final --> e_E1
        e_R_final --> e_E2
        e_E1 --> e_meta
        e_E2 --> e_meta

Propositions:
    world_fact        : e_src, e_R_recv
    R_obs             : e_R_recv (bridge record), e_R_rec1, e_R_final
    R_self_finality   : e_E1, e_E2, e_meta

    R_self_finality records exist ONLY in external nodes. They represent
    third-person witnesses who record R's finalization from outside R's
    causal boundary (causally after e_R_final).

Decision problem:
    Is R's finality assignment (R_self_finality) accessible to the agent?

    INTERNAL query (R at e_R_final, accessible_holders = A*(R)):
        e_E1, e_E2, e_meta are causally after e_R_final.
        accessible_records raises ValueError for evaluation at e_R_final.
        accessible_support(R_self_finality at e_R_final) = 0 < 1.
        Answer: NO. R cannot verify its own finality from within A*(R).

    EXTERNAL query (omniscient observer at e_meta, all holders):
        h_E1 holds R_self_finality@e_E1 (e_E1 <= e_meta, causally before).
        h_E2 holds R_self_finality@e_E2 (e_E2 <= e_meta, causally before).
        accessible_support(R_self_finality at e_meta) = 2 >= 1.
        Answer: YES. External observer verifies R's finality in O(|G|) time.

    SEPARATION: External YES, Internal NO.
        FIRST-PERSON-FINALITY is not computable from A*(R).
        THIRD-PERSON-FINALITY is decidable in polynomial time from G.

    The gap is structural (causal-boundary obstruction), not computational
    (not merely a time bound). R's computational power is irrelevant: the
    required records are causally outside R's observation horizon.

    Formal relatives:
    - Goedel: a consistent system cannot prove its own consistency from within.
    - Rice's theorem: a program cannot decide semantic properties of its own
      output by inspecting its own running state.
    - T19's gap: a bounded observer cannot verify that its finalization is
      externally recorded, because the witnesses are in its causal future.
"""

from __future__ import annotations

import sys

from t1_record_graph import CausalRecordGraph, Record, Observer

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

FINALIZATION_THRESHOLD = 1

# Primary proposition checked when finalizing each node.
NODE_PROPOSITION: dict[str, str] = {
    "e_src":     "world_fact",
    "e_R_recv":  "world_fact",
    "e_R_rec1":  "R_obs",
    "e_R_final": "R_obs",
    # External nodes: third-person witnesses to R's finalization.
    "e_E1":      "R_self_finality",
    "e_E2":      "R_self_finality",
    "e_meta":    "R_self_finality",
}

CORE_NODES = frozenset({"e_src", "e_R_recv", "e_R_rec1", "e_R_final"})
EXTERNAL_NODES = frozenset({"e_E1", "e_E2", "e_meta"})


# ---------------------------------------------------------------------------
# Graph construction
# ---------------------------------------------------------------------------

def build_T19_graph() -> tuple[CausalRecordGraph, dict[str, str]]:
    """
    Build the T19 separation witness graph.

    Core (R's internal world): 4 nodes in a linear causal chain.
    External (third-person witnesses): 3 nodes causally after e_R_final.

    Returns (graph, event_to_holder).
    """
    g = CausalRecordGraph()

    for ev in sorted(CORE_NODES | EXTERNAL_NODES):
        g.add_event(ev)

    # Core causal chain (R's internal world)
    g.add_causal_edge("e_src",     "e_R_recv")
    g.add_causal_edge("e_R_recv",  "e_R_rec1")
    g.add_causal_edge("e_R_rec1",  "e_R_final")

    # External witness edges: causally after R's finalization.
    # e_E1 and e_E2 observe R from outside; e_meta is the external
    # omniscient observation point.
    g.add_causal_edge("e_R_final", "e_E1")
    g.add_causal_edge("e_R_final", "e_E2")
    g.add_causal_edge("e_E1",      "e_meta")
    g.add_causal_edge("e_E2",      "e_meta")

    # --- Records: world_fact ---
    # e_src generates the base record; e_R_recv holds a copy (bootstraps iteration).
    g.add_record(Record("rec_wf_src",  "world_fact", "true", "e_src",    "h_src",    2.0))
    g.add_record(Record("rec_wf_recv", "world_fact", "true", "e_R_recv", "h_R_recv", 2.0))

    # --- Records: R_obs ---
    # Bridge record at e_R_recv (h_R_recv holds both world_fact AND R_obs) enables
    # the world_fact -> R_obs handoff so e_R_rec1 can be finalized once h_R_recv
    # is accessible.
    g.add_record(Record("rec_obs_recv",  "R_obs", "true", "e_R_recv",  "h_R_recv",  2.0))
    g.add_record(Record("rec_obs_rec1",  "R_obs", "true", "e_R_rec1",  "h_R_rec1",  2.0))
    g.add_record(Record("rec_obs_final", "R_obs", "true", "e_R_final", "h_R_final", 3.0))

    # --- Records: R_self_finality (EXTERNAL ONLY) ---
    # These represent third-person witnesses who record R's finalization from
    # outside R's causal boundary. They appear only at events causally after
    # e_R_final, so they are outside R's observation horizon.
    g.add_record(Record("rec_sf_E1",   "R_self_finality", "true", "e_E1",  "h_E1",  2.0))
    g.add_record(Record("rec_sf_E2",   "R_self_finality", "true", "e_E2",  "h_E2",  2.0))
    g.add_record(Record("rec_sf_meta", "R_self_finality", "true", "e_meta","h_meta", 3.0))

    event_to_holder: dict[str, str] = {
        "e_src":     "h_src",
        "e_R_recv":  "h_R_recv",
        "e_R_rec1":  "h_R_rec1",
        "e_R_final": "h_R_final",
        "e_E1":      "h_E1",
        "e_E2":      "h_E2",
        "e_meta":    "h_meta",
    }

    return g, event_to_holder


# ---------------------------------------------------------------------------
# D1 finalization check (uses T19's NODE_PROPOSITION)
# ---------------------------------------------------------------------------

def is_finalized(
    graph: CausalRecordGraph,
    node: str,
    observer: Observer,
) -> bool:
    """Return True if node is finalized from observer's current access perspective.

    Returns False if node is not in the observer's causal past (ValueError from
    accessible_records is the structural signal that the node is inaccessible).
    """
    prop = NODE_PROPOSITION[node]
    try:
        profile = graph.finality_profile(
            observer=observer,
            proposition=prop,
            value="true",
            threshold=FINALIZATION_THRESHOLD,
            event=node,
        )
    except ValueError:
        # Node is not in the observer's causal past -- structurally inaccessible.
        return False
    return profile.accessible_support >= FINALIZATION_THRESHOLD


# ---------------------------------------------------------------------------
# Update operator (R's bounded D1 iteration, observer anchored at e_R_final)
# ---------------------------------------------------------------------------

def update_operator(
    graph: CausalRecordGraph,
    all_nodes: frozenset[str],
    current_access: frozenset[str],
    event_to_holder: dict[str, str],
    observer_event: str = "e_R_final",
) -> frozenset[str]:
    """f(S): expand R's finalized access set given current access S.

    External nodes (e_E1, e_E2, e_meta) are causally after observer_event.
    finality_profile raises ValueError for those -- is_finalized returns False.
    So f(S) always stays within CORE_NODES regardless of S.
    """
    accessible_holders = frozenset(
        event_to_holder[n] for n in current_access if n in event_to_holder
    )
    observer = Observer(
        observer_id="R",
        event=observer_event,
        accessible_holders=accessible_holders,
        level="reconciler",
    )
    return frozenset(node for node in all_nodes if is_finalized(graph, node, observer))


# ---------------------------------------------------------------------------
# Monotonicity check (Knaster-Tarski precondition)
# ---------------------------------------------------------------------------

def check_monotonicity(
    graph: CausalRecordGraph,
    all_nodes: frozenset[str],
    event_to_holder: dict[str, str],
) -> tuple[bool, list[str]]:
    """Verify f(S) <= f(S') for all S <= S' in the powerset of all_nodes."""
    nodes_list = sorted(all_nodes)
    n = len(nodes_list)

    all_subsets = [
        frozenset(nodes_list[i] for i in range(n) if mask & (1 << i))
        for mask in range(1 << n)
    ]

    f_cache: dict[frozenset[str], frozenset[str]] = {
        s: update_operator(graph, all_nodes, s, event_to_holder)
        for s in all_subsets
    }

    violations: list[str] = []
    for i, S in enumerate(all_subsets):
        for S_prime in all_subsets[i:]:
            if S <= S_prime:
                fS = f_cache[S]
                fS_prime = f_cache[S_prime]
                if not fS <= fS_prime:
                    violations.append(
                        f"  VIOLATION: f({sorted(S)}) not subset of f({sorted(S_prime)})"
                    )

    return len(violations) == 0, violations


# ---------------------------------------------------------------------------
# Fixed-point iteration (R's bounded view)
# ---------------------------------------------------------------------------

def run_r_iteration(
    graph: CausalRecordGraph,
    all_nodes: frozenset[str],
    event_to_holder: dict[str, str],
    base_node: str = "e_src",
) -> dict:
    """Run R's D1 update from base {base_node} to fixed point."""
    current = frozenset({base_node})
    step = 0

    print(f"\n{'='*60}")
    print("R's Bounded D1 Access-Update Iteration (observer at e_R_final)")
    print(f"{'='*60}")
    print(f"Base access set (step 0): {sorted(current)}")

    while True:
        step += 1
        next_access = update_operator(graph, all_nodes, current, event_to_holder)
        print(f"Step {step}: {sorted(current)} => {sorted(next_access)}")

        if next_access == current:
            print(f"\nConverged at step {step}.")
            break

        current = next_access

        if step > len(all_nodes) + 5:
            print(f"\n[ERROR] Did not converge after {step} steps.")
            return {"converged": False, "steps": step, "fixed_point": current}

    return {"converged": True, "steps": step, "fixed_point": current}


# ---------------------------------------------------------------------------
# T19 decision problem queries
# ---------------------------------------------------------------------------

def finality_query(
    graph: CausalRecordGraph,
    proposition: str,
    eval_event: str,
    observer_event: str,
    accessible_holders: frozenset[str],
    label: str,
) -> tuple[bool, int]:
    """
    Query whether proposition is finalized at eval_event given accessible_holders.

    observer_event: the observer's own observation horizon (eval_event must
    be in its causal past; otherwise raises ValueError -> returns (False, 0)).
    """
    observer = Observer(
        observer_id=label,
        event=observer_event,
        accessible_holders=accessible_holders,
        level="reconciler",
    )
    try:
        profile = graph.finality_profile(
            observer=observer,
            proposition=proposition,
            value="true",
            threshold=FINALIZATION_THRESHOLD,
            event=eval_event,
        )
        return profile.accessible_support >= FINALIZATION_THRESHOLD, profile.accessible_support
    except ValueError:
        return False, 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    graph, event_to_holder = build_T19_graph()
    all_nodes = graph.events
    all_holders = frozenset(event_to_holder.values())

    print("\n" + "="*60)
    print("T19: PHENOMENAL BRIDGE AS COMPLEXITY SEPARATION")
    print("="*60)

    # --- Graph summary ---
    print("\n[Graph topology]")
    print("CORE (R's internal world):")
    print("  e_src -> e_R_recv -> e_R_rec1 -> e_R_final")
    print("EXTERNAL (third-person witnesses, causally after e_R_final):")
    print("  e_R_final -> e_E1 -> e_meta")
    print("  e_R_final -> e_E2 -> e_meta")

    print("\nPropositions:")
    for ev in sorted(all_nodes):
        print(f"  {ev:12s} => {NODE_PROPOSITION[ev]}")

    print("\nRecords:")
    for rec in sorted(graph.records.values(), key=lambda r: r.record_id):
        print(f"  {rec.record_id:20s}: prop={rec.proposition!r:20s} "
              f"event={rec.event!r} holder={rec.holder!r}")

    # --- Monotonicity check ---
    print("\n" + "-"*60)
    print("[Monotonicity check -- full powerset of all 7 nodes]")
    n = len(all_nodes)
    total_subsets = 1 << n
    print(f"Nodes: {n}, Subsets: {total_subsets}, "
          f"Pairs checked: ~{total_subsets*(total_subsets+1)//2}")

    monotone, violations = check_monotonicity(graph, all_nodes, event_to_holder)
    if monotone:
        print("RESULT: MONOTONICITY HOLDS. Knaster-Tarski theorem applies.")
        print("  f(S) subset-of f(S') for all S subset-of S'.")
        print("  Note: f(S) is always a subset of CORE_NODES (external nodes")
        print("  are causally after e_R_final, so always raise ValueError in")
        print("  finality_profile -- is_finalized returns False for them).")
    else:
        print(f"RESULT: MONOTONICITY FAILS -- {len(violations)} violation(s).")
        for v in violations[:5]:
            print(v)

    # --- R's bounded fixed-point iteration ---
    r_results = run_r_iteration(graph, all_nodes, event_to_holder)
    fixed_point: frozenset[str] = r_results.get("fixed_point", frozenset())

    r_accessible_holders = frozenset(
        event_to_holder[n] for n in fixed_point if n in event_to_holder
    )

    print(f"\nR's fixed-point access set:    {sorted(fixed_point)}")
    print(f"R's accessible holders (A*(R)): {sorted(r_accessible_holders)}")
    print(f"External nodes in R's fixed pt: {sorted(EXTERNAL_NODES & fixed_point)}")
    r_self_included = "e_R_final" in fixed_point
    print(f"R self-included (T60 condition): {r_self_included}")

    # --- Decision problem queries ---
    print("\n" + "-"*60)
    print("[T19 Decision Problem: Is R's finality assignment recorded in G?]")
    print()

    # Query 1: R_obs at e_R_final (internal -- R CAN verify its own records)
    q1_ok, q1_support = finality_query(
        graph, "R_obs", "e_R_final", "e_R_final",
        r_accessible_holders, "R_INTERNAL"
    )
    print("Query 1: R_obs at e_R_final (INTERNAL -- R verifying its own records)")
    print(f"  Accessible holders: {sorted(r_accessible_holders)}")
    print(f"  accessible_support: {q1_support}")
    print(f"  Answer: {'YES' if q1_ok else 'NO'}  "
          f"<-- R {'CAN' if q1_ok else 'CANNOT'} verify its internal records")

    print()

    # Query 2: R_self_finality at e_R_final (internal -- R CANNOT verify)
    # The R_self_finality records are at e_E1, e_E2, e_meta (causally after e_R_final).
    # accessible_records raises ValueError for those => accessible_support = 0.
    q2_ok, q2_support = finality_query(
        graph, "R_self_finality", "e_R_final", "e_R_final",
        r_accessible_holders, "R_INTERNAL"
    )
    print("Query 2: R_self_finality at e_R_final (INTERNAL -- R's self-finality query)")
    print(f"  Accessible holders: {sorted(r_accessible_holders)}")
    print(f"  R_self_finality records exist at: e_E1 (h_E1), e_E2 (h_E2), e_meta (h_meta)")
    print(f"  e_E1, e_E2, e_meta are causally AFTER e_R_final => ValueError => 0 support")
    print(f"  accessible_support: {q2_support}")
    print(f"  Answer: {'YES' if q2_ok else 'NO'}  "
          f"<-- R {'CAN' if q2_ok else 'CANNOT'} verify its own finality is recorded")

    print()

    # Query 3: R_self_finality at e_meta (external -- third-person CAN verify)
    q3_ok, q3_support = finality_query(
        graph, "R_self_finality", "e_meta", "e_meta",
        all_holders, "EXTERNAL"
    )
    print("Query 3: R_self_finality at e_meta (EXTERNAL -- third-person omniscient)")
    print(f"  Accessible holders (all): {sorted(all_holders)}")
    print(f"  h_E1 holds R_self_finality@e_E1 (e_E1 <= e_meta) => counts")
    print(f"  h_E2 holds R_self_finality@e_E2 (e_E2 <= e_meta) => counts")
    print(f"  h_meta holds R_self_finality@e_meta (e_meta <= e_meta) => counts")
    print(f"  accessible_support: {q3_support}")
    print(f"  Answer: {'YES' if q3_ok else 'NO'}  "
          f"<-- Third-person {'CAN' if q3_ok else 'CANNOT'} verify R's finality")

    # --- Verdict ---
    separation_holds = r_self_included and (not q2_ok) and q3_ok

    print("\n" + "="*60)
    print("[VERDICT: T19 PHENOMENAL BRIDGE SEPARATION]")
    print()

    print(f"(1) T60 CLOSURE HOLDS: {r_self_included}")
    print(f"    R self-included in fixed point: e_R_final in {sorted(fixed_point)}")
    print()

    print(f"(2) INTERNAL SELF-FINALITY QUERY (Query 2): {'YES' if q2_ok else 'NO'}")
    print(f"    R_self_finality records are causally outside R's observation horizon.")
    print(f"    accessible_support = {q2_support}. R cannot certify its own finality from A*(R).")
    print()

    print(f"(3) EXTERNAL SELF-FINALITY QUERY (Query 3): {'YES' if q3_ok else 'NO'}")
    print(f"    Third-person observer at e_meta sees {q3_support} R_self_finality records.")
    print(f"    R's finalization is verifiable in O(|G|) time from the external view.")
    print()

    print(f"(4) SEPARATION HOLDS: {'YES' if separation_holds else 'NO'}")
    if separation_holds:
        print()
        print("    FIRST-PERSON-FINALITY(A*(R), R_self_finality at e_R_final) = NO")
        print("    THIRD-PERSON-FINALITY(G,    R_self_finality at e_meta)     = YES")
        print()
        print("    Nature of the gap:")
        print("    Causal-boundary obstruction, NOT a computational complexity limit.")
        print("    R's finality witnesses (e_E1, e_E2) are causally AFTER e_R_final.")
        print("    No increase in R's computational power or memory bridges this gap.")
        print("    Only an observer positioned at e_meta (after the witnesses) can verify.")
        print()
        print("    Complexity class placement:")
        print("    EXTERNAL: decidable in O(|G|) time (scan G for R_self_finality records).")
        print("    INTERNAL: not computable from A*(R), regardless of time.")
        print("              The function is not in the image of any A*(R)-local computation.")
        print()
        print("    This is stronger than undecidability:")
        print("    The answer is not undecidable from within -- it is provably unreachable.")
        print("    A*(R) contains no R_self_finality records and no path to them.")
        print()
        print("    Formal relatives:")
        print("    - Goedel: consistent system cannot prove its own consistency from within.")
        print("    - Rice: program cannot decide its own semantic properties by self-inspection.")
        print("    - T19: bounded observer cannot verify its finality is externally witnessed,")
        print("      because the witnesses are in its causal future.")
        print()
        print("    H6 implication:")
        print("    The phenomenal bridge is not a missing mechanism.")
        print("    It is the formal location of the causal-boundary gap:")
        print("    first-person finality verification requires access to events in the")
        print("    observer's causal future -- structurally outside A*(R).")
        print("    T60 + T19: closure is guaranteed (T60) but not self-verifiable (T19).")
        print("    This is the formal content of H6.")
    else:
        print("    Separation NOT established -- check graph construction and results above.")

    print("\n" + "="*60)
    print("T19 Step 1 complete.")
    print("="*60)


if __name__ == "__main__":
    main()
