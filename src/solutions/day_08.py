"""
Solutions for AOC 2016 Day 8.
"""

from enum import Enum, auto, unique
import re


@unique
class Instruction(Enum):
    """
    Represents the different instructions that can be applied to the screen in
    AOC 2016 Day 8.
    """
    RECT = auto()
    ROTATE_ROW = auto()
    ROTATE_COL = auto()


def process_input_file():
    """
    Processes the AOC 2016 Day 8 input file into the format required by the
    solver functions.
    """
    input_data = []  # store tuples containing instruction and parameters
    regex_rect = re.compile(r"^rect (\d+)x(\d+)$")
    regex_rotate_row = re.compile(r"^rotate row y=(\d+) by (\d+)$")
    regex_rotate_col = re.compile(r"^rotate column x=(\d+) by (\d+)$")
    with open("./input/day_08.txt", encoding="utf-8") as file:
        for line in file.readlines():
            # Skip empty lines
            line = line.strip()
            if len(line) == 0:
                continue
            if (match_rect := regex_rect.match(line)) is not None:
                width = int(match_rect.group(1))
                height = int(match_rect.group(2))
                input_data.append((Instruction.RECT, width, height))
            elif (match_rotate_row := regex_rotate_row.match(line)) is not None:
                row = int(match_rotate_row.group(1))
                shift = int(match_rotate_row.group(2))
                input_data.append((Instruction.ROTATE_ROW, row, shift))
            elif (match_rotate_col := regex_rotate_col.match(line)) is not None:
                col = int(match_rotate_col.group(1))
                shift = int(match_rotate_col.group(2))
                input_data.append((Instruction.ROTATE_COL, col, shift))
    return input_data


def solve_part1(input_data):
    """
    Solves AOC 2016 Day 8 Part 1 // Applies the instructions given in the input
    data and counts how many pixels are lit after all instructions have been
    executed.
    """
    screen_grid = [["." for _ in range(0, 50)] for _ in range(0, 6)]
    for (instruction, param_1, param_2) in input_data:
        match instruction:
            case Instruction.RECT:
                width = param_1
                height = param_2
                for loc_y in range(0, height):
                    for loc_x in range(0, width):
                        screen_grid[loc_y][loc_x] = "#"  # pixel set to "on"
            case Instruction.ROTATE_ROW:
                row = param_1
                shift = param_2
                for _ in range(0, shift):
                    # Copy prior row, so changes don't change prior state record
                    prior_row = list(screen_grid[row])
                    for old_x in range(0, len(screen_grid[row])):
                        new_x = (old_x + 1) % len(screen_grid[row])
                        screen_grid[row][new_x] = prior_row[old_x]
            case Instruction.ROTATE_COL:
                col = param_1
                shift = param_2
                for _ in range(0, shift):
                    # List generator to create copy of prior column state
                    prior_col = [row[col] for row in screen_grid]
                    for old_y in range(0, len(screen_grid)):
                        new_y = (old_y + 1) % len(screen_grid)
                        screen_grid[new_y][col] = prior_col[old_y]
    return sum(row.count("#") for row in screen_grid)


def solve_part2(input_data):
    """
    Solves AOC 2016 Day 8 Part 2 // ###
    """
    return ()