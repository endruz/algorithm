from types import List
from collections import Counter


class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums, n = sorted(nums), len(nums)
        miss, repeat, step = n, 0, 1
        for i in range(n):
            if i and nums[i] == nums[i - 1]:
                repeat = nums[i]
                step = 0
                continue
            if miss == n and nums[i] != i + step:
                miss = i + step
        return [repeat, miss]


class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap, miss, repeat = Counter(nums), 0, 0
        for i in range(1, len(nums) + 1):
            count = hashmap.get(i, 0)
            if count == 1:
                continue
            elif count == 0:
                miss = i
            elif count == 2:
                repeat = i
        return [repeat, miss]
