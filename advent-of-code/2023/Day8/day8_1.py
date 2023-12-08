# https://adventofcode.com/2023/day/8
# --- Part One ---

import re

maps: dict[str, tuple[str, str]] = {}

with open("./puzzle_input.txt", "r") as f:
    instructions = f.readline().strip()
    f.readline()
    for line in f.readlines():
        pattern = r"^(?P<node>[A-Z]{3}) = \((?P<L>[A-Z]{3}), (?P<R>[A-Z]{3})\)"
        m = re.match(pattern, line)
        assert m is not None
        maps[m.groupdict()["node"]] = (m.groupdict()["L"], m.groupdict()["R"])

step = 0
current_node = "AAA"
flag = True

while flag:
    for instruction in instructions:
        i = 0 if instruction == "L" else 1
        current_node = maps[current_node][i]
        step += 1
        if current_node == "ZZZ":
            flag = False
            break

print(step)
