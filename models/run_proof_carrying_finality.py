"""Run the T10 proof-carrying metastable finality laboratory."""

from __future__ import annotations

from dataclasses import asdict
import json

from models.proof_carrying_finality import (
    IdealProofSystem,
    SnowballParameters,
    adversary_sweep,
    coarse_graining_summary,
    coarse_claim,
    run_experiment,
)


def serialize(value: object) -> object:
    if hasattr(value, "__dataclass_fields__"):
        return {key: serialize(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): serialize(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialize(item) for item in value]
    return value


def main() -> None:
    global_microstate = (1, 1, 1, 1, 1, 0, 0, 0, 0)
    parameters = SnowballParameters(
        sample_size=7,
        quorum=5,
        decision_threshold=4,
        max_rounds=80,
    )
    proof_system = IdealProofSystem()
    first = proof_system.issue_leaf(
        "witness-a",
        global_microstate,
        epoch=0,
        nonce="first",
    )
    same_claim_state = (1, 1, 0, 1, 0, 1, 0, 0, 0)
    second = proof_system.issue_leaf(
        "witness-b",
        same_claim_state,
        epoch=0,
        nonce="second",
    )
    forged = proof_system.forge("forger", 1 - coarse_claim(global_microstate), 0)

    output = {
        "configuration": {
            "global_microstate": global_microstate,
            "coarse_claim": coarse_claim(global_microstate),
            "parameters": parameters,
        },
        "coarse_graining": coarse_graining_summary(),
        "proof_functionality": {
            "same_claim_distinct_microstates": coarse_claim(global_microstate)
            == coarse_claim(same_claim_state),
            "distinct_commitments": first.commitment != second.commitment,
            "first_verifies": proof_system.verify(first),
            "second_verifies": proof_system.verify(second),
            "forgery_rejected": not proof_system.verify(forged),
            "public_fields": [
                "epoch",
                "claim",
                "support_count",
                "commitment",
                "proof_id",
                "tag",
            ],
            "security_status": "ideal functionality; not a cryptographic construction",
        },
        "forged_adversary_primary": run_experiment(
            trials=300,
            global_microstate=global_microstate,
            population_size=21,
            bit_error_rate=0.20,
            adversary_fraction=0.30,
            adversary_mode="forged",
            parameters=parameters,
            seed=10_000,
        ),
        "valid_dissent_primary": run_experiment(
            trials=300,
            global_microstate=global_microstate,
            population_size=21,
            bit_error_rate=0.20,
            adversary_fraction=0.30,
            adversary_mode="valid_dissent",
            parameters=parameters,
            seed=20_000,
        ),
        "forged_adversary_sweep": adversary_sweep(
            (0.0, 0.1, 0.2, 0.3, 0.4),
            adversary_mode="forged",
            trials=150,
            seed=30_000,
        ),
        "valid_dissent_sweep": adversary_sweep(
            (0.0, 0.1, 0.2, 0.3, 0.4),
            adversary_mode="valid_dissent",
            trials=150,
            seed=40_000,
        ),
    }
    print(json.dumps(serialize(output), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
