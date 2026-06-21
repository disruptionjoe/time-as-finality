# T113: Gap Presheaf Classification

## Route

Observer-relative reconstruction / GU mathematical-language import.

## Question

Does the restriction-closed gap assignment

```text
G(U) = A(U) - F(U)
```

classify exactly the phantom incomparability witnesses produced by the
multi-observer apparent/event-finality tests?

## Motivation

T56 showed that phantom incomparability is not an H1 obstruction in the sparse
observer cover. It lives instead as an H0-level mismatch between:

```text
A(U) = rho_U(S_global)
F(U) = S_local(U)
```

T57 then proved the Finality Reflection Property needed for `G` to restrict
correctly in the tested TaF model. T58 checked a first gap/phantom equivalence
family.

The GU integration roadmap makes this branch important because it is the
bounded, TaF-native version of the "finality torsion" story. Before the repo
uses torsion language as more than analogy, it should prove or refute a precise
classification result for `G`.

## Construction

Build a finite family of observer covers that includes:

- T51 one-sided phantom incomparability.
- T52 complementary-observer reconstruction.
- T53 underdetermined descent controls.
- T56 hidden-intermediary and sparse-cover cases.
- T57 branching-dependency record lattices.
- T58 well-formed extension cases and local-reversal controls.

For each cover, compute:

```text
A(U) = ambient global order restricted to U-accessible events
F(U) = apparent order computed from U-accessible events
G(U) = A(U) - F(U)
```

Then compare global sections of `G` against the independently computed set of
phantom incomparability witnesses.

## Success Criteria

- Define the object being classified: ordered event pairs, endpoint-accessible
  pairs, or typed gap witnesses.
- Prove or exhaustively test that every `G` section corresponds to a phantom
  incomparability witness.
- Prove or exhaustively test that every phantom incomparability witness appears
  in the appropriate `G` section.
- Preserve T57 restriction closure and non-lifting examples.
- Reject malformed cases where `F(U)` is not contained in `A(U)` or where local
  reversal creates fake gaps.
- State whether the classification is H0(G), a quotient of H0(G), or a
  stricter typed witness set.

## v0.1 Result

Implemented as a finite audit. Raw `H0(G)` is refuted as a classifier:

```text
raw gap sections: 13
phantom sections: 10
```

The supported object is a stricter typed subobject of `H0(G)`:

```text
typed gap sections: 10
phantom sections:   10
```

The typed subobject requires endpoint access, a canonical ambient completion,
`F(U) subset A(U)`, and local incomparability rather than reversal or conflict.
The extra raw gaps come from T53 noncanonical hidden-record repair and T58
local-reversal controls. FRP restriction closure is preserved.

## Failure Criteria

- `G` contains pairs that are not phantom incomparability witnesses.
- Phantom witnesses exist that do not appear in `G` under the declared endpoint
  and typing rules.
- The result silently assumes complement closure without FRP.
- Underdetermined T53-style cases are misclassified as canonical phantom
  repairs.
- The report upgrades "finality torsion" from analogy to geometry without a
  proved TaF-native classification theorem.

## Claim Impact

T113 upgrades the GU-facing story from analogy to a precise finite TaF result:

```text
phantom incomparability is classified by a typed subobject of the gap presheaf.
```

This justifies disciplined "typed torsion-like gap" language in technical
summaries, while still not importing GU physics.

Raw `H0(G)` remains too broad. Physical torsion and sheafification language
remain blocked.

## Known Guardrails

- This test does not validate GU.
- This test does not derive the arrow of time.
- This test does not prove that `F` sheafifies to `A`.
- This test does not establish a physical torsion tensor.

## Contribution Needed

Next contribution: decide whether the typed subobject has a natural abstract
definition beyond the current finite witness family, and whether it interacts
with the T19 accessible-witness gap as part of a common typed gap category.

## Reproduction

```bash
python -m unittest tests.test_gap_presheaf_classification -v
python -m models.run_t113
```

Artifacts:

- [`models/gap_presheaf_classification.py`](../models/gap_presheaf_classification.py)
- [`models/run_t113.py`](../models/run_t113.py)
- [`tests/test_gap_presheaf_classification.py`](test_gap_presheaf_classification.py)
- [`results/gap-presheaf-classification-v0.1.json`](../results/gap-presheaf-classification-v0.1.json)
- [`results/gap-presheaf-classification-v0.1-results.md`](../results/gap-presheaf-classification-v0.1-results.md)
- [`TECHNICAL-REPORT-gap-presheaf-classification-v0.1.md`](../TECHNICAL-REPORT-gap-presheaf-classification-v0.1.md)
