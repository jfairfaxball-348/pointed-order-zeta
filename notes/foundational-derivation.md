# Session 2 — Foundational Derivation

Date: 2026-09-25

Exit state: **FOUNDATIONS_PASS**.

This note checks the frozen \(\mathbf G_m\) starting object from first principles. It makes no novelty claim and does not begin the Session-3 literature audit or any later generalisation.

## 1. Definitions and hypotheses

Fix \(a\in\mathbf Z\setminus\{0,\pm1\}\). The project initially assumes that \(a\) is not a perfect power. For \(p\nmid a\), let \(\operatorname{ord}_p(a)\) be the order of \(a\bmod p\) in \(\mathbf F_p^\times\), and define
\[
I_a(p)=\frac{p-1}{\operatorname{ord}_p(a)}.
\]
The frozen Euler product is
\[
Z_a(s,z)=\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1},
\qquad z\ge0,\quad \Re(s)>1.
\]
For \(n\ge1\), put
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
\]
The field is independent of the chosen \(n\)-th root because any two choices differ by a power of \(\zeta_n\).

## 2. Elementary group theory and the \(z=0\) endpoint

Since \(|\mathbf F_p^\times|=p-1\), Lagrange gives
\[
\operatorname{ord}_p(a)\mid p-1.
\]
Hence \(I_a(p)\in\mathbf Z_{\ge1}\). If \(H=\langle a\bmod p\rangle\), then
\[
[\mathbf F_p^\times:H]
=\frac{p-1}{|H|}
=\frac{p-1}{\operatorname{ord}_p(a)}
=I_a(p).
\]
Thus
\[
I_a(p)=1
\iff
\langle a\bmod p\rangle=\mathbf F_p^\times,
\]
so \(I_a(p)=1\) exactly when \(a\bmod p\) is a primitive root.

At \(z=0\),
\[
Z_a(s,0)=\prod_{p\nmid a}(1-p^{-s})^{-1}
=\zeta(s)\prod_{p\mid a}(1-p^{-s}),
\]
because the frozen product omits exactly the primes dividing \(a\).

## 3. Exact criterion for \(n\mid I_a(p)\)

Let \(G=\langle g\rangle\) be cyclic of order \(N\), and write \(x=g^k\). Then
\[
\operatorname{ord}(x)=\frac{N}{\gcd(N,k)},
\qquad
[G:\langle x\rangle]=\gcd(N,k).
\]
Therefore
\[
n\mid [G:\langle x\rangle]
\iff
n\mid N\ \text{and}\ n\mid k.
\tag{3.1}
\]

Also \(x\in G^n\) exactly when the congruence
\[
nt\equiv k\pmod N
\]
is solvable, which occurs exactly when
\[
\gcd(n,N)\mid k.
\tag{3.2}
\]
When \(n\mid N\), (3.2) becomes \(n\mid k\). Combining with (3.1),
\[
\boxed{
n\mid [G:\langle x\rangle]
\iff
n\mid N\ \text{and}\ x\in G^n.
}
\tag{3.3}
\]
This is valid for composite \(n\) as well.

Applying this to \(G=\mathbf F_p^\times\), \(N=p-1\), and \(x=a\bmod p\),
\[
\boxed{
n\mid I_a(p)
\iff
n\mid p-1
\ \text{and}\
a\bmod p\in(\mathbf F_p^\times)^n.
}
\tag{3.4}
\]
Equivalently,
\[
n\mid I_a(p)
\iff
p\equiv1\pmod n
\ \text{and}\
X^n\equiv a\pmod p
\text{ has a nonzero solution}.
\tag{3.5}
\]

The congruence condition is essential. In \(C_6=\langle g\rangle\), \(g^2\) is a fourth power because \(4t\equiv2\pmod6\) is solvable, but
\[
[C_6:\langle g^2\rangle]=2,
\]
so \(4\nmid[C_6:\langle g^2\rangle]\). Concretely, \(2\) is a fourth power modulo \(7\), but \(I_2(7)=2\), so \(4\nmid I_2(7)\).

## 4. Kummer splitting equivalence

The polynomial \(X^n-a\) is separable over \(\mathbf Q\), and
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n})
\]
contains all roots \(\zeta_n^j a^{1/n}\). Thus \(K_n(a)\) is the splitting field of \(X^n-a\), hence a finite Galois extension even when \(X^n-a\) is reducible.

