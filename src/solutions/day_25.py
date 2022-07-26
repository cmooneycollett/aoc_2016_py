"""
Solutions for AOC 2016 Day 25.
"""

from copy import deepcopy
from src.utils.assembunny import AssembunnyInterpreter


def process_input_file():
    """
    Processes the AOC 2016 Day 25 input file into the format required by the
    solver functions. Returned value is an assembunny interpreter loaded with
    the assembunny code given in the input file.
    """
    with open("./input/day_25.txt", encoding="utf-8") as file:
        return AssembunnyInterpreter(file.read())


def solve_part1(assembunny_interpreter):
    """
    Solves AOC 2016 Day 25 Part 1 // Determines the lowest positive integer that
    can be used to initialize assembunny interpreter register "a" and cause the
    code to output the repeating clock signal indefinitely (modelled by this
    function as 1000 consecutive "good" clock tones).
    """
    seed = 1    # Initialised the assembunny interpreter "a" register
    cap = 1000  # Look for 1000 consecutive "good" clock tones
    while True:
        # Initialise the assembunny interpreter with the seed value
        test_interpreter = deepcopy(assembunny_interpreter)
        test_interpreter.set_register("a", seed)
        last_transmit = 1
        seen = 0
        for transmit in test_interpreter.execute_program():
            # Check if the transmitted value is a "good" clock tone
            if transmit == 0 and last_transmit == 1 or \
                    transmit == 1 and last_transmit == 0:
                seen += 1
                last_transmit = transmit
                if seen == cap:
                    return seed
            else:
                break
        seed += 1


def solve_part2(assembunny_interpreter):
    """
    Solves AOC 2016 Day 25 Part 2 // ###
    """
    return -1
