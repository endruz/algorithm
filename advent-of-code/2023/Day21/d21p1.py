# Puzzle: https://adventofcode.com/2023/day/21
# Input: https://adventofcode.com/2023/day/21/input
# --- Part One ---

from typing import Set, Tuple

with open("./puzzle_input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

hight, weight = len(grid), len(grid[0])


def get_starting_position(grid):
    for i, row in enumerate(grid):
        if "S" in row:
            return (i, row.index("S"))


def is_reachable(position: Tuple[int, int]):
    if not (0 <= position[0] < hight and 0 <= position[1] < weight):
        return False
    if grid[position[0]][position[1]] == "#":
        return False
    return True


def take_one_step(positions: Set[Tuple[int, int]]):
    next_positions = set()
    for position in positions:
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if is_reachable(p := (position[0] + i, position[1] + j)):
                next_positions.add(p)
    return next_positions


positions = {get_starting_position(grid)}

for _ in range(64):
    positions = take_one_step(positions)

print(len(positions))