Use the uniform exceptional set
\[
p\mid an.
\tag{4.1}
\]
If \(p\nmid an\), then \(X^n-a\) is separable modulo \(p\). Its discriminant has prime support contained in the primes dividing \(an\), so \(p\) is unramified in the splitting field.

For \(p\nmid n\), Frobenius in \(\mathbf Q(\zeta_n)\) sends
\[
\zeta_n\mapsto\zeta_n^p.
\]
Hence
\[
p\text{ splits completely in }\mathbf Q(\zeta_n)
\iff
p\equiv1\pmod n.
\tag{4.2}
\]

Assume \(p\nmid an\) and \(p\equiv1\pmod n\). Then \(\mathbf F_p\) contains all \(n\)-th roots of unity. If \(r^n=a\) in \(\mathbf F_p^\times\), all roots
\[
r,\zeta_n r,\ldots,\zeta_n^{n-1}r
\]
lie in \(\mathbf F_p\) and are distinct. Thus
\[
a\in(\mathbf F_p^\times)^n
\iff
X^n-a\text{ splits completely into distinct linear factors mod }p.
\tag{4.3}
\]
For a prime outside the discriminant, complete splitting of the polynomial modulo \(p\) is equivalent to complete splitting of \(p\) in its splitting field. Therefore
\[
p\text{ splits completely in }K_n(a)
\iff
p\equiv1\pmod n
\ \text{and}\
a\in(\mathbf F_p^\times)^n.
\tag{4.4}
\]
Combining with (3.4),
\[
\boxed{
p\nmid an
\Longrightarrow
\left(n\mid I_a(p)\right)
\iff
\left(p\text{ splits completely in }K_n(a)\right).
}
\tag{4.5}
\]

### Exceptional-prime and hypothesis audit

- If \(p\mid a\), \(\operatorname{ord}_p(a)\) is undefined, so such primes must be excluded.
- If \(p\mid n\), the clean equivalence cannot be asserted uniformly even if that prime happens to be unramified in a special field. Example: \(n=2,a=17,p=2\). Then \(I_{17}(2)=1\), but \(2\) splits in \(\mathbf Q(\sqrt{17})\).
- No extra discriminant primes occur outside those dividing \(an\).
- The choice of \(a^{1/n}\) does not matter after adjoining \(\zeta_n\).
- The non-perfect-power assumption on \(a\) is not needed for (3.4) or (4.5). Perfect powers can shrink \([K_n(a):\mathbf Q]\), so they matter for degree formulas and later constants.
- Negative \(a\) requires no correction: choose any root in an algebraic closure; the same splitting-field argument applies.
- “Entanglement” does not modify the individual fixed-\(n\) equivalence. It matters when fields for different \(n\) are combined, when degrees are factorized, or when an infinite inclusion-exclusion is turned into local factors.

## 5. Fixed-\(n\) Chebotarev density

For fixed \(n\), \(K_n(a)/\mathbf Q\) is finite Galois. Chebotarev applied to the identity conjugacy class gives density
\[
\frac1{[K_n(a):\mathbf Q]}
\]
for completely split primes. Since the exceptional set \(p\mid an\) is finite,
\[
\boxed{
\operatorname{dens}\{p:\ p\nmid a,\ n\mid I_a(p)\}
=
\frac1{[K_n(a):\mathbf Q]}.
}
\tag{5.1}
\]
This is a fixed-extension statement. It justifies finite linear combinations of the indicators \(\mathbf1_{n\mid I_a(p)}\), not an infinite sum over \(n\).

Targeted background check only: Andrew Sutherland, MIT 18.785 Fall 2018 Lecture 21, Theorem 21.15,
https://math.mit.edu/classes/18.785/2018fa/LectureNotes21.pdf,
gives the completely-split density \(1/[L:K]\); MIT 18.785 2016 Problem Set 10,
https://math.mit.edu/classes/18.785/2016fa/ProblemSet10.pdf,
notes that the corresponding Chebotarev sets also have their natural density. Historical/source-level auditing is deferred to Session 3.

## 6. Möbius inversion and the missing interchange

