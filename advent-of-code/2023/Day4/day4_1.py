# https://adventofcode.com/2023/day/4
# --- Part One ---

import math

result = 0
with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        splitted = line.strip().split(":")
        splitted = splitted[-1].strip().split("|")
        winning_numbers = splitted[0].strip().split()
        numbers_we_have = splitted[1].strip().split()
        match_times = 0
        for number in numbers_we_have:
            if number in winning_numbers:
                match_times += 1
        point = 0 if match_times == 0 else int(math.pow(2, match_times - 1))
        result += point

print(result)
