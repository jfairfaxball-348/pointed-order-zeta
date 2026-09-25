# Session 3 — Prior-Art Matrix

Date: 2026-09-25

Exit state: **PRIOR_ART_REFRAME**

This matrix audits the exact Session-2 structure, not merely similar terminology.  The collision labels are:

- **DIRECT_COLLISION** — essentially the same mathematical statement/object is already present.
- **IMMEDIATE_COROLLARY** — the project statement follows mechanically from a more general theorem.
- **PARTIAL_COLLISION** — a substantial component is known, but a real mathematical gap remains.
- **NEARBY_ONLY** — conceptually related without implying the project statement.
- **UNCLEAR** — theorem matching was not established confidently.

The strongest conclusion is that layers A--C, and much of the Kummer-constant structure in F, are established generalized-Artin theory.  The exact two-variable Euler product was not located in this audit, but its definition in (Re(s)>1) is packaging and its leading real singular exponent is strongly constrained by the already-known weighted prime asymptotic.  The surviving question is therefore narrower: analytic structure of the **infinite-Kummer weighted Euler product after its known mean has been removed**, rather than novelty of the residual-index transform itself.

## A--G layer verdict

| Layer | Session-3 verdict | Reason |
|---|---|---|
| **A. Residual-index distribution** | **DIRECT_COLLISION** | Residual index (i_a(p)) / (r_g(p)) is standard.  Exact index (I_a(p)=t) is the near-primitive-root problem; Wagstaff/Moree give the GRH density as a Kummer-degree Möbius sum.  Divisibility (nmid I_a(p)) is a classical complete-splitting criterion. |
| **B. General (f(I_a(p))) averages** | **DIRECT_COLLISION** | Pappalardi treats weighted sums for base (2); Felix--Murty Theorem 1.7 treats fixed (a) and a broad class of (f), using precisely the divisor/Möbius expansion and (K_n(a)=mathbf Q(zeta_n,a^{1/n})). |
| **C. (f_z(n)=n^{-z})** | **IMMEDIATE_COROLLARY** | For real (z>0), Session 2 gives (|g_z(n)|le1), so Felix--Murty Theorem 1.7 applies with (alpha=0).  Thus, on their GRH hypothesis, (Delta_a(z)) exists and equals the Session-2 degree series.  At (z=0), (Delta_a(0)=1) is elementary.  No source was located that singles out the full continuous (z)-family as a named object. |
| **D. (Z_a(s,z))** | **PARTIAL_COLLISION** | No direct source for the exact product was located.  General Frobenian/Chebotarev Euler-product theory covers finite Galois quotients, while (I_a(p)^{-z}) depends on an infinite Kummer tower.  In (Re(s)>1), however, the product itself is straightforward packaging once the weight is given. |
| **E. Varying singularity exponent / “spectrum”** | **PARTIAL_COLLISION** | For finite Frobenian weights, mean-value exponents in Mertens/Euler products are standard.  For the project weight, Felix--Murty already gives a prime asymptotic strong enough to make a (Delta_a(z)log(1/(s-1))) leading term a standard consequence by partial summation along the real axis.  A genuinely stronger holomorphic/two-variable statement was not located. |
| **F. Kummer tower / (L)-function factorisation** | **PARTIAL_COLLISION** | Akbary--Fakhari give product expressions, including entanglement corrections, for constants (sum g(n)/[K_n:mathbf Q]) with multiplicative (g), directly covering (g_z).  Lenstra--Moree--Stevenhagen give the profinite/character-sum entanglement framework.  No Artin/Dedekind-(L) factorisation or continuation of the exact (Z_a(s,z)) was located. |
| **G. Pointed algebraic-group / 1-motive generalisation** | **NEARBY_ONLY / NOT AUDITED TO NOVELTY STANDARD** | Division-field/elliptic analogues and profinite entanglement frameworks exist, but the hard scope limit prohibited a full 1-motive/abelian-variety audit.  No novelty inference is made. |

## Significant sources

### 1. Felix--Murty (2012): controlling collision for B and C

