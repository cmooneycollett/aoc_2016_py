"""
Solutions for AOC 2016 Day 12.
"""


from copy import deepcopy
from src.utils.assembunny import AssembunnyInterpreter


def process_input_file():
    """
    Processes the AOC 2016 Day 12 input file into the format required by the
    solver functions. Returned value is assembunny interpreter initialised with
    the instructions given in the input file.
    """
    with open("./input/day_12.txt", encoding="utf-8") as file:
        return AssembunnyInterpreter(file.read())


def solve_part1(assembunny_interpreter):
    """
    Solves AOC 2016 Day 12 Part 1 // Executes the assembunny program in the
    given assembunny interpreter, returning the resulting value in register "a".
    """
    assembunny_interpreter = deepcopy(assembunny_interpreter)
    assembunny_interpreter.execute_program()
    return assembunny_interpreter.get_register("a")


def solve_part2(assembunny_interpreter):
    """
    Solves AOC 2016 Day 12 Part 2 // Executes the assembunny program in the
    given assembunny interpreter with register "c" initialised to 1, returning
    the resulting value held in register "a".
    """
    assembunny_interpreter = deepcopy(assembunny_interpreter)
    assembunny_interpreter.set_register("c", 1)
    assembunny_interpreter.execute_program()
    return assembunny_interpreter.get_register("a")
