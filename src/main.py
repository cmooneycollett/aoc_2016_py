"""
This module contains the main solver methods for each day of AOC 2016.
"""


def solve_day_01():
    """
    Solves AOC 2016 Day 1 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 1 - \"No Time for a Taxicab\"")
    input_data = day_01.process_input_file()
    p1_solution = day_01.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_01.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_02():
    """
    Solves AOC 2016 Day 2 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 2 - \"Bathroom Security\"")
    input_data = day_02.process_input_file()
    p1_solution = day_02.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_02.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_03():
    """
    Solves AOC 2016 Day 3 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 3 - \"Squares With Three Sides\"")
    input_data = day_03.process_input_file()
    p1_solution = day_03.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_03.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


if __name__ == "__main__":
    # Import to allow execution from project top-level directory
    import os
    import sys
    sys.path.append(os.getcwd())
    # Solution module imports
    from src.solutions import day_01, day_02, day_03
    # Main solver methods
    print("==========")
    solve_day_01()
    solve_day_02()
    solve_day_03()