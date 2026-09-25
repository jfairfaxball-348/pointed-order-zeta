# Session 3 — Literature Landscape

Date: 2026-09-25

Exit state: **PRIOR_ART_REFRAME**

## Executive conclusion

The proposed \(\mathbf G_m\) programme collides substantially with established generalized-Artin theory.

The collision is strongest at the level of the residual index itself, fixed exact index, divisibility of the index, weighted prime averages, and the Möbius/Kummer degree series. In particular, Felix--Murty (2012), Theorem 1.7, proves under GRH a fixed-base asymptotic for a broad class of functions \(f(i_a(p))\), and its proof identifies the constant as
\[
\sum_{n\ge1}\frac{g(n)}{[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]},
\qquad f=\mathbf 1*g.
\]
For
\[
f_z(n)=n^{-z},\qquad g_z=\mu*f_z,
\]
Session 2 already proved \(|g_z(n)|\le1\) for every real \(z>0\). Thus the proposed mean \(\Delta_a(z)\) is an immediate specialization of Felix--Murty's theorem, subject to their GRH hypothesis. The infinite Möbius/Chebotarev interchange deliberately left unresolved in Session 2 is therefore already handled in the literature for this weight.

Akbary--Fakhari (2024) goes further at the level of constants: it explicitly formulates the generalized Artin problem with the same Kummer-degree series and gives product/character-sum expressions for such constants when the convolution weight is multiplicative. Since \(g_z\) is multiplicative, the project's constant belongs directly to that framework.

Accordingly, the residual-index mean should not be presented as a new “spectrum.” The surviving project, if pursued, should instead test whether the specific infinite-Kummer weighted Euler product
\[
Z_a(s,z)=\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1}
\]
has analytic structure substantially stronger than what follows formally from the already-known weighted prime asymptotic.

## 1. Standard object and terminology

The quantity
\[
I_a(p)=[(\mathbf Z/p\mathbf Z)^\times:\langle a\bmod p\rangle]
\]
is a standard **residual index**. Moree writes it as \(r_g(p)\) and calls \(r_g(p)=t\) the condition that \(g\) is a **near-primitive root of index \(t\)**. Felix--Murty and Akbary--Felix use \(i_a(p)\).

The literature also uses **generalized Artin problem** for weighted questions of the form
\[
\sum_{p\le x}f(i_a(p)).
\]
Pappalardi uses this language in the weighted-Hooley setting, and Akbary--Fakhari uses it explicitly for the general Kummer-degree constant.

## 2. The fixed-\(n\) Kummer criterion

Session 2 established, for \(p\nmid an\),
\[
n\mid I_a(p)\iff p\text{ splits completely in }K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
\]

Felix--Murty, Lemma 2.1, states precisely this equivalence in their notation and introduces it as a classical result. Pappalardi gives the base-\(2\) form in 1995 and attributes the splitting criterion to Dedekind.

Thus the Session-2 derivation was useful as an internal first-principles check, but it is not a new arithmetic mechanism. It is one of the standard bridges between residual index and generalized Artin theory.

For each fixed \(n\), ordinary Chebotarev gives
\[
\operatorname{dens}\{p:n\mid I_a(p)\}=\frac1{[K_n(a):\mathbf Q]}
\]
after omitting the finite exceptional set. No entanglement correction modifies this single-field statement.

## 3. Exact residual index is the near-primitive-root problem

The condition
\[
I_a(p)=t
\]
is the fixed residual-index or near-primitive-root problem.

Wagstaff's generalization of Artin's conjecture gives, on GRH, the density
\[
\delta(a,t)=\sum_{n\ge1}\frac{\mu(n)}{[\mathbf Q(\zeta_{nt},a^{1/(nt)}):\mathbf Q]},
\]
with hypotheses and exceptional cases encoded in the degree formula. Moree's *Near-Primitive Roots* gives a modern source-level treatment for rational \(g\ne-1,0,1\), including explicit Euler-product/correction-factor formulas and perfect-power/sign effects.

Murata had already treated exact residual index in 1991, and Pappalardi quotes this as established background.

Consequently, the full discrete distribution
\[
t\longmapsto\delta_a(t)
\]
is already a recognized generalized-Artin object under the standard GRH hypotheses used for fixed-base asymptotics. Whenever distributional interchange is justified,
\[
\Delta_a(z)=\sum_{t\ge1}\delta_a(t)t^{-z}.
\]
So \(\Delta_a(z)\) is naturally a Dirichlet/Mellin transform of the residual-index distribution, equivalently a Laplace transform of \(\log I_a(p)\).

## 4. General functions of residual index: direct collision

