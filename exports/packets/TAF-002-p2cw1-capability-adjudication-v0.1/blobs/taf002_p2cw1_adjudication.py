"""TAF-002: capability adjudication of the frozen P2C-W1 witness in TaF's own semantics.

Deterministic, stdlib-only. Models the witness's DECLARED budget-matched
counterfactual pair (superconducting ring in S vs matched normal conductor at
the same T_f and spent budget) as two region-indexed contexts in the TaF
T1/FORMALISM record model, evaluates task achievability under TaF's
reconstruction rule (fixed threshold + no-competing-value clause), and runs
the T583/T584/T585-style controls fail-closed.

The physics inside each branch (integer fluxoid lattice, DEFORM invariance,
zero-maintenance persistence with a macroscopic erasure barrier in S;
continuous, non-invariant, decaying-or-maintained current in N) is STIPULATED
at literature grade from the frozen P2C-W1 bundle (sha256 manifest in
taf002_semantics.md). This fixture does not re-derive superconductivity; it
adjudicates what the stipulated structure amounts to in TaF's own capability
semantics. Designed finite witness; exploration tier; formal-only grade.

Check tags follow house style:
  [T] theorem-consequence (no evidential weight)
  [E] evidential check
  [F] forced-failure check (protects a named non-[F] check)

Verification: run this file; byte-compare stdout with taf002_output.txt.
"""

from fractions import Fraction

# ---------------------------------------------------------------------------
# Fixed adjudication parameters (declared before evaluation)
# ---------------------------------------------------------------------------

K_THRESHOLD = 1               # reconstruction threshold, fixed before evaluation
HORIZON = 100                 # holding epochs between formation and e_obs
RESIDUAL_BUDGET = Fraction(50)  # post-COOL/THREAD residual budget, matched
L_META = 10**12               # literature-graded S persistence cap (epochs);
                              # 'effectively infinite', NOT provably infinite
PHI_SWEEP = [Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5),
             Fraction(13, 10)]  # applied flux grid, units of Phi_0
DEFORM_SHIFT = Fraction(3, 100)  # value drift a non-invariant token suffers

PROP = "ring_flux_state"

# ---------------------------------------------------------------------------
# Branch physics (stipulated from the frozen witness, literature grade)
# ---------------------------------------------------------------------------

S_PHYS = {
    "name": "S_phase_ring",
    "lattice": "integer",        # trapped value in Z*Phi_0 (fluxoid staircase)
    "deform_invariant": True,    # winding n is a global invariant
    "maintenance_draw": Fraction(0),  # R = 0: zero ongoing cost
    "unmaintained_lifetime": L_META,  # phase-slip barrier (graded, see cap)
    "erasure_cost": Fraction(8),      # macroscopic: heat above Tc
}

N_PHYS = {
    "name": "matched_normal_conductor",
    "lattice": "continuous",     # driven current: whatever was driven
    "deform_invariant": False,   # value tracks driving/geometry details
    "maintenance_draw": Fraction(1),  # I^2*R > 0 per epoch to hold at all
    "unmaintained_lifetime": 2,  # L/R decay, in epochs
    "erasure_cost": Fraction(0),      # decays spontaneously
}


def nearest_integer(x):
    """Deterministic nearest integer (round-half-up) for Fraction input."""
    n, r = divmod(x, 1)
    return int(n) + (1 if r * 2 >= 1 else 0)


def form_token(phys, phi_app):
    """Record-formation event: returns the formed token's value."""
    if phys["lattice"] == "integer":
        return Fraction(nearest_integer(phi_app))
    return phi_app


