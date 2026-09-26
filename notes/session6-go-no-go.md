# Session 6 — Adversarial Go / No-Go Gate

Date: 2026-09-26

Exit state: **PILOT_KILL**.

This session treats Sessions 3–5 as controlling. It does not alter the frozen residual-index statistic, the Euler product, the prior-art conclusions, the Level-1 conclusion, or the Session-5 continuation obstruction.

The scope is a fixed positive non-perfect-power integer (a>1) and fixed real (z>0), except where a statement is explicitly abstract or finite-level.

## 1. Green-light and kill standards fixed before the attack

A **GREEN LIGHT** requires at least one of:

1. a new Level-2 or Level-3 continuation theorem;
2. a power-saving centered discrepancy theorem;
3. a strong smoothed power-saving theorem plus a rigorous route to continuation;
4. a precise tower-averaged Chebotarev conjecture/theorem target together with a credible mechanism specific to the residual-index/Kummer tower;
5. a different object, still closely tied to residual index/Kummer structure, supporting a non-routine theorem programme not already standard generalized-Artin theory.

An unanswered question does not count. In particular, an abstract possibility of cancellation, a finite-level continuation theorem, or a generic request for stronger Chebotarev/large-sieve uniformity does not count.

A **KILL** results if no item above is met and the surviving task is, after correct reformulation, an improvement in generic/infinite-family Chebotarev or Artin-type prime distribution for which the residual-index object supplies no effective leverage beyond the classical generalized-Artin/Hooley architecture.

That is the standard used below.

---

## 2. Exact centered discrepancy decomposition

Write
[
pi_a^circ(x)=#{ple x:p
mid a}
]
and
[
pi_n^I(x)=#{ple x:p
mid a, nmid I_a(p)}.
]
Let
[
d_n=[K_n(a):mathbf Q],
qquad
g_z=mu*(nmapsto n^{-z}).
]
Under the same source-matched hypothesis under which
[
Delta_a(z)=sum_{nge1}rac{g_z(n)}{d_n}
]
is available, the pointwise finite divisor identity gives, for every (Nge1),
[
oxed{
D_z^circ(x)
=
sum_{nle N}g_z(n)
left(
pi_n^I(x)-rac{operatorname{li}(x)}{d_n}
ight)
+
mathcal T_z(x;N)
-
operatorname{li}(x)sum_{n>N}rac{g_z(n)}{d_n}
+
Delta_a(z)igl(operatorname{li}(x)-pi_a^circ(x)igr),
}
	ag{2.1}
]
where the hard divisor-supported prime tail is exactly
[
oxed{
mathcal T_z(x;N)
=
sum_{substack{ple x\p
mid a}}
sum_{substack{nmid I_a(p)\n>N}}g_z(n).
}
	ag{2.2}
]

Thus the four pieces are explicit:

1. **finite centered Kummer levels**
   [
   sum_{nle N}g_z(n)
   left(pi_n^I(x)-operatorname{li}(x)/d_night);
   ]
2. **divisor-supported prime tail** (mathcal T_z(x;N));
3. **degree-series tail**
   [
   -operatorname{li}(x)sum_{n>N}g_z(n)/d_n;
   ]
4. **PNT normalization correction**
   [
   Delta_a(z)(operatorname{li}(x)-pi_a^circ(x)).
   ]

Equivalently, centering first by (pi_a^circ(x)),
[
D_z^circ(x)
=
sum_{nle N}g_z(n)
left(
pi_n^I(x)-rac{pi_a^circ(x)}{d_n}
ight)
+
mathcal T_z(x;N)
-
pi_a^circ(x)sum_{n>N}rac{g_z(n)}{d_n}.
	ag{2.3}
]

For (p
mid an), (pi_n^I) is the completely-split counting function for (K_n(a)). As proved in Session 5, passing to the complete-splitting convention introduces only the already-recorded finite exceptional correction (the only possible accidental (pmid n) contribution is the (n=2,p=2) case, together with the fixed omission of (pmid a)). No hard term is hidden there.

Equation (2.1) is the sharp truncation identity used in this session.

---

## 3. Signed finite-level sum: what cancellation is actually present?

