# Access as Record-Restriction Invariant v0.1

## A. One-Page Synthesis

The recent tests are not merely repeating the word "access." They are
converging on a finite local-to-global object:

```text
observer-indexed record restriction data
  =
  sites / observers
  + local record values or D1 profiles
  + access or trusted reachability relation
  + provenance / independence partition
  + local quality or calibration predicate
  + compatibility / global reconstruction predicate
```

The best existing name for this object is close to T26's
`D1RestrictionSystem`, but T64/T66 show that the quantum-measurement branch
needs two extra fields to be first-class: provenance/independence partition and
calibration/threshold policy. Access alone is too weak; calibration alone is
also too weak. The recurring invariant is the restriction structure that says
which records are reachable, which reachable records count as independent, and
which local records can be glued into a global witness.

The recurring structure is:

```text
local record quality != observer-relative finality
```

because finality also depends on whether adequate witnesses lie in the
observer's accessible region and whether those witnesses are independent rather
than copied or provenance-dependent.

This appears in three different forms:

- T19: external self-finality witnesses exist, but they are outside the
  observer's access boundary.
- T64/T66: detector records can be high quality, redundant, and calibrated, but
  D1 still changes under access windows, thresholds, and provenance partitions.
- T51-T54/T58: local observer orders or context sections can be valid while the
  global reconstruction requires missing record bases, identity maps, overlap
  witnesses, or suborder compatibility.

So the working slogan "calibration cannot repair missing access" is basically
right, but incomplete. The sharper statement is:

```text
Local quality cannot repair missing access, missing provenance, or missing
descent data.
```

## Goal 1: Convergence Map

| Test | Initially explanatory variable | Load-bearing variable after test | Access | Provenance / independence | Calibration / local quality | Final outcome driver |
| --- | --- | --- | --- | --- | --- | --- |
| T60 Observer Closure | D1 fixed-point iteration and monotonicity | Reachability plus bridge record enabling closure | Yes: iterative access expansion | Weak: bridge record is a provenance-like record-of-recording | No | Fixed point exists only because graph reachability carries R's own recording events back into access. |
| T19 First-Person Finality | Self-reference / complexity separation | Causal access boundary for self-finality witnesses | Dominant | Weak: external witnesses certify R_self_finality | No | External truth is positive, internal verification fails because witnesses are outside A*(R). |
| T64 Stern-Gerlach Access Window | Detector-shaped reliability and redundancy | Access window, threshold, independence partition | Dominant | Dominant: archive copy does not add independent holder | Present but insufficient | Same detector proxy changes verdict under threshold and independence assumptions. |
| T66 POVM Calibration Obstruction | Calibrated POVM response matrices | Threshold policy plus provenance/independence partition | Dominant | Dominant: copied log vs independent archive flips finality | Present and explicit, still insufficient | Same POVM response supports opposite D1 verdicts under different provenance/threshold rules. |
| T58 Gap-Phantom Equivalence | H0 gap object `G=A-F` | Suborder compatibility `F(U) subset A(U)` | Present through observer-local apparent order | Present as local/ambient compatibility | No | Gap equals phantom incomparability only when local order is missing ambient order, not conflicting with it. |
| T51-T52 Colimits | Record-basis union / colimit | Bounded record access and complementary record bases | Dominant | Moderate: which record bases are merged matters | No | Phantom incomparabilities are repaired only by combining observer record bases. |
| T53-T54 Descent | Partial-order validity | Identity maps, overlap witnesses, record annotations, AM compatibility | Present | Dominant as descent data | Axis quality matters but does not suffice | Valid colimit is weaker than canonical reconstruction. |
| T25-T26 Restriction Systems | Scalar or vector D1 | Graph-indexed restriction system with transport and patches | Dominant | Present as patch / compatibility data | Local D1 values present but insufficient | Scalar/vector projections lose graph and gluing information. |

## Goal 2: Smallest Common Formal Object

Access boundary alone reproduces T19 but not T64/T66, because archive copies
can be accessible but non-independent. Provenance partition alone reproduces
the archive-copy problem but not T19, because the issue there is witness
unreachability. Calibration alone reproduces none of the separating results.

The smallest object that appears to reproduce all reviewed cases is:

```text
Access-Provenance Restriction Datum APRD =
  S: finite sites / observer domains
  R_s: records locally available at each site
  A_s: accessible records or trusted reachability from each site
  P: provenance / independence equivalence on records
  Q: local quality predicate on records
  C: compatibility, overlap, or patch constraints
  Gamma: global reconstruction / section predicate
```

T26's `D1RestrictionSystem` already contains most of this:

```text
sites, local D1 profiles, proposition values, trusted transport edges,
overlap tests, patch constraints, projection maps, compatibility predicate,
global-section predicate
```

What APRD adds explicitly for T64/T66 is:

