# https://adventofcode.com/2023/day/1
# --- Part Two ---

import re

result = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_map = {string: str(index + 1) for index, string in enumerate(digits)}
digit_pattern = "|".join(digits + ["[1-9]"])


def get_digit(pattern: str, string: str) -> str:
    digit_match = re.match(pattern, string)
    assert digit_match is not None
    digit = digit_match.groups()[0]
    return digit_map.get(digit, digit)


with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        first_digit = get_digit(rf"^.*?({digit_pattern}).*", line)
        last_digit = get_digit(rf".*({digit_pattern}).*?$", line)
        result += int(f"{first_digit}{last_digit}")
print(result)
