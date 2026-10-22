"""Basic and extended calculator operations for EECE435L Lab 6."""

import math


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return a / b; reject a zero divisor."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulus(a, b):
    """Return the Python remainder, with the sign of the divisor."""
    if b == 0:
        raise ValueError("Cannot calculate modulus with a zero divisor")
    return a % b


def power(base, exponent):
    """Raise base to exponent using Python's exponentiation rules."""
    return base ** exponent


def square_root(number):
    """Return the nonnegative real square root; reject negative inputs."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)