Under tower GRH, Session 5 gives
[
E_n(x):=
pi_n^I(x)-rac{operatorname{li}(x)}{d_n}
=
O_a(sqrt{x}log(nx))
]
up to the finite convention above. The triangle inequality gives
[
sum_{nle N}|g_z(n)E_n(x)|
ll_a
sqrt{x}Nlog(Nx),
]
which is too expensive at large (N).

The signs of (g_z) are genuinely Möbius-like on squarefree integers:
[
g_z(n)
=
(-1)^{omega(n)}n^{-z}prod_{ellmid n}(ell^z-1).
]
However, the functions (E_n(x)) are not multiplicative in (n), and their finite-level (L)-functions are coupled through field intersections. The scalar identity
[
sum_{nge1}rac{g_z(n)}{n^w}
=
rac{zeta(w+z)}{zeta(w)}
]
therefore does not transfer to
[
sum_n g_z(n)E_n(x).
]

There is nevertheless an exact covariance structure coming from nestedness. It is the strongest project-specific positive result of Session 6 and is isolated in Section 5.

---

## 4. Signed divisor-supported tail: an exact obstruction

For a positive integer (m), define
[
R_{z,N}(m)
=
sum_{substack{nmid m\n>N}}g_z(n).
]
The full divisor identity gives the exact formulas
[
oxed{
R_{z,N}(m)
=
m^{-z}
-
sum_{substack{nmid m\nle N}}g_z(n)
}
	ag{4.1}
]
and, by divisor pairing,
[
oxed{
R_{z,N}(m)
=
sum_{substack{dmid m\d<m/N}}g_z(m/d).
}
	ag{4.2}
]

These formulas preserve every sign. They show that the signed tail is not uniformly small.

If (q>N) is prime, then
[
R_{z,N}(q)=g_z(q)=q^{-z}-1,
]
so
[
oxed{|R_{z,N}(q)|longrightarrow1.}
	ag{4.3}
]
Thus no pointwise cancellation theorem for the truncated divisor sum can replace the Felix--Murty large-index analysis. Prime residual indices are a concrete obstruction to such a strategy.

The same obstruction appears in the local valuation expansion
[
m^{-z}
=
prod_ell
left(
1+sum_{1le kle v_ell(m)}g_z(ell^k)
ight).
	ag{4.4}
]
Higher powers have decay, but the first layer
[
g_z(ell)=ell^{-z}-1
]
does not. Reorganising by squarefree kernel, radical, or valuation vector therefore retains a non-decaying first-level obstruction.

Rankin tricks, Perron inversion in the divisor variable, and smooth/rough decomposition can redistribute this tail but cannot make (4.3) disappear. Any power saving must use distribution of the residual indices over primes, not an intrinsic smallness of the signed divisor tail.

---

## 5. Nested Kummer tower: exact profinite (L^2) structure

This is the strongest genuinely project-specific mechanism found.

Let
[
L_a=igcup_{nge1}K_n(a),
qquad
G_a=operatorname{Gal}(L_a/mathbf Q),
]
with normalized Haar measure (mu), and put
[
U_n=operatorname{Gal}(L_a/K_n(a)).
]

### 5.1 Exact lcm law

For all (m,nge1),
[
oxed{
K_m(a)K_n(a)=K_{operatorname{lcm}(m,n)}(a).
}
	ag{5.1}
]
Indeed (K_{operatorname{lcm}(m,n)}) contains both fields. Conversely, Bézout applied to
[
rac{operatorname{lcm}(m,n)}m,qquad
rac{operatorname{lcm}(m,n)}n
]
recovers both a primitive (operatorname{lcm}(m,n))-th root of unity and (a^{1/operatorname{lcm}(m,n)}) from the two smaller levels.

Hence
[
U_mcap U_n=U_{operatorname{lcm}(m,n)}
]
and
[
mu(U_n)=rac1{d_n}.
]

Let
[
X_n=mathbf1_{U_n},
qquad
Y_n=X_n-rac1{d_n}.
]
Then
[
oxed{
langle Y_m,Y_nangle_{L^2(G_a)}
=
rac1{d_{operatorname{lcm}(m,n)}}
-
rac1{d_md_n}.
}
	ag{5.2}
]

