# Session 5 — Reframed Mathematical Proof: continuation of the centered prime series

Date: 2026-09-26

Exit state: **CONTINUATION_PROOF_OBSTRUCTED**.

This note treats the Session-3 prior-art conclusions and the Session-4 Level-1 boundary results as controlling inputs. It does not alter the frozen definitions of (I_a(p)) or (Z_a(s,z)), and it makes no novelty claim.

The theorem-driven scope is a fixed **positive**, non-perfect-power integer (a>1) and a fixed real (z>0), unless a statement is explicitly finite-level and independent of that restriction.

The principal conclusion is negative but precise:

> Centering removes the trivial Chebotarev character and the (s=1) pole **exactly at every finite Kummer level**, and under Dedekind GRH every finite centered level continues holomorphically to (Re(s)>1/2). However, the strongest source-matched uniform estimate is only
> [
> C_{K_n(a)}(s)=O_{a,Omega}(log(2n))
> ]
> on compact subsets (Omegasubset{Re(s)>1/2}). Since (|g_z(q)|=1-q^{-z}	o1) on primes (q), this estimate is not summable over the Kummer tower. Moving truncation does not repair the problem with existing technology: the finite-level part admits a power-saving balance, but the large-divisor prime-support tail is controlled by Felix--Murty only at logarithmic scale. Thus no Level-2 or Level-3 continuation of the full (Q_a(s,z)) is proved.

This is an obstruction to the natural Kummer/Chebotarev/(L)-function proof strategy, **not** a proof that (Q_a) has no continuation.

---

## 1. Exact Session-5 target and preferred proof object

Recall
[
P_a(s,z)=sum_{p
mid a}I_a(p)^{-z}p^{-s},
qquad
P(s)=sum_p p^{-s},
]
and
[
Q_a(s,z)=P_a(s,z)-Delta_a(z)P(s).
]

The exact decomposition requested at the start of Session 5 is
[
oxed{
Q_a(s,z)
=
sum_{p
mid a}
igl(I_a(p)^{-z}-Delta_a(z)igr)p^{-s}
+
Delta_a(z)
left(
sum_{p
mid a}p^{-s}-P(s)
ight).
}
]
Since
[
sum_{p
mid a}p^{-s}-P(s)
=
-sum_{pmid a}p^{-s},
]
the second term is a finite entire Dirichlet polynomial.

It is therefore cleaner to use the omitted-prime centered series
[
oxed{
Q_a^circ(s,z)
:=
P_a(s,z)-Delta_a(z)P_a^circ(s,0)
=
sum_{p
mid a}
igl(I_a(p)^{-z}-Delta_a(z)igr)p^{-s},
}
]
where
[
P_a^circ(s,0):=sum_{p
mid a}p^{-s}.
]
Then
[
oxed{
Q_a(s,z)
=
Q_a^circ(s,z)
-
Delta_a(z)sum_{pmid a}p^{-s}.
}
]
Thus (Q_a) and (Q_a^circ) have exactly the same continuation problem.

**Preferred proof object after Session 5:** (Q_a^circ(s,z)), solely to remove the irrelevant finite omitted-prime correction. The project-level primary analytic object remains (Q_a(s,z)), equivalent up to an entire finite term.

The logarithmic derivative is not adopted as the primary object; see Section 7.

---

## 2. Centered Kummer expansion

Put
[
f_z(n)=n^{-z},
qquad
g_z=mu*f_z.
]
For every (p
mid a),
[
I_a(p)^{-z}
=
sum_{nmid I_a(p)}g_z(n).
]
For a prime power,
[
g_z(q^k)=q^{-kz}-q^{-(k-1)z}.
]
For real (z>0),
[
|g_z(n)|le1.
]

Let
[
d_n=[K_n(a):mathbf Q],
qquad
K_n(a)=mathbf Q(zeta_n,a^{1/n}).
]
In the source-matched positive-base setting, Felix--Murty Theorem 1.7 identifies
[
Delta_a(z)=sum_{nge1}rac{g_z(n)}{d_n}
]
under GRH for the relevant Kummer fields, and the degree estimate (d_nasymp_a narphi(n)) makes this series absolutely convergent.

Define the exact residual-divisibility prime series
[
S_{a,n}(s)
:=
sum_{substack{p
mid a\ nmid I_a(p)}}p^{-s}.
]
Then, for (Re(s)>1),
[
P_a(s,z)
=
sum_{nge1}g_z(n)S_{a,n}(s).
]
Subtracting the mean **before** separating finite-level (L)-functions gives
[
oxed{
Q_a^circ(s,z)
=
sum_{nge1}
g_z(n)
left(
S_{a,n}(s)-rac1{d_n}P_a^circ(s,0)
ight).
}
	ag{2.1}
]

