from types import List


class Solution1:
    """
    超时
    """
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        result = dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i]
            result = max(result, dp[i])
            for j in range(i):
                result = max(result, dp[i] - dp[j])
        return result


class Solution2:
    """
    动态规划
    """
    def maxSubArray(self, nums: List[int]) -> int:
        pre, result = 0, nums[0]
        for num in nums:
            pre = max(pre + num, num)
            result = max(result, pre)
        return result