For the base \(2\), Pappalardi (1995) begins from
\[
\sum_{p\le x} f(i_p)=\sum_{n\ge1}g(n)\pi(x,n),
\]
where \(f(m)=\sum_{n\mid m}g(n)\) and \(\pi(x,n)=\#\{p\le x:n\mid i_p\}\). He uses complete splitting in
\[
K_n=\mathbf Q(\zeta_n,2^{1/n})
\]
and effective Chebotarev estimates to establish weighted asymptotics under explicit hypotheses. This is already the same architecture as Session 2.

Felix--Murty (2012), Theorem 1.7, is the controlling fixed-base source. Let
\[
f(n)=\sum_{d\mid n}g(d)
\]
and suppose
\[
|g(n)|\ll\tau_k(n)^r(\log n)^\alpha,\qquad 0\le\alpha<1.
\]
Under GRH for the relevant Dedekind zeta functions, they prove
\[
\sum_{p\le x}f(i_a(p))
=
c_{a,f}\operatorname{li}(x)
+
O_a\!\left(\frac{x}{(\log x)^{2-\varepsilon-\alpha}}\right),
\]
and their proof identifies
\[
c_{a,f}=\sum_{d\ge1}\frac{g(d)}{[\mathbf Q(\zeta_d,a^{1/d}):\mathbf Q]}.
\]

For the project \(f_z(n)=n^{-z}\), Session 2 gives \(|g_z(n)|\le1\) for real \(z>0\). Hence Felix--Murty applies with \(\alpha=0\), yielding under the same GRH hypothesis
\[
\boxed{\Delta_a(z)=\sum_{n\ge1}\frac{g_z(n)}{[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]}\qquad(z>0).}
\]
At \(z=0\), \(\Delta_a(0)=1\) is elementary.

This is the strongest collision found in Session 3.

## 5. Kummer degrees and convergence

Write
\[
a=\pm a_0^h,
\]
where \(h\) is maximal and \(a_0>0\) is not a perfect power, and put
\[
n'=\frac{n}{(n,h)}.
\]

Felix--Murty Proposition 3.3, citing Wagstaff Proposition 4.1, gives
\[
[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]
=
\frac{n'\varphi(n)}{\varepsilon(n)}
=
\frac{n\varphi(n)}{\varepsilon(n)(n,h)},
\]
where \(\varepsilon(n)\in\{1/2,1,2\}\) is an explicit sign/discriminant/\(2\)-adic correction. For positive \(a\),
\[
\varepsilon(n)=
\begin{cases}
2,&2\mid n'\text{ and }d(a_0)\mid n,\\
1,&\text{otherwise}.
\end{cases}
\]
Their Corollary 3.4 gives
\[
[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]\asymp_a n\varphi(n).
\]

Therefore, for real \(z>0\),
\[
\sum_{n\ge1}\frac{|g_z(n)|}{[K_n(a):\mathbf Q]}
\ll_a
\sum_{n\ge1}\frac1{n\varphi(n)}
<\infty.
\]
So the Kummer series is absolutely convergent. Absolute convergence alone does not justify the prime-average interchange; Felix--Murty's theorem supplies that effective step under GRH.

Perucca--Sgobba--Tronto (2021) places such degree calculations in a broader modern Kummer-extension framework over number fields, but Wagstaff's rank-one \(\mathbf Q\)-formula is sharper for this project.

## 6. Entanglement

Lenstra--Moree--Stevenhagen explain Artin correction factors through dependencies among radical/cyclotomic splitting fields. In this language, entanglement means failure of naive independence of local splitting conditions, equivalently nontrivial intersections or finite-index constraints in the associated profinite Galois image. Character sums encode the correction factor.

Akbary--Fakhari extends this product-expression mechanism from density constants to more general sums
\[
\sum_{n\ge1}\frac{g(n)}{\#G(n)}.
\]

Thus entanglement matters when a global Kummer-degree sum is factorized into local factors or when conditions indexed by distinct primes are combined. It does **not** change the individual fixed-\(n\) equivalence.

## 7. The \(z\)-parameter

No inspected primary source was found that foregrounds the complete continuous family
\[
z\longmapsto\Delta_a(z)
\]
in the project's notation. That absence is not evidence of novelty: the family is mechanically contained in a theorem for much more general \(f\).

The correct classification is therefore **IMMEDIATE_COROLLARY**.

Endpoint observations reinforce the collision:

- \(z=0\): the constant weight \(1\), hence \(\Delta_a(0)=1\);
- \(z=1\): reciprocal residual-index weights already occur in older generalized-Artin/recurrence questions;
- \(z\to+\infty\): the pointwise weight tends to the primitive-root indicator, returning to Artin's classical problem, although interchanging this limit with a prime average is separate.

The word **spectrum** is not supported by the sources inspected. At the \(\mathbf G_m\) level, **Dirichlet/Mellin transform of the residual-index distribution** or **Laplace transform of \(\log I_a(p)\)** is more accurate.

## 8. The two-variable Euler product

No direct primary source was located in this audit for the exact product
\[
Z_a(s,z)=\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1}.
\]

Searches used residual index, prescribed/coindex order, near-primitive roots, generalized Artin, weighted Hooley, functions of the residual index, Frobenian functions, Chebotarev Euler products, prime-set zeta functions, Mertens theorems for Chebotarev sets, and weighted products of the form
\[
\prod_p(1-w(p)p^{-s})^{-1}.
\]

Nonappearance of the exact packaging is not evidence of novelty. In \(\Re(s)>1\), forming the product from a bounded prime weight is routine.

Nor is \(p\mapsto I_a(p)^{-z}\) obviously Frobenian in the standard finite-extension sense. Loughran--Matthiesen define a Frobenian function using Frobenius in one finite Galois extension, whereas \(I_a(p)^{-z}\) depends on divisibility across the entire Kummer tower.

Nevertheless, Felix--Murty gives the weighted prime asymptotic for
\[
w_z(p)=I_a(p)^{-z}.
\]
Standard partial summation then controls the \(k=1\) prime sum as \(s\to1^+\), while the \(k\ge2\) terms in
\[
\log Z_a(s,z)
=
\sum_p\sum_{k\ge1}\frac{w_z(p)^k}{kp^{ks}}
\]
are absolutely regular near the real boundary. Merely identifying \(\Delta_a(z)\) as the leading logarithmic coefficient is therefore unlikely to be a distinct research layer.

By contrast, these stronger questions were not located as direct consequences of the inspected sources:

- holomorphic/nonvanishing behavior of
  \[
  H_a(s,z)=Z_a(s,z)\zeta(s)^{-\Delta_a(z)};
  \]
- continuation of \(H_a(s,z)\) into a half-plane crossing \(\Re(s)=1\);
- uniform or holomorphic dependence on complex \(z\);
- convergent factorization into Dedekind or Artin \(L\)-functions from the infinite Kummer tower;
- possible natural boundaries or additional singularities.

## 9. Frobenian/Chebotarev comparison

Loughran--Matthiesen, Definition 2.1 and Lemma 2.4, provides the finite-Galois comparison. For a Frobenian weight \(\rho\) of mean \(m(\rho)\), they obtain prime-sum and reciprocal-prime asymptotics with leading coefficient \(m(\rho)\), together with a Mertens-type product whose exponent is \(m(\rho)\).

Arango-Piñeros--Keliher--Keyes prove the analogous Mertens theorem for prime sets defined by Chebotarev conjugacy conditions.

Thus “density/mean becomes an Euler-product exponent” is standard finite-Chebotarev/Frobenian technology. These sources do not directly collapse the infinite-tower problem.

## 10. What survives

The following do **not** survive as candidate novelty at the \(\mathbf G_m\) level:

1. residual index as the core arithmetic statistic;
2. fixed-\(n\) Kummer splitting;
3. densities for prescribed residual index;
4. the divisor/Möbius expansion for general \(f(I_a(p))\);
5. the Kummer-degree constant \(\sum_n(\mu*f)(n)/[K_n(a):\mathbf Q]\);
6. existence/formula for \(\Delta_a(z)\) for fixed real \(z>0\) under the standard GRH hypothesis;
7. the general role of entanglement correction factors.

The strongest potentially surviving question is:

> After taking the generalized-Artin mean \(\Delta_a(z)\) as known input, does the normalized infinite-Kummer weighted Euler product
> \[
> H_a(s,z)=Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
> \]
> possess a genuinely nontrivial analytic continuation, nonvanishing region, complex-\(z\) structure, or Kummer-tower \(L\)-function factorization that is not already a formal consequence of the weighted prime asymptotic?

This requires a new prior-art check focused specifically on analytic Euler products over infinite Galois towers before any novelty inference.

## 11. Verdict

**PRIOR_ART_REFRAME**

The project should not continue under the thesis that the continuous residual-index mean is a new Artin--Kummer “spectrum.” Layers A--C have collided directly or as immediate corollaries with known theory.

Session 4 may proceed only in reframed form, with Felix--Murty Theorem 1.7 treated as controlling input rather than something to reprove. Any computational pilot should test analytic behavior of the normalized Euler product and consistency with the already-known generalized-Artin constant, not rediscover \(\Delta_a(z)\) or the residual-index distribution.

No priority or novelty claim is made for the surviving analytic question.
