class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(lens-1):
            for j in range(i+1,lens):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            j = target - nums[i]
            if j in nums[:i]:
                return [nums.index(j), i]
        return []

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, value in enumerate(nums):
            if hashmap.get(target - value, -1) >= 0:
                return [hashmap.get(target - value, -1), index]
            else:
                hashmap.setdefault(value, index)
        return []
