# Puzzle: https://adventofcode.com/2023/day/11
# Input: https://adventofcode.com/2023/day/11/input
# --- Part Two ---

from typing import List, Tuple

with open("./puzzle_input.txt", "r") as f:
    universe = [list(line.strip()) for line in f.readlines()]


def expand_the_universe(universe: List[List[str]]) -> Tuple[List[int], List[int]]:
    expanded_rows = []
    expanded_cols = []
    height = len(universe)
    weight = len(universe[0])
    for index in range(height):
        for location in universe[index]:
            if location == "#":
                break
        else:
            expanded_rows.append(index)

    for j in range(weight):
        for i in range(height):
            if universe[i][j] == "#":
                break
        else:
            expanded_cols.append(j)
    return expanded_rows, expanded_cols


def get_galaxies(universe: List[List[str]]) -> List[Tuple[int, int]]:
    galaxies = []
    height = len(universe)
    weight = len(universe[0])
    for i in range(height):
        for j in range(weight):
            if universe[i][j] == "#":
                galaxies.append((i, j))
    return galaxies


def calculate_distance(i1: int, i2: int, expanded_list: List[int]) -> int:
    min_index = min(i1, i2)
    max_index = max(i1, i2)
    count = 0
    for index in expanded_list:
        if min_index < index < max_index:
            count += 1
    distance = max_index - min_index - count + count * 1000000
    return distance


expanded_rows, expanded_cols = expand_the_universe(universe)
galaxies = get_galaxies(universe)
result = 0

while galaxies:
    current_galaxy = galaxies.pop(0)
    for galaxy in galaxies:
        row_distance = calculate_distance(current_galaxy[0], galaxy[0], expanded_rows)
        col_distance = calculate_distance(current_galaxy[1], galaxy[1], expanded_cols)
        result += row_distance + col_distance


print(result)
