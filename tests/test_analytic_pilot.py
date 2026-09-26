import math
import unittest

from src.analytic_pilot import (
    compute_prime_residual_data,
    kummer_degree_positive_nonperfect,
    log_remainder,
    log_z,
    matched_log_h,
    mobius_convolution_weight,
    prime_dirichlet_sum,
    quadratic_discriminant_of_positive_a,
    smallest_prime_factor_sieve,
)


class AnalyticPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.primes, cls.spf = smallest_prime_factor_sieve(200)

    def test_degree_specialization(self):
        self.assertEqual(quadratic_discriminant_of_positive_a(2), 8)
        self.assertEqual(quadratic_discriminant_of_positive_a(5), 5)
        self.assertEqual(kummer_degree_positive_nonperfect(2, 8), 16)
        self.assertEqual(kummer_degree_positive_nonperfect(3, 12), 24)
        self.assertEqual(kummer_degree_positive_nonperfect(5, 10), 20)
        with self.assertRaises(NotImplementedError):
            kummer_degree_positive_nonperfect(4, 5)

    def test_gz_prime_power_formula_and_z0(self):
        g8 = mobius_convolution_weight(8, 1, self.spf)
        self.assertAlmostEqual(g8.real, 1 / 8 - 1 / 4)
        self.assertAlmostEqual(g8.imag, 0.0)
        self.assertEqual(mobius_convolution_weight(1, 0, self.spf), 1)
        for n in range(2, 100):
            self.assertAlmostEqual(abs(mobius_convolution_weight(n, 0, self.spf)), 0.0)

    def test_log_decomposition(self):
        data = compute_prime_residual_data(2, 200, self.primes, self.spf)
        s, z = 1.2, 1.0
        self.assertAlmostEqual(
            (log_z(data, s, z) - prime_dirichlet_sum(data, s, z)).real,
            log_remainder(data, s, z).real,
            places=13,
        )

    def test_z0_matched_normalization_is_finite_omitted_factor(self):
        data = compute_prime_residual_data(6, 200, self.primes, self.spf)
        s = 1.3
        value = matched_log_h(data, self.primes, s, 0, 1, 200)
        expected = math.log(1 - 2 ** (-s)) + math.log(1 - 3 ** (-s))
        self.assertAlmostEqual(value.real, expected, places=12)
        self.assertAlmostEqual(value.imag, 0.0, places=12)


if __name__ == "__main__":
    unittest.main()