**Authors:** Adam Tyler Felix; M. Ram Murty  
**Title:** *A Problem of Fomenko's Related to Artin's Conjecture*  
**Publication:** International Journal of Number Theory 8(7) (2012), 1687--1723  
**DOI:** 10.1142/S1793042112500984  
**Stable full text inspected:** https://www.researchgate.net/publication/263795683_A_PROBLEM_OF_FOMENKO%27S_RELATED_TO_ARTIN%27S_CONJECTURE

**Exact locations inspected**

- §1.4, **Theorem 1.7**.
- §2, **Lemma 2.1**.
- §3.2, **Proposition 3.3** and **Corollary 3.4**.
- §6.2, proof of Theorem 1.7, especially equations (6.6)--(6.10).

**Object and theorem match**

They define
[
i_a(p)=[(mathbf Z/pmathbf Z)^	imes:langle amod pangle],
]
the same object as (I_a(p)).

Lemma 2.1 is explicitly introduced as a **classical result** and states, for fixed (d), that
[
dmid i_a(p)
iff
p	ext{ splits completely in }mathbf Q(zeta_d,a^{1/d}).
]
This is the Session-2 fixed-(n) Kummer criterion in their notation.

Theorem 1.7 assumes GRH for the Dedekind zeta functions of the fields
(mathbf Q(zeta_n,a^{1/n})), and assumes
[
f(n)=sum_{dmid n}g(d),qquad
|g(n)|ll 	au_k(n)^r(log n)^alpha,quad 0lealpha<1.
]
It proves
[
sum_{ple x}f(i_a(p))
=
c_{a,f}operatorname{li}(x)
+
O_a!left(rac{x}{(log x)^{2-arepsilon-alpha}}ight),
]
and §6.2 identifies
[
c_{a,f}
=
sum_{dge1}
rac{g(d)}
{[mathbf Q(zeta_d,a^{1/d}):mathbf Q]}.
]

For (f=f_z:nmapsto n^{-z}), Session 2 proved
[
g_z=mu*f_z,qquad |g_z(n)|le1quad(z>0).
]
Hence Theorem 1.7 applies immediately with (alpha=0).  This is not merely nearby work: it supplies the missing infinite interchange, conditionally on GRH, and gives the exact proposed constant.

**Hypotheses/caveats**

- Their global theorem is GRH-conditional.
- Their general convention permits (ainmathbf Zsetminus{0,pm1}); the paper's headline applications often emphasize (a>1).
- Perfect powers are accommodated in the degree formula by the maximal exponent (h).
- Negative (a) is explicitly handled in Proposition 3.3.
- The individual splitting criterion itself is not restricted to non-perfect powers.

**Layers:** A explicit; B explicit; C immediate consequence; F partial.  
**Collision:** **DIRECT_COLLISION** for B; **IMMEDIATE_COROLLARY** for C.

---

### 2. Pappalardi (1995): earlier weighted-Hooley framework

**Author:** Francesco Pappalardi  
**Title:** *On Hooley's Theorem with Weights*  
**Publication:** Rendiconti del Seminario Matematico dell'Università e Politecnico di Torino 53(4) (1995), 375--388  
**Primary PDF inspected:** https://seminariomatematico.polito.it/rendiconti/cartaceo/53-4/375.pdf

**Exact locations inspected**

