# Puzzle: https://adventofcode.com/2023/day/3
# Input: https://adventofcode.com/2023/day/3/input
# --- Part One ---

with open("./puzzle_input.txt", "r") as f:
    schematic = [line.strip() for line in f.readlines()]

result = 0
max_i = len(schematic) - 1
max_j = len(schematic[0]) - 1


def is_symbol(char: str):
    return not char.isdigit() and char != "."


def is_adjacent_to_symbol(i: int, j: int):
    if i > 0 and j > 0 and is_symbol(schematic[i - 1][j - 1]):
        return True
    if i > 0 and is_symbol(schematic[i - 1][j]):
        return True
    if i > 0 and j < max_j and is_symbol(schematic[i - 1][j + 1]):
        return True
    if j > 0 and is_symbol(schematic[i][j - 1]):
        return True
    if j < max_j and is_symbol(schematic[i][j + 1]):
        return True
    if i < max_i and j > 0 and is_symbol(schematic[i + 1][j - 1]):
        return True
    if i < max_i and is_symbol(schematic[i + 1][j]):
        return True
    if i < max_i and j < max_j and is_symbol(schematic[i + 1][j + 1]):
        return True
    return False


for i in range(len(schematic)):
    previous_is_digit = False
    digit_str = ""
    is_adjacent = False
    for j in range(len(schematic[0])):
        char = schematic[i][j]
        if char.isdigit():
            if previous_is_digit:
                digit_str += char
            else:
                digit_str = char
            previous_is_digit = True
            is_adjacent = is_adjacent or is_adjacent_to_symbol(i, j)
            if j == max_j or not schematic[i][j + 1].isdigit():
                if is_adjacent:
                    result += int(digit_str)
                previous_is_digit = False
                digit_str = ""
                is_adjacent = False

print(result)
