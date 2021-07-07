from types import List
from collections import Counter


class Solution1:
    """
    暴力解法，超时
    """
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n, count = len(deliciousness), 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                m = deliciousness[i] + deliciousness[j]
                # 防止 m == 0 时也判断为 2 的幂
                if m and m & (m - 1) == 0:
                    count += 1
        return count % MOD


class Solution2:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        MOD = 10 ** 9 + 7
        counter = Counter(deliciousness)
        powersOfTwo = [2 ** i for i in range(22)]
        for value in deliciousness:
            for sum in powersOfTwo:
                target = sum - value
                count += counter.get(sum - value, 0)
                if target == value:
                    count -= 1
        return (count // 2) % MOD


class Solution3:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        count, counter = 0, dict()
        powersOfTwo = [2 ** i for i in range(22)]
        for value in deliciousness:
            for sum in powersOfTwo:
                count += counter.get(sum - value, 0)
            counter[value] += 1
        return count % MOD
