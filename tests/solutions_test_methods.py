"""
This module contains the test methods required to verify that the coded solvers
produce the correct solutions for AOC 2016.
"""

import unittest
from src.solutions import day_01, day_02


class SolutionsTestMethods(unittest.TestCase):
    """
    Contains the test methods for each problem part in AOC 2016, checking valid
    answers.
    """

    def test_day_01_p1(self):
        """
        Solution test method for AOC 2016 Day 1 Part 1.
        """
        input_data = day_01.process_input_file()
        solution = day_01.solve_part1(input_data)
        self.assertEqual(332, solution)

    def test_day_01_p2(self):
        """
        Solution test method for AOC 2016 Day 1 Part 2.
        """
        input_data = day_01.process_input_file()
        solution = day_01.solve_part2(input_data)
        self.assertEqual(166, solution)

    def test_day_02_p1(self):
        """
        Solution test method for AOC 2016 Day 2 Part 1.
        """
        input_data = day_02.process_input_file()
        solution = day_02.solve_part1(input_data)
        self.assertEqual("78985", solution)

    def test_day_02_p2(self):
        """
        Solution test method for AOC 2016 Day 2 Part 2.
        """
        input_data = day_02.process_input_file()
        solution = day_02.solve_part2(input_data)
        self.assertEqual("57DD8", solution)


if __name__ == "__main__":
    unittest.main()
