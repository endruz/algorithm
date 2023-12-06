# https://adventofcode.com/2023/day/6
# --- Part Two ---

import math
import numpy as np

with open("./puzzle_input.txt", "r") as f:
    time = int(f.readline().lstrip("Time:").replace(" ", "").strip())
    distance = int(f.readline().lstrip("Distance:").replace(" ", "").strip())

a, b = np.roots([1, -time, distance])
t1 = math.ceil(min(a, b))
t2 = math.floor(max(a, b))
ways = t2 - t1 + 1
print(ways)