### 2.1 Absolute convergence of (2.1) in the initial half-plane

For (sigma>1),
[
sum_{nge1}|g_z(n)|S_{a,n}(sigma)
=
sum_{p
mid a}p^{-sigma}
sum_{nmid I_a(p)}|g_z(n)|.
]
Session 4 proved
[
sum_{nmid I}|g_z(n)|le	au(I),
]
and hence the right side converges by (	au(I_a(p))ll_eta p^eta).

Also
[
P_a^circ(sigma,0)
sum_{nge1}rac{|g_z(n)|}{d_n}<infty.
]
Therefore (2.1) is an **exact absolutely convergent identity** for (Re(s)>1).

This is stronger bookkeeping than the uncentered separated tower, but it does not yet yield convergence after continuation of the individual terms.

### 2.2 Conversion to complete splitting

For (p
mid an),
[
nmid I_a(p)
iff
p	ext{ splits completely in }K_n(a).
]
The only possible discrepancy between (S_{a,n}) and the completely-split prime series comes from primes (pmid n).

If (pmid n), then (n>I_a(p)) because (I_a(p)le p-1<n), so such a prime never occurs in (S_{a,n}). On the splitting side, a prime (pmid n) is ramified already in the cyclotomic subfield except for the familiar conductor redundancy (nequiv2pmod4). If (n=2m) with (m>1) odd, complete splitting of (2) in (mathbf Q(zeta_m)) would require (2equiv1pmod m), impossible. Hence the only possible accidental finite correction is (n=2,p=2).

Let
[
P_{m split}^circ(s;K_n)
=
sum_{substack{p
mid a\p	ext{ splits completely in }K_n}}p^{-s}.
]
Then
[
S_{a,n}(s)
=
P_{m split}^circ(s;K_n)-e_{a,n}(s),
]
where (e_{a,n}=0) unless (n=2), and
[
e_{a,2}(s)
=
mathbf 1_{{2
mid a, 2	ext{ splits completely in }K_2(a)}},2^{-s}.
]
Thus (2.1) is equivalently a centered completely-split expansion plus a single finite entire correction.

**Conclusion:** centering before the (n)-sum cancels the finite-level mean exactly. It improves the analytic form of each level, but Section 6 shows that the known tower-uniform estimates still do not become summable.

---

## 3. Finite-level centered Chebotarev series

Let (K/mathbf Q) be a finite Galois extension, let
[
G=operatorname{Gal}(K/mathbf Q),
qquad
d=|G|=[K:mathbf Q],
]
and define
[
C_K(s)
=
P_{m split}(s;K)-rac1dP(s).
]

### 3.1 Trivial character cancellation

For an unramified prime (p), regular-character orthogonality gives
[
mathbf1_{{operatorname{Frob}_p=1}}
=
rac1d
sum_{chiinoperatorname{Irr}(G)}
chi(1)chi(operatorname{Frob}_p).
]
The trivial character contributes exactly (1/d). Therefore
[
mathbf1_{{operatorname{Frob}_p=1}}-rac1d
=
rac1d
sum_{substack{chiinoperatorname{Irr}(G)\chi
e1}}
chi(1)chi(operatorname{Frob}_p).
]
Consequently, in (Re(s)>1),
[
oxed{
C_K(s)
=
rac1d
sum_{chi
e1}chi(1)
sum_{p
mid D_K}
rac{chi(operatorname{Frob}_p)}{p^s}
-
rac1dsum_{pmid D_K}p^{-s}.
}
	ag{3.1}
]

So the trivial representation is removed **exactly**, before any logarithm is introduced.

### 3.2 Exact Artin-(L) identity

For an irreducible Artin character (chi), use the Euler-product logarithm in (Re(s)>1). Write
[
E_chi(s)
=
sum_{p
mid D_K}sum_{mge2}
rac{chi(operatorname{Frob}_p^m)}{mp^{ms}}
+
sum_{pmid D_K}sum_{mge1}
rac{
operatorname{tr}!left(
ho_chi(operatorname{Frob}_p^m)mid V_chi^{I_p}
ight)
}{mp^{ms}}.
]
Then
[
sum_{p
mid D_K}
rac{chi(operatorname{Frob}_p)}{p^s}
=
log L(s,chi)-E_chi(s).
]
The (mge2) part is absolutely and locally uniformly convergent for (Re(s)>1/2). The ramified part is a finite sum of local logarithms and is holomorphic already for (Re(s)>0).

Define
[
B_K(s)
=
rac1d
sum_{chi
e1}chi(1)E_chi(s)
+
rac1dsum_{pmid D_K}p^{-s}.
]
Using
[
sum_{chiinoperatorname{Irr}(G)}chi(1)^2=d,
]
one obtains local uniform convergence/boundedness of the prime-power contribution, and therefore
[
B_K(s)quad	ext{is holomorphic for }Re(s)>rac12.
]

