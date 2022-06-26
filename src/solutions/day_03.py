"""
Solutions for AOC 2016 Day 03.
"""


def process_input_file():
    """
    Processes the AOC 2016 Day 3 input file into the format required by the
    solver functions. Returned value is a list containing sub-lists with the
    triangle side lengths listed in the input file.
    """
    input_data = []
    with open("./input/day_03.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            sides = [int(value) for value in line.split()]
            input_data.append(sides)
    return input_data


def solve_part1(input_data):
    """
    Determines how many of the "triangles" in the input data are valid, where
    the sum of any two sides is greater than the size of the remaining side.
    """
    valid_count = 0
    for (side_a, side_b, side_c) in input_data:
        if side_a + side_b <= side_c:
            continue
        if side_a + side_c <= side_b:
            continue
        if side_b + side_c <= side_a:
            continue
        valid_count += 1
    return valid_count


def solve_part2(input_data):
    return -1
