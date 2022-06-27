"""
Solutions for AOC 2016 Day 4.
"""


from collections import Counter
import re


class Room:
    """
    Represents a Room as specified at the information kiosk in the Easter Bunny
    HQ.
    """

    def __init__(self, encrypted_name, sector_id, checksum):
        self.encrypted_name = encrypted_name
        self.sector_id = sector_id
        self.checksum = checksum

    def is_real_room(self):
        """
        Determines if the Room is a real room, by verifying if the checksum
        is correct as generated from the encrypted name.
        """
        # Count frequency of characters in encrypted name
        char_counts = Counter(self.encrypted_name)
        del char_counts["-"]    # Discount the "-" character
        if len(char_counts) < 5:
            return False
        # Sort the elements by their count, then alphabetically for ties
        elements_sorted = sorted(char_counts.most_common(),
                                 key=lambda count: (-count[1], count[0]))
        checksum = "".join(char for (char, _) in elements_sorted[0:5])
        return self.checksum == checksum

    def get_decrypted_name(self):
        """
        Returns the decrypted name of the room, determined by taking the
        encrypted name and forward-rotating the alphabetical characters a
        number of times equal to its sector ID.
        """
        decrypted_chars = list(self.encrypted_name)
        for (i, char) in enumerate(decrypted_chars):
            # Replace "-" with a single " "
            if char == "-":
                decrypted_chars[i] = " "
                continue
            # Rotate the current character through a-z by sector_id steps
            decrypted_chars[i] = chr(ord("a") + (ord(char) - ord("a") +
                                                 self.sector_id) % 26)
        decrypted_chars = "".join(decrypted_chars)
        return "".join(decrypted_chars)


def process_input_file():
    """
    Processes the AOC 2016 Day 4 input file into the format required by the
    solver functions. Returned value is a list containing the parsed Room
    objects specified in the input file.
    """
    input_data = []
    #regex_room = re.compile(r"([a-z\-])(\d+)\-\[([a-z]+)\]")
    regex_room = re.compile(r"([a-z\-]+)(\d+)\[([a-z]+)\]")
    with open("./input/day_04.txt", encoding="utf-8") as file:
        for line in file.readlines():
            # Ignore empty line
            line = line.strip()
            if len(line) == 0:
                continue
            # Extract room details
            match_room = regex_room.match(line)
            encrypted_name = match_room.group(1)[:-1]
            sector_id = int(match_room.group(2))
            checksum = match_room.group(3)
            room = Room(encrypted_name, sector_id, checksum)
            input_data.append(room)
    return input_data


def solve_part1(input_data):
    """
    Determines the sum of the sector IDs for all of the valid "rooms" given
    in the input data, with valid rooms being those with a checksum consisting
    of the five most common characters from its encrypted name (ties broken
    by alphabetical order).
    """
    sum_sector_id = 0
    for room in input_data:
        if room.is_real_room():
            sum_sector_id += room.sector_id
    return sum_sector_id


def solve_part2(input_data):
    """
    Returns the sector ID of the room whose decrypted (real) name indicates that
    it stores the North Pole objects.
    """
    for room in input_data:
        # Check if decrypted room name indicates room contains northpole objects
        decrypted_name = room.get_decrypted_name()
        if decrypted_name == "northpole object storage":
            return room.sector_id
    return -1
