"""Regression tests for the basic and extended calculator functions."""

import unittest

from calculator_Hassan_Nasrallah import (
    add, subtract, multiply, divide, modulus, power, square_root,
)


class TestCalculator(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_decimal(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_add_zero(self):
        self.assertEqual(add(8, 0), 8)

    def test_subtract_positive(self):
        self.assertEqual(subtract(9, 4), 5)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(4, 9), -5)

    def test_subtract_negative_operand(self):
        self.assertEqual(subtract(4, -3), 7)

    def test_multiply_positive(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-6, 7), -42)

    def test_multiply_zero(self):
        self.assertEqual(multiply(25, 0), 0)

    def test_divide_exact(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_fraction(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_negative(self):
        self.assertEqual(divide(-9, 3), -3)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "zero"):
            divide(5, 0)

    def test_modulus_remainder(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_exact_multiple(self):
        self.assertEqual(modulus(12, 4), 0)

    def test_modulus_negative_dividend(self):
        self.assertEqual(modulus(-10, 3), 2)

    def test_modulus_negative_divisor(self):
        self.assertEqual(modulus(10, -3), -2)

    def test_modulus_decimal(self):
        self.assertAlmostEqual(modulus(5.5, 2), 1.5)

    def test_modulus_by_zero(self):
        with self.assertRaisesRegex(ValueError, "zero"):
            modulus(10, 0)

    def test_power_positive(self):
        self.assertEqual(power(2, 5), 32)

    def test_power_zero_exponent(self):
        self.assertEqual(power(7, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -3), 0.125)

    def test_power_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_fractional_exponent(self):
        self.assertAlmostEqual(power(9, 0.5), 3)

    def test_power_zero_negative_exponent(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)

    def test_square_root_perfect_square(self):
        self.assertEqual(square_root(25), 5)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_fraction(self):
        self.assertAlmostEqual(square_root(0.25), 0.5)

    def test_square_root_irrational(self):
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)

    def test_square_root_negative(self):
        with self.assertRaisesRegex(ValueError, "negative"):
            square_root(-1)


if __name__ == '__main__':
    unittest.main()
