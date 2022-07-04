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
    return calculate_decompressed_length(input_data)


def solve_part2(_input_data):
    """
    Solves AOC 2016 Day 9 Part 2 // ###
    """
    return -1


def calculate_decompressed_length(input_data):
    """
    Processes the input data to determine the decompressed length of the file
    it represents. Function assumes the input data is correctly formatted and
    not corrupt, meaning the character sequence specified by a marker should
    not run past the end of the input data.
    """
    decompressed_length = 0
    regex_marker = re.compile(r"\((\d+)x(\d+)\)")
    index = 0
    while index < len(input_data):
        if input_data[index] != "(":
            index += 1
            decompressed_length += 1
            continue
        # We have found the start of a marker
        index_la = index + 1
        while index_la < len(input_data):
            if input_data[index_la] == ")":
                break
            index_la += 1
        # Extract the sequence length and number of repeats from the marker
        match_marker = regex_marker.search(input_data[index:index_la + 1])
        sequence_len = int(match_marker.group(1))
        repeats = int(match_marker.group(2))
        decompressed_length += sequence_len * repeats
        index = index_la + 1 + sequence_len
    return decompressed_length
