# TAF-001 evidence computation v0.1
# Pure Python, stdlib only, deterministic. Implements the Time as Finality
# T1/FORMALISM record model: finite causal record graph (DAG), record tokens
# (id, proposition, value, event, holder, erasure_cost), bounded observer
# access sets, the reconstruction rule (fixed threshold + no competing value
# at threshold), and the observer-indexed D1 profile (A, R, B, C).
# Evaluation uses causal reachability only; no topological ordering, metric
# time, or global clock enters the computation (invariance asserted below).

from collections import namedtuple
from itertools import combinations

Record = namedtuple("Record", "id prop value event holder erasure_cost")


def reachability(nodes, edges):
    """Transitive closure of the DAG as a set of ordered pairs (a, b), a <_c b."""
    reach = set(edges)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(reach):
            for (c, d) in list(reach):
                if b == c and (a, d) not in reach:
                    reach.add((a, d))
                    changed = True
    return reach


def causally_leq(a, b, reach):
    return a == b or (a, b) in reach


def accessible_supporting(records, access_set, prop, value, eval_event, reach):
    """Active records supporting (prop, value) causally available to the
    observer at eval_event: formation event <=_c eval_event AND holder in the
    observer's bounded access set (FORMALISM, Causal Record Graph, conds 1-2)."""
    return [r for r in records
            if r.prop == prop and r.value == value
            and r.holder in access_set
            and causally_leq(r.event, eval_event, reach)]


def antichain_width(events, reach):
    """Width of the largest causal antichain among the given formation events."""
    ev = sorted(set(events))
    best = 0
    for n in range(len(ev), 0, -1):
        for combo in combinations(ev, n):
            if all(not causally_leq(x, y, reach) and not causally_leq(y, x, reach)
                   for x, y in combinations(combo, 2)):
                return n
    return best


def d1_profile(records, access_set, prop, value, eval_event, reach, k):
    """F_O,e(x) = (A, R, B, C) per FORMALISM 'Observer-Indexed Finality Profile'."""
    supp = accessible_supporting(records, access_set, prop, value, eval_event, reach)
    A = len(supp)
    R = len({r.holder for r in supp})
    B = antichain_width([r.event for r in supp], reach) if supp else 0
    C = (A - k + 1) if A >= k else 0  # min accessible supporting erasures to drop below k
    return (A, R, B, C)


def reconstructible(records, access_set, prop, value, eval_event, reach, k):
    """FORMALISM 'Reconstruction Rule': accessible support reaches the fixed
    threshold AND no competing value for the same proposition reaches it."""
    A = len(accessible_supporting(records, access_set, prop, value, eval_event, reach))
    if A < k:
        return False
    competing_values = {r.value for r in records if r.prop == prop and r.value != value}
    for v2 in competing_values:
        A2 = len(accessible_supporting(records, access_set, prop, v2, eval_event, reach))
        if A2 >= k:
            return False
    return True


# ---------------------------------------------------------------------------
# Shared baseline world W0
# ---------------------------------------------------------------------------
EVAL = "e_obs"
K = 2  # reconstruction threshold, fixed before evaluation (FORMALISM primitive 6)

BASE_NODES = ["src", "a1", "a2", "b1", "b2", "c1", "d1", "d2",
              "f1", "f2", "f3", "f4", EVAL]
BASE_EDGES = [
    ("src", "a1"), ("a1", "a2"),            # a1 <_c a2 (chained formation)
    ("src", "b1"), ("src", "b2"),
    ("src", "c1"),
    ("src", "d1"), ("src", "d2"),
    ("src", "f1"), ("src", "f2"), ("src", "f3"), ("src", "f4"),
    ("a2", EVAL), ("b1", EVAL), ("b2", EVAL), ("c1", EVAL),
    ("d1", EVAL), ("d2", EVAL),
    ("f1", EVAL), ("f2", EVAL), ("f3", EVAL), ("f4", EVAL),
]
BASE_RECORDS = [
    Record("r1",  "p1", 1, "a1", "h1", 1),
    Record("r2",  "p1", 1, "a2", "h2", 1),
    Record("r3",  "p2", 1, "b1", "h1", 1),
    Record("r4",  "p2", 1, "b2", "h3", 1),
    Record("r5",  "p3", 1, "c1", "h4", 1),
    Record("r6",  "p4", 1, "d1", "h1", 1),
    Record("r7",  "p4", 0, "d2", "h2", 1),
    Record("r8",  "p5", 1, "f1", "h1", 1),
    Record("r9",  "p5", 1, "f2", "h2", 1),
    Record("r10", "p5", 0, "f3", "h3", 1),
    Record("r11", "p5", 0, "f4", "h3", 1),
]
BASE_ACCESS = frozenset({"h1", "h2"})

