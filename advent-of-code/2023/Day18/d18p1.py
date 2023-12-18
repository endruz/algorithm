# Puzzle: https://adventofcode.com/2023/day/18
# Input: https://adventofcode.com/2023/day/18/input
# --- Part One ---

import numpy as np
import cv2

perimeter = 0
points = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        assert len(splitted := line.strip().split(" ")) == 3
        step_length = int(splitted[1])
        dr, dc = dirs[splitted[0]]
        perimeter += step_length
        row, col = points[-1]
        points.append((row + dr * step_length, col + dc * step_length))

points_array = np.array(points)
area = cv2.contourArea(points_array)
area = area + perimeter // 2 + 1
print(area)
