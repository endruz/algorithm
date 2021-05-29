from typing import List


class Solution1:
    """
    暴力解法，超时
    """
    def totalHammingDistance(self, nums: List[int]) -> int:
        def hammingDistance(x: int, y: int) -> int:
            z = x ^ y
            count = 0
            for i in range(31):
                if z & 1:
                    count += 1
                z = z >> 1
            return count
        n, result = len(nums), 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                result += hammingDistance(nums[i], nums[j])
        return result


class Solution2:
    """
    因为 0 <= nums[i] <= 10^9 且 10^9 < 2^30，所以 nums[i] < 2^30 所有元素都可以转换为 30 位二进制。
    通过 (num >> i) & 1 获取元素第 i 位的值，第 i 位为 1 的元素有 c 个，为 0 的元素有 n - c 个。
    则第 i 位的汉明距离和为 c * (n - c)。
    从低到高依次求出所有位的汉明距离和相加。
    """
    def totalHammingDistance(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        for i in range(30):
            c = sum([(num >> i) & 1 for num in nums])
            result += c * (n - c)
        return result