- provenance / independence classes for duplicate records;
- calibration / threshold policy separating local detector quality from
  finality verdicts.

Candidate relation:

```text
D1RestrictionSystem + provenance partition + quality policy = APRD
```

This is probably the minimal finite object for the current evidence. Full sheaf
language is still not forced, but APRD is sheaf-compatible: it can be upgraded
when covers, restrictions, and cohomology are genuinely needed.

## Goal 3: General Theorem Status

Candidate statement:

```text
Improvements in local measurement quality cannot eliminate ambiguities caused
by inaccessible or provenance-dependent record structure.
```

This is not yet a proved theorem in the repo, but it is strongly suggested by
existing tests. A precise theorem schema is available:

```text
Calibration Insufficiency Lemma.

Let finality for observer o require at least k accessible independent witness
classes satisfying a local quality predicate Q. If a record r is outside A_o,
or if r lies in a provenance class already represented in A_o, then increasing
Q(r) cannot by itself change o's finality verdict.
```

This lemma is already instantiated by:

- T19: self-finality witnesses outside A*(R) cannot affect first-person verdict.
- T64: archive copy can increase raw accessible redundancy without increasing
  independent holder redundancy.
- T66: improving detector response matrices does not choose threshold or
  provenance; copied archive and independent archive have same calibration but
  different finality.

The theorem needs one more executable bridge: define APRD formally and show
T19, T64, and T66 are morphisms or projections of it.

Verdict: new theorem candidate, already implied in fragments by existing tests,
not false on current evidence.

## Goal 4: Beyond Quantum Measurement

The same structure appears outside quantum measurement.

T60 is the positive side: access expansion under a monotone operator reaches a
least fixed point because bridge records and return reachability exist.

T19 is the negative side: closure exists, but finality-of-closure witnesses
remain outside the bounded observer region.

T58 shows that gap witnesses are not arbitrary missing data; they require the
local apparent order to be a suborder of the ambient order. This is a
compatibility condition on restriction data.

T51-T54 show that access-dependent reconstruction is deeper than temporal
ordering. Bounded observers create phantom incomparabilities; colimits can
repair some; canonical reconstruction requires descent data beyond mere
partial-order validity.

T25-T26 already identify the formal direction: scalar and vector D1 are
projections. The graph-indexed restriction system is the actual carrier of the
information needed for transport and gluing.

## B. Theorem Candidate List

| Name | Verdict | Why |
| --- | --- | --- |
| Access Dominance Theorem | Too strong | Access is dominant in T19 and important in T64/T66, but provenance and descent data are also load-bearing. This name risks erasing independence and compatibility. |
| Calibration Insufficiency Theorem | Strong narrow theorem | Best for the quantum-detector thread. It says POVM/reliability improvements cannot determine D1 without access, threshold, and provenance rules. |
| Reconstruction Boundary Theorem | Best broad theorem name | Covers T19, T51-T54, T58, and T64/T66. It names the split between local records and global reconstructability without overclaiming that access alone is the invariant. |
| Accessible Witness Theorem | Good lemma name | Best for the T19/T64/T66 shared core: only accessible independent witnesses can alter observer-relative finality. |
| Provenance-Access Restriction Theorem | Most precise but less readable | Names the actual minimal object: access plus provenance/independence plus compatibility. Useful for formal work, less useful as a top-level claim. |

Recommended naming:

- broad family: **Reconstruction Boundary Theorem family**;
- first lemma: **Accessible Independent Witness Lemma**;
- quantum-detector corollary: **Calibration Insufficiency Corollary**.

## C. Assessment

Rating: **3. Emerging theorem family**.

This is stronger than a useful pattern because the same local-to-global shape
appears in observer closure, first-person finality, detector records,
contextuality, colimits, descent, and restriction systems. It is not yet a
candidate organizing principle for the entire repo because thermodynamic arrow,
black-hole horizons, and spacetime reconstruction still need to be rechecked
against APRD rather than assumed to fit.

The convergence is not misleading, but "access is the invariant" is too narrow.
The more precise invariant is:

```text
access-indexed independent witness structure with descent compatibility
```

or, operationally:

```text
which records can be reached, which reached records count independently, and
whether local witnesses can reconstruct a global section.
```

## Next Formal Move

Define APRD as a small extension of `D1RestrictionSystem` and implement three
projection tests:

1. T19 projection: inaccessible external witnesses keep first-person finality
   false while third-person finality is true.
2. T66 projection: same calibrated POVM data but different provenance partition
   flips D1 finality.
3. T51/T58 projection: missing ambient order yields phantom gaps only under
   the suborder condition.

If one object reproduces all three, promote the Reconstruction Boundary Theorem
family to a formal target. If any projection fails, keep this as a useful
pattern rather than a theorem family.