This is an exact covariance law, not a heuristic.

### 5.2 Unconditional (L^2) convergence

For positive non-perfect-power (a),
[
d_ngg_a narphi(n).
]
Since (|g_z(n)|le1),
[
sum_{m,nge1}
rac{|g_z(m)g_z(n)|}{d_{operatorname{lcm}(m,n)}}
le
sum_{ellge1}
rac{	au(ell)^2}{d_ell}
<infty.
	ag{5.3}
]
Therefore
[
oxed{
F_z(sigma)
:=
sum_{nge1}g_z(n)
left(
mathbf1_{U_n}(sigma)-rac1{d_n}
ight)
}
	ag{5.4}
]
converges unconditionally in (L^2(G_a,mu)).

Moreover, for every (arepsilon>0),
[
oxed{
left|
sum_{n>N}g_z(n)Y_n
ight|_2^2
ll_{a,arepsilon}
N^{-1+arepsilon},
qquad
left|
sum_{n>N}g_z(n)Y_n
ight|_2
ll_{a,arepsilon}
N^{-1/2+arepsilon}.
}
	ag{5.5}
]

Since
[
sum_{nge2}mu(U_n)=sum_{nge2}rac1{d_n}<infty,
]
Borel--Cantelli implies that Haar-almost every (sigma) belongs to only finitely many (U_n). For such a (sigma), the finite set
[
{n:sigmain U_n}
]
is divisor-closed and lcm-closed, hence is precisely the divisor set of a finite integer (I(sigma)). Consequently
[
sum_n g_z(n)mathbf1_{U_n}(sigma)
=
I(sigma)^{-z}
]
almost everywhere.

Thus (5.4) is genuinely a centered residual-index observable on the profinite Kummer image.

### 5.3 Why this does not green-light the project

The theorem above is a Haar statement. The project needs effective equidistribution of prime Frobenius elements against a family of observables whose finite level grows with (x).

Under tower GRH, one can expand a finite-window square and use (5.2) plus Chebotarev for the lcm composita. For (1le N<L),
[
sum_{substack{ple x\p
mid a}}
left|
sum_{N<nle L}
g_z(n)
left(
mathbf1_{nmid I_a(p)}-rac1{d_n}
ight)
ight|^2
ll_{a,z,arepsilon}
operatorname{li}(x)N^{-1+arepsilon}
+
sqrt{x},L^2log(Lx),
	ag{5.6}
]
up to harmless finite exceptional/PNT-normalization terms.

Equation (5.6) is the strongest conditional theorem obtained in Session 6. It proves that the covariance kernel survives at finite prime level, but the Chebotarev error pays for the lcm levels and becomes useless when (L) is large enough to control the full divisor tail. Cauchy--Schwarz does not convert (5.6) into the desired full power saving.

Most importantly, this (L^2) structure is not unique to finite (z). In the limit (z	oinfty), (g_z(n)	omu(n)), and the same lcm/inclusion--exclusion structure underlies the classical Artin primitive-root problem. The new (L^2) observation therefore does not make the finite-(z) problem demonstrably easier than the classical Hooley problem.

That is the decisive failure of green-light criterion D.

---

## 6. Smoothing the prime variable

For a smooth compactly supported (W),
[
D_{z,W}(X)
=
sum_{p
mid a}
left(I_a(p)^{-z}-Delta_a(z)ight)
W(p/X)
]
has the exact Kummer expansion
[
D_{z,W}(X)
=
sum_{nge1}g_z(n)
left[
sum_{substack{p
mid a\nmid I_a(p)}}W(p/X)
-
rac1{d_n}
sum_{p
mid a}W(p/X)
ight].
	ag{6.1}
]

Smoothing helps the vertical variable in an explicit formula: Mellin decay suppresses high zeros. It does not suppress the conductor/discriminant growth in (n), and the GRH finite-level error remains of square-root size with logarithmic (n)-dependence. Summing finite levels by absolute values still costs essentially (N); expanding a mean square still introduces lcm levels as in (5.6).