- p. 376: definition of (pi(x,n)=#{ple x:nmid i_p}), divisor/Möbius identity, Kummer field (K_n=mathbf Q(zeta_n,2^{1/n})), complete-splitting criterion.
- p. 377: **Theorem 1**; Murata's exact-index theorem.
- pp. 377--381: **Theorem 2** and proof.

For the base (2), Pappalardi writes
[
sum_{ple x}f(i_p)
=
sum_{nge1}g(n)pi(x,n),
]
with (g) obtained by Möbius inversion, and calls the corresponding asymptotic the **generalized Artin problem**.  He states that an odd prime splits completely in
[
K_n=mathbf Q(zeta_n,2^{1/n})
]
iff (nmid i_p), attributing the criterion to Dedekind.

Theorem 1 gives weighted asymptotics under summability/tail hypotheses; Theorem 2 develops weighted exact-index consequences.

**Layers:** A explicit; B explicit for (a=2); C potentially covered under its hypotheses but Felix--Murty is the stronger controlling fixed-(a) source.  
**Collision:** **DIRECT_COLLISION** (earlier special-base precedent).

---

### 3. Murata (1991): exact residual index before the later near-primitive-root literature

**Author:** Leo Murata  
**Title:** *A Problem Analogous to Artin's Conjecture for Primitive Roots and Its Applications*  
**Publication:** Archiv der Mathematik 57(6) (1991), 555--565  
**DOI:** 10.1007/BF01199060

Pappalardi, p. 377, quotes Murata's GRH asymptotic for
[
H_m(x)=#{ple x:i_p=m}
]
with explicit density (delta_m).  This establishes that exact-index distribution was already an explicit research object well before the present project.

**Layers:** A explicit for base (2).  
**Collision:** **DIRECT_COLLISION** for the exact-index distribution problem.

---

### 4. Wagstaff (1982): exact-index density and exact Kummer degrees

**Author:** Samuel S. Wagstaff Jr.  
**Title:** *Pseudoprimes and a Generalization of Artin's Conjecture*  
**Publication:** Acta Arithmetica 41(2) (1982), 141--150  
**DOI:** 10.4064/aa-41-2-141-150  
**Publisher record inspected:** https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/41/2/103408/pseudoprimes-and-a-generalization-of-artin-s-conjecture

Two later primary sources inspected in this audit reproduce/use Wagstaff's results:

- Moree, *Near-primitive roots*, Theorem 2, attributes to Wagstaff the GRH density
  [
  delta(g,t)
  =
  sum_{nge1}
  rac{mu(n)}
  {[mathbf Q(zeta_{nt},g^{1/(nt)}):mathbf Q]}.
  ]
- Felix--Murty, Proposition 3.3, explicitly cites Wagstaff Proposition 4.1 for the exact degree of
  (mathbf Q(zeta_n,a^{1/n})).

Thus the exact-index Möbius/Kummer mechanism and the needed degree structure are not new.

**Layers:** A explicit; F foundational.  
**Collision:** **DIRECT_COLLISION** for fixed exact residual index and degree machinery.

---

### 5. Moree (2013): near-primitive roots = fixed residual index

**Author:** Pieter Moree  
**Title:** *Near-Primitive Roots*  
**Publication:** Functiones et Approximatio Commentarii Mathematici 48(1) (2013)  
**DOI:** 10.7169/facm/2013.48.1.11  
**arXiv:** 1112.5090

**Exact locations inspected**

- §1: definition
  [
  r_g(p)=[(mathbf Z/pmathbf Z)^	imes:langle gmod pangle]
  ]
  as the **residual index modulo (p)**.
- §2, **Theorem 2**: Wagstaff's GRH density for arbitrary rational (g
e-1,0,1) and fixed (t).
- §2, **Theorem 3**: explicit Euler-product/correction-factor formulas, including sign and perfect-power cases.

The set (N_{g,t}) is exactly the set of primes with residual index (t), and Moree calls (g) a **near-primitive root of index (t)**.

**Layers:** A explicit; C transformable from A but not singled out; F adjacent through local correction formulas.  
**Collision:** **DIRECT_COLLISION** for A.

---

### 6. Akbary--Felix (2018): the phrase “function of the residual index” is established

**Authors:** Amir Akbary; Adam Tyler Felix  
**Title:** *On the Average Value of a Function of the Residual Index*  
**Publication:** Springer Proceedings in Mathematics & Statistics 251 (2018), 19--37  
**DOI:** 10.1007/978-3-319-97379-1_2  
**Author PDF inspected:** https://www.cs.uleth.ca/~akbary/Akbary-Felix-final.pdf

The paper defines the same residual index (i_a(p)), explicitly says there is “vast literature” on its distribution, and studies averages of (f(i_a(p))) while **both (a) and (p) vary**.  Its main averaged constant is
[
sum_{dge1}rac{g(d)}{darphi(d)}.
]
This is not the controlling fixed-base theorem (Felix--Murty is), but it reinforces the standard terminology and breadth of the weighted residual-index problem.

