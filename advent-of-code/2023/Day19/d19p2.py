# Puzzle: https://adventofcode.com/2023/day/19
# Input: https://adventofcode.com/2023/day/19/input
# --- Part Two ---

result = 0
workflows = {}
with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        if line := line.strip():
            splitted = line.split("{")
            workflow_name = splitted[0]
            rules = [
                rule_and_next.split(":")
                for rule_and_next in splitted[1][:-1].split(",")
            ]
            rules[-1].insert(0, "")
            workflows[workflow_name] = rules
        else:
            break

workflow_combinations = []


def get_combinations(combination):
    index, workflow_name = combination[-1]
    for index, value in enumerate(workflows[workflow_name]):
        _, next_workflow = value
        if next_workflow == "R":
            continue
        new_combination = combination + ((index, next_workflow),)
        if next_workflow == "A":
            workflow_combinations.append(new_combination)
            continue
        get_combinations(new_combination)


get_combinations(((-1, "in"),))

combinations = {}
for combination in workflow_combinations:
    rating_dict = {rating: [1, 4000] for rating in ["x", "m", "a", "s"]}
    for i in range(len(combination) - 1):
        _, workflow_name = combination[i]
        index, next_workflow_name = combination[i + 1]

        for j in range(len(workflows[workflow_name]) - 1):
            rule, next_workflow = workflows[workflow_name][j]
            rating, sign, value = rule[0], rule[1], int(rule[2:])
            if j == index:
                if sign == ">":
                    rating_dict[rating][0] = max(rating_dict[rating][0], value + 1)
                elif sign == "<":
                    rating_dict[rating][1] = min(rating_dict[rating][1], value - 1)
                break
            else:
                if sign == ">":
                    rating_dict[rating][1] = min(rating_dict[rating][1], value)
                elif sign == "<":
                    rating_dict[rating][0] = max(rating_dict[rating][0], value)

    combinations[combination] = rating_dict
    print(str(combination).ljust(100, " "), rating_dict)


for combination, rating_dict in combinations.items():
    n = 1
    for mn, mx in rating_dict.values():
        n *= max(0, mx - mn + 1)
    result += n

print(result)
