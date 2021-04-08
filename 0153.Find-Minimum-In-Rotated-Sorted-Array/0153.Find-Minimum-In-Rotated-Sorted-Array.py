from typing import List


class Solution:
    '''
    二分法
    当 nums[0] <= nums[-1] 时，则说明旋转过后的和旋转前数组一样，都是升序排序，则直接返回 nums[0]。否则使用二分法查找。
    nums[mid] < nums[right] 时，说明 [mid:right] 升序，最小值在 [left:mid] 区间，继续查找。
    反之 nums[mid] > nums[right] 时，说明 [left:mid] 升序，最小值在 [mid:right] 区间，继续查找。
    当 left 和 right 相邻时，则最小值一定是 nums[right]
    '''
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        else:
            left, right = 0, len(nums) - 1
            while left < right:
                if left + 1 == right:
                    break
                mid = (left + right) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid
            return nums[right]
