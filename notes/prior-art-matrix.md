# Session 3 — Prior-Art Matrix

Date: 2026-09-25

Exit state: **PRIOR_ART_REFRAME**

This matrix audits the exact Session-2 structure, not merely similar terminology.

Collision labels:

- **DIRECT_COLLISION** — essentially the same mathematical statement/object is already present.
- **IMMEDIATE_COROLLARY** — the project statement follows mechanically from a more general theorem.
- **PARTIAL_COLLISION** — a substantial component is known, but a real mathematical gap remains.
- **NEARBY_ONLY** — conceptually related without implying the project statement.
- **UNCLEAR** — theorem matching could not be established confidently.

The strongest conclusion is that layers A--C, and much of the Kummer-constant structure in F, are established generalized-Artin theory. The exact two-variable Euler product was not located, but its definition in \(\Re(s)>1\) is packaging and its leading real singular exponent is strongly constrained by the already-known weighted-prime asymptotic.

## A--G layer verdict

| Layer | Verdict | Source-level reason |
|---|---|---|
| **A. Residual-index distribution** | **DIRECT_COLLISION** | Residual index \(i_a(p)\) / \(r_g(p)\) is standard. Exact index \(I_a(p)=t\) is the near-primitive-root problem; Wagstaff/Moree give the GRH density as a Kummer-degree Möbius sum. Divisibility \(n\mid I_a(p)\) is a classical complete-splitting criterion. |
| **B. General \(f(I_a(p))\) averages** | **DIRECT_COLLISION** | Pappalardi treats weighted sums for base \(2\); Felix--Murty Theorem 1.7 treats fixed \(a\) and a broad class of \(f\), using precisely the divisor/Möbius expansion and \(K_n(a)=\mathbf Q(\zeta_n,a^{1/n})\). |
| **C. \(f_z(n)=n^{-z}\)** | **IMMEDIATE_COROLLARY** | For real \(z>0\), Session 2 gives \(|g_z(n)|\le1\), so Felix--Murty Theorem 1.7 applies with \(\alpha=0\). Under their GRH hypothesis, \(\Delta_a(z)\) exists and equals the Session-2 degree series. At \(z=0\), \(\Delta_a(0)=1\) is elementary. |
| **D. \(Z_a(s,z)\)** | **PARTIAL_COLLISION** | No direct source for the exact product was located. General Frobenian/Chebotarev Euler-product theory covers finite Galois quotients, while \(I_a(p)^{-z}\) depends on the entire Kummer tower. In \(\Re(s)>1\), however, the product itself is straightforward packaging once the weight is given. |
| **E. Varying singularity exponent / “spectrum”** | **PARTIAL_COLLISION** | For finite Frobenian weights, mean-value exponents in Mertens/Euler products are standard. For the project weight, Felix--Murty already gives a prime asymptotic strong enough to make a \(\Delta_a(z)\log(1/(s-1))\) leading term a standard real-variable consequence by partial summation. A stronger holomorphic/two-variable theorem was not located. |
| **F. Kummer tower / \(L\)-function factorisation** | **PARTIAL_COLLISION** | Akbary--Fakhari give product expressions, including entanglement corrections, for constants \(\sum g(n)/[K_n:\mathbf Q]\) with multiplicative \(g\), directly covering \(g_z\). Lenstra--Moree--Stevenhagen give the profinite/character-sum entanglement framework. No Artin/Dedekind-\(L\) factorisation or continuation of the exact \(Z_a(s,z)\) was located. |
| **G. Pointed algebraic-group / 1-motive generalisation** | **NEARBY_ONLY / NOT AUDITED TO NOVELTY STANDARD** | Division-field and elliptic analogues exist, but the Session-3 scope prohibited a full 1-motive/abelian-variety audit. No novelty inference is made. |

## Significant source matches

### Felix--Murty (2012) — controlling collision for B and C

**Authors:** Adam Tyler Felix; M. Ram Murty  
**Title:** *A Problem of Fomenko's Related to Artin's Conjecture*  
**Publication:** International Journal of Number Theory 8(7) (2012), 1687--1723  
**DOI:** 10.1142/S1793042112500984

**Exact locations inspected**

- §1.4, **Theorem 1.7**.
- §2, **Lemma 2.1**.
- §3.2, **Proposition 3.3** and **Corollary 3.4**.
- §6.2, proof of Theorem 1.7, especially equations (6.6)--(6.10).

