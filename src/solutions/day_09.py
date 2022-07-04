"""
Solutions for AOC 2016 Day 9.
"""


import re


def process_input_file():
    """
    Processes the AOC 2016 Day 9 input file into the format required by the
    solver functions. Returned value is a string containing the "file" contents
    given in the input file.
    """
    with open("./input/day_09.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Solves AOC 2016 Day 9 Part 1 // Uses Version 1 decompression method to
    determine the decompressed length of the file given in the input data.
    """
    return calculate_decompressed_length(input_data,
                                         use_version_two_decompression=False)


def solve_part2(input_data):
    """
    Solves AOC 2016 Day 9 Part 2 // Uses Version 2 decompression method to
    determine the decompressed length of the file, through decompressing any
    decompression markers within decompressed data.
    """
    return calculate_decompressed_length(input_data,
                                         use_version_two_decompression=True)


def calculate_decompressed_length(input_data,
                                  use_version_two_decompression=False):
    """
    Processes the input data to determine the decompressed length of the file
    it represents. Function assumes the input data is correctly formatted and
    not corrupt, meaning the character sequence specified by a marker should
    not run past the end of the input data.

    If the use_version_two_decompression parameter is set to True, the input
    data decompressed length is calculated by decompressing marker sequences
    containing within decompressed data.
    """
    decompressed_length = 0
    regex_marker = re.compile(r"\((\d+)x(\d+)\)")
    index = 0
    while index < len(input_data):
        if input_data[index] != "(":    # Not within a marked sequence
            index += 1
            decompressed_length += 1
            continue
        # We have found the start of a marker
        index_la = index + 1    # Look-ahead index
        while index_la < len(input_data):
            if input_data[index_la] == ")":
                break
            index_la += 1
        # Extract the sequence length and number of repeats from the marker
        match_marker = regex_marker.search(input_data[index:index_la + 1])
        sequence_len = int(match_marker.group(1))
        repeats = int(match_marker.group(2))
        # Calculate the length of the marker sequence
        if not use_version_two_decompression:
            decompressed_length += sequence_len * repeats
        else:
            # Extract the top-level decompression target and decompress
            decompression_target = input_data[
                index_la + 1: index_la + 1 + sequence_len]
            sub_decompressed_length = calculate_decompressed_length(
                decompression_target, use_version_two_decompression)
            decompressed_length += sub_decompressed_length * repeats
        # Look-ahead index will be index of the last ")" for top-level sequence
        index = index_la + 1 + sequence_len
    return decompressed_length
