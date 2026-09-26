# Session 4 — Reframed Analytic Pilot

Date: 2026-09-26

Exit state: **ANALYTIC_PILOT_REFRAME**.

Session 3 remains controlling prior art. No novelty claim is made for residual index, fixed residual-index distributions, the fixed-n Kummer splitting criterion, the Möbius/Kummer degree constant, general prime averages of f(I_a(p)), the fixed-real-z mean Delta_a(z) in the source-matched positive-base GRH setting, or generalized-Artin entanglement factors.

The main Session-4 conclusion is that the Euler product
\[
Z_a(s,z)=\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1}
\]
is useful packaging, but the difficult analytic information is concentrated more canonically in
\[
P_a(s,z)=\sum_{p\nmid a}I_a(p)^{-z}p^{-s}
\]
and especially in the centered series
\[
\boxed{Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s),}
\qquad
P(s)=\sum_p p^{-s}.
\]

## 1. Exact logarithmic decomposition

For real z>=0 and Re(s)>1,
\[
\log Z_a(s,z)
=
\sum_{p\nmid a}\sum_{k\ge1}
\frac{I_a(p)^{-zk}}{k p^{ks}}
=
P_a(s,z)+R_a(s,z),
\]
where
\[
R_a(s,z)
=
\sum_{p\nmid a}\sum_{k\ge2}
\frac{I_a(p)^{-zk}}{k p^{ks}}.
\]
Also put
\[
R_\zeta(s)=\log\zeta(s)-P(s)
=
\sum_p\sum_{k\ge2}\frac1{k p^{ks}}.
\]
For
\[
H_a(s,z)=Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
\]
we therefore have, exactly in Re(s)>1,
\[
\boxed{
\log H_a(s,z)
=
Q_a(s,z)+R_a(s,z)-\Delta_a(z)R_\zeta(s).
}
\]
This is the clean prime-zeta normalization. The difference between subtracting Delta_a(z)P(s) and subtracting Delta_a(z)log zeta(s) is entirely absorbed by the k>=2 terms.

## 2. The k>=2 remainder is harmless

Fix a compact subset of Re(s)>1/2 and choose sigma_0>1/2 below its real parts. Since real z>=0 gives I_a(p)^{-zk}<=1,
\[
\sum_p\sum_{k\ge2}
\left|
\frac{I_a(p)^{-zk}}{k p^{ks}}
\right|
\le
\sum_p\sum_{k\ge2}\frac1{k p^{k\sigma_0}}.
\]
The right side converges because its first term is dominated by sum_p p^{-2 sigma_0} and the remaining geometric tail is uniformly bounded. By the Weierstrass M-test,
\[
\boxed{R_a(s,z)\text{ is holomorphic for }\Re(s)>1/2.}
\]
The same argument applies to R_zeta(s). Hence every continuation obstruction visible in log H is in Q_a(s,z).

This is elementary and is recorded as a reduction, not as a novelty claim.

## 3. Exact consequence of the Felix–Murty error term

Felix–Murty Theorem 1.7 is used in the paper's standing positive-base setup. For f_z(n)=n^{-z}, z>0, Session 2 gives |g_z(n)|<=1, so their theorem yields under its GRH hypothesis, for every fixed epsilon>0,
\[
A_z(x)
:=
\sum_{\substack{p\le x\\p\nmid a}}I_a(p)^{-z}
=
\Delta_a(z)\operatorname{li}(x)
+
O_{a,z,\epsilon}\left(
\frac{x}{(\log x)^{2-\epsilon}}
\right).
\]
Equivalently, for any fixed 1<beta<2,
\[
A_z(x)=\Delta_a(z)\operatorname{li}(x)
+O_{a,z,\beta}\left(\frac{x}{(\log x)^\beta}\right).
\]
Combining this with the prime number theorem gives
\[
D_z(x):=A_z(x)-\Delta_a(z)\pi(x)
=
O_{a,z,\beta}\left(\frac{x}{(\log x)^\beta}\right).
\]

