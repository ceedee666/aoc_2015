import unittest
from unittest import TestCase

import main

test_string_1 = "ugknbfddgicrmopn"
test_string_2 = "aaa"
test_string_3 = "jchzalrnumimnmhp"
test_string_4 = "haegwjzuvuyypxyu"
test_string_5 = "dvszwmarrgswjxmb"


class Testing(TestCase):
    def test_is_nice(self):
        self.assertTrue(
            main.is_nice(test_string_1), "The string ugknbfddgicrmopn should be nice"
        )

        self.assertTrue(main.is_nice(test_string_2), "The string aaa should be nice")
        self.assertFalse(main.is_nice(test_string_3), "The string should not be nice")
        self.assertFalse(main.is_nice(test_string_4), "The string should not be nice")
        self.assertFalse(main.is_nice(test_string_4), "The string should not be nice")


if __name__ == "__main__":
    unittest.main()
