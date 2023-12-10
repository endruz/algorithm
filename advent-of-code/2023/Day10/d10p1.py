# https://adventofcode.com/2023/day/10
# --- Part One ---

with open("./puzzle_input.txt", "r") as f:
    grid = f.readlines()

hight, weight = len(grid), len(grid[0])
distance_grid = [[[] for _ in range(weight)] for _ in range(hight)]

def get_starting_position(grid):
    for i, row in enumerate(grid):
        if (j := row.find("S")) != -1:
            return (i, j)

def take_one_step(i: int, j: int, come_from: str, step_count: int):
    if not (0 <= i < hight) or not (0 <= j < weight):
        return None
    next_step_count = step_count + 1
    combo = f"{grid[i][j]}{come_from}"
    next_args = None
    if combo in ("|S", "LE", "JW"):
        next_args = (i - 1, j, "S", next_step_count)
    elif combo in ("|N", "7W", "FE"):
        next_args = (i + 1, j, "N", next_step_count)
    elif combo in ("-E", "JN", "7S"):
        next_args = (i, j - 1, "E", next_step_count)
    elif combo in ("-W", "LN", "FS"):
        next_args = (i, j + 1, "W", next_step_count)

    if next_args:
        distance_grid[i][j].append(step_count)
    return next_args

result = 0
start_i, start_j  = get_starting_position(grid)
distance_grid[start_i][start_j].append(0)
for args in [
    take_one_step(start_i - 1, start_j, "S", 1),
    take_one_step(start_i + 1, start_j, "N", 1),
    take_one_step(start_i, start_j - 1, "E", 1),
    take_one_step(start_i, start_j + 1, "W", 1)
    ]:
    while args is not None:
        args = take_one_step(*args)

for row in distance_grid:
    for distances in row:
        if len(distances):
            result = max(min(distances), result)

print(result)
