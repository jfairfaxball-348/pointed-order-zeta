"""Exact/numerically stable support for the Session-4 analytic pilot.

The Kummer-degree routine intentionally supports only positive non-perfect-power
integer bases, the clean Wagstaff/Felix--Murty specialization used here.
"""
from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable

from .residual_index import factorint, residual_index


@dataclass(frozen=True)
class PrimeResidualData:
    base: int
    cutoff: int
    primes: tuple[int, ...]
    indices: tuple[int, ...]


def smallest_prime_factor_sieve(limit: int) -> tuple[list[int], list[int]]:
    if limit < 2:
        return [], list(range(limit + 1))
    spf = list(range(limit + 1))
    spf[1] = 1
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for m in range(p * p, limit + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return [n for n in range(2, limit + 1) if spf[n] == n], spf


def factorint_from_spf(n: int, spf: list[int]) -> dict[int, int]:
    if n < 1 or n >= len(spf):
        raise ValueError("SPF table does not cover n")
    out: dict[int, int] = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out


def totients_up_to(limit: int, primes: Iterable[int]) -> list[int]:
    phi = list(range(limit + 1))
    if limit >= 1:
        phi[1] = 1
    for p in primes:
        if p > limit:
            break
        for m in range(p, limit + 1, p):
            phi[m] -= phi[m] // p
    return phi


def compute_prime_residual_data(a: int, cutoff: int, primes=None, spf=None) -> PrimeResidualData:
    if primes is None or spf is None:
        primes, spf = smallest_prime_factor_sieve(cutoff)
    ps, indices = [], []
    for p in primes:
        if p > cutoff:
            break
        if a % p:
            ps.append(p)
            indices.append(residual_index(a, p, factorint_from_spf(p - 1, spf)))
    return PrimeResidualData(a, cutoff, tuple(ps), tuple(indices))


def weight(index: int, z: complex) -> complex:
    return cmath.exp(-z * math.log(index))


def spectrum_prime_average(data: PrimeResidualData, all_primes: Iterable[int], z: complex, cutoff=None) -> complex:
    """pi(X)^(-1) sum_{p<=X,p not dividing a} I_a(p)^(-z)."""
    x = data.cutoff if cutoff is None else cutoff
    total = sum(weight(i, z) for p, i in zip(data.primes, data.indices) if p <= x)
    count = sum(1 for p in all_primes if p <= x)
    if not count:
        raise ValueError("no primes in requested range")
    return total / count


def prime_dirichlet_sum(data: PrimeResidualData, s: complex, z: complex, cutoff=None) -> complex:
    x = data.cutoff if cutoff is None else cutoff
    return sum(weight(i, z) * cmath.exp(-s * math.log(p))
               for p, i in zip(data.primes, data.indices) if p <= x)


def log_z(data: PrimeResidualData, s: complex, z: complex, cutoff=None) -> complex:
    xcut = data.cutoff if cutoff is None else cutoff
    total = 0j
    for p, i in zip(data.primes, data.indices):
        if p > xcut:
            break
        total -= cmath.log(1 - weight(i, z) * cmath.exp(-s * math.log(p)))
    return total


def log_remainder(data: PrimeResidualData, s: complex, z: complex, cutoff=None) -> complex:
    return log_z(data, s, z, cutoff) - prime_dirichlet_sum(data, s, z, cutoff)


def log_zeta_prime_product(primes: Iterable[int], s: complex, cutoff: int) -> complex:
    total = 0j
    for p in primes:
        if p > cutoff:
            break
        total -= cmath.log(1 - cmath.exp(-s * math.log(p)))
    return total


def matched_log_h(data, primes, s, z, delta, cutoff=None) -> complex:
    """Use the same prime cutoff in Z and the zeta Euler product."""
    x = data.cutoff if cutoff is None else cutoff
    return log_z(data, s, z, x) - delta * log_zeta_prime_product(primes, s, x)


def log_zeta_prime_product_excluding_base(primes, s: complex, cutoff: int, a: int) -> complex:
    """Truncated zeta Euler product with the primes dividing a omitted."""
    total = 0j
    for p in primes:
        if p > cutoff:
            break
        if a % p:
            total -= cmath.log(1 - cmath.exp(-s * math.log(p)))
    return total


def matched_log_h_omitted(data, primes, s, z, delta, cutoff=None) -> complex:
    """Matched-cutoff normalization by zeta_a(s), omitting primes dividing a."""
    x = data.cutoff if cutoff is None else cutoff
    return log_z(data, s, z, x) - delta * log_zeta_prime_product_excluding_base(
        primes, s, x, data.base
    )


@lru_cache(maxsize=None)
def maximal_power_exponent(a: int) -> int:
    h = 0
    for e in factorint(a).values():
        h = math.gcd(h, e)
    return h


@lru_cache(maxsize=None)
def squarefree_kernel(a: int) -> int:
    out = 1
    for p, e in factorint(a).items():
        if e % 2:
            out *= p
    return out


@lru_cache(maxsize=None)
def quadratic_discriminant_of_positive_a(a: int) -> int:
    d = squarefree_kernel(a)
    if d == 1:
        raise ValueError("a is a square")
    return d if d % 4 == 1 else 4 * d


def kummer_degree_positive_nonperfect(a: int, n: int, phi_n: int | None = None) -> int:
    """Wagstaff/Felix--Murty specialization: n*phi(n)/epsilon."""
    if a <= 1 or maximal_power_exponent(a) != 1:
        raise NotImplementedError("only positive non-perfect-power a is implemented")
    if phi_n is None:
        phi_n = n
        for p in factorint(n):
            phi_n -= phi_n // p
    disc = quadratic_discriminant_of_positive_a(a)
    epsilon = 2 if n % 2 == 0 and n % disc == 0 else 1
    return n * phi_n // epsilon


def mobius_convolution_weight(n: int, z: complex, spf=None) -> complex:
    if n == 1:
        return 1 + 0j
    factors = factorint_from_spf(n, spf) if spf is not None else factorint(n)
    out = 1 + 0j
    for p, e in factors.items():
        q = cmath.exp(-z * math.log(p))
        out *= q**e - q ** (e - 1)
    return out


def mobius_convolution_weights_up_to(cutoff: int, z: complex, spf: list[int]) -> list[complex]:
    values = [0j] * (cutoff + 1)
    values[1] = 1 + 0j
    q_cache: dict[int, complex] = {}
    for n in range(2, cutoff + 1):
        p, m = spf[n], n // spf[n]
        q = q_cache.setdefault(p, cmath.exp(-z * math.log(p)))
        values[n] = values[m] * (q if m % p == 0 else q - 1)
    return values


def kummer_delta_partials(a: int, z: complex, cutoffs: Iterable[int], spf, phi, g_values=None) -> dict[int, complex]:
    wanted = sorted(set(cutoffs))
    if not wanted:
        return {}
    top = wanted[-1]
    if a <= 1 or maximal_power_exponent(a) != 1:
        raise NotImplementedError("only positive non-perfect-power a is implemented")
    if g_values is None:
        g_values = mobius_convolution_weights_up_to(top, z, spf)
    disc = quadratic_discriminant_of_positive_a(a)
    out, total, j = {}, 0j, 0
    for n in range(1, top + 1):
        epsilon = 2 if n % 2 == 0 and n % disc == 0 else 1
        total += g_values[n] / (n * phi[n] // epsilon)
        if j < len(wanted) and n == wanted[j]:
            out[n] = total
            j += 1
    return out
