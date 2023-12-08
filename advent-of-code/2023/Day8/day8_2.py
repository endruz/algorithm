# https://adventofcode.com/2023/day/8
# --- Part Two ---

import re
import math

maps: dict[str, tuple[str, str]] = {}

with open("./puzzle_input.txt", "r") as f:
    instructions = f.readline().strip()
    f.readline()
    for line in f.readlines():
        pattern = r"^(?P<node>[A-Z]{3}) = \((?P<L>[A-Z]{3}), (?P<R>[A-Z]{3})\)"
        m = re.match(pattern, line)
        assert m is not None
        maps[m.groupdict()["node"]] = (m.groupdict()["L"], m.groupdict()["R"])


def get_step_count(node: str):
    step = 0
    flag = True

    while flag:
        for instruction in instructions:
            i = 0 if instruction == "L" else 1
            node = maps[node][i]
            step += 1
            if node.endswith("Z"):
                flag = False
                break
    return step


step_counts = [get_step_count(node) for node in maps.keys() if node.endswith("A")]

print(math.lcm(*step_counts))
