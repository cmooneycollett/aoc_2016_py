"""
Solutions for AOC 2016 Day 18.
"""


import re


def process_input_file():
    """
    Processes the AOC 2016 Day 18 input file into the format required by the
    solver functions. Returns the tiles in the first row of the trap room as
    given in the input file.
    """
    with open("./input/day_18.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(first_row):
    """
    Solves AOC 2016 Day 18 Part 1 // Determines the number of safe tiles there
    are in the first 40 rows of the trap room including the given first row.
    """
    return calculate_safe_tiles_in_rows(first_row, 40)


def solve_part2(first_row):
    """
    Solves AOC 2016 Day 18 Part 2 // ###
    """
    return -1


def calculate_safe_tiles_in_rows(first_row, total_rows):
    """
    Calculates the number of safe tiles are in the trap room with the given
    first row and total number of rows.
    """
    # No safe tiles if no rows considered
    if total_rows <= 0:
        return 0
    # Consider first row
    trap_row = first_row
    safe_count = trap_row.count(".")
    if total_rows == 1:
        return safe_count
    # Use regex to match one of the four trap patterns
    regex_trap = re.compile(r"(\^\^\.|\.\^\^|\^\.\.|\.\.\^)")
    # Consider each other row
    for _ in range(total_rows - 1):
        next_row = ""
        for (index, char) in enumerate(trap_row):
            # Determine the header for each tile in the next row
            if index == 0:
                header = f".{char}{trap_row[index + 1]}"
            elif index == len(trap_row) - 1:
                header = f"{trap_row[index - 1]}{char}."
            else:
                header = f"{trap_row[index - 1]}{char}{trap_row[index + 1]}"
            # Check if the header matches a trap pattern
            if regex_trap.match(header) is not None:
                next_row += "^"
            else:
                next_row += "."
        trap_row = next_row
        safe_count += trap_row.count(".")
    return safe_count
