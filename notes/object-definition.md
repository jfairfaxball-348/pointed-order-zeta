# Frozen Starting Object

## Scope

Session 1 freezes a starting object, not a significance claim.

Let \(a\in\mathbf Z\setminus\{0,\pm1\}\), initially with \(a\) not a perfect power. For each prime \(p\nmid a\), define \(\operatorname{ord}_p(a)\) to be the multiplicative order of the reduction of \(a\) in \(\mathbf F_p^\times\).

Define
\[
I_a(p)=\frac{p-1}{\operatorname{ord}_p(a)}
=[\mathbf F_p^\times:\langle a\bmod p\rangle].
\]

This is the residual index. In particular, \(I_a(p)=1\) iff the reduction of \(a\) generates \(\mathbf F_p^\times\).

## Starting Euler product

Define
\[
Z_a(s,z)
=\prod_{p\nmid a}\left(1-I_a(p)^{-z}p^{-s}\right)^{-1}.
\]

Initial rigorous working range: real \(z\ge0\), \(\Re(s)>1\).

No analytic continuation is assumed.

The notation \(\mathcal Z_a(s,z)\) may be used in mathematical prose.

## Provisional spectrum

Define, whenever the limit exists,
\[
\Delta_a(z)
=\lim_{x\to\infty}\frac1{\pi(x)}
\sum_{\substack{p\le x\\p\nmid a}} I_a(p)^{-z}.
\]

The names “Artin–Kummer order spectrum” and “order spectrum” are experimental and must remain unfrozen until the prior-art audit.

## Endpoint targets to verify later

At \(z=0\), later work must derive carefully
\[
Z_a(s,0)=\zeta(s)\prod_{p\mid a}(1-p^{-s}),
\]
when precisely the primes dividing \(a\) are omitted.

For fixed \(p\), as \(z\to+\infty\),
\[
I_a(p)^{-z}\to
\begin{cases}
1,&I_a(p)=1,\\
0,&I_a(p)>1.
\end{cases}
\]

This statement is only factorwise. Any conclusion about the full infinite Euler product requires independent convergence control.

For the provisional spectrum, the intended endpoint checks are \(\Delta_a(0)=1\) when existence/normalization is justified and an Artin-density limit as \(z\to\infty\) only under hypotheses that later derivation and literature justify.

## Kummer target

Set
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n}),
\]
with all required caveats for perfect powers, reducibility, exceptional primes, and entanglement.

The project target is to derive the precise relation between \(n\mid I_a(p)\) and Frobenius/splitting conditions in \(K_n(a)\). Only after that should Möbius inversion be used to obtain any mean-value expansion.

## Analytic target

For the initial domain, formally expanding logarithms suggests
\[
\log Z_a(s,z)
=\sum_p\sum_{k\ge1}\frac{I_a(p)^{-zk}}{k p^{ks}}.
\]

The future analytic question is whether the \(k=1\) term produces a singular coefficient \(\Delta_a(z)\) near \(s=1\), with the \(k\ge2\) contribution regular enough to isolate a factor resembling
\[
H_a(s,z)(s-1)^{-\Delta_a(z)}.
\]

This is explicitly **not** a theorem at scaffold stage.
