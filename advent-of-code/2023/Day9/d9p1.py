# https://adventofcode.com/2023/day/9
# --- Part One ---

result = 0
def get_next_value(nums: list[int]):
    nums_list = [nums]
    while not all([num == 0 for num in nums_list[-1]]):
        current_list = nums_list[-1]
        tmp_list = []
        for i in range(1, len(current_list)):
            tmp_list.append(current_list[i] - current_list[i - 1])
        nums_list.append(tmp_list)

    next_value = 0
    for i in range(len(nums_list) - 2, -1, -1):
        next_value += nums_list[i][-1]
    return next_value


with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        nums = [int(num) for num in line.strip().split()]
        next_value = get_next_value(nums)
        result += next_value

print(result)

