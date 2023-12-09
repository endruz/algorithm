from typing import List


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        value = nums[-1]
        for i in range(length - 2, -1, -1):
            if nums[i] == value:
                nums.pop(i)
                length -= 1
            else:
                value = nums[i]
        return length


class Solution2:
    '''
    双指针
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fast = slow = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