For Re(s)>1, partial summation gives
\[
Q_a(s,z)
=
s\int_{2^-}^{\infty}D_z(x)x^{-s-1}\,dx.
\]
At Re(s)=1 the absolute majorant is
\[
\frac1{x(\log x)^\beta},
\]
which is integrable because beta>1. Therefore the integral converges locally uniformly up to the closed boundary Re(s)>=1. In particular,
\[
\boxed{\lim_{s\to1^+}Q_a(s,z)\text{ exists and is finite}.}
\]

This is a boundary-continuity statement, not analytic continuation through Re(s)=1.

### Differentiability threshold

One s-derivative introduces a factor comparable to log x. Absolute convergence at s=1 would be forced by beta>2. Felix–Murty supplies every beta<2, not beta>2. Thus the quoted error does not imply differentiability of Q_a at s=1. More generally, m boundary derivatives would be forced by beta>m+1.

### What stronger error would cross the line?

No fixed logarithmic saving x/(log x)^B supplies absolute Mellin convergence in any open half-plane Re(s)<1. A power-saving discrepancy such as
\[
D_z(x)=O(x^\theta(\log x)^C),\qquad \theta<1,
\]
would instead make the Mellin integral holomorphic for Re(s)>theta. This is the scale of strengthening needed by this route.

## 4. Level-1 boundary asymptotic

Combining the finite boundary value of Q_a with the holomorphic k>=2 remainders gives, for fixed source-matched positive a and fixed real z>0 under the Felix–Murty GRH hypotheses,
\[
\lim_{s\to1^+}\log H_a(s,z)
=
Q_a(1,z)+R_a(1,z)-\Delta_a(z)R_\zeta(1).
\]
The limit is finite and real, hence
\[
\boxed{
H_a(s,z)\longrightarrow C_a(z)\in(0,\infty)
\quad(s\to1^+).
}
\]
Equivalently,
\[
\boxed{
Z_a(s,z)
\sim
C_a(z)\zeta(s)^{\Delta_a(z)}
\sim
C_a(z)(s-1)^{-\Delta_a(z)}.
}
\]

This is **LEVEL 1 — REAL BOUNDARY ASYMPTOTIC** only. It is essentially automatic by partial summation once Felix–Murty is accepted as input, so it does not survive as a distinct novelty layer.

At z=0 everything is exact and unconditional:
\[
Z_a(s,0)=\zeta(s)\prod_{p\mid a}(1-p^{-s}),
\]
so
\[
H_a(s,0)=\prod_{p\mid a}(1-p^{-s}).
\]

## 5. Finite omitted-prime normalization

The frozen normalization by full zeta is consistent; it deliberately leaves the finite factors coming from p|a. If instead
\[
\zeta_a(s)=\prod_{p\nmid a}(1-p^{-s})^{-1}
=
\zeta(s)\prod_{p\mid a}(1-p^{-s}),
\]
then
\[
\widehat H_a(s,z)=Z_a(s,z)\zeta_a(s)^{-\Delta_a(z)}
\]
differs from H_a only by the explicit finite factor
\[
\prod_{p\mid a}(1-p^{-s})^{-\Delta_a(z)}.
\]
At z=0, widehat H_a(s,0)=1. No hidden infinite normalization is required.

## 6. Kummer-indicator expansion: rigorous interchange in Re(s)>1

