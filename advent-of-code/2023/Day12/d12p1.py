# Puzzle: https://adventofcode.com/2023/day/12
# Input: https://adventofcode.com/2023/day/12/input
# --- Part One ---

import re
from typing import List


def count_arrangements(
    springs: str,
    groups: List[int],
    springs_index=0,
    cur_group_size=0,  # If cur_group_size == 0, it means that it is not in the damager group.
    next_group_index=0,
):
    if springs_index == len(springs):
        return 1 if cur_group_size <= 1 and next_group_index == len(groups) else 0

    count = 0

    if springs[springs_index] in ".?":
        if cur_group_size <= 1:
            count += count_arrangements(
                springs, groups, springs_index + 1, -1, next_group_index
            )

    if springs[springs_index] in "#?":
        if cur_group_size > 1:
            count += count_arrangements(
                springs, groups, springs_index + 1, cur_group_size - 1, next_group_index
            )
        elif cur_group_size < 1 and next_group_index < len(groups):
            count += count_arrangements(
                springs,
                groups,
                springs_index + 1,
                groups[next_group_index],
                next_group_index + 1,
            )

    return count


result = 0
with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        match = re.match(r"(?P<springs>[?#.]*) (?P<groups>[\d,]*)", line)
        assert match is not None
        match_dict = match.groupdict()
        springs = match_dict.get("springs", "")
        groups = [int(i) for i in match_dict.get("groups", "").split(",")]
        result += count_arrangements(springs, groups)

print(result)
