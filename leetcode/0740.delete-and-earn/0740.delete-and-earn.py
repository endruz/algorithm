from typing import List

"""
由示例 2 可知，当数组中有 m 个值为 n 的元素时，通过重复操作值为 n 的元素。最多可获取 mn 的点数。
通过字典存储操作某个值可获取的最大点数，key 为值，value 为最大点数。
再对 key 进行排序，之后进行动态规划，可参考 0213. 打家劫舍 II
"""


class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = dict()
        for n in nums:
            dic[n] = dic.get(n, 0) + n
        nums = sorted(dic.keys())
        length = len(nums)
        if length == 1:
            return dic[nums[0]]
        max_list = [0] * length
        max_list[0] = dic[nums[0]]
        if nums[0] + 1 == nums[1]:
            max_list[1] = max(dic[nums[0]], dic[nums[1]])
        else:
            max_list[1] = dic[nums[0]] + dic[nums[1]]

        for i in range(2, length):
            if nums[i - 1] + 1 == nums[i]:
                max_list[i] = max(max_list[i - 1], max_list[i - 2] + dic[nums[i]])
            else:
                max_list[i] = max_list[i - 1] + dic[nums[i]]
        return max_list[-1]


class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = dict()
        for n in nums:
            dic[n] = dic.get(n, 0) + n
        nums = sorted(dic.keys())
        length = len(nums)
        if length == 1:
            return dic[nums[0]]
        pre, cur = 0, dic[nums[0]]
        for i in range(1, length):
            if nums[i - 1] + 1 == nums[i]:
                pre, cur = cur, max(cur, pre + dic[nums[i]])
            else:
                pre, cur = cur, cur + dic[nums[i]]
        return cur
