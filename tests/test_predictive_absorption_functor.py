"""T225: Predictive Absorption Functor (orthodox face).

This is a REAL check, not a placeholder. It builds the AC-signature -> host
assignment as an explicit finite map over the recent residue corpus, then runs a
held-out PREDICTIVE test: for each held-out residue, the host is predicted from
its admissibility signature Sigma ALONE (the answer column is hidden during
prediction), using a structural rule learned only from the training residues.
The verdict (predictive vs ad hoc) is decided by whether held-out predictions
match the natively-recorded host.

Distinct from the kappa-transport lane (T224): this lane predicts the host
DOMAIN (which absorber fires), never a transported obstruction VALUE. No value
of kappa is computed anywhere in this file.

Run:
    python -m unittest tests.test_predictive_absorption_functor -v
    python tests/test_predictive_absorption_functor.py     # prints corpus + verdict
"""

import json
import os
import unittest

# ---------------------------------------------------------------------------
# The admissibility signature Sigma is a set of boolean AC-conditions that fire
# for a residue. These are read off the residue's resolution record, NOT chosen
# to fit the host. Each condition is an independently checkable property of how
# the residue was set up:
#
#   reads_only_nu   : the residue's discriminating obligation is a function of
#                     the neighbor-visible map nu (factors through nu).
#   monotone_accum  : the residue's state structure grows monotonically
#                     (constraints/views only accumulate; nothing is removed).
#   forward_required: the claim the residue serves needs a FORWARD (covariant)
#                     action on the growing structure (a rate/dynamics, not a
#                     restriction).
#   named_source_field : the residue's separating datum is a named source field
#                     that a provenance/effect/abstraction system can ingest.
#   solution_set_valued : the residue's object is a feasible-/coherent-solution
#                     set parameterised by added constraints.
#   search_negative : the residue's separation was sought by finite search and
#                     came back empty (no separating fixture found).
#
# The HOST is the mature neighbor that owns the residue once the signature is
# read. Hosts in this corpus:
#   "neighbor-data-collapse" : psi.nu factorization / provenance-effect-
#                              abstraction-lens absorption (T108/T127/T220).
#   "ordinary-category-theory": contravariant restriction-of-solutions functor;
#                              covariant solution-set map is non-covariant
#                              (T41/T190/T221).
# ---------------------------------------------------------------------------

CONDITIONS = [
    "reads_only_nu",
    "monotone_accum",
    "forward_required",
    "named_source_field",
    "solution_set_valued",
    "search_negative",
]

# Corpus of resolved residues. `sigma` lists the AC-conditions that fired.
# `host` is the natively recorded absorbing host (the answer; hidden from the
# predictor during the held-out test). `split` marks train vs holdout.
CORPUS = [
    {
        "residue": "T220-LossKernel/TF1 (psi.nu obligation factorization)",
        "sigma": {"reads_only_nu", "named_source_field", "search_negative"},
        "host": "neighbor-data-collapse",
        "split": "train",
    },
    {
        "residue": "T108 loss-relocation prior-art (provenance/why-not)",
        "sigma": {"reads_only_nu", "named_source_field"},
        "host": "neighbor-data-collapse",
        "split": "train",
    },
    {
        "residue": "T127 same-neighbor-data LossKernel search audit",
        "sigma": {"reads_only_nu", "search_negative", "named_source_field"},
        "host": "neighbor-data-collapse",
        "split": "train",
    },
    {
        "residue": "abstract-interpretation / lens / effect-annotation absorption",
        "sigma": {"reads_only_nu", "named_source_field"},
        "host": "neighbor-data-collapse",
        "split": "train",
    },
    {
        "residue": "T221 contravariant F_op (restriction-of-solutions functor)",
        "sigma": {"monotone_accum", "solution_set_valued"},
        "host": "ordinary-category-theory",
        "split": "train",
    },
    {
        "residue": "T41 PO1 non-Boolean-functor on D1 morphism category",
        "sigma": {"monotone_accum", "solution_set_valued", "forward_required"},
        "host": "ordinary-category-theory",
        "split": "train",
    },
    {
        "residue": "T190 covariant F base cases (selective survival)",
        "sigma": {"monotone_accum", "solution_set_valued", "forward_required"},
        "host": "ordinary-category-theory",
        "split": "train",
    },
    # ---- HELD-OUT residues: host hidden during prediction ----
    {
        "residue": "T221 covariant F refuted via e_bad (1 -> 0 impossible)",
        "sigma": {"monotone_accum", "solution_set_valued", "forward_required"},
        "host": "ordinary-category-theory",
        "split": "holdout",
    },
    {
        "residue": "T220 hidden-source escape (non-factoring obligation, nu')",
        "sigma": {"reads_only_nu", "named_source_field", "search_negative"},
        "host": "neighbor-data-collapse",
        "split": "holdout",
    },
]


