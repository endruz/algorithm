# Puzzle: https://adventofcode.com/2023/day/14
# Input: https://adventofcode.com/2023/day/14/input
# --- Part Two ---

from typing import Dict

with open("./puzzle_input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

height, weight = len(grid), len(grid[0])


def run_cycle(grid):
    # to the north
    for j in range(weight):
        foothold = 0
        for i in range(height):
            if grid[i][j] == "#":
                foothold = i + 1
            elif grid[i][j] == "O":
                if i != foothold:
                    grid[foothold][j] = "O"
                    grid[i][j] = "."
                foothold += 1

    # to the west
    for i in range(height):
        foothold = 0
        for j in range(weight):
            if grid[i][j] == "#":
                foothold = j + 1
            elif grid[i][j] == "O":
                if j != foothold:
                    grid[i][foothold] = "O"
                    grid[i][j] = "."
                foothold += 1

    # to the south
    for j in range(weight):
        foothold = height - 1
        for i in range(height - 1, -1, -1):
            if grid[i][j] == "#":
                foothold = i - 1
            elif grid[i][j] == "O":
                if i != foothold:
                    grid[foothold][j] = "O"
                    grid[i][j] = "."
                foothold -= 1

    # to the east
    for i in range(height):
        foothold = weight - 1
        for j in range(weight - 1, -1, -1):
            if grid[i][j] == "#":
                foothold = j - 1
            elif grid[i][j] == "O":
                if j != foothold:
                    grid[i][foothold] = "O"
                    grid[i][j] = "."
                foothold -= 1

    return grid


def get_load(grid):
    result = 0
    for j in range(weight):
        for i in range(height):
            if grid[i][j] == "O":
                result += height - i
    return result


cycle_count = 1000000000
seen: Dict[str, int] = {}

while cycle_count > 0:
    key = str(grid)
    if key in seen:
        cycle_count %= seen[key] - cycle_count
    seen[key] = cycle_count
    grid = run_cycle(grid)
    cycle_count -= 1

assert cycle_count == 0

print(get_load(grid))
