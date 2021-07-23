from types import List
from collections import defaultdict


class Solution:
    """
    用差分数组 diff 维护相邻两个整数的被覆盖区间数量变化量
    其中 diff[i] 对应覆盖整数 i 的区间数量相对于覆盖 i - 1 的区间数量变化量。
    这样，当遍历到闭区间 [l, r] 时，l 相对于 l - 1 被覆盖区间数量多 1，r + 1 相对于 r 被覆盖区间数量少 1。
    对应到差分数组上，我们需要将 diff[l] 加上 1，并将 diff[r+1] 减去 1。

    在维护完差分数组 diff 后，我们遍历 diff 求前缀和得出覆盖每个整数的区间数量。
    下标 i 对应的被覆盖区间数量即为初始数量 0 加上 [1,i] 闭区间的变化量之和。
    在计算被覆盖区间数量的同时，我们可以一并判断 [left, right] 闭区间内的所有整数是否都被覆盖。
    """
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = defaultdict(int)
        for le, ri in ranges:
            diff[le] += 1
            diff[ri + 1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True
