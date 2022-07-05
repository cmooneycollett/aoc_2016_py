"""
Solutions for AOC 2016 Day 10.
"""

from copy import deepcopy
from dataclasses import dataclass
from enum import Enum, auto, unique
import re


@unique
class Entity(Enum):
    """
    Represents the different entities that can receive microchips.
    """
    BOT = auto()
    OUTPUT = auto()

    @staticmethod
    def from_string(input_string):
        """
        Converts the given string into the corresponding enum member. Returns
        None if the input string does not match an enum member.
        """
        match input_string.lower():
            case "bot":
                return Entity.BOT
            case "output":
                return Entity.OUTPUT
            case _:
                return None


@dataclass
class BotInstruction:
    """
    Contains the fields in the instruction for a bot to distribute its
    microchips when it holds two microchips.
    """
    from_bot: int
    low_target: Entity
    low_id: int
    high_target: Entity
    high_id: int


def process_input_file():
    """
    Processes the AOC 2016 Day 10 input file into the format required by the
    solver functions. Returned value is a tuple containing the bots (with
    initial microchips), output bins and bot instructions (in this order).
    """
    regex_value = re.compile(r"^value (\d+) goes to bot (\d+)$")
    regex_bot_instruction = re.compile(r"^bot (\d+) gives low to (bot|output) "
                                       r"(\d+) and high to (bot|output) (\d+)$")
    bots = {}
    outputs = {}
    instructions = []
    with open("./input/day_10.txt", encoding="utf-8") as file:
        for line in file.readlines():
            # Ignore blank lines
            if len(line := line.strip()) == 0:
                continue
            if (match_value := regex_value.match(line)) is not None:
                value = int(match_value.group(1))
                bot_id = int(match_value.group(2))
                if bot_id not in bots:
                    bots[bot_id] = [value]
                else:
                    bots[bot_id].append(value)
            elif (match_bot_instruction := regex_bot_instruction.match(line)) is not None:
                from_bot = int(match_bot_instruction.group(1))
                low_target = Entity.from_string(match_bot_instruction.group(2))
                low_id = int(match_bot_instruction.group(3))
                high_target = Entity.from_string(
                    match_bot_instruction.group(4))
                high_id = int(match_bot_instruction.group(5))
                # Initial populate from bot into bots map
                if from_bot not in bots:
                    bots[from_bot] = []
                # Initial populate low target into bots or outputs map
                if low_target == Entity.BOT and low_id not in bots:
                    bots[low_id] = []
                elif low_target == Entity.OUTPUT and low_id not in outputs:
                    outputs[low_id] = []
                # Initial populate high target into bots or outputs map
                if high_target == Entity.BOT and high_id not in bots:
                    bots[high_id] = []
                elif high_target == Entity.OUTPUT and high_id not in outputs:
                    outputs[high_id] = []
                # Record the bot instruction
                instructions.append(BotInstruction(
                    from_bot, low_target, low_id, high_target, high_id))
    # Ensure the microchips in the bots and output bins are sorted
    for bot in list(bots.keys()):
        bots[bot] = sorted(bots[bot])
    for output in list(outputs.keys()):
        outputs[output] = sorted(outputs[output])
    return (bots, outputs, instructions)


def solve_part1(input_data):
    """
    Solves AOC 2016 Day 10 Part 1 // Determines the number of the bot that is
    responsible for comparing value-61 microchips with the value-17 microchips.
    """
    (bots, outputs, instructions) = deepcopy(input_data)
    # Check if initial bot state has a matching value
    for (bot, microchips) in bots.items():
        if len(microchips) == 2 and microchips[0] == 17 and microchips[1] == 61:
            return bot
    # Execute each instruction and check if the low or high bot matches
    processed_instructions = []
    while len(instructions) > 0:
        instruction_to_remove = []
        for instruction in instructions:
            if len(bots[instruction.from_bot]) != 2:
                continue
            instruction_to_remove.append(instruction)
            low_chip = bots[instruction.from_bot][0]
            high_chip = bots[instruction.from_bot][1]
            bots[instruction.from_bot] = []
            # Low chip
            if instruction.low_target == Entity.BOT:
                bots[instruction.low_id].append(low_chip)
                bots[instruction.low_id] = sorted(bots[instruction.low_id])
                if len(bots[instruction.low_id]) == 2 and \
                        bots[instruction.low_id][0] == 17 and \
                        bots[instruction.low_id][1] == 61:
                    return instruction.low_id
            else:
                outputs[instruction.low_id].append(low_chip)
                outputs[instruction.low_id] = sorted(
                    outputs[instruction.low_id])
            # High chip
            if instruction.high_target == Entity.BOT:
                bots[instruction.high_id].append(high_chip)
                bots[instruction.high_id] = sorted(bots[instruction.high_id])
                if len(bots[instruction.high_id]) == 2 and \
                        bots[instruction.high_id][0] == 17 and \
                        bots[instruction.high_id][1] == 61:
                    return instruction.high_id
            else:
                outputs[instruction.high_id].append(high_chip)
                outputs[instruction.high_id] = sorted(
                    outputs[instruction.high_id])
        if len(instruction_to_remove) == 0:
            break
        instructions.remove(instruction_to_remove[0])
        processed_instructions.append(instruction_to_remove[0])
    # Return a dummy value here to indicate failure
    return -1


def solve_part2(_input_data):
    """
    Solves AOC 2016 Day 10 Part 2 // ###
    """
    return -1
