from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = matrix[0]
        operator = -1
        del matrix[0]

        def fun(matrix, operator):
            length = len(matrix)
            if operator == -1:
                start = 0
                stop = length
                step = 1
            else:
                start = length - 1
                stop = -1
                step = -1
            for i in range(start, stop, step):
                result.append(matrix[i].pop(operator))
            while matrix[operator]:
                result.append(matrix[operator].pop(operator))
            for index in range(length-1, -1, -1):
                if not matrix[index]:
                    del matrix[index]

        while matrix:
            fun(matrix, operator)
            operator = -1 if operator == 0 else 0

        return result
