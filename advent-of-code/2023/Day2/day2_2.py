# https://adventofcode.com/2023/day/2
# --- Part Two ---

result = 0
with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        splitted = line.strip().split(":")
        max_red = max_green = max_blue = 0
        for round in splitted[-1].split(";"):
            for cube in round.strip().split(","):
                if cube.endswith("blue"):
                    blue_num = int(cube.strip().rstrip(" blue"))
                    if blue_num > max_blue:
                        max_blue = blue_num
                if cube.endswith("green"):
                    green_num = int(cube.strip().rstrip(" green"))
                    if green_num > max_green:
                        max_green = green_num
                if cube.endswith("red"):
                    red_num = int(cube.strip().rstrip(" red"))
                    if red_num > max_red:
                        max_red = red_num
        result += max_red * max_green * max_blue

print(result)