A **uniform family** of smoothed power-saving estimates would be sufficient for continuation: with a dyadic partition of unity, bounds stable for twists (u^{-it}) and with controlled seminorm dependence would give Mellin convergence/contour shifting in a half-plane. A power saving for one fixed test function would not by itself imply continuation.

No theorem matched in Section 7 supplies such a smoothed tower estimate. Smoothing therefore does not materially change the go/no-go decision.

---

## 7. Large sieve for Frobenius: theorem-level match audit

### 7.1 Zywina, Theorem 3.3

Zywina's *The Large Sieve and Galois Representations*, Theorem 3.3, assumes a system of **independent** Galois representations indexed by pairwise coprime ideals, finite image groups of polynomial size, and ramification in a fixed finite set plus the indexing prime. Independence is explicitly equivalent to linear disjointness of the corresponding fields.

The prime Kummer levels have superficially compatible size and ramification:
[
|G_ell|asympell^2,
qquad
operatorname{Ram}(K_ell)subseteq{ell}cup{p:pmid a}.
]
After isolating finite entanglement, prime-index quotients are the closest available match.

But the required object is a **weighted signed sum over all (n)**, including composite levels and the nested relations (K_msubset K_n) for (mmid n). Zywina's theorem sieves primes satisfying simultaneous local membership conditions. It does not estimate
[
sum_{nle N}g_z(n)E_n(x)
]
or the divisor-supported tail. The actual all-(n) family is deliberately non-independent.

**Verdict:** partial structural match, theorem mismatch. It does not give the Session-6 target.

### 7.2 Kowalski's large sieve for Frobenius

Kowalski's 2006 theorem is a large sieve for Frobenius conjugacy classes in coherent/lisse-sheaf systems over finite-field parameter spaces, with monodromy hypotheses. The varying object is a geometric family over a base variety.

The deterministic sequence
[
K_n(a)/mathbf Q,qquad n=1,2,ldots
]
is not such a family. There is no parameter variety and no matching monodromy system whose theorem statement yields the weighted (n)-average above.

**Verdict:** nearby technology, not a hypothesis match.

### 7.3 Murty--Petersen Bombieri--Vinogradov theorem

Murty--Petersen average over arithmetic-progression moduli for a **fixed** number-field splitting condition. Their mixed theorem twists a fixed extension by congruence classes; it does not average a deterministic tower of varying Kummer extensions.

**Verdict:** wrong averaging variable.

### Large-sieve conclusion

No audited large-sieve theorem produces the required weighted cancellation over the full Kummer index (n). Invoking "large sieve for Frobenius" as a Session-7 plan would therefore mean developing a new theorem, not applying an existing one.

---

## 8. Zero-density / explicit-formula audit

### 8.1 Thorner--Zaman, Theorem 1.1

Thorner--Zaman's zero-density theorem fixes a nontrivial finite group (G) and averages over Galois extensions (K/mathbf Q) with
[
operatorname{Gal}(K/mathbf Q)cong G.
]
Its family parameter explicitly includes
[
mathfrak m_{mathfrak F}(Q)
=
max_K
#{K':Kcap K'
emathbf Q}.
]

The Kummer tower has the opposite geometry:

- (G_n) varies with (n);
- (|G_n|=d_nasymp narphi(n)) grows;
- the fields are systematically nested/intersecting.

Taking singleton families loses the average and gives no advantage over the already-used GRH Chebotarev estimate.

**Verdict:** clear mismatch.

### 8.2 Lemke Oliver--Smith, Theorem 1.9 / Proposition 1.10

Their averaged Chebotarev framework controls most extensions of fixed degree/group after excluding fields containing specified bad subextensions. The effective range in Proposition 1.10 contains degree-dependent powers of (logDelta_K), and the paper explicitly emphasizes the obstruction caused by common subfields.

Our family has unbounded degree and forced common subfields. It is one deterministic tower rather than a large family from which exceptional fields can be discarded.

**Verdict:** no usable match.

### 8.3 Explicit formulas and averaged zeros

