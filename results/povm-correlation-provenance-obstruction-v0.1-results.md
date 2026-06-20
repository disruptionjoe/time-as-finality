# T67 Results: Correlation Provenance Obstruction

Strongest claim: Pairwise detector correlation can audit similarity of records, but it cannot by itself determine whether two records belong to the same D1 independence class.

Weakened claim: The T66 repair path 'derive provenance from measured channel-correlation alone' is too weak. Copied archives and independent readout chains can be observationally correlation-equivalent.

## Exact-overlap witness

- dependent scenario: dependent_transport_noisy; independent scenario: independent_exact_overlap; agreement gap: 0.0; phi gap: 0.0
- interpretation: A noisy copied archive and an independent readout pair have the same pairwise correlation statistics in the finite witness family.

## Best scalar-threshold audits

- agreement: threshold=1.0, orientation=dependent_if_score_ge_threshold, errors=2, misclassified=['dependent_transport_noisy', 'dependent_transport_very_noisy']
- phi: threshold=1.0, orientation=dependent_if_score_ge_threshold, errors=2, misclassified=['dependent_transport_noisy', 'dependent_transport_very_noisy']

## Next move

Add intervention metadata: delayed-copy tests, write-once tags, or signed detector provenance graphs. Then test whether those extra observables fix the independence partition before D1 is evaluated.
