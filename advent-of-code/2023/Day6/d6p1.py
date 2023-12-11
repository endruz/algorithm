# Puzzle: https://adventofcode.com/2023/day/6
# Input: https://adventofcode.com/2023/day/6/input
# --- Part One ---

with open("./puzzle_input.txt", "r") as f:
    time_list = [int(t) for t in f.readline().strip().split()[1:]]
    distance_list = [int(d) for d in f.readline().strip().split()[1:]]

result = 1
for index, time in enumerate(time_list):
    ways = 0
    for t in range(time):
        if (time - t) * t > distance_list[index]:
            ways += 1
    result *= ways

print(result)
