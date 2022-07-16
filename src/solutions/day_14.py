"""
Solutions for AOC 2016 Day 14.
"""


from collections import deque
import hashlib
import re


def process_input_file():
    """
    Processes the AOC 2016 Day 14 input file into the format required by the
    solver functions. Returned value is the pre-arranged salt string given in
    the input file.
    """
    with open("./input/day_14.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(salt):
    """
    Solves AOC 2016 Day 14 Part 1 // Determines the index that produces the 64th
    key for the one-time pad (without using key-stretching).
    """
    return find_index_for_key(salt, 64, use_key_stretching=False)


def solve_part2(salt):
    """
    Solves AOC 2016 Day 14 Part 2 // Determines the index that produces the 64th
    key for the one-time pad, with key-stretching enabled.
    """
    return find_index_for_key(salt, 64, use_key_stretching=True)


def find_index_for_key(salt, key_ord, use_key_stretching=False):
    """
    Determines the index required to produce the n'th key, using the given salt.
    Key-stretching can be utilised if required.
    """
    # Initialise the hash queue
    hash_queue = deque([])  # Storing: (index, MD5 hex digest)
    for index in range(0, 1000):
        hex_digest = calculate_md5_hexdigest(salt, index, use_key_stretching)
        hash_queue.append((index, hex_digest))
    keys_found = 0
    regex_char_triple = re.compile(r"([a-z0-9])\1\1")
    while True:
        # Pop hash and add new one to the end
        (index, hex_digest) = hash_queue.popleft()
        backfill_index = hash_queue[-1][0] + 1
        backfill_hex_digest = calculate_md5_hexdigest(salt, backfill_index,
                                                      use_key_stretching)
        hash_queue.append((backfill_index, backfill_hex_digest))
        # Check if current hex digest has character triple
        if (match_char_triple := regex_char_triple.search(hex_digest)) is not None:
            # Check the hash queue for character quintuple
            regex_char_quintuple = re.compile(
                rf"({match_char_triple.group(1)})\1\1\1\1")
            quintuple_found = False
            for (_, queue_hex_digest) in hash_queue:
                if regex_char_quintuple.search(queue_hex_digest) is not None:
                    quintuple_found = True
                    break
            if quintuple_found:
                keys_found += 1
        if keys_found == key_ord:
            return index


def calculate_md5_hexdigest(salt, index, use_key_stretching=False):
    """
    Calculates the MD5 hash from the given salt and index. Key-stretching can be
    utilised if required.
    """
    hex_digest = hashlib.md5(f"{salt}{index}".encode()).hexdigest()
    if use_key_stretching:
        for _ in range(0, 2016):
            hex_digest = hashlib.md5(hex_digest.encode()).hexdigest()
    return hex_digest