The introduction also records the earlier (f(n)=1/n) problem arising from Laxton's recurrence conjecture.  Thus even the special point (z=1) has an older arithmetic interpretation.

**Layers:** A/B explicit in an averaged-over-(a) variant; C includes a known special point (z=1).  
**Collision:** **PARTIAL_COLLISION** to the fixed-(a) project, stronger as terminology/prior-art evidence.

---

### 7. Akbary--Fakhari (2024): product formula for the exact generalized-Artin constant

**Authors:** Amir Akbary; Milad Fakhari  
**Title:** *Constants for Artin-like Problems in Kummer and Division Fields*  
**Publication:** Research in Number Theory 10 (2024), article 22  
**DOI:** 10.1007/s40993-024-00509-6  
**arXiv:** 2211.13913

**Exact locations inspected**

- Introduction, **Theorem 1.1** (preprint numbering): product expressions for (sum g(n)/[K_n:mathbf Q]) in the Kummer family.
- **Theorem 1.3**: general profinite-group formulation.
- **Problem 1.5 (Generalized Artin Problem)** and equation (1.14):
  [
  c_{f,a}
  :=
  sum_{nge1}
  rac{g(n)}{[K_n:mathbf Q]},
  qquad
  g(n)=sum_{dmid n}mu(d)f(n/d).
  ]
- Discussion immediately after (1.15): for multiplicative (f) (equivalently (g)), their product identity gives an explicit product formula for the Felix--Murty constant.

This is an especially strong collision with any claim that the Session-2 Möbius/Kummer degree series or its local-factor/entanglement structure is a new construction.  Since (f_z) and (g_z) are multiplicative, the theorem applies once the stated absolute-convergence condition is checked; Wagstaff's degree bound and (|g_z|le1) do so.

**Layers:** B explicit framework; C immediate consequence at constant level; F explicit.  
**Collision:** **DIRECT_COLLISION** for the generalized-Artin constant framework; **IMMEDIATE_COROLLARY** for (g_z).

---

### 8. Lenstra--Moree--Stevenhagen (2014): entanglement means dependence of local splitting conditions

**Authors:** H. W. Lenstra Jr.; Pieter Moree; Peter Stevenhagen  
**Title:** *Character Sums for Primitive Root Densities*  
**Publication:** Mathematical Proceedings of the Cambridge Philosophical Society 157(3) (2014), 489--511  
**DOI:** 10.1017/S0305004114000450  
**arXiv:** 1112.4816

The paper identifies the naive product of local splitting densities and the correction factor caused by **entanglement** of the Kummer splitting fields.  It encodes the correction by characters of the adelic/profinite Galois image.

This verifies the Session-2 distinction:

- entanglement **does** affect independence, degree multiplicativity, and local-to-global product formulas;
- entanglement **does not** invalidate the individual fixed-(n) statement
  [
  nmid I_a(p)
  iff
  p	ext{ splits completely in }K_n(a)
  ]
  away from the finite exceptional/ramified set.

**Layers:** A/F explicit or structural; G nearby through the paper's elliptic-curve application.  
**Collision:** **DIRECT_COLLISION** for the meaning and role of entanglement.

---

### 9. Perucca--Sgobba--Tronto (2021): modern general Kummer-degree framework

**Authors:** Antonella Perucca; Pietro Sgobba; Sebastiano Tronto  
**Title:** *The Degree of Kummer Extensions of Number Fields*  
**Publication:** International Journal of Number Theory 17(5) (2021), 1091--1110  
**DOI:** 10.1142/S1793042121500263  
**Author repository inspected:** https://orbilu.uni.lu/handle/10993/42470

They treat
[
K(zeta_n,sqrt[n_1]{alpha_1},ldots,sqrt[n_r]{alpha_r})
]
over a number field and prove that all degrees reduce, via a computable integer, to finitely many exceptional cases and otherwise have maximal expected degree.  For the present rank-one (mathbf Q) problem, Wagstaff's exact formula is sharper and controlling; this source shows that the degree problem belongs to a developed modern Kummer framework rather than an unexplored gap.

