# Puzzle: https://adventofcode.com/2023/day/19
# Input: https://adventofcode.com/2023/day/19/input
# --- Part One ---

import re

result = 0
parts = []
workflows = {}
with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        if m := re.match(
            r"\{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)\}", line
        ):
            parts.append(
                {
                    rating: int(m.groupdict().get(rating, 0))
                    for rating in ["x", "m", "a", "s"]
                }
            )
        elif line := line.strip():
            splitted = line.split("{")
            workflow_name = splitted[0]
            rules = [
                rule_and_next.split(":")
                for rule_and_next in splitted[1][:-1].split(",")
            ]
            workflows[workflow_name] = rules

for part in parts:
    workflow_name = "in"
    while True:
        for rule, next in workflows[workflow_name][:-1]:
            for rating in ["x", "m", "a", "s"]:
                rule = rule.replace(rating, str(part[rating]))
            if eval(rule):
                workflow_name = next
                break
        else:
            workflow_name = workflows[workflow_name][-1][0]
        if workflow_name == "R":
            break
        elif workflow_name == "A":
            result += sum(part.values())
            break

print(result)
