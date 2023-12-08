# https://adventofcode.com/2023/day/1
# --- Part One ---

result = 0
with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        digits = [char for char in line if char.isdigit()]
        result += int(f"{digits[0]}{digits[-1]}")
print(result)