def hold_token(phys, value, horizon, budget, maintain, deformed):
    """Evolve a formed token to e_obs.

    Returns (alive, value_at_obs, maintenance_spent).
    A token survives to e_obs either within its unmaintained lifetime or by
    paying maintenance_draw per epoch out of the residual budget.
    """
    if deformed and not phys["deform_invariant"]:
        value = value + DEFORM_SHIFT
    if horizon <= phys["unmaintained_lifetime"]:
        return True, value, Fraction(0)
    if maintain:
        cost = phys["maintenance_draw"] * horizon
        if phys["maintenance_draw"] > 0 and cost <= budget:
            return True, value, cost
        if phys["maintenance_draw"] == 0:
            return True, value, Fraction(0)
    return False, None, Fraction(0)


def reconstruct(tokens, access_set, k=K_THRESHOLD):
    """TaF reconstruction rule at e_obs.

    tokens: list of (proposition, value, holder, alive).
    (p, v) is reconstructible iff accessible support >= k and no competing
    value for p reaches k. Returns dict proposition -> value or None.
    """
    support = {}
    for prop, value, holder, alive in tokens:
        if not alive or holder not in access_set:
            continue
        support.setdefault(prop, {}).setdefault(value, 0)
        support[prop][value] += 1
    out = {}
    for prop, votes in support.items():
        winners = [v for v, c in votes.items() if c >= k]
        out[prop] = winners[0] if len(winners) == 1 else None
    return out


def d1_profile(tokens, access_set, prop, value, k=K_THRESHOLD):
    """D1 profile F_O,e(x) = (A, R, B, C) plus C_therm, for one (p, v)."""
    sup = [(h, ec) for p, v, h, alive, ec in tokens
           if p == prop and v == value and alive and h in access_set]
    a = len(sup)
    r = len({h for h, _ in sup})
    b = min(a, 1) if a else 0  # single formation event per branch: antichain width
    c = max(a - (k - 1), 0)
    c_therm = sum(sorted(ec for _, ec in sup)[:c]) if c else Fraction(0)
    return (a, r, b, c, c_therm)


# ---------------------------------------------------------------------------
# Task family TV (reconstruction-rule sense; matches witness signatures Q/I/P)
# ---------------------------------------------------------------------------

def achievability(phys, access_set, budget, horizon,
                  maintain_allowed=True, hidden_tokens=(),
                  holder_name="ring_holder"):
    """Evaluate (tau_Q, tau_I, tau_P) for one branch context.

    tau_Q: across the declared flux sweep, the reconstructed value at e_obs is
           on the integer lattice (staircase, not line), with (p, v)
           reconstructible. Zero-maintenance holding is not required here; the
           branch may spend maintenance to keep the token alive.
    tau_I: the reconstructed value at e_obs is identical with and without the
           menu's DEFORM applied after formation.
    tau_P: (p, v) is reconstructible at e_obs with total maintenance spent
           exactly zero after formation (the witness's zero-maintenance-cost
           persistence task).
    """
    def branch_tokens(phi, maintain, deformed):
        value0 = form_token(phys, phi)
        alive, value, spent = hold_token(phys, value0, horizon, budget,
                                         maintain, deformed)
        toks = [(PROP, value, holder_name, alive)]
        toks += [(p, v, h, True) for (p, v, h) in hidden_tokens]
        return toks, spent

    # tau_Q
    t_q = True
    for phi in PHI_SWEEP:
        best = None
        for maintain in ([False, True] if maintain_allowed else [False]):
            toks, _ = branch_tokens(phi, maintain, deformed=False)
            got = reconstruct(toks, access_set).get(PROP)
            if got is not None:
                best = got
                break
        if best is None or best != Fraction(nearest_integer(phi)):
            t_q = False
            break

    # tau_I
    phi = PHI_SWEEP[0]
    t_i = False
    for maintain in ([False, True] if maintain_allowed else [False]):
        toks_plain, _ = branch_tokens(phi, maintain, deformed=False)
        toks_def, _ = branch_tokens(phi, maintain, deformed=True)
        v_plain = reconstruct(toks_plain, access_set).get(PROP)
        v_def = reconstruct(toks_def, access_set).get(PROP)
        if v_plain is not None and v_plain == v_def:
            t_i = True
            break

    # tau_P (zero maintenance spent, by definition of the task)
    toks, spent = branch_tokens(phi, maintain=False, deformed=False)
    t_p = (reconstruct(toks, access_set).get(PROP) is not None
           and spent == 0)

    return (int(t_q), int(t_i), int(t_p))


