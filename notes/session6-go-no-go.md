# Session 6 — Adversarial Go / No-Go Gate

Date: 2026-09-26

Exit state: **PILOT_KILL**.

Sessions 3–5 remain controlling. This session does not alter the frozen object, undo the prior-art conclusions, weaken the Session-4 Level-1 result, or reinterpret the Session-5 method obstruction as a non-continuation theorem.

Unless stated otherwise, the theorem-driven scope is a fixed positive non-perfect-power integer \(a>1\) and a fixed real \(z>0\).

## 1. Success and kill standards fixed before the attack

A **GREEN LIGHT** requires at least one of the following.

1. A new Level-2 or Level-3 continuation theorem.
2. A power-saving centered discrepancy theorem.
3. A strong smoothed power-saving theorem plus a rigorous route from it to continuation.
4. A precise tower-averaged Chebotarev conjecture/theorem target together with a credible mechanism specific to the residual-index/Kummer tower.
5. A different object, still closely tied to residual index/Kummer structure, supporting a non-routine theorem programme not already contained in generalized-Artin theory.

An unanswered question, finite-level continuation, or a generic request for stronger Chebotarev/large-sieve uniformity does not satisfy this standard.

A **KILL** results if none of the items above survives and the remaining task is essentially a new theorem about generic/infinite-family Artin or Chebotarev uniformity for which the Pointed Order Zeta construction contributes no effective leverage.

That is the standard used below.

---

## 2. Exact centered discrepancy decomposition

Write
\[
\pi_a^\circ(x)=\#\{p\le x:p\nmid a\},
\qquad
\pi_n^I(x)=\#\{p\le x:p\nmid a,\ n\mid I_a(p)\},
\]
and
\[
d_n=[K_n(a):\mathbf Q],
\qquad
g_z=\mu*(n\mapsto n^{-z}).
\]

Under the same source-matched hypotheses for which
\[
\Delta_a(z)=\sum_{n\ge1}\frac{g_z(n)}{d_n},
\]
the pointwise finite divisor identity gives, for every \(N\ge1\),
\[
\boxed{
D_z^\circ(x)
=
\sum_{n\le N}g_z(n)
\left(
\pi_n^I(x)-\frac{\operatorname{li}(x)}{d_n}
\right)
+
\mathcal T_z(x;N)
-
\operatorname{li}(x)\sum_{n>N}\frac{g_z(n)}{d_n}
+
\Delta_a(z)\bigl(\operatorname{li}(x)-\pi_a^\circ(x)\bigr),
}
\tag{2.1}
\]
where
\[
\boxed{
\mathcal T_z(x;N)
=
\sum_{\substack{p\le x\\p\nmid a}}
\sum_{\substack{n\mid I_a(p)\\n>N}}g_z(n).
}
\tag{2.2}
\]

Thus the four pieces are exactly:

- the signed finite-level Kummer sum;
- the divisor-supported prime tail;
- the Kummer-degree series tail;
- the PNT/omitted-prime normalization correction.

Equivalently, centering first by \(\pi_a^\circ(x)\),
\[
D_z^\circ(x)
=
\sum_{n\le N}g_z(n)
\left(
\pi_n^I(x)-\frac{\pi_a^\circ(x)}{d_n}
\right)
+
\mathcal T_z(x;N)
-
\pi_a^\circ(x)\sum_{n>N}\frac{g_z(n)}{d_n}.
\tag{2.3}
\]

For \(p\nmid an\), \(\pi_n^I\) is the completely-split counting function for \(K_n(a)\). Session 5 proved that changing to the complete-splitting convention introduces only the fixed finite exceptional correction already recorded there: the only possible accidental \(p\mid n\) contribution is the \(n=2,p=2\) case, together with the fixed omission of primes dividing \(a\). No hard term is hidden in this correction.

Equation (2.1) is the sharp truncation identity used in this session.

---

## 3. Signed finite-level sum

Under tower GRH, Session 5 gives
\[
E_n(x):=
\pi_n^I(x)-\frac{\operatorname{li}(x)}{d_n}
=
O_a(\sqrt{x}\log(nx))
\]
up to the finite convention above. The triangle inequality gives
\[
\sum_{n\le N}|g_z(n)E_n(x)|
\ll_a
\sqrt{x}N\log(Nx).
\]

