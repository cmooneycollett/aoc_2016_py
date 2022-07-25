"""
This module contains the code required to parse and interpret assembunny code.
"""


from enum import Enum, auto, unique
import re


@unique
class AssembunnyOperation(Enum):
    """
    Represents the different assembunny code operations.
    """
    COPY = auto()           # cpy
    INCREASE = auto()       # inc
    DECREASE = auto()       # dec
    JUMP_NOT_ZERO = auto()  # jnz
    TOGGLE = auto()         # tgl


class AssembunnyInterpreter:
    """
    Represents a computer that can interpret assembunny code.
    """

    def __init__(self, raw_input):
        self.registers = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.program_counter = 0
        self.instructions = self.parse_raw_input(raw_input)

    def try_register_read(self, param):
        """
        Trys to read from the registers using the param (if it is a letter).
        Otherwise returns the integer conversion of the param.
        """
        if isinstance(param, int):
            return param
        elif param.strip("-").isnumeric():
            return int(param)
        return self.registers[param]

    def get_register(self, reg):
        """
        Gets the value of the requested register.
        """
        return self.registers[reg]

    def set_register(self, reg, value):
        """
        Sets the value of the requested register to the given value.
        """
        old_value = self.registers[reg]
        self.registers[reg] = value
        return old_value

    def execute_program(self):
        """
        Executes the program loaded into the assembunny interpreter, halting
        when the program counter is outside of the instruction space.
        """
        while 0 <= self.program_counter < len(self.instructions):
            instruct = self.instructions[self.program_counter]
            match instruct[0]:
                case AssembunnyOperation.COPY:
                    if isinstance(instruct[2], str):
                        value = self.try_register_read(instruct[1])
                        self.registers[instruct[2]] = value
                case AssembunnyOperation.INCREASE:
                    if isinstance(instruct[1], str):
                        self.registers[instruct[1]] += 1
                case AssembunnyOperation.DECREASE:
                    if isinstance(instruct[1], str):
                        self.registers[instruct[1]] -= 1
                case AssembunnyOperation.JUMP_NOT_ZERO:
                    value = self.try_register_read(instruct[1])
                    if value != 0:
                        self.program_counter += self.try_register_read(instruct[2])
                        self.program_counter -= 1
                case AssembunnyOperation.TOGGLE:
                    target_index = self.program_counter + \
                        self.try_register_read(instruct[1])
                    # Ignore any toggles targeting index outside instruct space
                    if 0 <= target_index < len(self.instructions):
                        target_instruct = self.instructions[target_index]
                        match target_instruct[0]:
                            case AssembunnyOperation.COPY:  # 2-arg
                                target_instruct = (AssembunnyOperation.JUMP_NOT_ZERO,
                                    target_instruct[1], target_instruct[2])
                            case AssembunnyOperation.INCREASE:  # 1-arg
                                target_instruct = (AssembunnyOperation.DECREASE,
                                    target_instruct[1])
                            case AssembunnyOperation.DECREASE:  # 1-arg
                                target_instruct = (AssembunnyOperation.INCREASE,
                                    target_instruct[1])
                            case AssembunnyOperation.JUMP_NOT_ZERO: # 2-arg
                                target_instruct = (AssembunnyOperation.COPY,
                                    target_instruct[1], target_instruct[2])
                            case AssembunnyOperation.TOGGLE:    # 1-arg
                                target_instruct = (AssembunnyOperation.INCREASE,
                                    target_instruct[1])
                        self.instructions[target_index] = target_instruct
            self.program_counter += 1

    @classmethod
    def parse_raw_input(cls, raw_input):
        """
        Processes raw input and converts it into the corresponding instructions
        in assembuny code.
        """
        instructions = []
        regex_cpy = re.compile(r"^cpy ([abcd]|-?\d+) ([abcd])$")
        regex_inc = re.compile(r"^inc ([abcd])$")
        regex_dec = re.compile(r"^dec ([abcd])$")
        regex_jnz = re.compile(r"^jnz ([abcd]|-?\d+) ([abcd]|-?\d+)$")
        regex_tgl = re.compile(r"^tgl ([abcd]|-?\d+)$")
        for line in raw_input.splitlines():
            if len(line := line.strip()) == 0:
                continue
            if match_cpy := regex_cpy.match(line):
                param1 = match_cpy.group(1)
                param2 = match_cpy.group(2)
                instructions.append((AssembunnyOperation.COPY, param1, param2))
            elif match_inc := regex_inc.match(line):
                param1 = match_inc.group(1)
                instructions.append((AssembunnyOperation.INCREASE, param1))
            elif match_dec := regex_dec.match(line):
                param1 = match_dec.group(1)
                instructions.append((AssembunnyOperation.DECREASE, param1))
            elif match_jnz := regex_jnz.match(line):
                param1 = match_jnz.group(1)
                param2 = match_jnz.group(2)
                instructions.append(
                    (AssembunnyOperation.JUMP_NOT_ZERO, param1, param2))
            elif match_tgl := regex_tgl.match(line):
                param1 = match_tgl.group(1)
                instructions.append((AssembunnyOperation.TOGGLE, param1))
        return instructions
