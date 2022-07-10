"""
Solutions for AOC 2016 Day 11.
"""


from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum, auto, unique
import itertools
import re


@unique
class ComponentType(Enum):
    """
    Represents the different types of components present within the facility.
    """
    GENERATOR = auto()
    MICROCHIP = auto()


@dataclass
class Component:
    """
    Represents an individual component described by its type and name.
    """
    type: ComponentType
    name: str


@dataclass
class State:
    """
    Represents a possible state of the facility.
    """
    moves: int
    floor: int
    floor_data: dict


def process_input_file():
    """
    Processes the AOC 2016 Day 11 input file into the format required by the
    solver functions.
    """
    regex_generator = r"([a-z-]+) generator"
    regex_microchip = r"([a-z-]+)-compatible microchip"
    floor = 1
    input_data = {}
    with open("./input/day_11.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            input_data[floor] = []
            # Find generators
            for generator in re.findall(regex_generator, line):
                input_data[floor].append(
                    Component(ComponentType.GENERATOR, generator))
            # Find microchips
            for microchip in re.findall(regex_microchip, line):
                input_data[floor].append(
                    Component(ComponentType.MICROCHIP, microchip))
            input_data[floor] = sorted(
                input_data[floor], key=lambda comp: (comp.type.value, comp.name))
            floor += 1
    return State(0, 1, input_data)


def solve_part1(input_data):
    """
    Solves AOC 2016 Day 11 Part 1 // Determines the minimum number of moves
    required to move all components to the top floor.
    """
    return find_minimum_moves_to_top_floor(input_data)


def solve_part2(_input_data):
    """
    Solves AOC 2016 Day 11 Part 2 // ###
    """
    return -1


def find_minimum_moves_to_top_floor(initial_state):
    """
    Takes the initial state and determines the minimum number of moves required
    to move all components up to the top floor.
    """
    state_queue = deque([initial_state])
    seen_states = set([calculate_state_hash(initial_state)])
    max_moves_seen = 0
    while len(state_queue) > 0:
        state = state_queue.popleft()
        if state.floor == 4 and check_if_all_components_at_top_floor(state):
            return state.moves
        if state.moves > max_moves_seen:
            max_moves_seen = state.moves
        # Find all the possible next states from the current state
        for next_state in get_next_states(state):
            # If a next state hasn't been seen already, add it to back of queue
            if (next_state_hash := calculate_state_hash(next_state)) not in seen_states:
                seen_states.add(next_state_hash)
                state_queue.append(next_state)


def calculate_state_hash(state):
    """
    Calculates the hash of the given state, by hashing the string representation
    of the state.
    """
    return hash(f"moves {state.moves} // floor {state.floor} // {str(state.floor_data)}")


def get_next_states(state):
    """
    Determines the possible next states from the given state.
    """
    next_states = []
    move_options = itertools.chain(
        itertools.combinations(state.floor_data[state.floor], 2),
        itertools.combinations(state.floor_data[state.floor], 1))
    for components in move_options:
        for floor_delta in [-1, 1]:
            # Dont move down if all floors below are empty
            if floor_delta == -1:
                skip = True
                for sub_floor in range(1, state.floor):
                    if len(state.floor_data[sub_floor]) > 0:
                        skip = False
                        break
                if skip:
                    continue
            # Check that next floor is valid number
            if not 1 <= (next_floor := state.floor + floor_delta) <= 4:
                continue
            next_floor_data = deepcopy(state.floor_data)
            # Remove components from current floor and add to next floor
            for comp in components:
                next_floor_data[state.floor].remove(comp)
                next_floor_data[next_floor].append(comp)
            next_floor_data[next_floor] = sorted(
                next_floor_data[next_floor],
                key=lambda comp: (comp.type.value, comp.name))
            # Check if both current and next floor are valid
            if validate_floor(next_floor_data[state.floor]) and \
                    validate_floor(next_floor_data[next_floor]):
                next_states.append(
                    State(state.moves + 1, next_floor, next_floor_data))
    return next_states


def validate_floor(floor_components):
    """
    Determines if the floor components are valid, so that a microchip is not
    destroyed by being in the same area as an incompatible generator.
    """
    # Valid if fewer than two components
    if len(floor_components) == 0:
        return True
    generators = set(
        comp.name for comp in floor_components if comp.type == ComponentType.GENERATOR)
    microchips = set(
        comp.name for comp in floor_components if comp.type == ComponentType.MICROCHIP)
    # Valid if only one type of component
    if len(generators) == 0 or len(microchips) == 0:
        return True
    # Invalid if microchip does not have matching generator
    if len(generators) >= 1:
        for chip in microchips:
            if chip not in generators:
                return False
    # Valid if each microchip has matching generator if at least one generator
    return True


def check_if_all_components_at_top_floor(state):
    """
    Checks if all components are at the top floor.
    """
    for floor in range(1, 4):
        if len(state.floor_data[floor]) != 0:
            return False
    return True