The signs of \(g_z\) are Möbius-like on squarefree integers:
\[
g_z(n)
=
(-1)^{\omega(n)}n^{-z}\prod_{\ell\mid n}(\ell^z-1).
\]
But the discrepancies \(E_n(x)\) are not multiplicative in \(n\), and the finite-level \(L\)-functions are coupled through field intersections. Hence the scalar identity
\[
\sum_{n\ge1}\frac{g_z(n)}{n^w}
=
\frac{\zeta(w+z)}{\zeta(w)}
\]
does not transfer to
\[
\sum_n g_z(n)E_n(x).
\]

Nestedness does, however, create an exact covariance law. This is the strongest project-specific positive result of Session 6 and is proved in Section 5.

---

## 4. Signed divisor-supported tail

For a positive integer \(m\), set
\[
R_{z,N}(m)
=
\sum_{\substack{n\mid m\\n>N}}g_z(n).
\]
The divisor identity gives
\[
\boxed{
R_{z,N}(m)
=
m^{-z}
-
\sum_{\substack{n\mid m\\n\le N}}g_z(n),
}
\tag{4.1}
\]
and divisor pairing gives
\[
\boxed{
R_{z,N}(m)
=
\sum_{\substack{d\mid m\\d<m/N}}g_z(m/d).
}
\tag{4.2}
\]

These formulas preserve all signs. They also give a sharp obstruction to any pointwise signed-tail saving. If \(q>N\) is prime, then
\[
R_{z,N}(q)=g_z(q)=q^{-z}-1,
\]
and therefore
\[
\boxed{|R_{z,N}(q)|\to1.}
\tag{4.3}
\]

Thus the signed tail is not intrinsically small. Any useful saving must use the distribution of residual indices over primes, not cancellation inside every truncated divisor sum.

The same first-level obstruction appears in the valuation expansion
\[
m^{-z}
=
\prod_\ell
\left(
1+\sum_{1\le k\le v_\ell(m)}g_z(\ell^k)
\right),
\tag{4.4}
\]
because
\[
g_z(\ell)=\ell^{-z}-1
\]
does not decay with \(\ell\). Reorganising by squarefree kernel, radical, powerful part, or valuation vector therefore does not eliminate the problem.

Rankin tricks, Perron inversion in the divisor variable, divisor pairing, and smooth/rough decomposition can redistribute the tail but cannot remove (4.3).

---

## 5. Nested Kummer tower: exact profinite \(L^2\) structure

This is the strongest genuinely project-specific mechanism found.

Let
\[
L_a=\bigcup_{n\ge1}K_n(a),
\qquad
G_a=\operatorname{Gal}(L_a/\mathbf Q),
\]
with normalized Haar measure \(\mu\), and let
\[
U_n=\operatorname{Gal}(L_a/K_n(a)).
\]

### 5.1 Exact lcm compositum law

For all \(m,n\ge1\),
\[
\boxed{
K_m(a)K_n(a)=K_{\operatorname{lcm}(m,n)}(a).
}
\tag{5.1}
\]

The inclusion from left to right is immediate. Conversely, if \(L=\operatorname{lcm}(m,n)\), then
\[
\gcd(L/m,L/n)=1.
\]
Bézout therefore recovers both \(\zeta_L\) from \(\zeta_m,\zeta_n\) and \(a^{1/L}\) from \(a^{1/m},a^{1/n}\). Hence equality holds.

It follows that
\[
U_m\cap U_n=U_{\operatorname{lcm}(m,n)}
\]
and
\[
\mu(U_n)=\frac1{d_n}.
\]

Put
\[
X_n=\mathbf1_{U_n},
\qquad
Y_n=X_n-\frac1{d_n}.
\]
Then
\[
\boxed{
\langle Y_m,Y_n\rangle_{L^2(G_a)}
=
\frac1{d_{\operatorname{lcm}(m,n)}}
-
\frac1{d_md_n}.
}
\tag{5.2}
\]

