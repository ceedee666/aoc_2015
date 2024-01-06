import unittest
from unittest import TestCase

import main

test_string = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""


class Testing(TestCase):
    def test_solve_part_1(self):
        self.assertEqual(62842880, main.solve(test_string.split("\n")))

    def test_solve_part_2(self):
        self.assertEqual(57600000, main.solve(test_string.split("\n"), calories=500))


if __name__ == "__main__":
    unittest.main()
