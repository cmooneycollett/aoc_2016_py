"""
Solutions for AOC 2016 Day 5.
"""


import hashlib


def process_input_file():
    """
    Processes the AOC 2016 Day 5 input file into the format required by the
    solver functions. Returned value is the string representing the door ID
    given in the input file.
    """
    with open("./input/day_05.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Determines the eight-character password for the first door by extracting
    sixth character from successive MD5 hashes found to commence with five
    zeroes.
    """
    index = 0
    door_password = []
    door_id = input_data
    while len(door_password) < 8:
        # Keep conducting hashes until next valid hash is found
        hash_result = hashlib.md5(f"{door_id}{index}".encode())
        index += 1
        hex_digest = hash_result.hexdigest()
        # Check for "interesting" hash
        if hex_digest.startswith("00000"):
            door_password.append(hex_digest[5])
    return "".join(door_password)


def solve_part2(input_data):
    return -1
