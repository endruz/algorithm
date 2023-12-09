from typing import List

"""
将二维数组化为一维数组，将问题转化为 560.和为K的子数组
"""


class Solution1:
    """
    枚举，超时
    """
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n, count = len(matrix[0]), len(matrix), 0

        def _func(submatrix: List[int], target: int) -> int:
            count = 0
            for i in range(1, m + 1):
                for j in range(m - i + 1):
                    if sum(submatrix[j: j + i]) == target:
                        count += 1
            return count

        for y1 in range(0, n):
            submatrix = [0 for _ in range(m)]
            for y2 in range(y1, n):
                for colume in range(m):
                    submatrix[colume] += matrix[y2][colume]
                count += _func(submatrix, target)
        return count


class Solution2:
    """
    前缀和 + 哈希表优化
    """
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n, count = len(matrix[0]), len(matrix), 0

        def _func(submatrix: List[int], target: int) -> int:
            count, pre = 0, 0
            hashmap = {0: 1}
            for num in submatrix:
                pre += num
                if pre - target in hashmap.keys():
                    count += hashmap[pre - target]
                hashmap[pre] = hashmap.get(pre, 0) + 1
            return count

        for y1 in range(0, n):
            submatrix = [0 for _ in range(m)]
            for y2 in range(y1, n):
                for colume in range(m):
                    submatrix[colume] += matrix[y2][colume]
                count += _func(submatrix, target)
        return count
