"""
Solutions for AOC 2016 Day 6.
"""


from collections import Counter


def process_input_file():
    """
    Processes the AOC 2016 Day 6 input file into the format required by the
    solver functions. Returned value is a list with the eight-character messages
    given in the input file.
    """
    with open("./input/day_06.txt", encoding="utf-8") as file:
        return (line.strip() for line in file.readlines()
                if len(line.strip()) > 0)


def solve_part1(input_data):
    """
    Processes the messages in the input data to determine the error-corrected
    version of the message, by determining the most-common character in each
    of the each message character positions.
    """
    message_error_corrected = ""
    position_chars = ["" for _ in range(0, 8)]
    for message in input_data:
        for position in range(0, 8):
            position_chars[position] += message[position]
    for chars in position_chars:
        counter = Counter(chars)
        message_error_corrected += counter.most_common()[0][0]
    return message_error_corrected


def solve_part2(input_data):
    return -1