An explicit formula for each fixed (K_n) is already available through Session 5. Smoothing improves decay in zero height but does not provide cancellation between zeros belonging to different (n). Treating
[
zeta_{K_n}(s)/zeta(s)
]
as a family does not tame the rapidly growing degree/conductor, and no audited zero-density theorem allows precisely this nested varying-degree family.

**Zero-density conclusion:** no material improvement over tower GRH for the present purpose.

---

## 9. Alternative expansions of the weight

### 9.1 Exact-index basis

The exact identity
[
I_a(p)^{-z}
=
sum_{tge1}t^{-z}mathbf1_{I_a(p)=t}
	ag{9.1}
]
does produce a much better **coefficient tail**:
[
sum_{t>N}t^{-z}mathbf1_{I=t}
le N^{-z}
]
pointwise.

But the first term is
[
mathbf1_{I_a(p)=1},
]
the primitive-root indicator. Its fixed-base prime-counting problem is precisely classical Artin/Hooley territory and does not presently come with the required power-saving discrepancy. Fixed exact index (t>1) is the near-primitive-root problem and is built by Möbius inclusion--exclusion over the same Kummer fields.

Thus exact-index reorganisation exchanges a hard large-divisor tail for hard low-(t) exact-index discrepancies.

**Verdict:** cleaner coefficients, no stronger analytic theorem.

### 9.2 Large (z)

For every fixed (z>0),
[
I^{-z}
=
mathbf1_{I=1}
+
sum_{tge2}t^{-z}mathbf1_{I=t}.
	ag{9.2}
]
The tail has small coefficient mass when (z) is numerically large, but the primitive-root coefficient is exactly (1). No fixed threshold (z_0) removes the hardest low-index term.

Hence large (z) does not create a nonempty continuation range accessible by known theorems.

### 9.3 Special values (z=1,2)

For squarefree (n),
[
g_1(n)=mu(n)rac{arphi(n)}n,
]
and, using
[
d_n=rac{narphi(n)}{arepsilon_a(n)},
]
[
oxed{
rac{g_1(n)}{d_n}
=
arepsilon_a(n)rac{mu(n)}{n^2}.
}
	ag{9.3}
]
Likewise
[
g_2(n)
=
mu(n)prod_{pmid n}(1-p^{-2})
]
and
[
oxed{
rac{g_2(n)}{d_n}
=
arepsilon_a(n)rac{mu(n)}{n^2}
prod_{pmid n}left(1+rac1pight)
}
	ag{9.4}
]
for squarefree (n).

These are useful simplifications of the **mean constant**. The centered Chebotarev error (E_n(x)) has no compensating (1/d_n), so (9.3)–(9.4) do not improve the continuation problem.

### 9.4 Perron/Laplace/valuation/profinite bases

The profinite basis is the most successful alternative and gives Section 5's (L^2) theorem. Perron, Laplace, dyadic, or valuation expansions do not eliminate the non-decaying first divisibility layer. No basis tested produces a prime-side summable norm that is both exact and effectively equidistributed.

---

## 10. Can Level 2 require less than global power saving?

Yes logically, but no credible arithmetic route was found.

The implication
[
D_z^circ(x)=O(x^	heta)
Longrightarrow
Q_a^circ(s,z)	ext{ holomorphic for }Re(s)>	heta
]
is sufficient, not logically necessary.

One can formulate weaker boundary criteria using pseudofunctions, distributions, or Tauberian theory. Those criteria can prove boundary regularity without a pointwise power saving, but they do not automatically produce holomorphic continuation to an open region left of (Re(s)=1).

Conversely, if (Q_a^circ) had local continuation through a strip together with ordinary polynomial vertical control, a smooth Mellin inversion/contour shift would give power savings for a rich class of dyadic smooth prime sums. Thus a uniform smoothed power-saving theorem is a reasonable proxy for a credible local-complex route.

No verifiable pseudofunction, spectral, or transformed-discrepancy hypothesis specific to this arithmetic sequence was found. Abstract functional analysis therefore does not count as a green-light mechanism.

---

## 11. Lower-bound / natural-scale audit

No theorem was found that rules out a power saving.

