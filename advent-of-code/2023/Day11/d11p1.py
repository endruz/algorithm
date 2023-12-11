# Puzzle: https://adventofcode.com/2023/day/11
# Input: https://adventofcode.com/2023/day/11/input
# --- Part One ---

from typing import List, Tuple

with open("./puzzle_input.txt", "r") as f:
    universe = [list(line.strip()) for line in f.readlines()]


def expand_the_universe(universe: List[List[str]]):
    height = len(universe)
    weight = len(universe[0])
    for index in range(height - 1, -1, -1):
        for location in universe[index]:
            if location == "#":
                break
        else:
            universe.insert(index, ["."] * weight)

    height = len(universe)
    for j in range(weight - 1, -1, -1):
        for i in range(height - 1, -1, -1):
            if universe[i][j] == "#":
                break
        else:
            for i in range(height - 1, -1, -1):
                universe[i].insert(j, ".")


def get_galaxies(universe: List[List[str]]) -> List[Tuple[int, int]]:
    galaxies = []
    height = len(universe)
    weight = len(universe[0])
    for i in range(height):
        for j in range(weight):
            if universe[i][j] == "#":
                galaxies.append((i, j))
    return galaxies


expand_the_universe(universe)
galaxies = get_galaxies(universe)
result = 0

while galaxies:
    current_galaxy = galaxies.pop(0)
    for galaxy in galaxies:
        row_distance = abs(current_galaxy[0] - galaxy[0])
        col_distance = abs(current_galaxy[1] - galaxy[1])
        result += row_distance + col_distance

print(result)