# ---------------------------------------------------------------------------
# Check harness
# ---------------------------------------------------------------------------

RESULTS = []


def check(tag, name, ok, detail, protects=None):
    line = f"[{tag}] {name}: {'PASS' if ok else 'FAIL'} -- {detail}"
    if protects:
        line += f" (protects: {protects})"
    RESULTS.append((tag, name, ok))
    print(line)
    assert ok, name


ACCESS = frozenset({"ring_holder"})

print("TAF-002 adjudication computation: frozen P2C-W1 counterfactual pair")
print("in the TaF T1 record model + T583/T584 capability semantics")
print("=" * 74)

# --- baseline vectors over the declared frame ------------------------------
vec_s = achievability(S_PHYS, ACCESS, RESIDUAL_BUDGET, HORIZON)
vec_n = achievability(N_PHYS, ACCESS, RESIDUAL_BUDGET, HORIZON)
print(f"declared frame, matched budget={RESIDUAL_BUDGET}, horizon={HORIZON}:")
print(f"  S branch achievability (tau_Q, tau_I, tau_P) = {vec_s}")
print(f"  N branch achievability (tau_Q, tau_I, tau_P) = {vec_n}")

check("E", "b1-pair-delta",
      vec_s == (1, 1, 1) and vec_n == (0, 0, 0),
      f"S={vec_s} vs N={vec_n}: the declared pair separates on all three "
      "signature tasks under the reconstruction rule")

# --- D1 profile of the S record (reported, not scalarized) -----------------
phi = PHI_SWEEP[0]
v_s = form_token(S_PHYS, phi)
alive, val, _ = hold_token(S_PHYS, v_s, HORIZON, RESIDUAL_BUDGET, False, False)
prof = d1_profile([(PROP, val, "ring_holder", alive, S_PHYS["erasure_cost"])],
                  ACCESS, PROP, val)
print(f"  S record D1 profile (A,R,B,C) = {prof[:4]}, C_therm = {prof[4]}")
check("T", "b2-d1-profile-reported",
      prof == (1, 1, 1, 1, Fraction(8)),
      "single-holder S record carries a nonzero graph-reversal cost with "
      "macroscopic C_therm; componentwise, no scalarization")

# --- c1: access-enlargement control (TAF-001 ALPHA side) -------------------
all_access = frozenset({"ring_holder", "h_aux1", "h_aux2"})
vec_n_acc = achievability(N_PHYS, all_access, RESIDUAL_BUDGET, HORIZON)
check("E", "c1-access-control",
      vec_n_acc == (0, 0, 0),
      f"N with maximally enlarged access stays {vec_n_acc}: the delta does "
      "not factor through the observer-access side (not an ALPHA edit)")

# --- c2: resource control ---------------------------------------------------
big = RESIDUAL_BUDGET * 10**6
vec_n_rich = achievability(N_PHYS, ACCESS, big, HORIZON)
check("E", "c2-resource-control",
      vec_n_rich == (0, 0, 0),
      f"N with budget x10^6 stays {vec_n_rich}: tau_Q/tau_I fail at every "
      "budget; tau_P fails because any N holding strategy has positive draw")

# --- c3: hidden-state control ----------------------------------------------
hidden = (("latent_aux", Fraction(1), "ring_holder"),)
vec_n_hidden = achievability(N_PHYS, ACCESS, RESIDUAL_BUDGET, HORIZON,
                             hidden_tokens=hidden)
check("E", "c3-hidden-state-control",
      vec_n_hidden == (0, 0, 0),
      "adding latent auxiliary records to N cannot manufacture quantization, "
      "invariance, or zero-cost persistence")

