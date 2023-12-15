# Puzzle: https://adventofcode.com/2023/day/15
# Input: https://adventofcode.com/2023/day/15/input
# --- Part One ---


def get_hash(step: str):
    hash_value = 0
    for char in step:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value


result = 0
with open("./puzzle_input.txt", "r") as f:
    for step in f.readline().strip().split(","):
        result += get_hash(step)

print(result)
