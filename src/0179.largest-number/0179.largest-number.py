from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
        if nums[0] == "0":
            return nums[0]
        else:
            return "".join(nums)