This is an exact covariance law, not a heuristic.

### 5.2 Unconditional Haar \(L^2\) convergence

For positive non-perfect-power \(a\),
\[
d_n\gg_a n\varphi(n).
\]
Since \(|g_z(n)|\le1\),
\[
\sum_{m,n\ge1}
\frac{|g_z(m)g_z(n)|}{d_{\operatorname{lcm}(m,n)}}
\le
\sum_{\ell\ge1}
\frac{\tau(\ell)^2}{d_\ell}
<\infty.
\tag{5.3}
\]
The last series converges because \(d_\ell\gg_a \ell\varphi(\ell)\) and the divisor function has sub-polynomial growth.

Therefore
\[
\boxed{
F_z(\sigma)
=
\sum_{n\ge1}g_z(n)
\left(
\mathbf1_{U_n}(\sigma)-\frac1{d_n}
\right)
}
\tag{5.4}
\]
converges unconditionally in \(L^2(G_a,\mu)\).

More quantitatively, for every \(\varepsilon>0\),
\[
\boxed{
\left\|
\sum_{n>N}g_z(n)Y_n
\right\|_2^2
\ll_{a,\varepsilon}
N^{-1+\varepsilon},
\qquad
\left\|
\sum_{n>N}g_z(n)Y_n
\right\|_2
\ll_{a,\varepsilon}
N^{-1/2+\varepsilon}.
}
\tag{5.5}
\]

Since
\[
\sum_{n\ge2}\mu(U_n)
=
\sum_{n\ge2}\frac1{d_n}
<\infty,
\]
Borel--Cantelli implies that Haar-almost every \(\sigma\) belongs to only finitely many \(U_n\). For such \(\sigma\), the set
\[
S(\sigma)=\{n:\sigma\in U_n\}
\]
is finite, divisor-closed, and lcm-closed. If \(I(\sigma)\) is the lcm of its elements, then \(I(\sigma)\in S(\sigma)\), and divisor closure shows that \(S(\sigma)\) is exactly the divisor set of \(I(\sigma)\). Thus
\[
\sum_n g_z(n)\mathbf1_{U_n}(\sigma)
=
I(\sigma)^{-z}
\]
almost everywhere.

So (5.4) is genuinely a centered residual-index observable on the profinite Kummer image.

### 5.3 Prime-side finite-window theorem under TGRH

The Haar result does not itself imply effective equidistribution of prime Frobenius elements against observables whose level grows with \(x\).

Still, under tower GRH one can expand a finite-window square and use (5.2) together with effective Chebotarev at the lcm levels. For \(1\le N<L\),
\[
\boxed{
\sum_{\substack{p\le x\\p\nmid a}}
\left|
\sum_{N<n\le L}
g_z(n)
\left(
\mathbf1_{n\mid I_a(p)}-\frac1{d_n}
\right)
\right|^2
\ll_{a,z,\varepsilon}
\operatorname{li}(x)N^{-1+\varepsilon}
+
\sqrt{x}\,L^2\log(Lx),
}
\tag{5.6}
\]
up to the fixed exceptional/PNT-normalization terms.

This is the strongest conditional theorem obtained in Session 6. It verifies that the covariance structure survives at finite prime level, but the error pays for all pairwise lcm levels. It becomes useless when \(L\) is large enough to approximate the full divisor tail. Cauchy--Schwarz therefore does not turn (5.6) into the desired power-saving first moment.

Most importantly, the same covariance mechanism survives as \(z\to\infty\), when \(g_z(n)\to\mu(n)\). It is therefore already present in the inclusion--exclusion architecture of the classical Artin primitive-root problem. The \(L^2\) theorem does not demonstrate that finite \(z\), or the Euler-product packaging, makes the prime problem easier.

This is the decisive failure of green-light criterion D.

---

## 6. Smoothing

For a smooth compactly supported \(W\),
\[
D_{z,W}(X)
=
\sum_{p\nmid a}
\left(I_a(p)^{-z}-\Delta_a(z)\right)
W(p/X)
\]
has the exact expansion
\[
D_{z,W}(X)
=
\sum_{n\ge1}g_z(n)
\left[
\sum_{\substack{p\nmid a\\n\mid I_a(p)}}W(p/X)
-
\frac1{d_n}\sum_{p\nmid a}W(p/X)
\right].
\tag{6.1}
\]