They define
\[
i_a(p)=[(\mathbf Z/p\mathbf Z)^\times:\langle a\bmod p\rangle],
\]
the same object as \(I_a(p)\).

Lemma 2.1 is introduced as a **classical result** and states, for fixed \(d\), that
\[
d\mid i_a(p)
\iff
p\text{ splits completely in }\mathbf Q(\zeta_d,a^{1/d}),
\]
away from the usual exceptional primes.

Theorem 1.7 assumes GRH for the relevant Kummer fields and assumes
\[
f(n)=\sum_{d\mid n}g(d),
\qquad
|g(n)|\ll\tau_k(n)^r(\log n)^\alpha,
\quad
0\le\alpha<1.
\]
It proves
\[
\sum_{p\le x}f(i_a(p))
=
c_{a,f}\operatorname{li}(x)
+
O_a\!\left(
\frac{x}{(\log x)^{2-\varepsilon-\alpha}}
\right).
\]
The proof identifies
\[
c_{a,f}
=
\sum_{d\ge1}
\frac{g(d)}
{[\mathbf Q(\zeta_d,a^{1/d}):\mathbf Q]}.
\]

For
\[
f_z(n)=n^{-z},
\qquad
g_z=\mu*f_z,
\]
Session 2 proved
\[
|g_z(n)|\le1
\qquad(z>0).
\]
Hence Theorem 1.7 applies immediately with \(\alpha=0\) in the paper's standing positive-base setup. This supplies the missing infinite interchange, conditionally on GRH, and gives the exact proposed constant.

**Hypothesis nuance:** the paper opens by fixing a natural number \(a>1\). Its Kummer-degree Proposition 3.3 explicitly treats arbitrary integers \(a\ne0,\pm1\), including \(a<0\), and later generalized-Artin literature phrases the framework for integer \(a\). This audit did not locate a separate theorem-text statement extending Felix--Murty Theorem 1.7 itself to negative \(a\). Therefore the direct theorem match for \(\Delta_a(z)\) is recorded as fully verified for positive bases; the negative-base weighted asymptotic remains a source-matching item. This does not rescue novelty of the \(\mathbf G_m\) construction.

**Layers:** A explicit; B explicit; C immediate consequence for the source-matched positive-base case; F partial.  
**Collision:** **DIRECT_COLLISION** for B; **IMMEDIATE_COROLLARY** for C.

### Pappalardi (1995) — earlier weighted-Hooley framework

**Author:** Francesco Pappalardi  
**Title:** *On Hooley's Theorem with Weights*  
**Publication:** Rendiconti del Seminario Matematico dell'Università e Politecnico di Torino 53(4) (1995), 375--388

On p. 376 Pappalardi defines
\[
\pi(x,n)=\#\{p\le x:n\mid i_p\},
\]
uses the divisor/Möbius identity
\[
\sum_{p\le x}f(i_p)
=
\sum_{n\ge1}g(n)\pi(x,n),
\]
introduces
\[
K_n=\mathbf Q(\zeta_n,2^{1/n}),
\]
and states the complete-splitting criterion. On p. 377 he calls the resulting weighted asymptotic the **generalized Artin problem**. Theorem 1 gives weighted asymptotics under summability/tail hypotheses; Theorem 2 develops weighted exact-index consequences.

**Layers:** A explicit; B explicit for \(a=2\).  
**Collision:** **DIRECT_COLLISION** as an earlier special-base precedent.

### Murata (1991) — exact residual index

**Author:** Leo Murata  
**Title:** *A Problem Analogous to Artin's Conjecture for Primitive Roots and Its Applications*  
**Publication:** Archiv der Mathematik 57(6) (1991), 555--565  
**DOI:** 10.1007/BF01199060

Pappalardi quotes Murata's GRH asymptotic for
\[
H_m(x)=\#\{p\le x:i_p=m\},
\]
with explicit density. Exact residual index was therefore already an explicit research object.

**Layer:** A explicit.  
**Collision:** **DIRECT_COLLISION**.

### Wagstaff (1982) — exact-index density and exact Kummer degrees

