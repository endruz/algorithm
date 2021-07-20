from types import List


class Solution1:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        sums = [0 for _ in range(n)]
        for i in range(n):
            sums[i] = nums[i] + nums[-(i + 1)]
        return max(sums)


class Solution2:
    """
    Solution1 优化
    """
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        result = 0
        for i in range(n):
            result = max(result, nums[i] + nums[-(i + 1)])
        return result