Smoothing helps the vertical variable in an explicit formula because the Mellin transform of \(W\) decays rapidly. It does not remove the conductor/discriminant dependence in \(n\). The finite-level GRH error remains of square-root size with logarithmic \(n\)-dependence, and mean-square expansions again introduce lcm composita.

A sufficiently uniform family of smoothed power-saving estimates would imply continuation: a dyadic partition of unity plus estimates stable under Mellin twists and controlled by finitely many seminorms of \(W\) would permit Mellin continuation/contour shifting. A power saving for one isolated \(W\) would not suffice.

No theorem matched in Sections 7–8 supplies such a uniform smoothed tower estimate. Smoothing therefore does not materially improve the go/no-go case.

---

## 7. Large sieve for Frobenius: theorem matching

### 7.1 Zywina, Theorem 3.3

Zywina's Theorem 3.3 assumes a collection of **independent** Galois representations indexed by pairwise coprime ideals, with finite image groups of polynomial size and ramification only in a fixed finite set plus primes dividing the index. In Definition 3.2, independence is explicitly equivalent to linear disjointness of the associated fields.

Prime Kummer levels superficially fit the size and ramification pattern:
\[
|G_\ell|\asymp\ell^2,
\qquad
\operatorname{Ram}(K_\ell)\subseteq\{\ell\}\cup\{p:p\mid a\}.
\]
After finite entanglement is isolated, prime-index quotients are the closest available match.

But the Session-6 quantity is a signed weighted sum over **all** \(n\), including composite levels and the deliberate nested relations
\[
m\mid n\Longrightarrow K_m(a)\subseteq K_n(a).
\]
Zywina's theorem is a sieve bound for primes satisfying simultaneous local membership conditions. It does not estimate
\[
\sum_{n\le N}g_z(n)E_n(x)
\]
or the divisor-supported tail.

**Theorem verdict:** partial structural match; no solution of the target.

### 7.2 Kowalski's large sieve for Frobenius

Kowalski's 2006 large sieve concerns Frobenius conjugacy classes in coherent/lisse-sheaf systems over finite-field parameter spaces with monodromy hypotheses. The varying object is a geometric family over a base variety.

The deterministic sequence
\[
K_n(a)/\mathbf Q
\]
is not such a family. No matching theorem statement yields an average over \(n\).

**Theorem verdict:** nearby technology; hypothesis mismatch.

### 7.3 Murty--Petersen Bombieri--Vinogradov theorem

Murty--Petersen obtain a mixed Bombieri--Vinogradov theorem in which arithmetic-progression moduli vary around a fixed number-field splitting condition. The averaging variable is the progression modulus, not a deterministic family of varying Kummer extensions.

**Theorem verdict:** wrong averaging variable.

### Large-sieve conclusion

No audited large-sieve theorem produces the required cancellation across the full Kummer index. A Session-7 plan invoking “large sieve for Frobenius” would require the invention of a materially new theorem, not the application of an existing one.

---

## 8. Zero-density and explicit-formula matching

### 8.1 Thorner--Zaman, Theorem 1.1

Thorner--Zaman fix a nontrivial finite group \(G\) and average over Galois extensions \(K/\mathbf Q\) satisfying
\[
\operatorname{Gal}(K/\mathbf Q)\cong G.
\]
Their theorem explicitly contains the intersection multiplicity
\[
\mathfrak m_{\mathfrak F}(Q)
=
\max_K
\#\{K':K\cap K'\ne\mathbf Q\}.
\]

The Kummer tower has the opposite geometry:

- the Galois group varies with \(n\);
- its order \(d_n\asymp n\varphi(n)\) grows;
- intersections are systematic and large because the fields are nested.

A singleton application destroys the family average and gives no advantage over the GRH Chebotarev estimate already used.

**Theorem verdict:** clear mismatch.

### 8.2 Lemke Oliver--Smith, Theorem 1.9 and Proposition 1.10

