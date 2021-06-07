from typing import List
from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(index: int, target: int) -> int:
            if index == n:
                return 1 if target == 0 else 0
            return dfs(index + 1, target - nums[index]) + dfs(index + 1, target + nums[index])

        return dfs(0, target)
