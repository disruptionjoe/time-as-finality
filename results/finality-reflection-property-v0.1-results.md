# T57 Results: Finality Reflection Property

## Verdict

T57 supports FRP for the T56 apparent-order model and licenses the gap-presheaf restriction step as a finite theorem. It also rejects the stronger idea that complements are automatically presheaves and leaves the arrow-origin circularity question open.

## Theorem Statement

Finality Reflection Property (v0.1): for the T56 apparent-order construction, if V is a proper subpatch of U in record-access order, then every non-reflexive pair in F(V) appears in the restriction of F(U) to V-accessible events. Equivalently, absence from F(U) reflects downward to absence from F(V). Therefore G(U)=A(U)-F(U) is closed under restriction. This closure is conditional on the TaF apparent-order definition and is not true for arbitrary complements.

## Reflection Checks

| Cover | Nested patch pairs | Checked event pairs | FRP holds | Violations |
| --- | ---: | ---: | --- | ---: |
| hidden_intermediary_record_lattice | 19 | 6 | True | 0 |
| branching_dependency_record_lattice | 65 | 60 | True | 0 |

## Gap Restriction Checks

| Cover | Nested patch pairs | Closed | Violations | Non-lifting examples |
| --- | ---: | --- | ---: | ---: |
| hidden_intermediary_record_lattice | 19 | True | 0 | 1 |
| branching_dependency_record_lattice | 65 | True | 0 | 6 |

## Generic Complement Counterexample

- Witness pair: `['x', 'y']`
- FRP holds: `False`
- Complement restriction closed: `False`
- Explanation: The ambient assignment is stable, but the chosen subassignment violates FRP: the smaller patch has (x,y) while the larger patch does not. Therefore the complement of the larger patch restricts outside the smaller complement.

## Hypothesis Results

### H0: refuted

The T56 apparent-order construction need not satisfy FRP.

Evidence: FRP held across both record-lattice witnesses.

### H1: supported

Apparent order is monotone under record-access inclusion.

Evidence: For every nested patch pair V<U, F(V) was included in rho(F(U)).

### H2: supported

The T56 gap assignment is restriction-closed once FRP holds.

Evidence: Every larger-patch gap restricted into the smaller-patch gap.

### H3: refuted

Complement restriction closure is automatic for any subassignment.

Evidence: The generic complement counterexample violates FRP and its larger complement restricts outside the smaller complement.

### H4: left_open

FRP resolves the T56 medium circular risk on arrow direction.

Evidence: FRP only proves monotonicity after directed source/target records are given. It does not derive that direction from substrate-free task composability.

## Limits

- The executable witnesses are finite record lattices, not an arbitrary machine-checked proof over all finite covers.
- The proof assumes the T56 event-access rule and record-dependency source/target relation.
- FRP gives restriction closure only; smaller-patch phantom gaps need not lift to larger patches.
- FRP does not derive the direction of finality arrows.

## Next Questions

- Turn the proof sketch into a short formal lemma in FORMALISM with explicit quantifiers over finite covers.
- Use FRP to test whether H0(G) is exactly the T51-T52 phantom-pair set.
- Attack T56 Q4 separately: derive or reject arrow direction from constructor-style task composability.