"""
Solutions for AOC 2016 Day 23.
"""


from copy import deepcopy
from src.utils.assembunny import AssembunnyInterpreter


def process_input_file():
    """
    Processes the AOC 2016 Day 23 input file into the format required by the
    solver functions. Returned value is an assembunny interpreter instance
    initialised with the assembunny code instructions given in the input file.
    """
    with open("./input/day_23.txt", encoding="utf-8") as file:
        return AssembunnyInterpreter(file.read())


def solve_part1(assembunny_interpreter):
    """
    Solves AOC 2016 Day 23 Part 1 // Runs the program in the assembunny code
    interpreter with register "a" initialised to 7 (all others initialised to 0)
    and returns the value saved to register "a" (the value that should be sent
    to the safe).
    """
    assembunny_interpreter = deepcopy(assembunny_interpreter)
    assembunny_interpreter.set_register("a", 7)
    assembunny_interpreter.execute_program()
    return assembunny_interpreter.get_register("a")


def solve_part2(assembunny_interpreter):
    """
    Solves AOC 2016 Day 23 Part 2 // Runs the program in the assembunny code
    interpreter with register "a" initialised to 12 (all others initialised to
    0) and returns the value saved to register "a" (the value that should be
    sent to the safe).
    """
    assembunny_interpreter = deepcopy(assembunny_interpreter)
    assembunny_interpreter.set_register("a", 12)
    assembunny_interpreter.execute_program()
    return assembunny_interpreter.get_register("a")