For Dirichlet convolution,
\[
(h*k)(m)=\sum_{d\mid m}h(d)k(m/d).
\]
Let \(\mathbf1(n)=1\), let \(\varepsilon\) be the convolution identity, and recall
\[
\mu*\mathbf1=\varepsilon.
\]
For any arithmetic function \(f\), put \(g=\mu*f\). Then
\[
\mathbf1*g
=(\mathbf1*\mu)*f
=\varepsilon*f
=f,
\]
so
\[
\boxed{
f(m)=\sum_{n\mid m}(\mu*f)(n).
}
\tag{6.1}
\]
Applying \(m=I_a(p)\),
\[
f(I_a(p))
=
\sum_{n\mid I_a(p)}(\mu*f)(n)
=
\sum_{n\ge1}(\mu*f)(n)\mathbf1_{n\mid I_a(p)}.
\tag{6.2}
\]
The last sum is pointwise finite for each fixed \(p\).

For fixed \(N\), Chebotarev permits termwise averaging:
\[
\lim_{x\to\infty}\frac1{\pi(x)}
\sum_{\substack{p\le x\\p\nmid a}}
\sum_{n\le N}(\mu*f)(n)\mathbf1_{n\mid I_a(p)}
=
\sum_{n\le N}\frac{(\mu*f)(n)}{[K_n(a):\mathbf Q]}.
\tag{6.3}
\]
What remains unjustified is the infinite formula
\[
\operatorname{average}_p f(I_a(p))
\stackrel?=
\sum_{n\ge1}\frac{(\mu*f)(n)}{[K_n(a):\mathbf Q]}.
\tag{6.4}
\]
One sufficient kind of missing input would be uniform tail control such as
\[
\lim_{N\to\infty}\limsup_{x\to\infty}
\frac1{\pi(x)}
\sum_{\substack{p\le x\\p\nmid a}}
\left|
\sum_{\substack{n\mid I_a(p)\\n>N}}(\mu*f)(n)
\right|=0.
\tag{6.5}
\]
Fixed-\(n\) Chebotarev alone does not imply this.

## 7. Specialisation \(f_z(n)=n^{-z}\)

Let
\[
f_z(n)=n^{-z},
\qquad
g_z=\mu*f_z.
\]
Both \(\mu\) and \(f_z\) are multiplicative, hence \(g_z\) is multiplicative. For a prime power \(q^k\), \(k\ge1\),
\[
\boxed{
g_z(q^k)=q^{-kz}-q^{-(k-1)z}
=-q^{-(k-1)z}(1-q^{-z}).
}
\tag{7.1}
\]
Thus, for \(n=\prod q^{k_q}\),
\[
\boxed{
g_z(n)
=n^{-z}\prod_{q\mid n}(1-q^z)
=(-1)^{\omega(n)}n^{-z}\prod_{q\mid n}(q^z-1).
}
\tag{7.2}
\]
For \(z>0\),
\[
|g_z(n)|
=
\prod_{q^k\parallel n}q^{-(k-1)z}(1-q^{-z})
\le1.
\tag{7.3}
\]

At \(z=0\), \(f_0=\mathbf1\), so
\[
g_0=\mu*\mathbf1=\varepsilon.
\]
Hence \(g_0(1)=1\) and \(g_0(n)=0\) for \(n>1\), giving the pointwise identity \(f_0(I_a(p))=1\).

