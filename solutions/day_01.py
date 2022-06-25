"""
Solutions for AOC 2016 Day 1.
"""

from dataclasses import dataclass
from enum import auto, Enum, unique


@dataclass
class Location2D:
    """
    Represents a point location on a two-dimensional plane.
    """
    loc_x: int
    loc_y: int

@unique
class CardinalDirection(Enum):
    """
    Represents the four different cardinal directions of: North, East, South and
    West.
    """
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def rotate90_clockwise(self):
        """
        Gets the resulting cardinal direction after rotating by 90 degrees in
        the clockwise direction.
        """
        match self:
            case CardinalDirection.NORTH:
                return CardinalDirection.EAST
            case CardinalDirection.EAST:
                return CardinalDirection.SOUTH
            case CardinalDirection.SOUTH:
                return CardinalDirection.WEST
            case CardinalDirection.WEST:
                return CardinalDirection.NORTH

    def rotate90_counterclockwise(self):
        """
        Gets the resulting cardinal direction after rotating by 90 degrees in
        the counter-clockwise direction.
        """
        match self:
            case CardinalDirection.NORTH:
                return CardinalDirection.WEST
            case CardinalDirection.EAST:
                return CardinalDirection.NORTH
            case CardinalDirection.SOUTH:
                return CardinalDirection.EAST
            case CardinalDirection.WEST:
                return CardinalDirection.SOUTH


def main():
    """
    Solves AOC 2016 Day 1 Parts 1 and 2, printing out the solutions.
    """
    input_data = process_input_file()
    p1_solution = solve_part1(input_data)
    print(f"P1 solution - {p1_solution}")
    # p2_solution = solve_part2(input_data)
    # print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2016 Day 1 input file into the format required by the
    solver functions. Returned value is a list of tuples containing the turn
    direction (either left ("L") or right ("R")) and the number of steps to be
    taken (as int).
    """
    input_data = []
    with open("./inputs/day_01.txt", encoding="utf-8") as file:
        raw_input = file.read().strip()
        for order in raw_input.split(", "):
            direction = order[0]
            steps = int(order[1:])
            input_data.append((direction, steps))
    return input_data


def solve_part1(input_data):
    """
    Determines how many block away from the origin Easter Bunny HQ is by
    conducting the steps given in the input data and calculating the Manhattan
    distance of the resulting location from the origin.
    """
    direction = CardinalDirection.NORTH # Start by facing North
    location = Location2D(0, 0) # Assume starting location as 2D origin
    for (turn_direction, steps) in input_data:
        if turn_direction == "L":   # Left turn
            direction = direction.rotate90_counterclockwise()
        else:   # Right turn
            direction = direction.rotate90_clockwise()
        # Take steps in current direction
        match direction:
            case CardinalDirection.NORTH:
                location.loc_y += steps
            case CardinalDirection.EAST:
                location.loc_x += steps
            case CardinalDirection.SOUTH:
                location.loc_y -= steps
            case CardinalDirection.WEST:
                location.loc_x -= steps
    # Calculate Manhattan distance of end location from origin
    return abs(location.loc_x) + abs(location.loc_y)


def solve_part2(input_data):
    return


if __name__ == "__main__":
    main()
