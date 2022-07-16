"""
Solutions for AOC 2016 Day 13.
"""


from collections import deque
from enum import Enum, auto, unique
from src.utils.cartography import Location2D


@unique
class CellType(Enum):
    """
    Represents the possible cell types.
    """
    OPEN_SPACE = auto()
    WALL = auto()


def process_input_file():
    """
    Processes the AOC 2016 Day 13 input file into the format required by the
    solver functions. Returned value is the office designer's favourite number,
    as given in the input file.
    """
    with open("./input/day_13.txt", encoding="utf-8") as file:
        return int(file.read().strip())


def solve_part1(seed_value):
    """
    Solves AOC 2016 Day 13 Part 1 // Determines the fewest number of steps
    required to reach location (31,39) when starting at (1,1).
    """
    start_loc = Location2D(1, 1)
    target_loc = Location2D(31, 39)
    return find_minimum_steps_to_target_location(start_loc, target_loc,
                                                 seed_value)


def solve_part2(seed_value):
    """
    Solves AOC 2016 Day 13 Part 2 // Determines the number of distinct
    locations, including the starting location, that can be reached in at most
    50 steps.
    """
    start_loc = Location2D(1, 1)
    max_steps = 50
    return find_total_reachable_locations(start_loc, max_steps, seed_value)


def find_total_reachable_locations(start_loc, max_steps, seed_value):
    """
    Calculates the total number of locations, including the starting location,
    that can be reached by taking at most the given number of steps.
    """
    visited_cells = set([start_loc])
    # Begin: starting location, 0 steps
    to_be_visited = deque([(start_loc, 0)])
    while len(to_be_visited) > 0:
        # Get the next location to be visited
        state = to_be_visited.popleft()
        (_, steps) = state
        if steps > max_steps:
            return len(visited_cells) - len(to_be_visited) - 1
        # Determine next locations to visit
        for next_state in generate_next_states(state, seed_value):
            (next_location, _) = next_state
            if next_location not in visited_cells:
                visited_cells.add(next_location)
                to_be_visited.append(next_state)


def find_minimum_steps_to_target_location(start_loc, target_loc, seed_value):
    """
    Finds the minimum number of steps needed to reach the target location from
    the starting location, using a BFS approach. Cell types are dynamically
    calculated during search.
    """
    visited_cells = set([start_loc])
    to_be_visted = deque([(start_loc, 0)])  # Begin: starting location, 0 steps
    while len(to_be_visted) > 0:
        # Get the next location to be visited
        state = to_be_visted.popleft()
        (location, steps) = state
        if location == target_loc:
            return steps
        # Determine next locations to visit
        for next_state in generate_next_states(state, seed_value):
            (next_location, _) = next_state
            if next_location not in visited_cells:
                visited_cells.add(next_location)
                to_be_visted.append(next_state)


def generate_next_states(state, seed_value):
    """
    Determines the next states (location and steps taken) that can be reached
    from the current state. Note that diagonal moves are not permitted.
    """
    next_steps = state[1] + 1
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for (x_delta, y_delta) in directions:
        new_x = state[0].loc_x + x_delta
        new_y = state[0].loc_y + y_delta
        # Skip new locations that are outside of building
        if new_x < 0 or new_y < 0:
            continue
        # Skip new locations that are walls
        if determine_cell_type(new_x, new_y, seed_value) == CellType.WALL:
            continue
        # Yield the next valid state
        new_location = Location2D(new_x, new_y)
        yield (new_location, next_steps)


def determine_cell_type(loc_x, loc_y, seed_value):
    """
    Determines what type of cell is at the given location.
    """
    value = loc_x * loc_x + 3 * loc_x + 2 * loc_x * loc_y + loc_y + \
        loc_y * loc_y
    value += seed_value
    ones_count = bin(value).count("1")
    if ones_count % 2 == 0:
        return CellType.OPEN_SPACE
    return CellType.WALL
