# Puzzle: https://adventofcode.com/2023/day/3
# Input: https://adventofcode.com/2023/day/3/input
# --- Part Two ---

with open("./puzzle_input.txt", "r") as f:
    schematic = [line.strip() for line in f.readlines()]

result = 0
max_i = len(schematic) - 1
max_j = len(schematic[0]) - 1


def get_index_of_digit(i: int, j: int):
    index_dict: dict[int, list[int]] = {i - 1: [], i: [], i + 1: []}
    if i > 0 and j > 0 and schematic[i - 1][j - 1].isdigit():
        index_dict[i - 1].append(j - 1)
    if i > 0 and schematic[i - 1][j].isdigit():
        index_dict[i - 1].append(j)
    if i > 0 and j < max_j and schematic[i - 1][j + 1].isdigit():
        index_dict[i - 1].append(j + 1)
    if j > 0 and schematic[i][j - 1].isdigit():
        index_dict[i].append(j - 1)
    if j < max_j and schematic[i][j + 1].isdigit():
        index_dict[i].append(j + 1)
    if i < max_i and j > 0 and schematic[i + 1][j - 1].isdigit():
        index_dict[i + 1].append(j - 1)
    if i < max_i and schematic[i + 1][j].isdigit():
        index_dict[i + 1].append(j)
    if i < max_i and j < max_j and schematic[i + 1][j + 1].isdigit():
        index_dict[i + 1].append(j + 1)
    return index_dict


def is_digit(i, j):
    if not (0 <= i < len(schematic)):
        return False
    if not (0 <= j < len(schematic[0])):
        return False
    return schematic[i][j].isdigit()


def get_j_range(i, j):
    min_j = j
    while is_digit(i, min_j):
        min_j -= 1
    min_j += 1

    max_j = j
    while is_digit(i, max_j):
        max_j += 1

    return min_j, max_j


def get_gear_ratio(index_dict: dict):
    n = []
    for i, j_list in index_dict.items():
        if j_list:
            j = j_list[0]
            min_j, max_j = get_j_range(i, j)
            n.append(int(schematic[i][min_j:max_j]))
            if max_j < (j := j_list[-1]):
                min_j, max_j = get_j_range(i, j)
                n.append(int(schematic[i][min_j:max_j]))
    if len(n) == 2:
        return n[0] * n[1]
    return None


for i in range(len(schematic)):
    for j in range(len(schematic[0])):
        if (char := schematic[i][j]) == "*":
            index_dict = get_index_of_digit(i, j)
            if (gear_ratio := get_gear_ratio(index_dict)) is not None:
                result += gear_ratio

print(result)
