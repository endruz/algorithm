from typing import List


class Solution1:
    '''
    暴力解法
    '''
    def search(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == target:
                return True
            else:
                return False


class Solution2:
    '''
    二分法
    设旋转的下标为 k。旋转前 nums 非降序，所以 nums[:k] 内的元素一定大于等于 nums[k:] 内的元素
    left < mid < k < right 时，nums[mid] > nums[right]，nums[left:mid] 有序。
    若 target 在 [left:mid] 中时，继续向左搜索，反之向右搜索。
    left < k < mid < right 时，nums[mid] < nums[right]，nums[mid:right] 有序
    若 target 在 [mid:right] 中时，继续向右搜索，反之向左搜索。
    ---
    因为可以存在重复的数字， 当 nums[left] = nums[mid] = nums[right] 时，会存在问题，无法判断向哪搜索。
    例如 [2,1,2,2,2] 和 [2,2,2,1,2]。
    这时自动将 left 向右移一位，right 向左移一位来避免这种情况。
    '''
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
