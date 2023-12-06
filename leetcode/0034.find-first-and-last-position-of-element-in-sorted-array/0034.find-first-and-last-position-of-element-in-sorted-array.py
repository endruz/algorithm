from types import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        # indexl
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        indexl = left
        # indexr
        left, right = 0, n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[right] != target:
            return [-1, -1]
        indexr = right
        return [indexl, indexr]
