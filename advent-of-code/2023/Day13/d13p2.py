# Puzzle: https://adventofcode.com/2023/day/13
# Input: https://adventofcode.com/2023/day/13/input
# --- Part Two ---
from typing import List


def get_mirror(grid):
    for i in range(len(grid) - 1):
        smudge = 0
        for j in range(min(i + 1, len(grid) - i - 1)):
            for x in range(len(grid[0])):
                if grid[i - j][x] != grid[i + j + 1][x]:
                    smudge += 1
        if smudge == 1:
            return i + 1
    return 0


def get_points(grid):
    horizontal = get_mirror(grid)
    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    vertical = get_mirror(grid)
    return vertical + horizontal * 100


result = 0
with open("./puzzle_input.txt", "r") as f:
    grid: List[List[str]] = []
    for line in f.readlines():
        if line := line.strip():
            grid.append(list(line))
        else:
            result += get_points(grid)
            grid = []
    if len(grid) > 0:
        result += get_points(grid)

print(result)