Equation (3.1) becomes
[
oxed{
C_K(s)
=
rac1d
sum_{chi
e1}chi(1)log L(s,chi)
-
B_K(s),
qquad
Re(s)>1.
}
	ag{3.2}
]

The regular representation gives
[
zeta_K(s)
=
prod_{chiinoperatorname{Irr}(G)}
L(s,chi)^{chi(1)},
]
with the trivial factor equal to (zeta(s)). Hence, using the canonical Euler-product logarithm in (Re(s)>1),
[
oxed{
C_K(s)
=
rac1d
log!left(rac{zeta_K(s)}{zeta(s)}ight)
-
B_K(s).
}
	ag{3.3}
]

This is the preferred exact finite-level identity.

### 3.3 What happens at (s=1)

The Aramata--Brauer theorem says that for Galois (K/mathbf Q),
[
A_K(s):=rac{zeta_K(s)}{zeta(s)}
]
is entire. See Murty--Murty, *Non-vanishing of L-functions and Applications*, Chapter 2, §3. Since both zeta functions have simple poles at (1),
[
A_K(1)=rac{operatorname{Res}_{s=1}zeta_K(s)}
{operatorname{Res}_{s=1}zeta(s)}

e0.
]
Thus the finite-level pole is genuinely canceled, not merely hidden in notation.

Unconditionally, every fixed (K) therefore has a (K)-dependent neighborhood of (s=1) on which (A_K) is zero-free and a holomorphic logarithm exists. Hence every fixed (C_K) has local continuation across (s=1).

Under GRH for (zeta_K) and RH for (zeta), (A_K) has no zero in
[
Re(s)>rac12.
]
The half-plane is simply connected, so there is a unique holomorphic branch of (log A_K) agreeing with the Euler-product branch for real (s>1). Therefore:

> **Finite-level continuation theorem (conditional).**  
> Under GRH for (zeta_K) and RH for (zeta), (C_K(s)) extends holomorphically to
> [
> Re(s)>rac12.
> ]

No Artin holomorphy assumption is needed for this aggregate statement. Artin holomorphy would justify the individual nontrivial factors in (3.2), but it does not improve the tower problem below.

---

## 4. Kummer degrees, ramification, discriminants, and conductors

Let
[
K_n=K_n(a)=mathbf Q(zeta_n,a^{1/n}),
qquad
d_n=[K_n:mathbf Q],
]
with (a>1) a positive non-perfect-power integer.

### 4.1 Exact degree scale

Wagstaff's formula, reproduced as Felix--Murty Proposition 3.3, specializes to
[
d_n=rac{narphi(n)}{arepsilon_a(n)},
]
where
[
arepsilon_a(n)=
egin{cases}
2,&2mid n	ext{ and }d(a)mid n,\
1,&	ext{otherwise},
end{cases}
]
and (d(a)) is the relevant quadratic discriminant.

Hence
[
oxed{
rac12narphi(n)le d_nle narphi(n)le n^2.
}
	ag{4.1}
]

### 4.2 Explicit discriminant bound

Felix--Murty Lemma 3.2 quotes Hensel's inequality in the form
[
log|D_K|
le
[K:mathbf Q]
left(
log [K:mathbf Q]
+
sum_{p	ext{ ramified in }K}log p
ight),
	ag{4.2}
]
with Serre (1981), p. 130, as the source.

Felix--Murty Lemma 3.5 proves that every prime ramified in (K_n(a)) divides (an). Therefore
[
sum_{p	ext{ ramified in }K_n}log p
le
logoperatorname{rad}(an)
le
log a+log n.
]
Using (d_nle n^2),
[
oxed{
log|D_{K_n}|
le
d_nigl(3log n+log aigr).
}
	ag{4.3}
]
Equivalently,
[
oxed{
|D_{K_n}|^{1/d_n}le a,n^3.
}
	ag{4.4}
]

Thus (log|D_{K_n}|) is (O_a(d_nlog n)=O_a(narphi(n)log n)); the root discriminant grows at most polynomially in (n), while the discriminant itself is exponential on the degree scale.

### 4.3 Artin conductors

The conductor--discriminant formula (for example Neukirch, *Algebraic Number Theory*, VII §11) gives
[
|D_K|
=
prod_{chiinoperatorname{Irr}(G)}
mathfrak f(chi)^{chi(1)}.
]
The trivial character has conductor (1). Therefore the aggregate Artin representation
[
operatorname{Reg}_G-mathbf1
]
whose (L)-function is (zeta_K/zeta) has conductor (|D_K|).

