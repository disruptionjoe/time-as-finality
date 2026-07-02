# P04 Run - Topologist / Sheaf Theorist

- timestamp: 2026-06-20T12:39:34-05:00
- goal_id: P04
- selected_persona: Topologist / Sheaf Theorist
- selected_goal: Rebuild the apparent-finality cohomology story with explicit coefficient systems, support presheaves, covers, restriction maps, and counterexamples.
- bounded_question: What is the narrowest topology-facing story the repo can defend today that cleanly separates `H0` gap facts from `H1` obstruction claims?

## Repo Context Read

- [`/Github Repos/time-as-finality/tests/T56-sheaf-cohomology-apparent-finality.md`](/Github%20Repos/time-as-finality/tests/T56-sheaf-cohomology-apparent-finality.md)
- [`/Github Repos/time-as-finality/tests/T58-gap-phantom-equivalence.md`](/Github%20Repos/time-as-finality/tests/T58-gap-phantom-equivalence.md)
- [`/Github Repos/time-as-finality/tests/T59-finite-to-infinite-boundary-audit.md`](/Github%20Repos/time-as-finality/tests/T59-finite-to-infinite-boundary-audit.md)
- [`/Github Repos/time-as-finality/tests/T65-causal-reduction-holonomy.md`](/Github%20Repos/time-as-finality/tests/T65-causal-reduction-holonomy.md)
- [`/Github Repos/time-as-finality/tests/T69-losskernel-failure-type.md`](/Github%20Repos/time-as-finality/tests/T69-losskernel-failure-type.md)
- [`/Github Repos/time-as-finality/tests/T89-accessible-witness-gap-lemma.md`](/Github%20Repos/time-as-finality/tests/T89-accessible-witness-gap-lemma.md)
- [`/Github Repos/time-as-finality/tests/T92-accessible-witness-gap-restriction.md`](/Github%20Repos/time-as-finality/tests/T92-accessible-witness-gap-restriction.md)
- [`/Github Repos/time-as-finality/results/finite-to-infinite-boundary-audit-v0.1-results.md`](/Github%20Repos/time-as-finality/results/finite-to-infinite-boundary-audit-v0.1-results.md)
- [`/Github Repos/time-as-finality/results/losskernel-failure-type-v0.1-results.md`](/Github%20Repos/time-as-finality/results/losskernel-failure-type-v0.1-results.md)
- [`/Github Repos/time-as-finality/results/accessible-witness-gap-restriction-v0.1-results.md`](/Github%20Repos/time-as-finality/results/accessible-witness-gap-restriction-v0.1-results.md)

## Work Performed

1. Re-read the apparent-finality branch at the specification level:
   - `T56` for the original `H1` attempt;
   - `T58` for the bounded `H0(G)` phantom-pair equivalence;
   - `T89` and `T92` for the proposition-domain accessible-witness gap lane.
2. Re-read the executable boundary surfaces that limit any upgrade:
   - `T59` for the Mobius/coefficient-boundary warning;
   - `T69` for the loss-morphism and support/cover caveats;
   - `T65` for the distinct CHSH `H1` line with explicit `Z/2Z` structure.
3. Collapsed the branch into two lanes and recorded the minimum admission rules for each lane.

## Result

### 1. The defensible lane today is an `H0` gap program

The cleanest shared structure across `T56`, `T58`, `T89`, and `T92` is not "cohomology"
in the broad sense. It is a finite degree-0 gap object:

```text
A(U) = ambient object over patch U
F(U) = locally auditable or locally computed object over U
G(U) = A(U) - F(U)
```

What is currently supported:

- `T56`: phantom incomparability is not detected by `H1` in the sparse cover; it lives at the
  section-compatibility / gap level. The ambient assignment `A` behaves contravariantly, while
  the local apparent-order assignment `F` is not itself a presheaf.
- `T58`: in the bounded `T51/T52` witness class, `G(U)` matches exactly the independently
  reported phantom pairs, provided the local object is a suborder of the ambient object.