Their averaged Chebotarev framework controls most extensions of fixed degree/group after excluding fields containing specified bad subextensions. The effective range has degree-dependent powers of \(\log\Delta_K\), and the paper explicitly records common subfields as an averaging obstruction.

Our family has unbounded degree, forced common subfields, and only one deterministic tower from which no exceptional subfamily can be discarded.

**Theorem verdict:** no usable match.

### 8.3 Explicit formulas and averaged zeros

Each fixed \(K_n\) already has the explicit-formula control isolated in Session 5. Smoothing damps high zeros but does not give cancellation between the zero sets belonging to different \(n\). No audited zero-density theorem treats precisely this nested varying-degree family with useful dependence on \(n\).

**Conclusion:** zero-density technology does not materially improve on tower GRH for the Session-6 target.

---

## 9. Alternative weight expansions

### 9.1 Exact-index reorganisation

Exactly,
\[
I_a(p)^{-z}
=
\sum_{t\ge1}t^{-z}\mathbf1_{I_a(p)=t}.
\tag{9.1}
\]
The coefficient tail is excellent:
\[
\sum_{t>N}t^{-z}\mathbf1_{I=t}
\le N^{-z}
\]
pointwise.

But the first term is
\[
\mathbf1_{I_a(p)=1},
\]
the primitive-root indicator. Its fixed-base prime-distribution problem is the classical Artin/Hooley problem. Fixed \(t>1\) is the near-primitive-root problem and is itself obtained by Möbius inclusion--exclusion over the same Kummer tower.

Thus exact-index reorganisation trades the large-divisor tail for hard low-\(t\) discrepancies.

**Verdict:** better coefficients; no stronger analytic theorem.

### 9.2 Large \(z\)

For every fixed \(z>0\),
\[
I^{-z}
=
\mathbf1_{I=1}
+
\sum_{t\ge2}t^{-z}\mathbf1_{I=t}.
\tag{9.2}
\]
The tail is numerically small for large \(z\), but the primitive-root coefficient remains exactly \(1\). No fixed \(z_0\) removes the hardest term.

**Verdict:** no useful continuation range \(z>z_0\) was found.

### 9.3 \(z=1\) and \(z=2\)

For squarefree \(n\),
\[
g_1(n)=\mu(n)\frac{\varphi(n)}n.
\]
Using
\[
d_n=\frac{n\varphi(n)}{\varepsilon_a(n)},
\]
one gets
\[
\boxed{
\frac{g_1(n)}{d_n}
=
\varepsilon_a(n)\frac{\mu(n)}{n^2}.
}
\tag{9.3}
\]

For squarefree \(n\),
\[
g_2(n)=\mu(n)\prod_{p\mid n}(1-p^{-2}),
\]
and
\[
\boxed{
\frac{g_2(n)}{d_n}
=
\varepsilon_a(n)\frac{\mu(n)}{n^2}
\prod_{p\mid n}\left(1+\frac1p\right).
}
\tag{9.4}
\]

These simplify the **mean constants**. The centered error \(E_n(x)\) does not carry the factor \(1/d_n\), so these identities do not improve tower convergence.

### 9.4 Perron, Laplace, valuation and profinite bases

The profinite basis is the only alternative that yielded a genuinely stronger norm: the Haar \(L^2\) theorem of Section 5. Perron, Laplace, dyadic, or valuation expansions retain the non-decaying first divisibility layer. No basis tested gives an exact prime-side expansion with a summable effective norm.

---

## 10. Level 2 without a global sharp power saving

A global bound
\[
D_z^\circ(x)=O(x^\theta),\qquad \theta<1,
\]
is sufficient but not logically necessary for continuation.

Pseudofunction, pseudomeasure, distributional boundary, or Tauberian methods can prove boundary regularity from weaker hypotheses. But boundary regularity is not itself holomorphic continuation to an open region left of \(\Re(s)=1\).

Conversely, a local continuation of \(Q_a^\circ\) through a strip, together with ordinary polynomial vertical control, would permit a Mellin contour shift and produce power savings for a rich class of smooth dyadic prime sums. Hence a **uniform smoothed power-saving theorem** is a fair proxy for a credible local-complex route.