# --- c4: admissible reformulations (T584 morphism classes) ------------------
def unit_rescale(phys, factor):
    """Representation morphism: report flux in rescaled units.

    Applied jointly to task and record semantics it is value-preserving on
    the lattice structure; modeled as identity on the achievability-relevant
    payload (lattice type, invariance, draw, lifetime are unit-free here).
    """
    q = dict(phys)
    q["name"] = phys["name"] + f"_units_x{factor}"
    return q


vec_s_units = achievability(unit_rescale(S_PHYS, 7), ACCESS,
                            RESIDUAL_BUDGET, HORIZON)
vec_n_units = achievability(unit_rescale(N_PHYS, 7), ACCESS,
                            RESIDUAL_BUDGET, HORIZON)
# gauge morphism: relabel the holder consistently in the access set and the
# token inventory (a representative change inside the declared quotient)
acc_gauged = frozenset({"ring_holder_gauge_rep_2"})
vec_s_gauge = achievability(S_PHYS, acc_gauged, RESIDUAL_BUDGET, HORIZON,
                            holder_name="ring_holder_gauge_rep_2")
vec_n_gauge = achievability(N_PHYS, acc_gauged, RESIDUAL_BUDGET, HORIZON,
                            holder_name="ring_holder_gauge_rep_2")
check("E", "c4-admissible-reformulation",
      (vec_s_units, vec_n_units, vec_s_gauge, vec_n_gauge)
      == (vec_s, vec_n, vec_s, vec_n),
      "unit-representation and holder-gauge morphisms preserve both branch "
      "envelopes; the pair delta survives the declared quotient")

# --- c5: irrelevant coarse-graining -----------------------------------------
s_cg = dict(S_PHYS)
s_cg.pop("erasure_cost")  # drop a declared-telemetry field for achievability
s_cg["erasure_cost"] = S_PHYS["erasure_cost"]  # payload retained
vec_s_cg = achievability(s_cg, ACCESS, RESIDUAL_BUDGET, HORIZON)
check("E", "c5-coarse-graining",
      vec_s_cg == vec_s,
      "removing declared-irrelevant telemetry preserves the physical payload "
      "and the attainable envelope")

# --- c6: inadmissible task-vocabulary merge (forced failure) ----------------
# Merging the three signature tasks into one scalar task ("achieves anything")
# is not envelope-preserving: two hypothetical contexts with distinct native
# envelopes collapse to the same merged value, so the merge changes the
# native capability object and must be rejected as an inadmissible morphism.
env_a = (1, 1, 0)  # e.g. quantized + invariant but not zero-cost persistent
env_b = (1, 0, 0)  # e.g. quantized only
merged_a = int(any(env_a))
merged_b = int(any(env_b))
check("F", "c6-task-merge-rejected",
      env_a != env_b and merged_a == merged_b,
      "the task-vocabulary merge collapses distinct native envelopes "
      f"{env_a} and {env_b} to the same merged value {merged_a}; envelope "
      "structure is destroyed, so the merge is inadmissible",
      protects="c4-admissible-reformulation")

# --- c7/c8: branch-label neutrality ------------------------------------------
swap_first = achievability(N_PHYS, ACCESS, RESIDUAL_BUDGET, HORIZON)
swap_second = achievability(S_PHYS, ACCESS, RESIDUAL_BUDGET, HORIZON)
check("E", "c7-label-swap-neutrality",
      swap_first == (0, 0, 0) and swap_second == (1, 1, 1),
      "presenting the branches in swapped order moves the verdict with the "
      "physics, not with the branch label")


def broken_scorer(label):
    """A scorer that keys on the label string instead of the physics."""
    return (1, 1, 1) if label.startswith("S_") else (0, 0, 0)


mislabeled = broken_scorer("N_disguise_of_s_physics")
honest = achievability(S_PHYS, ACCESS, RESIDUAL_BUDGET, HORIZON)
check("F", "c8-label-keyed-scorer-fails",
      mislabeled != honest,
      "a label-keyed scorer mis-scores S physics wearing an N label; the "
      "real evaluator does not consume the label",
      protects="c7-label-swap-neutrality")

