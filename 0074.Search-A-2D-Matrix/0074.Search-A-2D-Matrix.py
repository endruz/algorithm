class Solution1:
    '''
    遍历查找
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False


class Solution2:
    '''
    先定位所在行，再二分查找
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if target > matrix[i][n-1]:
                continue
            left, right = 0, n - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            break
        return False


class Solution3:
    '''
    两次二分查找
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 第一次二分查找，定位所在行
        low, high = -1, m - 1
        while low < high:
            # print(low, high)
            mid = (high - low + 1) // 2 + low
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                low = mid
            else:
                high = mid - 1
        # print(low)
        # 第二次二分查找，查找具体位置
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if target == matrix[low][mid]:
                return True
            elif target < matrix[low][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

class Solution4:
    '''
    两次二分查找（内置函数）
    bisect_right 返回的是在特定值插入有序列表索引的位置，若有相同值则插入该值右侧
    bisect_left 返回的是在特定值插入有序列表索引的位置，若有相同值则插入该值左侧
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from bisect import bisect_right, bisect_left
        m, n = len(matrix), len(matrix[0])
        # 定位所在行
        target_row = bisect_right([row[0] for row in matrix], target) - 1
        # 查找具体位置
        if target_row < 0:
            return False
        target_col = bisect_left(matrix[target_row], target)
        if target_col >= n:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False

class Solution5:
    '''
    全局二分查找
    根据 mid 求出在二维矩阵中的具体位置，然后判断 left 和 right 的移动方式。
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n * m -1
        while left <= right:
            mid = (right - left) // 2 + left
            curr = matrix[mid // n][mid % n]
            if target == curr:
                return True
            elif target < curr:
                right = mid - 1
            else:
                left = mid + 1
        return False