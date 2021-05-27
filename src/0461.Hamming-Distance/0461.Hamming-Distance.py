class Solution:
    """
    先计算 x ^ y，然后统计结果中等于 1 的位数
    """
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0
        for i in range(31):
            if z & 1:
                count += 1
            z = z >> 1
        return count
