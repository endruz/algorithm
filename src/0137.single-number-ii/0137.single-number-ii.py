from typing import List
from collections import Counter


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length, num, time = len(nums), -2 ** 31 - 1, 0
        for i in range(length):
            if nums[i] == num:
                time += 1
            elif time == 1:
                return num
            else:
                num, time = nums[i], 1
            if time == 1 and i == length - 1:
                return num


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        index, nums = 0, sorted(nums)
        while index < len(nums) - 2:
            if nums[index] == nums[index + 2]:
                index += 3
            else:
                return nums[index]
        else:
            return nums[index]


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k in counter.keys():
            if counter[k] == 1:
                return k