- `T89`: the T19 first-person / third-person gap can be written in the same shape, but with
  unary propositions rather than order pairs.
- `T92`: that unary gap lane is restriction-closed only under explicit conditions:
  ambient restriction, audit monotonicity, and stable proposition typing.

So the honest shared theorem-shaped story is:

```text
TaF has a finite typed H0 gap program with multiple object types
(order-pair gaps, proposition gaps), not a single universal H1/cohomology theorem.
```

### 2. `H1` survives only as an explicitly typed, coefficient-bearing branch

The repo does have a real `H1` lane, but it is much narrower than the old prose implied.

- `T65` is an actual coefficient-bearing obstruction story: CHSH on a 4-cycle cover with
  `Z/2Z` holonomy data.
- `T59` shows why that discipline matters: the same Mobius witness is detected by a
  transition-aware `Z/2Z` encoding and missed by a coefficient-blind scalar encoding.
- `T69` adds the second warning: cover topology alone is not enough. The result depends on
  the coefficient/support object, the allowed loss morphisms, and the exact cover semantics.

That yields the minimal admission rule for any future `H1` claim:

1. Name the cover and its overlaps.
2. Name the section object on each patch.
3. Name the coefficient system or support-presheaf / transition data.
4. Name the restriction maps or cocycle transitions.
5. Name the allowed loss morphism class if monotonicity or "obstruction relocation" is claimed.
6. State at least one counterexample showing what fails when coefficient or support data are forgotten.

Without all six, the branch should not use `H1` rhetoric.

### 3. Counterexamples that should govern future wording

Three counterexamples do most of the policing work:

- `T56` sparse hidden-intermediary cover: phantom gap present, but `H1 = 0`.
  This blocks "phantom incomparability is an H1 obstruction."
- `T59` coefficient-blind Mobius encoding: continuous obstruction present, but the scalar parity
  reduction produces a false global section.
  This blocks "finite parity language automatically detects the continuous obstruction."
- `T92` semantic-relabeling and audit-monotonicity controls:
  the unary accessible-witness gap only restricts when the proposition typing is stable and the
  larger patch does not lose auditability.
  This blocks "any ambient-minus-local difference is a valid gap presheaf."

### 4. Recommended rebuild of the cohomology story

If this branch is summarized later, it should be split as:

- `H0 lane`: finite typed gap objects `G = A - F`, with separate instances for
  order-pair gaps (`T56/T58`) and proposition gaps (`T89/T92`).
- `H1 lane`: explicit coefficient-bearing obstruction witnesses such as CHSH
  holonomy (`T65`) and any future continuous sheaf examples that pass the `T59` boundary.
- `Bridge claim`: open. The repo does not yet show that the `H0` gap lanes and the `H1`
  obstruction lanes are instances of one common typed category; it only shows that they
  share a family resemblance in bounded finite witnesses.

## Blocker

The branch still lacks a single explicit "cohomology discipline" note that declares:

- which current objects are genuinely presheaves;
- which objects are only local assignments inside an ambient presheaf;
- which coefficient systems are fixed in each `H1` example;
- and which counterexamples block generalization.

Until that note exists, future summaries can still slide back into saying "sheaf/cohomology"
when the actual result is only an `H0` gap witness.

## Proposed Next Action

1. Have `P05 - Algebraic Topologist` turn this into an invariant dictionary:
   `gap object`, `global-section failure`, `obstruction class`, `support object`,
   `cycle-destroying loss`, and `typed restriction witness`.
2. If a documentation pass is later authorized, add a short guardrail note near the
   T56/T58/T89/T92 branch saying: "`H0` gap witnesses are the default story; `H1`
   requires an explicit coefficient-bearing construction."

## Claim-Status Posture

- No claim-status changes recommended.
- Narrow positive statement: the repo supports a finite typed `H0` gap program.
- Narrow caution: current `H1` language is only justified for explicitly typed,
  coefficient-bearing witnesses with named covers and restriction data.
- Open gap: no common formal category yet unifies the order-pair and proposition-gap lanes.
