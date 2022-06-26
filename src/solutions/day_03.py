"""
Solutions for AOC 2016 Day 3.
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
    for sides in input_data:
        if check_triangle_validity(sides):
            valid_count += 1
    return valid_count


def solve_part2(input_data):
    """
    Determines how many of the "triangles" in the input data are valid, where
    the sum of any two sides is greater than the size of the remaining side.
    """
    valid_count = 0
    for row in range(0, len(input_data), 3):
        for column in range(0, 3):
            side_a = input_data[row][column]
            side_b = input_data[row + 1][column]
            side_c = input_data[row + 2][column]
            if check_triangle_validity([side_a, side_b, side_c]):
                valid_count += 1
    return valid_count


def check_triangle_validity(sides):
    """
    Checks if the given sides specify a valid "triangle" as per the AOC 2016
    Day 3 problem description (a "triangle" is valid where the sum of any two
    sides is greater than the size of the remaining side).
    """
    if len(sides) != 3:
        return False
    return sides[0] + sides[1] > sides[2] and \
        sides[0] + sides[2] > sides[1] and \
        sides[1] + sides[2] > sides[0]
