# Puzzle: https://adventofcode.com/2023/day/10
# Input: https://adventofcode.com/2023/day/10/input
# --- Part Two ---

with open("./puzzle_input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

hight, weight = len(grid), len(grid[0])
distance_grid = [[float("inf")] * weight for _ in range(hight)]


def get_starting_position(grid):
    for i, row in enumerate(grid):
        if "S" in row:
            return (i, row.index("S"))



def take_one_step(i: int, j: int, come_from: str, step_count: int):
    if not (0 <= i < hight) or not (0 <= j < weight):
        return None
    combo = f"{grid[i][j]}{come_from}"
    next_args = None
    if combo in ("|S", "LE", "JW"):
        next_args = (i - 1, j, "S", step_count + 1)
    elif combo in ("|N", "7W", "FE"):
        next_args = (i + 1, j, "N", step_count + 1)
    elif combo in ("-E", "JN", "7S"):
        next_args = (i, j - 1, "E", step_count + 1)
    elif combo in ("-W", "LN", "FS"):
        next_args = (i, j + 1, "W", step_count + 1)

    if next_args:
        distance_grid[i][j] = min(distance_grid[i][j], step_count)
    return next_args


result = 0
start_i, start_j = get_starting_position(grid)
distance_grid[start_i][start_j] = 0
for args in [
    take_one_step(start_i - 1, start_j, "S", 1),
    take_one_step(start_i + 1, start_j, "N", 1),
    take_one_step(start_i, start_j - 1, "E", 1),
    take_one_step(start_i, start_j + 1, "W", 1),
]:
    while args is not None:
        args = take_one_step(*args)

# replace S
options = []
if distance_grid[start_i - 1][start_j] == 1:
    options.append({"|", "L", "J"})
if distance_grid[start_i + 1][start_j] == 1:
    options.append({"|", "7", "F"})
if distance_grid[start_i][start_j - 1] == 1:
    options.append({"-", "7", "J"})
if distance_grid[start_i][start_j + 1] == 1:
    options.append({"-", "F", "L"})

grid[start_i][start_j] = (options[0] & options[1]).pop()

result = 0
for i in range(hight):
    j = 0
    is_inside = False
    while j < weight:
        if distance_grid[i][j] == float("inf"):
            result += is_inside
        elif grid[i][j] == "|":
            is_inside = not is_inside
        else:
            loop_enter_top = grid[i][j] == "L"
            j += 1
            while grid[i][j] == "-":
                j += 1
            loop_exit_top = grid[i][j] == "J"
            if loop_enter_top != loop_exit_top:
                is_inside = not is_inside
        j += 1
print(result)
