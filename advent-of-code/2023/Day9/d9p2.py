# Puzzle: https://adventofcode.com/2023/day/9
# Input: https://adventofcode.com/2023/day/9/input
# --- Part Two ---

result = 0


def get_previous_value(nums: list[int]):
    nums_list = [nums]
    while not all([num == 0 for num in nums_list[-1]]):
        current_list = nums_list[-1]
        tmp_list = []
        for i in range(1, len(current_list)):
            tmp_list.append(current_list[i] - current_list[i - 1])
        nums_list.append(tmp_list)

    previous_value = 0
    for i in range(len(nums_list) - 2, -1, -1):
        previous_value = nums_list[i][0] - previous_value
    return previous_value


with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        nums = [int(num) for num in line.strip().split()]
        previous_value = get_previous_value(nums)
        result += previous_value

print(result)
