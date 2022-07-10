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


def solve_day_04():
    """
    Solves AOC 2016 Day 4 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 4 - \"Security Through Obscurity\"")
    input_data = day_04.process_input_file()
    p1_solution = day_04.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_04.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_05():
    """
    Solves AOC 2016 Day 5 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 5 - \"How About a Nice Game of Chess?\"")
    input_data = day_05.process_input_file()
    p1_solution = day_05.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_05.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_06():
    """
    Solves AOC 2016 Day 6 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 6 - \"Signals and Noise\"")
    input_data = day_06.process_input_file()
    p1_solution = day_06.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_06.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_07():
    """
    Solves AOC 2016 Day 7 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 7 - \"Internet Protocol Version 7\"")
    input_data = day_07.process_input_file()
    p1_solution = day_07.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_07.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_08():
    """
    Solves AOC 2016 Day 8 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 8 - \"Two-Factor Authentication\"")
    input_data = day_08.process_input_file()
    p1_solution = day_08.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_08.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_09():
    """
    Solves AOC 2016 Day 9 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 9 - \"Explosives in Cyberspace\"")
    input_data = day_09.process_input_file()
    p1_solution = day_09.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_09.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_10():
    """
    Solves AOC 2016 Day 10 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 10 - \"Balance Bots\"")
    input_data = day_10.process_input_file()
    p1_solution = day_10.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day_10.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


def solve_day_11():
    """
    Solves AOC 2016 Day 11 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2016 Day 11 - \"Radioisotope Thermoelectric Generators\"")
    input_data = day_11.process_input_file()
    # p1_solution = day_11.solve_part1(input_data)
    # print(f"> P1 solution - {p1_solution}")
    p2_solution = day_11.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


if __name__ == "__main__":
    # Import to allow execution from project top-level directory
    import os
    import sys
    sys.path.append(os.getcwd())
    # Solution module imports
    from src.solutions import day_01, day_02, day_03, day_04, day_05, day_06, \
        day_07, day_08, day_09, day_10, day_11
    # Main solver methods
    print("==========")
    # solve_day_01()
    # solve_day_02()
    # solve_day_03()
    # solve_day_04()
    # solve_day_05()
    # solve_day_06()
    # solve_day_07()
    # solve_day_08()
    # solve_day_09()
    # solve_day_10()
    solve_day_11()
