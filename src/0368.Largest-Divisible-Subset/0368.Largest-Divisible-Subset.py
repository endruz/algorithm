from typing import List


class Solution:
    """
    由于存在「整除子集」中任意两个值必然存在倍数/约数关系的性质，我们自然会想到对 nums 进行排序，
    然后从集合 nums 中从大到小进行取数，每次取数只考虑当前决策的数是否与「整除子集」中的最后一个数成倍数关系即可。
    """
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        # 列表 f 中 f[i] 为以 nums[i] 为结尾的最长「整除子集」长度。
        # 列表 g 中 g[i] 为以 nums[i] 为结尾的最长「整除子集」的 nums[i] 是由哪个下标转移而来，满足 f[i] = f[g[i]] + 1
        f, g = [0] * n, [0] * n

        for i in range(n):
            # 至少包含自身一个数，因此起始长度为 1，由自身转移而来
            length, pre = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    # 如果能接在更长的序列后面，则更新「最大长度」&「从何转移而来」
                    if f[j] + 1 > length:
                        length += 1
                        pre = j
            # 记录「最终长度」&「从何转移而来」
            f[i] = length
            g[i] = pre

        # 遍历所有的 f[i]，取得「最大长度」和「对应下标」
        max_len = index = -1
        for i in range(n):
            if f[i] > max_len:
                max_len = f[i]
                index = i

        # 使用 g[] 数组回溯出具体方案
        result = list()
        for _ in range(max_len):
            result.append(nums[index])
            index = g[index]
        result.reverse()
        return result
