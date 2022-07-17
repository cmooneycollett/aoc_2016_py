"""
Solutions for AOC 2016 Day 15.
"""


import re


class Disc:
    """
    Represents a rotating disk with one slot and a set number of total
    positions.
    """

    def __init__(self, disc_num, total_pos, start_pos):
        self.disc_num = disc_num
        self.total_pos = total_pos
        self.start_pos = start_pos
        self.offset = (total_pos - start_pos) % total_pos

    def validate_time(self, time):
        """
        Checks if the slot position of the disk will be aligned with the capsule
        if the button is pressed at the given time.
        """
        if time + self.disc_num < self.offset:
            return False
        return (time + self.disc_num - self.offset) % self.total_pos == 0


def process_input_file():
    """
    Processes the AOC 2016 Day 15 input file into the format required by the
    solver functions. Returned value is list of Disc objects, which specified
    the number, total positions and starting position of each disc listed in the
    input file.
    """
    regex_disc = re.compile(
        r"^Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).$")
    discs = []
    with open("./input/day_15.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if (match_disc := regex_disc.match(line)) is not None:
                disc_num = int(match_disc.group(1))
                total_pos = int(match_disc.group(2))
                start_pos = int(match_disc.group(3))
                discs.append(Disc(disc_num, total_pos, start_pos))
    return discs


def solve_part1(discs):
    """
    Solves AOC 2016 Day 15 Part 1 // Determines the first time at which the
    button can be pressed in order to get a capsule to fall through all discs,
    specified in the input data.
    """
    time = 0
    while True:
        valid_time = True
        for disc in discs:
            if not disc.validate_time(time):
                valid_time = False
                break
        if valid_time:
            break
        time += 1
    return time


def solve_part2(input_data):
    """
    Solves AOC 2016 Day 15 Part 2 // ###
    """
    return -1
