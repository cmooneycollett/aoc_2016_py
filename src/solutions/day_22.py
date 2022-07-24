"""
Solutions for AOC 2016 Day 22.
"""


from dataclasses import dataclass
import re


@dataclass
class NodeData:
    """
    Represents the used and available space for a single node, in terabytes.
    """
    used: int
    available: int


def process_input_file():
    """
    Processes the AOC 2016 Day 22 input file into the format required by the
    solver functions. Returned value is a 2D array with elements containing the
    node data for each element of the storage cluster grid.
    """
    items = []
    regex_nodedata = re.compile(
        r"^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$")
    with open("./input/day_22.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if (match_nodedata := regex_nodedata.match(line)):
                loc_x = int(match_nodedata.group(1))
                loc_y = int(match_nodedata.group(2))
                used = int(match_nodedata.group(4))
                available = int(match_nodedata.group(5))
                items.append(((loc_x, loc_y), NodeData(used, available)))
    # Shift the grid to start at location (0,0)
    min_x = min(x for ((x, _), _) in items)
    max_x = max(x for ((x, _), _) in items)
    min_y = min(y for ((_, y), _) in items)
    max_y = max(y for ((_, y), _) in items)
    node_grid = [[NodeData(0, 0) for _ in range(max_x - min_x + 1)]
                 for _ in range(max_y - min_y + 1)]
    for ((loc_x, loc_y), nodedata) in items:
        node_grid[loc_y - min_y][loc_x - min_x] = nodedata
    return node_grid


def solve_part1(node_grid):
    """
    Solves AOC 2016 Day 22 Part 1 // Determines the number of viable pairs of
    nodes in the given node grid.
    """
    viable_pairs = 0
    for (row, node_row) in enumerate(node_grid):
        for col in range(len(node_row)):
            viable_pairs += count_viable_pairs(node_grid, col, row)
    return viable_pairs


def solve_part2(input_data):
    """
    Solves AOC 2016 Day 22 Part 2 // ###
    """
    return -1


def count_viable_pairs(node_grid, loc_x, loc_y):
    """
    Counts the number of viable pairs the node at the specified location forms
    with other nodes in the node grid.
    """
    if node_grid[loc_y][loc_x].used == 0:
        return 0
    viable_pairs = 0
    for (row, node_row) in enumerate(node_grid):
        for (col, node_data) in enumerate(node_row):
            # Node cannot form a viable pair with itself
            if row == loc_y and col == loc_x:
                continue
            node_a = node_grid[loc_y][loc_x]
            node_b = node_data
            if node_a.used <= node_b.available:
                viable_pairs += 1
    return viable_pairs
