"""Tests for the optional greeting application."""

import unittest

from app import greet as app_greet
from my_module import greet


class TestMyModule(unittest.TestCase):
    def test_world(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_pybuilder(self):
        self.assertEqual(greet("PyBuilder"), "Hello, PyBuilder!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_app_greeting(self):
        self.assertEqual(app_greet("Hassan"), "Hello, Hassan!")


if __name__ == '__main__':
    unittest.main()
