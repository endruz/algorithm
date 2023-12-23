# Puzzle: https://adventofcode.com/2023/day/23
# Input: https://adventofcode.com/2023/day/23/input
# --- Part One ---

from collections import deque
from copy import deepcopy
from typing import Deque, Optional, Tuple


with open("./puzzle_input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

height, weight = len(grid), len(grid[0])


def get_first_paths_in_line(i) -> Optional[Tuple[int, int]]:
    for j in range(weight):
        if grid[i][j] == ".":
            return (i, j)
    return None


start_point = get_first_paths_in_line(0)
end_point = get_first_paths_in_line(height - 1)

print(start_point, end_point)

assert start_point is not None
assert end_point is not None


def is_reachable(position: Tuple[int, int]):
    i, j = position
    return 0 <= i < height and 0 <= j <= weight and grid[i][j] != "#"


direction = {
    "<": (0, -1),
    ">": (0, 1),
    "v": (1, 0),
    "^": (-1, 0),
}

result = 0
queue: Deque = deque([(start_point, set())])

while queue:
    cur_position, visited = queue.popleft()
    if cur_position == end_point:
        result = max(result, len(visited))
        print(result)
        continue

    visited.add(cur_position)

    i, j = cur_position
    if grid[i][j] in direction:
        row, col = direction[grid[i][j]]
        if (next_position := (i + row, j + col)) not in visited:
            queue.append((next_position, deepcopy(visited)))
    else:
        for row, col in direction.values():
            if (
                is_reachable(next_position := (i + row, j + col))
                and next_position not in visited
            ):
                queue.append((next_position, deepcopy(visited)))

print(result)
