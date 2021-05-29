from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        value = 1
        left, right, top, bottom = 0, n-1, 0, n-1
        while value <= n**2:
            for i in range(left, right+1):
                matrix[top][i] = value
                value += 1
            for j in range(top+1, bottom+1):
                matrix[j][right] = value
                value += 1
            for i in range(right-1, left-1, -1):
                matrix[bottom][i] = value
                value += 1
            for j in range(bottom-1, top, -1):
                matrix[j][left] = value
                value += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix
