# Puzzle: https://adventofcode.com/2023/day/15
# Input: https://adventofcode.com/2023/day/15/input
# --- Part Two ---

from typing import Dict, List, Tuple
from collections import defaultdict


def get_hash(step: str):
    hash_value = 0
    for char in step:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value


boxes: Dict[int, List[Tuple[str, int]]] = defaultdict(list)

with open("./puzzle_input.txt", "r") as f:
    for step in f.readline().strip().split(","):
        if step.endswith("-"):
            label = step[:-1]
            hash_value = get_hash(label)
            for i, pair in enumerate(boxes[hash_value]):
                if pair[0] == label:
                    del boxes[hash_value][i]
                    break
        else:
            label, focal_length = step.split("=")
            hash_value = get_hash(label)
            for i, pair in enumerate(boxes[hash_value]):
                if pair[0] == label:
                    boxes[hash_value][i] = (label, int(focal_length))
                    break
            else:
                boxes[hash_value].append((label, int(focal_length)))

result = 0
for i, pairs in boxes.items():
    for j, pair in enumerate(pairs):
        result += (i + 1) * (j + 1) * pair[-1]

print(result)