For real z>0,
\[
I_a(p)^{-z}=\sum_{n\mid I_a(p)}g_z(n),
\qquad g_z=\mu*f_z.
\]
For q^j,
\[
|g_z(q^j)|=(1-q^{-z})q^{-(j-1)z}.
\]
Hence for m=prod q^{e_q},
\[
\sum_{n\mid m}|g_z(n)|
=
\prod_{q^{e_q}\parallel m}(2-q^{-e_qz})
\le 2^{\omega(m)}
\le \tau(m).
\]
For every eta>0, tau(m)<<_eta m^eta. Since I_a(p)<=p-1, for sigma>1 choose 0<eta<sigma-1 to obtain
\[
\sum_p p^{-\sigma}
\sum_{n\mid I_a(p)}|g_z(n)|
<<
\sum_p p^{-\sigma+\eta}<\infty.
\]
Therefore the order of summation can be interchanged absolutely:
\[
\boxed{
P_a(s,z)
=
\sum_{n\ge1}g_z(n)
\sum_{\substack{p\nmid an\\p\text{ splits completely in }K_n(a)}}
p^{-s},
\qquad \Re(s)>1.
}
\]
The finitely many exceptional primes are explicitly excluded.

This shows that the Kummer expansion is a rigorous structural identity in the initial domain, not merely formal.

## 7. Finite-level Artin/Dedekind L-function factorization

Fix one finite Galois extension K/Q with G=Gal(K/Q), d=|G|. The regular-character identity gives
\[
1_{\{e\}}(g)
=
\frac1d
\sum_{\chi\in\widehat G}\chi(1)\chi(g).
\]
For unramified p, complete splitting is equivalent to Frob_p=e. Thus, in Re(s)>1,
\[
P_{\rm split}(s;K)
=
\frac1d\sum_\chi\chi(1)\log L(s,\chi)-E_K(s),
\]
where E_K contains the finitely many ramified-prime contributions and the unramified prime-power terms m>=2. The m>=2 part is absolutely holomorphic in Re(s)>1/2.

Using the factorization of the regular representation,
\[
\prod_\chi L(s,\chi)^{\chi(1)}=\zeta_K(s),
\]
this is equivalently
\[
\boxed{
P_{\rm split}(s;K)
=
\frac1d\log\zeta_K(s)-E_K(s),
\qquad \Re(s)>1.
}
\]
This is the exact finite-level factorization requested by Session 4. Beyond Re(s)>1, logarithms require branch choices and control of zeros/poles; a logarithmic derivative may be cleaner.

## 8. Tower-level collapse of the naive L-product

Substituting the finite-level formula into the Kummer expansion formally suggests
\[
\sum_{n\ge1}
\frac{g_z(n)}{[K_n(a):\mathbf Q]}
\log\zeta_{K_n(a)}(s)
\]
plus correction terms.

The original split-prime sum is absolutely convergent in Re(s)>1 because of the divisor-support estimate above. But separating it into individual log zeta_K terms loses that mechanism. The trivial bound
\[
\log\zeta_K(\sigma)
\le [K:\mathbf Q]\log\zeta(\sigma),
\qquad \sigma>1,
\]
only gives
\[
\frac{|g_z(n)|}{[K_n:\mathbf Q]}
|\log\zeta_{K_n}(\sigma)|
\le |g_z(n)|\log\zeta(\sigma),
\]
and sum_n |g_z(n)| diverges.

Therefore
\[
\boxed{
\text{degree growth alone does not justify the naively separated infinite L-product.}
}
\]
This does not rule out every possible reorganization. It shows that a new cancellation or uniform conductor/discriminant mechanism is required.

## 9. Complex z

For z=sigma+i tau,
\[
g_z(p^k)=p^{-(k-1)z}(p^{-z}-1),
\]
so
\[
|g_z(p^k)|=p^{-(k-1)\sigma}|1-p^{-z}|.
\]
For positive non-perfect-power a, the Wagstaff/Felix–Murty specialization gives
\[
[K_n(a):\mathbf Q]\ge \frac12 n\varphi(n).
\]
Thus the absolute Kummer series is bounded by twice the multiplicative majorant
\[
\sum_n\frac{|g_z(n)|}{n\varphi(n)}.
\]
Its Euler factors have first-order size O(p^{-2}) for sigma>=0 and O(p^{-2-sigma}) for -1<sigma<0; higher prime powers form a geometric tail. Consequently
\[
\boxed{
\sum_{n\ge1}\frac{|g_z(n)|}{[K_n(a):\mathbf Q]}<\infty
\quad\text{for }\Re(z)>-1.
}
\]
The convergence is locally uniform there, so the Kummer-degree series is holomorphic in z on Re(z)>-1.

