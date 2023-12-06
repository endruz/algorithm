from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, result = len(points), 1

        def pointNum(i: List[int], j: List[int]) -> int:
            count = 0
            if i[0] - j[0] == 0:
                for p in points:
                    if p[0] == i[0]:
                        count += 1
            elif i[1] - j[1] == 0:
                for p in points:
                    if p[1] == i[1]:
                        count += 1
            else:
                # k = (i[1] - j[1])/(i[0] - j[0])
                # (i[1] - p[1]) == k * (i[0] - p[0])
                #    |
                #    V
                # (i[1] - p[1]) == (i[1] - j[1])/(i[0] - j[0]) * (i[0] - p[0])
                #    |
                #    V
                # (i[1] - p[1]) * (i[0] - j[0]) == (i[1] - j[1]) * (i[0] - p[0])
                for p in points:
                    if (i[1] - p[1]) * (i[0] - j[0]) == (i[1] - j[1]) * (i[0] - p[0]):
                        count += 1
            return count

        def dfs(i: str) -> None:
            nonlocal result
            if i == n - 1:
                return
            for j in range(i + 1, n):
                result = max(result, pointNum(points[i], points[j]))
            dfs(i + 1)

        dfs(0)
        return result
