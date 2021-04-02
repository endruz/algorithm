from typing import List


class Solution1:
    '''
    暴力破解
    根据直方图，我们可以得出每列可存的水量为 "左边最高一列" 和 "右边最高一列" 中的最小值 减去 该列的高度
    以此来进行暴力破解
    '''
    def trap(self, height: List[int]) -> int:
        length = len(height)
        result = 0
        for i in range(1, length - 1):
            left_height = max(height[:i])
            right_height = max(height[i: length])
            h = min(left_height, right_height) - height[i]
            if h > 0:
                result += h
        return result


class Solution2:
    '''
    动态规划
    暴力破解中计算每列 "左边最高一列" 和 "右边最高一列" 的方法存在多次重复计算。
    使用两个列表分别通过一次循环来记录每个位置左边和右边的最大高度
    之后的思路就和暴力破解一样了
    '''
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_highest_list = [0] * length
        right_highest_list = [0] * length

        for i in range(1, length):
            left_highest_list[i] = max(left_highest_list[i-1], height[i-1])

        for i in range(length-2, -1, -1):
            right_highest_list[i] = max(right_highest_list[i+1], height[i+1])

        result = 0
        for i in range(1, length - 1):
            h = min(left_highest_list[i], right_highest_list[i]) - height[i]
            if h > 0:
                result += h
        return result


class Solution3:
    '''
    双指针
    left, right 是分别指向左右两个端点的柱子的指针
    left_highest, right_highest 分别表示左右两个指针遇到过的最高的柱子的高度
    比较 left_highest, right_highest 中更小的那一个和对应那一侧指针所指的高度
    若为负则更新最高值，若为正则可获取指针所指那一列的蓄水量
    每次把更小的那一侧指针向中间移动
    '''
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left, right = 0, length - 1
        left_highest, right_highest = 0, 0
        result = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] < left_highest:
                    result += left_highest - height[left]
                else:
                    left_highest = height[left]
                left += 1
            else:
                if height[right] < right_highest:
                    result += right_highest - height[right]
                else:
                    right_highest = height[right]
                right -= 1
        return result