This is only a statement about the degree series. Session 4 did not prove or source-match a complex-z weighted prime-average theorem.

Separately, for Re(s)>1, the frozen Euler product is normally convergent in z on compact subsets of Re(z)>=0.

## 10. Three analytic levels

**LEVEL 1 — REAL BOUNDARY ASYMPTOTIC:** established conditionally for fixed positive a and fixed real z>0 from Felix–Murty plus partial summation; exact at z=0.

**LEVEL 2 — LOCAL COMPLEX FACTORIZATION THROUGH s=1:** not established. The known logarithmic prime-counting error is insufficient.

**LEVEL 3 — HALF-PLANE / GLOBAL CONTINUATION:** not established. Finite-level L-function identities exist, but the naive tower reorganization has no justified convergence mechanism.

## 11. Adversarial decision questions

1. Does the known weighted prime asymptotic prove a finite real limit for H_a(s,z)? **Yes**, in the source-matched positive-base GRH setting.
2. Is this essentially automatic by partial summation? **Yes**.
3. Is there a theorem supporting actual complex continuation through s=1? **No theorem was found or proved in this session**.
4. Is the k>=2 remainder harmless in Re(s)>1/2? **Yes**.
5. Is all hard information concentrated in P_a(s,z)? **More precisely in Q_a(s,z)=P_a(s,z)-Delta_a(z)P(s)**.
6. Is Z_a analytically more informative than P_a for the surviving problem? **No; it adds a holomorphic k>=2 packaging layer**.
7. Can the weighted prime series be decomposed into Kummer/Chebotarev prime series with rigorous interchange in Re(s)>1? **Yes**.
8. Can the finite-level series be expressed using Artin/Dedekind L-functions? **Yes**.
9. Is there a credible convergence mechanism for summing the separated L-function expressions over the tower? **Not from degree growth alone**.
10. Does normalization exhibit stable numerical behavior? **Yes under matched prime cutoffs; see notes/computational-pilot.md**.
11. Is complex z meaningful beyond a harmless parameter? **The degree series has a genuine holomorphic domain Re(z)>-1, but no new prime-mean theorem was established**.
12. Is there a theorem-sized surviving problem? **Yes, but it belongs to Q_a rather than the bare Euler product**.

## 12. The theorem-sized next question

For fixed positive non-perfect-power a and fixed real z>0, under a precisely stated GRH package if needed:

> Does
> \[
> Q_a(s,z)=\sum_{p\nmid a}I_a(p)^{-z}p^{-s}-\Delta_a(z)P(s)
> \]
> admit holomorphic continuation to any region Re(s)>1-delta with delta>0? If so, can this be obtained from a uniformly controlled Kummer-tower Chebotarev/Artin-L expansion, perhaps after passing to a logarithmic derivative?

Because log H differs from Q_a by a function holomorphic on Re(s)>1/2, this is exactly the obstruction to the corresponding local continuation of H_a.

## 13. Verdict

**ANALYTIC_PILOT_REFRAME**

The Level-1 singular normalization of Z_a collapses to a routine consequence of the known generalized-Artin weighted prime asymptotic. The Euler product remains useful notation, but it is not the fundamental object for the surviving analytic problem.

The replacement object is
\[
\boxed{Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s).}
\]

Session 5 should proceed in **reframed mathematical-proof form**, focused on continuation of Q_a and on whether the finite-level L-function identities can be reorganized uniformly over the Kummer tower. It should not treat the Level-1 boundary constant, Delta_a(z), or the bare existence of Z_a as novelty.
