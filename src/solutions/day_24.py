"""
Solutions for AOC 2016 Day 24.
"""

from collections import deque
from enum import Enum, auto, unique
import itertools
from src.utils.cartography import Location2D


@unique
class TileType(Enum):
    """
    Represents the different types of tile in the grid.
    """
    OPEN = auto()
    WALL = auto()


def process_input_file():
    """
    Processes the AOC 2016 Day 24 input file into the format required by the
    solver functions. Returned value is tuple containing the 2D array
    representing the grid state and a dict containing the 2D-location of the
    numbered locations.
    """
    with open("./input/day_24.txt", encoding="utf-8") as file:
        numbered_locations = {}
        grid = []
        loc_y = 0
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            new_row = []
            loc_x = 0
            for char in line:
                if char == ".":
                    new_row.append(TileType.OPEN)
                elif char == "#":
                    new_row.append(TileType.WALL)
                elif char in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    new_row.append(TileType.OPEN)
                    numbered_locations[char] = Location2D(loc_x, loc_y)
                loc_x += 1
            grid.append(new_row)
            loc_y += 1
    return (grid, numbered_locations)


def solve_part1(grid_data):
    """
    Solves AOC 2016 Day 24 Part 1 // Determines the fewest number of moves
    required for the robot to visit all of the numbered locations at least once,
    starting from the "0" location.
    """
    (grid, numbered_locations) = grid_data
    # For each numbered location, determine minimum steps to each other one
    distances = determine_numbered_location_distances(grid, numbered_locations)
    return determine_min_steps_to_visit_all_nodes(distances)


def determine_min_steps_to_visit_all_nodes(distances, return_to_zero=False):
    """
    Determines the minimum steps required to visit each node at least once,
    starting at node "0". The distance includes the the distance to return to
    node "0" if option is specified as True.
    """
    chars = [char for char in distances if char != "0"]
    orders = itertools.permutations(chars)
    min_distance = None
    for order in orders:
        # Calculate the total distance for the current node order
        total_distance = distances["0"][order[0]]
        for index in range(1, len(order)):
            total_distance += distances[order[index - 1]][order[index]]
        if return_to_zero:
            total_distance += distances[-1]["0"]
        # Check if a new minimum distance has been found
        if min_distance is None or total_distance < min_distance:
            min_distance = total_distance
    return min_distance


def determine_numbered_location_distances(grid, numbered_locations):
    """
    Determines the distance of each numbered location from all others.
    """
    distances = {}
    for start_num in numbered_locations:
        distances[start_num] = {}
        for end_num in numbered_locations:
            if start_num == end_num:
                continue
            start_loc = numbered_locations[start_num]
            target_loc = numbered_locations[end_num]
            steps = determine_min_steps_between_locations(
                grid, start_loc, target_loc)
            distances[start_num][end_num] = steps
    return distances


def determine_min_steps_between_locations(grid, start_loc, target_loc):
    """
    Determines the minimum number of steps between the start and target
    locations in the grid.
    """
    # State: current location, steps
    state_queue = deque([(start_loc, 0)])
    visited = set([start_loc])
    while len(state_queue) > 0:
        state = state_queue.popleft()
        (location, steps) = state
        if location == target_loc:
            return steps
        for next_state in generate_next_location_states(grid, state):
            (next_loc, _) = next_state
            if next_loc not in visited:
                visited.add(next_loc)
                state_queue.append(next_state)
    return -1


def generate_next_location_states(grid, state):
    """
    Generates the next location states from the given state on the grid.
    """
    for (delta_x, delta_y) in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        (loc, steps,) = state
        new_x = loc.loc_x + delta_x
        new_y = loc.loc_y + delta_y
        if new_y < 0 or new_y >= len(grid) or new_x < 0 or \
                new_x > len(grid[loc.loc_y]):
            continue
        if grid[new_y][new_x] == TileType.WALL:
            continue
        new_loc = Location2D(new_x, new_y)
        yield (new_loc, steps + 1)


def solve_part2(input_data):
    """
    Solves AOC 2016 Day 24 Part 2 // ###
    """
    return -1
