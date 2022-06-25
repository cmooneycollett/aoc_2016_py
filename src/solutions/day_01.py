"""
Solutions for AOC 2016 Day 1.
"""


from src.utils.cartography import CardinalDirection, Location2D


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
    direction = CardinalDirection.NORTH  # Start by facing North
    location = Location2D(0, 0)  # Assume starting location as 2D origin
    for (turn_direction, steps) in input_data:
        if turn_direction == "L":   # Left turn
            direction = direction.rotate90_counterclockwise()
        else:   # Right turn
            direction = direction.rotate90_clockwise()
        # Take steps in current direction
        match direction:
            case CardinalDirection.NORTH:
                location = Location2D(location.loc_x, location.loc_y + steps)
            case CardinalDirection.EAST:
                location = Location2D(location.loc_x + steps, location.loc_y)
            case CardinalDirection.SOUTH:
                location = Location2D(location.loc_x, location.loc_y - steps)
            case CardinalDirection.WEST:
                location = Location2D(location.loc_x - steps, location.loc_y)
    # Calculate Manhattan distance of end location from origin
    return abs(location.loc_x) + abs(location.loc_y)


def solve_part2(input_data):
    """
    Determines the location of Easter Bunny HQ by identifying how many blocks
    away from the origin (Manhattan distance) the first location to be visited
    twice is.
    """
    direction = CardinalDirection.NORTH  # Start by facing North
    location = Location2D(0, 0)  # Assume starting location as 2D origin
    locations_visited = set()   # Track locations that have been visited
    locations_visited.add(location)
    for (turn_direction, steps) in input_data:
        if turn_direction == "L":   # Left turn
            direction = direction.rotate90_counterclockwise()
        else:   # Right turn
            direction = direction.rotate90_clockwise()
        # Take each step separately
        found_bunny_hq = False
        for _ in range(0, steps):
            match direction:
                case CardinalDirection.NORTH:
                    location = Location2D(location.loc_x, location.loc_y + 1)
                case CardinalDirection.EAST:
                    location = Location2D(location.loc_x + 1, location.loc_y)
                case CardinalDirection.SOUTH:
                    location = Location2D(location.loc_x, location.loc_y - 1)
                case CardinalDirection.WEST:
                    location = Location2D(location.loc_x - 1, location.loc_y)
            # Add location to visited location and check if it has been visited
            if location in locations_visited:
                found_bunny_hq = True
                break
            locations_visited.add(location)
        if found_bunny_hq:
            break
    # Calculate Manhattan distance of end location from origin
    return abs(location.loc_x) + abs(location.loc_y)
