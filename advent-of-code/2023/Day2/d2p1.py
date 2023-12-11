# Puzzle: https://adventofcode.com/2023/day/2
# Input: https://adventofcode.com/2023/day/2/input
# --- Part One ---

result = 0
max_red, max_green, max_blue = 12, 13, 14

with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        splitted = line.strip().split(":")
        game_id = int(splitted[0].lstrip("Game "))
        is_possible = True
        for round in splitted[-1].split(";"):
            if not is_possible:
                break
            for cube in round.strip().split(","):
                if cube.endswith("blue"):
                    blue_num = int(cube.strip().rstrip(" blue"))
                    if blue_num > max_blue:
                        is_possible = False
                        break
                if cube.endswith("green"):
                    green_num = int(cube.strip().rstrip(" green"))
                    if green_num > max_green:
                        is_possible = False
                        break
                if cube.endswith("red"):
                    red_num = int(cube.strip().rstrip(" red"))
                    if red_num > max_red:
                        is_possible = False
                        break
        if is_possible:
            result += game_id

print(result)
