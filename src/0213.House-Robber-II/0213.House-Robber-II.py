from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_max(nums):
            length = len(nums)
            if length == 1:
                return nums[0]
            max_list = [0] * length
            max_list[0] = nums[0]
            max_list[1] = max(nums[0], nums[1])
            for i in range(2, length):
                max_list[i] = max(max_list[i - 1], max_list[i - 2] + nums[i])
            return max_list[-1]
        length = len(nums)
        if length == 1:
            return nums[0]
        return max(rob_max(nums[0:length-1]), rob_max(nums[1:length]))
