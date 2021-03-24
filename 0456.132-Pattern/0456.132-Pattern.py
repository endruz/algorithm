class Solution1:
    '''
    暴力破解
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        numsi = nums[0]
        for j in range(1, length):
            if numsi >= nums[j]:
                numsi = nums[j]
                continue
            for k in range(j+1, length):
                if numsi < nums[k] < nums[j]:
                    return True
            numsi = min(numsi, nums[j])
        return False

class Solution2:
    '''
    单调栈
    倒序遍历 nums
    stack 为单调递减栈，每次遇到较大的值时，最后一个出栈的值为 numsk，入栈的值为 numsj。
    numsk 为遍历过的数中小于 numsj 的最大的一个。
    栈顶存储的是 numsj
    变量 numsk 存储 numsk
    当前遍历的数为 numsi
    因为 numsj > numsk 永远成立，所以当且仅当 numsi < numsk 时返回 True
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        stack = list()
        # 模拟一个最小的数
        numsk = - (10 ** 9 + 1)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < numsk:
                return True
            while stack and stack[-1] < nums[i]:
                numsk = stack.pop()
            stack.append(nums[i])
        return False
