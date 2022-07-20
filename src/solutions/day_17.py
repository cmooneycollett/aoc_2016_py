"""
Solutions for AOC 2016 Day 17.
"""

from collections import deque
import hashlib
from src.utils.cartography import Location2D


def process_input_file():
    """
    Processes the AOC 2016 Day 17 input file into the format required by the
    solver functions. Returns the Easter Bunny vault passcode given in the input
    file.
    """
    with open("./input/day_17.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(vault_passcode):
    """
    Solves AOC 2016 Day 17 Part 1 // Determines the shortest path from the
    starting location in the 4-by-4 room grid to the vault location in the
    bottom right of the grid.
    """
    # Starting location is (1,1) - target location is (4,4)
    state_queue = deque([(Location2D(1, 1), "")])   # state: location, path
    while True:
        # Pop a room from the queue and check if the vault has been reached
        state = state_queue.popleft()
        (location, path) = state
        if location.loc_x == 4 and location.loc_y == 4:
            return path
        # Get the next possible rooms
        next_states = generate_next_room_states(vault_passcode, state)
        for next_state in next_states:
            state_queue.append(next_state)


def solve_part2(vault_passcode):
    """
    Solves AOC 2016 Day 17 Part 2 // ###
    """
    return -1


def generate_next_room_states(vault_passcode, state):
    """
    Generates the next room states from the current state.
    """
    # Generate the MD5 hash for current room, take first four chars of hexdigest
    chunk = hashlib.md5(
        f"{vault_passcode}{state[1]}".encode()).hexdigest()[0:4]
    next_states = []
    # UP
    match chunk[0]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_y > 1:
                new_location = Location2D(state[0].loc_x, state[0].loc_y - 1)
                next_states.append((new_location, state[1] + "U"))
    # DOWN
    match chunk[1]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_y < 4:
                new_location = Location2D(state[0].loc_x, state[0].loc_y + 1)
                next_states.append((new_location, state[1] + "D"))
    # LEFT
    match chunk[2]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_x > 1:
                new_location = Location2D(state[0].loc_x - 1, state[0].loc_y)
                next_states.append((new_location, state[1] + "L"))
    # RIGHT
    match chunk[3]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_x < 4:
                new_location = Location2D(state[0].loc_x + 1, state[0].loc_y)
                next_states.append((new_location, state[1] + "R"))
    return next_states
