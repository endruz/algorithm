from typing import List


class Solution_1:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        暴力解法
        '''
        length = len(nums)
        result = [-1] * length
        for i in range(length):
            for value in nums[i+1:] + nums[:i]:
                if nums[i] < value:
                    result[i] = value
                    break
        return result


class Solution_2:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        单调栈 + 循环数组
        '''
        length = len(nums)
        result = [-1] * length
        stack = []
        # 因为是循环数组（最后一个元素的下一个元素是数组的第一个元素）
        # 相当于循环了两遍数组(最后一个元素只循环一次)，这里用下标模拟
        for i in range(2 * length - 1):
            # 这里 j 为数组实际循环到的下标
            index = i % length
            # 栈中存储的是循环过的下标
            # 一旦栈尾下标的值比当前下标的值小，则说明当前下标的值是第一个比栈尾下标的值更大的数
            # 这时候出栈，并将值填入结果列表中
            # 继续判断，直到栈尾下标的值比当前下标的值大。这说明之前下标的值都比当前值大
            while stack and nums[stack[-1]] < nums[index]:
                result[stack.pop()] = nums[index]
            # 当前下标入栈
            stack.append(index)
        return result