No arithmetic hypothesis of this type is currently verifiable for the residual-index sequence. Abstract functional analysis therefore does not count as a green-light mechanism.

---

## 11. Lower-bound and natural-scale audit

No theorem obtained here rules out a power saving.

Fixed finite Kummer levels have the usual explicit-formula oscillations associated with zeta zeros and are expected to fluctuate on a square-root scale under GRH. This is compatible with a target
\[
O(x^{1-\delta})
\]
for any \(\delta<1/2\).

Accordingly:

- no natural boundary is inferred;
- no impossibility of continuation is claimed;
- \(x^{1/2+o(1)}\) is at most a heuristic natural scale for the full discrepancy.

The project is killed because no credible project-specific attack route survives, not because the desired discrepancy was proved false.

---

## 12. Technology audit summary

Sources actually used in Session 6:

- D. Zywina, *The Large Sieve and Galois Representations*, Theorem 3.3 — independent representations / linearly disjoint fields; no all-\(n\) nested weighted discrepancy.
- E. Kowalski, *The large sieve, monodromy and zeta functions of curves* — geometric finite-field Frobenius family, not the deterministic Kummer tower.
- J. Thorner and A. Zaman, *A Zero Density Estimate for Dedekind Zeta Functions*, Theorem 1.1 — fixed finite Galois group plus explicit intersection multiplicity; mismatched to nested growing degree.
- R. J. Lemke Oliver and A. Smith, *Faithful Artin induction and the Chebotarev density theorem*, Theorem 1.9 and Proposition 1.10 — fixed-degree/group “most fields” technology with common-subfield obstruction.
- M. R. Murty and K. L. Petersen, *A Bombieri--Vinogradov theorem for all number fields* — averages progression moduli around a fixed splitting problem, not the Kummer level.
- Hooley and the modern Artin literature — the \(t=1\) exact-index term remains the classical fixed-base primitive-root problem; average-over-base results do not supply the needed fixed-\(a\) power saving.

No source audited supplies a theorem that closes (2.1).

---

## 13. Strongest positive and negative results

### Strongest unconditional theorem proved in Session 6

The lcm-covariance/Haar-\(L^2\) theorem (5.1)–(5.5): the nested Kummer tower supports an exact centered covariance kernel and a residual-index observable whose Haar \(L^2\) tail is
\[
O_{a,\varepsilon}(N^{-1/2+\varepsilon}).
\]

### Strongest conditional theorem proved in Session 6

Under tower GRH, the finite-window prime mean-square estimate (5.6):
\[
\sum_{p\le x}
\left|
\sum_{N<n\le L}
g_z(n)(\mathbf1_{n\mid I_a(p)}-1/d_n)
\right|^2
\ll
\operatorname{li}(x)N^{-1+\varepsilon}
+
\sqrt{x}L^2\log(Lx),
\]
with the standard finite corrections.

### Strongest obstruction

The exact signed divisor tail satisfies
\[
R_{z,N}(q)=q^{-z}-1
\]
for every prime \(q>N\), so it has no uniform pointwise saving. At the same time, transferring the Haar \(L^2\) saving to primes forces effective Chebotarev at growing lcm levels, and the audited averaging theorems do not match that task.

### Strongest project-specific source of cancellation

The lcm covariance / profinite Haar-\(L^2\) structure.

### Strongest reason to continue

That \(L^2\) theorem is mathematically clean and may be useful as a standalone probabilistic/profinite model for generalized-Artin statistics.

### Strongest reason to kill

The missing bridge is exactly an effective prime-equidistribution theorem for a growing nested Kummer tower. The same \(L^2\) structure persists at the primitive-root endpoint \(g=\mu\), so Pointed Order Zeta has not supplied a distinctive mechanism that makes the hard generalized-Artin problem tractable.

This fails the Session-6 green-light standard.

---

## 14. Final adversarial questions

1. **What exact mathematical problem remains?**  
   Prove a power-saving prime discrepancy, or a uniform smoothed substitute, by effectively transferring the Haar \(L^2\) Kummer cancellation to Frobenius primes at growing tower depth.

