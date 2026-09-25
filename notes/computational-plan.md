# Computational Pilot Plan

**Status: planned, not implemented.**

Computation begins after foundational identities are sound.

## Exact arithmetic core

For integer \(a\) and prime \(p\nmid a\):

1. factor \(p-1\) exactly;
2. compute \(\operatorname{ord}_p(a)\) exactly by divisor reduction / prime-factor tests;
3. compute \(I_a(p)=(p-1)/\operatorname{ord}_p(a)\).

No floating-point order calculations.

## Empirical spectrum

For cutoff \(x\), compute
\[
\Delta_a(z;x)
=\frac{1}{\pi(x)}
\sum_{\substack{p\le x\\p\nmid a}} I_a(p)^{-z}.
\]

Initial \(z\)-grid:

\[
0,\ 0.1,\ 0.25,\ 0.5,\ 1,\ 2,\ 4,\ 8,
\]
plus a deliberately large \(z\) to probe the primitive-root endpoint.

Initial bases: \(2,3,5,6,10\), then selected perfect powers and examples chosen to expose entanglement/correction effects.

Record cutoffs, prime counts, arithmetic precision, runtime, and convergence diagnostics.

## Kummer-series comparison

Only after Session 2 and literature work justify the formula, compare empirical means to finite truncations of a Kummer-degree series such as
\[
\sum_{n\le N}\frac{g_z(n)}{[K_n(a):\mathbf Q]}.
\]

Never compare to an unverified theoretical expression as though it were ground truth.

## Euler-product diagnostic

For \(s>1\), compute finite-prime approximations to
\[
\log Z_a(s,z)
=\sum_{p\le P}\sum_{k\ge1}
\frac{I_a(p)^{-zk}}{k p^{ks}},
\]
using a controlled truncation.

Where a defensible value of \(\Delta_a(z)\) is available, inspect
\[
\log Z_a(s,z)-\Delta_a(z)\log\frac1{s-1}
\]
as \(s\to1^+\) and \(P\) grows.

This is diagnostic evidence only.

## Alternative transforms

The pilot should compare the starting weight with:

- \(e^{-z\log I_a(p)}\) (identical presentation of the starting weight);
- \(\operatorname{ord}_p(a)/(p-1)\);
- powers of that normalized order;
- \(e^{-zI_a(p)}\);
- an auxiliary-variable generating function;
- a Dirichlet generating function in the index;
- Laplace/Mellin transforms of \(\log I_a(p)\).

Evaluation criteria: endpoint behavior, Möbius compatibility, Kummer interpretation, analytic tractability, and portability to elliptic/abelian settings.
