"""
Solutions for AOC 2016 Day 16.
"""


def process_input_file():
    """
    Processes the AOC 2016 Day 16 input file into the format required by the
    solver functions. Returned value is the initial state given in the input
    file for the modified dragon curve algorithm.
    """
    with open("./input/day_16.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(initial_state):
    """
    Solves AOC 2016 Day 16 Part 1 // Determines the "checksum" for the data
    generated using modified dragon curve algorithm to fill a disk of length
    272.
    """
    dragon_data_blob = generate_dragon_curve_data(initial_state, 272)
    return generate_checksum(dragon_data_blob)


def solve_part2(initial_state):
    """
    Solves AOC 2016 Day 16 Part 2 // ###
    """
    return -1


def apply_dragon_curve_iteration(initial_state):
    """
    Applies a single iteration of the modified dragon curve algorithm to the
    given initial state, returning the output of the iteration.
    """
    modified_half = list(initial_state[::-1])
    for (index, char) in enumerate(modified_half):
        match char:
            case "0":
                modified_half[index] = "1"
            case "1":
                modified_half[index] = "0"
    modified_half = "".join(modified_half)
    return f"{initial_state}0{modified_half}"


def generate_dragon_curve_data(initial_state, disk_length):
    """
    Generates a blob of data using the modified dragon curve algorithm to fill
    the given disk length.
    """
    dragon_data_blob = initial_state
    while len(dragon_data_blob) < disk_length:
        dragon_data_blob = apply_dragon_curve_iteration(dragon_data_blob)
    return dragon_data_blob[:disk_length]


def apply_checksum_iteration(input_data):
    """
    Applies a single iteration of the dragon curve checksum algorithm to the
    given dragon data blob.
    """
    if len(input_data) % 2 == 1:
        return input_data
    checksum = ""
    for index in range(0, len(input_data), 2):
        match input_data[index:index+2]:
            case "00" | "11":
                checksum += "1"
            case "01" | "10":
                checksum += "0"
    return checksum


def generate_checksum(dragon_data_blob):
    """
    Processes the dragon data blob until the checksum has an odd number of
    characters.
    """
    input_data = apply_checksum_iteration(dragon_data_blob)
    while len(input_data) % 2 == 0:
        input_data = apply_checksum_iteration(input_data)
    return input_data
