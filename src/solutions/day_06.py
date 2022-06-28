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
        return [line.strip() for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(input_data):
    """
    Processes the messages in the input data to determine the error-corrected
    version of the message, by determining the most-common character in each of
    the message character positions.
    """
    message_error_corrected = ""
    position_counters = determine_message_position_counters(input_data)
    for counter in position_counters:
        message_error_corrected += counter.most_common()[0][0]
    return message_error_corrected


def solve_part2(input_data):
    """
    Processes the messages in the input data to determine the error-corrected
    version of the message, by determining the least-common character in each of
    the message character positions.
    """
    message_error_corrected = ""
    position_counters = determine_message_position_counters(input_data)
    for counter in position_counters:
        # Reverse-sort the counter for the least common character is first
        reverse_sorted_counter = sorted(
            counter.most_common(), key=lambda item: item[1])
        message_error_corrected += reverse_sorted_counter[0][0]
    return message_error_corrected


def determine_message_position_counters(messages):
    """
    Processes the given messages, to return a list of strings representing the
    characters from each respective position in the messages.
    """
    position_chars = ["" for _ in range(0, 8)]
    counters = []
    for message in messages:
        for position in range(0, 8):
            position_chars[position] += message[position]
    for chars in position_chars:
        counters.append(Counter(chars))
    return counters
