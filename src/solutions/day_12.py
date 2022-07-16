"""
Solutions for AOC 2016 Day 12.
"""


from enum import Enum, auto, unique
import re


@unique
class Instruction(Enum):
    """
    Represents the different assembunny code instructions.
    """
    COPY = auto()           # cpy
    INCREASE = auto()       # inc
    DECREASE = auto()       # dec
    JUMP_NOT_ZERO = auto()  # jnz


def process_input_file():
    """
    Processes the AOC 2016 Day 12 input file into the format required by the
    solver functions. Returned value is list of tuples representing the
    assembunny code instructions given in the input file.
    """
    input_data = []
    regex_cpy = re.compile(r"^cpy ([abcd]|-?\d+) ([abcd])$")
    regex_inc = re.compile(r"^inc ([abcd])$")
    regex_dec = re.compile(r"^dec ([abcd])$")
    regex_jnz = re.compile(r"^jnz ([abcd]|-?\d+) (-?\d+)$")
    with open("./input/day_12.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if (match_cpy := regex_cpy.match(line)) is not None:
                param_1 = match_cpy.group(1)
                param_2 = match_cpy.group(2)
                input_data.append((Instruction.COPY, param_1, param_2))
            elif (match_inc := regex_inc.match(line)) is not None:
                param_1 = match_inc.group(1)
                input_data.append((Instruction.INCREASE, param_1))
            elif (match_dec := regex_dec.match(line)) is not None:
                param_1 = match_dec.group(1)
                input_data.append((Instruction.DECREASE, param_1))
            elif (match_jnz := regex_jnz.match(line)) is not None:
                param_1 = match_jnz.group(1)
                param_2 = match_jnz.group(2)
                input_data.append(
                    (Instruction.JUMP_NOT_ZERO, param_1, param_2))
    return input_data


def solve_part1(input_data):
    """
    Solves AOC 2016 Day 12 Part 1 // Executes the assembunny instructions given
    in the input data, and returns the resulting value held in register "a".
    """
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    execute_assembunny_program(input_data, registers)
    return registers["a"]


def solve_part2(input_data):
    """
    Solves AOC 2016 Day 12 Part 2 // Executes the assembunny instructions given
    in the input data with register "c" initialised to 1, and returns the
    resulting value held in register "a".
    """
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    execute_assembunny_program(input_data, registers)
    return registers["a"]


def execute_assembunny_program(assembunny_program, registers):
    """
    Executes the given assembunny program, using the given registers.
    """
    program_counter = 0
    while 0 <= program_counter < len(assembunny_program):
        instruct = assembunny_program[program_counter]
        match instruct[0]:
            case Instruction.COPY:
                value = try_register_read(instruct[1], registers)
                registers[instruct[2]] = value
            case Instruction.INCREASE:
                registers[instruct[1]] += 1
            case Instruction.DECREASE:
                registers[instruct[1]] -= 1
            case Instruction.JUMP_NOT_ZERO:
                value = try_register_read(instruct[1], registers)
                if value != 0:
                    program_counter += int(instruct[2])
                    program_counter -= 1
        program_counter += 1


def try_parse_int(string):
    """
    Trys to parse the input string as an integer, otherwise returns the given
    string if the conversion fails.
    """
    try:
        return int(string)
    except ValueError:
        return string


def try_register_read(param, registers):
    """
    Trys to read from the registers using the param (if it is a letter).
    Otherwise returns the integer conversion of the param.
    """
    if param.isnumeric():
        return int(param)
    return registers[param]
