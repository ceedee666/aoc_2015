import unittest
from unittest import TestCase

import main

test_string = """H => HO
H => OH
O => HH

HOH"""


test_string_2 = """H => HO
H => OH
O => HH

HOHOHO"""


class Testing(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(4, main.solve(test_string.split("\n")))
        self.assertEqual(7, main.solve(test_string_2.split("\n")))


if __name__ == "__main__":
    unittest.main()