**Layers:** F adjacent/general.  
**Collision:** **NEARBY_ONLY** for the precise (mathbf Q), rank-one formula; important contextual prior art.

---

### 10. Loughran--Matthiesen (2024): finite Frobenian mean controls prime/Mertens exponents

**Authors:** Daniel Loughran; Lilian Matthiesen  
**Title:** *Frobenian Multiplicative Functions and Rational Points in Fibrations*  
**Publication:** Journal of the European Mathematical Society 26 (2024), 4779--4830  
**DOI:** 10.4171/JEMS/1374

**Exact locations inspected**

- §2.1, **Definition 2.1**: a Frobenian function factors through the Frobenius classes of a **finite Galois extension**.
- §2.1, **Lemma 2.4**: if (m(ho)
e0), then
  [
  sum_{ple x}ho(p)=m(ho)operatorname{Li}(x)+cdots,
  quad
  sum_{ple x}rac{ho(p)}p=m(ho)loglog x+C_ho+cdots,
  ]
  and a corresponding Mertens product has exponent (m(ho)).

This confirms that “mean value becomes an Euler-product exponent” is standard in the finite-Frobenian setting.

However, for fixed (z>0), (pmapsto I_a(p)^{-z}) is **not obviously a Frobenian function in Definition 2.1's sense**: it depends on arbitrarily deep Kummer divisibility information and is not shown to factor through one finite Galois extension.  Therefore this source is not a direct theorem about (Z_a(s,z)).

**Layers:** D/E adjacent.  
**Collision:** **NEARBY_ONLY** to the exact project weight; conceptually strong.

---

### 11. Arango-Piñeros--Keliher--Keyes (2022): Mertens for Chebotarev sets

**Authors:** Santiago Arango-Piñeros; Daniel Keliher; Christopher Keyes  
**Title:** *Mertens' Theorem for Chebotarev Sets*  
**Publication:** International Journal of Number Theory 18(8) (2022), 1823--1842  
**DOI:** 10.1142/S1793042122500932  
**arXiv:** 2103.14747

The paper generalizes Mertens' product theorem to prime sets defined by conjugacy classes in finite Galois extensions.  It supports the conclusion that density exponents of finite Chebotarev prime sets are standard technology, but it does not directly handle the infinite-tower residual-index weight.

**Layers:** D/E adjacent.  
**Collision:** **NEARBY_ONLY**.

---

### 12. Hooley (1967) and Lenstra (1977): classical generalized-Artin baseline

**Christopher Hooley**, *On Artin's Conjecture*, J. Reine Angew. Math. 225 (1967), 209--220, DOI 10.1515/crll.1967.225.209.

Hooley proves Artin's primitive-root density under GRH, supplying the classical (I_a(p)=1) endpoint of the exact-index family.

**H. W. Lenstra Jr.**, *On Artin's Conjecture and Euclid's Algorithm in Global Fields*, Invent. Math. 42 (1977), 201--224, DOI 10.1007/BF01389788.

Lenstra develops a broader Artin/Chebotarev framework and is repeatedly cited by the later exact-index and entanglement literature.

**Layers:** A foundational; F structural.  
**Collision:** classical baseline rather than the strongest direct collision with B/C.

## Field-degree audit