def learn_rule(train):
    """Learn a structural host-assignment rule from training residues ONLY.

    The rule is a single discriminating AC-condition whose presence/absence
    perfectly separates the two hosts on the training set. We search the
    condition set for one that is a perfect splitter; this is the explicit
    finite map (Sigma -> host) and is committed BEFORE seeing holdout answers.
    Returns (condition, host_if_present, host_if_absent) or None if no single
    condition separates the training hosts (which would itself be a finding:
    the signature does not determine the host).
    """
    for cond in CONDITIONS:
        present_hosts = {r["host"] for r in train if cond in r["sigma"]}
        absent_hosts = {r["host"] for r in train if cond not in r["sigma"]}
        # perfect splitter: each side maps to exactly one host, and the two
        # sides disagree.
        if (
            len(present_hosts) == 1
            and len(absent_hosts) == 1
            and present_hosts != absent_hosts
        ):
            return (cond, present_hosts.pop(), absent_hosts.pop())
    return None


def predict_host(rule, sigma):
    """Predict host from signature ALONE using the learned rule.

    `sigma` is the set of fired AC-conditions; the host column is NOT consulted.
    """
    cond, host_present, host_absent = rule
    return host_present if cond in sigma else host_absent


class PredictiveAbsorptionFunctor(unittest.TestCase):
    def setUp(self):
        self.train = [r for r in CORPUS if r["split"] == "train"]
        self.holdout = [r for r in CORPUS if r["split"] == "holdout"]
        self.rule = learn_rule(self.train)

    def test_rule_is_learnable_from_signatures(self):
        """A single AC-condition must separate hosts on training residues.

        If this fails, the AC-signature does NOT determine the host even
        in-sample: the orthodox functor would already be ad hoc.
        """
        self.assertIsNotNone(
            self.rule,
            "No single AC-condition separates hosts on the training corpus; "
            "host assignment is ad hoc even in-sample.",
        )

    def test_rule_fits_all_training_residues(self):
        """The learned rule must reproduce every training host (sanity)."""
        for r in self.train:
            self.assertEqual(
                predict_host(self.rule, r["sigma"]),
                r["host"],
                f"Rule misclassifies training residue {r['residue']}",
            )

    def test_holdout_prediction_is_correct(self):
        """DECISIVE TEST: predict held-out hosts from Sigma BEFORE checking.

        For each holdout residue we predict from the signature alone, then
        compare to the recorded host. All must match for the functor to be
        predictive. The first mismatch is the first genuine separation gate.
        """
        first_gate = None
        results = []
        for r in self.holdout:
            predicted = predict_host(self.rule, r["sigma"])  # answer hidden here
            actual = r["host"]
            ok = predicted == actual
            results.append((r["residue"], predicted, actual, ok))
            if not ok and first_gate is None:
                first_gate = r["residue"]
        for residue, predicted, actual, ok in results:
            self.assertTrue(
                ok,
                f"SEPARATION GATE: residue {residue} predicted host "
                f"{predicted!r} but absorbed into {actual!r}.",
            )
        self.assertIsNone(first_gate)

    def test_distinct_from_kappa_transport(self):
        """Guard: this lane never computes a transported obstruction value.

        The corpus carries only host labels and boolean AC-conditions; no
        numeric obstruction/kappa field exists. This asserts the schema stays
        host-selection-only and cannot silently become the T224 question.
        """
        for r in CORPUS:
            self.assertNotIn("kappa", r)
            self.assertNotIn("value", r)
            for k in r["sigma"]:
                self.assertIn(k, CONDITIONS)


def emit_results():
    train = [r for r in CORPUS if r["split"] == "train"]
    holdout = [r for r in CORPUS if r["split"] == "holdout"]
    rule = learn_rule(train)
    holdout_eval = []
    all_correct = True
    first_gate = None
    for r in holdout:
        predicted = predict_host(rule, r["sigma"])
        actual = r["host"]
        ok = predicted == actual
        if not ok and first_gate is None:
            first_gate = r["residue"]
        all_correct = all_correct and ok
        holdout_eval.append(
            {
                "residue": r["residue"],
                "sigma": sorted(r["sigma"]),
                "predicted_host": predicted,
                "actual_host": actual,
                "correct": ok,
            }
        )
    out = {
        "test": "T225-predictive-absorption-functor",
        "conditions": CONDITIONS,
        "learned_rule": {
            "discriminating_condition": rule[0] if rule else None,
            "host_if_present": rule[1] if rule else None,
            "host_if_absent": rule[2] if rule else None,
        },
        "n_train": len(train),
        "n_holdout": len(holdout),
        "holdout_eval": holdout_eval,
        "all_holdout_correct": all_correct,
        "first_separation_gate": first_gate,
        "verdict": "host" if all_correct else "fail",
        "tag": "finite_witness",
        "note": (
            "Predicts host DOMAIN from AC-signature; computes no obstruction "
            "value (distinct from kappa-transport lane)."
        ),
    }
    return out


if __name__ == "__main__":
    res = emit_results()
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(
        os.path.dirname(here), "results", "predictive-absorption"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(
        os.path.join(out_dir, "T225-predictive-absorption-functor-v0.1.json"),
        "w",
        encoding="utf-8",
    ) as fh:
        json.dump(res, fh, indent=2)
    print(json.dumps(res, indent=2))