2. **Is it actually specific to residual indices/Kummer towers?**  
   Its notation is specific, but its hard analytic core is not sufficiently so: at \(z\to\infty\) it contains the classical primitive-root inclusion--exclusion problem.

3. **What project-specific structure might make it solvable?**  
   The exact lcm compositum law and covariance kernel (5.2).

4. **Did nested Kummer fields provide useful cancellation?**  
   Yes in Haar \(L^2\); no effective power-saving prime theorem followed.

5. **Did the signed \(g_z\)-sum materially improve over absolute estimates?**  
   At the profinite \(L^2\) level yes; for the required prime discrepancy no.

6. **Did the signed divisor-supported tail materially improve?**  
   No. Prime residual indices give the exact obstruction (4.3).

7. **Did smoothing help?**  
   It improves zero-height decay but not tower/conductor dependence; not materially.

8. **Did large-sieve-for-Frobenius technology match the family?**  
   No. The closest theorem assumes independent representations and is a sieve theorem, not the required nested weighted discrepancy theorem.

9. **Did zero-density technology match the family?**  
   No. The audited results fix finite groups/degrees and penalize intersections.

10. **Did exact-index reorganisation help?**  
    It improves coefficient tails but exposes the primitive-root term.

11. **Is there a useful special range of \(z\)?**  
    No fixed nonempty range was found. Large \(z\) keeps the \(t=1\) term; \(z=1,2\) simplify constants only.

12. **Can Level-2 continuation plausibly be attacked without full power-saving prime discrepancy?**  
    Logically yes through a uniform smoothed/local-complex theorem, but no verifiable arithmetic mechanism was found.

13. **What is the strongest new theorem proved in Session 6?**  
    The unconditional profinite lcm-covariance and Haar-\(L^2\)-tail theorem.

14. **What is the strongest conditional theorem?**  
    The tower-GRH finite-window prime mean-square estimate (5.6).

15. **What is the strongest obstruction?**  
    Exact non-smallness of the signed divisor tail on prime indices plus the failure of audited averaging technology to bridge the growing nested tower.

16. **What exact missing lemma would Session 7 try to prove?**  
    Counterfactually: a prime-side \(L^2\) equidistribution estimate for the full Kummer observable, uniform to a power-sized level and with a controlled infinite tail.

17. **Is that lemma plausibly approachable with current mathematics?**  
    Not as a project-specific next lemma. It would require materially new family-Chebotarev/large-sieve technology.

18. **Would proving it be a recognizable mathematical contribution?**  
    Yes, but primarily as a new effective theorem for generalized Artin/Kummer towers, not as a consequence of Pointed Order Zeta.

19. **Would the project still be worth pursuing if the Euler product \(Z_a(s,z)\) disappeared entirely?**  
    The profinite \(L^2\) observation is worth retaining, but the active continuation problem would become a generalized-Artin uniformity project rather than this project.

20. **Is there enough substance to justify another research session?**  
    No under the hard standard fixed in Section 1.

---

## 15. Final verdict

\[
\boxed{\textbf{PILOT\_KILL}}
\]

The pilot succeeded as an adversarial investigation: it found where the original object collapses into prior art, proved the finite-level analytic structure, isolated the true infinite-tower obstruction, and extracted a clean profinite \(L^2\) theorem. What remains is a difficult and potentially important generalized-Artin/Chebotarev averaging problem, but no credible residual-index-specific mechanism makes it tractable enough to justify continued investment in this project.

No Session 7 should be opened.

### Standalone material worth retaining

- notes/foundational-derivation.md — exact residual-index/Kummer splitting derivation.
- notes/prior-art-matrix.md and notes/literature.md — source-level generalized-Artin collision map.
- notes/analytic-pilot.md — reduction from the Euler product to the centered prime series.
- notes/continuation-proof.md — finite-level centered \(L\)-function identity, discriminant bounds, and rigorous tower obstruction.
- this note — the lcm covariance/Haar-\(L^2\) theorem and the theorem-mismatch audit.
- src/, scripts/, tests/ — exact arithmetic and analytic-pilot code.

These remain useful research notes and code, not a mandate to continue Pointed Order Zeta.
