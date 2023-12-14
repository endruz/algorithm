# Puzzle: https://adventofcode.com/2023/day/14
# Input: https://adventofcode.com/2023/day/14/input
# --- Part One ---

with open("./puzzle_input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

height, weight = len(grid), len(grid[0])

result = 0
for j in range(weight):
    foothold = 0
    for i in range(height):
        if grid[i][j] == "#":
            foothold = i + 1
        elif grid[i][j] == "O":
            result += height - foothold
            foothold += 1

print(result)