For every irreducible (chi),
[
chi(1)logmathfrak f(chi)
le
log|D_K|.
]
For (K=K_n(a)), (4.3) therefore gives
[
oxed{
logmathfrak f(chi)
le
rac{d_n}{chi(1)}
igl(3log n+log aigr).
}
	ag{4.5}
]

The number or dimensions of irreducible representations do **not** by themselves create an extra finite-level explosion: regular-character aggregation uses
[
sum_chichi(1)^2=d_n
]
and packages the complete nontrivial contribution into (zeta_{K_n}/zeta). The obstruction is instead the lack of decay with (n) after this normalized aggregation.

---

## 5. Effective Chebotarev uniformity in the Kummer level

Felix--Murty Theorem 3.1 records Serre's GRH refinement of effective Chebotarev: for a finite Galois (K/mathbf Q),
[
pi_K(x)
=
rac{operatorname{li}(x)}{[K:mathbf Q]}
+
O!left(
sqrt{x}
left(
rac{log|D_K|}{[K:mathbf Q]}
+log x
ight)
ight),
	ag{5.1}
]
with an absolute implied constant.

Combining (4.2), the Kummer degree formula, and the ramification restriction yields Felix--Murty Corollary 3.6:
[
oxed{
pi_n(x)
=
rac{operatorname{li}(x)}{d_n}
+
O_a!igl(sqrt{x}log(nx)igr),
}
	ag{5.2}
]
under GRH for (zeta_{K_n}).

This is the key uniform estimate. The factor (d_n) has disappeared from the error because the discriminant enters as (log|D_{K_n}|/d_n).

Assume the tower package
[
	ext{GRH for }zeta_{K_n(a)}	ext{ for every }nge1.
	ag{TGRH}
]
Since (K_1=mathbf Q), this includes RH. Subtracting the RH prime-number-theorem estimate gives the centered counting discrepancy
[
E_n(x)
:=
pi_n(x)-rac1{d_n}pi(x)
=
O_a!igl(sqrt{x}log(nx)igr).
	ag{5.3}
]

### 5.1 Mellin consequence

For a fixed (n), partial summation gives
[
C_{K_n}(s)
=
sint_{2^-}^{infty}E_n(x)x^{-s-1},dx
]
after the finite ramified-prime convention is matched.

If
[
sigma=Re(s)>rac12,
qquad
delta=sigma-rac12,
]
then (5.3) yields
[
|C_{K_n}(s)|
ll_a
|s|
int_2^infty
x^{-1-delta}log(nx),dx.
]
Therefore
[
oxed{
|C_{K_n}(s)|
ll_a
|s|
left(
rac{log(2n)}{sigma-	frac12}
+
rac1{(sigma-	frac12)^2}
ight).
}
	ag{5.4}
]
In particular, on every compact
[
OmegaSubset{Re(s)>1/2},
]
[
oxed{
sup_{sinOmega}|C_{K_n}(s)|
ll_{a,Omega}log(2n).
}
	ag{5.5}
]

This is the strongest tower-uniform analytic bound obtained in Session 5.

### 5.2 How large may (n=n(x)) be?

For an **individual** Kummer field, the main term in (5.2) dominates the error whenever
[
d_n,log(nx)log x=o(sqrt{x}).
	ag{5.6}
]
Since (d_nle n^2), every fixed
[
nle x^{1/4-eta}
]
with (eta>0) is safely in the asymptotic range. In particular, (nle(log x)^A) is harmless for every fixed (A).

The (x^{1/4}) scale is also genuinely visible in the bound: for prime (n), (d_n=n(n-1)), so the estimate no longer makes the main term dominate once (n) is appreciably larger than (x^{1/4}).

For a **weighted family** (nle N), using only (|g_z(n)|le1), (5.3) gives
[
oxed{
sum_{nle N}
|g_z(n)E_n(x)|
ll_a
sqrt{x},Nlog(Nx).
}
	ag{5.7}
]
This is a genuine power-saving contribution if (N=x^alpha) with (alpha<1/2). The finite levels themselves are therefore not the decisive obstruction.

---

## 6. Truncating the Kummer tower

In (Re(s)>1), split (2.1) as
[
Q_a^circ(s,z)
=
Q_{le N}(s,z)+Q_{>N}(s,z).
]

### 6.1 Finite piece

Up to the single (n=2,p=2) entire correction,
[
Q_{le N}(s,z)
=
sum_{nle N}g_z(n)C_{K_n}(s)
+	ext{finite entire terms}.
]
Under (TGRH), every finite piece extends holomorphically to
[
Re(s)>rac12.
]
On compact (OmegaSubset{Re(s)>1/2}),
[
oxed{
Q_{le N}(s,z)
=
O_{a,z,Omega}(Nlog(2N)).
}
	ag{6.1}
]

