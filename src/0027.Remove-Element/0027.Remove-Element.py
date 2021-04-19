from typing import List


class Solution:
    '''
    双指针
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        point = 0
        for num in nums:
            if num != val:
                nums[point] = num
                point += 1
        return point