# Shared task vocabulary TV: five reconstruction tasks in the FORMALISM
# reconstruction-rule sense. A task is achieved in a world iff its
# proposition-value pair is reconstructible for O at e_obs under threshold K.
TASKS = [("tau1", "p1", 1), ("tau2", "p2", 1), ("tau3", "p3", 1),
         ("tau4", "p4", 1), ("tau5", "p5", 1)]

# ---------------------------------------------------------------------------
# Intervention ALPHA: access-structure change only (T46 RecordAccessSystem
# observer-access side). Holder-access set {h1,h2} -> {h1,h2,h3}. The causal
# record graph and record inventory are byte-identical to W0.
# ---------------------------------------------------------------------------
ALPHA_ACCESS = frozenset({"h1", "h2", "h3"})

# ---------------------------------------------------------------------------
# Intervention BETA: record-formation change under fixed access. The observer
# access set stays {h1,h2}. Four new record-formation events (n1-n4) and four
# new record tokens are added to the causal graph (T46 generation/propagation
# side): new propositions' support forms at holders already inside the fixed
# access set.
# ---------------------------------------------------------------------------
BETA_NODES = BASE_NODES + ["n1", "n2", "n3", "n4"]
BETA_EDGES = BASE_EDGES + [
    ("src", "n1"), ("src", "n2"), ("src", "n3"), ("src", "n4"),
    ("n1", EVAL), ("n2", EVAL), ("n3", EVAL), ("n4", EVAL),
]
BETA_RECORDS = BASE_RECORDS + [
    Record("r12", "p3", 1, "n1", "h1", 1),
    Record("r13", "p3", 1, "n2", "h2", 1),
    Record("r14", "p4", 1, "n3", "h2", 1),
    Record("r15", "p4", 0, "n4", "h1", 1),
]


def evaluate(label, nodes, edges, records, access):
    reach = reachability(nodes, edges)
    # Topological-order invariance guard: reachability is computed from the
    # edge set alone; recompute with reversed edge insertion order and assert
    # identity, per the FORMALISM invariance requirement.
    assert reach == reachability(list(reversed(nodes)), list(reversed(edges)))
    print(f"== {label} | access set = {sorted(access)} | threshold k = {K} ==")
    vector = []
    for tname, p, v in TASKS:
        prof = d1_profile(records, access, p, v, EVAL, reach, K)
        ok = reconstructible(records, access, p, v, EVAL, reach, K)
        comp = {v2: len(accessible_supporting(records, access, p, v2, EVAL, reach))
                for v2 in sorted({r.value for r in records
                                  if r.prop == p and r.value != v})}
        vector.append(1 if ok else 0)
        print(f"  {tname} ({p},{v}): D1=(A={prof[0]},R={prof[1]},"
              f"B={prof[2]},C={prof[3]}) competing_accessible_support={comp} "
              f"reconstructible={ok}")
    print(f"  achievability vector over TV = {tuple(vector)}")
    print()
    return tuple(vector)


w0 = evaluate("W0  baseline", BASE_NODES, BASE_EDGES, BASE_RECORDS, BASE_ACCESS)
wa = evaluate("W_A ALPHA (access change, records/graph fixed)",
              BASE_NODES, BASE_EDGES, BASE_RECORDS, ALPHA_ACCESS)
wb = evaluate("W_B BETA (record formation added, access fixed)",
              BETA_NODES, BETA_EDGES, BETA_RECORDS, BASE_ACCESS)

print("summary:")
print(f"  W0  = {w0}")
print(f"  W_A = {wa}")
print(f"  W_B = {wb}")
print(f"  ALPHA newly achievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wa) if y > x]}")
print(f"  ALPHA newly unachievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wa) if y < x]}")
print(f"  BETA  newly achievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wb) if y > x]}")
print(f"  BETA  newly unachievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wb) if y < x]}")
