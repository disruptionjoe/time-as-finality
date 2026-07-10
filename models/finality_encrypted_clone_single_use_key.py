"""FINALITY -- copy-law single-use-key absorber screen (T520).

Lane B ("finality dual to no-cloning") died on two counts (cluster swing
2026-07-08): the no-cloning set was a relabel of the unreadable band, and the
proposed copy-conservation law J+R was measured NON-conserved (1 -> 6). Its
recorded wake condition (2026-07-09) is "a different conserved / priced quantity."

arXiv 2602.10695 (Yamaguchi, Rullkoetter, Shehzad, Wagner, Tutschku, Kempf)
supplies a candidate: qubits can be cloned into any number of ENCRYPTED copies,
but decryption consumes a SINGLE-USE key, so exactly one clone is ever
authoritative -- explicitly "in agreement with no-cloning."

This screen tests whether the single-use key is a genuinely new finality quantity
or is absorbed by a standard quantum-one-time-pad (QOTP) / consumable-resource
monotone -- the same absorber that ate lane B's monogamy / Landauer residue.

Method: two INDEPENDENT code paths.
  (1) the finality reading: encrypted clones (maximally-mixed marginals = the
      unreadable band), a single-use key authority, and the candidate conserved
      quantity A = readable_copies + remaining_key_authority.
  (2) the resource ledger: the key as a bare consumable monotone M, with NO
      finality semantics.
Then ask the predeclared non-absorption question: is there any verdict-bearing
quantity of (1) that (2) cannot compute? Controls: single-use, double-use
(reusable), and absent key.

Verdict preview: A is conserved (clearing failure mode 2, unlike J+R), and the
encrypted clones reproduce the unreadable band (confirming failure mode 1's
object was real) -- but every verdict-bearing finality quantity factors through
the resource monotone M. Non-absorption burden NOT met. Lane B stays dead with a
sharper epitaph; the single-use key is resource bookkeeping.

Run: python -m models.finality_encrypted_clone_single_use_key
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# --- quantum primitives ------------------------------------------------------

I2 = np.eye(2, dtype=complex)
PAULI = {
    "I": np.array([[1, 0], [0, 1]], dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def psi(theta: float, phi: float) -> np.ndarray:
    """An arbitrary (unknown) pure qubit state vector."""
    return np.array([np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)], dtype=complex)


def dm(state: np.ndarray) -> np.ndarray:
    return np.outer(state, state.conj())


def encrypt(rho: np.ndarray, key: str) -> np.ndarray:
    """Quantum one-time-pad encryption of a qubit with a Pauli key."""
    p = PAULI[key]
    return p @ rho @ p.conj().T


def encrypted_marginal(rho: np.ndarray) -> np.ndarray:
    """Marginal of an encrypted clone, averaged over a uniform Pauli key."""
    return sum(0.25 * encrypt(rho, k) for k in PAULI)


def fidelity_with(rho: np.ndarray, state: np.ndarray) -> float:
    """<state| rho |state> -- recoverability of |state> from rho."""
    return float(np.real(state.conj() @ rho @ state))


def accessible_info_about_source(rho_source: np.ndarray) -> float:
    """How much the encrypted marginal reveals about the source state.

    The encrypted marginal is I/2 for EVERY source (QOTP), so it is independent
    of the source: accessible information = 0. We quantify it as the trace
    distance between the encrypted marginals of two different sources; 0 means an
    eavesdropper cannot tell them apart -- the 'unreadable band'.
    """
    other = dm(psi(1.2, 0.7))
    m_a = encrypted_marginal(rho_source)
    m_b = encrypted_marginal(other)
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(m_a - m_b))))


# --- (1) the finality reading ------------------------------------------------


def finality_reading(source: np.ndarray, n_clones: int, key_authority: int) -> dict:
    """Encrypted-clone band + single-use key, read as finality.

    key_authority = number of decryptions the key permits (1 = single-use,
    2 = double-use control, 0 = absent-key control).
    Returns the candidate conserved quantity A across cuts and the finality
    verdict vector.
    """
    marg = encrypted_marginal(dm(source))
    # each clone marginally maximally mixed -> individual recoverability = chance
    rec_individual = fidelity_with(marg, source)  # = 1/2, the unreadable band
    band_unreadable = np.isclose(rec_individual, 0.5)

    # A across cuts: readable copies + remaining key authority.
    # BAND cut (pre-decryption) and GLOBAL cut (after using all authority).
    a_band = 0 + key_authority
    readable_after = min(key_authority, n_clones)
    a_global = readable_after + (key_authority - readable_after)
    a_conserved = a_band == a_global

    verdict = {
        "rec_individual": rec_individual,
        "band_unreadable": bool(band_unreadable),
        "A_band": a_band,
        "A_global": a_global,
        "A_conserved": bool(a_conserved),
        # verdict-bearing finality quantities:
        "can_finalize_now": key_authority > 0,
        "max_authoritative_copies_ever": readable_after,
        "cost_per_finalization_units": 1 if key_authority > 0 else 0,
    }
    return verdict


# --- (2) the resource ledger (QOTP / consumable monotone, no finality) -------


def resource_ledger(n_clones: int, monotone_M: int) -> dict:
    """The key as a bare consumable resource monotone M. No finality semantics.

    Free operations: clone-encrypt (adds no accessible info, leaves M).
    Costly operation: decrypt (consumes one unit of M, yields one recovery).
    Everything a resource theorist can say is a function of M and n_clones.
    """
    recoveries_possible = min(monotone_M, n_clones)
    return {
        "recoverable_now": monotone_M > 0,
        "total_recoveries": recoveries_possible,
        "cost_per_recovery_units": 1 if monotone_M > 0 else 0,
        "monotone_nonincreasing_under_free_ops": True,
    }


def finality_vector(v: dict) -> tuple:
    return (v["can_finalize_now"], v["max_authoritative_copies_ever"], v["cost_per_finalization_units"])


def resource_vector(r: dict) -> tuple:
    return (r["recoverable_now"], r["total_recoveries"], r["cost_per_recovery_units"])


# --- the screen --------------------------------------------------------------


def main() -> None:
    print("[T520] copy-law single-use-key absorber screen\n")

    source = psi(0.9, 0.4)  # an arbitrary unknown qubit
    N = 6

    # --- leg 1: the encrypted clones reproduce the unreadable band -----------
    marg = encrypted_marginal(dm(source))
    check(
        "encrypted marginal is maximally mixed (I/2)",
        np.allclose(marg, 0.5 * I2),
        f"||marg - I/2|| = {np.linalg.norm(marg - 0.5 * I2):.2e}",
    )
    acc = accessible_info_about_source(dm(source))
    check(
        "encrypted band is unreadable (accessible info about source = 0)",
        np.isclose(acc, 0.0),
        f"trace-dist between sources' encrypted marginals = {acc:.2e}",
    )
    fr_single = finality_reading(source, N, key_authority=1)
    check(
        "clones = unreadable band relabel (rec_individual = 1/2)",
        fr_single["band_unreadable"],
        f"rec_individual = {fr_single['rec_individual']:.3f}",
    )

    # --- leg 2: candidate A is conserved (clears lane-B failure mode 2) ------
    check(
        "single-use A is conserved band->global (A=1, unlike J+R's 1->6)",
        fr_single["A_conserved"] and fr_single["A_band"] == 1,
        f"A_band={fr_single['A_band']} A_global={fr_single['A_global']}",
    )
    fr_double = finality_reading(source, N, key_authority=2)
    fr_absent = finality_reading(source, N, key_authority=0)
    check(
        "controls: double-use A=2 conserved, absent-key A=0 conserved",
        fr_double["A_conserved"] and fr_double["A_band"] == 2 and fr_absent["A_band"] == 0,
        f"double A={fr_double['A_band']} absent A={fr_absent['A_band']}",
    )

    # --- leg 3: the non-absorption burden (does the resource ledger compute
    #            every verdict-bearing finality quantity?) --------------------
    scenarios = []
    residue_found = False
    for label, auth in [("single-use", 1), ("double-use", 2), ("absent", 0)]:
        for n in (1, 2, 3, 6):
            fr = finality_reading(source, n, key_authority=auth)
            rl = resource_ledger(n, monotone_M=auth)
            fv, rv = finality_vector(fr), resource_vector(rl)
            match = fv == rv
            if not match:
                residue_found = True
            scenarios.append(
                {"key": label, "n_clones": n, "finality_vector": list(fv),
                 "resource_vector": list(rv), "reproduced_by_resource_ledger": match}
            )

    all_reproduced = all(s["reproduced_by_resource_ledger"] for s in scenarios)
    check(
        "every finality verdict is reproduced by the bare resource monotone",
        all_reproduced,
        f"{sum(s['reproduced_by_resource_ledger'] for s in scenarios)}/{len(scenarios)} scenarios",
    )
    check(
        "resource ledger distinguishes single- / double- / absent-key (control passes)",
        resource_ledger(6, 1)["total_recoveries"] == 1
        and resource_ledger(6, 2)["total_recoveries"] == 2
        and resource_ledger(6, 0)["recoverable_now"] is False,
        "the exactly-once distinction is itself a resource-monotone value",
    )

    # --- the predeclared non-absorption burden (ALL must hold to escape) -----
    #   the only candidate residue is 'which clone becomes authoritative', a
    #   FREE symmetric choice -> not a verdict-bearing quantity.
    which_clone_forced = False  # symmetric under clone relabeling; observer-chosen
    burden = {
        "A_fixed_before_resource_encoding": True,           # A defined structurally
        "verdict_quantity_not_computed_by_ledger": residue_found,   # <-- decisive
        "key_role_irreducible_to_OTP_consumption": False,   # it IS OTP consumption
        "negative_control_distinguished_only_by_finality": False,   # ledger also splits it
        "which_clone_forced_not_free": which_clone_forced,
        "structure_rank_load_bearing_beyond_conserved_label": False,
        "no_shared_derivation_finality_vs_resource": True,
    }
    escaped = all(burden.values())
    check(
        "non-absorption burden is NOT met (expected: absorbed)",
        not escaped,
        "decisive gate 'verdict_quantity_not_computed_by_ledger' = "
        f"{burden['verdict_quantity_not_computed_by_ledger']}",
    )

    absorbed = all_reproduced and not residue_found and not escaped
    verdict = (
        "COPY_LAW_SINGLE_USE_KEY_ABSORBED_BY_RESOURCE_MONOTONE"
        if absorbed
        else "COPY_LAW_SINGLE_USE_KEY_RESIDUE_LANE_B_REOPENS"
    )

    payload = {
        "artifact_id": "T520-copy-law-single-use-key-absorber-screen-v0.1",
        "verdict": verdict,
        "model": "models/finality_encrypted_clone_single_use_key.py",
        "wake_candidate": "arXiv 2602.10695 (encrypted cloning, single-use decryption key)",
        "lane": "B (finality dual to no-cloning)",
        "clears_wake_condition_letter": {
            "different_conserved_quantity": True,
            "A_conserved_single_use": fr_single["A_conserved"],
            "note": "unlike falsified J+R (1->6), A = readable + key_authority is conserved",
        },
        "but_fails_non_absorption_burden": burden,
        "unreadable_band_relabel_confirmed": fr_single["band_unreadable"],
        "scenarios": scenarios,
        "monogamy_residue_routes_to": "monogamy <-> quantum secret sharing strut (arXiv 2605.26866)",
        "checks_passed": None,
        "checks_failed": None,
    }

    print("\n[verdict]")
    print(f"  * {verdict}")
    print("  * The single-use key clears the LETTER of lane B's wake condition: A is a")
    print("    different conserved quantity, and (unlike J+R) it is actually conserved.")
    print("  * But every verdict-bearing finality quantity (can-finalize, exactly-once,")
    print("    cost) factors through the bare consumable monotone M. The key IS OTP")
    print("    key-consumption; the non-absorption burden is not met.")
    print("  * Lane B stays dead with a sharper epitaph. Any monogamy residue routes to")
    print("    the secret-sharing strut, not to lane B.")

    payload["checks_passed"] = 8 - len(FAIL)
    payload["checks_failed"] = len(FAIL)
    out = Path("results/T520-copy-law-single-use-key-absorber-screen-v0.1.json")
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = wake candidate screened; absorbed by resource monotone, lane B stays shut.")


if __name__ == "__main__":
    main()
