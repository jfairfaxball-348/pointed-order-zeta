"""Exact elementary computations for residual indices modulo primes.

Session 2 support code: dependency-free and intended for small exact
consistency checks, not large-scale experiments.
"""

from __future__ import annotations

from math import gcd


def factorint(n: int) -> dict[int, int]:
    """Return the exact prime factorization of a positive integer."""
    if n < 1:
        raise ValueError("factorint expects n >= 1")
    factors: dict[int, int] = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def is_prime(n: int) -> bool:
    """Deterministic trial-division primality test for small inputs."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def multiplicative_order_mod_prime(a: int, p: int) -> int:
    """Compute ord_p(a) exactly by factoring p-1 and stripping factors."""
    if not is_prime(p):
        raise ValueError("p must be prime")
    if gcd(a, p) != 1:
        raise ValueError("multiplicative order is undefined when p divides a")

    order = p - 1
    for q in factorint(p - 1):
        while order % q == 0 and pow(a, order // q, p) == 1:
            order //= q
    return order


def residual_index(a: int, p: int) -> int:
    """Return I_a(p) = (p-1)/ord_p(a)."""
    order = multiplicative_order_mod_prime(a, p)
    return (p - 1) // order


def is_nth_power_mod_prime(a: int, n: int, p: int) -> bool:
    """Check a mod p is an n-th power by independent exact brute force."""
    if n < 1:
        raise ValueError("n must be >= 1")
    if not is_prime(p):
        raise ValueError("p must be prime")
    if gcd(a, p) != 1:
        raise ValueError("a must be nonzero modulo p")
    target = a % p
    return any(pow(x, n, p) == target for x in range(1, p))


def residual_divisibility_criterion(a: int, n: int, p: int) -> tuple[bool, bool]:
    """Return both sides of the Session-2 finite-group criterion."""
    lhs = residual_index(a, p) % n == 0
    rhs = (p - 1) % n == 0 and is_nth_power_mod_prime(a, n, p)
    return lhs, rhs
