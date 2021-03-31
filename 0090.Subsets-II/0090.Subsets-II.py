from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        length = len(nums)

        def dfs(index, path):
            res.append(path)
            for i in range(index, length):
                if i > index and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return res
