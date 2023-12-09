from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = nums[0]
        dp = {nums[0] % k: 0}
        for i in range(1, len(nums)):
            sum += nums[i]
            j = sum % k
            if j == 0:
                return True
            if j in dp.keys():
                if i - dp[j] > 1:
                    return True
            else:
                dp[j] = i
        return False
