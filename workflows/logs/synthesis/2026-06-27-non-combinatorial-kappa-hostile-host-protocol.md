---
document_type: synthesis_protocol
queue_item: 3
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# Non-Combinatorial Kappa Hostile Host Protocol

## Scope

This note completes queue item 3 from
`workflows/logs/best-next-move/2026-06-27-next-10-research-orchestration.md`.
It is a protocol artifact only. It does not update `CLAIM-LEDGER.md`,
`ROADMAP.md`, tests, results, code, or open-problem files.

The target is not another matched kappa fixture. The target is a hostile
non-combinatorial host where the native obstruction is computed in its own units
before transport, and where the source kappa, target native value, and synthetic
`nu` cover are not all assigned the same integer by construction.

## Grounding Readout

Read surfaces used:

- `ROADMAP.md` T239 entry: T239 left the next edge as a non-combinatorial
  value-gap or rate-distortion native genre after the Helly/quorum-intersection
  genre.
- `CLAIM-LEDGER.md` 2026-06-26 correction: the kappa line is a finite
  multi-domain re-encoding catalogue, not prediction, because paired fixtures
  wrote the same integer `k` into the source cover, native witness, and synthetic
  `nu` cover.
- `open-problems/typed-loss-transport-test.md`: a genuine transport test must
  compute source kappa, map to an unrelated host, predict before native
  measurement, then compare without per-domain retuning.
- T239/T244 artifacts: T244 supplies a useful value-gap positive fixture, but the
  2026-06-26 correction makes it insufficient as a hostile host because its
  native rank is still synchronized with fixture `k`.
- `COMPLEXITY-LEDGER.md`: any future executable artifact may say
  `finite_witness` or `poly_decider` only when the declared finite classifier
  earns it; no hardness, scaling, or general theorem language is licensed.

## Hostile Host Definition

Use a finite POMDP/value-of-information or rate-distortion host `B` with native
units independent of kappa:

- `Delta_i`: native value gap for block `i`, measured in reward units, expected
  loss units, bits, or nats.
- `epsilon`: pre-registered floor in the same native units.
- `V_B = (Delta_1, ..., Delta_m)`: the native value vector.
- `rank_B_epsilon = count independent blocks with Delta_i > epsilon`: an
  optional integer summary, derived after the native comparison is defined.

The native comparison is `V_B` first, not `rank_B_epsilon` first. Two hosts can
therefore have the same integer rank but different native values, or the same
visible data but different native values around `epsilon`.

## Protocol

1. Freeze a target-host panel before source pairing.
   - Declare host parameters, native units, `epsilon`, block independence, and
     how `Delta_i` is computed.
   - Include at least six hosts: clear positives, at-floor cases, below-floor
     cases, shared-block multiplicity, same-visible-data non-splits, and
     deliberately mismatched source/target pairs.
   - Seal the native values in the run manifest before any source kappa is
     computed. A later implementation can do this with a hash of the target
     host manifest.

2. Compute source kappa independently.
   - Build source `A` from the existing T39/T224 kappa machinery without reading
     target native values.
   - Pre-register the source-to-host pairing rule before unsealing target native
     values. The rule may read source kappa and declared structural metadata, but
     must not read `Delta_i`, `rank_B_epsilon`, or `compute_kappa(nu_B)`.

3. Write the prediction before native comparison.
   - The prediction record must contain `kappa_A`, the allowed fields read by the
     transport rule, and the predicted native target quantity.
   - If the prediction is an integer, specify whether it predicts
     `rank_B_epsilon`, a threshold crossing pattern, or only presence/absence.
   - If the native host has real units, retain the real-unit comparison even when
     an integer rank is also reported.

4. Compute the target natively.
   - Compute `Delta_i` using the host's own value or rate-distortion procedure.
   - Compute `rank_B_epsilon` only after the real-unit value vector is recorded.
   - The native procedure must not call `compute_kappa`, `nu_from_*`, cycle
     helpers, quorum helpers, or the source builder.

5. Build `nu_B` from visible host data, not from the native rank.
   - `nu_B` may be built from observation partitions, decision-channel
     indistinguishability, or declared visible equivalence classes.
   - It must not emit one frustrated cycle per above-floor block by directly
     reading `rank_B_epsilon`.
   - If no such native-to-`nu` construction exists, the verdict is
     `inconclusive_missing_visible_functor`, not a pass.

6. Compare in three columns.
   - Report `kappa_A`, native `V_B`, native `rank_B_epsilon`, and
     `compute_kappa(nu_B)` separately.
   - At least one retained control row must have a mismatch among these columns;
     otherwise the run has not shown the equality gate can fail.
   - Do not discard mismatches after seeing them.

## Required Controls

| Control | Purpose | Required outcome |
| --- | --- | --- |
| Count-all classifier | Proves the gate is not a raw-cell counter. | Fails at an at-floor or shared-block case. |
| Same-visible-data non-split | Tests whether visible `nu` can distinguish native value. | Two hosts share visible data while `V_B` or `rank_B_epsilon` differs; either transport fails or the missing field is named. |
| At-floor strictness | Tests the threshold boundary. | `Delta_i = epsilon` does not count as above-floor. |
| Shared-block multiplicity | Tests independence rather than cell count. | Multiple above-floor cells in one block count once. |
| Source-target mismatch | Provides a real falsifying branch. | At least one pre-registered source `kappa_A` does not equal native target rank. |
| T244-style positive fixture | Keeps the prior value-gap artifact as a calibration control. | May pass, but cannot be the only positive evidence. |

## Verdict Taxonomy

- `hostile_pass`: the pre-registered transport rule predicts the native host on
  the blinded panel, including controls where equality was not built into the
  fixture; `nu_B` is generated from visible host data independently of native
  rank.
- `catalogue_only`: the run shows that kappa can re-encode the host after a
  native rank is known, but not predict it.
- `boundary_named`: same-visible-data or source-target mismatch controls show
  that visible kappa cannot determine the host's native value without adding a
  new field.
- `inconclusive_missing_visible_functor`: the native host is well-defined, but no
  independent construction of `nu_B` from visible host data is available.
- `killed`: the pre-registered prediction misses and cannot be repaired without
  reading target native values or retuning kappa.

## Acceptance-Criteria Satisfaction

- Source kappa, target native value, and synthetic `nu` are separated by protocol:
  the target panel is frozen first, native values stay in real host units, `nu_B`
  is built only from visible host data, and mismatch controls are retained.
- The host has own units and a native comparison before transport:
  `Delta_i`, `epsilon`, and `V_B` are recorded before any integer rank is used.
- Negative controls include the required count-all classifier and same-visible-data
  non-split, plus at-floor, shared-block, and source-target mismatch controls.
- The output distinguishes catalogue from prediction through explicit verdicts.

## No-Promotion Guardrails

- Do not describe the result as a genre-agnostic theorem, independent-motivation
  closure, or T224 promotion.
- Do not say the kappa line predicts anything unless the verdict is
  `hostile_pass` under the blinded hostile-host protocol.
- Do not use physics, continuum, value-as-law, hardness, NP-hard, or scalable
  theorem language.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or
  open-problem files from this synthesis note.
- The strongest current safe language remains: finite multi-domain
  re-encoding catalogue, with the hostile non-combinatorial prediction question
  open until the protocol above is executed.
