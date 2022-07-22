"""
Solutions for AOC 2016 Day 19.
"""


def process_input_file():
    """
    Processes the AOC 2016 Day 19 input file into the format required by the
    solver functions. Returned value is the number of elves involved in the
    gift exchange game.
    """
    with open("./input/day_19.txt", encoding="utf-8") as file:
        return int(file.read().strip())


def solve_part1(num_elves):
    """
    Solves AOC 2016 Day 19 Part 1 // Determines which elf ends up with all of
    the presents when the gift exchange game ends (where elves in play steal the
    presents from the elf on their left), modelling the game on the Josephus
    problem with k=2.
    """
    power = 1
    value = 2
    while True:
        power += 1
        new_value = 2**power
        if new_value > num_elves:
            break
        value = new_value
    return 2 * (num_elves - value) + 1


def solve_part2(num_elves):
    """
    Solves AOC 2016 Day 19 Part 2 // Determines which elf ends up with all of
    the presents when the gift exchange game ends (where elves in play steal the
    presents from the elf directly opposite them in the circle).
    """
    elves_in_play = list(range(1, num_elves + 1))
    index = 0
    while len(elves_in_play) > 1:
        # Remove elf directly opposite from current elf (left elf for tie-break)
        target = (index + len(elves_in_play) // 2) % len(elves_in_play)
        del elves_in_play[target]
        # Accomodate for removing an elf earlier in the list
        if target < index:
            index -= 1
        index = (index + 1) % len(elves_in_play)
    return elves_in_play[0]
