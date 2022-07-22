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
    Solves AOC 2016 Day 20 Part 1 // Determines the lowest-valued "IP address"
    that is not blocked by the ranges given in the input data.
    """
    joined_ranges = []
    for (lower_bound, upper_bound) in ip_ranges:
        if len(joined_ranges) == 0:
            joined_ranges.append((lower_bound, upper_bound))
            continue
        # See if there is any overlap with last range, or current range is adjacent
        if (lower_bound < joined_ranges[-1][1] or lower_bound == joined_ranges[-1][1] + 1) and \
                upper_bound > joined_ranges[-1][1]:
            joined_ranges[-1] = (joined_ranges[-1][0], upper_bound)
        elif lower_bound > joined_ranges[-1][1] + 1:
            break
    return joined_ranges[0][1] + 1


def solve_part2(ip_ranges):
    """
    Solves AOC 2016 Day 20 Part 2 // Determines the number of "IP addresses"
    that are permitted by the given IP ranges, where IP addresses can range
    between 0 and 4294967295 (inclusive).
    """
    max_ip_addr = 4294967295
    joined_ranges = []
    for (lower_bound, upper_bound) in ip_ranges:
        if len(joined_ranges) == 0:
            joined_ranges.append((lower_bound, upper_bound))
            continue
        # Check if there is overlap with last range, or current range is adjacent
        if (lower_bound < joined_ranges[-1][1] or lower_bound == joined_ranges[-1][1] + 1) and \
                upper_bound > joined_ranges[-1][1]:
            joined_ranges[-1] = (joined_ranges[-1][0], upper_bound)
        elif lower_bound > joined_ranges[-1][1] + 1:
            joined_ranges.append((lower_bound, upper_bound))
    allowed_ips = 0
    for index in range(0, len(joined_ranges) - 1):
        allowed_ips += joined_ranges[index+1][0] - joined_ranges[index][1] - 1
    allowed_ips += max_ip_addr - joined_ranges[-1][1]
    return allowed_ips
