# Session 2 Derivation Plan

Session 2 has one job: decide whether the starting object is internally sound enough to enter a serious prior-art audit.

## A. Elementary group identities

For each admissible pair \((a,p)\):

1. derive \(\operatorname{ord}_p(a)\mid p-1\);
2. derive \(I_a(p)=(p-1)/\operatorname{ord}_p(a)\in\mathbf Z_{\ge1}\);
3. identify it explicitly with the subgroup index in \(\mathbf F_p^\times\);
4. verify \(I_a(p)=1\) iff \(a\) is a primitive root mod \(p\).

## B. Euler-product sanity checks

In the initial convergence range, derive the \(z=0\) identity from the Euler factors and keep track of omitted primes.

Separate these notions for \(z\to\infty\):

- convergence of an individual Euler factor;
- convergence of the log Euler product;
- convergence/limit of the full product.

No interchange of limit and infinite product without a theorem.

## C. Residual-index divisibility versus Kummer splitting

For fixed \(n\), derive the exact statement relating
\[
n\mid I_a(p)
\]
to the reduction of \(a\) being an \(n\)-th power / the Frobenius behavior of \(p\) in
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
\]

Track explicitly:

- primes dividing \(a n\);
- ramification;
- any congruence condition \(p\equiv1\pmod n\);
- whether complete splitting is exactly the right condition;
- dependence on the chosen radical presentation;
- perfect-power and entanglement caveats.

## D. Möbius inversion

Starting from a verified divisor-indicator identity, derive for suitable arithmetic functions \(f\) an identity of the form
\[
f(I)=\sum_{n\mid I}(\mu*f)(n),
\]
then average over primes only when the necessary summation and density arguments are justified.

Specialize cautiously to \(f_z(n)=n^{-z}\) and record the exact formula for
\[
g_z=\mu*f_z.
\]

Do not call the resulting prime average formula new.

## E. Small exact checks

Add executable code/tests for small bases and primes. Multiplicative order must be exact; no floating-point computation of orders.

Use checks to falsify derivation mistakes, not to establish density theorems.

## Required document

Write `notes/foundational-derivation.md` with hypotheses before conclusions and a dedicated “failure modes / caveats” section.

## Session-2 exit

Use exactly one:

- `FOUNDATIONS_PASS`
- `FOUNDATIONS_NEED_REPAIR`
- `OBJECT_COLLAPSES`