A fixed finite Kummer level has the usual explicit-formula oscillations associated with zeta zeros, suggesting square-root-scale fluctuations under GRH. Such fluctuations are compatible with a target (O(x^{1-delta})) for any (delta<1/2).

Therefore:

- no natural boundary is inferred;
- no impossibility theorem is claimed;
- (x^{1/2+o(1)}) may be a heuristic natural scale, not a proved lower bound for the full weighted discrepancy.

The project is killed for lack of a credible project-specific route, not because the desired discrepancy is proved false.

---

## 12. Targeted prior-art / technology audit summary

The sources actually used in Session 6 are:

- D. Zywina, *The Large Sieve and Galois Representations*, Theorem 3.3: independent Galois representations / linearly disjoint fields; does not produce the required all-(n) weighted discrepancy.
- E. Kowalski, *The large sieve, monodromy and zeta functions of curves*, Theorem 3.1 / large-sieve framework: geometric finite-field family, not the deterministic Kummer tower.
- J. Thorner and A. Zaman, *A Zero Density Estimate for Dedekind Zeta Functions*, Theorem 1.1: fixed finite Galois group and an explicit field-intersection multiplicity; mismatched to a nested growing-degree tower.
- R. J. Lemke Oliver and A. Smith, *Faithful Artin induction and the Chebotarev density theorem*, Theorem 1.9 and Proposition 1.10: fixed-degree/group "most fields" technology with common-subfield obstructions; not a deterministic unbounded-degree tower theorem.
- M. R. Murty and K. L. Petersen, *A Bombieri--Vinogradov theorem for all number fields*: averages progression moduli around a fixed splitting problem; wrong averaging variable.
- Hooley / modern Artin literature: the (t=1) exact-index component remains the classical fixed-base primitive-root problem; average-over-(a) progress does not supply the required fixed-(a) power saving.

No source audited supplies an existing tower-averaged theorem that closes (2.1).

---

## 13. Strongest positive, strongest negative, and decision

### Strongest positive result obtained

The unconditional profinite theorem (5.2)–(5.5): nestedness gives an exact lcm covariance kernel and an (L^2)-convergent centered residual-index observable with tail
[
O_{a,arepsilon}(N^{-1/2+arepsilon})
]
in Haar (L^2).

This is real structure invisible to the Session-5 (L^1) treatment.

### Strongest conditional result obtained

Under tower GRH, the finite-window prime mean-square bound (5.6):
[
sum_{ple x}
left|
sum_{N<nle L}g_z(n)(mathbf1_{nmid I_a(p)}-1/d_n)
ight|^2
ll
operatorname{li}(x)N^{-1+arepsilon}
+
sqrt{x}L^2log(Lx),
]
with the standard fixed finite corrections.

It verifies the covariance mechanism but does not reach the full tail.

### Strongest obstruction obtained

The exact signed tail satisfies
[
R_{z,N}(q)=q^{-z}-1
]
for every prime (q>N), so the signed divisor tail has no uniform pointwise saving. At the same time, every known attempt to transfer the Haar (L^2) saving to primes reintroduces effective Chebotarev for composita whose levels grow with the truncation.

### Strongest project-specific mechanism

The lcm covariance / profinite (L^2) structure.

### Strongest reason to continue

That (L^2) structure is mathematically clean, nontrivial, and could be useful in a future project about probabilistic/profinite models of generalized Artin statistics.

### Strongest reason to kill

The only missing bridge is precisely an effective prime-equidistribution theorem for a growing nested Kummer tower. The (L^2) mechanism already survives at the primitive-root endpoint (g=mu), so it does not show that Pointed Order Zeta or finite (z) makes the classical generalized-Artin difficulty easier. Existing large-sieve and zero-density theorems do not match the family. The remaining proof request is therefore an improvement of general Artin/Chebotarev uniformity rather than a theorem programme powered by the project's new object.

This fails the Session-6 green-light standard.

---

## 14. Final adversarial questions

1. **What exact mathematical problem remains?**  
   Prove a power-saving prime discrepancy, or a uniform smoothed substitute, for the centered residual-index weight by effectively transferring the Haar (L^2) Kummer-tower cancellation to Frobenius primes.

