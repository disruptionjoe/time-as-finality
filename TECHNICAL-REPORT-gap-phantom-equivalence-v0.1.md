# Technical Report: Gap-Phantom Equivalence v0.1

## Question

T56 left the following open question:

```text
Is H0(G) isomorphic to the set of phantom incomparability witnesses
from T51-T52?
```

T58 turns this into a finite executable audit. For each observer view in T51
and T52, it compares:

```text
A(U) = event-finality / colimit order visible at U
F(U) = observer-local apparent order
G(U) = A(U) - F(U)
```

against the phantom incomparability pairs independently reported by the
existing T51 and T52 models.

## Result

The equivalence holds for the tested T51/T52 well-formed extension witnesses:

```text
G(U) = phantom_pairs(U)
```

Specifically:

- T51 Observer A has empty gap and no phantom.
- T51 Observer B has exactly one gap pair, matching its one phantom.
- T52 Observer A has exactly one gap pair, matching its one phantom.
- T52 Observer B has exactly one gap pair, matching its one phantom.

All four observer views also satisfy:

```text
F(U) subset A(U)
```

so the apparent order is a suborder of the ambient event-finality order.

## Boundary

T58 includes a hostile local-reversal control:

```text
A(U) = {(a,b)}
F(U) = {(b,a)}
```

Here:

```text
G(U) = {(a,b)}
phantom_pairs(U) = empty
```

because the local observer did not see `a` and `b` as incomparable; it asserted
the reverse comparison. This is a conflict with the ambient order, not phantom
incomparability.

Therefore the refined claim is:

```text
In the tested T51/T52 witness class, if F(U) is a suborder of A(U),
then H0(G) exactly enumerates phantom incomparability witnesses.
```

The suborder condition is not decorative. It separates missing ambient order
from conflicting local order.

## Claim Status

T58 strengthens T56 Q1 from an open question to a bounded positive result for
the existing T51/T52 finite witness family.

It does not promote the result to a universal theorem about arbitrary
observer assignments, arbitrary covers, or arbitrary presheaves.

## Why It Matters

T56 rejected the original H1 cohomology interpretation and suggested that the
right invariant was H0(G). T58 gives the first executable evidence that this
replacement is not merely a relabeling: in the core phantom-incomparability
witnesses that motivated the question, the gap sections exactly recover the
phantom witnesses.

The local-reversal control also sharpens the required hypotheses. A future
general theorem must include a compatibility or extension premise equivalent
to:

```text
F(U) subset A(U)
```

or else classify local/ambient conflict separately.

## Open Questions

- Does the same equivalence hold for T56-style covers with restricted event
  domains rather than T51/T52 all-event observer views?
- Can the suborder condition be derived from Finality Reflection Property
  plus a descent compatibility condition?
- Should conflict-enriched descent from T55 classify the hostile reversal
  control before any gap-presheaf invariant is evaluated?
- T56 Q2-Q4 remain open: sheafification, nerve cohomology, and arrow-direction
  circularity are not resolved here.
