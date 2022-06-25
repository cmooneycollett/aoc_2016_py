"""
Solutions for AOC 2016 Day 2.
"""


from src.utils.cartography import Location2D


def process_input_file():
    """
    Processes the AOC 2016 Day 2 input file into the format required by the
    solver functions. Returned value is a list containing the strings listed
    in the input file.
    """
    with open("./inputs/day_02.txt", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(input_data):
    """
    Follows the instructions listed in the input data to determine the code to
    the Easter Bunny HQ bathroom door.
    """
    door_code = []
    keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    loc = Location2D(1, 1)  # Start at the "5" button
    for instruction in input_data:
        for char in instruction:
            match char:
                case "U":
                    if loc.loc_y > 0:
                        loc = Location2D(loc.loc_x, loc.loc_y - 1)
                case "L":
                    if loc.loc_x > 0:
                        loc = Location2D(loc.loc_x - 1, loc.loc_y)
                case "R":
                    if loc.loc_x < len(keypad[loc.loc_y]) - 1:
                        loc = Location2D(loc.loc_x + 1, loc.loc_y)
                case "D":
                    if loc.loc_y < len(keypad) - 1:
                        loc = Location2D(loc.loc_x, loc.loc_y + 1)
        # Add the button at the current location to the door code
        door_code.append(keypad[loc.loc_y][loc.loc_x])
    return "".join(door_code)


def solve_part2(input_data):
    """
    Follows the instructions listed in the input data to determine the code to
    the Easter Bunny HQ bathroom door, using the more complex keypad
    arrangement.
    """
    door_code = []
    # Pad invalid cells with "0" to make up a neat 5x5 grid
    keypad = [["0", "0", "1", "0", "0"], ["0", "2", "3", "4", "0"],
              ["5", "6", "7", "8", "9"], ["0", "A", "B", "C", "0"],
              ["0", "0", "D", "0", "0"]]
    loc = Location2D(0, 2)  # Start at the "5" button
    for instruction in input_data:
        for char in instruction:
            # Check if the next move can be made, otherwise no chance to loc
            match char:
                case "U":
                    new_loc = Location2D(loc.loc_x, loc.loc_y - 1)
                    if loc.loc_y > 0 and \
                            keypad[new_loc.loc_y][new_loc.loc_x] != "0":
                        loc = new_loc
                case "L":
                    new_loc = Location2D(loc.loc_x - 1, loc.loc_y)
                    if loc.loc_x > 0 and \
                            keypad[new_loc.loc_y][new_loc.loc_x] != "0":
                        loc = new_loc
                case "R":
                    new_loc = Location2D(loc.loc_x + 1, loc.loc_y)
                    if loc.loc_x < len(keypad[loc.loc_y]) - 1 and \
                            keypad[new_loc.loc_y][new_loc.loc_x] != "0":
                        loc = new_loc
                case "D":
                    new_loc = Location2D(loc.loc_x, loc.loc_y + 1)
                    if loc.loc_y < len(keypad) - 1 and \
                            keypad[new_loc.loc_y][new_loc.loc_x] != "0":
                        loc = new_loc
        # Add the button at the current location to the door code
        door_code.append(keypad[loc.loc_y][loc.loc_x])
    return "".join(door_code)
