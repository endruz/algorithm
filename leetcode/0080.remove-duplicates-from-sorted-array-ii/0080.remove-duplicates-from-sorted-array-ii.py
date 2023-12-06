from typing import List


class Solution1:
    '''
    第一想法，不符合题意
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        index = count = 1
        length = len(nums)
        while index < length:
            if nums[index] == nums[index - 1]:
                if count < 2:
                    count += 1
                    index += 1
                else:
                    del nums[index]
                    length -= 1
            else:
                count = 1
                index += 1
        return length


class Solution2:
    '''
    双指针
    当列表长度小于等于 2 时，一定符合条件，可直接返回。
    当列表长度大于 2 时，
    慢指针 slow : 指向当前即将放置元素的位置；则 slow - 1 是刚才已经放置了元素的位置。
    快指针 fast : 向后遍历所有元素。
    当 nums[fast] == nums[slow - 2] 时，即当前遍历的元素和上上次放置的元素相同。
    因为是一个有序数组且每个元素最多出现两次，则说明 fast 指向的元素至少是第三次出现，不进行放置。
    当不等于时，放置元素并移动慢指针 slow
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length
        else:
            slow = 2
            for fast in range(2, length):
                if nums[fast] != nums[slow - 2]:
                    nums[slow] = nums[fast]
                    slow += 1
            return slow
