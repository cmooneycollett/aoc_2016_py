"""
Solutions for AOC 2016 Day 21.
"""


from enum import Enum, auto, unique
import re

from ordered_set import OrderedSet


@unique
class ScramblerInstruction(Enum):
    """
    Represents the different instructions that can be executed by the scrambler.
    """
    SWAP_POS = auto()
    SWAP_LETTER = auto()
    ROTATE_LEFT = auto()
    ROTATE_RIGHT = auto()
    ROTATE_BASED_LETTER = auto()
    REVERSE_POS = auto()
    MOVE_POS = auto()


def process_input_file():
    """
    Processes the AOC 2016 Day 21 input file into the format required by the
    solver functions. Returned value is the list of scrambler instructions given
    in the input file.
    """
    instructions = []
    regex_swap_pos = re.compile(r"^swap position (\d+) with position (\d+)$")
    regex_swap_letter = re.compile(r"^swap letter ([a-z]) with letter ([a-z])$")
    regex_rotate_left = re.compile(r"^rotate left (\d+) step[s]?$")
    regex_rotate_right = re.compile(r"^rotate right (\d+) step[s]?$")
    regex_rotate_based_letter = re.compile(r"^rotate based on position of letter ([a-z])$")
    regex_reverse_pos = re.compile(r"^reverse positions (\d+) through (\d+)$")
    regex_move_pos = re.compile(r"^move position (\d+) to position (\d+)$")
    with open("./input/day_21.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if (match_swap_pos := regex_swap_pos.match(line)):
                param1 = int(match_swap_pos.group(1))
                param2 = int(match_swap_pos.group(2))
                instructions.append((ScramblerInstruction.SWAP_POS, param1, param2))
            elif (match_swap_letter := regex_swap_letter.match(line)):
                param1 = match_swap_letter.group(1)
                param2 = match_swap_letter.group(2)
                instructions.append((ScramblerInstruction.SWAP_LETTER, param1, param2))
            elif (match_rotate_left := regex_rotate_left.match(line)):
                param1 = int(match_rotate_left.group(1))
                instructions.append((ScramblerInstruction.ROTATE_LEFT, param1))
            elif (match_rotate_right := regex_rotate_right.match(line)):
                param1 = int(match_rotate_right.group(1))
                instructions.append((ScramblerInstruction.ROTATE_RIGHT, param1))
            elif (match_rotate_based_letter := regex_rotate_based_letter.match(line)):
                param1 = match_rotate_based_letter.group(1)
                instructions.append((ScramblerInstruction.ROTATE_BASED_LETTER, param1))
            elif (match_reverse_pos := regex_reverse_pos.match(line)):
                param1 = int(match_reverse_pos.group(1))
                param2 = int(match_reverse_pos.group(2))
                instructions.append((ScramblerInstruction.REVERSE_POS, param1, param2))
            elif (match_move_pos := regex_move_pos.match(line)):
                param1 = int(match_move_pos.group(1))
                param2 = int(match_move_pos.group(2))
                instructions.append((ScramblerInstruction.MOVE_POS, param1, param2))
    return instructions


def solve_part1(operations):
    """
    Solves AOC 2016 Day 21 Part 1 // Determines the result of passing the string
    "abcdefgh" through the given scrambler operations.
    """
    output = list("abcdefgh")
    for opera in operations:
        match opera[0]:
            case ScramblerInstruction.SWAP_POS:
                pos_left = opera[1]
                pos_right = opera[2]
                letter_left = output[pos_left]
                letter_right = output[pos_right]
                output[pos_right] = letter_left
                output[pos_left] = letter_right
            case ScramblerInstruction.SWAP_LETTER:
                pos_left = output.index(opera[1])
                pos_right = output.index(opera[2])
                output[pos_left] = opera[2]
                output[pos_right] = opera[1]
            case ScramblerInstruction.ROTATE_LEFT:
                new_output = list(output)
                for (index, char) in enumerate(output):
                    new_index = index - opera[1]
                    if new_index < 0:
                        new_index += len(output)
                    new_output[new_index] = char
                output = new_output
            case ScramblerInstruction.ROTATE_RIGHT:
                new_output = list(output)
                for (index, char) in enumerate(output):
                    new_index = (index + opera[1]) % len(output)
                    new_output[new_index] = char
                output = new_output
            case ScramblerInstruction.ROTATE_BASED_LETTER:
                # Calculate number of steps
                steps = output.index(opera[1])
                if steps >= 4:
                    steps += 1
                steps += 1
                new_output = list(output)
                for (index, char) in enumerate(output):
                    new_index = (index + steps) % len(output)
                    new_output[new_index] = char
                output = new_output
            case ScramblerInstruction.REVERSE_POS:
                slice_rev = output[opera[1]:opera[2] + 1][::-1]
                for index in range(opera[1], opera[2] + 1):
                    output[index] = slice_rev[index - opera[1]]
            case ScramblerInstruction.MOVE_POS:
                letter = output[opera[1]]
                output.remove(output[opera[1]])
                output.insert(opera[2], letter)
    return "".join(output)


def solve_part2(input_data):
    """
    Solves AOC 2016 Day 21 Part 2 // ###
    """
    return -1