### 6.2 Tail in the original prime representation

In the initial half-plane,
[
|Q_{>N}(s,z)|
le
sum_{p
mid a}p^{-sigma}
sum_{substack{nmid I_a(p)\n>N}}|g_z(n)|
+
P_a^circ(sigma,0)
sum_{n>N}rac{|g_z(n)|}{d_n}.
	ag{6.2}
]
For every fixed (sigma>1), the first term tends to zero by dominated convergence using the Session-4 divisor bound, and the second tends to zero by degree growth. This proves the exact tower identity there.

But (6.2) has no useful majorant at (sigmale1). The convergence mechanism is the **primewise divisor support** (nmid I_a(p)); it disappears when the continued finite-level (C_{K_n}) are treated separately.

### 6.3 Counting-function truncation

The degree tail is benign. Felix--Murty's proof of Theorem 1.7 gives, for every fixed (	heta>0),
[
sum_{n>N}rac{|g_z(n)|}{d_n}
ll_{a,z,	heta}
rac{log N}{N^{1-	heta}}.
	ag{6.3}
]

The hard term is the prime-supported large-divisor tail
[
mathcal T_z(x;N)
:=
sum_{substack{ple x\p
mid a}}
sum_{substack{nmid I_a(p)\n>N}}g_z(n).
	ag{6.4}
]
Absolute values give
[
|mathcal T_z(x;N)|
le
sum_{substack{ple x\I_a(p)>N}}	au(I_a(p)).
	ag{6.5}
]

Felix--Murty Lemma 3.11 controls this when
[
N=rac{sqrt{x}}{(log x)^B}
]
for fixed (B):
[
oxed{
sum_{substack{ple x\I_a(p)>N}}
	au(I_a(p))
ll_{a,arepsilon,B}
rac{x}{(log x)^{2-arepsilon}}.
}
	ag{6.6}
]
Their proof of Theorem 1.7 then combines (5.7), (6.3), and (6.6) and obtains precisely the familiar logarithmic-saving error
[
O_a!left(rac{x}{(log x)^{2-arepsilon}}ight)
]
for the present (alpha=0) weight.

Thus a moving truncation has already been executed, in effect, by the controlling generalized-Artin theorem. Its large-divisor tail is the term that prevents a power saving.

### 6.4 The optimistic power balance and the missing theorem

There is a useful proof-planning calculation.

If one could replace the actual prime tail (6.4) by a power-saving approximation to its density tail, then taking
[
N=x^alpha
]
would produce two natural exponents:

- finite-level Chebotarev error: (x^{1/2+alpha+o(1)});
- Kummer-degree mean tail: (x^{1-alpha+o(1)}).

Balancing gives
[
alpha=rac14,
qquad
x^{3/4+o(1)}.
]

This is **not a theorem**. It identifies exactly what is missing: a power-saving estimate for the divisor-supported tail around (N=x^{1/4}), or cancellation in the weighted (g_z(n))-sum strong enough to replace such an estimate.

The existing Felix--Murty tail theorem is instead naturally located near
[
Nasymprac{sqrt{x}}{(log x)^B},
]
where the small-level Chebotarev sum is itself only logarithmically smaller than (x).

---

## 7. Logarithmic-derivative route