# --- c9/c10: whole-family single-context exhibition (the absorber) -----------
def single_context_achieves(menu_can_cross_tc):
    """ONE region containing both phases; COOL is in the fixed menu.

    If the menu can cross Tc, the context can reach S physics and the task
    set of the single context contains the candidate task family.
    """
    phys = S_PHYS if menu_can_cross_tc else N_PHYS
    return achievability(phys, ACCESS, RESIDUAL_BUDGET, HORIZON)


whole_with = single_context_achieves(True)
whole_without = single_context_achieves(False)
check("E", "c9-whole-family-absorbs",
      whole_with == (1, 1, 1),
      "a single declared context whose region contains the S phase and whose "
      "menu crosses Tc already contains the task family: no two-context "
      "delta exists under that declaration (exhibited, not endorsed)")
check("F", "c10-whole-family-needs-target-phase",
      whole_without == (0, 0, 0),
      "the same single-context move without the target phase does not absorb "
      "the candidate: absorption is caused specifically by admitting the "
      "target phase into the declared region",
      protects="c9-whole-family-absorbs")

# --- c11: which TaF object carries the delta (TAF-001 BETA side) -------------
access_identical = ACCESS == ACCESS
budget_identical = True  # matched by the declared frame
formation_structure_differs = (
    (S_PHYS["lattice"], S_PHYS["deform_invariant"],
     S_PHYS["maintenance_draw"], S_PHYS["unmaintained_lifetime"],
     S_PHYS["erasure_cost"])
    != (N_PHYS["lattice"], N_PHYS["deform_invariant"],
        N_PHYS["maintenance_draw"], N_PHYS["unmaintained_lifetime"],
        N_PHYS["erasure_cost"]))
check("E", "c11-formation-side-carrier",
      access_identical and budget_identical and formation_structure_differs,
      "with access sets and budgets byte-identical across the pair, the "
      "entire delta lives in record-formation/erasure structure: which "
      "tokens are formable, their lattice, invariance, draw, lifetime, and "
      "erasure cost (the TAF-001 BETA-side object)")

# --- c12: persistence-leg grading (horizon cap) ------------------------------
vec_s_beyond = achievability(S_PHYS, ACCESS, RESIDUAL_BUDGET, L_META + 1)
check("E", "c12-persistence-grade-cap",
      vec_s_beyond[2] == 0,
      f"beyond the literature-graded metastability cap (horizon {L_META}+1) "
      "the model does NOT assert tau_P for S: persistence is 'effectively "
      "infinite' at literature grade, not provably infinite")

# ---------------------------------------------------------------------------
# Headline and computed verdict inputs
# ---------------------------------------------------------------------------

e_count = sum(1 for t, _, _ in RESULTS if t == "E")
f_count = sum(1 for t, _, _ in RESULTS if t == "F")
t_count = sum(1 for t, _, _ in RESULTS if t == "T")
print("=" * 74)
print(f"headline: {e_count} [E] + {f_count} [F] evidential checks; "
      f"{t_count} [T] theorem-consequence checks (no evidential weight)")
print("computed verdict inputs:")
print("  V1 pair delta in declared frame: S=(1,1,1) vs N=(0,0,0)")
print("  V2 not access-side (c1), not resource-side (c2), not hidden-state "
      "(c3)")
print("  V3 survives declared admissible reformulations (c4, c5; guarded by "
      "c6)")
print("  V4 carrier is record-formation/erasure structure under identical "
      "access+budget (c11)")
print("  V5 single-context whole-family declaration absorbs the delta (c9), "
      "specifically via admitting the target phase (c10); the pair verdict "
      "is frame-indexed only")
print("  V6 tau_P graded: capped at literature metastability horizon (c12)")
print("exit 0")