**Author:** Samuel S. Wagstaff Jr.  
**Title:** *Pseudoprimes and a Generalization of Artin's Conjecture*  
**Publication:** Acta Arithmetica 41(2) (1982), 141--150  
**DOI:** 10.4064/aa-41-2-141-150

Later primary sources inspected in this audit reproduce/use Wagstaff's results:

- Moree, *Near-Primitive Roots*, Theorem 2, attributes to Wagstaff the GRH density
  \[
  \delta(g,t)
  =
  \sum_{n\ge1}
  \frac{\mu(n)}
  {[\mathbf Q(\zeta_{nt},g^{1/(nt)}):\mathbf Q]}.
  \]
- Felix--Murty, Proposition 3.3, explicitly cites Wagstaff Proposition 4.1 for the exact degree of
  \[
  \mathbf Q(\zeta_n,a^{1/n}).
  \]

**Layers:** A explicit; F foundational.  
**Collision:** **DIRECT_COLLISION**.

### Moree (2013) — near-primitive roots are fixed residual index

**Author:** Pieter Moree  
**Title:** *Near-Primitive Roots*  
**Publication:** Functiones et Approximatio Commentarii Mathematici 48(1) (2013)  
**DOI:** 10.7169/facm/2013.48.1.11  
**arXiv:** 1112.5090

In §1 Moree defines
\[
r_g(p)=[(\mathbf Z/p\mathbf Z)^\times:\langle g\bmod p\rangle]
\]
as the **residual index modulo \(p\)** and defines \(N_{g,t}\) by \(r_g(p)=t\). In §2, **Theorem 2** gives Wagstaff's GRH density for arbitrary rational \(g\ne-1,0,1\) and fixed \(t\); **Theorem 3** gives explicit Euler-product/correction-factor formulas including sign and perfect-power cases.

**Layer:** A explicit.  
**Collision:** **DIRECT_COLLISION**.

### Akbary--Felix (2018) — “function of the residual index” is established terminology

**Authors:** Amir Akbary; Adam Tyler Felix  
**Title:** *On the Average Value of a Function of the Residual Index*  
**Publication:** Springer Proceedings in Mathematics & Statistics 251 (2018), 19--37  
**DOI:** 10.1007/978-3-319-97379-1_2

This paper studies averages of \(f(i_a(p))\) while both \(a\) and \(p\) vary and uses constants of the form
\[
\sum_{d\ge1}\frac{g(d)}{d\varphi(d)}.
\]
It is not the controlling fixed-base theorem, but it confirms the standard terminology and the breadth of the weighted residual-index literature. The introduction also records older interest in \(f(n)=1/n\), so the special point \(z=1\) is not new as a weight.

**Layers:** A/B explicit in an averaged-over-\(a\) variant; C has an old special point.  
**Collision:** **PARTIAL_COLLISION** to the fixed-\(a\) formulation.

### Akbary--Fakhari (2024) — product formula for the generalized-Artin constant

**Authors:** Amir Akbary; Milad Fakhari  
**Title:** *Constants for Artin-like Problems in Kummer and Division Fields*  
**Publication:** Research in Number Theory 10 (2024), article 22  
**DOI:** 10.1007/s40993-024-00509-6  
**arXiv:** 2211.13913

