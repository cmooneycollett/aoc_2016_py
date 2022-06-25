"""
This module contains classes and functions to represent and operate on points
and objects in N-dimensional spaces.
"""

from dataclasses import dataclass
from enum import auto, Enum, unique


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


@dataclass(frozen=True, eq=True)
class Location2D:
    """
    Represents a point location on a two-dimensional plane.
    """
    loc_x: int
    loc_y: int


# class Location2D:
#     """
#     Represents a point location on a two-dimensional plane.
#     """

#     def __init__(self, loc_x, loc_y):
#         self.loc_x = loc_x
#         self.loc_y = loc_y

#     def __hash__(self):
#         return (53  + self.loc_x) * 53 + self.loc_y
#         # return hash(val for val in [self.loc_x, self.loc_y * 10])
#         # hash_value = hash(self.loc_x)
#         # hash_value = hash(self.loc_y)
#         # return hash_value

#     def update_location(self, delta_x, delta_y):
#         """
#         Updates the location by adjusting the x- and y-values by the given
#         delta values.
#         """
#         self.loc_x += delta_x
#         self.loc_y += delta_y