Separately, \(\Delta_a(0)\) exists because
\[
\frac1{\pi(x)}
\sum_{\substack{p\le x\\p\nmid a}}1
=
1-\frac{\#\{p\le x:p\mid a\}}{\pi(x)}
\to1.
\]
Therefore \(\Delta_a(0)=1\).

For fixed \(n\),
\[
g_z(n)=\sum_{d\mid n}\mu(d)(n/d)^{-z}.
\]
The divisor sum is finite, so as \(z\to+\infty\) only \(d=n\) survives:
\[
\boxed{
g_z(n)\to\mu(n)
}
\tag{7.4}
\]
pointwise. This does not justify passing the limit through an infinite degree series.

## 8. Convergence diagnostics for the Kummer series

The suggested series is
\[
\sum_{n\ge1}\frac{g_z(n)}{[K_n(a):\mathbf Q]}.
\tag{8.1}
\]
Elementary containment gives
\[
\varphi(n)
\le
[K_n(a):\mathbf Q]
\le
n\varphi(n).
\tag{8.2}
\]
The lower bound alone does not settle convergence.

For \(z>0\), \(|g_z(n)|\le1\), so the sufficient condition
\[
\sum_{n\ge1}\frac1{[K_n(a):\mathbf Q]}<\infty
\tag{8.3}
\]
would imply absolute convergence. A concrete sufficient lower bound would be
\[
[K_n(a):\mathbf Q]\gg n^{1+\eta}
\]
for some \(\eta>0\).

The weight \(g_z\) supplies little decay on primes:
\[
|g_z(q)|=1-q^{-z}\to1.
\]
Thus degree growth must do substantial work. Conditional convergence might use the sign \((-1)^{\omega(n)}\), but no such cancellation theorem is asserted here.

Session 3 must determine the actual known degree formulas/lower bounds and whether the required convergence/interchange theorem is already standard.

## 9. Elementary Euler-product convergence

Let \(z\ge0\) and \(\sigma=\Re(s)>1\). Since \(I_a(p)\ge1\),
\[
|I_a(p)^{-z}p^{-s}|\le p^{-\sigma}.
\]
Moreover,
\[
\sum_{p\nmid a}\sum_{k\ge1}
\left|
\frac{I_a(p)^{-zk}}{k p^{ks}}
\right|
\le
\sum_p\sum_{k\ge1}\frac1{k p^{k\sigma}}
=
\log\zeta(\sigma)<\infty.
\]
Therefore the Euler product is absolutely well behaved in the initial domain, and the logarithmic expansion is rigorous:
\[
\boxed{
\log Z_a(s,z)
=
\sum_{p\nmid a}\sum_{k\ge1}
\frac{I_a(p)^{-zk}}{k p^{ks}},
\qquad
z\ge0,\ \Re(s)>1.
}
\tag{9.1}
\]
Nothing here establishes continuation or any singular behaviour at \(s=1\).

## 10. Exact computational verification

Session 2 adds dependency-free exact code for:
- factoring \(p-1\) by trial division;
- exact multiplicative order by prime-factor stripping;
- the residual index;
- an independent brute-force modular \(n\)-th-power check.

The tests cover bases \(2,3,5,6,10\), small primes through \(31\), composite \(n\), \(n\nmid p-1\), negative bases, perfect-power bases, and primes dividing \(a\). They also exhaust the cyclic-group identity for all cyclic group orders \(N\le40\), all elements, and \(n\le40\). No floating point is used. The suite passes.

These computations are consistency tests only, not evidence for a density theorem.

## 11. Failure modes and caveats

1. The condition \(n\mid p-1\) cannot be dropped from the power-residue criterion.
2. Primes \(p\mid a\) are outside the definition.
3. Primes \(p\mid n\) must be excluded from the uniform Kummer equivalence even when a special field is unramified there.
4. Perfect powers can lower field degrees but do not break the fixed-\(n\) criterion.
5. Negative \(a\) introduces no extra correction.
6. Entanglement belongs to degree/tower/inclusion-exclusion issues, not the individual criterion.
7. Fixed-\(n\) Chebotarev does not justify an infinite \(n\)-sum.
8. Absolute convergence of the degree series is not yet established.
9. Euler-product control is proved only for \(z\ge0,\Re(s)>1\).

## 12. Session-2 verdict

**Exit state: FOUNDATIONS_PASS.**

The strongest identity established is
\[
\boxed{
p\nmid an
\Longrightarrow
n\mid I_a(p)
\iff
\left(p\equiv1\pmod n\ \text{and}\ a\in(\mathbf F_p^\times)^n\right)
\iff
p\text{ splits completely in }K_n(a).
}
\]
For each fixed \(n\), Chebotarev then gives density \(1/[K_n(a):\mathbf Q]\).

The most important caveat is that the fixed-\(n\) result does not justify exchanging the infinite Möbius expansion with the prime-density limit. Degree growth and a uniform tail argument are still required.

Session 3 must search for generalized Artin/near-primitive-root results on residual-index distributions; averages of general \(f(I_a(p))\); exact formulas and lower bounds for \([\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]\); perfect-power and entanglement corrections; convergence/interchange of the Möbius degree series; and whether the continuous family \(n^{-z}\) or the two-variable Euler-product packaging adds anything beyond established machinery.
