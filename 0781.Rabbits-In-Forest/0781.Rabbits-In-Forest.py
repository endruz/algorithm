from typing import List


class Solution1:
    '''
    统计每个数字出现的次数
    当一个兔子还有 x 个其他的兔子和自己有相同的颜色时，说明该花色的兔子一共有 x+1 个。
    当有 v(v > x+1) 个兔子回答了 x，则说明有多种花色的兔子数量是 x。
    因为是计算兔子的最小数量，我们可以把数量为 x 的兔子种数估算为 v / (k + 1) 向上取整。
    '''
    def numRabbits(self, answers: List[int]) -> int:
        from math import ceil
        count = dict()
        result = 0
        for i in answers:
            count[i] = count.setdefault(i, 0) + 1
        for k, v in count.items():
            result += ceil(v / (k + 1)) * (k + 1)
        return result


class Solution2:
    '''
    方法一的优化
    使用内置函数 collections.Counter 来统计每个数字出现的次数
    ceil(v / (k + 1)) 可以等价转换为 (v + k) // (k + 1)
    '''
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        result = 0
        count = Counter(answers)
        for k, v in count.items():
            result += (v + k) // (k + 1) * (k + 1)
        return result