2. **Is it actually specific to residual indices/Kummer towers?**  
   Its notation is, but its hard analytic core is not sufficiently specific: at (z	oinfty) it contains the classical Artin primitive-root inclusion--exclusion problem.

3. **What project-specific structure might make it solvable?**  
   The exact lcm compositum law and covariance kernel (5.2).

4. **Did nested Kummer fields provide useful cancellation?**  
   Yes in Haar (L^2); no effective power-saving prime theorem followed.

5. **Did the signed (g_z)-sum materially improve over absolute estimates?**  
   At the profinite (L^2) level yes; for the required prime discrepancy no.

6. **Did the signed divisor-supported tail materially improve?**  
   No. Prime residual indices give the exact obstruction (4.3).

7. **Did smoothing help?**  
   It improves zero-height decay but not tower/conductor dependence; not materially.

8. **Did large-sieve-for-Frobenius technology match the family?**  
   No. The closest theorem assumes independent representations and is a sieve theorem, not the required nested weighted discrepancy.

9. **Did zero-density technology match the family?**  
   No. The audited results fix a finite Galois group/degree and penalize intersections.

10. **Did exact-index reorganisation help?**  
    It improves coefficient tails but exposes the primitive-root term, so not analytically enough.

11. **Is there a useful special range of (z)?**  
    No fixed nonempty range was found. Large (z) retains the (t=1) term; (z=1,2) simplify constants only.

12. **Can Level-2 continuation plausibly be attacked without full power-saving prime discrepancy?**  
    Logically yes via a uniform smoothed/local-complex theorem, but no verifiable arithmetic mechanism was found.

13. **What is the strongest new theorem proved in Session 6?**  
    The unconditional profinite lcm-covariance and (L^2)-tail theorem (5.2)–(5.5).

14. **What is the strongest conditional theorem?**  
    The TGRH finite-window prime mean-square bound (5.6).

15. **What is the strongest obstruction?**  
    Exact non-smallness of the signed divisor tail on prime indices plus failure of all audited averaging technologies to bridge the growing nested tower.

16. **What exact missing lemma would Session 7 try to prove?**  
    Counterfactually: an effective prime-side (L^2) equidistribution estimate for the full Kummer observable, uniform to a power-sized level and with a controlled infinite tail.

17. **Is that lemma plausibly approachable with current mathematics?**  
    Not as a project-specific next lemma. It would require new family-Chebotarev/large-sieve technology beyond the matched theorems.

18. **Would proving it be a recognizable mathematical contribution?**  
    Yes, but primarily as a new effective theorem for generalized Artin/Kummer towers, not as a consequence of Pointed Order Zeta.

19. **Would the project still be worth pursuing if the Euler product (Z_a(s,z)) disappeared entirely?**  
    The profinite (L^2) observation is worth preserving, but the active continuation programme would become a generalized-Artin uniformity project rather than this project.

20. **Is there enough substance to justify another research session?**  
    No under the hard standard fixed in Section 1.

---

## 15. Verdict

[
oxed{	extbf{PILOT_KILL}}
]

The pilot has been successful in the adversarial sense: it found exactly where the original object collapses into prior art, proved the finite-level analytic structure, identified the true infinite-tower obstruction, and extracted a clean profinite (L^2) theorem. What remains is a difficult and potentially important generalized-Artin/Chebotarev averaging problem, but the project has not shown a credible residual-index-specific mechanism that makes that problem tractable.

No Session 7 should be opened.

### Standalone pieces worth retaining

- notes/foundational-derivation.md: exact residual-index/Kummer splitting derivation.
- notes/prior-art-matrix.md and notes/literature.md: source-level generalized-Artin collision map.
- notes/analytic-pilot.md: reduction from the Euler product to the centered prime series.
- notes/continuation-proof.md: finite-level centered (L)-function identity, discriminant bounds, and rigorous tower obstruction.
- this note: the lcm covariance/profinite (L^2) theorem and theorem-mismatch audit.
- src/, scripts/, and tests/: a small exact arithmetic engine useful for future residual-index experiments.

These are retained as research notes/code, not as a mandate to continue the Pointed Order Zeta programme.
