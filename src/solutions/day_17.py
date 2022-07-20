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
    starting location (0,0) in the 4-by-4 room grid to the vault location (3,3)
    in the bottom right of the grid.
    """
    # Starting location is (0,0) - target location is (3,3)
    state_queue = deque([(Location2D(0, 0), "")])   # state: location, path
    while len(state_queue) > 0:
        # Pop a room from the queue and check if the vault has been reached
        state = state_queue.popleft()
        (location, path) = state
        if location.loc_x == 3 and location.loc_y == 3:
            return path
        # Get the next possible rooms
        for next_state in generate_next_room_states(vault_passcode, state):
            state_queue.append(next_state)


def solve_part2(vault_passcode):
    """
    Solves AOC 2016 Day 17 Part 2 // Determines the longest path from the
    starting location (0,0) in the 4-by-4 room grid to the vault location (3,3)
    in the bottom right of the grid.
    """
    # Starting location is (0,0) - target location is (3,3)
    state_queue = deque([(Location2D(0, 0), "")])   # state: location, path
    longest_path_len = 0
    while len(state_queue) > 0:
        # Pop a room and check if the vault has been reached
        state = state_queue.popleft()
        (location, path) = state
        # End a path when it reaches the vault, and check for longest path len
        if location.loc_x == 3 and location.loc_y == 3:
            if len(path) > longest_path_len:
                longest_path_len = len(path)
            continue
        # Get the next possible rooms
        for next_state in generate_next_room_states(vault_passcode, state):
            state_queue.append(next_state)
    return longest_path_len


def generate_next_room_states(vault_passcode, state):
    """
    Generates the next room states from the current state, by taking into 
    account the MD5 hash for current room and path to determine whether doors
    are open or closed.
    """
    # Generate the MD5 hash for current room, take first four chars of hexdigest
    chunk = hashlib.md5(
        f"{vault_passcode}{state[1]}".encode()).hexdigest()[0:4]
    next_states = []
    # UP - "U"
    match chunk[0]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_y > 0:
                new_location = Location2D(state[0].loc_x, state[0].loc_y - 1)
                next_states.append((new_location, state[1] + "U"))
    # DOWN - "D"
    match chunk[1]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_y < 3:
                new_location = Location2D(state[0].loc_x, state[0].loc_y + 1)
                next_states.append((new_location, state[1] + "D"))
    # LEFT - "L"
    match chunk[2]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_x > 0:
                new_location = Location2D(state[0].loc_x - 1, state[0].loc_y)
                next_states.append((new_location, state[1] + "L"))
    # RIGHT - "R"
    match chunk[3]:
        case "b" | "c" | "d" | "e" | "f":
            if state[0].loc_x < 3:
                new_location = Location2D(state[0].loc_x + 1, state[0].loc_y)
                next_states.append((new_location, state[1] + "R"))
    return next_states
