# Puzzle: https://adventofcode.com/2023/day/16
# Input: https://adventofcode.com/2023/day/16/input
# --- Part One ---

with open("./puzzle_input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]


height, weight = len(grid), len(grid[0])

def take_one_step(i: int, j: int, come_from: str):
    if not (0 <= i < height) or not (0 <= j < weight):
        return []

    next_args = []
    combo = f"{grid[i][j]}{come_from}"
    if combo in (".N", "/E", r"\W", "|W", "|E", "|N"):
        next_args.append((i + 1, j, "N"))

    if combo in (".S", "/W", r"\E", "|W", "|E", "|S"):
        next_args.append((i - 1, j, "S"))

    if combo in (".W", "/S", r"\N", "-S", "-N", "-W"):
        next_args.append((i, j + 1, "W"))

    if combo in (".E", "/N", r"\S", "-S", "-N", "-E"):
        next_args.append((i, j - 1, "E"))

    return next_args

energized = set()
args_list = [(0, 0, "W")]

while args_list:
    args = args_list.pop(0)
    if next_step_args := take_one_step(*args):
        energized.add(args)
    for a in next_step_args:
        if a in energized:
            continue
        args_list.append(a)

print(len({e[:2] for e in energized}))