At a fixed finite level, differentiating (3.3) gives
[
oxed{
C_K'(s)
=
rac1d
left(
rac{zeta_K'}{zeta_K}(s)
-
rac{zeta'}{zeta}(s)
ight)
-
B_K'(s).
}
	ag{7.1}
]
This removes the branch choice for (log(zeta_K/zeta)), but replaces it by poles at zeros of the quotient.

Under GRH, those zeros lie on (Re(s)=1/2), so (7.1) is holomorphic for (Re(s)>1/2). It can be integrated back from any base point (s_0>1), where the original Euler series fixes the constant of integration.

For the full project object,
[
Q_a'(s,z)
=
-sum_{p
mid a}
igl(I_a(p)^{-z}-Delta_a(z)igr)
(log p)p^{-s}
]
only in the original domain where termwise differentiation is justified. Session 4 already showed why the known boundary discrepancy is insufficient: one derivative inserts an extra (log x), while Felix--Murty supplies an exponent strictly below the (eta>2) threshold needed for absolute convergence at (s=1).

The finite Level-1 boundary value of (Q_a) can normalize an integration **after** a continuation theorem is proved, but it cannot create the derivative or the continuation.

Most importantly, differentiating does not restore any decay in (n). Under the same GRH/discriminant input, the normalized logarithmic derivative has the same (O_{a,Omega}(log(2n)))-type tower dependence on compact subsets away from (Re(s)=1/2).

**Verdict:** the logarithmic derivative improves branch bookkeeping at a fixed level but does not improve tower convergence.

---

## 8. The easiest nontrivial weights (z=1) and (z=2)

For (z=1),
[
g_1(p^k)
=
-rac{p-1}{p^k},
]
hence
[
oxed{
g_1(n)
=
(-1)^{omega(n)}
rac{arphi(operatorname{rad}n)}{n}.
}
	ag{8.1}
]
For squarefree (n),
[
|g_1(n)|=rac{arphi(n)}n.
]
In particular, on primes
[
|g_1(q)|=1-rac1q	o1.
]

For (z=2),
[
g_2(p^k)
=
-rac{p^2-1}{p^{2k}},
]
so
[
oxed{
g_2(n)
=
(-1)^{omega(n)}
rac{prod_{pmid n}(p^2-1)}{n^2}.
}
	ag{8.2}
]
For squarefree (n),
[
|g_2(n)|
=
prod_{pmid n}(1-p^{-2}),
]
and again
[
|g_2(q)|=1-q^{-2}	o1.
]

Thus neither (z=1) nor (z=2) supplies the (n)-decay needed to sum (5.5) absolutely. Large integer (z) is no better on squarefree (n): (g_z(n)	omu(n)) pointwise.

The (z=1) mean is already part of prior-art reciprocal-residual-index questions; no new mean-value claim is made here.

There may be cancellation from the signs of (g_z). Indeed the scalar Dirichlet series formally satisfies
[
sum_{nge1}rac{g_z(n)}{n^w}
=
rac{zeta(w+z)}{zeta(w)}
]
in its absolute-convergence region. But the finite-level analytic functions (C_{K_n}(s)) are neither known to vary multiplicatively nor smoothly enough in (n) for this scalar cancellation to be transferred to the tower. No such theorem is asserted.

---

## 9. Power-saving discrepancy route and targeted prior art

Define the omitted-prime discrepancy
[
D_z^circ(x)
=
sum_{substack{ple x\p
mid a}}
igl(I_a(p)^{-z}-Delta_a(z)igr).
]
A bound
[
D_z^circ(x)
=
O(x^	heta(log x)^C),
qquad
	heta<1,
	ag{9.1}
]
would imply, by the same Mellin/partial-summation argument as Session 4, that (Q_a^circ(s,z)) is holomorphic for
[
Re(s)>	heta.
]

Session 5 checked the proof ingredients actually used in the residual-index literature rather than re-running the broad novelty audit:

1. **Felix--Murty 2012.** Their Theorem 3.1 records Serre's field-uniform GRH Chebotarev estimate; Corollary 3.6 specializes it to (K_n(a)); Lemma 3.11 gives the large-index tail; Theorem 1.7 combines them. For (|g_z|le1), the final error remains
   [
   x(log x)^{-2+arepsilon},
   ]
   not a power saving.
2. **Earlier exact-index work.** Murata/Moree-style fixed-index estimates remain compatible with the same generalized-Artin/GRH architecture. They do not supply a theorem that sums the present centered infinite weight with a power-saving remainder.
3. **Finite Chebotarev prime-series theory.** Character orthogonality and Aramata--Brauer give the finite-level continuation described in Section 3. This does not address summation over an infinite tower.
4. **Large sieve for Frobenius / zero-density methods.** Targeted searches located powerful family results, but no theorem was found whose hypotheses match this nested, unbounded-degree Kummer family and which supplies cancellation in
   [
   sum_{nle N}g_z(n)
   left(
   pi_n(x)-rac{operatorname{li}(x)}{d_n}
   ight)
   ]
   together with a power-saving estimate for (6.4). Nonappearance in this targeted check is not a novelty claim.

### What stronger hypotheses would actually be needed?

**Artin holomorphy alone does not solve the problem.** It allows the individual factors in (3.2) to be treated as holomorphic functions, but it neither restores a factor (1/d_n) in the effective Chebotarev error nor makes (|g_z(n)|) summable.

**Artin holomorphy + Artin GRH still does not automatically solve the problem.** Standard individual conductor bounds lead to the same (O(log n))-scale normalized finite-level control.

A genuinely useful new input would have to be **tower-averaged**, for example a theorem giving cancellation beyond the triangle bound in
[
sum_{nle N}g_z(n)E_n(x),
]
and, crucially, a power-saving centered estimate for the large-divisor tail
[
mathcal T_z(x;N)
-
pi_a^circ(x)sum_{n>N}rac{g_z(n)}{d_n}
]
for some (N=x^alpha) with (alpha>0).

This is substantially more specific than “GRH across the tower.”

---

## 10. Complex (z)

Complex (z) remains secondary. Session 4 already established absolute/local-uniform convergence of the degree series for (Re(z)>-1) in the positive non-perfect-power setting.

The present obstruction occurs before any useful two-variable continuation can be claimed. Although every finite truncation is holomorphic in (z), no tower-uniform (s)-estimate was obtained that would justify a two-variable theorem.

No new complex-(z) theorem is claimed in Session 5.

---

## 11. Rigorous obstruction theorem for the natural tower proof

The obstruction can now be stated precisely.

> **Proposition (failure of the standard absolute-convergence tower argument).**  
> Fix (a>1) positive and not a perfect power, and (z>0). Assume (TGRH). For every compact
> [
> OmegaSubset{Re(s)>1/2},
> ]
> the centered finite-level functions satisfy
> [
> sup_{sinOmega}|C_{K_n(a)}(s)|
> ll_{a,Omega}log(2n).
> ]
> This estimate cannot provide a locally uniform absolute-convergence proof for
> [
> sum_{nge1}g_z(n)C_{K_n(a)}(s)
> ]
> on (Omega), because already on primes (q),
> [
> |g_z(q)|=1-q^{-z}	o1
> ]
> and
> [
> sum_q |g_z(q)|log q=infty.
> ]
> The same obstruction remains after passing to logarithmic derivatives.

This proposition says that the **available uniform estimate is nonsummable**. It does not assert that the actual tower series diverges conditionally.

A second, complementary obstruction is the moving-truncation result:

> **Proposition (current tail technology is logarithmic).**  
> With the source-matched Felix--Murty large-index estimate, a moving Kummer truncation can recover the known
> [
> O!left(x(log x)^{-2+arepsilon}ight)
> ]
> discrepancy scale, but it does not produce any (O(x^	heta)), (	heta<1), bound. The term preventing a power saving is the prime-supported large-divisor tail (6.4), not the finite-level Chebotarev error or the Kummer-degree mean tail.

These are proof-method obstructions, not natural-boundary theorems.

---

## 12. Proof-level classification

### LEVEL 1 — boundary regularity

Already established in Session 4. Not reproved here.

### LEVEL 2 — local complex continuation of the full (Q_a)

**Not proved.**

Every **fixed finite Chebotarev level** does have local continuation across (s=1) unconditionally, and under GRH it continues to (Re(s)>1/2), but the infinite Kummer sum cannot presently be passed through that continuation.

### LEVEL 3 — half-plane continuation of the full (Q_a)

**Not proved.**

A power-saving discrepancy would suffice, but existing fixed-base weighted residual-index technology gives only logarithmic savings.

### LEVEL 4 — global structure

**Not reached.**

No natural boundary, secondary singularity pattern, or convergent infinite (L)-factorization is proved.

---

## 13. Adversarial decision questions

1. **Is (Q_a(s,z)) still the correct primary analytic object?**  
   Yes, up to the analytically preferable but exactly equivalent omitted-prime variant (Q_a^circ).

2. **Does centering before the Kummer (n)-sum materially improve convergence?**  
   It materially improves each finite level by deleting the trivial mean and pole exactly. It does **not** make the known tower-uniform bounds summable.

3. **Does the trivial character/pole cancel exactly at finite level?**  
   Yes. Regular-character orthogonality removes the trivial character, and Aramata--Brauer packages the remainder as (zeta_K/zeta), which is entire and nonzero at (s=1).

4. **What is the exact finite-level centered (L)-function formula?**  
   [
   oxed{
   C_K(s)
   =
   rac1{[K:mathbf Q]}
   log!left(rac{zeta_K(s)}{zeta(s)}ight)
   -
   B_K(s),
   }
   ]
   in (Re(s)>1), with (B_K) holomorphic for (Re(s)>1/2). Equivalently,
   [
   C_K(s)
   =
   rac1dsum_{chi
e1}chi(1)log L(s,chi)-B_K(s).
   ]

5. **What explicit bound is available for (log|D_{K_n(a)}|)?**  
   [
   oxed{
   log|D_{K_n(a)}|
   le
   d_n(3log n+log a).
   }
   ]

6. **What effective Chebotarev bound is available uniformly in (n)?**  
   Under Dedekind GRH,
   [
   oxed{
   pi_n(x)
   =
   rac{operatorname{li}(x)}{d_n}
   +
   O_a(sqrt{x}log(nx)).
   }
   ]

7. **Up to what (n=n(x)) can it be summed?**  
   Individual asymptotics are comfortably uniform for (nle x^{1/4-eta}), and certainly for polylogarithmic (n). Summing by absolute values over (nle N) costs
   [
   O_a(sqrt{x}Nlog(Nx)).
   ]

8. **Can a moving Kummer truncation produce a power-saving prime discrepancy with current tools?**  
   No. The finite-level and degree-tail pieces could support such a balance, but the available prime-supported large-divisor tail estimate is only logarithmic.

9. **Does GRH suffice?**  
   Not via the current tower method. GRH supplies excellent finite-level control but no summable (n)-decay and no power-saving large-divisor tail.

10. **Would Artin holomorphy materially help?**  
    It cleans up individual factor holomorphy but does not materially improve tower convergence. Artin holomorphy plus GRH is still missing tower-averaged conductor/error cancellation.

11. **Does the logarithmic derivative produce better tower convergence?**  
    No. It removes log branches but keeps the same conductor/discriminant scale and introduces zero poles on the critical line.

12. **Is the infinite (L)-function expansion rigorously meaningful anywhere beyond (Re(s)>1)?**  
    Not as an infinite tower with the estimates established here. Each finite truncation is meaningful farther left; the full sum is only rigorously justified in the original half-plane.

13. **Is there a proof of Level 2 or Level 3 continuation for (Q_a)?**  
    No.

14. **If not, is there a rigorous obstruction explaining the failure?**  
    Yes: the centered finite-level GRH bound is (O(log n)), nonsummable against (g_z), and the moving-truncation large-divisor tail is known only with logarithmic saving.

15. **Is there a different theorem-sized object that should replace (Q_a)?**  
    No compelling replacement emerged. A smoothed or truncated discrepancy is useful as a proof instrument, not as a superior primary object.

16. **Is there still a serious Session-6 problem?**  
    Yes. It is no longer “find an (L)-factorization.” It is to prove or disprove a tower-averaged power-saving discrepancy theorem that preserves divisor support.

---

## 14. Strongest results of Session 5

### Strongest unconditional theorem proved in-project

For every finite Galois (K/mathbf Q),
[
C_K(s)
=
rac1dlog(zeta_K(s)/zeta(s))-B_K(s)
]
in (Re(s)>1), with (B_K) holomorphic for (Re(s)>1/2); the trivial character cancels exactly. By Aramata--Brauer, (C_K) has a (K)-dependent holomorphic continuation through a neighborhood of (s=1).

For the Kummer fields,
[
log|D_{K_n(a)}|le d_n(3log n+log a).
]

### Strongest conditional theorem proved in-project

Under (TGRH), each finite centered Kummer level and every finite Kummer truncation continue holomorphically to
[
Re(s)>rac12,
]
and on compact subsets,
[
C_{K_n(a)}(s)=O_{a,Omega}(log(2n)).
]

### Strongest obstruction proved

The GRH finite-level estimate is not summable over (n) against (g_z), even after exact centering, because (g_z(q)) does not decay on primes. The only known way to recover the original convergence is primewise divisor support; the source-matched large-divisor estimate for that support yields only the already-known logarithmic prime discrepancy, not a power saving.

No claim is made that (Q_a) itself fails to continue.

---

## 15. Session-6-sized question

The surviving theorem-sized question is now more precise than the Session-5 opening question.

For fixed positive non-perfect-power (a) and real (z>0), can one prove, under a clearly stated hypothesis package, a power-saving **tower-averaged centered Kummer estimate**, for some (alpha>0), of the form
[
sum_{nle x^alpha}
g_z(n)
left(
pi_n(x)-rac{operatorname{li}(x)}{d_n}
ight)
+
mathcal T_z(x;x^alpha)
-
operatorname{li}(x)
sum_{n>x^alpha}rac{g_z(n)}{d_n}
=
O(x^{1-delta})
]
for some (delta>0)?

Equivalent formulations with a smooth prime cutoff are acceptable if the smoothing can be removed or translated into holomorphic continuation of (Q_a).

The critical new input would be one of:

- cancellation among the finite-level Chebotarev errors as (n) varies;
- a large-sieve/zero-density theorem genuinely uniform for this Kummer tower;
- a power-saving estimate for the divisor-supported tail;
- or a different argument for (Q_a) that avoids tower separation entirely.

This is the Session-6 problem. Session 5 does not begin it.

---

## 16. Decision

**Exit state: CONTINUATION_PROOF_OBSTRUCTED.**

Reason: the continuation target remains mathematically meaningful and (Q_a^circ) remains the correct proof object, but the natural Kummer/Chebotarev/(L)-function route is blocked by a specific tower-uniform convergence problem. Exact centering kills the finite-level pole, GRH continues every finite level, and discriminant growth is controlled; nevertheless the continued finite-level estimates lose the degree/divisor-support decay needed to sum the tower, while the known moving-truncation tail estimate is only logarithmic.

Session 6 should proceed **in reframed proof form**, targeting the tower-averaged power-saving discrepancy above rather than repeating the infinite (L)-function factorization attempt.