Felix--Murty Proposition 3.3 reproduces Wagstaff Proposition 4.1.  Write
[
a=pm a_0^h,
]
where (h) is maximal and (a_0>0) is not a perfect power, and put
[
n'=rac{n}{(n,h)}.
]
Then
[
[mathbf Q(zeta_n,a^{1/n}):mathbf Q]
=
rac{n'arphi(n)}{arepsilon(n)}
=
rac{narphi(n)}
{arepsilon(n)(n,h)}.
]

For (a>0),
[
arepsilon(n)=
egin{cases}
2,&2mid n'	ext{ and }d(a_0)mid n,\
1,&	ext{otherwise}.
end{cases}
]

For (a<0), Proposition 3.3 gives the explicit (2)-adic case distinction: (arepsilon(n)=1) for odd (n); (arepsilon(n)=1/2) when (n) is even and (n') is odd; and, when (n') is even, the possible factor (2) is controlled by congruence classes modulo (4,8) and divisibility by the relevant quadratic discriminants (d(-a_0)), (d(2a_0)), or (d(a_0)).

The key uniform fact is
[
arepsilon(n)in{1/2,1,2},
qquad
1le(n,h)le h,
]
hence Felix--Murty Corollary 3.4 gives
[
[mathbf Q(zeta_n,a^{1/n}):mathbf Q]asymp_a narphi(n).
]

Consequences for the Session-2 series:

1. (|g_z(n)|le1) for every real (z>0).
2. Therefore
   [
   sum_{nge1}
   rac{|g_z(n)|}{[K_n(a):mathbf Q]}
   ll_a
   sum_{nge1}rac1{narphi(n)}
   <infty.
   ]
3. The Kummer series is absolutely convergent for every fixed real (z>0) (and trivially at (z=0)).
4. Absolute convergence of the constant is **not by itself** the prime-average interchange; Felix--Murty Theorem 1.7 supplies that step under GRH.

Thus the Session-2 convergence concern is standardly resolvable at the level of the degree series, and the hard analytic interchange is also already handled conditionally for (g_z).

## Fixed-(n) source chain

The project identity
[
nmid I_a(p)
iff
p	ext{ splits completely in }mathbf Q(zeta_n,a^{1/n})
]
is not a Session-2 novelty claim.

The audit located the following chain:

1. Felix--Murty (2012), Lemma 2.1, calls it a **classical result** and states it in exactly this field.
2. Pappalardi (1995), p. 376, states the base-(2) version and calls it a **criterion due to Dedekind**.
3. Hooley/Lenstra/Wagstaff machinery uses the same radical/cyclotomic splitting conditions in primitive-root and generalized-Artin arguments.

The audit did not locate a single nineteenth-century theorem statement phrased in modern residual-index notation; the classical attribution is therefore recorded, not overstated.

## Entanglement audit

In this project, “entanglement” should be reserved for dependencies between Kummer/cyclotomic layers that obstruct naive independence or multiplicativity.  It includes:

- nontrivial intersections among radical/cyclotomic fields;
- failure of a naive product of local densities;
- correction factors in generalized Artin constants;
- dependencies among splitting conditions indexed by distinct primes;
- finite-index/profinite Galois-image effects encoded by characters.

It does **not** mean that the fixed-(n) criterion is corrected by an extra factor.  That criterion remains an exact splitting statement.  The correction appears only when multiple (n)-conditions are assembled into global densities or Euler products.

## Audit of the (z)-parameter

The outcome is closest to **C** in the requested A--E taxonomy:

> **C. It follows immediately from a known theorem for general arithmetic functions.**

More precisely:

- no inspected source was found to single out the entire continuous family (f_z(n)=n^{-z}) under exactly this notation;
- Felix--Murty Theorem 1.7 applies immediately for each fixed real (z>0);
- Akbary--Fakhari then supplies a product/entanglement expression for the corresponding constant because (g_z) is multiplicative;
- (z=1) is not even a new isolated weight: (1/i_a(p)) already appears in older generalized-Artin/recurrence questions;
- (z=0) is the trivial constant weight;
- as (z	o+infty), the transform tends formally/pointwise toward the primitive-root indicator, whose density is the classical Artin problem.

The mathematically natural language is
[
Delta_a(z)=sum_{tge1}delta_a(t)t^{-z},
]
when the residual-index distribution (delta_a(t)) and interchange are justified.  This is a **Mellin/Dirichlet transform of the discrete residual-index distribution**, equivalently the **Laplace transform of (log I_a(p))**:
[
I_a(p)^{-z}=e^{-zlog I_a(p)}.
]
No operator-theoretic or geometric “spectrum” was identified.

## Audit of the exact two-variable Euler product

No direct source was located for
[
Z_a(s,z)
=
prod_{p
mid a}
(1-I_a(p)^{-z}p^{-s})^{-1}.
]

Searches included combinations of: residual index; near-primitive root; generalized Artin; weighted Hooley; arithmetic functions of the residual index; Frobenian Euler products; Chebotarev Euler products; prime-set zeta functions; Mertens Chebotarev; Mellin/Dirichlet transforms of residual-index distributions; and the exact local-factor shape.

The correct collision statement is therefore **not** “the product is new.”  Rather:

- in (Re(s)>1), defining the Euler product from a bounded prime weight is routine;
- its logarithm's (kge2) terms are absolutely regular there and near the real boundary;
- Felix--Murty already provides, under GRH, the weighted prime asymptotic for (w_z(p)=I_a(p)^{-z});
- standard partial summation therefore makes the leading (Delta_a(z))-coefficient in the real (s	o1^+) logarithmic divergence essentially automatic;
- finite-Frobenian results such as Loughran--Matthiesen Lemma 2.4 demonstrate the same mean-to-exponent mechanism in a standard finite-Galois setting, but the exact project weight is not shown to be finite Frobenian.

The potentially nontrivial surviving layer is stronger analytic structure: holomorphic/nonvanishing normalization, continuation to a half-plane crossing (Re(s)=1), uniform/complex-(z) dependence, or a convergent Kummer-tower (L)-factorisation.

## Adversarial decision questions

1. **Is (I_a(p)) standard?** Yes.  Standard names include **residual index** (i_a(p)), (r_g(p)), and subgroup index of (amod p).
2. **Are densities for (I_a(p)=t) known?** Yes, under GRH in general fixed-base form; this is the near-primitive-root/fixed residual-index problem.
3. **Are densities for (nmid I_a(p)) standard?** Yes.  For fixed (n), complete splitting in (K_n(a)) and Chebotarev give the density unconditionally as a fixed finite-extension density; effective uniform estimates used in infinite sums are where GRH enters.
4. **Does the literature use (mathbf Q(zeta_n,a^{1/n})) for precisely these conditions?** Yes, explicitly.
5. **Is (sum_n(mu*f)(n)/[K_n(a):mathbf Q]) a standard generalized-Artin expression?** Yes.  Felix--Murty prove exactly this constant; Akbary--Fakhari call it the Generalized Artin Problem constant.
6. **Does a general-(f) theorem imply (Delta_a(z))?** Yes, conditionally on GRH: Felix--Murty Theorem 1.7, because (|g_z|le1).
7. **Does anything substantive remain in the (z)-parameter itself?** Not at the level of existence or the degree-series formula for fixed real (zge0).  Possible surviving work concerns joint analytic dependence on complex (z), uniformity, or the associated two-variable Euler product.
8. **Is (Z_a(s,z)) already covered by standard Frobenian Euler-product theory?** Not literally by the finite-extension definition inspected.  The weight depends on the infinite Kummer tower.
9. **Would an expert regard the product as one-line packaging of known results?** Its definition for (Re(s)>1) and its leading real boundary exponent are very close to packaging once Felix--Murty is known.  Stronger continuation/factorisation claims are not one-line consequences of the sources inspected.
10. **Is there a project-specific surviving difficulty?** Potentially yes: analytic continuation/normalisation and (L)-factorisation of the infinite-Kummer weighted Euler product, especially uniformly in complex (z).  This must be tested as a **reframed** question, not treated as established novelty.

## Session-3 decision

**Exit state: PRIOR_ART_REFRAME.**

The (mathbf G_m) residual-index mean/spectrum layer substantially collapses into generalized-Artin theory.  The project should not proceed by treating (Delta_a(z)), its Möbius/Kummer series, or the residual-index distribution as new.

The precise surviving reframe is:

> Study the analytic structure of the normalized infinite-Kummer weighted Euler product
> [
> H_a(s,z)
> :=
> Z_a(s,z),zeta(s)^{-Delta_a(z)}
> ]
> (with the finite omitted-prime factor treated consistently), under hypotheses where (Delta_a(z)) is already known from generalized-Artin theory.  Determine whether (H_a(s,z)) has genuinely stronger holomorphic/nonvanishing continuation, controlled complex-(z) dependence, or an Artin/Dedekind-(L) factorisation that is not already a formal consequence of weighted prime asymptotics.

This is a reframe, not a novelty claim.
