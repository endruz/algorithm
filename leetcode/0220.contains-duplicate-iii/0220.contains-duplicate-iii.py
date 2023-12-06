from typing import List


class Solution1:
    '''
    暴力解法-超时
    '''
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        length = len(nums)
        for i in range(length - 1):
            end = length if length < i + k + 1 else i + k + 1
            for j in range(i + 1, end):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False


class Solution2:
    '''
    桶排序
    '''
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getID(value):
            if value >= 0:
                return value // (t + 1)
            else:
                return (value + 1) // (t + 1) - 1
        barrel = dict()
        for i in range(len(nums)):
            index = getID(nums[i])
            if index in barrel.keys():
                return True
            if (index + 1) in barrel.keys() and abs(nums[i] - barrel[index + 1]) <= t:
                return True
            if (index - 1) in barrel.keys() and abs(nums[i] - barrel[index - 1]) <= t:
                return True
            barrel[index] = nums[i]
            if i >= k:
                barrel.pop(getID(nums[i - k]))
        return False
