"""
This module contains the test methods required to verify that the coded solvers
produce the correct solutions for AOC 2016.
"""


import unittest
from src.solutions import day_01, day_02, day_03, day_04, day_05, day_06, \
    day_07, day_08, day_09


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

    def test_day_03_p1(self):
        """
        Solution test method for AOC 2016 Day 3 Part 1.
        """
        input_data = day_03.process_input_file()
        solution = day_03.solve_part1(input_data)
        self.assertEqual(862, solution)

    def test_day_03_p2(self):
        """
        Solution test method for AOC 2016 Day 3 Part 2.
        """
        input_data = day_03.process_input_file()
        solution = day_03.solve_part2(input_data)
        self.assertEqual(1577, solution)

    def test_day_04_p1(self):
        """
        Solution test method for AOC 2016 Day 4 Part 1.
        """
        input_data = day_04.process_input_file()
        solution = day_04.solve_part1(input_data)
        self.assertEqual(173787, solution)

    def test_day_04_p2(self):
        """
        Solution test method for AOC 2016 Day 4 Part 2.
        """
        input_data = day_04.process_input_file()
        solution = day_04.solve_part2(input_data)
        self.assertEqual(548, solution)

    def test_day_05_p1(self):
        """
        Solution test method for AOC 2016 Day 5 Part 1.
        """
        input_data = day_05.process_input_file()
        solution = day_05.solve_part1(input_data)
        self.assertEqual("f77a0e6e", solution)

    def test_day_05_p2(self):
        """
        Solution test method for AOC 2016 Day 5 Part 2.
        """
        input_data = day_05.process_input_file()
        solution = day_05.solve_part2(input_data)
        self.assertEqual("999828ec", solution)

    def test_day_06_p1(self):
        """
        Solution test method for AOC 2016 Day 6 Part 1.
        """
        input_data = day_06.process_input_file()
        solution = day_06.solve_part1(input_data)
        self.assertEqual("dzqckwsd", solution)

    def test_day_06_p2(self):
        """
        Solution test method for AOC 2016 Day 6 Part 2.
        """
        input_data = day_06.process_input_file()
        solution = day_06.solve_part2(input_data)
        self.assertEqual("lragovly", solution)

    def test_day_07_p1(self):
        """
        Solution test method for AOC 2016 Day 7 Part 1.
        """
        input_data = day_07.process_input_file()
        solution = day_07.solve_part1(input_data)
        self.assertEqual(115, solution)

    def test_day_07_p2(self):
        """
        Solution test method for AOC 2016 Day 7 Part 2.
        """
        input_data = day_07.process_input_file()
        solution = day_07.solve_part2(input_data)
        self.assertEqual(231, solution)

    def test_day_08_p1(self):
        """
        Solution test method for AOC 2016 Day 8 Part 1.
        """
        input_data = day_08.process_input_file()
        solution = day_08.solve_part1(input_data)
        self.assertEqual(123, solution)

    def test_day_08_p2(self):
        """
        Solution test method for AOC 2016 Day 8 Part 2.
        """
        input_data = day_08.process_input_file()
        solution = day_08.solve_part2(input_data)
        self.assertEqual("AFBUPZBJPS", solution)

    def test_day_09_p1(self):
        """
        Solution test method for AOC 2016 Day 9 Part 1.
        """
        input_data = day_09.process_input_file()
        solution = day_09.solve_part1(input_data)
        self.assertEqual(98135, solution)

    def test_day_09_p2(self):
        """
        Solution test method for AOC 2016 Day 9 Part 2.
        """
        input_data = day_09.process_input_file()
        solution = day_09.solve_part2(input_data)
        self.assertEqual(10964557606, solution)


if __name__ == "__main__":
    unittest.main()
