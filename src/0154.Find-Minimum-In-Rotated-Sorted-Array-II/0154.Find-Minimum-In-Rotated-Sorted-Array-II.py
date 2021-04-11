from typing import List


class Solution:
    '''
    二分法
    思路同 0153
    '''
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1
        return nums[right]