The paper gives product expressions for sums of the form
\[
\sum_{n\ge1}\frac{g(n)}{\#G(n)}
\]
when \(g\) is multiplicative and the Galois groups form the relevant profinite system.

Its **Problem 1.5 (Generalized Artin Problem)** explicitly writes
\[
c_{f,a}
:=
\sum_{n\ge1}
\frac{g(n)}{[K_n:\mathbf Q]},
\qquad
g(n)=\sum_{d\mid n}\mu(d)f(n/d),
\]
and the discussion after equation (1.15) notes that their product identity gives an explicit product formula for the Felix--Murty constant when \(f\), equivalently \(g\), is multiplicative.

Since \(g_z\) is multiplicative, this directly contains the project's constant once convergence is checked.

**Layers:** B explicit; C immediate consequence at the constant level; F explicit.  
**Collision:** **DIRECT_COLLISION** for the generalized-Artin constant framework; **IMMEDIATE_COROLLARY** for \(g_z\).

### Lenstra--Moree--Stevenhagen (2014) — controlling meaning of entanglement

**Authors:** H. W. Lenstra Jr.; Pieter Moree; Peter Stevenhagen  
**Title:** *Character Sums for Primitive Root Densities*  
**Publication:** Mathematical Proceedings of the Cambridge Philosophical Society 157(3) (2014), 489--511  
**DOI:** 10.1017/S0305004114000450  
**arXiv:** 1112.4816

They identify the naive product of local splitting densities and the correction factor caused by **entanglement** of Kummer splitting fields, encoded through characters of the adelic/profinite Galois image.

This verifies the Session-2 distinction:

- entanglement affects independence, degree multiplicativity, and local-to-global product formulas;
- entanglement does **not** invalidate the individual fixed-\(n\) statement
  \[
  n\mid I_a(p)
  \iff
  p\text{ splits completely in }K_n(a)
  \]
  away from the finite exceptional/ramified set.

**Layers:** A/F structural.  
**Collision:** **DIRECT_COLLISION** for the meaning and role of entanglement.

### Perucca--Sgobba--Tronto (2021) — modern general Kummer-degree framework

**Authors:** Antonella Perucca; Pietro Sgobba; Sebastiano Tronto  
**Title:** *The Degree of Kummer Extensions of Number Fields*  
**Publication:** International Journal of Number Theory 17(5) (2021), 1091--1110  
**DOI:** 10.1142/S1793042121500263

They treat
\[
K(\zeta_n,\sqrt[n_1]{\alpha_1},\ldots,\sqrt[n_r]{\alpha_r})
\]
over a number field and reduce degree computation to finitely many exceptional cases via a computable integer. For the present rank-one \(\mathbf Q\)-problem, Wagstaff's exact formula is sharper.

**Layer:** F adjacent/general.  
**Collision:** **NEARBY_ONLY** for the exact rank-one formula.

### Loughran--Matthiesen (2024) — finite Frobenian mean controls Mertens exponents

**Authors:** Daniel Loughran; Lilian Matthiesen  
**Title:** *Frobenian Multiplicative Functions and Rational Points in Fibrations*  
**Publication:** Journal of the European Mathematical Society 26(12) (2024), 4779--4830  
**DOI:** 10.4171/JEMS/1374

In §2.1, **Definition 2.1** defines a Frobenian function using Frobenius classes in a **finite Galois extension**. **Lemma 2.4** gives, for a Frobenian function \(\rho\) of mean \(m(\rho)\),
\[
\sum_{p\le x}\rho(p)
=
m(\rho)\operatorname{Li}(x)+\cdots,
\]
\[
\sum_{p\le x}\frac{\rho(p)}p
=
m(\rho)\log\log x+C_\rho+\cdots,
\]
and a corresponding Mertens product with exponent \(m(\rho)\).

This confirms that “mean value becomes an Euler-product exponent” is standard in the finite-Frobenian setting.

However, for fixed \(z>0\),
\[
p\longmapsto I_a(p)^{-z}
\]
is not shown to factor through one finite Galois extension; it depends on arbitrarily deep Kummer divisibility information.

**Layers:** D/E adjacent.  
**Collision:** **NEARBY_ONLY** to the exact project weight.

### Arango-Piñeros--Keliher--Keyes (2022) — Chebotarev Mertens theorem

**Authors:** Santiago Arango-Piñeros; Daniel Keliher; Christopher Keyes  
**Title:** *Mertens' Theorem for Chebotarev Sets*  
**Publication:** International Journal of Number Theory 18(8) (2022), 1823--1842  
**DOI:** 10.1142/S1793042122500932  
**arXiv:** 2103.14747

This generalizes Mertens' product theorem to prime sets defined by conjugacy classes in finite Galois extensions. It supports the conclusion that density exponents for finite Chebotarev prime sets are standard technology, but it does not directly handle the infinite-tower residual-index weight.

**Layers:** D/E adjacent.  
**Collision:** **NEARBY_ONLY**.

## Field-degree audit

Write
\[
a=\pm a_0^h,
\]
where \(h\) is maximal and \(a_0>0\) is not a perfect power, and put
\[
n'=\frac{n}{(n,h)}.
\]
Felix--Murty Proposition 3.3, reproducing Wagstaff Proposition 4.1, gives
\[
[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]
=
\frac{n'\varphi(n)}{\varepsilon(n)}
=
\frac{n\varphi(n)}
{\varepsilon(n)(n,h)}.
\]

For \(a>0\),
\[
\varepsilon(n)=
\begin{cases}
2,&2\mid n'\text{ and }d(a_0)\mid n,\\
1,&\text{otherwise}.
\end{cases}
\]

For \(a<0\), Proposition 3.3 gives an explicit \(2\)-adic case distinction involving the discriminants of \(\mathbf Q(\sqrt{-a_0})\), \(\mathbf Q(\sqrt{2a_0})\), or \(\mathbf Q(\sqrt{a_0})\), depending on \(n'\) modulo \(4\) and \(n\) modulo \(4\) or \(8\).

The key uniform fact is
\[
\varepsilon(n)\in\{1/2,1,2\},
\qquad
1\le(n,h)\le h,
\]
hence Felix--Murty Corollary 3.4 gives
\[
[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]\asymp_a n\varphi(n).
\]

Consequences for Session 2:

1. \(|g_z(n)|\le1\) for every real \(z>0\).
2. Hence
   \[
   \sum_{n\ge1}
   \frac{|g_z(n)|}{[K_n(a):\mathbf Q]}
   \ll_a
   \sum_{n\ge1}\frac1{n\varphi(n)}
   <\infty.
   \]
3. The Kummer series is absolutely convergent for each fixed real \(z>0\), and trivially at \(z=0\).
4. Absolute convergence of the constant is **not by itself** the prime-average interchange; Felix--Murty Theorem 1.7 supplies that step under GRH.

## Fixed-\(n\) source chain

The project identity
\[
n\mid I_a(p)
\iff
p\text{ splits completely in }\mathbf Q(\zeta_n,a^{1/n})
\]
is not a Session-2 discovery claim.

The audit located this chain:

1. Felix--Murty (2012), Lemma 2.1, calls it a **classical result** and states it in exactly this field.
2. Pappalardi (1995), p. 376, states the base-\(2\) version and calls it a **criterion due to Dedekind**.
3. Hooley/Lenstra/Wagstaff machinery uses the same radical/cyclotomic splitting conditions in primitive-root and generalized-Artin arguments.

The audit did not locate a single nineteenth-century theorem statement phrased in modern residual-index notation. The classical attribution is therefore recorded without overstating priority.

## Entanglement audit

In this project, “entanglement” should be reserved for dependencies between Kummer/cyclotomic layers that obstruct naive independence or multiplicativity. It includes:

- nontrivial intersections among radical/cyclotomic fields;
- failure of a naive product of local densities;
- correction factors in generalized Artin constants;
- dependencies among splitting conditions indexed by distinct primes;
- finite-index/profinite Galois-image effects encoded by characters.

It does **not** mean that the fixed-\(n\) criterion needs an extra correction factor.

## Audit of the \(z\)-parameter

The requested A--E classification is:

> **C. It follows immediately from a known theorem for general arithmetic functions.**

More precisely:

- no inspected source was found to single out the entire continuous family \(f_z(n)=n^{-z}\) under exactly this notation;
- Felix--Murty Theorem 1.7 applies immediately for each fixed real \(z>0\);
- Akbary--Fakhari supplies a product/entanglement expression for the corresponding constant because \(g_z\) is multiplicative;
- \(z=1\) is not a new isolated weight: reciprocal residual index already occurs in earlier generalized-Artin/recurrence questions;
- \(z=0\) is the trivial constant weight;
- as \(z\to+\infty\), the transform tends pointwise toward the primitive-root indicator, whose density is the classical Artin problem.

The mathematically natural language is
\[
\Delta_a(z)
=
\sum_{t\ge1}\delta_a(t)t^{-z}
\]
when the residual-index distribution \(\delta_a(t)\) and interchange are justified. This is a **Dirichlet/Mellin transform of the discrete residual-index distribution**, equivalently a **Laplace transform of \(\log I_a(p)\)**:
\[
I_a(p)^{-z}=e^{-z\log I_a(p)}.
\]

No operator-theoretic or geometric “spectrum” was identified.

## Audit of the exact two-variable Euler product

No direct primary source was located for
\[
Z_a(s,z)
=
\prod_{p\nmid a}
(1-I_a(p)^{-z}p^{-s})^{-1}.
\]

Searches included equivalent formulations: residual index, near-primitive root, generalized Artin, weighted Hooley, arithmetic functions of residual index, Frobenian Euler products, Chebotarev Euler products, prime-set zeta functions, Mertens Chebotarev, and Mellin/Dirichlet transforms of residual-index distributions.

The correct conclusion is **not** “the product is new.” Rather:

- in \(\Re(s)>1\), defining the Euler product from a bounded prime weight is routine;
- its logarithm's \(k\ge2\) terms are absolutely regular near the real boundary;
- Felix--Murty already supplies, under GRH, the weighted-prime asymptotic for
  \[
  w_z(p)=I_a(p)^{-z};
  \]
- standard partial summation therefore makes the leading \(\Delta_a(z)\)-coefficient in the real \(s\to1^+\) logarithmic divergence essentially automatic;
- finite-Frobenian results demonstrate the same mean-to-exponent mechanism in a standard finite-Galois setting, but the exact project weight is not shown to be finite Frobenian.

The potentially nontrivial surviving layer is stronger analytic structure: holomorphic/nonvanishing normalization, continuation to a half-plane crossing \(\Re(s)=1\), uniform/complex-\(z\) dependence, or a convergent Kummer-tower \(L\)-factorisation.

## Adversarial decision questions

1. **Is \(I_a(p)\) already standard?** Yes. Standard names include **residual index** \(i_a(p)\), \(r_g(p)\), and subgroup index of \(a\bmod p\).
2. **Are densities for \(I_a(p)=t\) known?** Yes, under GRH in general fixed-base form; this is the near-primitive-root/fixed residual-index problem.
3. **Are densities for \(n\mid I_a(p)\) standard?** Yes. For fixed \(n\), complete splitting in \(K_n(a)\) and Chebotarev give the density unconditionally as a fixed finite-extension statement; GRH enters effective uniform estimates used in infinite sums.
4. **Does the literature already use \(\mathbf Q(\zeta_n,a^{1/n})\) for these conditions?** Yes, explicitly.
5. **Is \(\sum_n(\mu*f)(n)/[K_n(a):\mathbf Q]\) a standard generalized-Artin expression?** Yes. Felix--Murty proves exactly this constant; Akbary--Fakhari explicitly calls the surrounding framework the Generalized Artin Problem.
6. **Does a general-\(f\) theorem imply \(\Delta_a(z)\)?** Yes, conditionally on GRH, in Felix--Murty's positive-base setup: Theorem 1.7 applies because \(|g_z|\le1\). The corresponding negative-base theorem statement was not independently source-matched in this audit.
7. **Does anything substantive remain in the \(z\)-parameter itself?** Not at the level of existence or the degree-series formula for fixed real \(z\ge0\). Possible surviving work concerns joint analytic dependence on complex \(z\), uniformity, or the associated two-variable Euler product.
8. **Is \(Z_a(s,z)\) already covered by standard Frobenian Euler-product theory?** Not literally by the finite-extension definition inspected. The weight depends on the infinite Kummer tower.
9. **Would an expert regard the product as one-line packaging of known results?** Its definition for \(\Re(s)>1\) and its leading real boundary exponent are very close to packaging once Felix--Murty is known. Stronger continuation/factorisation claims are not one-line consequences of the inspected sources.
10. **Is there a project-specific surviving difficulty?** Potentially yes: analytic continuation/normalization and \(L\)-factorisation of the infinite-Kummer weighted Euler product, especially uniformly in complex \(z\). This must be tested as a **reframed** question, not treated as established novelty.

## Session-3 decision

**Exit state: PRIOR_ART_REFRAME.**

The \(\mathbf G_m\) residual-index mean/spectrum layer substantially collapses into generalized-Artin theory. The project should not proceed by treating \(\Delta_a(z)\), its Möbius/Kummer series, or the residual-index distribution as new.

The precise surviving reframe is:

> Study the analytic structure of the normalized infinite-Kummer weighted Euler product
> \[
> H_a(s,z)
> :=
> Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
> \]
> (with the finite omitted-prime factor treated consistently), under hypotheses where \(\Delta_a(z)\) is already known from generalized-Artin theory. Determine whether \(H_a(s,z)\) has genuinely stronger holomorphic/nonvanishing continuation, controlled complex-\(z\) dependence, or an Artin/Dedekind-\(L\) factorisation that is not already a formal consequence of weighted prime asymptotics.

This is a reframe, not a novelty claim.
