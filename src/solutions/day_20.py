"""
Solutions for AOC 2016 Day 20.
"""


def process_input_file():
    """
    Processes the AOC 2016 Day 20 input file into the format required by the
    solver functions. Returned value is list of ranges given in the input file.
    """
    ip_ranges = []
    with open("./input/day_20.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            values = [int(value) for value in line.split("-")]
            ip_ranges.append((values[0], values[1]))
    ip_ranges = sorted(ip_ranges, key=lambda ip_range: (
        ip_range[0], ip_range[1]))
    return ip_ranges


def solve_part1(ip_ranges):
    """
    Solves AOC 2016 Day 20 Part 1 // Determines the lowest-valued "IP" that is
    not blocked by the ranges given in the input data.
    """
    joined_ranges = []
    for (lower_bound, upper_bound) in ip_ranges:
        if len(joined_ranges) == 0:
            joined_ranges.append((lower_bound, upper_bound))
            continue
        # See if there is any overlap with ranges
        if (lower_bound < joined_ranges[0][1] or lower_bound == joined_ranges[0][1] + 1) and \
                upper_bound > joined_ranges[0][1]:
            joined_ranges[0] = (joined_ranges[0][0], upper_bound)
        elif lower_bound > joined_ranges[0][1] + 1:
            break
    return joined_ranges[0][1] + 1


def solve_part2(input_data):
    """
    Solves AOC 2016 Day ## Part 2 // ###
    """
    return -1
